from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from main import Settings, main

if __name__ == '__main__':
    # Initiating Settings object
    settings = Settings()

    ### Creating the CLI argument parser
    parser = ArgumentParser(description="Generates Custom Gcode Required by my PCB Manufacturing Machine :)", 
            formatter_class=ArgumentDefaultsHelpFormatter)

    ### Adding the positional arguments
    parser.add_argument('src', help="Source Gerber file to be converted to Gcode\n")

    ### Adding keyword Arguments
    parser.add_argument('-D', '--dest', default="./pcb_gcode.nc", help="Destination Gcode file\n")
    parser.add_argument("-M", "--mirrored", default=False, type=bool, help="Mirror Given Srouce Gerber file. Used for traces of DIP components\n")
    parser.add_argument("-ALL", "--all-gcode", default=False, type=bool, help="Creates a Gcode file with hole drilling gcode, ink laying gcode and laser drawing gcode\n")
    parser.add_argument("--holes", default=False, type=bool, help="Adds hole drilling gcode to Gcode file\n")
    parser.add_argument("--ink", default=False, type=bool, help="Adds ink laying gcode to Gcode file\n")
    parser.add_argument("--laser", default=False, type=bool, help="Adds laser drawing gcode to Gcode file\n")
    # I am not adding those instead they have to be changed in the configuration file
    # for key, value in Settings.default_settings_dict.items():
    #     parser.add_argument(f"--{key}", default=value, type=type(value), help="self-explained")

    ### Extracting User inputs!
    # Getting arguments
    settings.settings_dict.update(vars(parser.parse_args()))


    ### Executing the Program!
    main(settings)

