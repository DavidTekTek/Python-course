# Function to decide clothing based on temperature
def clothing_decision(temperature):

# Assuming below 18°C is considered cold
    if temperature < 18:  
        return "It's cold, you should wear a jacket."
    else:
        return "The weather is mild, you can wear light clothes."

# Ask the user for the current temperature
temperature = float(input("Enter the current temperature (in °C): "))

# Print the clothing recommendation
print(clothing_decision(temperature))
