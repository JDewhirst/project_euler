'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

''' notes
Two number a and b
We can ignore when a = b
we can ignore when either a or b have trailing 0's 
'''

palindrome = 0

for i in range(999,100,-1):
    for j in range(999,100,-1):
        if (i%10 !=0) and (j%10 != 0) and (i != j):
            number = i*j
            string = str(number)
            if string == string[::-1]:
                if number > palindrome:
                    palindrome = number
                    
print(palindrome)
            