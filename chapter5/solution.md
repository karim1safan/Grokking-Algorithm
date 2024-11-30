### Which of these hash functions are consistent? 
`Hint: consistent means the same output for the same input`
#### 5.1 `f(x) = 1`
- consistent
#### 5.2 `f(x) = rand()`
- not consistent
#### 5.3 `f(x) = next_empty_slot()`
- not consistent
#### 5.4 `f(x) = len(x)` 
- consistent
----------------------------------------------------------
### Suppose you have these four hash functions that work with strings:
##### (A) Return “1” for all input.
##### (B) Use the length of the string as the index.
##### (C) Use the first character of the string as the index. So, all strings starting with a are hashed together, and so on.
##### (D) Map every letter to a prime number: `a = 2, b = 3, c = 5, d = 7, e = 11`, and so on. For a string, the hash function is the sum of all the characters modulo the size of the hash. For example, if your hash size is 10, and the string is “bag”, the index is `3 + 2 + 17 % 10 = 22 % 10 = 2`.

#### 5.5 A phonebook where the keys are names and values are phone numbers. The names are as follows: Esther, Ben, Bob, and Dan.


----------------------------------------------------------
#### 5.6 A mapping from battery size to power. The sizes are A, AA, AAA, and AAAA.
**<ins>answer</ins>**
- The correct answer is `B` and `D`
```
- Assume a hash table size of 10 slots
- If we applied (B) hash function -> no collision 
  -> len(A) = 1, len(AA) = 2, len(AAA) = 3, len(AAAA) = 4
if we applied (D) hash function -> no collision
- a = 2 
A => 2*1 % 10 = 2 % 10 = 2
AA => 2*2 % 10 = 4 % 10 = 4
AAA => 2*3 % 10 = 6 % 10 = 6
AAAA => 2*4 % 10 = 8 % 10 = 8
```
----------------------------------------------------------
#### 5.7 A mapping from book titles to authors. The titles are Maus, Fun Home, and Watchmen.
**<ins>answer</ins>**
- The correct answer is `B`, `C` and `D`
```
- If we applied (B) hash function
str[0] = M, F, H, W -> no collision

- If we applied (D) hash function
Maus -> (39+2+) % 10 = 
Fun -> () % 10 = 
Home -> () % 10 = 
Watchmen -> () % 10 = 
```