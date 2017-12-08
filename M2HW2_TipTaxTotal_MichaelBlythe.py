#CTI-110
#M2HW2: Tip, Tax, and Total
#Michael Blythe
#9/10/17
#

#Message
print('Price of your meal?')

#Price of meal input
mealCost = float(input('$'))

#Calculation for the tip
mealTip = float(mealCost *.18)

#Calculation for the tax
mealTax = float(mealCost *.07)

#Total meal cost
mealTotal = float(mealCost + mealTip + mealTax)

#Show tip
print('Your tip is $', format(mealTip, ',.2f'))

#Show tax
print('Your tax is $', format(mealTax, ',.2f'))

#Show total
print('Your total is $', format(mealTotal, ',.2f'))

