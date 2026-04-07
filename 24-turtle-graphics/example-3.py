from turtle import *

screen = Screen()
screen.setup(width=1.0, height=1.0)
delay(50)

circle(50)

up()
goto(-20,60)
down()
dot(20)

up()
goto(20,60)
down()
dot(20)

up()
goto(20,40)
left(90)
down()
circle(20, -160)

done()