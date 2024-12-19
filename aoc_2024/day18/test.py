import unittest
from script import parse, solve1, solve2

TEST_FILE = 'sample.txt'


class TestDay18(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve1(parse(TEST_FILE), 6, 12), 22)

    def test_part2(self):
        self.assertEqual(solve2(parse(TEST_FILE), 6, 12), (6, 1))


if __name__ == '__main__':
    unittest.main()