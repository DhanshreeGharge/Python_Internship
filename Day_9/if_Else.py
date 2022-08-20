no1 = 10
no2 = 10
no3 = 30
"""
if condition:
    statement 
"""

if no1 > no3 :
    print("No1 is greater than No3")

if no2 < no3 :
    print("No2 is smaller than no3")

# using if elif
if no1 > no2:
    print("No1 is greater than No2")
elif no2>no3 :
    print("No2 is greater than No3")
elif no1 == no2 :
    print("No1 is equal to No2")
else :
    print("Wrong Output")

#using if else
if no1 > no3 :
    print("No1 is greater than No3")
else :
    print("No3 is greater than No1")

#Short hand if
if no3 > no1 : print("No3 is greater than No1")

#Short if else
print("No1 is greater than No3") if no1 > no3  else print("No1 is Smaller than No3")

#Using and keyword (logical operator)
if no1 == no2 and no1 < no3:
    print("N1 and N2 both are equal, and No1 is less than No3")