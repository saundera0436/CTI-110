#Drawing snowflakes
#CTI-110
#P4T1C - snowflakes
#10-17-2018
#Anthony Saunders




#Set up turtle
import turtle

#Set up window
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Snowflakes")

#Create ant
ant = turtle.Turtle()
ant.shape("turtle")
ant.color("white")





ant.left(90)

for x in range(0,6):
    ant.forward(100)
    ant.forward(-40)
    ant.left(40)
    ant.forward(30)
    ant.forward(-30)
    ant.right(80)
    ant.forward(30)
    ant.forward(-30)
    ant.left(40)
    ant.forward(-60)

    ant.right(60)
