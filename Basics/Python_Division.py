#Task
#The provided code stub reads two integers, a and b, from STDIN.

#Add logic to print two lines. The first line should contain the result
#of integer division, a//b. The second line should contain the result of float division, a/b.

#No rounding or formatting is necessary.

#-------------------------------------------------------------------------------

#number 1
a = int(input('Enter the first number: '))

#number 2
b = int(input('Enter the second number: '))

#Result of integer divison
result_int = int((a//b))

#Result of float divison
result_float = float((a/b))

#print results
print(result_int)
print(result_float)
