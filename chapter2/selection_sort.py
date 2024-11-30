def findSmallest(arr):
    smallest_value = arr[0] # suppose the smallest value is the first value
    smallest_index = 0 # the index of the smallest value 

    for i in range(1, len(arr)): # start from 1 not 0 
        if arr[i] < smallest_value: # find the smallest value 
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_value = findSmallest(arr)
        newArr.append(arr.pop(smallest_value))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
