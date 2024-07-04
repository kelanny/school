#!/usr/bin/env python3
""" Console module """

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command when an empty line is entered.
        """
        pass

    def do_help(self, arg):
        """
        Provides help for commands.
        """
        if arg:
            # If specific command help is requested, call default help
            return super().do_help(arg)
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF   quit   help")
            print("\nType 'help <command>' to see more details about a specific command.")
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        
        try:
            model_class = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        
        new_instance = model_class()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        print(all_objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        del all_objs[key]
        storage.save()
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [class name]
        """
        all_objs = storage.all()
        
        if not arg:
            print([str(obj) for obj in all_objs.values()])
            return
        
        try:
            model_class = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        
        print([str(obj) for key, obj in all_objs.items() if key.startswith(model_class.__name__)])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        
        if len(args) < 3:
            print("** attribute name missing **")
            return
        
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_name = args[2]
        attribute_value = args[3]
        
        setattr(all_objs[key], attribute_name, attribute_value)
        all_objs[key].save()



        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
