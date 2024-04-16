import turtle

# Screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

# LeftBat
left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape("square")
left_bat.shapesize(stretch_wid=5, stretch_len=1)
left_bat.color("white")
left_bat.penup()
left_bat.goto(-350, 0)

# RightBat
right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape("square")
right_bat.shapesize(stretch_wid=5, stretch_len=1)
right_bat.color("white")
right_bat.penup()
right_bat.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.changeX = 0.07
ball.changeY = -0.03

# Score
left_player_score = 0
right_player_score = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Left Player: {left_player_score}         Right Player: {right_player_score}", align="center",
            font=("Helvetica", 24, "normal"))


def left_bat_up():
    y = left_bat.ycor()
    y += 30
    left_bat.sety(y)


def left_bat_down():
    y = left_bat.ycor()
    y -= 30
    left_bat.sety(y)


def right_bat_up():
    y = right_bat.ycor()
    y += 30
    right_bat.sety(y)


def right_bat_down():
    y = right_bat.ycor()
    y -= 30
    right_bat.sety(y)


screen.onkey(left_bat_up, "w")
screen.onkey(left_bat_down, "s")
screen.onkey(right_bat_up, "Up")
screen.onkey(right_bat_down, "Down")

screen.listen()

while True:
    screen.update()  # Refreshing window
    ball.setx(ball.xcor() + ball.changeX)
    ball.sety(ball.ycor() + ball.changeY)

    # Bouncing back from top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.changeY *= -1
    # Bouncing back from bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.changeY *= -1
    # Ball goes out at right
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.changeX *= -1
        left_player_score += 1
        score.clear()
        score.write(f"Left Player: {left_player_score}         Right Player: {right_player_score}", align="center",
                    font=("Helvetica", 24, "normal"))
    # Ball goes out at left
    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.changeX *= -1
        right_player_score += 1
        score.clear()
        score.write(f"Left Player: {left_player_score}         Right Player: {right_player_score}", align="center",
                    font=("Helvetica", 24, "normal"))
    # Bouncing back from bat
    if (right_bat.xcor() - 20 < ball.xcor() < right_bat.xcor() and
            right_bat.ycor() - 40 < ball.ycor() < right_bat.ycor() + 40):
        ball.setx(right_bat.xcor() - 20)
        ball.changeX *= -1

    if (left_bat.xcor() + 20 > ball.xcor() > left_bat.xcor() and
            left_bat.ycor() - 40 < ball.ycor() < left_bat.ycor() + 40):
        ball.setx(left_bat.xcor() + 20)
        ball.changeX *= -1
