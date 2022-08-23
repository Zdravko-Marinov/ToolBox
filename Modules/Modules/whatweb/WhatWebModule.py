import os

target = "" # ip url etc
exportFile = False

command_str = "whatweb "

def execute_Command():
    os.system(command_str + target)