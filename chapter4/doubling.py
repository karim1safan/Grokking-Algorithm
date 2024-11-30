def doubling(arr):
  for i in range(0, len(arr)): # O(N)
    arr[i] *= 2
  return arr

def doubling2(arr):
  arr[0] *= 2 # O(1)
  return arr

print(doubling([1,2,3])) # 2, 4, 6
print(doubling2([1,2,3])) # 2, 2, 3