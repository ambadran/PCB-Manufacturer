'''
This file has function to generate the gcode we want
'''
from gerber_tools import *
from enum import Enum
from typing import Callable, Optional


class ToolChange(Enum):
    Deselect = 0
    Select = 1


class CoordMode(Enum):
    ABSOLUTE = 0
    INCREMENTAL = 1


class Tool(Enum):
    Empty = 0
    Laser = 1
    Spindle = 2
    Pen = 3


def get_coordinate_from_kwargs(kwargs) -> str:
    '''
    reads the kwargs argument and return something like X_Y_ for gcode usage

    :param kwargs: must input either coordinate=[x, y] or one of x=int, y=int, z=int or a combination of those three
    :return: gcode coordinate string
    '''
    gcode = ''

    coordinate_mode = False
    letter_mode = False

    for key, value in kwargs.items():

        if key == 'coordinate':
            if letter_mode:
                raise ValueError("Can't have both coordinate argument and x, y or z arguments")
            coordinate_mode = True

            if type(value) != list:
                raise ValueError("Coordinate value must a list of two integer/float (x and y) or three integers/float (x, y, z)")

            if len(value) == 2:
                if not(type(value[0]) == int or type(value[1]) == int or type(value[0]) == float or type(value[1]) == float):
                    raise ValueError("Coordinate list must only contain integers or floats")
                gcode += f'X{value[0]}Y{value[1]}'

            elif len(value) == 3:
                if not(type(value[0]) == int or type(value[1]) == int or type(value[0]) == float or type(value[1]) == float or type(value[2]) == int or type(value[2] == float)):
                    raise ValueError("Coordinate list must only contain integers or floats")
                gcode += f'X{value[0]}Y{value[1]}Z{value[2]}'
            else:
                raise ValueError("Coordinate list must contain 2 or 3 integer/float values: [x, y] or [x, y, z]")


        elif key == 'x' or key == 'X':
            if coordinate_mode:
                raise ValueError("Can't have both coordinate argument and x, y or z arguments")
            letter_mode = True

            if not(type(value) == int or type(value) == float):
                raise ValueError('X value must be an integer or float')

            gcode += f'X{value}'

        elif key == 'y' or key == 'Y':
            if coordinate_mode:
                raise ValueError("Can't have both coordinate argument and x, y or z arguments")
            letter_mode = True 

            if not(type(value) == int or type(value) == float):
                raise ValueError('Y value must be an integer or float')

            gcode += f'Y{value}'

        elif key == 'z' or key == 'Z':
            if coordinate_mode:
                raise ValueError("Can't have both coordinate argument and x, y or z arguments")
            letter_mode = True 

            if not(type(value) == int or type(value) == float):
                raise ValueError('Z value must be an integer or float')

            gcode += f'Z{value}'

        else:
            raise ValueError("Unknown keyword argument! Supported keywords: coordinate, x, y, z")

    return gcode


def set_grbl_coordinate(coordinate_mode: CoordMode, comment: Optional[str]=None, **coordinate) -> str:
    '''
    overwrites the current grbl working coordinate
    :param kwargs: must input either coordinate=[x, y] or one of x=int, y=int, z=int or a combination of those three

    :return: gcode line of the wanted inputs
    '''
    comment_available = False

    if coordinate_mode == CoordMode.ABSOLUTE:
        gcode = "G10 P0 L20 "
    elif coordinate_mode == CoordMode.INCREMENTAL:
        gcode = '#TODO '
    else:
        raise ValueError("Unsupported Mode!")

    gcode += get_coordinate_from_kwargs(coordinate)

    if comment:
        gcode += f" ; {comment}"

    gcode += '\n'

    return gcode


def move(coordinate_mode: CoordMode, feedrate: Optional[int]=None, comment: Optional[str]=None, **coordinates) -> str:
    '''
    must input either coordinate=[x, y] or one of x=int, y=int, z=int or a combination of those three
    must also input feedrate=int
    return gcode line of the wanted inputs
    '''

    if coordinate_mode == CoordMode.ABSOLUTE:
        gcode = 'G01 '
    elif coordinate_mode == CoordMode.INCREMENTAL:
        gcode = '#TODO ' #TODO:

    gcode += get_coordinate_from_kwargs(coordinates)

    if feedrate:
        gcode += f"F{feedrate}"
    if comment:
        gcode += f" ; {comment}"

    gcode += '\n'

    return gcode


