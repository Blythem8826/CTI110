# CTI-110 
# M5HW2
# Michael Blythe
# 10/29/17
#
def main():
    print('Enter a positive numbers to add')
    print('Enter a negative number to quit and display total')
    print()
    numberAdd = int(input('Please enter a number: '))

    totalAmount=0
    
    while numberAdd >= 0:
        totalAmount = totalAmount + numberAdd
        numberAdd = int(input('Please enter more numbers: '))
    print('----------------')
    print('The total is: ', totalAmount)
                         
main()
