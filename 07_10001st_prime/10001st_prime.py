'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
from math import ceil
# primes cannot be even
# primes only have factors 1 and themselves

def isPrime(n):
    if (n <= 1): return False
    if (n == 2): return True
    if (n % 2 == 0): return False
    if (n < 9): return True
    if (n % 3 == 0): return False
    for i in range(5,int(n**0.5)+1,6):
        if (n % i == 0) or (n % (i+2) == 0): 
            return False
    return True

# then to find the Kth prime

N = 10001
primes = 1
i = 1
while primes<N:
    i += 2
    if isPrime(i):
        primes += 1

print(i)