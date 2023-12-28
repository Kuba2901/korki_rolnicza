import requests


class BlogPost:
	def __init__(self, id: int, title: str, description: str, photo_url: str, category: str, content_text: str, content_html: str, created_at: str, updated_at: str) -> None:
		self.id	= id
		self.title = title
		self.description = description
		self.photo_url = photo_url
		self.category = category
		self.content_text = content_text
		self.content_html = content_html
		self.created_at = created_at
		self.updated_at = updated_at


class PostsManager:
	def __init(self, posts_count: int) -> None:
		self.posts_count = posts_count
		self.url = f"https://api.slingacademy.com/v1/sample-data/blog-posts?limit={self.posts_count}"

	def request_data(self):
		response = requests.get(self.url)
		return (response)

	def parse_data(self):
		response = self.request_data()
		blogs = response["blogs"]

	
