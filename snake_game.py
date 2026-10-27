import turtle 
import time

delay = 0.1

wm = turtle.Screen()
wm.title("Snake Game")
wm.bgcolor("green")
wm.setup(width=600, height=600)
wm.tracer(0)  # Turns off the screen updates

wm.mainloop()

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"

#Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)



# main game loop
while True:
    wm.update()

move()

time.sleep(delay)


wm.mainloop()