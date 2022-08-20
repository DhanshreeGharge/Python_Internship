#Set is a collection of Unique values
import numbers


set1 = {"Apple", "Mango", "Banana", "Apple", 10, 20.5}
print(set1)

print(len(set1))

#set constructor
set_Constructor = set(("Pink", "Black", "White"))
print(set_Constructor)

print("Pink" in set_Constructor)

#for loop
for color in set_Constructor:
    print(color)

#add() method
set_Constructor.add("Yellow")
print(set_Constructor)

# set_Constructor.add("Purple", "Blue", "Sky")

#update() method
set2 = {10, 20, 30, 40, 50}
set_Constructor.update(set2) 
print(set_Constructor)

list1 = [11, 21, 31, 41, 51]
set_Constructor.update(list1)
print(set_Constructor)

#using remove() method
set_Constructor.remove(11)
set_Constructor.remove("Yellow")
# set_Constructor.remove("Yellow")  - it will throw error
print(set_Constructor)

set_Constructor.discard("Yellow")   #- it will not throw error
print(set_Constructor)

#remove last element of the set
books = {"Java", "Python", "C", "C++"}
print(books.pop())
print(books)

books.clear()
print(books)

del books
# print(books)

#union() method
Numbers = {101, 102, 103, 104, 105, 101, 101}
Strings = {"Shankar", "Snehal", "Pranjal", "Shankar", 101, 102}
combine_Set = Numbers.union(Strings)
print(combine_Set)

Numbers.intersection_update(Strings)
print(Numbers)

duplicate_values = Numbers.intersection(Strings)
print(duplicate_values)

Numbers.symmetric_difference_update(Strings)
print(Numbers)