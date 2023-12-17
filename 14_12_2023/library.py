import json
from typing import List

class Book:
	def __init__(self, id=1, title='title', author='author', publish_date='publish_date') -> None:
		self.id = id
		self.title = title
		self.author = author
		self.publish_date = publish_date
		self.available = True

	def to_json(self):
		return {
			"id": self.id,
			"title": self.title,
			"author": self.author,
			"publish_date": self.publish_date,
			"available": self.available
		}
	
	def from_json(self, data):
		self.id = data['id']
		self.title = data['title']
		self.author = data['author']
		self.publish_date = data['publish_date']
		self.available = data['available']

class Library:
	def __init__(self, file_name):
		self.file_name = file_name
		self.books = self.get_books()

	def get_books(self) -> List[Book]:
		try:
			file = open(self.file_name, 'r')
		except:
			with open(self.file_name, "w") as file:
				json.dump({}, file)
			
			file = open(self.file_name, 'r')

		data = json.load(file)
		books_list = []

		for v in data.values():
			book = Book()
			book.from_json(v)
			books_list.append(book)

		file.close()
		return books_list
	
	def add_book(self, id, title, author, publish_date):
		new_book = Book(id, title, author, publish_date)
		self.books.append(new_book)
		self.dump_to_file()

	def dump_to_file(self):
		data = {}
		for book in self.books:
			book_id = str(book.id)
			book_json = book.to_json()
			data[book_id] = book_json
			print(data)

		with open(self.file_name, "w") as file:
			json.dump(data, file, indent=2)

	def remove_book(self, id):
		for book in self.books:
			if id == book.id:
				self.books.remove(book)
				self.dump_to_file()
				return True
		return False
	
	def view_book(self, id, title):
		for book in self.books:
			if id == book.id:
				break
			if title == book.title:
				break

	def toggle_availability(self, id) -> bool:
		for book in self.books:
			if id == book.id:
				book.available = not book.available
				self.dump_to_file()
				return book.available
		return None

