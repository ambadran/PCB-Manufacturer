'''
PCB manufacturer CAM program

My custom Gcode Generator :)))
'''
from recenter import recenter_gerber_file
from holes_gcode_generator import create_generate_holes_gcode

if __name__ == '__main__':

    file_path = 'default.gbr'
    user_x_offset = 5
    user_y_offset = 5
    feedrate = 600
    spindle_speed = 230
    file_name = 'default.gcode'

    recenter_gerber_file(file_path, user_x_offset, user_y_offset)

    create_generate_holes_gcode(file_path, feedrate, spindle_speed, file_name)

    
