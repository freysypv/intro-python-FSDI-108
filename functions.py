"""
A function is a block of code that only runs when its called
we can pass data to function (parameters), and they can return data

def function_name(parameters):
    #code block (indented)
    #preform actions using the parameters
    return value # optional

"""

# Simple function without parameters

def my_function():
    print("This is my function") # this runs when the fuction is called

my_function()  # call function

def other_function():
    print("This is another function")


other_function()

# a function can be call mult times
my_function()

# function with parameters
def print_full_name(first_name, last_name, middle_name):
   print(f"the name is: {first_name} {last_name} {middle_name}")

print_full_name("Fre", "Pena", "T")

#functions that return values
#insted of just printing functions can send back (return)data

def get_full_name(fname, lname):
    return f"{fname} {lname}" #sends back the full name as text

# Store returned value in a varieble
full_name = get_full_name("freysy",  "pena")
print(full_name)

# function with default parameters
#A defaul parremeter means the function will use that value
# if no argument is provided when calling the funbction

def greet(name="student"):
    print(f"Hello, {name}! Welcome to class!")

#calling with no argument -> use the default
greet()

# calling with AGUMENT -> OVERRIDES THE DEFAULT
greet("Leo")

