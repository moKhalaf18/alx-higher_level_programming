#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l_dig = number % -(10)
        print(-(l_dig), end='')
    else:
        l_dig = number % 10
        print(l_dig, end='')
    return abs(l_dig)
