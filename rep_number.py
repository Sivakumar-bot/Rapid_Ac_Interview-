"""
using rep_number(arr,ty=”i”) function print all the numbers that are repeating in given array and 
the number of times they are repeated
"""
from array import array

def rep_number(arr,ty='i'):
    """
    rep_number function accepts 1st argument as a value list , 2nd argument as type of array(default is signed integer('i'))
    """
    try:
        given=array(ty ,arr)
        
        #creating dict using dict comprehension
        #dict keys as repeating number and values as number times they are repeating 
        sort_list={i:given.count(i) for i in given if given.count(i)>1}
        
      
        #iterate the dict items in for loop and print keys and values
        for i,j  in sort_list.items():
            print(i,"Repeated->",j,"times")
            
    #Raise the Type error if input sequence is not a interger and different data types
    except :
        raise TypeError(" Please Enter the valid array Sequence ")
        
if __name__=="__main__":
    rep_number([1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1])
