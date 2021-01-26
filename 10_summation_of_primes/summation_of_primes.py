'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# isPrime fn from problem 7
# this if very brute force, has complexity of sqrt(n)
'''
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
    
N = 2000000
primes = 1
primes_sum = 5 # 2 and 3 are prime
i = 5
while i<N:
    if isPrime(i):
        primes_sum += i
    i += 2
    if i <= N and isPrime(i):
        primes_sum += i
    i += 4
        
print(primes_sum)
'''
## This is a soln using the sieve of Eratosthenes
from math import floor
N = 2000000
cross_limit = floor(2000000**0.5)
sieve = [False for a in range(N)]

for i in range(4,N,2):
    #print(i)
    sieve[i] = True
    
for i in range(3,cross_limit,2):
    if not sieve[i]: 
        for j in range(i**2,N,2*i):
            sieve[j] = True
            
prime_sum = 0
for i in range(2,N):
    if not sieve[i]: prime_sum += i

print(prime_sum)