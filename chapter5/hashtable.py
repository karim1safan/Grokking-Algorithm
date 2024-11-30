# hash table of production price
book = dict() # empty hash table
phone_book = {} # same as dict()

# hash table has key and value
book['apple'] = 0.67
book['milk'] = 1.49
book['avocado'] = 1.49

phone_book['police'] = 111
phone_book['emergency'] = 123


print(book)
print(book['avocado']) # O(1)