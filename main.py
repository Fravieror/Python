import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")  # Give the shape of a turtle
timmy.color("red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)  # It creates a canvas when the turtle will be showed
my_screen.exitonclick()  # It ends the program when click is performed in the screen

