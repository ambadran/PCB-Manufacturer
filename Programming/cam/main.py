'''
#TODO: The MOST IMPORTANT TASK NOW is to implement something to prevent choosing a tool when a tool is already mounted
PCB manufacturer CAM program

My custom Gcode Generator :)))
'''

from gerber_tools import *
from gcode_tools import *
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import json

class Settings:
    '''
    Class to make it easier to call and manipulate settings
    '''
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
        "laser_power": 150
    }

    def __init__(self):
        self.settings_dict = {}

    def __getattr__(self, key):
        if key not in self.settings_dict:
            return self.default_settings_dict[key]

        else:
            return self.settings_dict[key]

    @property
    def tool(self):
        return get_tool_func(self.X_latch_offset_distance_in, self.X_latch_offset_distance_out, self.tool_home_coordinates, self.tool_offsets, self.attach_detach_time)

# Initiating DefaultSettings object
settings = Settings()

### Creating the CLI argument parser
parser = ArgumentParser(description="Generates Custom Gcode Required by my PCB Manufacturing Machine :)", 
        formatter_class=ArgumentDefaultsHelpFormatter)

### Adding the positional arguments
parser.add_argument('src', help="Source Gerber file to be converted to Gcode")

### Adding keyword Arguments
parser.add_argument('-D', '--dest', default="./pcb_gcode.nc", help="Destination Gcode file")
parser.add_argument("-M", "--mirrored", default=False, type=bool, help="Mirror Given Srouce Gerber file. Used for traces of DIP components")
for key, value in Settings.default_settings_dict.items():
    parser.add_argument(f"--{key}", default=value, type=type(value), help="self-explained")

### Extracting User inputs!
settings.settings_dict.update(vars(parser.parse_args()))

### Executing the Program!
### Main Code ###
# Read the gerber file
gerber = Gerber(file_path=settings.src)

# Recenter Gerber File with wanted Offset
gerber.recenter_gerber_file(settings.user_x_offset, settings.user_y_offset)

gcode = ''

# Creating the holes_gcode
gcode += generate_holes_gcode(gerber, settings.tool, settings.router_Z_up_position, 
                              settingsrouter_Z_down_position, settings.router_feedrate_XY, 
                              settings.router_feedrate_Z, settings.spindle_speed, 
                              terminate_after = False)

# Creating the PCB ink laying Gcode
gcode += generate_ink_laying_gcode(gerber, settings.tool, settings.tip_thickness, 
                                   settings.pen_down_position, settings.ink_laying_feedrate, 
                                   initiated_before=True, terminate_after = False)

# Creating the PCB trace laser Toner Transfer Gcode
gcode += generate_pcb_trace_gcode(gerber, settings.tool, settings.optimum_laser_Z_position, 
                                  settings.pcb_trace_feedrate, settings.laser_power, 
                                  initiated_before=True)

# exporting the created Gcode
export_gcode(gcode, settings.dest)

