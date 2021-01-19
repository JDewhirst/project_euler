#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

evenFibNums = []
sumOfEvenFibNums = 2
prev1 = 1
prev2 = 2
while prev2 < 4000000:
    nextVal = prev1 + prev2
    #print(prev1,prev2,nextVal)
    if nextVal%2 == 0:
        sumOfEvenFibNums += nextVal
    prev1 = prev2
    prev2 = nextVal
    
print(sumOfEvenFibNums)
