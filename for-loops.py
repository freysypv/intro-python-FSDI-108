"""
A for loop in python is a control structure that lets you repest a block of code for 
each item in a sequence ( such as list, string, tuple, range of numbers ect...)

for variable in sequence:
    #code block runs for each item in the sequence
"""

#basic example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for letter in "Leopoldo":
    print(letter)

print("______________________________")

# range() genarates a sequence of numbers
for x in range(5): # index by 0
    print(x)

print("______________________________")

#star and end range

for x in range(2, 6):
    print(x)


print("__________________________")    

#step
for x in range(0, 10, 2):
    print(x)


#mini challenge
# print("pick a number:")
num = int(input("Enter number:"))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
    

