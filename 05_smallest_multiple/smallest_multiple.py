'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Any number that is evenly divisible by 2520 is also
# evenly divisible by 1,2,3,4,5,6,7,8,9,10
# The number must be a multiple of 20,
# increment by 20 in search

a = [i for i in range(11,21)]
a.append(2520)
not_divisible = True

i = 2520
while not_divisible:
    current = True
    for number in a:
        if (i % number) != 0:
            current = False
            break
    if current:
        break
    i += 20
    #print(i)
        
print(i)