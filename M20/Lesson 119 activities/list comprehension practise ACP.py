# Input from the user
number = int(input("Enter a number: "))

# List comprehension to generate odd numbers under the input value
odd_numbers = [num for num in range(1, number) if num % 2 != 0]

# Print the generated odd numbers list
print(f"Odd numbers under {number}: {odd_numbers}")

# List of fruits
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']

# List comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

# Print the new list with updated values
print("Fruits with capitalized first letters:", capitalized_fruits)
