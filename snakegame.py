
import turtle
import time as t
import random

# Creating a window screen
w = turtle.Screen()
w.title("Snake Game")
w.setup(width=600, height=600) #height and width of the game window
w.tracer(0)

#Setting head of the Snake
snake = turtle.Turtle()
snake.shape("circle")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "S"

# Food for snake in the game
food = turtle.Turtle()
colour = 'red'
shape = 'square'
food.speed(0)
food.shape(shape)
food.color(colour)
food.penup()
food.goto(0, 100)

p = turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("black")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Score : 0 | High Score : 0", align="center",font=("Arial", 20, "bold"))

#initialising the score and high score to 0
delay = 0.1
score = 0
hs = 0



#Updating co-ordinates of the Snake
def go():
	if snake.direction == "u":
		yc = snake.ycor()
		snake.sety(yc+20)
	if snake.direction == "r":
		xc = snake.xcor()
		snake.setx(xc+20)
	if snake.direction == "d":
		yc = snake.ycor()
		snake.sety(yc-20)
	if snake.direction == "l":
		xc = snake.xcor()
		snake.setx(xc-20)

#Game will be closed on pressing Escape
def closegame():
    w.bye()

#Setting direction of Snake
def l():
	if snake.direction != "r":
		snake.direction = "l"

def d():
	if snake.direction != "u":
		snake.direction = "d"

def u():
	if snake.direction != "d":
		snake.direction = "u"

def r():
	if snake.direction != "l":
		snake.direction = "r"



		
w.listen()
w.onkeypress(u, "Up")
w.onkeypress(d, "Down")
w.onkeypress(l, "Left")
w.onkeypress(r, "Right")
w.onkeypress(closegame,"Escape")
parts = [] 


# main game
while True:
	w.update()
	if  snake.ycor() > 290 or snake.ycor() < -290 or snake.xcor() > 290 or snake.xcor() < -290:
		t.sleep(1)
		snake.goto(0, 0)
		snake.direction = "S"
		colour = 'red'
		shape = 'square'
		for i in parts:  i.goto(1000, 1000)

		parts.clear()
		score = 0
		delay = 0.1
		p.clear()
		p.write("Score : {} | High Score : {} ".format(score, hs), align="center", font=("Arial", 20, "bold"))
	if snake.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding segment
		newone = turtle.Turtle()
		newone.speed(0)
		newone.shape("circle")
		newone.color("orange") # tail colour
		newone.penup()
		parts.append(newone)
		delay -= 0.001
		score += 10
		if score > hs:
			hs = score
		p.clear()
		p.write("Score : {} | High Score : {} ".format(score, hs), align="center", font=("Arial", 20, "bold"))
	# Checking for snake collisions with body parts
	for obj in range(len(parts)-1, 0, -1):
		x = parts[obj-1].xcor()
		y = parts[obj-1].ycor()
		parts[obj].goto(x, y)
	if len(parts) > 0:
		x = snake.xcor()
		y = snake.ycor()
		parts[0].goto(x, y)

	go()


	for i in parts:
		if i.distance(snake) < 10:
			t.sleep(1)
			snake.goto(0, 0)
			snake.direction = "S"
			colour = 'red'
			shape = 'square'
			for i in parts:
				i.goto(1000, 1000)
			parts.clear()

			score = 0
			delay = 0.1
			p.clear()
			p.write("Score : {} | High Score : {} ".format(score, hs), align="center", font=("Arial", 20, "bold"))
	t.sleep(delay)
        

w.mainloop()
