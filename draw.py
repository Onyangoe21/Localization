# Modified version of file from https://www.101computing.net/cell-phone-trilateration-algorithm/
# I am using this file from the website mentioned above and instead of random numbers, I am doing my analysis in a circle

import turtle
from random import randint

def drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3,color, message):
  myPen = turtle.Turtle()
  myPen.hideturtle()
  #myPen.tracer(0)
  myPen.speed(1)
  
  
  window = turtle.Screen()
  window.bgcolor("white")
  
  
#   x1 = randint(-150,-80)
#   y1 = randint(-150,150)
#   x2 = randint(80,150)
#   y2 = randint(20,150)
#   x3 = randint(80,150)
#   y3 = randint(-150,-20)
#   x = randint(-60,60)
#   y = randint(-60,60)
#   r1 = ((x-x1)**2 + (y-y1)**2)**0.5
#   r2 = ((x-x2)**2 + (y-y2)**2)**0.5
#   r3 = ((x-x3)**2 + (y-y3)**2)**0.5
  myPen.penup()
  myPen.goto((y1 + r1 + 10), 0)
  myPen.pendown()
  myPen.color("black")
  myPen.write(message)
  myPen.up()

  myPen.color(color)
  myPen.penup()
  myPen.goto(x1-5,y1)
  myPen.pendown()
  myPen.goto(x1+5,y1)
  myPen.penup()
  myPen.goto(x1,y1-5)
  myPen.pendown()
  myPen.goto(x1,y1+5)
  myPen.penup()

  myPen.goto(x1,y1-r1)
  myPen.pendown()
  myPen.circle(r1)
  
  myPen.color(color)
  myPen.penup()
  myPen.goto(x2-5,y2)
  myPen.pendown()
  myPen.goto(x2+5,y2)
  myPen.penup()
  myPen.goto(x2,y2-5)
  myPen.pendown()
  myPen.goto(x2,y2+5)
  myPen.penup()
  
  myPen.goto(x2,y2-r2)
  myPen.pendown()
  myPen.circle(r2)
  myPen.penup()
  
  myPen.color(color)
  myPen.goto(x3-5,y3)
  myPen.pendown()
  myPen.goto(x3+5,y3)
  myPen.penup()
  myPen.goto(x3,y3-5)
  myPen.pendown()
  myPen.goto(x3,y3+5)
  
  myPen.penup()
  myPen.goto(x3,y3-r3)
  myPen.pendown()
  myPen.circle(r3)
  
  myPen.getscreen().update()
  myPen.clear()
  return x1,y1,r1,x2,y2,r2,x3,y3,r3
