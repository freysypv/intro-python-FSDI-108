# Tuples are just like lists - they can store multiple items
# but !! they are immutable( you canot change them after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)


# accessing items
print(my_tuple[0])
print(my_tuple[2])

# Check it item exists
if "apple" in my_tuple:
    print("Yes, apple is in the tuple")

# length of a tuple
print(len(my_tuple))  

# Single item tuple
# You must add a comma at the end or python won't reconise as a tuple
single = ("grape")
print(type(single)) # this is a string
tuple = ("water",)
print(type(tuple)) # this is a tuple

# nested tuples
tuple1 = ("a", "b", "c")
tuple2 = ("1", "2", "3")
combine = (tuple1, tuple2)
print(combine)

#mini challege travel gag

travel_bag  = ("ID",("phone", "headphones", "shoes", "money"))
print(travel_bag[1])
print(travel_bag[3])

if "shoes" in travel_bag:
    print("You are ready to walk!")
else:
    print("You forgot your shoes")

essentials = ("medical kit", "toiletries", "sunglasses")  
final_bag = (travel_bag, essentials) 


print(len("travel_bag)", "essentials"))
print("final_bag")




