#List using Constructor
from os import remove
from turtle import clear


fruitList = list(("grapes", "grapes", "banana", "apple", "Mango", "Chiku", "apple", "cherry", "orange", "kiwi", "mango"))
print(fruitList)

fruitList_without_using_constructor = ["grapes", "banana", "apple"]
print(fruitList_without_using_constructor)
print(type(fruitList_without_using_constructor ))

mixed_list = list(("Rahul", 16, 55, "Pune" ))
print(mixed_list)
print(type(mixed_list))

#changing the elements
fruitList[0] = "Mango"
print(fruitList)

fruit_list = ["apple", "cherry", "orange", "kiwi", "mango", "apple", "cherry", "orange", "kiwi", "mango"]
print(fruit_list)

fruit_list=["Mango", "Kiwi", "Guava"]
print(fruit_list)

fruit_list[1:3] = ["Grapes"]
print(fruit_list)

#Using insert() method
fruit_list.insert(2, "Apple")
print(fruit_list)

#using apppend() method to insert new element at the end of the list
fruit_list.append("Orange")
print(fruit_list)

#using extend() method
extended_list = fruit_list.extend(mixed_list)
print(extended_list)

list1 = ["Rahul", "Ramesh", "Shyam"]
list2 = ["Ganesh", "Sachin"]

list1.extend(list2)
print(list1)

tuple1 = ("Rahul", "Ramya", "Rakesh", "Snehal")

list1.extend(tuple1)
print(list1)

#remove() method
list1.remove("Rahul")
print(list1)

#pop() method
list1.pop()
print(list1);

#del keyword - deleting first item of list
del list1[0]
print(list1)

#delete complete list
del list1
del tuple1

#empty the list using clear() method
print("list2 = ", list2)
list2.clear()
print("list2 = ", list2)

print(len(list2))
# list2[0] = "Apple"
# print(list2)

list2.insert(0, "Apple")
print(list2)

#copy() method
new_list1 = ["Apple", "Mango"]
new_list2 = ["Banana", "Cherry"]
# new_list2 = new_list1
new_list2 = new_list1.copy()
print(new_list2)
new_list2.insert(2, "Rahul")
print(new_list1)