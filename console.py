#!/usr/bin/python3
"""
This is the entry point for the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    This class implements quit, end of line (EOF) and help commands
    """
<<<<<<< HEAD
    prompt = "hbnb"
    valid_classes = ["BaseModel]", "User"]

=======
    prompt = "(hbnb) "

    models = ["BaseModel", "User", "State", "City", "Amenity",
              "Place", "Review"]
>>>>>>> 67c617e55efc3fafebfbdbdb40ba96e0e6a4f2a0

    def do_quit(self, val):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ displays the prompt if no command is typed """
        pass

    def do_EOF(self, val):
        """ This is the EOF method """
        print('')
        return True

    def do_create(self, val):
        """ Creates a new instance of the basemodel and save to json file """
        if len(val) == 0:
            print("** class name missing **")
        else:
            try:
<<<<<<< HEAD
                values = val.split(f"{commands[0]()}")
                storage.save()
                instance = BaseModel()
                instance.save()
=======
                values = val.split()
                instance = eval(f"(values[0])()")
                storage.save()
>>>>>>> 67c617e55efc3fafebfbdbdb40ba96e0e6a4f2a0
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
                    obj = storage.all()
                    Key = eval(values[0]).get(values[1])
                    if key in obj:
                        print(key)
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
                    obj = storage.all()
                    key = eval(values[0]).get(values[1])
                    if key in obj:
                        del instance
                        storage.save()
                    else:
                        print("** no instance found **")
                except NameError:
                    print("** class doesn't exist **")

    def do_all(self, val):
        """ prints all string representation of all instances """
        try:
            obj = storage.all()
            values = val.split()
            if len(values) == 0:
                for key, value in obj.items():
                    print(str(value))
            else:
                for key, value in obj.items():
                    if key.split(".")[0] == values[0]:
                        print(str(value))
                print([str(instance) for instance in instances])
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
