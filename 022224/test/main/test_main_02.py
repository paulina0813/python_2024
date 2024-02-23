import unittest
import main

class TestMain(unittest.TestCase):
    
    def setUp(self):
        print("Starting the automated tests for the sum_five function")
    
    def test_sum_five_one(self):
        test_parameter = 5
        result = main.sum_five(test_parameter)
        self.assertEqual(result, 10)
        print("Validaring sum_five_one if it's correct")
    
    
    def test_sum_five_two(self):
        test_parameter = 'string'
        result = main.sum_five(test_parameter)
        self.assertIsInstance(result, ValueError)
        print("Validaring sum_five_two if it's correct")
    
    def test_sum_five_three(self):
        test_parameter = ''
        result = main.sum_five(test_parameter)
        self.assertEqual(result, "Please enter a number")
        print("Validaring sum_five_three if it's correct")
        

#unittest.main()

if __name__ == '__main__':
    unittest.main()