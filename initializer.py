"""
Initialises remembrall files for user
"""
import sys
import os
import json
import subprocess
from constants import *

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

	def init_remembrall(self):
		""" 
		initializes remembrall system:
			sets-up remmebrall folder and config file
			sets-up crontab
		"""
		self.init_vars()
		self.create_remembrall_folder()
		self.create_config()

	def init_vars(self):
		self.home_dir = self.get_home_dir()
		self.tty = self.get_tty()
		self.remembrall_home = self.get_remembrall_home()


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
			output = subprocess.check_output(["tty"])
		except Exception as e:
			print("Couldn't get tty output! :(")
			print(e)
			sys.exit(1)
		else:
			tty = output[:len(output)-2]
			#self.tty = tty
			return tty

	def get_active_ttys(self):
		pass

	def find_active_ttys(self):
		""" should fetch all active terminals at the moment """
		pass

	def get_remembrall_home(self):
		""" returns path of remembrall home directory"""
		return self.home_dir + "/.remembrall"

	def create_remembrall_folder(self):		
		""" creates remembrall home dir """
		if not os.path.exists(self.remembrall_home):
			print("Creating remembrall home directory!")
			os.makedirs(self.get_remembrall_home())
		else:
			print("Remembrall already exists!")

	def create_config(self):
		""" creates config JSON files """		
		home = self.get_remembrall_home()
		self.remembrall_config = self.get_remembrall_config()
		# create config file
		with open(home + "/" + REMEMBRALL_CONFIG_FILE, "w") as config_file:			
			json.dump(self.remembrall_config, config_file, indent=4)

		# create to-do list file
		with open(home + "/" + TODO_LIST_FILE, "w") as todo_file:
			json.dump({}, todo_file, indent=4)

		config_file.close()
		todo_file.close()

	def get_remembrall_config(self):
		name = str(raw_input("Please enter your name: "))
		reminder_interval = int(raw_input(\
			"Please enter reminder interval (in minutes): "))
		active_ttys = [self.tty]  # replace with get active ttys function
		data = {
			"name": name,
			"reminder_interval": reminder_interval,
			"active_tty": active_ttys,
		}		
		return data


class CronJob():
	""" 
		Cron job initializer.
	"""
	def __init__(self, remembrall):
		if remembrall and isinstance(remembrall, Remembrall):
			self.remembrall = remembrall
			print("Initialized cron-job object")
		else:
			print("Error in initializing cron-job, no remembrall object found!")
			sys.exit(1)


	def set_cron(self):
		remembrall_config = self.remembrall.remembrall_config
		if not remembrall_config:
			print("User config not available! Please re-initialize Remembrall!")
			sys.exit(1)
		else:
			interval = remembrall_config.get("reminder_interval", None)
			if interval is None:
				print("Reminder interval not available!")
				sys.exit(1)
			else:
				print(interval)
				


# test function
def test_main():	
	remembrall = Remembrall()
	remembrall.init_remembrall()	

# entry point for console scripts
def entry():
	remembrall = Remembrall()
	print("Sweeping To-Do list! \n\n")	

if __name__ == "__main__":
	test_main()	


