import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

ALIGN = "center"
FONT = ("Courier", 36, "normal")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Centre line
centre_line = turtle.Turtle()
centre_line.speed(0)
centre_line.shape("square")
centre_line.color("white")
centre_line.shapesize(stretch_wid=30, stretch_len=0.2)
centre_line.penup()
centre_line.goto(0, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6

# Initial scores
score_a = 0
score_b = 0

# Live scores
scores = turtle.Turtle()
scores.speed(0)
scores.color("white")
scores.hideturtle()
scores.penup()
scores.goto(-200, 260)
scores.write("0", align=ALIGN, font=FONT)
scores.goto(200, 260)
scores.write("0", align=ALIGN, font=FONT)

# Pause and resume game
is_pause = False

# Move paddles
def paddle_a_up():
    if is_pause == False:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if is_pause == False:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if is_pause == False:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if is_pause == False:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

def interrupt():
    global is_pause
    if is_pause == False:
        is_pause = True
    else:
        is_pause = False
    return is_pause

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "d")
window.onkeypress(paddle_a_down, "c")
window.onkeypress(paddle_b_up, "k")
window.onkeypress(paddle_b_down, "m")
window.onkeypress(interrupt, "space")

# Game loop
while True:

    if is_pause == False:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check borders

        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav &")

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav &")

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            scores.clear()
            scores.goto(-200, 260)
            scores.write(score_a, align=ALIGN, font=FONT)
            scores.goto(200, 260)
            scores.write(score_b, align=ALIGN, font=FONT)
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            scores.clear()
            scores.goto(-200, 260)
            scores.write(score_a, align=ALIGN, font=FONT)
            scores.goto(200, 260)
            scores.write(score_b, align=ALIGN, font=FONT)
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
            os.system("afplay bounce.wav &")

        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav &")

    else:
        window.update()
