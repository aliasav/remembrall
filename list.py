"""
	To-Do List class and logic goes here
"""
import sys
import datetime
import json
import string
import random
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
				#print("Successfully initialized to-do-list obj! %s" %self)
				pass

		else:
			print("No remembrall obj found!")
			sys.exit(1)

	def add_item(self):
		item_details = self.get_item_details()
		self.list_data["items"].append(item_details)
		self.set_items_count()
		self.write_to_file(self.list_data)

	def set_items_count(self):
		""" sets items count in list_data """
		self.list_data["count"] = len(self.list_data["items"])

	def get_item_details(self):
		title = str(raw_input("Title: "))
		details = str(raw_input("Details: "))
		id = self.id_generator()
		return {
			"title": title,
			"details": details,
			"id": id,
		}

	def delete_item(self, id):
		pass

	def list_items(self, show_ids=False):
		""" displays list of items """
		print("\n***************|| To-Do list ||***************\n")
		self.fetch_list_data()
		items = self.list_data["items"]
		if len(items)>0:
			for i in items:
				print("Title: %s" %i["title"])
				print("Details: %s" %i["details"])
				if show_ids:
					print("Id: %s" %i["id"])
				print("\n")
		else:
			print("Your To-Do list is empty!")
			print("\n")

	def id_generator(self):
		size = 5
		chars = string.ascii_uppercase + string.digits
		return ''.join(random.choice(chars) for _ in range(size))


	def remind(self):
		pass

	def edit_item(self, id):
		pass

	def clear_list(self):
		self.fetch_list_data()
		self.list_data["items"] = []
		self.set_items_count()
		self.write_to_file(self.list_data)
		print("*************|| Cleared your To-Do list ||*************")

	def write_to_file(self, data):
		if data:
			try:
				with open(self.remembrall.remembrall_home + "/" + TODO_LIST_FILE, "w") as todo_file:
					json.dump(data, todo_file, indent=4)
					print("Items saved successfully!")
			except Exception as e:
				print(e)
				sys.exit(1)
			else:
				todo_file.close()


	def fetch_list_data(self):
		""" fetches list json data """
		try:
			with open(self.remembrall.remembrall_home + "/" + TODO_LIST_FILE, "r") as todo_file:
				data = json.load(todo_file)
				self.list_data = data
			todo_file.close()
		except Exception as e:
			print(e)
			sys.exit(1)		

	def check_json_keys(self, data):
		pass

if __name__ == "__main__":
	remembrall = Remembrall()
	remembrall.init_vars()
	if not remembrall.check_init():
		remembrall.init_remembrall()
	else:
		todo = ToDoList(remembrall)
		todo.fetch_list_data()
		#todo.add_item()
		todo.list_items()
		#todo.clear_list()



