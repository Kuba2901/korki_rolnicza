from typing import Dict, List
import json

class BlogPost:
	# Default BlogPost class constructor
	def __init__(self, id: int, title: str, content: Dict, author: str, created_at: str) -> None:
		self.id = id
		self.title = title
		self.content = content
		self.author = author
		self.created_at = created_at


	# Convert the instance to JSON data
	def toJson(self):
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content,
			"author": self.author,
			"created_at": self.created_at
		}
	
	# Reassign instance values to the JSON fields
	def fromJson(self, data):
		self.id = data['id']
		self.title = data["title"]
		self.content = data["content"]
		self.author = data["author"]
		self.created_at = data["created_at"]

class BlogPostManager:
	def __init__(self, file_name: str) -> None:
		self.file_name = file_name
		self.posts = self.get_posts()

	# Adds the new post to instance's list and saves it in file
	def add_post(self, id: int, title: str, content: Dict, author: str, created_at: str) -> None:
		new_post = BlogPost(id, title, content, author, created_at)
		self.posts.append(new_post)
		# self.dump_to_file()
		print("[+] Post added")

	# Saves all posts from the instance to the file
	def dump_to_file(self):
		# REMOVE THIS COMMENT: (converts all posts to a JSON-like body with "str" as id and {} as body)
		# data = {str(post.id): post.toJson() for post in self.posts}
		data = {}
		for post in self.posts:
			post_id_str = str(post.id)
			post_json = post.toJson()
			data[post_id_str] = post_json

		with open(self.file_name, "w") as file:
			json.dump(data, file, indent=2)

	# Goes through the list of all posts in the BlogPostManager instance, if a post of the provided ID is found, then the values are changed and changes are saved to the file
	def update_post(self, id: int, title: str, content: Dict) -> None:
		for post in self.posts:
			if post.id == id:
				post.title = title
				post.content = content
				self.dump_to_file()
				print("[@] Post updated")
				break

	# Deletes post of the provided ID if exists, else nothing is done
	def delete_post(self, id: int) -> bool:
		for post in self.posts:
			if post.id == id:
				self.posts.remove(post)
				self.dump_to_file()
				return True
		return False

	# Reads posts from the file of the provided file_name, then converts each of them into BlogPost instances and appends to a list, then the function returns the list
	def get_posts(self) -> List[BlogPost]:
		file = open(self.file_name, "r")
		data = json.load(file)
		posts_list = []
		for v in data.values():
			post = BlogPost(1, "", {}, "", "")
			post.fromJson(v)
			posts_list.append(post)
		file.close()
		return posts_list

	# Displays the post in the JSON format
	def view_post(self, id: int):
		for post in self.posts:
			if post.id == id:
				print(post.toJson())
				break

			

