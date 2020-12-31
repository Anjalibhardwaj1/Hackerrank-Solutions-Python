#Task
#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# 1) The first line contains the sum of the two numbers.
# 2) The second line contains the difference of the two numbers (first - second).
# 3)  third line contains the product of the two numbers.

# Constraints
# 1 <= a <= 10**10
# 1 <= b <= 10**10

#-----------------------------------------------------------

#prompt
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))

#sum of two numbers
sum = first_num+second_num

#first-second
difference = first_num-second_num

#first_num*second_num
product = first_num*second_num

#print the sum, difference, and product
print('The sum is {}.'.format(sum))
print('The difference is {}.'.format(difference))
print('The product is {}.'.format(product))
