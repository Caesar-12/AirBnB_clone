#!/usr/bin/python3

"""
contains the entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    CLI class
    """

    avail_class = ('BaseModel')
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Execute nothing"""
        pass

    def do_create(self, line):
        """Create: creates a new instance """
        if line not in self.avail_class:
            print("** class doesn't exist **")
        elif len(line) == 0:
            print("** class name missing **")
        else:
            newObj = eval("{}()".format(line))
            newObj.save()
            print(newObj.id)

    def do_show(self, line):
        """show: prints string representation of an instance"""
        comm = line.split()
        if len(comm) == 0:
            print("** class name missing **")
            return False
        elif len(comm) < 2:
            print("** instance id missing **")
            return False
        elif comm[0] not in self.avail_class:
            print("** class doesn't exist **")
            return False

        all_objs = storage.all()
        key = "{}.{}".format(comm[0], comm[1])
        for obj_id in all_objs.keys():
            if key == obj_id:
                obj = all_objs[obj_id]
                print(obj)
                return False
        print("** no instance found **")

    def do_destroy(self, line):
        """destroy: deletes an instance"""
        comm = line.split()

        if len(comm) == 0:
            print("** class name missing **")
            return False
        elif comm[0] not in self.avail_class:
            print("** class doesn't exist**")
            return False
        elif len(comm) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        key = "{}.{}".format(comm[0], comm[1])
        for obj_id in all_objs.keys():
            if key == obj_id:
                del all_objs[obj_id]
                storage.save()
                return False
        print("** no instance found **")

    def do_all(self, line):
        """all: displays all instances representaion"""
        comm = line.split()
        if len(comm) == 1 and comm[0] not in self.avail_class:
            print("** class doesn't exist **")
        all_objs = storage.all()
        obj_list = []
        for obj_id in all_objs.keys():
            obj_list.append(all_objs[obj_id].__str__())
        print(obj_list)

    def do_update(self, line):
        """update: initializes instances attributes"""
        comm = line.split()
        if len(comm) == 0:
            print("** class name missing **")
            return False
        elif comm[0] not in self.avail_class:
            print("** class name missing **")
            return False
        elif len(comm) < 2:
            print("** instance id missing **")
            return False
        elif len(comm) < 3:
            print("** attribute name missing **")
            return False
        elif len(comm) < 4:
            print("** value missing **")
            return False
        all_objs = storage.all()
        key = "{}.{}".format(comm[0], comm[1])
        try:
            obj = all_objs[key]
        except KeyError:
            print("** no instance found **")
            return False
        if comm[3].isdigit():
            setattr(obj, comm[2], int(comm[3]))
            storage.save()
        else:
            try:
                setattr(obj, comm[2], float(comm[3]))
                storage.save()
            except:
                setattr(obj, comm[2], str(comm[3]))
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
