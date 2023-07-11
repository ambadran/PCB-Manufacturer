
def test_recenter():
    # script inputs
    file_path = 'all.gbr'
    user_x_offset = 0  # unit is mm. from origin
    user_y_offset = 0  # unit is mm. from origin

    recenter_gerber_file(file_path, user_x_offset, user_y_offset)

def test_holes_gcode():

    gerber_file_path = 'gerber_files/all.gbr'
    file_name = 'gcode_files/gcode.nc'

    feedrate = 600
    spindle_speed = 230

    gerber_file = read_gerber_file(gerber_file_path)

    gcode = generate_holes_gcode(gerber_file, feedrate, spindle_speed)
    export_gcode(gcode, file_name)


