# Marching Squares Turtle Implementation
# by Joshua Cochrane
# 14 June 2023

# Imports
import turtle
import random
import math
from time import sleep as wait

# Settings
squareResolution = 70 # the amount of squares that should be present across each axis

screenWidth = 900
screenHeight = 900

backgroundColor = "black"
nodeColourOff = "lightgray"
nodeColourOn = "white"
nodesToggled = False
nodeRadius = (screenWidth / squareResolution) / 8
lineColour = "white"

nodeOffThreshold = .5
nodeOffMaximum = 1

resetDelay = 1
resetToggled = False

# Variables
squares = []

# Turtle setup
screen = turtle.Screen()
screen.bgcolor(backgroundColor)
screen.title("Joshua Cochrane | Marching Squares Turtle Implementation")
screen.setup(width = screenWidth + 16, height = screenHeight + 16)
screen.setworldcoordinates(0, screen.window_height(), screen.window_width(), 0)
screen.delay(0)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Functions
def Setup():
    # Set up the squares array
    for x in range(squareResolution + 1):
        squares.append([])
        for y in range(squareResolution + 1):
            squares[x].append([])

def GenerateSquareCorners():
    # Generate the corners for the squares
    # add 1 to implement bottom and right edges
    for x in range(squareResolution + 1):
        for y in range(squareResolution + 1):
            num = random.randint(0, nodeOffMaximum)
            squares[x][y] = 0 if num >= nodeOffThreshold else 1

def DrawSquareCorners():    
    for x in range(squareResolution + 1):
        for y in range(squareResolution + 1):
            pen.penup()
            
            xPos = (x * (screenWidth / squareResolution))
            yPos = (y * (screenHeight / squareResolution))
            
            if round(squares[x][y]) == 0:
                pen.color(nodeColourOff)
            else:
                pen.color(nodeColourOn)
                pen.begin_fill()
            
            pen.goto(xPos, yPos)
            pen.pendown()
            
            pen.circle(nodeRadius)
            pen.end_fill()
 
def DrawLine(startCoords, endCoords):
    pen.color(lineColour)
    pen.goto(startCoords[0], startCoords[1])
    pen.pendown()
    pen.goto(endCoords[0], endCoords[1])
    pen.penup()

def DrawIsolines():
    pen.penup()
    pen.color(lineColour)
    
    for x in range(squareResolution):
        for y in range(squareResolution):
            case = GetCaseFromCorners(
                squares[x][y],
                squares[x + 1][y],
                squares[x + 1][y + 1],
                squares[x][y + 1]
            )
            
            xPos = (x * (screenWidth / squareResolution))
            yPos = (y * (screenHeight / squareResolution))
            
            edgeA = (xPos + ((screenWidth / squareResolution) * 0.5), yPos)
            edgeB = (xPos + (screenWidth / squareResolution), yPos + ((screenHeight / squareResolution) * 0.5))
            edgeC = (xPos + ((screenWidth / squareResolution) * 0.5), yPos + (screenHeight / squareResolution))
            edgeD = (xPos, yPos + ((screenHeight / squareResolution) * 0.5))
            
            if case in [1, 14]:
                DrawLine(edgeC, edgeD)
                continue
            elif case in [2, 13]:
                DrawLine(edgeB, edgeC)
                continue
            elif case in [3, 12]:
                DrawLine(edgeB, edgeD)
                continue
            elif case in [4, 11]:
                DrawLine(edgeA, edgeB)
                continue
            elif case == 5:
                DrawLine(edgeA, edgeD)
                DrawLine(edgeB, edgeC)
                continue
            elif case in [6, 9]:
                DrawLine(edgeA, edgeC)
                continue
            elif case in [7, 8]:
                DrawLine(edgeA, edgeD)
                continue
            elif case == 10:
                DrawLine(edgeA, edgeB)
                DrawLine(edgeC, edgeD)
                continue

def GetCaseFromCorners(a, b, c, d):
    return (a * 8) + (b * 4) + (c * 2) + d

def Run():
    Setup()
    
    while True:
        GenerateSquareCorners()
        pen.clear()
        
        if nodesToggled:
            DrawSquareCorners()
            screen.update()
            
        DrawIsolines()
        screen.update()
        
        if not resetToggled:
            break
        
        wait(resetDelay)
    
    screen.mainloop()

# Primary
if __name__ == "__main__":
    Run()