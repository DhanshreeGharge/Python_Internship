#Dictionary in python = english to marathi dictionary
#It is collection of key value pairs
# Dict1 = {"key":"value","key2":"value2"}


Employee = {
  "name": "shiv",
  "designation": "software",
  "experience": 3,
}
print(Employee)
# print(type(Employee))

#Dictionary do not allow duplicate keys, if dictionary contains duplicate keys then it always trys to hold the recent value. i.e. Shiv
Employee = {
  "name": "shiv",
  "designation": "software",
  "experience": 3,
  "name" : "Shiv"
}
print(Employee)

# Keys with different cases are always treated as a different
# Here name and NAME are different
# Keys in dictionary are always case-sensitive
Employee = {
  "name": "shiv",
  "designation": "software",
  "experience": 3,
  "NAME" : "Shiv",
  "colors" : ["Black", "Orange", "Pink"]
}
print(Employee)

print(len(Employee))

#Accessing the Dictionary items by using keys
print("colors", Employee["colors"])

#Accessing dictionary items using get() method
print(Employee.get("colors"))

#Obtaining all the keys using keys() method
employee_keys = Employee.keys()
print(employee_keys)

#Obtaining all the values using values() method
employee_values = Employee.values()
print(employee_values)

#changing the values of dictionary
Employee["designation"] = "Khatarnak Programmer"
print(Employee["designation"])

#Obtaining all the items using items() method
employee_items = Employee.items()
print(employee_items)

#checking whether a key exist or not
print("name" in Employee)

#update() method - adding a new key value in dictionary
Employee.update({"join_year": 2020, "Salary" : 50000000})
print(Employee)

#deleting key value pair using pop() method
Employee.pop("Salary")
print(Employee)

#removing the last item in dictionary using popitem() method
Employee.popitem()
print(Employee)

#removing item from dictionary using del keyword
del Employee["colors"]
print(Employee)

#removing all items from the dictionary using clear() method
Employee.clear()
print(Employee)

student = {
    "Name" : "Sameer", 
    "Roll_no" : 101,
    "Department" : "Civil",
    "college" : "GPP"
}
print(student)

department = {
    "Name" : "Computer",
    "Years" : 3,
    "Subject" : ["java", "C", "C++"]
}
print(department)

student1 = student.copy()
print(student1)

student1.update(department)
print(student1)

#create dictionary of computer class - Nested Dictionary
Student_3 = {"Name" : "Shubhra", "Roll No": 103}
computer_class = {
    "Student_1" : {"Name" : "Shiv", "Roll no" : 101 },
    "Student_2" : {"Name" : "Snehal", "Roll no" : 102},
    "Student_3" : Student_3
}
print(computer_class)