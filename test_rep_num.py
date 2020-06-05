import unittest
from rep_number import rep_number

class TestRep(unittest.TestCase):
    def test_repnum(self):
        """
        test correct output
        """
        #using dict or set as sequence in array initializer,will not return anythig 
        #set and dict remove the duplicates  
        self.assertEqual(rep_number({12,12,13,14,13}),None)
        self.assertEqual(rep_number({12:12,13:14,13:12}),None)
        

        
        
        #testing exception case
        with self.assertRaises(TypeError):
            rep_number(["12","12",5])
        with self.assertRaises(TypeError):
            rep_number("12",13,5,5)
        with self.assertRaises(TypeError):
            rep_number([12.1,3.5,12.1])
        with self.assertRaises(TypeError):
            rep_number([-1,13,34,56,34,56,"12"],ty='f')
        with self.assertRaises(TypeError):
            rep_number([-1,13,34,56,34,56,12+2j],ty='f')       
            
        
if __name__=="__main__":
    unittest.main()

        
