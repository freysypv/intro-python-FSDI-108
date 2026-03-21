# is boolian

#if -> checks a condition
# elif -> (else if) checks another condition if the first is falsde
# else -> runs if all other connditions are false


# if file or varible is mostly types hit tab once to auto complite

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

    # short hand if statements
if x > 5: print("x is greater than 5")

#short hand if ... else
print("Even") if x % 2 == 0 else print("odd")

#nested If statements

if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

#combining Condition
age = 18

if age >= 18 and age <=21:
    print("you are between 18 and 21 years old!")


"""
MINI Challenge
1. ask user to enter today's temperature in farenheit and store it in a varieble calles tempeerature
2. use i- elif-else statements to classify the temperature:
if themp >= 86, and temp """

print("Enter temperature in fahrenheit")

temperature = int(input("Enter temperature in fahrenheit"))

if temperature >= 86: print("it is hot outside!")

elif temperature >= 68 and temperature < 86: print("Weather is nice.")

if temperature >= 50 and temperature < 68: print("it's a bit chilly")

elif temperature < 50: print("It is cold!")


