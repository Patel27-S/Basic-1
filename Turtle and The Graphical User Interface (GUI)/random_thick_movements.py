from turtle import Turtle, Screen
import random 

# Initializing the Turtle() and Screen() objects.
turtle_ji = Turtle()

screen_ji = Screen()


# Since, we want random colors, I am declaring lists of different colors and 
# for random directions; the directions' list is also declared. 
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'magenta']
directions = [0,90,180,270]


# Let us put turtle_ji's shape :
turtle_ji.shape('turtle')

# Let us make turtle_ji's path making quite thicker :
turtle_ji.pensize(10)
turtle_ji.speed(10)


for _ in range(200):
    # Below, is how the movements of turtle_ji would be :
    # Firstly a turtle would choose any random color.
    # Secondly, it will move forward by 40 units.
    # Thereafter, it will tilt in any random direction.
    # The process will be repeatedly occuring. 
    turtle_ji.color(random.choice(colors))
    turtle_ji.forward(30)
    turtle_ji.right(random.choice(directions))


screen_ji.exitonclick()