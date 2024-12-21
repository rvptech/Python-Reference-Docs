
# A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")   # To add one item to a set use the add() method.
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"} 
thisset.update(tropical)  # To add items from another set into the current set, use the update() method
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")   # To remove an item in a set, use the remove(), or the discard() method.
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()   # The clear() method empties the set.
print(thisset) 


thisset = {"apple", "banana", "cherry"}
del thisset   # The del keyword will delete the set completely.
print(thisset)


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)   # Loop through the set, and print the values
  

# Union 

# The union() method returns a new set with all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# Join Multiple Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# Join a Set and a Tuple

# The union() method allows you to join a set with other data types, like lists or tuples.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# Update

# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Intersection

# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)


# Difference

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)


# Use the difference_update() method to keep the items that are not present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)


# Symmetric Differences

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


# Use the symmetric_difference_update() method to keep the items that are not present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

