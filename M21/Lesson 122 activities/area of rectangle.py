
# Define a class for Rectangle
class Rectangle:
    # Constructor to initialize the length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate the area
    def calculate_area(self):
        return self.length * self.width

# Ask the user to input length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an object of the Rectangle class
rectangle = Rectangle(length, width)

# Calculate and print the area of the rectangle
print(f"The area of the rectangle is: {rectangle.calculate_area()}")
