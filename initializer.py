"""
Initialises remembrall files for user
"""
import sys
import os
import json
import subprocess

class Remembrall():
	"""
		Remembrall initialiser
		Creates a hidden remembrall folder in User's home folder.
		Config JSON file created with user's information 
	"""

	def __init__(self):

		self.home_dir = None
		self.tty = None

	def init_remembrall(self):
		self.init_vars()		

	def init_vars(self):
		self.home_dir = self.get_home_dir()
		self.tty = self.get_tty()
		self.remembrall_home = self.get_remembrall_home()
		self.create_remembrall_folder()

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
		""" finds terminal to display output to. 
			Will be used to set crontab """
		try:
			output = subprocess.check_output(["tty"])
		except Exception as e:
			print("Couldn't get tty output! :(")
			print(e)
			sys.exit(1)
		else:
			return output[:len(output)-2]

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
		""" creates config JSON file """
		home = self.get_remembrall_home()
		with open(home+"/config.json", "w") as config_file:
			data = {}
			json.dump(data, config_file)

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


