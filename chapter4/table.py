def multiplication_table(arr):
  # time complexity: O(N*N) => O(N^2)
  for i in arr: # O(N)
    for j in [2, 3, 7, 8, 10]: # O(N)
      res = i * j
      print(res)

multiplication_table([1,2,3])