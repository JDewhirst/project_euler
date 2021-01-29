'''
Work out the first ten digits of the sum of the one-hundred 50-digit numbers in input.txt
'''

# python handles big integers natively. 
# So this is easy but boring

import sys

nums = []
for line in sys.stdin:
    nums.append(int(line.strip("\n")))
    
print(nums)
s = sum(nums)
s = str(s)
print(s[:10])