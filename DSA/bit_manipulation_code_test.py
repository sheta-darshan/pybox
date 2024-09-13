import unittest
from io import StringIO
import sys
import unittest.mock
from bit_manipulation_code import bitManipulation

class TestBitManipulation(unittest.TestCase):
    
    def capture_output(self, func, *args):
        """ Helper function to capture the output of the bitManipulation function. """
        old_stdout = sys.stdout
        new_stdout = StringIO()
        sys.stdout = new_stdout
        func(*args)
        sys.stdout = old_stdout
        return new_stdout.getvalue().strip()
    
    def test_bitManipulation(self):
        # Test case 1
        output = self.capture_output(bitManipulation, 70, 3)
        self.assertEqual(output, "1 70 66")
        
        # Test case 2
        output = self.capture_output(bitManipulation, 8, 1)
        self.assertEqual(output, "0 9 8")
        
        # Additional test cases
        # Test case 3
        output = self.capture_output(bitManipulation, 15, 4)
        self.assertEqual(output, "1 15 7")  # Bit 4 in 15 (1111) is 1, set 4th bit = 15, clear 4th bit = 7
        
        # Test case 4
        output = self.capture_output(bitManipulation, 31, 5)
        self.assertEqual(output, "1 31 15")  # Bit 5 in 31 (11111) is 1, set 5th bit = 63, clear 5th bit = 47
        
        # Test case 5
        output = self.capture_output(bitManipulation, 1, 5)
        self.assertEqual(output, "0 17 1")  # Bit 5 in 1 (00001) is 0, set 5th bit = 33, clear 5th bit = 32
    
if __name__ == '__main__':
    unittest.main()
