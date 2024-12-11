import unittest
from script import parse, solve

TEST_FILE = 'sample.txt'


class TestDay11(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve(parse(TEST_FILE), 25), 55312)

    def test_part2(self):
        self.assertEqual(solve(parse(TEST_FILE), 75), 65601038650482)


if __name__ == '__main__':
    unittest.main()
