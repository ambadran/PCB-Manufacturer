'''
#TODO: The MOST IMPORTANT TASK NOW is to implement something to prevent choosing a tool when a tool is already mounted
PCB manufacturer CAM program

My custom Gcode Generator :)))
'''

from gerber_tools import *
from gcode_tools import *

if __name__ == '__main__':

    #NOTE!!!! The gerber file is assumed to be mirrorred!!!!!
    gerber_file_path = 'gerber_files/default.gbr'
    # gerber_file_path = 'gerber_files/test.gbr'
    gcode_file_path = 'gcode_files/default.gcode'
    new_file_name = 'test2.gbr'

    ##### Tweaking Arguments #####

    # Offset PCB from (0, 0)
    user_x_offset = 2
    user_y_offset = 2

    ### Tool Home positions and latch offset (as absolute values)
    X_latch_offset_distance_in = 188  # ABSOLUTE value
    X_latch_offset_distance_out = 92  # ABSOLUTE value
    attach_detach_time = 5 # the P attribute in Gcode is in seconds
    tool_home_coordinates = {1: Coordinate(165, 0, 11), 2: Coordinate(165, 91, 12), 3: Coordinate(165, 185.5, 12)}  # ABSOLUTE values

    tool_offsets = {0: Coordinate(0, 0, 0), 1: Coordinate(0, 0, 0), 2: Coordinate(0, 0, 0), 3: Coordinate(0, 0, 0)}  #TODO: find this value ASAP, 

    tool = get_tool_func(X_latch_offset_distance_in, X_latch_offset_distance_out, tool_home_coordinates, tool_offsets, attach_detach_time)

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
    # Tip Thickness in mm
    tip_thickness = 4

    ### Laser Module Tweaking Values
    # Z positions
    optimum_laser_Z_position = 16  # 44mm from laser head to PCB
    # Feedrates
    pcb_trace_feedrate = 600
    # Power intensities
    laser_power = 150 


    ### Main Code ###
    # Read the gerber file
    gerber = Gerber(gerber_file_path)

    # Recenter Gerber File with wanted Offset
    gerber.recenter_gerber_file(user_x_offset, user_y_offset)

    gcode = ''

    # Creating the holes_gcode
    gcode += generate_holes_gcode(gerber, tool, router_Z_up_position, router_Z_down_position, router_feedrate_XY, router_feedrate_Z, spindle_speed, terminate_after = False)

    # Creating the PCB ink laying Gcode
    gcode += generate_ink_laying_gcode(gerber, tool, tip_thickness, pen_down_position, ink_laying_feedrate, initiated_before=True, terminate_after = False)

    # Creating the PCB trace laser Toner Transfer Gcode
    gcode += generate_pcb_trace_gcode(gerber, tool, optimum_laser_Z_position, pcb_trace_feedrate, laser_power, initiated_before=True)

    # exporting the created Gcode
    export_gcode(gcode, gcode_file_path)

    
