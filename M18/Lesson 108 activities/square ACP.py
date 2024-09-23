import turtle

# Set up the turtle screen
screen = turtle.Screen()

# Create a turtle object
square_turtle = turtle.Turtle()
square_turtle.speed(2)  # Adjust speed

# List of colors to make the square colorful
colors = ['red', 'blue', 'green', 'purple']

# Function to draw a colorful square
def draw_colorful_square(size):
    for i in range(4):  # A square has 4 sides
        square_turtle.pencolor(colors[i])  # Change color for each side
        square_turtle.forward(size)  # Move forward by 'size' units
        square_turtle.left(90)  # Turn left by 90 degrees

# Draw a square with a specified size
draw_colorful_square(150)

# Hide the turtle when done
square_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
