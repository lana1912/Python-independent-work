# Определить является ли число совершенным 
import re


def perfect_number(n):
    result = 0
    for e in range(1,n):
        if n % e == 0:
            result += e
    return n == result 
print(perfect_number(30))
    