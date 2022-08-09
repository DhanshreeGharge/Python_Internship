String1 = "Python"
string2 = "Intership"
space = " "
result =  String1 +space+ string2
print(result)

#String Format Method
name = "My name is Dhanshree, and i am {} years old, I like {}"
print(name.format(18,"choclate"))

"""
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Format


"""

#Any string is always True, Any Number is always true
#empty strings are false, 0 is false

print(bool())
print(bool("is this true"))
print(bool(1234))
print(bool(0))
print(bool(""))

print(bool(()))
print(bool([]))
print(bool({}))
print(bool(False))
print(bool(None))
