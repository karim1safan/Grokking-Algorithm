def binary_search(list, item):
    low = 0 # start = 0 
    height = len(list) - 1 # end = 5 - 1 = 4

    while low <= height: # 0 <= 4
        mid = (low + height) // 2 # (0 + 4) // 2 = 2
        guess = list[mid] # list[2] = 5
        
        if guess == item: # 5 == 3
            return mid
        elif guess > item: # 5 > 3
            height = mid - 1 # height = 2 - 1 = 1
        else:
            low = mid + 1
    return None
    
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # index: 1
print(binary_search(my_list, -1)) # None