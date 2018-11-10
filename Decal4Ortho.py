"""Decal4Ortho.

Usage:
  Decal4Ortho.py [--decal DECAL] [--remove DECAL | --remove-all | --replace DECAL] [--ex-com COMMAND]... [options] (DIRECTORY...)
  Decal4Ortho.py (-h | --help)
  Decal4Ortho.py --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --decal DECAL        Decal to apply. Suggested decals to try are:
                       DEFAULT (lib/g10/decals/maquify_1_green_key.dcl)
                       lib/g10/decals/grass_and_asphalt_green_key.dcl
  --remove DECAL       Remove the specified decal
  --remove-all         Remove all decals
  --replace DECAL      Replace this decal with the specified decal.
  --ex-com COMMAND     Exclude files with these commands [default: WET]
                       Set to NONE if you don't wish to exclude any files.
  --extension EXT      File extension to apply changes to [default: ter]   
  --debug              Print debug info   

"""
from docopt import docopt
import os

DECAL_COMMAND = "DECAL_LIB"
DEFAULT_DECAL = "lib/g10/decals/maquify_1_green_key.dcl"


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Decal4Ortho 0.1')

    DEBUG = arguments["--debug"]
    DEBUG = True

    # if DEBUG:
    print(arguments)

    extension = arguments["--extension"].lower()
    filepaths = []

    for directory in arguments["DIRECTORY"]:
        for dirpath, dirnames, files in os.walk(directory):
            for fname in files:
                if fname.lower().endswith(extension):
                    filepaths.append(os.path.join(dirpath, fname))
    
    for fpath in filepaths:
        if DEBUG:
            print("Opening: ", fpath)

        read_file = open(fpath, 'r')
        data = read_file.read()
        read_file.close()

        data_lines = data.split("\n")
        new_data_lines = []

        exclude_file = False

        for line in data_lines:
            include_line = True

            for command in arguments["--ex-com"]:
                if command != "NONE" and command in line:
                    if DEBUG:
                        print("Excluding file because it contains", command)

                    exclude_file = True
                    break

            if DECAL_COMMAND in line:
                if arguments["--remove-all"]:
                    include_line = False

                if arguments["--remove"] is not None:
                    remove_decal = arguments["--remove"]
                    if remove_decal in line:
                        include_line = False

                if arguments["--replace"] is not None:
                    replace_decal = arguments["--replace"]
                    if replace_decal in line:
                        new_line = DECAL_COMMAND + " " + arguments["--decal"]
                        if DEBUG:
                            print("Replacing: ", line, " with ", new_line)
                        line = new_line
                        include_line = True

            if include_line:
                new_data_lines.append(line)
            else:
                if DEBUG:
                    print("Removing decal: ", line)

        if arguments["--decal"] is not None and not exclude_file:
            decal = arguments["--decal"]

            if decal == "DEFAULT":
                decal = DEFAULT_DECAL

            new_line = DECAL_COMMAND + " " + decal
            if DEBUG:
                print("Adding decal: ", new_line)
            new_data_lines.append(new_line)


        if not exclude_file:
            new_data = "\n".join(new_data_lines)
            
            if DEBUG:
                print("Writing final file:")
                print(new_data)

            os.remove(fpath)

            write_file = open(fpath, 'w')
            write_file.write(new_data)
            write_file.close()

        if DEBUG:
            print()