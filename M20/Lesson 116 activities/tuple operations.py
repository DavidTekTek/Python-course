#create a tuple with different data types
tuplex = ("tuple", False, 4.1, 1)
print(tuplex)

#create a tuple
tuplex = (4, 9, 2, 8, 3, 1) 
print(tuplex)

#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurrences of item 60 from a tuple
tuple1 = (80, 10, 60, 70, 60)
print(tuple1.count(60))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index is exclusive
_slice = tuplex[3:5]
print(_slice)

#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)