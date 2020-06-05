import unittest
import num

class TestNum(unittest.TestCase):
    """
    test correct Exception raise
    """    
    def test_eq(self): 
        with self.assertRaises(TypeError):  
            num.num(12.3)
        with self.assertRaises(TypeError):  
            num.num(0)
        with self.assertRaises(TypeError):  
            num.num(-1)
        with self.assertRaises(TypeError):
            num.num(12+3j)
        with self.assertRaises(TypeError):
            num.num("12")
        
if __name__=='__main__':
    unittest.main()