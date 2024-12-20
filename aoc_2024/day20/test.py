import unittest
from script import parse, solve

TEST_FILE = 'sample.txt'


class TestDay20(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve(*parse(TEST_FILE), 2, 30), 4)

    def test_part2(self):
        self.assertEqual(solve(*parse(TEST_FILE), 20, 70), 41)


if __name__ == '__main__':
    unittest.main()
