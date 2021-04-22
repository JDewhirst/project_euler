'''
A Pythagorean triplet is a set of three natural number, a < b < c,
for which a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 =5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc
'''

# We could use itertools.combinations to generate all the combinations of three numbers up to 1000. That would be a lot of numbers though, just doing that might take more than a minute.

# SQR(1000) = 31.6..
# CBR(1000) = 10

# Better to generate all the numbers which sum to 1000 first ?
N = 1000

for i in range(1,N):
    for j in range(i+1,N):
        k = N - i - j
        if i**2 + j**2 == k**2: print(i,j,k, i*j*k)