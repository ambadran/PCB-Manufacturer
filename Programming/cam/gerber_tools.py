'''
This files contains functions to parse gerber files and deal with them
'''
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class BlockType(Enum):
    Conductor = 'Conductor'
    ComponentPad = 'ComponentPad'
    Profile = 'Profile'

class ShapeType(Enum):
    Circle = 'C'
    Rectangle = 'R'
    Oval = 'O'

@dataclass
class Coordinate:
    x: int | float
    y: int | float
    z: Optional[int | float] = None

    def __getitem__(self, index) -> float:
        '''
        Enable slicing of coordinate objects
        '''
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Only X, Y, Z values available")

    def __len__(self) -> int:
        '''
        return whether it's x,y or x,y,z
        '''
        if self.z is None:
            return 2
        else:
            return 3

    @classmethod
    def get_min_max(cls, coordinates_list: list[Coordinate]) -> tuple[Coordinate, Coordinate]:
        '''
        finds the Min, Max of X and Y coordinates from input list of coordinates

        :param coordinates: list of coordinates [(x, y), ..]
        :return: ((x_min, y_min), (x_max, y_max))
        '''

        x_min, y_min = coordinates_list[0].x, coordinates_list[0].y
        x_max, y_max = x_min, y_min

        for coordinate in coordinates_list:

            new_x, new_y = coordinate.x, coordinate.y

            if new_x < x_min:
                x_min = new_x

            elif new_x > x_max:
                x_max = new_x

            if new_y < y_min:
                y_min = new_y

            elif new_y > y_max:
                y_max = new_y

        return Coordinate(x_min, y_min), Coordinate(x_max, y_max)
            

class Block:
    '''
    Gerber Block of coordinates
    each block is named like this 'Dxx' where xx is the number that identifies this block
    each block has a group type which determines whether it is drill coordinate, trace coordinate or edge coordinates
    each block has a thickness assigned to it
    each block has it's own set of coordinates
    '''
    def __init__(self, D_num: int, coordinates: list[Coordinate], block_type: BlockType, shape_type: ShapeType, 
                    thickness: float, thickness2: Optional[float]=None, 
                    coordinates_with_multiplier: Optional[list[Coordinate]]=None):
        self.D_num = D_num
        self.coordinates = coordinates
        self.block_type = block_type
        self.shape_type = shape_type
        self.thickness = thickness
        self.thickness2 = thickness2
        self.coordinates_with_multiplier = coordinates_with_multiplier



    @classmethod
    def from_gerber(cls, gerber_object: Gerber, block_type: BlockType) -> list[Block]:
        '''
        :param gerber_file: gerber file in string form
        :param block_type: what block type wanted to be extracted from the gerber file

        :returns: a list of ALL Block objects of a specific BlockType found in a gerber file 
        '''
        gerber_file = gerber_object.gerber_file
        g_file_lines = gerber_file.split('\n')

        d_nums: list[ind] = []
        coordinates: dict[int: list[Coordinate]] = {}  # key is index and value is value
        coordinates_with_multiplier: dict[int: list[Coordinate]] = {}  # key is index and value is value
        shape_types: list[ShapeType] = []
        thicknesses: list[float] = []
        thicknesses2: list[float] = []
        # getting the Dxx of the block we want and shape types
        to_ShapeType = {shape_type.value: shape_type for shape_type in ShapeType}
        for line_num, line in enumerate(g_file_lines):
            if block_type.value in line:
                wanted_line = g_file_lines[line_num+1]

                # getting the D number of the profile definition, by finding the last char that is a digit
                start_wanted_index = wanted_line.find('%ADD') + 4
                for char_num, char in enumerate(wanted_line[start_wanted_index:]):
                    if not char.isdigit():
                        end_wanted_index = 4 + char_num
                        break
                d_nums.append(wanted_line[start_wanted_index:end_wanted_index])
                coordinates[d_nums[-1]] = []
                coordinates_with_multiplier[d_nums[-1]] = []
                shape_types.append(to_ShapeType[wanted_line[end_wanted_index]])

                if shape_types[-1] == ShapeType.Rectangle or shape_types[-1] == ShapeType.Oval: 
                    # two thickness values; length and width
                    thickness, thickness2 = wanted_line[end_wanted_index+2:wanted_line.index('*')].split('X')
                    thicknesses.append(float(thickness))
                    thicknesses2.append(float(thickness2))

                elif shape_types[-1] == ShapeType.Circle:
                    # one thickness value
                    thicknesses.append(float(wanted_line[end_wanted_index+2:wanted_line.index('*')]))
                    thicknesses2.append(None)


        # getting all the gerber coordinates under the wanted Dxx
        take_lines = False
        g_file_lines_start_ind = gerber_file[:gerber_file.find('D')].count('\n')  # coordinates start from first 'D' occurance
        for line_num, line in enumerate(g_file_lines[g_file_lines_start_ind:]):

            #TODO: ASSUMPTION!! Here I am assuming start of a block always looks like this 'Dxyz', where x is int, y int or nothing and z is any character
            if line.startswith('D'):  # decide on whether to take lines or not
                current_dnum = line[1:-1]
                take_lines = current_dnum in d_nums
                continue

            if take_lines:
                coordinate = Gerber.get_XY(line)
                if coordinate is not None:
                    coordinates_with_multiplier[current_dnum].append(coordinate)
                    coordinate.x /= gerber_object.x_multiplier
                    coordinate.y /= gerber_object.y_multiplier
                    coordinates[current_dnum].append(coordinate)

        debug = False
        if debug:
            print(len(d_nums))
            print(len(shape_types))
            print(len(thicknesses))
            print(len(coordinates))
            print(len(coordinates_with_multiplier))
            print(len(thicknesses2))
            print()

            print(d_nums)
            print(shape_types)
            print(thicknesses)
            print(coordinates)
            print(coordinates_with_multiplier)
            print(thicknesses2)
            print()

        blocks = []
        for ind in range(len(d_nums)):
            blocks.append(Block(d_nums[ind], coordinates[d_nums[ind]], block_type, shape_types[ind], 
                            thicknesses[ind], thicknesses2[ind], 
                            coordinates_with_multiplier[d_nums[ind]]))

        return blocks

    def __str__(self):
        thickness2_str =  "" if self.thickness2 is None else f"x{self.thickness2}"
        return f"D{self.D_num} of shape {self.shape_type}, thickness {self.thickness}{thickness2_str} and {len(self.coordinates)} coordinates"


