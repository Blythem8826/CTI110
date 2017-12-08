# CTI-110 
# M5HW3
# Michael Blythe
# 10/29/17
#
def main():
    userNumber = int( input( "Enter a nonnegative number: " ) )
    
    while userNumber < 1:
        userNumber = int( input( "Only enter a positive number: " ) )

    factorial = 1

    for newInteger in range( 1, userNumber + 1 ):
        factorial = factorial * newInteger

    print( "The factorial of", userNumber, "is", factorial )
    
main()
