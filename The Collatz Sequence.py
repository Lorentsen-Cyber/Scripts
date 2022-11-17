import time, random, sys

def Collatz(number):
    print('Starting number:' + str(number))
    while number != 1:
        if number %2:
            number = (3 * number + 1)
            print(number)
        else:
            number = (number // 2)
            print(number)
    


Collatz(5)
        