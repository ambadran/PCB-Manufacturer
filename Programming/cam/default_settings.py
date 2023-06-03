from data_structures import Coordinate

default_settings_dict = {

    # Offset PCB from (0, 0)
    "user_x_offset": 2,
    "user_y_offset": 2,

    ### Tool Home positions and latch offset (as absolute values)
    "X_latch_offset_distance_in": 188,  # ABSOLUTE value
    "X_latch_offset_distance_out": 92,  # ABSOLUTE value
    "attach_detach_time": 5, # the P attribute in Gcode is in seconds
    "tool_home_coordinates": {1: Coordinate(165, 0, 11), 
                            2: Coordinate(165, 91, 12), 
                            3: Coordinate(165, 185.5, 12)},  # ABSOLUTE values

    "tool_offsets": {0: Coordinate(0, 0, 0), 
                   1: Coordinate(0, 0, 0), 
                   2: Coordinate(0, 0, 0), 
                   3: Coordinate(0, 0, 0)},  #TODO: find this value ASAP, 


    ### spindle tweaking values
    # Z positions
    "router_Z_up_position": 20,
    "router_Z_down_position": 25,
    # Feedrates
    "router_feedrate_XY": 700,
    "router_feedrate_Z": 10,
    # Power intensities
    "spindle_speed": 230,

    ### Pen Tweaking Values
    # Z positions
    "pen_down_position": 10,
    # Feedrates
    "ink_laying_feedrate": 100,
    # Tip Thickness in mm
    "tip_thickness": 4,

    ### Laser Module Tweaking Values
    # Z positions
    "optimum_laser_Z_position": 16,  # 44mm from laser head to PCB
    # Feedrates
    "pcb_trace_feedrate": 600,
    # Power intensities
    "laser_power": 150,

    # destination
    'dest': 'test.gcode',

    # mirrored
    'mirrored': False,

    # Gcode Modes
    'all_gcode': False,
    'ink': False,
    'laser': False,
    'holes': False

}


