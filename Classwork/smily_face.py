from turtle import *
# A function is defined for each part, with following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home

class face():

    def __init__(self, xpos, ypos)
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'

    def setSize(self, radius):
        self.size  = radius

    def drawSelf(self):
        self.goHome()
        pensize(3)
        speed (0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)
 # --------------------------------------------------
 #    Functions that are called from with the class
 # --------------------------------------------------



   
 # After drawing each part, turtle position 
 # returns to centre. Parts can be drawn in any order

    def goHome(self):
        penup()
        goto(self.coord)

        setheading(0)

    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)

