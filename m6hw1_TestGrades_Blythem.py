#Michael Blythe
#M6HW1
#CTI-110
#11/6/17
#
#


def main():
    #establishes total variable
    total = 0
    
    #message to user asking for 5 grades
    print('Enter 5 grades to obtain your average.')
    
    #asks user for input a number of times specified in range
    #also calls the fuction determine_grade to apply letter grade to each input
    #adds the grade total and sends the total off to calc_average to be caculated
    #lastly prints average
    for i in range(0,5):
        grade = int(input('Please enter your grade: '))
        letterGrade = determine_grade(grade)
        total += grade
        print(letterGrade)
    print('Your average is: ', calc_average(total))
    
#calculates the average using the total variable
def calc_average(total):
    
    return total / 5
    
#returns a letter grade based on certain criteria
def determine_grade(grades):
    if grades >= 90:
        return('Your grade is: A')
    elif grades <=89 and grades >= 80:
        return('Your grade is: B')
    elif grades <=79 and grades >= 70:
        return('Your grade is: C')
    elif grades <=69 and grades >= 60:
        return('Your grade is: D')
    else:
        return('Your grade is: F')
main()
