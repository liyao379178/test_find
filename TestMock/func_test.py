# import unittest
# import TestMock.function
#
#
# class MyTestCase(unittest.TestCase):
#
# 	def test_add_and_multiply(self):
# 		x = 3
# 		y = 4
# 		addition, multiple = TestMock.function.add_and_multiply(x, y)
# 		self.assertEquals(7, addition)
# 		self.assertEquals(12, multiple)


import unittest
from unittest.mock import patch
import TestMock.function


class MyTestCase(unittest.TestCase):

	@patch("TestMock.function.multiply")
	def test_add_and_multiply2(self, mock_multiply):
		x = 3
		y = 5
		mock_multiply.return_value = 15
		addition, multiple = TestMock.function.add_and_multiply(x, y)
		mock_multiply.assert_called_once_with(3, 5)

		self.assertEqual(8, addition)
		self.assertEqual(15, multiple)


if __name__ == '__main__':
	unittest.main()
