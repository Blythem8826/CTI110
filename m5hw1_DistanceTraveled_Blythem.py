# CTI-110 
# M5HW1
# Michael Blythe
# 10/29/17
#

def main():
    speed = float( input("What is the vehicle speed in miles per hour?: " ))
    hours = int( input( "How many hours has the vehicle been traveling?: " ))

    print( "Hours","\tDistance Traveled" )
    print( "- - - - - - - - -")
    for totalHours in range( 1, hours + 1 ):
        distance = speed * totalHours
        print( totalHours ,"\t",distance )
main()
