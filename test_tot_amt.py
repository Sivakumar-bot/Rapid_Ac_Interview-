import unittest
from tot_amt import tot_amt

class TestToltal(unittest.TestCase):
    def test_eqamt(self):
        """
        test correct output
        """        
        self.assertEqual(tot_amt({"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}),275)
        self.assertEqual(tot_amt({"Sam": 83, "Sasi": -48}),35)
        self.assertEqual(tot_amt({"Sai": 67, "Sathish": 48.5}),115.5)
        
        #python dict will not accept the duplicate keys
        self.assertEqual(tot_amt({"Madhu": 67, "karthi": 48,"Madhu":82,"Deva":34,"Deva":56}),186)
        
        
        #testing exception case
        with self.assertRaises(TypeError):
            tot_amt([12,13,5])
        with self.assertRaises(TypeError):
            tot_amt({"siva": '50', "kumar": 48})       
            
if __name__=="__main__":
    unittest.main()

        
