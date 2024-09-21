# Function to calculate the product of all elements in a tuple
def tuple_product(tup):
    product = 1  # Initialize product as 1
    for num in tup:
        product *= num  # Multiply each element
    return product

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

# Calculate and print the product of the tuples
print("Product of tup1:", tuple_product(tup1))
print("Product of tup2:", tuple_product(tup2))