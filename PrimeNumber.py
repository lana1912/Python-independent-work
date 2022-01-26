# Определить является ли число простым
def prime_number(n):
    if n != 1:
        for e in range(2,n):
            if n % e == 0:
                return False
            return True
print(prime_number(6))