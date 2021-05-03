import sys
import os.path

options = []
files = []

def lecture_argv():
    mutually_exlcusive = 0
    for arg in sys.argv:
        if "--" in arg:
            if (arg == "--upper" or arg == "--lower") and mutually_exlcusive == 0:
                mutually_exlcusive = 1
                options.append(arg)
            elif (arg == "--upper" or arg == "--lower") and mutually_exlcusive == 1:
                print("Error mutually exclusive : you can't use --upper and --lower ")
                return -1
            else:
                options.append(arg)
        else :
            if ".py" not in arg:
                files.append(arg)

    print(options)
    print(files)

def core_application():
    if strict_mode() == -1:
        return -1

    for file in files:
        file_name = file.split(".")[0]
        openFile = open(file, "r")
        for option in options:
            if option == "--verbose":
                print(f"# processing file {file_name}")
            elif option == "--upper":
                for line in openFile.readlines():
                    print(line.upper())
            elif option == "--lower":
                for line in openFile.readlines():
                    print(line.decode('utf-8').lower())

def strict_mode():
    if "--strict" in options:
        for file in files:
            if not os.path.exists(file):
                print(f"Error : {file} file not exist")
                return -1
    else :
        for file in files:
            if not os.path.exists(file):
                files.remove(file)
                print(files)

lecture_argv()
core_application()

