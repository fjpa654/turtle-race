from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 500)

user_bet = screen.textinput("Make your bet", "enter a color")

color = ["red", "yellow", "green", "blue", "purple"]

t1 = Turtle("turtle")
t2 = Turtle("turtle")
t3 = Turtle("turtle")
t4 = Turtle("turtle")
t5 = Turtle("turtle")

t1.color(color[0])
t2.color(color[1])
t3.color(color[2])
t4.color(color[3])
t5.color(color[4])

t1.penup()
t2.penup()
t3.penup()
t4.penup()
t5.penup()


t1.goto(-200, 100)
t2.goto(-200, 50)
t3.goto(-200, 0)
t4.goto(-200, -50)
t5.goto(-200, -100)



screen.exitonclick()
