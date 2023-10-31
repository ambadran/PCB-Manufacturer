from data_structures import Coordinate

default_settings_dict = {

    # Offset PCB from (0, 0)
    "x_offset": 2,
    "y_offset": 2,

    ### Tool Home positions and latch offset (as absolute values)
    "X_latch_offset_distance_in": 188,  # ABSOLUTE value
    "X_latch_offset_distance_out": 92,  # ABSOLUTE value
    "attach_detach_time": 5, # the P attribute in Gcode is in seconds
    "tool_home_coordinates": {1: Coordinate(165, 0, 10.5), 
                            2: Coordinate(165, 91, 12), 
                            3: Coordinate(165, 185.5, 12)},  # ABSOLUTE values

    "tool_offsets": {0: Coordinate(0, 0, 0), 
                   1: Coordinate(0, 0, 0), 
                   2: Coordinate(0, 0, 0), 
                   3: Coordinate(0, 0, 0)},  #TODO: find this value ASAP, 


    ### spindle tweaking values
    # Z positions
    "router_Z_up_position": 10,
    "router_Z_down_position": 13,
    # Feedrates
    "router_feedrate_XY": 600,
    "router_feedrate_Z_drilling": 1,
    "router_feedrate_Z_up_from_pcb": 20,
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
    # Include edge cut in pcb laser marking
    "include_edge_cuts": True,
    # Laser Gcode Passes
    "laser_passes": 1,
    # Show laser Gcode Creation Debugging info and visualization :)
    'debug_laser': False,

    # destination
    'dest': './default.gcode',


    # mirrored
    'mirrored': False,

    # Gcode Modes
    'all_gcode': False,
    'ink': False,
    'laser': False,
    'holes': False,


}


