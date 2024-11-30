# Recursive Way
def my_sum(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  return arr[0] + my_sum(arr[1:])


print(my_sum([2,4,6])) # 12

'''
When you’re writing a recursive function involving an array, the base case is
often an empty array or an array with one element. If you’re stuck, try that first
'''