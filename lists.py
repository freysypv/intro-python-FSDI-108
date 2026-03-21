#lists are used to store mult items in a single variable.
#Think of a container that can hold many items
#list are written with square brackets []
 
my_list = [10, 20, 30, 40, 50]
# print(my_list)

# list can contain dufferent data type
mixed_list = [1, "apple", 3.5,]
print(mixed_list)

# you can access list items by their Index number
#(insdexing starts at 0)

fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # first item (apple)
print(fruits[2])

#you can also use a Negative indexes to count from the end
print(fruits[-2])


# Modifying list items
fruits[1] = "mango"
print(fruits)

# adding items
fruits.append("orange") # add to the end
print(fruits)

fruits.insert(1,"kiwi")

# remove item  by values (you can selete the item you want to remove)
fruits.remove("apple")
print(fruits)

#removes the last item
fruits.pop()
print(fruits)

#looping through a list
for fruit in fruits:
    print(fruit)

# check if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

#list length
print(len(fruits))# return number of items in container





                    # Assiment 2

# add  coment assiment/ print out every step 


# list creation
planets = [ "Mars", "Venus", "Mercury", "Earth","Saturn", "Jupiter"]
print(f"list; {planets} length: {len(planets)}")

#Printing the third planet mercury
third_planets = planets[2]
print(f"The third planet is: {third_planets}")

# Changing Earth to My green home sweet home!

planets[3] = "My green home, Sweet home!"
print(f"New list:{planets} length: {len(planets)}")

#Removing a planet
planets.remove("Venus")
print(f"List without Venus: {planets} length: {len(planets)}")

#remove planets with .pop
planets.pop(0)
print(f"List after rimoving first planet:{planets} length:{len(planets)}")