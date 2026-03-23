#sets are used to store multiple items in a single varieble.
#sets are unordered and unindexed and have no duplicates

# sets are written with curly brackets {}
fruits = {"apple", "banana", "cherry"}
print(fruits)

# no duplicates allowed
fruits = {"apple", "banana", "apple"}
print(fruits) # ignores duplicates

# check if item exists
print("banana" in fruits)

# adding items
fruits.add("orange")
print(fruits)

# adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

#removing items
fruits.remove("banana")
print(fruits)

# if you are not sure the item exist use discard()
fruits.discard("kiwi")
print(fruits)

# Set operations (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # combinie both (no duplicates) to add more , then set3, set4 ect
print(set1.intersection(set2)) # commen elements will be print
print(set1.difference(set2)) #Whats only in set1

#mini chalenge party guest

invited_friends = {"Alex", "sam", "Leo", "Nina"}
rsvped = {"Nina", "sam", "Jordan"}
print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))

invited_friends.update(["jose", "Mary"])
print(invited_friends)

rsvped.discard("sam")

print(rsvped)
print(len(invited_friends))

if "Leo" in rsvped:
    print("Here is leo")
else:
    print("Leo is not coming!")