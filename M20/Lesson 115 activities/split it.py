# Assigning odd and even numbers to variables
a = [1, 3, 5, 7, 9, 11, 13, 15]
x = [2, 4, 6, 8, 10, 12, 14, 16]

# Function to split a list into two halves
def split_list(lst):
    mid = len(lst) // 2  # Find the middle index
    return lst[:mid], lst[mid:]

# Splitting the odd and even number lists
split_odd = split_list(a)
split_even = split_list(x)

# Printing the split lists
print("Odd numbers split:", a)
print("Even numbers split:", x)
