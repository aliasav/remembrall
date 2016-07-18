"""
	To-Do List class and logic goes here
"""
import sys
import datetime
from initializer import Remembrall
from constants import *

class ToDoList():

	def __init__(self, remembrall):
		if remembrall and isinstance(remembrall, Remembrall):
			try:
				self.remembrall = remembrall			
				self.created_at = datetime.datetime.now()
				self.list_data = None
				self.list_name = None				
			except Exception as e:
				print(e)
				sys.exit(1)
			else:
				print("Successfully initialized to-do-list obj! %s" %self)

		else:
			print("No remembrall obj found!")
			sys.exit(1)

	def add_item(self):
		pass

	def delete_item(self, id):
		pass

	def list_items(self):
		pass

	def list_items_ids(self):
		pass

	def generate_id(self):
		pass

	def remind(self):
		pass

	def edit_item(self, id):
		pass

	def clear_list(self, id):
		pass

	def write_to_file(self, data):
		pass

	def fetch_list_data(self):
		""" fetches list json data """
		try:
			with open(self.remembrall.home_dir + "/" + TODO_LIST_FILE, "r") as todo_file:
				data = json.load(todo_file)
				self.list_data = data
			todo_file.close()
		except Exception as e:
			print(e)
			sys.exit(1)		

	def check_json_keys(self, data):
		pass



