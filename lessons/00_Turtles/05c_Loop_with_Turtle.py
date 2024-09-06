
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... 
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
tina.color('pink')
tina.begin_fill()
for i in range(5):
    tina.forward(90)
    tina.left(55)# Your code here
tina.forward(90)
tina.left(43)
tina.forward(60)
tina.end_fill()
... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
