import unittest
import requests
from unittest.mock import patch, Mock
from models import BlogPost, PostsManager
from typing import Dict, List

class TestBlogPost(unittest.TestCase):
	def test_to_json(self) -> None:
		instance = BlogPost(1, "t1", "d1", "p1", "ca1", "ct1", "ch1", "cat1", "upa1")
		expected = {
			"user_id": 1, 
			"title": "t1", 
			"description": "d1", 
			"photo_url": "p1", 
			"category": "ca1", 
			"content_text": "ct1", 
			"content_html": "ch1", 
			"created_at": "cat1", 
			"updated_at": "upa1"
		}

		return self.assertEqual(expected, instance.to_json())

	def test_blog_post_from_json(self) -> None:
		data = {
			"user_id": 1, 
			"title": "t1", 
			"description": "d1", 
			"photo_url": "p1", 
			"category": "ca1", 
			"content_text": "ct1", 
			"content_html": "ch1", 
			"created_at": "cat1", 
			"updated_at": "upa1"
		}

		instance = BlogPost.blog_post_from_json(data)
		expected = BlogPost(1, "t1", "d1", "p1", "ca1",
		 "ct1", "ch1", "cat1", "upa1")
		
		self.assertEqual(expected, instance)
	
class TestPostsManager(unittest.TestCase):
	def test_request_data(self):
		manager = PostsManager(1)
		response = manager.request_data()

		self.assertIsInstance(response, requests.models.Response)

	def test_parse_data(self):
		posts_count = 1
		manager = PostsManager(posts_count)
		requested_data = manager.parse_data()

		# Proper type returned
		self.assertEqual(len(requested_data), posts_count)
	
	@patch("models.PostsManager.get_json_res")
	def test_parse_data(self, mocked_get_json_res: Mock):
		posts_count = 1
		manager = PostsManager(posts_count)
		mocked_get_json_res.return_value = {"blogs": [{
			"user_id": 1, 
			"title": "t1", 
			"description": "d1", 
			"photo_url": "p1", 
			"category": "ca1", 
			"content_text": "ct1", 
			"content_html": "ch1", 
			"created_at": "cat1", 
			"updated_at": "upa1"
		},
		# {
		# 	"user_id": 2, 
		# 	"title": "t2", 
		# 	"description": "d2", 
		# 	"photo_url": "p2", 
		# 	"category": "ca2", 
		# 	"content_text": "ct2", 
		# 	"content_html": "ch2", 
		# 	"created_at": "cat2", 
		# 	"updated_at": "upa2"
		# },
		]}
		requested_data = manager.parse_data()

		# Proper type returned
		self.assertEqual(len(requested_data), posts_count)

	@patch("models.PostsManager.get_posts")
	def test_get_blogs_len(self, mocked_get_posts: Mock):
		mocked_get_posts.return_value = [BlogPost( 1,  "t1", "d1", "p1", "ca1", "ct1", "ch1", "cat1", "upa1")]
		manager = PostsManager(1)
		self.assertEqual(manager.get_blogs_len(), 1)

if __name__=="__main__":
	unittest.main()