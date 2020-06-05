import unittest
from cricket_sc import cricket_sc

class Testcricket(unittest.TestCase):
    def test_cricket(self):
        """
        test correct output
        """
        
        #testing exception case
        with self.assertRaises(TypeError):
            cricket_sc(["1","2",6])
        with self.assertRaises(TypeError):
            cricket_sc("1",13,5,5)
        with self.assertRaises(TypeError):
            cricket_sc([12.1,3.5,12.1])
        with self.assertRaises(TypeError):
            cricket_sc([-12,-35,12])
        
    
        
if __name__=="__main__":
    unittest.main()

        
