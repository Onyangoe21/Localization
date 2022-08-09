## Localization

* This repo is mainly for analyzing positioning of recievers in tri-lateration: 
* If you are about to decide on **how to space your receivers**, this is the right analysis for you: 🙂
* The draw section makes use of simplified computation geometry from https://www.101computing.net/cell-phone-trilateration-algorithm/
* The trilateration file has the following methods:
      1. findLocation()
      2. findRadius()
      3. ErrorAnalysis()

### findLocation():
* This method takes the location of all the receivers and the respective radii from transmitter and calculates the specific position of the transmitter:
* It returns two values: x and y:

### findRadius():
* This function takes two points on a cartesian plane and returns the distance between them

### ErrorAnalysis():
* This function takes an optional boolean param simulate_random and if the boolean is true, it does the error analysis based on random locations of receivers computed in the following section of the code:
---
  `
  x1 = randint(-150,-80)
  y1 = randint(-150,150)
  x2 = randint(-80,80)
  y2 = randint(20,150)
  x3 = randint(80,150)
  y3 = randint(-150,-20)
  `
