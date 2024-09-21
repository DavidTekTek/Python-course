# Function to calculate the average of a tuple
def tuple_average(tup):
    # Calculate the sum of the tuple elements
    total = sum(tup)
    # Calculate the number of elements in the tuple
    count = len(tup)
    # Calculate the average
    average = total / count
    return average

# tuple assigned
my_tuple = (10, 20, 30, 40, 50)

# Print the average of the tuple
print("The average of the tuple is:", tuple_average(my_tuple))