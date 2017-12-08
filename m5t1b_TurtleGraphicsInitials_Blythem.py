# CTI-110 
# M5T1a - Shapes
# Michael Blythe
# 10/11/17
#

def main():
    import turtle
    wn = turtle.Screen()
    tiny = turtle.Turtle()

    # move tiny
    tiny.penup()
    tiny.back(200)
    tiny.pendown()
        
    # tiny will draw the square
    for t in range(1):
        tiny.left(90)
        tiny.forward(100)
        tiny.right(140)
        tiny.forward(80)
        tiny.left(100)
        tiny.forward(80)
        tiny.right(140)
        tiny.forward(100)
        tiny.left(90)

    # move tiny
    tiny.penup()
    tiny.forward(50)
    tiny.pendown()

        # tiny will draw the square
    for t in range(1):
        tiny.left(90)
        tiny.forward(100)
        tiny.right(90)
        tiny.forward(50)
        tiny.right(90)
        tiny.forward(50)
        tiny.right(90)
        tiny.forward(50)
        tiny.right(180)
        tiny.forward(65)
        tiny.right(90)
        tiny.forward(50)
        tiny.right(90)
        tiny.forward(65)
    
main()
