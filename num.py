"""
Print the numbers from 1 to N ,using num(n) function

if the number is multiples of three, print “Fizz” instead of the number 

and for the multiples of five print “Buzz”
For numbers which are multiples of both three and five print “FizzBuzz”
"""

def num(n):
    """
    num function accepts one Natural integer number (greater than 0) as a Argument
    """
    try:
        #check if the given number is Negative or Zero if yes then it will raise Exception
        if n<=0 :
            raise TypeError 
        #iterate given number through the loop using range function
        for i in range(n):
            
            #condition checks if "i" multiples of both 3 and 5
            if (i+1)%3==0 and (i+1)%5==0:
                print("FizzBuzz",end="," if (i+1)!=n else "")
                
            #condition checks if "i" multiples of 3   
            elif (i+1)%3==0 and not (i+1)%5==0:
                print("Fizz",end="," if (i+1)!=n else "")
                
            #condition checks if "i" multiples of 5
            elif (i+1)%5==0 and not (i+1)%3==0:
                print("Buzz",end="," if (i+1)!=n else "")
                
            #if number(i) is not multiples of 3 and 5 then print the number 
            else:
                print(i+1,end="," if (i+1)!=n else "")
    except :
        raise TypeError ("Please Enter the Natural interger number(greater than 0)")
        
if __name__=='__main__':
    num(17)
