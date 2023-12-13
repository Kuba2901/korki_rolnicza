# test_calculator.py

import unittest
from unittest.mock import patch, Mock
from calculator import add

class TestAddFunction(unittest.TestCase):
	@patch('calculator.add')
	def test_add_function(self, mock_add):
		mock_add.return_value = 8
		result = add(3, 5)
		self.assertEqual(result, mock_add.return_value)

if __name__ == '__main__':
	unittest.main()
