#!/usr/bin/python3
"""
This is the entry point for the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class implements quit, end of line (EOF) and help commands
    """
    prompt = "hbnb"

    def do_quit(self, val):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ displays the prompt if no command is typed """
        pass

    def do_EOF(self, val):
        """ This is the EOF method """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
