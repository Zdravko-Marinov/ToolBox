import os

target = "" # ip url etc
exportFile = False

is_stealth = False
is_aggressive = False
is_heavy = False

command_str = "whatweb "

def execute_Command():
    os.system(command_str + target)