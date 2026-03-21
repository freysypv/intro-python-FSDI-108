print("Hello World from Python!") # No semocolons needed
print(2)
print(5+3)
print(True)


# shortcuts
#Sdave file ctrl + S
#run last command in terminal - up arrow
# comments /single line

"""
multi line  comments
idfioagffg
this too
"""

# variebles and concatenation

name = "Leo"
age = 23
print(name) #print the varieble value


# concatination (joininf strings with +)
# cancatination can't combine string and interger
#Fix it cast age to string using str()
print(" My name is " + name + " and I am " + str(age) + " years old " )

name = "Fre"
age = "37"
middle_name = "Job"
last_name = "pena"
found = "true"

print(name)
print ("my name is" + name + str(age) + "years old.")
print("Did he show up tp class?" + str(found))


# mini challege
 
name = "Martin"
place = "Park"
activity = "walking"
age = "5"


print( name + " was at the " + place + " with her dog " + activity + ". Her dog is " + str(age) )

# F-string
# Cleaner way to format strings
work = "sdgku"
job = "professor" 
#start with f "" varieble in {}

print(f"I work at {work} my job is {job}!")

# multi - line f-string
print (f"""
My name is {name} {middle_name} {last_name}
I like python!
    Type indentations

""")

# type function
print(type(name))  #<class 'str'
print(type(age))    #int
print(type(found)) #bool

# casting (changing data types)

print(20 + int ("20"))
print(20)
print(20 + 2.98)

# user input
# input() lets the user type values into the terminal
user_name = input("enter your name")
print(f"Hello, {user_name}")

print(input())

#input() always returns a string
print(input("enter your age:"))

#example: converting input to int
# new_age = int(input("enter your age: "))
# print(age + new_age)


#mini challege

pizzas_slices = int(input("enter pizza slices"))
people = int(input("enter how many people"))

slice_per_person = pizzas_slices / people

print(slice_per_person)







      
"""
echo "# intro-python-FSDI-108" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:freysypv/intro-python-FSDI-108.git
git push -u origin main
"""