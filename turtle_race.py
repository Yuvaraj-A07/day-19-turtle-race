import random
from turtle import Turtle, Screen

is_race_on = True
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -240
y = -150
all_turtle = []
for col in colors:
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(col)
    tim.goto(x, y)
    y += 50
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won the game")

            else:
                print("You lose the game")
                print(f"{winning_color} turtle has won the game")



        dist = random.randint(0,10)
        turtle.forward(dist)




screen.exitonclick()