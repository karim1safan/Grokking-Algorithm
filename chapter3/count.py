def countdown(i):
    print(i)
    if i <= 0: # base case
        return
    else:
        countdown(i - 1) # recursion case


countdown(5) 