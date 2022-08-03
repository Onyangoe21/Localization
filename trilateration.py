# This is a python file analysing erros in trilateration for different positioning of the receivers
# Test assumes a sphere of a given radius and should give least distance between receivers for minimum error
from turtle import delay
import math
from draw import drawCellTowers
import time


#A function to apply trilateration formulas to return the (x,y) intersection point of three circles
# Method structure adopted from https://www.101computing.net/cell-phone-trilateration-algorithm/
def findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y

def findNewRadius(target_x, target_y, tx_x, tx_y):
    radius = math.sqrt(((target_y - tx_y)* (target_y - tx_y)) + ((target_x - tx_x)*(target_x - tx_x)))
    return radius

x1 = 0
y1 = 2

x2 = 1
y2 = 1

x3 = 0
y3 = 0

r1 = findNewRadius(0,1,x1, y1)
r2 = findNewRadius(0,1,x2, y2)
r3 = findNewRadius(0,1,x3, y3)

#Apply trilateration algorithm to locate phone
x,y = findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
print("Cell Phone Location:")
print(x,y)

# for i in range(10):
#     print("started")
#     drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3)
#     x,y = findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
#     print(x,y)
#     time.sleep(0.0001)
#Output phone location / coordinates


