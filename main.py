"""
Remembrall: A To-Do list that sned terminal reminders

Usage:  
    main.py init
    main.py show [<function1>]
    main.py add [id]
    main.py (-h | --help)

Examples:
    main.py list add "Gotta catch a Pikachu!"
    main.py list remove <id>
    main.py init
  

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
        remembrall = Remembrall()
        remembrall.init_remembrall()
        if args.get("init", False) == True:
            print("Initializing sequence completed!")
        elif args.get("show", False) == True:
            todo = ToDoList(remembrall)
            todo.fetch_list_data()
            func1 = args.get("<function1>", None)
            if func1 == "ids":
                todo.list_items(True)
            else:
                todo.list_items(False)
        elif args.get("add", False) == True:
            id = args.get("id", None)            
            todo = ToDoList(remembrall)
            todo.fetch_list_data()            
            todo.add_item()            

def console_entry():
    """ Entry point for console scripts """
    args_remembrall_mapper(get_args())

if __name__ == '__main__':
    args_remembrall_mapper(get_args())
