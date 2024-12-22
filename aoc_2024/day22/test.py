import unittest
from script import parse, solve1, solve2

TEST_FILE_1 = 'sample1.txt'
TEST_FILE_2 = 'sample2.txt'


class TestDay2X(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve1(parse(TEST_FILE_1)), 37327623)

    def test_part2(self):
        self.assertEqual(solve2(parse(TEST_FILE_2)), 23)


if __name__ == '__main__':
    unittest.main()
