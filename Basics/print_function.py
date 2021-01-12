#The included code stub will read an integer, n, from STDIN. Without using any
#string methods, try to print the following:
# 123...n

#Constraints
#1 <= n <= 150

#User input
n = int(input('Enter a number n: '))

#create a num list
num = []

#check bounds
if n >= 1 and n <= 150:

    #loop through range
    for i in range(1, n+1):
        #append through list
        num.append(i)

    #unpack sequence and print num
    print(*num, sep='')
