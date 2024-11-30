def my_count(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return 1
  return 1 + my_count(arr[1:])

print(my_count([1,2,3,4])) # 4
print(my_count([])) # 0
print(my_count([1])) # 1

# [] => 0
# [1] => 1
# [1,2] => 2
# [1,2,3] => 3
# [1,2,3,4] => 4