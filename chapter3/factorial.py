def fact(n):
    if n == 1: # base case 
        return 1
    else:
        return n * fact(n - 1) # recursive case
    
print(fact(3))
