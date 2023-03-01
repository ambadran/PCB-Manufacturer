'''
This file has function to generate the gcode we want
'''
from gerber_tools import *
from enum import Enum
from typing import Callable


class Mode(Enum):
    Deselect = 0
    Select = 1


class Tool(Enum):
    Empty = 0
    Laser = 1
    Spindle = 2
    Pen = 3


def move(**kwargs) -> str:
    '''
    must input either coordinate=[x, y] or one of x=int, y=int, z=int or a combination of those three
    must also input feedrate=int
    return gcode line of the wanted inputs
    '''

    coordinate_mode = False
    letter_mode = False

    feedrate_available = False
    comment_available = False

    gcode = 'G01 '

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

        elif key == 'feedrate':
            feedrate_available = True  # will note assign now in case the arguments are not in order. feedrate must be in the end

        elif key == 'comment':
            comment_available = True

        else:
            raise ValueError("Unknown keyword argument! Supported one: coordinate, x, y, z, feedrate")

    if feedrate_available:
        gcode += f"F{kwargs['feedrate']}"
    if comment_available:
        gcode += f" ; {kwargs['comment']}"

    gcode += '\n'

    return gcode


def get_tool_func(latch_offset_distance: int, tool_home_coordinates: dict[int: list[int, int, int]]) -> Callable:
    '''
    Closure Function to define constant values for latch_offset_distance and tool_home_coordinates
    #NOTE latch_offset_distance and tool_home_coordinates are assumed to be absolute values!!!
    '''
    def tool(mode: Mode, wanted_tool: Tool) -> str:
        '''
        #NOTE VERY VERY IMPORTANT, THIS FUNCTION ASSUMES TOOL HEAD IS EMPTY!!!
        Generate Gcode to select/deselect wanted tool
        :mode: select or deselect Mode Enum
        wanted_tool: the wanted tool to select/deselect

        :return: gcode to select and activate the tool
        #TODO: implement eeprom tool select memory in microcontroller, read it to know last tool selected
        '''
        gcode = ''
        
        tool_home_coordinate = tool_home_coordinates[wanted_tool.value]

        if mode == Mode.Select:
            ### Go get the tool
            gcode += f"; Getting and Activating Tool-{wanted_tool.value}\n"
            # go to tool coordinate but male latch is just outside the female latch
            gcode += move(coordinate=tool_home_coordinate, comment=f'Go to Tool-{wanted_tool.value} Home Pos')
            # Now male latch inside female latch
            gcode += move(x=latch_offset_distance, comment='Enter Female Kinematic Mount Home Pos')
            # now male latch twisting and locking on
            gcode += f"A1 ; Latch on Kinematic Mount\n"  
            # Wait until male latch is fully locked on
            gcode += f"G4 P5000 ; Wait for Kinematic Mount to fully attach\n"  
            # now pull off the female kinematch mount off its hanger
            gcode += move(coordinate=tool_home_coordinate, comment='Exit Female Kinematic Mount Home Pos')

            ### Activate it by sending the corresponding tool number in the multiplexer
            gcode += f'C{wanted_tool.value} ; Choosing tool {wanted_tool.value} in the choose demultiplexer circuits\n'

        elif mode == Mode.Deselect:
            ### Deactivate it by selecting the empty tool in the multiplexer
            gcode += f"; Returning the Deactivating Tool-{wanted_tool.value}"
            # go to tool coordinate but male latch is just outside the female latch
            gcode += move(coordinate=tool_home_coordinate, comment=f'Go to Tool-{wanted_tool.value} Home Pos')
            # Now male latch inside female latch
            gcode += move(x=latch_offset_distance, comment='Enter Female Kinematic Mount Home Pos')  
            # male latch untwisting from female latch and locking off
            gcode += f"A0 ; Latch OFF Kinematic Mount\n" 
            # Wait until male latch is fully locked off
            gcode += f"G4 P5000 ; Wait for Kinematic Mount to fully detach\n"
            # now pull off the female kinematch mount off its hanger
            gcode += move(coordinate=tool_home_coordinate, comment='Exit Female Kinematic Mount Home Pos')  

            ### Go put the the tool back, now we know for sure when C0 is selected, no tool is there
            gcode += 'C0 ; PWM Tool select demultiplexer to select tool zero which is the empty tool slot in multiplexers\n'

        else:
            raise ValueError("Mode unknown")

        gcode += '\n'
        return gcode

    return tool


def generate_holes_gcode(gerber_file: str, tool: Callable, motor_up_z_position: int, motor_down_z_position: int, feedrate_XY: int, feedrate_Z: int, spindle_speed: int, terminate_after=True) -> str:
    '''
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
    gcode += f"G10 P0 L20 X0 Y0 Z0 ; Force Reset current coordinates after homing\n\n"

    # Activiate Tool number 2, The Spindle
    gcode += tool(Mode.Select, Tool.Spindle)

    # setting the S value which sets pwm speed when we enable it, 
    if spindle_speed < 0 or spindle_speed > 250:
        raise ValueError("spindle_speed is only from 0-250")
    gcode += f'S{spindle_speed} ; sets pwm speed when we enable it\n'

    # Moving Motor to proper up Z position and home position
    gcode += move(z=motor_up_z_position, feedrate=feedrate_Z)
    gcode += '\n'

    # Turn the DC motor on and wait two seconds
    gcode += 'M3 ; Turn Motor ON\n'
    gcode += 'G4 P2000 ; dwell for 2 seconds so motor reaches full RPM\n\n'

    # Cutting starts here :)
    coordinates = extract_block_coordinates(gerber_file, 'ComponentPad')
    for coordinate in coordinates:
        gcode += move(coordinate=coordinate, feedrate=feedrate_XY)
        gcode += move(z=motor_down_z_position, feedrate=feedrate_Z)
        gcode += move(z=motor_up_z_position, feedrate=feedrate_Z)
    gcode += '\n'

    # deactivating the tool PWM
    gcode += 'M5 ; Turn Motor OFF\n\n'

    # Get the tool back to its place and deactivate the tool
    gcode += tool(Mode.Deselect, Tool.Spindle)

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



