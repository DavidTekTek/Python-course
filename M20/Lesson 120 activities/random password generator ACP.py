import random
import string

# Function to generate random password
def generate_password(length):
    # Define characters: lowercase, uppercase, and digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    # Create a pool of characters
    all_characters = lowercase_letters + uppercase_letters + digits

    # Generate random password from the pool
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Convert the password to a list to shuffle
    password_list = list(password)
    random.shuffle(password_list)  # Shuffle the characters

    # Join the shuffled characters to form the final password
    final_password = ''.join(password_list)

    return final_password

# Ask the user for the desired password length
length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Generated password:", password)
