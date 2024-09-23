import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Background color

# Create a turtle object
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Set the speed to the maximum

# List of colors for the spiral
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

# Draw a spiral
for i in range(100):
    spiral_turtle.pencolor(colors[i % len(colors)])  # Change color for each iteration
    spiral_turtle.forward(i * 10)  # Move forward
    spiral_turtle.left(144)  # Turn left by 144 degrees (for a spiral shape)

# Hide the turtle when done
spiral_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()