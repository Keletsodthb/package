def sum_array(array):
    summation=sum(i for i in array)

    return summation
    '''Return sum of all items in array'''

def fibonacci(n):
    #  Display the nth number in Fibonacci sequence
# first two terms
    n1 = 0
    n2 = 1
# check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(n1)
    else:
        for count in range(2,n) :
              nth = n1 + n2
           # update values
              n1 = n2
              n2 = nth
    return n2

    #'''Return nth term in fibonacci sequence'''

def factorial(n):
# factorial function to find the factorial of a number n.

    factor = 1

# check if the number is negative, positive or zero
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            factor = factor*i


    return factorial

#Return n!

def reverse(word):
    s1 = ''
    length = len(word) - 1
    while length >= 0:
        s1 = s1 + word[length]
        length = length - 1
    return s1
    '''Return word in reverse'''
