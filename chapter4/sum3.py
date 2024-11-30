# sum numbers from 1 to n using recursive way
def my_sum(n):
  if n == 0 or n == 1:
    return 1
  return n + my_sum(n-1)

print(my_sum(5)) # 15
