#Find the sum of all the multiples of 3 or 5 below 1000.

# multiples = []
# for i in range(1,1000):
    # if (i%3 == 0) or (i%5 == 0):
        # multiples.append(i)

# print(sum(multiples))

#you could also do this cutting out the middle man. Just add i to a
#variable init at 0 everytime it's true, cuts out all the appending

# Faster way
# Calc sum of all numbers divisible by 3 = a
# Calc sum of all numbers divisible by 5 = b
# Calc sum of all numbers divisible by 15 = c 
# Result = a + b - c
#  1+2+3+...+p=0.5*p*(p+1)

r = 999
def SumDivisibleBy(n):
    p = r // n 
    return n * ( p *(p+1) ) // 2
    
print( SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15) )