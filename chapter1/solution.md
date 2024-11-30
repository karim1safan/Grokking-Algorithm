#### 1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

**<ins>solution</ins>**
```
n = 128 names     steps = ???

log2 (128) = x

2 ^ x = 128

2 ^ x = 2 ^ 7

base == base -> exp. = exp.

x = 7             steps = 7
```
---------------------------------------------------------
#### 1.2 Suppose you double the size of the list. What’s the maximum number of steps now?

**<ins>solution</ins>**
```
n = 128 * 2 names         steps = ???

log2 (256) = steps

2 ^ steps = 256 

2 ^ steps = 2 ^ 8

base == base -> exp. = exp.

steps = 8
```
---------------------------------------------------------
### Give the run time for each of these scenarios in terms of Big O

#### 1.3 You have a name, and you want to find the person’s phone number in the phone book. 

**<ins>solution</ins>** 

1) Simple Search Algorithm
    - Best Case Scenario  : `O(1)`
    - Worst Case Scenario : `O(N)`

2) Binary Search Algorithm
    - Best Case Scenario  : `O(1)`
    - Worst Case Scenario : `O(log N)`
---------------------------------------------------------
#### 1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

**<ins>solution</ins>**

Simple Search Algorithm [Linear Search]
- Best case : `O(1)`
- Worst case: `O(N)`

---------------------------------------------------------

#### 1.5 You want to read the numbers of every person in the phone book.

**<ins>solution</ins>**
- `O(N)`

---------------------------------------------------------

1.6 You want to read the numbers of just the A character. 

**<ins>solution</ins>**
```
- The letters in english are 26 characters

- N / 26 => no. of names start with A

- N => no. of persons in the phone book

- k = 26

- O(N / 26) ==> O(N / K)

- K is constant (we ignore const. numbers)

- O(N)
```