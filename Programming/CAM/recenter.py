
def recenter_gerber_file(file_path, user_x_offset, user_y_offset):
    '''
    :param file_path: .gbr file path
    :param user_x_offset: wanted x offset from origin. if 0 then pcb will start at 0
    :param user_y_offset: wanted y offset from origin. if 0 then pcb will start at 0

    overwrites the file with the new correct coordinate values
    '''

    # reading the file
    with open(file_path) as g_file:
        gerber_file = g_file.read() 
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


    # adding offset to every coordinate value
    def update_line(line: str, coordinates: list[int, int]) -> str:
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


    for line_num, line in enumerate(g_file_lines):

        coordinates = get_XY(line)
        if coordinates:
            coordinates[0] += x_offset
            coordinates[1] += y_offset

            g_file_lines[line_num] = update_line(line, coordinates)


    # overwriting the gerber file with the new offset added values
    new_file = "\n".join(g_file_lines)
    with open(file_path, 'w') as g_file:
        g_file.write(new_file)


if __name__ == '__main__':

    # script inputs
    file_path = 'all.gbr'
    user_x_offset = 0  # unit is mm. from origin
    user_y_offset = 0  # unit is mm. from origin

    recenter_gerber_file(file_path, user_x_offset, user_y_offset)


