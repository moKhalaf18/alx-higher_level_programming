#!/usr/bin/python3
def fizzbuzz():
    msg = ''
    for i in range(1, 101):
        if (i % 15 == 0):
            msg = 'FizzBuzz'
        elif (i % 5 == 0):
            msg = 'Buzz'
        elif (i % 3 == 0):
            msg = 'Fizz'
        else:
            msg = i
        print(msg, end=' ')
