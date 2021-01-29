'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def rule(num):
    if num%2 == 0:
        return int(num/2)
    else:
        return int(3*n + 1)

if __name__=="__main__":
    N = 1000000
    store = {1:4,2:2}
    i = 3
    
    while i < N:
        n = i
        sequence = [n]
        while n not in store:
            n = rule(n)
            sequence.append(n)
        l = len(sequence)
        for j in range(l-1):
            store[sequence[j]] = l - j + store[sequence[-1]] -1
        i += 1
        #print(len(sequence),sequence)
    
    maximum = 0
    for key in store:
        #print(key, store[key])
        maximum = max(maximum,store[key])
    
    maxkey = max(store, key=store.get)
    print(maxkey, "has the longest chain of value", maximum)
    
    '''
    while n:
        if n in store:
            i += 1
            break
        else:
            store[n] = 1
            if n%2 == 0:
                n = n/2
            else:
                n = 3*n + 1
            if n in store:
                for item in sequence:
                    store[item] = store[n] + 1
            else:
                store[n] = 1
                sequence.append(n)
                print(sequence, store)
                for item in sequence:
                    store[item] += 1
            i += 1
    '''
                
    