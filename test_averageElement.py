import unittest
import averageElements

class testAverage(unittest.TestCase):
    def test_neg(self):
        self.assertEqual(averageElements.average([-1, -2, -3]), -2)
    def test_zero(self):
        self.assertEqual(averageElements.average([0,0,1,2]), .75)
    def test_floats(self):
        self.assertEqual(averageElements.average([.5, .8, 1.3]), .87)
        
if __name__ == '__main__':
    unittest.main()