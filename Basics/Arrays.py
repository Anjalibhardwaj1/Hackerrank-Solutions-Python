#Task
#You are given a space separated list of numbers.
#Your task is to print a reversed NumPy array with the element type float.
import numpy as np

#function that takes in an array
def arrays(arr):
    #stores array in list variable of type float
    list = np.array(arr, float)
    #reverses list variable
    return list[::-1]

#user input array
arr = input("Enter a list here: ").strip().split(' ')

#call function
arrays(arr)
