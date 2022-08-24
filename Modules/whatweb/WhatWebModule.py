import os

target = "" # ip url etc
exportFile = False

is_stealth = False
is_aggressive = False
is_heavy = False

prefix_command = "whatweb "
command_str = "whatweb "

def command_builder():
    command_str = prefix_command

def execute_command():
    os.system(command_str)