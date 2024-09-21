from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "yellow", "purple", "green", "orange"]
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtle = []

for turtle_index in range(0,6):
    pagong = Turtle(shape="turtle")
    pagong.penup()
    pagong.color(colors[turtle_index])
    pagong.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(pagong)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        speed = random.randint(0,10)
        turtle.forward(speed)


screen.exitonclick()
