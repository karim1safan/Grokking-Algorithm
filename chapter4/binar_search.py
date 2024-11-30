def bsearch(arr, left, right, target):

  if left > right:
    return False

  mid = (left + right) // 2 
  
  if arr[mid] == target:
    return True
  elif (arr[mid] > target):
    return bsearch(arr, left, mid - 1, target)
  else:
    return bsearch(arr, mid + 1, right, target)

arr = [1, 3, 5, 7, 9]
item = bsearch(arr, 0, len(arr) - 1, 4)

if item :
  print("Item found")
else:
  print("Item not found")


'''
binary search
arr = [10, 2, 4, 12, 20], target = 12
sort(arr)
[2, 4, 10, 12, 20]
left = 0, right = 4, mid = left + right // 2 = 2
arr[mid] = 10 

1- arr[mid] == target
  return mid
2- arr[mid] > target
  mid = right + 1
3- arr[mid] < target
  mid = lef - 1

'''