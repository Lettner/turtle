import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex

n=8
i=0
while i<n:
    alex.forward(100)
    alex.left(360/n)
    i=i+1
print("vége")
