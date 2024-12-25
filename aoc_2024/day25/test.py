import unittest
from script import parse, solve1

TEST_FILE = 'sample.txt'


class TestDay2X(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve1(*parse(TEST_FILE)), 3)


if __name__ == '__main__':
    unittest.main()
