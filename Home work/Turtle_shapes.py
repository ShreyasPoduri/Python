import turtle

turtle.Screen().bgcolor("Blue")

sc = turtle.Screen()

sc.setup(400,300)

turtle.title("Welcome To My Canvas")

turtle.done()

# Triangle
board = turtle.Turtle()

board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

turtle.done()


# Square

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

board.forward(100)
board.left(90)

#First Triangle

board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)


board.penup()
board.right(150)
board.forward(50)

#Second Triangle

board.pendown()

board.right(90)
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)