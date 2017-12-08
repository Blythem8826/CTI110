# CTI-110 
# M3HW1 - Age Classifier 
# Michael Blythe
# 9/13/17
#

def main():
# code will display a person's age group
    score = int(input('What is your age? '))

    if score == 1:
        print('Infant')
    elif score <=12 and score >= 2:
        print('Child')
    elif score <=20 and score >= 13:
        print('Teenager')
    else:
        print('Adult')
main()
