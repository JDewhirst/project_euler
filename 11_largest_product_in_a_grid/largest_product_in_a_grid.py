'''
In the 20×20 grid (see input.txt) what is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

'''
import sys
from math import prod

def ReadIn():
    return [list( map(int,line.strip("\n").split() ) ) for line in sys.stdin]
    
def Row(arr,window):
    X = len(arr[0]) #cols
    Y = len(arr) #rows
    max_prod = 0
    for row in arr:
        i = 0
        while i<(X-window+1):
            #print(i)
            if 0 in row[i:i+window]:
                i += row[i:i+window].index(0)
            else:
                new_product = prod(row[i:i+window])
                max_prod = max(max_prod, new_product)
            i += 1
                
    return max_prod

def Column(arr, window):
    X = len(arr[0]) # columns
    Y = len(arr) # rows
    max_prod = 0
    for i in range(Y-window+1):
        for j in range(X):
            new_product = 1
            for k in range(window):
                new_product *= arr[i+k][j]
            max_prod = max(max_prod, new_product)
    
    return max_prod
    
def Diagonal(arr,window):
    X = len(arr[0]) # columns
    Y = len(arr) # rows
    max_prod = 0 
    for i in range(X-window+1):
        for j in range(Y-window+1):
            new_product = 1
            for k in range(window):
                new_product *= arr[j+k][i+k]
            max_prod = max(max_prod, new_product)
            
    for i in range(X -window+1):
        for j in range(window-1,Y):
            new_product = 1
            for k in range(window):
                new_product *= arr[j-k][i+k]
            max_prod = max(max_prod, new_product)

    return max_prod


if __name__=="__main__":

    grid = ReadIn()
    #for line in grid:
    #    print(line)
        
    window = 4
    ''''
    test = [[ i for i in range(10)],
            [ i for i in range(10)],
            [ i for i in range(10)],
            [ i for i in range(10)]]
    print(test)
    print("rowise",Row(test,window))
    print("columnwise",Column(test,window))
    print("diagonal",Diagonal(test,window))
    '''
    greatest_prod = 0
    cur_prod = Row(grid,window)
    if greatest_prod < cur_prod: greatest_prod = cur_prod
    print("rowise",cur_prod)
    

    cur_prod = Column(grid,window)
    if greatest_prod < cur_prod: greatest_prod = cur_prod
    print("columnwise",cur_prod)
    

    cur_prod = Diagonal(grid,window)
    if greatest_prod < cur_prod: greatest_prod = cur_prod
    print("diagonal",cur_prod)
    
    print("greatest",greatest_prod)
   
    
    
                
            
    