def get_tool_func(latch_offset_distance_in: int, latch_offset_distance_out: int, tool_home_coordinates: dict[int: tuple[int, int, int]], tool_offsets: dict[int: tuple[int, int, int]]) -> Callable:
    '''
    Closure Function to define constant values for:
    :param latch_offset_distance_in: the distance the male end kinematic mount has to move (+X) to enter female latch
                                     #NOTE this value is INCREMENTAL

    :param latch_offset_distance_out: after the male and female kinematic mount are joined, the distance to move
                                      back to pull the female kinematic mount body off the hanger (-X)
                                      #NOTE this value is INCREMENTAL

    :param tool_home_coordinates: dictionary for each tool, where the value is the coordinate of the home position of the
                                  corresponding tool
                                  #NOTE this value is ABSOLUTE relative to origin (origin is zero when no head is there)

    :param tool_offsets: dictionary for each tool, where the value is the coordinate offset to set the new exact
                         end effector position relative from Origin (0, 0, 0)
                         #NOTE this value is INCREMENTAL 

    :returns: the actual tool changing gcode generator function with the proper setup values
    '''
    def tool(tool_change_mode: ToolChange, wanted_tool: Tool) -> str:
        '''
        #NOTE VERY VERY IMPORTANT, THIS FUNCTION ASSUMES TOOL HEAD IS EMPTY!!!
        #NOTE VERY VERY IMPORTANT, THIS FUNCTION ASSUMES THE MACHINE IS HOMED!!!

        Generate Gcode to select/deselect wanted tool
        :param tool_change_mode: select or deselect Mode Enum
        :param wanted_tool: the wanted tool to select/deselect

        :return: gcode to select and activate the tool
        #TODO: implement eeprom tool select memory in microcontroller, read it to know last tool selected
        '''
        gcode = ''
        
        tool_home_coordinate = tool_home_coordinates[wanted_tool.value]
        tool_offset = tool_offsets[wanted_tool.value]

        if tool_change_mode == ToolChange.Select:

            gcode += f"; Getting and Activating Tool-{wanted_tool.value}\n"

            ### Go get the tool
            # go to tool coordinate but male latch is just outside the female latch
            gcode += move(CoordMode.ABSOLUTE, comment=f'Go to Tool-{wanted_tool.value} Home Pos', coordinate=tool_home_coordinate)
            # Now male latch inside female latch, using incremental gcode
            gcode += move(CoordMode.INCREMENTAL, comment='Enter Female Kinematic Mount Home Pos', x=latch_offset_distance_in)
            # now male latch twisting and locking on
            gcode += f"A1 ; Latch on Kinematic Mount\n"  
            # Wait until male latch is fully locked on
            gcode += f"G4 P5000 ; Wait for Kinematic Mount to fully attach\n"  
            # now pull off the female kinematch mount off its hanger, using incremental gcode
            gcode += move(CoordMode.INCREMENTAL, comment='Exit Female Kinematic Mount Home Pos', x=latch_offset_distance_out)

            ### Fixing Current Coordinate according the new tool head
            gcode += set_grbl_coordinate(CoordMode.INCREMENTAL, comment=' ;Add tool offset coordinate', coordinate=tool_offset)

            ### Activate it by sending the corresponding tool number in the multiplexer
            gcode += f'C{wanted_tool.value} ; Choosing tool {wanted_tool.value} in the choose demultiplexer circuits\n'

        elif tool_change_mode == ToolChange.Deselect:

            gcode += f"; Returning the Deactivating Tool-{wanted_tool.value}"

            ### Selecting empty tool slot in the multiplexer to stop any potential end effector action.
            gcode += 'C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers\n'

            ### Overide current coordinate to go to tool home pos relative to origin by inversing the tool_offset
            tool_offset = [i*-1 for i in tool_offset]
            gcode += set_grbl_coordinate(CoordMode.INCREMENTAL, comment=' ;Remove tool offset coordinate', coordinate=tool_offset)

            ### Deactivate it by selecting the empty tool in the multiplexer
            # go to tool coordinate but male latch is just outside the female latch
            gcode += move(CoordMode.ABSOLUTE, comment=f'Go to Tool-{wanted_tool.value} Home Pos', coordinate=tool_home_coordinate)
            # Put the tool back to it's hanger
            inverse_latch_offset_distance_out = -1*latch_offset_distance_out
            gcode += move(CoordMode.INCREMENTAL, comment='Enter Female Kinematic Mount Home Pos', x=inverse_latch_offset_distance_out)
            # male latch untwisting from female latch and locking off
            gcode += f"A0 ; Latch OFF Kinematic Mount\n" 
            # Wait until male latch is fully locked off
            gcode += f"G4 P5000 ; Wait for Kinematic Mount to fully detach\n"
            # Now pull off the male kinematic mount away from the female kinematic mount
            inverse_latch_offset_distance_in = -1*latch_offset_distance_in
            gcode += move(CoordMode.INCREMENTAL, comment='Exit Female Kinematic Mount Home Pos', x=inverse_latch_offset_distance_in)

        else:
            raise ValueError("Mode unknown")

        gcode += '\n'
        return gcode

    return tool


