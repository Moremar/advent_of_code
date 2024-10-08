import unittest
import script1
import script2

TEST_FILE = "sample.txt"


class TestDay03(unittest.TestCase):

    def test_part_1(self):
        self.assertEqual(script1.compute(TEST_FILE), 4)

    def test_part_2(self):
        self.assertEqual(script2.compute(TEST_FILE), 3)


if __name__ == '__main__':
    unittest.main()
