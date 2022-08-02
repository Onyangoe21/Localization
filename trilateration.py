# This is a python file analysing erros in trilateration for different positioning of the receivers
# Test assumes a sphere of a given radius and should give least distance between receivers for minimum error

#A function to apply trilateration formulas to return the (x,y) intersection point of three circles
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


x1 = 0
y1 = 1

x2 = 1
y2 = 0

x3 = 0
y3 = -1

r1 = 1
r2 = 1
r3 = 1

#Apply trilateration algorithm to locate phone
x,y = findLocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)

#Output phone location / coordinates
print("Cell Phone Location:")
print(x,y)
