#Drawing my initials using turtle
#CTI-110
#p4t1a - Drawing Initials
#10-17-2018

# Set up turtle
import turtle

#Set up window and attributes
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("My initials")

#Create ant
ant = turtle.Turtle()
ant.shape("turtle")
ant.color("white")



# Make ant draw an "A"
ant.left(90)
ant.forward(100)
ant.right(90)
ant.forward(50)
ant.right(90)
ant.forward(100)
ant.left(180)
ant.forward(50)
ant.left(90)
ant.forward(50)


# Make ant draw an "S"
ant.forward(100)
ant.left(90)
ant.forward(100)
ant.left(90)
ant.forward(100)
ant.right(90)
ant.forward(100)
ant.right(90)
ant.forward(100)

#wait for user to close
wn.mainloop()





