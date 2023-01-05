

# finding the all x and y values, then getting the min of each, then getting the offset value
def get_XY(line: str) -> list:
    '''
    :param line: line string from gerber file
    :return: a 2 value list of x and y 
    '''

    if not line.startswith('X'):
        return []

    x = int(line[1 : line.index('Y')])
    y = int(line[line.index('Y')+1 : line.index('D')])

    return [x, y]


def extract_block_coordinates(file_path: str, block_name: str) -> list[list[int, int]]:
    '''
    :param file_path: directory to gerber file
    :param block_name: usually gerber block names are 'ComponentPad' for PCB holes, 
                        'Profile' for PCB cutout and 'Conductor' for traces
    :return: list of coordinate list, coordinate list is an x and y values 
    '''

    with open(file_path) as g_file:
        gerber_file = g_file.read() 
    g_file_lines = gerber_file.split('\n')


    # getting the AperFunction,ComponentPad definition. It contains the definition of the PCB holes
    coordinates = []
    for line_num, line in enumerate(g_file_lines):
        if block_name in line:
            wanted_line = g_file_lines[line_num+1]

            # getting the D number of the profile definition
            start_wanted_index = wanted_line.find('%ADD') + 4
            for char_num, char in enumerate(wanted_line[start_wanted_index:]):
                if not char.isdigit():
                    end_wanted_index = 4 + char_num
                    break
            d_num = wanted_line[start_wanted_index:end_wanted_index] 

            # finding the D block of the profile definition
            for line_num, line in enumerate(g_file_lines):
                if line.startswith('D' + d_num):
                    D_block_start_line = line_num + 1

            for line_num, line in enumerate(g_file_lines[D_block_start_line:]):
                if line.startswith('D'):
                    D_block_end_line = D_block_start_line + line_num
                    break

            edge_coordinates_block = g_file_lines[D_block_start_line:D_block_end_line]

            for line in edge_coordinates_block:
                coordinates.append(get_XY(line))

    # extracting decimal percision form gerber file to know how to turn to mm
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

    # converting coordinates to mm
    for ind, coordinate in enumerate(coordinates):
        coordinates[ind][0] /= x_multiplier
        coordinates[ind][1] /= y_multiplier

    return coordinates


def move(**kwargs) -> str:
    '''
    must input either coordinate=[x, y] or one of x=int, y=int, z=int or a combination of those three
    must also input feedrate=int
    return gcode line of the wanted inputs
    '''

    coordinate_mode = False
    letter_mode = False

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
            pass  # will note assign now in case the arguments are not in order. feedrate must be in the end

        else:
            raise ValueError("Unknown keyword argument! Supported one: coordinate, x, y, z, feedrate")

    if 'feedrate' in kwargs.keys():
        gcode += f"F{kwargs['feedrate']}"

    gcode += '\n'

    return gcode


def generate_holes_gcode(coordinates: list[list[int, int]], feedrate: int, spindle_speed: int) -> str:
    '''
    :param coordinates: list of coordinate list, coordinate list is an x and y values 
    :param feedrate: integer mm/minute, only for x and y movement, z movement is hardcoded here
    :param spindle_speed: rpm of DC motor to drill holes, please note that the value is 0-250
    :param file_name: the name of the generated gcode file

    This function creates the gcode content as string according to the input coordinates
    '''
    #TODO: measure it and put it here
    motor_feedrate = 10  # mm/min
    motor_up_z_position = 20  # mm
    motor_down_z_position = 25  # mm

    # G-Code to be generated
    gcode = '; This gcode is generated by my python script specially for my PCB manufacturer project :))\n\n'

    gcode += 'G21 ; to set metric units\n'
    gcode += 'G90 ; to set absolute mode , G91 for incremental mode\n'
    gcode += 'G94 ; To set the active feed rate mode to units per minute mode\n\n'

    gcode += f'F{feedrate} ; setting default feedrate\n\n'

    # HOMING, machine is at (0, 0, 0) now
    #TODO: 

    # M5 disables spindle PWM, S sets pwm speed when we enable it, 
    if spindle_speed < 0 or spindle_speed > 250:
        raise ValueError("spindle_speed is only from 0-250")
    gcode += f'M5 ; disabling spindle PWM\n'
    gcode += f'S{spindle_speed} ; sets pwm speed when we enable it\n'
    gcode += f'C2 ; C2 chooses second tool in the choose PWM demultiplexer circuit I built\n\n'

    # Moving Motor to proper up Z position and home position
    gcode += move(z=motor_up_z_position, feedrate=motor_feedrate)
    gcode += '\n'

    # Turn the DC motor on and wait two seconds
    gcode += 'M3 ; Turn Motor ON\n'
    gcode += 'G4 P2000 ; dwell for 2 seconds so motor reaches full RPM\n\n'

    # Cutting starts here :)
    for coordinate in coordinates:
        gcode += move(coordinate=coordinate, feedrate=feedrate)
        gcode += move(z=motor_down_z_position, feedrate=motor_feedrate)
        gcode += move(z=motor_up_z_position, feedrate=motor_feedrate)
    gcode += '\n'

    # deactivating the tool PWM
    gcode += 'M5 ; Turn Motor OFF\n'
    gcode += 'C0 ; PWM Tool select demultiplexer to select tool zero (which is nothing)\n\n'

    # Return Home (HOMING)
    #TODO:

    return gcode


def export_gcode(gcode: str, file_name: str):
    '''
    :param gcode: the actual gcode file content
    :param file_name: the wanted gcode filename
    creates the gcode file
    '''
    with open(file_name, 'w') as g_file:
        g_file.write(gcode)


def create_generate_holes_gcode(file_path: str, feedrate: int, spindle_speed: int, file_name: str):
    '''
    :param file_path: gerber file path
    :param feedrate: integer mm/minute, only for x and y movement, z movement is hardcoded here
    :param spindle_speed: rpm of DC motor to drill holes, please note that the value is 0-250
    :param file_name: the wanted gcode filename

    Does everything
    '''
    coordinates = extract_block_coordinates(file_path, 'ComponentPad')
    gcode = generate_holes_gcode(coordinates, feedrate, spindle_speed)
    export_gcode(gcode, file_name)


if __name__ == '__main__':

    file_path = 'all.gbr'

    feedrate = 600
    spindle_speed = 230

    file_name = 'gcode.nc'

    create_generate_holes_gcode(file_path, feedrate, spindle_speed, file_name)

