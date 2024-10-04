"""Penta Spiral

This program already works. See if you can change it to make it draw a different pattern.

"""


import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def getNextColor(i):
    return colors[i % len(colors)]
colors = ('lightgreen','lightblue','purp','magenta')
window = turtle.Screen()
window.bgcolor("pink")
window.setup(width=600, height=600)
# Make a new turtle
myTurtle = turtle.Turtle()

# This code sets our shape to a turtle
myTurtle.shape("turtle")

# Set your turtle's speed
myTurtle.speed(10)

# Set your turtle's color
myTurtle.color("hotpink")

# Use a loop to repeat the code below 50 times
for i in range(60):

    # Set the turtle color to a random color
    myTurtle.pencolor(getNextColor(i))

    # Move the turtle (5*i) pixels. 'i' is the loop variable
    myTurtle.forward(3 * i)

    # Turn the turtle (360/7) degrees to the right
    myTurtle.right(360 /5 + i*3)

    # Change the turtle width to 'i' (the loop variable)
    myTurtle.width(4)

    # Check the pattern against the picture in the recipe. If it matches, you are done!


turtle.done()

# Now check in your code!