from time import sleep

def print_items1(list):
  for item in list: # O(N)
    print(item)

def print_items2(list): # O(N)
  for item in list:
    sleep(1)
    print(item)

print(print_items1([2,4,6,8,10]))
print("------------------")
print(print_items2([2,4,6,8,10]))


# Which one do you think will be faster in practice?
'''
I think print_items
will be much faster because it doesn’t pause for 1 second before printing
an item
'''

# quick sort and merge sort have the same time complexity O(N log N)
# quick sort in worst case O(N^2)
# Quicksort doesn’t check to see whether the input array is already sorted

'''
O(C*N)

C: constant number
N: number of operations

10 millisecond * N => print_item1() -> O(N)
1 sec * N => print_item2() -> O(N)

Quicksort has a smaller constant than merge sort.
So if they’re both O(n log n) time, quicksort is faster

'''