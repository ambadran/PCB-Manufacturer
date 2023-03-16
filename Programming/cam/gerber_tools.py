'''
This files contains functions to parse gerber files and deal with them
'''
from __future__ import annotations
from enum import Enum
from dataclasses import dataclass


class BlockType(Enum):
    Conductor = 'Conductor'
    ComponentPad = 'ComponentPad'
    Profile = 'Profile'

@dataclass
class Coordinate:
    x: float
    y: float
    z: float = None

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


def get_min_max(coordinates: list[Coordinate]) -> tuple[Coordinate, Coordinate]:
    '''
    finds the Min, Max of X and Y coordinates from input list of coordinates

    :param coordinates: list of coordinates [(x, y), ..]
    :return: ((x_min, y_min), (x_max, y_max))
    '''

    x_min, y_min = coordinates[0]
    x_max, y_max = x_min, y_min

    for coordinate in coordinates:

        new_x, new_y = coordinate.x, coordinate.y

        if new_x < x_min:
            x_min = new_x

        elif new_x > x_max:
            x_max = new_x

        if new_y < y_min:
            y_min = new_y

        elif new_y > y_max:
            y_max = new_y

    return Coordiante((x_min, x_max)), (Coordiante(y_min, y_max))
        

class Block:
    '''
    Gerber Block of coordinates
    each block is named like this 'Dxx' where xx is the number that identifies this block
    each block has a group type which determines whether it is drill coordinate, trace coordinate or edge coordinates
    each block has a thickness assigned to it
    each block has it's own set of coordinates
    '''
    def __init__(self, D_num: int, coordinates: list[Coordinate], block_type: BlockType, thickness: float):
        self.parent_block = parent_block
        self.D_num = D_num
        self.coordinates = coordiantes

    @classmethod
    def from_gerber(cls, gerber_file: str, block_type: BlockType) -> list[Block]:
        '''
        :param gerber_file: gerber file in string form
        :param block_type: what block type wanted to be extracted from the gerber file

        :returns: a list of ALL Block objects of a specific BlockType found in a gerber file 
        '''
        pass

    def extract_block_coordinates(gerber_file: str, block_name: str, with_multiplier:bool = False) -> list[list[int, int]]:
        '''
        :param gerber_file: gerber_file as a single string
        :param block_name: usually gerber block names are 'ComponentPad' for PCB holes, 
                            'Profile' for PCB cutout and 'Conductor' for traces
        :param with_multiplier: gerber file coordinate values are usually intger values of mm values 
                                multiplied by a huge mutiplier, e.g 10**6
        :return: list of coordinate list, coordinate list is an x and y values 
        '''


        g_file_lines = gerber_file.split('\n')

        coordinates = []

        # getting the Dxx of the block we want
        d_nums = []
        for line_num, line in enumerate(g_file_lines):
            if block_name in line:
                wanted_line = g_file_lines[line_num+1]

                # getting the D number of the profile definition, by finding the last char that is a digit
                start_wanted_index = wanted_line.find('%ADD') + 4
                for char_num, char in enumerate(wanted_line[start_wanted_index:]):
                    if not char.isdigit():
                        end_wanted_index = 4 + char_num
                        break
                d_nums.append(wanted_line[start_wanted_index:end_wanted_index])

        # getting all the gerber coordinates under the wanted Dxx
        take_lines = False
        g_file_lines_start_ind = gerber_file[:gerber_file.find('D')].count('\n')  # coordinates start from first 'D' occurance
        for line_num, line in enumerate(g_file_lines[g_file_lines_start_ind:]):

            #TODO: ASSUMPTION!! Here I am assuming start of a block always looks like this 'Dxyz', where x is int, y int or nothing and z is any character
            if line.startswith('D'):  # decide on whether to take lines or not
                take_lines = line[1:-1] in d_nums
                continue

            if take_lines:
                coordinate = get_XY(line)
                if coordinate is not None:
                    coordinates.append(coordinate)

        # Get multiplier if user wants to remove it
        if not with_multiplier:
            x_multiplier, y_multiplier = get_x_y_multiplier(gerber_file)

            # converting coordinates to mm
            for ind, coordinate in enumerate(coordinates):
                coordinates[ind][0] /= x_multiplier
                coordinates[ind][1] /= y_multiplier

        return coordinates

    def extract_block_drawing_width(gerber_file: str, D_num: int) -> float:
        '''
        Extracts the width of drawings of a specific block D number from gerber file. 
            e.g- D16 is a 'ComponentPad' and is thickness 0.8mm

        :param gerber_file: gerber_file to read from
        :param D_num: D number of the wanted block to get the thickness of

        :return: float value of the thickness of the D number block
        '''
        thickness: float
        return thickness

    def __str__(self):
        return f"D{self.D_num} of thickness {self.thickness} and {len(self.coordinates)} coordinates"


