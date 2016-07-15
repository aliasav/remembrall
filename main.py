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
from docopt import docopt, DocoptExit
from initializer import entry

def get_args():
    try:
        arguments = docopt(__doc__)
    except DocoptExit as e:
        print("Invalid Command, refer to the manual!")
        print(e)    
    except Exception as e:        
        print("Invalid Command, refer to the manual!")
        print(e)    
    else:        
        #print(arguments)
        return arguments

def console_entry():
    """Entry point for console scripts"""
    args = get_args()
    entry()

if __name__ == '__main__':
    args = get_args()
