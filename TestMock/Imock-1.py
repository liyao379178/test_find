from unittest import mock
import unittest
from TestMock.Imock import MockCount


class TestCount(unittest.TestCase):

	def test_add(self):
		count = MockCount()
		count.add = mock.Mock(return_value=13, side_effect=count.add)
		result = count.add(8, 8)
		print(result)
		count.add.assert_called_with(8, 8)
		self.assertEquals(result, 16)


if __name__ == '__main__':
	unittest.main()
