'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1+2+...+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025-385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# sum(i**2) - sum(i)**2 i 1 to 100

numbers = [i for i in range(1,101)]
squares = [num**2 for num in numbers]

print(sum(numbers)**2 - sum(squares))