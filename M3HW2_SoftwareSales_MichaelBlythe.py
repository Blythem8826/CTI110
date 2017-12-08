# CTI-110 
# M3HW2 - SoftwareSales
# Michael Blythe
# 9/13/17
#

def main():
# Input number of packages
        packages = int(input('Enter number of packages purchased: '))

# Nondiscounted total calculation
        totalPrice = packages *99

# Discount calculation
        discount10 = (totalPrice)-(totalPrice *.10)
        discount20 = (totalPrice)-(totalPrice *.20)
        discount30 = (totalPrice)-(totalPrice *.30)
        discount40 = (totalPrice)-(totalPrice *.40)

# Output discounted price with message
        if packages <=19 and packages >=10:
                print('10% discount applied. Your discounted price: $', format(discount10, ',.2f'))
        elif packages <=49 and packages >= 20:
                print('20% discount applied. Your discounted price: $', format(discount20, ',.2f'))
        elif packages <=99 and packages >= 50:
                print('30% discount applied. Your discounted price: $', format(discount30, ',.2f'))
        elif packages >= 100:
                print('40% discount applied. Your discounted price: $', format(discount40, ',.2f'))
        else:
                print('No discount: $', format(totalPrice, ',.2f'))

main()
