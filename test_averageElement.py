import unittest
import averageElements

class testAverage(unittest.TestCase):
    def test_neg(self):
        #Passing Test
        self.assertEqual(averageElements.average([-1, -2, -3]), -2)
        #Failing Test
        #self.assertEqual(averageElements.average([-1, -2, -3]), -1)
    def test_zero(self):
        #Passing Test
        self.assertEqual(averageElements.average([0,0,1,2]), .75)
        #Failing Test
        #self.assertEqual(averageElements.average([0,0,1,2]), .7333)
    def test_floats(self):
        #Passing Test
        self.assertEqual(averageElements.average([.5, .8, 1.3]), .87)
        #Failing Test
        #self.assertEqual(averageElements.average([.5, .8, 1.3]), .89)

if __name__ == '__main__':
    unittest.main()