def generate_holes_gcode(gerber_file: str, tool: Callable, motor_up_z_position: int, motor_down_z_position: int, feedrate_XY: int, feedrate_Z: int, spindle_speed: int, terminate_after=True) -> str:
    '''
    Takes in String gerber file content, identifies the PCB holes and generates the Gcode to drill the holes from begging to end!

    :param gerber_file: the file that we want to get the holes coordinate from
    :param tool: The tool function defined inside the get_tool_func closure function, it generates gcode to select wanted tool
    :param motor_up_z_position: position the drill bit is not touching the PCB is off a reasonable offset above the PCB
    :param motor_down_z_position: position the drill bit has completely drilled through the PCB 
    :param feedrate_XY: integer mm/minute, only for x and y movement
    :param feedrate_Z: integer mm/minute, only for z movement, which must be much slower for spindle to cut properly
    :param spindle_speed: rpm of DC motor to drill holes, please note that the value is 0-250, default value is 230 as tested.
    :param termiante_after: if true will Cut off machine power after job finishes

    :return: This function creates the gcode content as string according to the input coordinates
    '''

    check_GerberFile(gerber_file)

    # G-Code to be generated
    gcode = '; This gcode is generated by my python script specially for my PCB manufacturer project :))\n\n'

    gcode += 'G21 ; to set metric units\n'
    gcode += 'G90 ; to set absolute mode , G91 for incremental mode\n'
    gcode += 'G94 ; To set the active feed rate mode to units per minute mode\n\n'

    gcode += f'F{feedrate_XY} ; setting default feedrate\n\n'

    # M5 disables spindle PWM, C0 chooses empty tool slot in multiplexer, to ensure no endeffector works by mistake 
    gcode += f'M5 ; disabling spindle PWM\n'
    gcode += f'C0 ; Choosing the empty tool slot in the multiplexer circuits\n\n'

    # Turn ON Machine
    gcode += f"B1 ; Turn ON Machine\n\n"

    # HOMING, machine is at (0, 0, 0) now
    gcode += f"$H ; Homing :)\n"

    # Make sure grbl understands it's at zero now
    gcode += set_grbl_coordinate(CoordMode.ABSOLUTE,comment="Force Reset current coordinates after homing\n", coordinate=[0, 0, 0])

    # Activiate Tool number 2, The Spindle
    gcode += tool(ToolChange.Select, Tool.Spindle)

    # setting the S value which sets pwm speed when we enable it, 
    if spindle_speed < 0 or spindle_speed > 250:
        raise ValueError("spindle_speed is only from 0-250")
    gcode += f'S{spindle_speed} ; sets pwm speed when we enable it\n'

    # Moving Motor to proper up Z position and home position
    gcode += move(CoordMode.ABSOLUTE, z=motor_up_z_position, feedrate=feedrate_Z)
    gcode += '\n'

    # Turn the DC motor on and wait two seconds
    gcode += 'M3 ; Turn Motor ON\n'
    gcode += 'G4 P2000 ; dwell for 2 seconds so motor reaches full RPM\n\n'

    # Cutting starts here :)
    coordinates = extract_block_coordinates(gerber_file, 'ComponentPad')
    for coordinate in coordinates:
        gcode += move(CoordMode.ABSOLUTE, coordinate=coordinate, feedrate=feedrate_XY)
        gcode += move(CoordMode.ABSOLUTE, z=motor_down_z_position, feedrate=feedrate_Z)
        gcode += move(CoordMode.ABSOLUTE, z=motor_up_z_position, feedrate=feedrate_Z)
    gcode += '\n'

    # deactivating the tool PWM
    gcode += 'M5 ; Turn Motor OFF\n\n'

    # Get the tool back to its place and deactivate the tool
    gcode += tool(ToolChange.Deselect, Tool.Spindle)

    # Turn Machine Off
    if terminate_after:
        gcode += 'B0 ; Turn Machine OFF\n'

    return gcode


