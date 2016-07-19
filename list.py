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
		print("\n***************|| Add Item ||***************\n")
		item_details = self.get_item_details()
		self.list_data["items"].append(item_details)
		self.set_items_count()
		self.write_to_file(self.list_data)

	def set_items_count(self):
		""" sets items count in list_data """
		self.list_data["count"] = len(self.list_data["items"])

	def get_item_details(self, generate_id=True, edit_id=None):		
		title = str(raw_input("Enter Title: "))
		details = str(raw_input("Enter Details: "))
		if generate_id:
			id = self.id_generator()
		else:
			id = edit_id
		print("\n")
		return {
			"title": title,
			"details": details,
			"id": id,
		}

	def delete_item(self, id):
		print("\n***************|| Delete Item ||***************\n")
		if not id:
			print("\nNo ID given\nYou can check item IDs using 'remembrall show ids'!\n")
			sys.exit(1)
		elif self.check_item_id(id):
			self.list_data["items"][:] = [d for d in self.list_data["items"] if d.get('id') != id]
			self.write_to_file()
			print("Deleted item!\n")
		else:
			print("\nItem not found! ID: %s\nYou can check item IDs using 'remembrall show ids'!\n" %id)

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

	def edit_item(self, id=None):
		print("\n***************|| Edit Item ||***************\n")
		if id==None:
			print("\nNo ID given\nYou can check item IDs using 'remembrall show ids'!\n")
			sys.exit(1)
		elif self.check_item_id(id):
			for i in self.list_data["items"]:
				if i["id"]==id:
					item_data = self.get_item_details(True, id)
					i["title"] = item_data["title"]
					i["details"] = item_data["details"]
					break
			self.write_to_file()
		else:
			print("\nItem not found! ID: %s\nYou can check item IDs using 'remembrall show ids'!\n" %id)

	def check_item_id(self, id=None):
		if not id:
			return False
		else:
			items = self.list_data["items"]
			if len(items)==0:
				return False
			else:
				for i in items:
					if i["id"] == id:
						return True
				return False

	def clear_list(self):
		self.fetch_list_data()
		self.list_data["items"] = []
		self.set_items_count()
		self.write_to_file(self.list_data)
		print("\n*************|| Cleared your To-Do list ||*************\n")

	def write_to_file(self, data=None):
		""" writes list data to list.json """

		# if data not provided, use data available in class
		if not data:
			data = self.list_data		
		try:
			with open(self.remembrall.remembrall_home + "/" + TODO_LIST_FILE, "w") as todo_file:
				json.dump(data, todo_file, indent=4)
				#print("List saved successfully!")
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



