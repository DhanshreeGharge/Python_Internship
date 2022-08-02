from ast import NotIn


string1="hello i am shiv and i as software engineer"
print(string1[0])
print(len(string1))

#to check the character is present in the given string
print("software"in string1)

string2="10 20 30 40 50 60 70 80 90 100"
result="10"in string2

print(result)

Notinresult="angular" not in string1
print(Notinresult)

#String Slicing
print(string1[0:5])
print(string1[:5])      #string slicing from start
print(string1[31:])     ##string slicing to the End

#Negative string slicing
print(string1[-17:-12])
"""
engineer positive indexing=0 1 2 3 4 5 6 7 8
engineer negative indexing=-8 -7 - 6 -5 -4  -3 -2 -1
"""
