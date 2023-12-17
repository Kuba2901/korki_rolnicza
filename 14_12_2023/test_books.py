import unittest
from unittest.mock import patch, Mock, mock_open
from library import Book, Library

class TestBook(unittest.TestCase):
	def test_to_json(self):
		expected = {
			"id": 1,
			"title": "t1",
			"author": "a1",
			"publish_date": "p1",
			"available": True
		}

		data = Book(1, "t1", "a1", "p1")
		self.assertEqual(data.to_json(), expected)

	def test_from_json(self):
		data = {'id': "1", "title": "t1", "author": "a1", "publish_date": "p1", "available": True}
		book_instance = Book()
		book_instance.from_json(data)

		expected = Book(1, "t1", "a1", "p1")
		self.assertEqual(book_instance.author, expected.author)
		self.assertEqual(book_instance.title, expected.title)
		self.assertEqual(book_instance.publish_date, expected.publish_date)	


class TestLibrary(unittest.TestCase):
	def setUp(self):
		self.file_name = "test_cars.json"
		self.library = Library(self.file_name)

	def tearDown(self):
		with patch("builtins.open", mock_open(), create=True):
			open(self.file_name, "w").close()


	def test_get_books(self):
		file_content = '{"1": {"id": 1, "title": "t1", "author": "a1", "publish_date": "p1", "available": true}}'
		with patch("builtins.open", mock_open(read_data=file_content), create=True):
			books = self.library.get_books()
			self.assertEqual(len(books), 1)
			self.assertIsInstance(books[0], Book)

	# @patch("builtins.open", mock_open(), create=True)
	@patch("library.Book.to_json")
	# @patch("library.Library.to_json")
	def test_add_car(self, mock_to_json):
		self.library.add_book(1, "t1", "a1", "p1")
		mock_to_json.assert_called_once()




if __name__ == '__main__':
	unittest.main()