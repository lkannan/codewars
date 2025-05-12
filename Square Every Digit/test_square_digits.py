import unittest
from square_digits import square_digits

class TestSquareDigits(unittest.TestCase):
    def test_square_digits(self):
        # Test case with mixed digits
        self.assertEqual(square_digits(9119), 811181)
        
        # Test case with zero
        self.assertEqual(square_digits(0), 0)
        
        # Test case with single digit
        self.assertEqual(square_digits(5), 25)
        
        # Test case with all same digits
        self.assertEqual(square_digits(222), 444)
        
        # Test case with ascending digits
        self.assertEqual(square_digits(123), 149)
        
        # Test case with larger numbers
        self.assertEqual(square_digits(765), 493625)

if __name__ == '__main__':
    unittest.main()