"""
A while loop reapts a block of code as a conditon is true.
Be Carfull- if the condition never becames false, you will get a infinite loop

whle condiction:
    # code block runs as long condition is true
"""

count = 1
while count <= 5:
    print("Count is: ", count)
    count += 1
    count += 1 #assignment operator which adds 1 and loop stop at =5

    # using Break to stop the loop

    number = 0
    
    while True:
        print(number)
        number += 1
        if number == 3:
            break # stops the loop when it gests to 3

# using continue to skip an iteration
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue # skip
    print(count)

# else with while loop
# # the else block runs when the loop condition becames False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop has finished")

# mini challenge password checker
# password = int(input("Enter passward"))

password = ""  # empty string
while password != "secret123": # keeps while password is wrong
    password = input("Enter the password:")
    if password != "secret123": #if wrong
        print("Wrong! Try again.")
#once they enter the corect password
print( "Access granted")










