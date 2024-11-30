def find_max(arr):
  if len(arr) == 0:
    return 0
  elif len(arr) == 1:
    return arr[0]
  elif len(arr) == 2:
    if arr[0] > arr[1]:
      return arr[0]
    else:
      return arr[1]
  else:
    mx = find_max(arr[1:])
    if (arr[0] > mx):
      return arr[0]
    else:
      return mx

print(find_max([20,10,2,100,1])) # 100
print(find_max([20])) # 20
print(find_max([50,10])) # 20
print(find_max([])) # 0