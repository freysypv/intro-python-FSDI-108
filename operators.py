# 1. Arithetic operators

x = 1
y = 2 
res = 0

res = x + y 
print(res)

res = x - y 
print(res)

res = x / y 
print(res)

res = x * y 
print(res)

#2 Assiment Operators - used to asing values to varieble
# means " put this inside the (varieble)"

x = 5
x += 5
x /= 3
x *= 3
x -= 3
print(x)

#3 comparison operator
#- used to compear two values
# same as if else
# == (equa; to), 1= (not equal), < >(<= =>)(less?greaterthan)


#4 Logica; Operator - used to combine conditional statemnts
# used with booleans true / false
# and -> Both must true
x = 3
y = 10
z = 3

print(x== y and y == z)# False, because both conditions mus tbe true
print(x == y == z) # or -> at least one must be true
print(not x == y) # not -> flios true to false (vice versa)

#5. Identity operators - used to compare the objjests, not they are the same
# but if the are actually the same objct
#is  -> checks if two things are the same
#is not -> check if they are not the same
x = 3
y = 4

print(x is y)
print(x is not y)

# 6 mebership  Operatort - used to test is a sequence is presented in an objecrt
# in -> check if something exist in a sequence (list)
#not in - > checks if something does not exist inside

x = [1, 3, 2, 4, 5, ] # this is a list
 
print(4 in x)
print(9 not in x)