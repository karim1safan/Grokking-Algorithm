def quicksort(arr):
  if len(arr) < 2: # base case
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot] # all elements less than the pivot
    greater = [i for i in arr[1:] if i > pivot] # all elements greater than the pivot
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

# speed of algo. dependent on the pivot you choose
