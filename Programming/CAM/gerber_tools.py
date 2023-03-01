
def check_GerberFile(gerber_file: str) -> None:
    '''
    :param gerber_file: gerber file read and returned as string

    raises error if it's not a gerber file
    '''
    pass

def read_gerber_file(file_path: str) -> str:
    '''
    :param file_path: path to a gerber file
    reads the gerber file checks if it's a gerber file
    then returns it
    '''
    with open(file_path) as g_file:
        gerber_file = g_file.read() 

    check_GerberFile(gerber_file)

    return gerber_file


# finding the all x and y values, then getting the min of each, then getting the offset value
def get_XY(line: str) -> list[int, int]:
    '''
    :param line: line string from gerber file
    :return: a 2 value list of x and y 
    '''

    if not line.startswith('X'):
        return []

    x = int(line[1 : line.index('Y')])
    y = int(line[line.index('Y')+1 : line.index('D')])

    return [x, y]


def extract_block_coordinates(gerber_file: str, block_name: str) -> list[list[int, int]]:
    '''
    :param gerber_file: gerber_file as a single string
    :param block_name: usually gerber block names are 'ComponentPad' for PCB holes, 
                        'Profile' for PCB cutout and 'Conductor' for traces
    :return: list of coordinate list, coordinate list is an x and y values 
    '''

    check_GerberFile(gerber_file)

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

def generate_line(line: str, coordinates: list[int, int]) -> str:
    '''
    :param line: the old line
    :param coordinates: list of x value and y value
    :return: line string with update coordinates values
    '''
    if not line.startswith('X'):
        raise ValueError("the input line doesn't start with X. This is not a coordinate line.")

    line = line.replace(line[1 : line.index('Y')], str(coordinates[0]))
    line = line.replace(line[line.index('Y')+1 : line.index('D')], str(coordinates[1]))

    return line

def recenter_gerber_file(gerber_file: str, user_x_offset: int=2, user_y_offset: int=2) -> str:
    '''
    :param gerber_file: the gerber file read, checked and returned as string
    :param user_x_offset: wanted x offset from origin. if 0 then pcb will start at 0
    :param user_y_offset: wanted y offset from origin. if 0 then pcb will start at 0

    :returns: the new gerber file as string
    '''
    g_file_lines = gerber_file.split('\n')

    # getting the AperFunction,Profile definition. It contains the definition of the PCB edges
    for line_num, line in enumerate(g_file_lines):
        if 'Profile' in line:
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


    x_min, y_min = get_XY(edge_coordinates_block[0])
    x_max, y_max = x_min, y_min
    for line in edge_coordinates_block:

        new_x, new_y = get_XY(line)

        if new_x < x_min:
            x_min = new_x

        elif new_x > x_max:
            x_max = new_x

        if new_y < y_min:
            y_min = new_y

        elif new_y > y_max:
            y_max = new_y

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



    x_offset = -x_min + user_x_offset * x_multiplier 
    y_offset = -y_min + user_y_offset * y_multiplier



    for line_num, line in enumerate(g_file_lines):

        coordinates = get_XY(line)
        if coordinates:
            coordinates[0] += x_offset
            coordinates[1] += y_offset

            g_file_lines[line_num] = generate_line(line, coordinates)


    new_file = "\n".join(g_file_lines)

    return new_file

def create_gerber_file(gerber_file: str, gerber_file_name: str) -> None:
    """
    This function just writes the string input gerber file content to a <file_name>.gbr
    :gerber_file: gerber file content as string
    :gerber_file_name: name of the file to be created/overwritten
    """
    check_GerberFile(gerber_file)

    with open(gerber_file_name, 'w') as g_file:
        g_file.write(new_file)


