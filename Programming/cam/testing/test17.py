    parser.add_argument('-D', '--dest', default=default_settings_dict['dest'], help="Destination Gcode file\n")
    parser.add_argument("-M", "--mirrored", default=default_settings_dict['mirrored'], type=bool, help="Mirror Given Srouce Gerber file. Used for traces of DIP components\n")
    parser.add_argument("--x-offset", default=default_settings_dict['x_offset'], type=int, help="Value PCB offseted from Y axis\n")
    parser.add_argument("--y-offset", default=default_settings_dict['y_offset'], type=int, help="Value PCB offseted from X axis\n")
    parser.add_argument("-ALL", "--all-gcode", default=default_settings_dict['all_gcode'], help="Creates a Gcode file with hole drilling gcode, ink laying gcode and laser drawing gcode\n")
    parser.add_argument("--holes", default=default_settings_dict['holes'], help="Adds hole drilling gcode to Gcode file\n")
    parser.add_argument("--ink", default=default_settings_dict['ink'], help="Adds ink laying gcode to Gcode file\n")
    parser.add_argument("--laser", default=default_settings_dict['laser'], help="Adds laser drawing gcode to Gcode file\n")
    parser.add_argument("--debug-laser", default=default_settings_dict['debug_laser'], help="Shows Simulation of the PCB laser trace coordinates\n")
    # I am not adding those instead they have to be changed in the configuration file
    # for key, value in Settings.default_settings_dict.items():
    #     parser.add_argument(f"--{key}", default=value, type=type(value), help="self-explained")


