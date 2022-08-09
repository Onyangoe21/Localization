# This is a python file analysing erros in trilateration for different positioning of the receivers
# Test assumes a sphere of a given radius and should give least distance between receivers for minimum error
from random import randint
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


# Write a function to analyze changes in receiver locations in a pependicular manner:
# Parameters: simulate_random controls whether the movement of receivers is done at random or perpendicularly
def errorAnalysis(simulate_random = False):
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

    noise_offset = 50
    color = "green"
    message = "Test drawing"
    while(y1 <= 40 or simulate_random):
        # Calculate the radii based on the locations we have for an accurate location
        r1 = findNewRadius(0,1,x1, y1)
        r2 = findNewRadius(0,1,x2, y2)
        r3 = findNewRadius(0,1,x3, y3)

        # Find location and draw
        message = "Without the noise:"
        color = "green"
        x,y = findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
        print("Location:")
        print(x,y)
        drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3, color, message)

        # Draw with negative effect from noise
        message = "With positive effect from noise:"
        color = "red"
        n_x,n_y = findLocation(x1,y1,r1 + noise_offset,x2,y2,r2 + noise_offset,x3,y3,r3 + noise_offset)
        print("Location affected 'negatively':")
        print(n_x,n_y)
        r1 = findNewRadius(n_x,n_y,x1, y1)
        r2 = findNewRadius(n_x,n_y,x2, y2)
        r3 = findNewRadius(n_x,n_y,x3, y3)
        drawCellTowers(x1,y1,r1,x2,y2,r2,x3,y3,r3, color, message, True)

        # Calculate maximum difference
        magnitude_diff = math.sqrt(((n_y - y)* (n_y - y)) + ((n_x - x)*(n_x - x)))
        print("Error: ", magnitude_diff)
        if(simulate_random):
          x1 = randint(-150,-80)
          y1 = randint(-150,150)
          x2 = randint(-80,80)
          y2 = randint(20,150)
          x3 = randint(80,150)
          y3 = randint(-150,-20)
        else:
          y1 += 5
          x2 += 5
          y3 -= 5


errorAnalysis(True)
