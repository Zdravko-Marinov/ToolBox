import os

#Class with variables to use
class Vars:
    def __init__(self):
        self.on_error = False
        self.command_str = ""



Vars_ = Vars()
target = "" # ip url etc

is_stealth = False
is_aggressive = False
is_heavy = False

prefix_command = "whatweb "


def execute_command():
    os.system(Vars_.command_str)
    print(Vars_.command_str)

#Function for setting up the scan mode
def scan_mode():

    if(is_stealth):
        return " -a 1"
    if(is_aggressive):
        return " -a 3"
    if(is_heavy):
        return " -a 4"
    
    return ""

#Function that builds the command
def command_builder():
    Vars_.command_str = prefix_command

# Add target into command string
    if(target != ""):
        Vars_.command_str += target
    else:
        Vars_.on_error = True ## error code

# Add Scan mode
    Vars_.command_str += scan_mode()

    if(Vars_.on_error == False):
        execute_command()