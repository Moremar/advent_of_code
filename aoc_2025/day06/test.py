import unittest
from script import parse1, parse2, solve

TEST_FILE = 'sample.txt'


class TestDay06(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve(*parse1(TEST_FILE)), 4277556)

    def test_part2(self):
        self.assertEqual(solve(*parse2(TEST_FILE)), 3263827)


if __name__ == '__main__':
    unittest.main()
