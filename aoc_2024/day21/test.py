import unittest
from script import parse, solve

TEST_FILE = 'sample.txt'


class TestDay2X(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve(parse(TEST_FILE), 3), 126384)


if __name__ == '__main__':
    unittest.main()
