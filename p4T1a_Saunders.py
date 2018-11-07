#Drawing shapes
#CTI-110
#p4t1a - shapes
#Anthony Saunders

#Set up turtle
import turtle

# Set up window and its attributes
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title(" Ant and Ron make shapes")

# Create ant
ant = turtle.Turtle()
ant.shape("turtle")
ant.color("white")

# Create ron
ron = turtle.Turtle()
ron.color("black")
ron.pensize(3)

# Make ant draw a square
for i in range(4):
    ant.forward(50)
    ant.left(90)

# Make ant draw a triangle
for i in range(3):
    
    ron.forward(80)
    ron.left(120)


# Wait for user to close 
wn.mainloop()
