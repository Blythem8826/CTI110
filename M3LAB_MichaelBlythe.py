# CTI-110
# M3LAB_MichaelBlythe
# 9/17/17

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    score = int(input('Give me a score: '))

    if score >= 90:
        print('Your grade is: A')
    elif score <=89 and score >= 80:
        print('Your grade is: B')
    elif score <=79 and score >= 70:
        print('Your grade is: C')
    elif score <=69 and score >= 60:
        print('Your grade is: D')
    else:
        print('Your grade is: F')


# program start
main()
