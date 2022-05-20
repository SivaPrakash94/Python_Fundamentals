'These are the unittest for our product'

import unittest                             # <-- Testing tool
from math_tools import square, triple       # <-- Functions under test

class TestMathToolkit(unittest.TestCase):   # <-- Test suite

    def test_square(self):                  # <-- Test case 1
        self.assertEqual(square(5), 25)     # <----- Test step 1
        self.assertEqual(square(1), 1)      # <----- Test step 2
        self.assertEqual(square(0), 0)      # <----- Test step 3
        with self.assertRaises(TypeError):  # <----- Test step 4
            square('hello')

    def test_triple(self):                  # <-- Test case 2
        self.assertEqual(triple(5), 15)
        self.assertEqual(triple(1), 3)
        self.assertEqual(triple(0), 0)
        with self.assertRaises(TypeError):
            triple('hello')

    def test_square_bug_117535(self):
        # square() incorrectly handled negatives
        self.assertEqual(square(-5), 25)

    def test_square_bug_117635(self):
        # square() incorrectly handles floats
        self.assertEqual(square(2.5), 6.25)

if __name__ == '__main__':

    unittest.main()                         # <-- Test runner