class Gerber:
    '''
    Class to implement basic functionlity to read, manipulate and write gerber files
    '''
    def __init__(self, file_path: str):
        self.gerber_file = self.read_gerber_file(file_path)
        self.x_multiplier, self.y_multiplier = self.get_x_y_multiplier()

        self.blocks: dict[BlockType: list[Block]] = {

                        BlockType.Profile: Block.from_gerber(self, BlockType.Profile), 

                        BlockType.Conductor: Block.from_gerber(self, BlockType.Conductor),

                        BlockType.ComponentPad: Block.from_gerber(self, BlockType.ComponentPad)
                }

        self.coordinates: dict[BlockType: list[Coordinate]] = {

            BlockType.Profile:
                [coordinate for block in self.blocks[BlockType.Profile] for coordinate in block.coordinates],

            BlockType.Conductor:
                [coordinate for block in self.blocks[BlockType.Conductor] for coordinate in block.coordinates],

            BlockType.ComponentPad:
                [coordinate for block in self.blocks[BlockType.ComponentPad] for coordinate in block.coordinates],
        }

        self.coordinates_with_multiplier: dict[BlockType: list[Coordinate]] = {

            BlockType.Profile:
                [coordinate for block in self.blocks[BlockType.Profile] for coordinate in block.coordinates_with_multiplier],

            BlockType.Conductor:
                [coordinate for block in self.blocks[BlockType.Conductor] for coordinate in block.coordinates_with_multiplier],

            BlockType.ComponentPad:
                [coordinate for block in self.blocks[BlockType.ComponentPad] for coordinate in block.coordinates_with_multiplier],
        }



    def read_gerber_file(self, file_path: str) -> str:
        '''
        :param file_path: path to a gerber file
        reads the gerber file checks if it's a gerber file
        then returns it
        '''
        with open(file_path) as g_file:
            gerber_file = g_file.read() 

        self.check_GerberFile()

        return gerber_file

    def check_GerberFile(self) -> None:
        '''
        raises error if it's not a gerber file
        '''
        pass

    def create_gerber_file(self, gerber_file_name: str) -> None:
        """
        This function just writes the string input gerber file content to a <file_name>.gbr
        :gerber_file_name: name of the file to be created/overwritten
        """
        gerber_file = self.gerber_file
        self.check_GerberFile()

        with open(gerber_file_name, 'w') as g_file:
            g_file.write(gerber_file)

    @classmethod
    def get_XY(cls, line: str) -> Coordinate:
        '''
        :param line: line string from gerber file
        :return: a Coordinate object
        '''

        if not line.startswith('X'):
            return None

        try:
            x = int(line[1 : line.index('Y')])
        except ValueError:  # it's a float not an integer 
            x = float(line[1 : line.index('Y')])

        try:
            y = int(line[line.index('Y')+1 : line.index('D')])
        except ValueError:  # it's a float not an integer
            y = float(line[line.index('Y')+1 : line.index('D')])

        return Coordinate(x, y)

    def generate_line(self, line: str, coordinate: Coordinate) -> str:
        '''
        :param line: the old line, #NOTE: it's wanted to get the D value at the end of each gerber coordinate line
        :param coordinates: list of x value and y value
        :return: line string with update coordinates values
        '''
        # Make sure it's indeed a coorindate gerber line
        if not line.startswith('X'):
            raise ValueError("the input line doesn't start with X. This is not a coordinate line.")

        if type(coordinate.x)!= int or type(coordinate.y) != int:
            raise ValueError("Coordinates to be written to gerber file MUST be integers NOT floats")
        
        # Get Index of x coordinate value and y coordinate value
        D_value = line[line.index('D'):]

        # Creating the new line 
        new_line = f"X{str(coordinate.x)}Y{str(coordinate.y)}{D_value}"

        return new_line

    def get_x_y_multiplier(self) -> tuple[int, int]:
        '''
        gerber files has coordinates in mm * 10**6 or even 8, this function return the multipler, e.g- the 10**6 

        :return: two integers one for the x multipler and the other for the y multiplier
        '''
        gerber_file = self.gerber_file

        start_ind = gerber_file.index("%FSLA") + 5
        end_ind = start_ind + gerber_file[start_ind:].index('\n')

        percision_set_line = gerber_file[start_ind:end_ind]

        ger_percision_x_format = int(percision_set_line[1 : percision_set_line.index('Y')])
        ger_percision_y_format = int(percision_set_line[percision_set_line.index('Y')+1 : percision_set_line.index('*')])

        if ger_percision_x_format == 46:
            x_multiplier = 10**6
        else:
            raise ValueError("unknown percision x format in line that contain '%FSLA'")

        if ger_percision_y_format == 46:
            y_multiplier = 10**6
        else:
            raise ValueError("unknown percision y format in line that contain '%FSLA'")

        return x_multiplier, y_multiplier

    def apply_multiplier(self, coordinate: Coordinate) -> Coordinate:
        '''
        applies to gerber multiplier to a list of coordinates
            e.g: 1.36 -> 1360000000

        :param coordinate: coordinates to apply multiplier to
        :return: coordinate with applied multiplier
        '''
        return Coordinate(int(coordinate.x * self.x_multiplier), int(coordinate.y * self.y_multiplier))


    def recenter_gerber_file(self, user_x_offset: int, user_y_offset: int) -> None:
        '''
        self.gerber_file is recentered according to input offsets

        :param user_x_offset: wanted x offset from origin. if 0 then pcb will start at 0
        :param user_y_offset: wanted y offset from origin. if 0 then pcb will start at 0
        '''

        # Get the all coordinates that relate to the Edge of the PCB
        coordinates = self.coordinates_with_multiplier[BlockType.Profile]

        # Get X and Y, min and max
        min_coordinate, max_coordinate = Coordinate.get_min_max(coordinates)
        x_min = min_coordinate.x
        y_min = min_coordinate.y

        # Calculating the offset to be added to each coordinate in the gerber file
        x_offset = int(-x_min + user_x_offset * self.x_multiplier)
        y_offset = int(-y_min + user_y_offset * self.y_multiplier)

        # Generating the new gerber file with the offset added to every line of coordinates
        g_file_lines = self.gerber_file.split('\n')
        for line_num, line in enumerate(g_file_lines):

            coordinates = Gerber.get_XY(line)
            if coordinates:
                coordinates.x += x_offset
                coordinates.y += y_offset

                g_file_lines[line_num] = self.generate_line(line, coordinates)

        new_file = "\n".join(g_file_lines)

        self.gerber_file = new_file


if __name__ == '__main__':

    gerber_file_path = 'gerber_files/default.gbr'
    # gerber_file_path = 'gerber_files/test.gbr'

    new_file_name = 'gerber_files/test2.gbr'

    # Offset PCB from (0, 0)
    user_x_offset = 3.5
    user_y_offset = 4.5

    # Initializing GerberFile Object
    gerber_object = Gerber(gerber_file_path)

    # Recenter Gerber File with wanted Offset
    gerber_object.recenter_gerber_file(user_x_offset, user_y_offset)
    
    # Writing a new gerber file for current gerber file content
    gerber_object.create_gerber_file(new_file_name)


