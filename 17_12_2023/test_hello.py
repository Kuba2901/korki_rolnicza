import unittest
from mock import mock, patch
from hello_main import get_external_data, process_external_data

class Test(unittest.TestCase):
	@patch(hello_main.get_external_data)
	def test_process_external_data(self, mocked_external_data):
		mocked_external_data.return_value = "hello world"
		process_external_data()

if __name__ == '__main__':
	unittest.main()