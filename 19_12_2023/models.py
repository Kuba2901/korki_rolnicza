import requests
from typing import List, Dict

class BlogPost:
	def __init__(self, user_id: int, title: str, description: str, photo_url: str, category: str, content_text: str, content_html: str, created_at: str, updated_at: str) -> None:
		self.user_id = user_id
		self.title = title
		self.description = description
		self.photo_url = photo_url
		self.category = category
		self.content_text = content_text
		self.content_html = content_html
		self.created_at = created_at
		self.updated_at = updated_at

	def to_json(self) -> Dict:
		return {
			"user_id": self.user_id,
			"title": self.title,
			"description": self.description,
			"photo_url": self.photo_url,
			"category": self.category,
			"content_text": self.content_text,
			"content_html": self.content_html,
			"created_at": self.created_at,
			"updated_at": self.updated_at
		}

	def __str__(self) -> str:
		return f"""
User ID: {self.user_id}
Title: {self.title}
Description: {self.description}
Category: {self.category}
Created At: {self.created_at}
Updated At: {self.updated_at}
"""

	@classmethod
	def blog_post_from_json(cls, data: Dict) -> None:
		user_id = data["user_id"]
		title = data["title"]
		description = data["description"]
		photo_url = data["photo_url"]
		category = data["category"]
		content_text = data["content_text"]
		content_html = data["content_html"]
		created_at = data["created_at"]
		updated_at = data["updated_at"]

		return BlogPost(user_id, title, description, photo_url, category, content_text, content_html, created_at, updated_at)
	


	def __eq__(self, other) -> bool:
		return (self.user_id == other.user_id and
			self.title == other.title and
					self.description == other.description and
						self.photo_url == other.photo_url and
							self.category == other.category and
								self.content_text == other.content_text and
									self.content_html == other.content_html and
										self.created_at == other.created_at and
											self.updated_at == other.updated_at)



class PostsManager:
	def __init__(self, posts_count: int) -> None:
		self.posts_count = posts_count
		self.url = f"https://api.slingacademy.com/v1/sample-data/blog-posts?limit={self.posts_count}"
		self.posts = self.get_posts()

	def request_data(self) -> requests.models.Response:
		response = requests.get(self.url)
		response.raise_for_status()
		return (response)

	def get_json_res(self) -> Dict:
		response = self.request_data()
		json_res = response.json()
		return (json_res)

	def parse_data(self) -> List[Dict]:
		json_res = self.get_json_res()
		blogs = json_res['blogs']
		return (blogs)

	def get_blogs_len(self):
		return (len(self.posts))

	def get_posts(self) -> List[BlogPost]:
		blogs_json = self.parse_data()

		blogs_list = []
		
		for blog_json in blogs_json:
			post = BlogPost.blog_post_from_json(blog_json)
			blogs_list.append(post)

		return (blogs_list)

	def print_posts_data(self) -> None:
		for i in range(len(self.posts)):
			post = self.posts[i]
			print(post)

	
