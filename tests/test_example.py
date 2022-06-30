import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from example_package.example import add_one


class TestExamplePackage(unittest.TestCase):

    def test_add_one(self):
        expected = 1
        actual = add_one(0)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
