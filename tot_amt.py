"""
Accept Dictionary, names as keys and amount paid by each of them as interger Values
then Return the total amount of values

"""
def tot_amt(val):
    """
    function accepts dict(keys and value) as argument
    """
    #check the type of the argument
    #if type is not dict then it will raise error
    if type(val)==dict:
        try:
            #get the amount from dict using values function
            #Total the amount using sum function
            return sum(val.values())
        except:
            raise TypeError("please Enter the Dictionary with integer type of values")
    else:
        raise TypeError("Please Enter the Dictionary type sequence")

            
    
