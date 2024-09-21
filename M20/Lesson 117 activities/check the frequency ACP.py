# Given test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask the user to enter the value for which to check the frequency
value = int(input("Enter the value to check its frequency: "))

# Check the frequency of the given value in the dictionary
frequency = list(test_dict.values()).count(value)

# Print the result
print(f"The frequency of the value {value} is:", frequency)
