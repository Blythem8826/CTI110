#Michael Blythe
#M6T2
#CTI-110
#11/1/17
#
#This program will convert feet to inches

#Global constant to use
INCHES_FEET = 12

def main():
    #Gets the user input
    feet = int(input('Please enter the number of feet: '))
    #Prints the calculated inches in message to user
    print('There are', feet_to_inches(feet), 'inches in', feet,'ft')

#calculates the number of inches from user input and returns result
def feet_to_inches(feet):
    #Calculation using user input and global constant
    return feet * INCHES_FEET
main()