def generate_ink_laying_gcode(gerber_file: str, tool: Callable, pen_down_position: int, feedrate: int, terminate_after=True) -> str:
    '''
    :param gerber_file: the file that we want to get the holes coordinate from
    :param tool: The tool function defined inside the get_tool_func closure function, it generates gcode to select wanted tool
    :param pen_down_position: position that pen touches PCB in Z axis
    :param feedrate: integer mm/minute, only for x and y movement, z movement is hardcoded here
    :param termiante_after: if true will Cut off machine power after job finishes

    :return: This function creates the gcode content as string according to the input coordinates
    '''

    coordinates = extract_block_coordinates(gerber_file, 'Profile')
    print(coordinates)

    return ''


def generate_pcb_trace_gcode(gerber_file: str, tool: Callable, optimum_focal_distance: int, feedrate: int, laser_power: int, terminate_after=True) -> str:
    '''
    :param gerber_file: the file that we want to get the holes coordinate from
    :param tool: The tool function defined inside the get_tool_func closure function, it generates gcode to select wanted tool
    :param optimum_focal_distance: the distance at the laser is at its best focal distance
    :param feedrate: integer mm/minute, only for x and y movement, z movement is hardcoded here
    :param laser_power: laser intensity for toner transfer, please note that the value is 0-250, default value is 150 as tested.
    :param termiante_after: if true will Cut off machine power after job finishes

    :return: This function creates the gcode content as string according to the input coordinates
    '''
    return ''


def export_gcode(gcode: str, file_name: str) -> None:
    '''
    :param gcode: the actual gcode file content
    :param file_name: the wanted gcode filename
    creates the gcode file
    '''
    with open(file_name, 'w') as g_file:
        g_file.write(gcode)


if __name__ == '__main__':

    #NOTE!!!! The gerber file is assumed to be mirrorred!!!!!
    gerber_file_path = 'gerber_files/default.gbr'
    gcode_file_path = 'gcode_files/default.gcode'

    ##### Tweaking Arguments #####

    # Offset PCB from (0, 0)
    user_x_offset = 2
    user_y_offset = 2

    ### Tool Home positions and latch offset (as absolute values)
    latch_offset_distance_in = 5  #TODO: find this value ASAP, NOTE that this value is INCREMANTAL
    latch_offset_distance_out = -10  #TODO: find this value ASAP, NOTE that this value is INCREMENTAL
    tool_home_coordinates = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0]}  #TODO: find this value ASAP, NOTE this value is ABSOLUTE
    # NOTE this value is INCREMENTAL, it's absolute relative to origin when machine is homed.
    tool_offsets = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0]}  #TODO: find this value ASAP, 
    tool = get_tool_func(latch_offset_distance_in, latch_offset_distance_out, tool_home_coordinates, tool_offsets)

    ### spindle tweaking values
    # Z positions
    router_Z_up_position = 20
    router_Z_down_position = 25
    # Feedrates
    router_feedrate_XY = 700
    router_feedrate_Z = 10
    # Power intensities
    spindle_speed = 230

    ### Pen Tweaking Values
    # Z positions
    pen_down_position = 10 
    # Feedrates
    ink_laying_feedrate = 100

    ### Laser Module Tweaking Values
    # Z positions
    optimum_laser_Z_position = 16  # 44mm from laser head to PCB
    # Feedrates
    pcb_trace_feedrate = 600
    # Power intensities
    laser_power = 150 



    gerber_file = read_gerber_file(gerber_file_path)

    recentered_gerber_file = recenter_gerber_file(gerber_file, user_x_offset, user_y_offset)

    gcode = generate_ink_laying_gcode(recentered_gerber_file, tool, pen_down_position, ink_laying_feedrate, terminate_after = False)

    print(gcode)
