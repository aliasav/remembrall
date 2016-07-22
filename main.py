"""
Remembrall: A terminal to-do list and reminder.

Usage:  
    remembrall init
    remembrall show [<function1>]
    remembrall add
    remembrall edit [<id>]
    remembrall delete [<id>]
    remembrall clear
    remembrall remind [<action>]
    remembrall (-h | --help)

Examples:
    remembrall list add "Gotta catch a Pikachu!"
    remembrall list remove <id>
    remembrall init
  

Options:
    -h, --help

"""
from docopt import docopt, DocoptExit, Dict
from initializer import entry, Remembrall, CronJob
from list import ToDoList

def get_args():
    try:
        arguments = docopt(__doc__)        
    except DocoptExit as e:
        print("Invalid Command, refer to the manual!")
        print(e)  
        return None  
    except Exception as e:        
        print("Invalid Command, refer to the manual!")
        print(e)
        return None 
    else:        
        #print(arguments)
        return arguments

def args_remembrall_mapper(args):
    """ maps arguments to Remembrall's functions """    
    if args and (type(args) == Dict):

        # initialize remembrall and list
        remembrall = Remembrall()
        remembrall.init_remembrall()
        cron = CronJob(remembrall)
        todo = ToDoList(remembrall)
        todo.fetch_list_data()
        
        # map args to functions
        if args.get("init", False) == True:
            cron.set_cron(True)
            print("Initializing sequence completed!\n")
        # show: display items
        elif args.get("show", False) == True:            
            func1 = args.get("<function1>", None)
            if func1 == "ids":
                todo.list_items(True)
            else:
                todo.list_items(False)
        # add: add to list
        elif args.get("add", False) == True:
            todo.add_item()
        # edit: edit item in list
        elif args.get("edit", False) == True:
            id = args.get("<id>", None)
            todo.edit_item(id) 
        # delete: deletes item in list
        elif args.get("delete", False) == True: 
            id = args.get("<id>", None)
            todo.delete_item(id)
        # clear: clear list
        elif args.get("clear", False) == True:
            todo.clear_list() 
        # remind functions
        elif args.get("remind", False) == True:
            action = args.get("<action>", None)
            if action:
                if action == "clear":
                    cron.remove_cron()
                elif action == "reset":
                    cron.set_cron(True)

def console_entry():
    """ Entry point for console scripts """
    args_remembrall_mapper(get_args())

if __name__ == '__main__':
    args_remembrall_mapper(get_args())
