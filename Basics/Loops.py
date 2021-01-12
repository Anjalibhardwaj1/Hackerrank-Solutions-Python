#Task
#The provided code reads and integer, n, from STDIN.
#For all non-negative integers i < n, print i**2 .
#The list of non-negative integers that are less than n = 3 is [0, 1, 2].
#Print the square of each number on a separate line.

#Constraints
# 1 <= n <= 20

#User input of n
n = int(input('Enter a number between 1-20: '))

#while user enters a number out of bounds
while not ( n >= 1 and n <= 20):
    n = int(input('Sorry, enter a number between 1-20: '))

#while the user enters a number that is in bounds
while n >= 1 and n <= 20:
    #Starting from 0 to n print the squares
    for i in range(0, n):
        print(i**2)
    break
