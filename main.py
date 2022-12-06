from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
# timmy_turtle.shape("turtle")
# timmy_turtle.color("red")

# for _ in range(12):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)
#     for __ in range(4):
#         timmy_turtle.forward(50)
#         timmy_turtle.right(30)
#         for ___ in range(4):
#             timmy_turtle.forward(50)
#             timmy_turtle.right(30)
# timmy_turtle.pensize(5)

# Move the turtle to the starting position for the line
# timmy_turtle.penup()
# timmy_turtle.goto(-100, 0)
# timmy_turtle.pendown()

# Draw a dashed line
# for i in range(10):
#     timmy_turtle.dot(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(20)
#     timmy_turtle.pendown()

colour = ["CornflowerBlue", "DarkOrchid", "IndianRed", "Purple", "Black", "Brown", "Grey", "Yellow", "Green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)

for shape in range(3,11):
    timmy_turtle.color(random.choice(colour))
    draw_shape(shape)



screen = Screen()
screen.exitonclick()
