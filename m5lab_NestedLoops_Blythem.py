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
    tiny.forward(1)
    tiny.pendown()
    for t in range(8):
        for t in range(2):
            for t in range(1):
                tiny.right(90)
                tiny.forward(20)
                tiny.left(135)
                tiny.forward(30)
                tiny.right(225)
                tiny.forward(22)
                tiny.right(45)
                tiny.forward(30)
            tiny.left(135)
            tiny.forward(20)
            tiny.backward(20)
            tiny.left(90)
            tiny.forward(20)
            tiny.backward(20)
            tiny.right(45)
            tiny.backward(20)
            tiny.left(45)
        tiny.right(45)
        tiny.backward(20)
        tiny.right(45)
        tiny.forward(123)
        tiny.left(45)

       

main()
