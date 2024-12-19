import unittest
from script import parse, solve1, solve2

TEST_FILE = 'sample.txt'


class TestDay17(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(solve1(*parse(TEST_FILE)), '4,6,3,5,6,3,5,2,1,0')

    # no test for part 2, since the solve2() function is reverse-engineering the actual input


if __name__ == '__main__':
    unittest.main()
