import unittest
import main

class TestMain(unittest.TestCase):
    def test_sum_five_one(self):
        
        test_parameter = 1
        
        result = main.sum_five(test_parameter)
        
        self.assertEqual(result, 6)

    def test_sum_five_two(self):
        
        test_parameter = 2
        
        result = main.sum_five(test_parameter)
        
        self.assertEqual(result, 4)

unittest.main()