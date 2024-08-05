#!/usr/bin/python3
""" The Airbnb console Project """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary of available classes
entity_classes = {
    "Amenity": Amenity, "BaseModel": BaseModel, "City": City,
    "Place": Place, "Review": Review, "State": State, "User": User
}

class AirbnbCommand(cmd.Cmd):
    """ The Airbnb Console """
    prompt = '(HBNB) '

    def do_exit(self, arg):
        """ Exit the console """
        return True

    def emptyline(self):
        """ Override the emptyline method to do nothing """
        return False

    def do_quit(self, arg):
        """ Exit the console """
        return True

    def parse_key_value(self, arguments):
        """ Parse the key-value pairs from the argument list """
        parsed_dict = {}
        for arg in arguments:
            if "=" in arg:
                key, value = arg.split('=', 1)
                if value.startswith('"') and value.endswith('"'):
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                parsed_dict[key] = value
        logging.debug(f"Parsed dictionary: {parsed_dict}")
        return parsed_dict

    def do_create(self, arg):
        """ Creates a new instance of a class """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return False
        if args[0] in entity_classes:
            new_attributes = self.parse_key_value(args[1:])
            instance = entity_classes[args[0]](**new_attributes)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ Prints an instance based on the class and id """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return False
        if args[0] in entity_classes:
            if len(args) > 1:
                instance_key = f"{args[0]}.{args[1]}"
                if instance_key in models.storage.all():
                    print(models.storage.all()[instance_key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class and id """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in entity_classes:
            if len(args) > 1:
                instance_key = f"{args[0]}.{args[1]}"
                if instance_key in models.storage.all():
                    del models.storage.all()[instance_key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representations of instances """
        args = shlex.split(arg)
        instance_list = []
        if not args:
            all_instances = models.storage.all()
        elif args[0] in entity_classes:
            all_instances = models.storage.all(entity_classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in all_instances:
            instance_list.append(str(all_instances[key]))
        print("[", end="")
        print(", ".join(instance_list), end="")
        print("]")

    def do_update(self, arg):
        """ Update an instance based on the class name, id, attribute & value """
        args = shlex.split(arg)
        integer_attributes = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]
        float_attributes = ["latitude", "longitude"]
        if not args:
            print("** class name missing **")
        elif args[0] in entity_classes:
            if len(args) > 1:
                instance_key = f"{args[0]}.{args[1]}"
                if instance_key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integer_attributes:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in float_attributes:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[instance_key], args[2], args[3])
                            models.storage.all()[instance_key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
