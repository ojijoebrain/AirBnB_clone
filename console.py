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

    def do_create(self, val):
        """ Creates a new instance of the basemodel and save to json file """
        if len(val) == 0:
            print("** class name missing **")
        
        else:
            try:
                instance = eval(val)()
                instance.save()
                print(instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, val):
        """ prints the string representation of an instatnce """
        if len(val) == 0:
            print("** class name missing **")
        else:
            values = val.split()
            if len(values) < 2:
                print('** instance id missing **')
            else:
                try:
                    instance = eval(values[0]).get(values[1])
                    if instance:
                        print(instance)
                    else:
                        print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")
    
    def do_destroy(self, val):
        """ deletes an instance of a class using its id"""
        if len(val) == 0:
            print("** class name missing **")
        else:
            values = val.split()
            if len(values) < 2:
                print("** instance id missing **")
            else:
                try:
                    instances = eval(values[0]).all()
                    if instances:
                        instance = instances.get(values[1])
                        if instance:
                            del instance
                            BaseModel.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** class doesn't exist **")
                except NameError:
                    print("** class doesn't exist **")

    def do_all(self, val):
        """ prints all string representation of all instances """
        try:
            if val:
                instances = eval(val).all()
            else:
                instances = BaseModel.all()
            if instances:
                print([str(instance) for instance in instances])
            else:
                print("[]")
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, val):
        """ 
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
