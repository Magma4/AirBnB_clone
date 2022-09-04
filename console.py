#!/usr/bin/python3
"""this is the console for AirBnB"""

import cmd
import sys
import json
import os
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """this class defines a console object
    """
    prompt = '(hbnb)'

    def do_quit(self, *args):
        """quits the interpreter"""
        return True

    def do_EOF(self, obj):
        """EOF exits the program"""
        print()
        return True

    def emptyline(self):
        return

    def do_create(self, arg):
        """creates a new object and saves it"""
        cmds = self.parseline(arg)
        listclasses = ["BaseModel", "User", "Place", "City", "State", "Review"\
                       , "Amenity"]
        if cmds[2] == '':
            print("** class name missing **")
            return
        list_of_cmds = cmds[2].split(" ")
        if list_of_cmds[0] in listclasses:
            if list_of_cmds[0] == "BaseModel":
                new = BaseModel()
            elif list_of_cmds[0] == "User":
                new = User()
            elif list_of_cmds[0] == "Place":
                new = Place()
            elif list_of_cmds[0] == "City":
                new = City()
            elif list_of_cmds[0] == "State":
                new = State()
            elif list_of_cmds[0] == "Review":
                new = Review()
            elif list_of_cmds[0] == "Amenity":
                new = Amenity()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id
        """
        cmds = self.parseline(arg)
        listclasses = ["BaseModel", "User"]
        if cmds[2] == '':
            print("** class name missing **")
            return
        list_of_cmds = cmds[2].split(" ")
        lenth_of_cmds = len(list_of_cmds)
        if list_of_cmds[0] not in listclasses:
            print("** class doesn't exist **")
            return
        if lenth_of_cmds == 1:
            print("** instance id missing **")
            return
        if os.path.exists("file.json"):
            with open("file.json", "r", encoding="utf-8") as f:
                dic = json.loads(f.read())
                for key, value in dic.items():
                    same_class = (dic[key])['__class__'] == list_of_cmds[0]
                    if (dic[key])['id'] == list_of_cmds[1] and same_class:
                        if (dic[key])['__class__'] == "BaseModel":
                            print(BaseModel(**value))
                        elif (dic[key])['__class__'] == "User":
                            print(User(**value))
                        return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        cmds = self.parseline(arg)
        listclasses = ["BaseModel", "User"]
        if cmds[2] == '':
            print("** class name missing **")
            return
        list_of_cmds = cmds[2].split(" ")
        lenth_of_cmds = len(list_of_cmds)
        if list_of_cmds[0] not in listclasses:
            print("** class doesn't exist **")
            return
        if lenth_of_cmds == 1:
            print("** instance id missing **")
            return
        if os.path.exists("file.json"):
            with open("file.json", "r", encoding="utf-8") as f:
                dic = json.loads(f.read())
                for key, value in dic.items():
                    same_class = (dic[key])['__class__'] == list_of_cmds[0]
                    if (dic[key])['id'] == list_of_cmds[1] and same_class:
                        del(dic[key])
                        break
            with open("file.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(dic))
                return
        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the class name
        """
        cmds = self.parseline(arg)
        listclasses = ["BaseModel", "User"]
        if cmds[2] != '':
            list_of_cmds = cmds[2].split(" ")
            if list_of_cmds[0] not in listclasses:
                print("** class doesn't exist **")
                return
        objlist = []
        if os.path.exists("file.json"):
            with open("file.json", "r", encoding="utf-8") as f:
                obj = json.loads(f.read())
                for key, value in obj.items():
                    if value['__class__'] == "BaseModel":
                        objlist.append(str(BaseModel(**value).__str__()))
                    elif value['__class__'] == "User":
                        objlist.append(str(User(**value).__str__()))
        print(objlist)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or updating attribute
        """
        cmds = self.parseline(arg)
        listclasses = ["BaseModel", "User"]
        if cmds[2] == '':
            print("** class name missing **")
            return
        list_of_cmds = shlex.split(cmds[2])
        lenth_of_cmds = len(list_of_cmds)
        if list_of_cmds[0] not in listclasses:
            print("** class doesn't exist **")
            return
        if lenth_of_cmds == 1:
            print("** instance id missing **")
            return
        if os.path.exists("file.json"):
            with open("file.json", "r", encoding="utf-8") as f:
                dic = json.loads(f.read())
                for key, value in dic.items():
                    same_class = (dic[key])['__class__'] == list_of_cmds[0]
                    if same_class and ((dic[key])['id'] == list_of_cmds[1]):
                        if lenth_of_cmds < 3:
                            print("** attribute name missing **")
                            return
                        if lenth_of_cmds < 4:
                            print("** value missing **")
                            return

                        stripped = list_of_cmds[3]
                        (dic[key])[list_of_cmds[2]] = stripped
                        with open("file.json", "w", encoding="utf-8") as f:
                            f.write(json.dumps(dic))
                            return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
