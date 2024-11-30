# def bsearch(arr, left, right, target):
#   left = 0
#   right = len(arr) - 1
#   mid = (left + right) // 2 
  
#   if arr[mid] == target:
#     return True
#   elif (arr[mid] > target):
#     bsearch(arr, left, mid - 1, target)
#   else:
#     bsearch(arr, mid + 1, right, target)
#   return False

# arr = [1, 3, 5, 7, 9]
# print(bsearch(arr, 0, len(arr) - 1, 3))



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