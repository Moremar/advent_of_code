import unittest
import script1
import script2

TEST_FILE = "sample.txt"


class TestDay01(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(script1.compute(TEST_FILE), 1)

    def test_part2(self):
        self.assertEqual(script2.compute(TEST_FILE), 14)


if __name__ == '__main__':
    unittest.main()
