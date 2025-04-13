import unittest
from exercise_2 import index_power

class TestIndexPower(unittest.TestCase):
    def test_index_power_with_valid_index(self):
        self.assertEqual(index_power([1, 2, 3, 4], 2), 9)
        self.assertEqual(index_power([1, 3, 10, 100], 3), 1000000)
        self.assertEqual(index_power([0, 1], 0), 1)
        self.assertEqual(index_power([5, 7, 9, 11], 1), 7)
        
    def test_index_power_with_invalid_index(self):
        self.assertEqual(index_power([1, 2], 3), -1)
        self.assertEqual(index_power([1, 2, 3], 5), -1)
        self.assertEqual(index_power([], 0), -1)
        
    def test_index_power_zero(self):
        self.assertEqual(index_power([5, 0, 10], 1), 0)
        self.assertEqual(index_power([1, 2, 3], 0), 1)
    
    def test_index_power_large_numbers(self):
        self.assertEqual(index_power([2, 3, 4], 2), 16)
        self.assertEqual(index_power([10], 0), 1)

if __name__ == "__main__":
    unittest.main()
    
#test case by AI