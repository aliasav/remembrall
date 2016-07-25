"""
Initialises remembrall files for user
"""
import sys
import os
import json
import subprocess
import traceback
from constants import *
from future.utils import lmap
from builtins import input
from crontab import CronTab

class Remembrall():
	"""
		Remembrall initialiser
		Creates a hidden remembrall folder in User's home folder.
		Config JSON file created with user's information 
	"""
	def __init__(self):
		self.home_dir = None
		self.tty = None
		self.remembrall_config = None
		self.todo_file = None
		self.remembrall_home = None
		self.which_remembrall = None

	def init_remembrall(self):
		""" 
		initializes remembrall system:
			sets-up remmebrall folder and config file
			sets-up crontab
		"""
		self.init_vars()
		if not self.check_init():
			self.create_remembrall_folder()
			self.create_config()
		else:			
			#print("Remembrall already initialized, you're good to go!")
			pass

	def init_vars(self):
		self.home_dir = self.get_home_dir()
		self.tty = self.get_tty()
		self.remembrall_home = self.get_remembrall_home()	
		self.remembrall_config = self.get_remembrall_config_file_data()	
		#self.which_remembrall = self.get_which_remembrall()

	def get_home_dir(self):
		""" returns user's home directory path """
		try:
			home_dir = os.path.expanduser("~")
		except Exception as e:
			print("Couldn't get home directory! :(")
			print(e)
			sys.exit(1)
		else:
			return home_dir

	def get_tty(self):
		""" Finds terminal to direct output to. 
			Will be used to set crontab """

		try:
			output = subprocess.check_output("who")
			#print(output)
		except Exception as e:
			print("Couldn't get tty output! :(")
			print(e)
			traceback.print_exc()
			sys.exit(1)
		else:
			active_ttys = self.process_tty_output(output)
			#print("active_ttys: %s" %active_ttys)
			self.active_ttys = active_ttys
			return active_ttys

	def process_tty_output(self, o):
		""" process 'who' cmd output and return 
		list of active ttys """
		clean = o.lstrip().rstrip()
		if (type(clean)==type(b'')):
			clean = clean.decode("utf-8")
		clean_list = clean.split("\n")[1:]
		active_ttys = lmap(lambda x: x.split()[1], clean_list)		
		return active_ttys

	def get_remembrall_home(self):
		""" returns path of remembrall home directory"""
		return self.home_dir + "/.remembrall"

	def get_which_remembrall(self):
		output = subprocess.check_output(["which", "remembrall"])
		if type(output)==type(b""):
			output = output.decode("utf-8")
		output = output.lstrip().rstrip().replace("\n", "")
		return output

	def create_remembrall_folder(self):		
		""" creates remembrall home dir """
		if not os.path.exists(self.remembrall_home):
			print("Creating remembrall home directory!")
			os.makedirs(self.get_remembrall_home())
		else:
			print("Seems like Remembrall already exists!")

	def create_config(self):
		""" creates config JSON files """		
		home = self.get_remembrall_home()
		self.remembrall_config = self.get_remembrall_config_input()
		# create config file
		with open(home + "/" + REMEMBRALL_CONFIG_FILE, "w") as config_file:			
			json.dump(self.remembrall_config, config_file, indent=4)

		# create to-do list file
		with open(home + "/" + TODO_LIST_FILE, "w") as todo_file:
			json.dump({"items": [], "count": 0}, todo_file, indent=4)

		config_file.close()
		todo_file.close()

	def check_init(self):
		""" returns True if remembrall has been initialized """
		home = self.remembrall_home
		if not os.path.exists(home):
			return False
		if not os.path.exists(home + "/" + REMEMBRALL_CONFIG_FILE):
			return False
		if not os.path.exists(home + "/" + TODO_LIST_FILE):
			return False

		config = self.get_remembrall_config_file_data()
		if config.get("init", False) == True:
			return True
		else:
			return False

	def get_remembrall_config_input(self):
		name = str(input("Please enter your name: "))
		reminder_interval = int(input(\
			"Please enter reminder interval (in minutes): "))
		active_ttys = self.get_tty()
		data = {
			"name": name,
			"reminder_interval": reminder_interval,
			"active_tty": active_ttys,
			"init": True,
			"which_remembrall": self.get_which_remembrall(),
		}		
		return data

	def get_remembrall_config_file_data(self):
		try:
			config_data = None
			if os.path.exists(self.remembrall_home+"/"+REMEMBRALL_CONFIG_FILE):
				with open(self.remembrall_home+"/"+REMEMBRALL_CONFIG_FILE, "r") as config_file:
					config_data = json.load(config_file)
				config_file.close()
			else: pass
		except Exception as e:
			print(e)
			sys.exit(1)
		else:			
			return config_data

class CronJob():
	""" 
		Cron job initializer.
	"""
	def __init__(self, remembrall):
		if remembrall and isinstance(remembrall, Remembrall):
			self.remembrall = remembrall
			self.cron = CronTab(user=True)
			#print("Initialized cron-job object")
		else:
			print("\nError in initializing cron-job, no remembrall object found!\n")
			sys.exit(1)

	def set_cron(self, input_flag=False):
		""" sets reminder cron
			will clear existing crons first
		 """
		self.remove_all_crons()	
		
		if self.remembrall.check_init():
			remembrall_config = self.remembrall.remembrall_config
			which_remembrall = self.remembrall.get_which_remembrall()
			if input_flag:
				cron_settings = self.get_cron_settings_input()
				interval = cron_settings.get("reminder_interval", None)
			else:
				interval = remembrall_config.get("reminder_interval", None)

			cron_cmd = which_remembrall + " show " + "> /dev/" + \
						self.remembrall.tty[0]								
			job = self.cron.new(cron_cmd, comment="remembrall")

			if interval:
				interval = int(interval)
				job.minute.every(interval)
				
			self.cron.write()		
			print("\nReminder set sucessfully!\nYou'll get a terminal notification every %s minutes!\n" \
				%interval)

	def remove_cron(self):
		""" removes all crons """
		self.cron.remove_all(comment="remembrall")
		self.cron.write()
		print("\nCleared reminders!\n")

	def remove_all_crons(self):
		try:
			self.cron.remove_all(comment="remembrall")
			self.cron.write()
		except Exception as e:
			pass
		else:
			pass

	def get_cron_settings_input(self):
		""" get user input for cron settings """
		reminder_interval = int(input(\
			"\nPlease enter reminder interval (in minutes): "))
		return {
			"reminder_interval": reminder_interval,
		}

# test function
def test_main():	
	remembrall = Remembrall()
	remembrall.init_remembrall()
	#remembrall.create_config()		
	cron = CronJob(remembrall)
	#cron.set_cron()
	cron.remove_cron()

# entry point for console scripts
def entry():
	remembrall = Remembrall()
	print("Sweeping To-Do list! \n\n")	

if __name__ == "__main__":
	test_main()	


