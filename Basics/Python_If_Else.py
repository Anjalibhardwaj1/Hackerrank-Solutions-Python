#Task
#Given an integer, n, perform the following conditional actions:

# If n is odd, print "Weird"
# If n is even and in the inclusive range of 2 to 5, print "Not Weird"
# If n is even and in the inclusive range of 6 to 20, print "Weird"
# If n is even and greater than 20, print "Not Weird"

#Input Format
#A single line containing a positive integer, n.

#Constraints
# 1 <= n <= 100

#Output Format
#Print "Weird" if the number is weird. Otherwise, print "Not Weird"

#------------------------------------------------------------

#Welcome message
print('\nWelcome')

while True:
    #enter a number
    number = int(input('Enter a number from 1 to 100: '))

    #boundary condition.
    if number < 1 or number > 100:
        print('Please enter a number from 1 to 100...\n')
        continue

    break

#checking if number is weird or not...
if number % 2 != 0:
    print('Weird')
elif number % 2 == 0 and (number >= 2 and number <= 5):
    print('Not Weird')
elif number % 2 == 0 and (number >= 6 and number <= 20):
    print('Weird')
elif number % 2 == 0 and  number > 20:
    print('Not Weird')

print('\nGoodbye')
exit()
