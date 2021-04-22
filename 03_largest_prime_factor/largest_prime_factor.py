# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
import math
N = 600851475143
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Find the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n /= 2
          
    # n must be odd at this point, skip the even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
print(maxPrimeFactors(N)) 