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

def errorAnalysis():
    # Equidistant from a central point is assummed based on increasing area of intersections for different "error rings" around circles
    # what happens with a constant shift in radius? for all three receivers moving along same axis:
    # Position expected to stay constant:
    # Varying y1, x2, y3

    x1 = 0
    y1 = 1

    x2 = 1
    y2 = 0

    x3 = 0
    y3 = -1

    r1 = findNewRadius(0,1,x1, y1)
    r2 = findNewRadius(0,1,x2, y2)
    r3 = findNewRadius(0,1,x3, y3)

    noise_offset = 1
    color = "green"
    message = "Test drawing"
    while(y1 <= 20):
        r1 = findNewRadius(0,1,x1, y1)
        r2 = findNewRadius(0,1,x2, y2)
        r3 = findNewRadius(0,1,x3, y3)

        x,y = findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
        print("Location:")
        print(x,y)
        drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3, color, message)
        y1 += 5
        x2 += 5
        y3 -= 5

errorAnalysis()
