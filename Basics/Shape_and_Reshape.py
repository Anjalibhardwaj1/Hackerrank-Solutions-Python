#Task
#You are given a space separated list of nine integers. Your task is to convert this list into a
#X NumPy array.
import numpy as np

arr = input("Enter a list: ").strip().split()

change_array = np.array(arr, int)
change_array.shape = (3, 3)
print(change_array)
