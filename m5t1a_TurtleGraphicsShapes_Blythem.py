# CTI-110 
# M5T1a - Shapes
# Michael Blythe
# 10/11/17
#

def main():
    import turtle
    wn = turtle.Screen()
    tiny = turtle.Turtle()
    # tiny will draw the square
    for t in [0,1,2,3]:
        tiny.forward(100)
        tiny.left(90)
    # move tiny
    tiny.penup()
    tiny.forward(120)
    tiny.pendown()
    # tiny will draw the triangle
    for t in [0,1,2]:
        tiny.forward(100)
        tiny.left(120)
main()
