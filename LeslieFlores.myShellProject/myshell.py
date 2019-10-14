# Leslie Flores - Final Project: Building a Shell
# Part of the foundation of this code is from
# https://danishprakash.github.io/2018/09/27/shell-in-python.html

import os
import subprocess

from list_dir import *
from change_dir import *
from help_manual import *
from execute_cmd import *

def main(): # the primary function for this project
    while True:
        command = input("$ ")
        if command[:4] == "dir ": # used to list contents in directory
            list_dir(command[4:])
        elif command[:3] == "cd ": # used to change directory
            change_dir(command[3:])
        elif command[:5] == "echo ": # used to check the comment/command
            print(command[5:])
        elif command == "environ": # used to list all the environment strings
            print(os.environ)
        elif command == "help": # used to display the user manual with a filter
            help_manual()
        elif command == "pause": # used to pause the operation of the shell
            pause = input("Please press ENTER to continue. ")
        elif command == "clr": # used for clearing screen
            os.system('clear')
        elif command == "quit": # used to quit the shell
            break
        else:
            execute_cmd(command) # if cmd not listed above then moving along


if '__main__' == __name__:
    main()
