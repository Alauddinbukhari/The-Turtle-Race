from turtle import Turtle,Screen
import random
# tim= Turtle()
# screen=Screen()
# def move_forward():
#     tim.forward(50)
# def forward():
#     tim.forward(50)
# def backward():
#     tim.backward(50)
#
#
# def counter_clock():
#     tim.left(10)
#
# def clockwise():
#     tim.right(10)
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# def circle():
#     tim.circle(50)
#
#
#
#
# tim.speed(1)
# screen.listen()
#
#
# screen.onkey(fun=move_forward,key="space")
# screen.onkey(fun=forward,key="w")
# screen.onkey(fun=backward,key="s")
# screen.onkey(fun=counter_clock,key="d")
# screen.onkey(fun=clockwise,key="a")
# screen.onkey(fun=circle,key="b")
#
# screen.onkey(fun=clear_drawing,key="c")
race_on=False
colors=["cadetBlue2","red","orange","blue","chocolate2","cyan2"]
y_positions=[-70,-40,-10,20,50,80]
screen=Screen()
screen.setup(width=500,height=400)#width=colums, height= rows
screen.title("The Turtle Race Show")
user_bet=screen.textinput(title="Make a bet",prompt="which turtle wil win the race? Enter a color:")
turtles=[]
for i in range(6):
    t=Turtle("turtle")
    t.color(colors[i])
    turtles.append(t)
    t.penup()
    t.goto(-230,y_positions[i])
    t.write(colors[i],font=("Gooddog",15,"normal"))
if user_bet:
    race_on=True

while  race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on=False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
        rand_dis = random.randint(1, 10)
        turtle.forward(rand_dis)



screen.exitonclick()



