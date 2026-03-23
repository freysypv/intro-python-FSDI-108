# Dictionaries store data in key:value pairs.
# Written with curly brackets {}

students = {
    "name" : "leo",
    "age" : 23,
    "major" : "computer Science"
}
print(students)

#accesing items
print(students["name"])
print(students.get("major")) # another way to accesss

# Adding Items
students["graduation_year"] = 2025
print(students)

#Changing  Values
students["age"] = 25
print(students)

# removing Items
students.pop("major") #remove key value
print(students)

# check If a key exists
if "name" in students:
    print("key 'name' exists in the dictionary!")

# nested Dictionary
students = {
    "student1" : {"name" : "leo", "age":22},
    "student2" : {"name": "alex", "age": 21}
}
print()

report_card = {
    "name" : "Jose",
    "subject" : "python",
    "grade" : (90,85,88)

}
print( report_card ["name"])
print(report_card ["subject"])

res = 90 + 85 + 88
print(res)
res /=3
print(res)

grades = report_card ["grade"]
average = sum(grades) / len(grades)
print(f"Average Grade: {average:}")



report_card = {
    "name": "Pedro",
    "subject": "Python",
    "grades": (80, 90,100)
}
print(f"student:{report_card["name"]}, subject:{report_card["subject"]}")

report_card["average"] = sum(report_card["grades"]) / len(report_card['grades'])

if report_card["average"] >= 90:
    print("Excellent")
elif report_card["average"] >= 70:
    print("Good job")
else:
    print("need Improvement")

report_card.pop("subject")
print(report_card)



    
   # Assiment 2


#key values

bike = {
    "brand": "Honda",
    "model": "Cub 110cc",
    "Year": 1990,
   
}
print(f"int dictionary: {bike} length: [len(bike)]")

#2 getting values by key

bike_brand = bike["brand"]
print(f"bike brand is: {bike_brand}")

#3 adding new key values
bike["color"] = "red"
print(f"Dictionary after adding a color key:(bike) length: {len(bike)}")

#4 updating the key values
bike['year'] = 2024
print(f"Update year: {bike} length: {len(bike)}")

#5 removing key
bike.pop("model")
print(f"update dictionary:{bike} length:{len(bike)}")
