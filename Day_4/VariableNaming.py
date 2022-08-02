#Variable naming Rules
myvar = "Shiv"
my_var = "Shiv"
_my_var = "Shiv"
myVar = "Shiv"
MYVAR = "Shiv"
myvar2 = "Shiv"

"""
#Invalid Variable Names
2myvar = "Shiv"
my-var = "Shiv"
my var = "Shiv"
"""
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(myvar2)
print(MYVAR)

"""
print(2myvar)
print(my-var)
print(my var)
"""

# the way to write variables:  a=50; b="Dhanshree"; c=3.14

#Assigning Multiple Values to Multiple Variables
col1, col2, col3 = "red", "orange", "green"

print(col1)
print(col2)
print(col3)

#Assigning one Value to Multiple Variables
col1= col2= col3 = "White"
print(col1)
print(col2)
print(col3)

#Assigning values from list to variables
colors=["White", "Black", "Pink"]
col1, col2, col3 = colors;
print(col1)
print(col2)
print(col3)

#Uses of + operator
#Multiple Variables in one statements
x = "Shiv "
y = "is "
z = "awesome"
print(x + y + z)
print(x , y , z)


x = 1000
y = 10
print(x + y)

"""
x = 100
y = "shiv"
print(x + y)
"""