class Gerber:
    '''
    Class to implement basic functionlity to read, manipulate and write gerber files
    '''
    def __init__(self, file_path: str):
        self.gerber_file = self.read_gerber_file(file_path)
        self.x_multiplier, self.y_multiplier = self.get_x_y_multiplier()
        self.edge_blocks: List[Block] = 
        self.trace_blocks: list[Block]
        self.

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

    def create_gerber_file(gerber_file_name: str) -> None:
        """
        This function just writes the string input gerber file content to a <file_name>.gbr
        :gerber_file_name: name of the file to be created/overwritten
        """
        gerber_file = self.gerber_file
        self.check_GerberFile(gerber_file)

        with open(gerber_file_name, 'w') as g_file:
            g_file.write(gerber_file)

    def get_XY(self, line: str) -> list[int, int]:
        '''
        :param line: line string from gerber file
        :return: a 2 value list of x and y 
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

        return [x, y]

    def generate_line(self, line: str, coordinates: list[int, int]) -> str:
        '''
        :param line: the old line
        :param coordinates: list of x value and y value
        :return: line string with update coordinates values
        '''
        # Make sure it's indeed a coorindate gerber line
        if not line.startswith('X'):
            raise ValueError("the input line doesn't start with X. This is not a coordinate line.")
        
        # Get Index of x coordinate value and y coordinate value
        D_value = line[line.index('D'):]
        
        # Creating the new line 
        new_line = f"X{str(coordinates[0])}Y{str(coordinates[1])}{D_value}"

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

    def recenter_gerber_file(self, user_x_offset: int, user_y_offset: int) -> None:
        '''
        self.gerber_file is recentered according to input offsets

        :param user_x_offset: wanted x offset from origin. if 0 then pcb will start at 0
        :param user_y_offset: wanted y offset from origin. if 0 then pcb will start at 0
        '''
        gerber_file = self.gerber_file

        # Get the all coordinates that relate to the Edge of the PCB
        coordinates = extract_block_coordinates(gerber_file, 'Profile', with_multiplier=True)

        # Get X and Y, min and max
        x_min_max, y_min_max = get_min_max(coordinates)
        x_min = x_min_max[0]
        y_min = y_min_max[0]

        # Get X and Y multiplier
        x_multiplier, y_multiplier = get_x_y_multiplier(gerber_file)    

        # Calculating the offset to be added to each coordinate in the gerber file
        x_offset = -x_min + user_x_offset * x_multiplier 
        y_offset = -y_min + user_y_offset * y_multiplier

        # Generating the new gerber file with the offset added to every line of coordinates
        g_file_lines = gerber_file.split('\n')
        for line_num, line in enumerate(g_file_lines):

            coordinates = get_XY(line)
            if coordinates:
                coordinates[0] += x_offset
                coordinates[1] += y_offset

                g_file_lines[line_num] = generate_line(line, coordinates)

        new_file = "\n".join(g_file_lines)

        self.gerber_file = new_file

    def __str__(self):
        return self.gerber_file

if __name__ == '__main__':

    gerber_file_path = 'gerber_files/default.gbr'
    # gerber_file_path = 'gerber_files/test.gbr'

    new_file_name = 'test2.gbr'

    # Offset PCB from (0, 0)
    user_x_offset = 3
    user_y_offset = 6

    # Initializing GerberFile Object
    gerber_object = Gerber(gerber_file_path)

    # Recenter Gerber File with wanted Offset
    gerber_object.recenter_gerber_file(user_x_offset, user_y_offset)
    
    gerber_object.create_gerber_file(new_file_name)


