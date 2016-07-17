"""
Remembrall: A To-Do list that sned terminal reminders

Usage:  
    main.py init
    main.py list <function> [id]
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
        if args.get("init", None) == True:
            print("Initialising Remembrall in your system!")
            remembrall = Remembrall()
            remembrall.init_remembrall()
            cron = CronJob(remembrall)

def console_entry():
    """ Entry point for console scripts """
    args_remembrall_mapper(get_args())

if __name__ == '__main__':
    args_remembrall_mapper(get_args())
