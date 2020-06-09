import unittest

from clock import findAngle, InvalidTimeError


class TestAngle(unittest.TestCase):

    def test_six(self):
        self.assertEqual(findAngle(6, 0), 180)

    def test_six_fifteen(self):
        self.assertEqual(findAngle(6, 15), 97.5)

    def test_invalid_time(self):
        with self.assertRaises(InvalidTimeError):
            findAngle(13, 15)


if __name__ == '__main__':
    unittest.main()