#### 4.1 Write out the code for the earlier sum function.

**<ins>solution</ins>**

```py
def my_sum(arr):
  if len(arr) == 0: # base case
    return 0
  elif len(arr) == 1: # base case
    return arr[0]
  return arr[0] + my_sum(arr[1:]) # recursive case
```

---

#### 4.2 Write a recursive function to count the number of items in a list.

**<ins>solution</ins>**

```py
def my_count(arr):
  if len(arr) == 0: # base case
    return 0
  elif len(arr) == 1: # base case
    return 1
  return 1 + my_count(arr[1:]) # recursive case
```

---

#### 4.3 Find the maximum number in a list.

**<ins>solution</ins>**

```py
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
```

---

#### 4.4 Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

**<ins>solution</ins>**

```py
def bsearch(arr, left, right, target):

  # base case
  if left > right:
    return False

  # recursive case
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
```

---

## How long would each of these operations take in Big O notation?

#### 4.5 Printing the value of each element in an array.

**<ins>solution</ins>**

```py
for item in arr: # O(N)
  print(item)
```

---

#### 4.6 Doubling the value of each element in an array.

**<ins>solution</ins>**

```py
for i in range(0, len(arr)): # O(N)
  arr[i] *= 2
```

---

#### 4.7 Doubling the value of just the first element in an array.

**<ins>solution</ins>**

```py
def doubling2(arr):
  arr[0] *= 2 # O(1)
```

---

#### 4.8 Creating a multiplication table with all the elements in the array. So if your array is [2, 3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 3, then by 7, and so on.

**<ins>solution</ins>**

```py
def multiplication_table(arr):
  # time complexity: O(N*N) => O(N^2)
  for i in arr: # O(N)
    for j in [2, 3, 7, 8, 10]: # O(N)
      res = i * j
      print(res)
```
