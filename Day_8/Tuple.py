Tuple1 = ("Apple", "Banana", "Cherry", "Banana", 10, 20, 30, 10.2)
print(Tuple1)

#len()
print(len(Tuple1))

#Creating tuple using tuple() constructor
tuple2 = tuple(("Rahul", "Ramesh", "Ramya"))
print(tuple2)

#Single element tuple 
tuple3 = ("One")
print(tuple3)
print(type(tuple3))

tuple4 = ("one",)
print(type(tuple4))

print(Tuple1[2])

#tuple is unchangable, we cant asign the value to the tuple after creating it.
# tuple4[1] = "Two"
# print(tuple4)

#Converting tuples to list for modifying purpose
list1 = list(tuple2)
list1.insert(2, "Sameer")
new_tuple = tuple(list1)    #Converting tuple into list
print(new_tuple)

#Packing of tuple
fruits = ("Apple", "Banana", "Cherry")

#Unpacking of tuple
(fruits1, fruits2, fruits3) = fruits
print(fruits1, fruits2, fruits3)

colors = ("Red", "Pink", "Black", "White", "Blue", "Purple")
(red, pink, black, *others) = colors
print(red, pink, black, others)

(red1, pink1, *others1, blue, purple) = colors
print(red1, pink1, others1, blue, purple)

t_colors = ("Black", "White", "Red")
t_numbers = (10, 20, 30, 40, 30 ,30, 40, 30 ,30, 40, 30 ,30, 40, 30 ,30, 40, 30 ,30, 40, 30 ,30, 40, 30 ,30)

combine_tuple = t_colors+t_numbers
print(combine_tuple)

repeated_tuple = t_colors * 3
print(repeated_tuple)

#count() 
print(t_numbers.count(30))

#index()
print(t_numbers.index(30))