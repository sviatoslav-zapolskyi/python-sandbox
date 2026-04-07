from turtle import *

screen = Screen()
screen.setup(width=1.0, height=1.0)
delay(50)

width(3)
up()         # Підняти перо, щоб при пересуванні не залишати сліду
goto(0, -50) # Пересунути черепашку в точку С
down()       # Опустити перо, щоб почати залишати слід
circle(50)

done()