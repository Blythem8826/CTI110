#Michael Blythe
#M6T1
#CTI-110
#10/30/17
#
#This program will convert kilometers to miles

#Global constant for conversion equation
KILOMETER_CONVERSION = 0.6214

def main():
    
    #Gets user input of kilometers
    kilometers = float(input('Please enter a distance in kilometer: '))

    #Displays converted distance in miles
    show_miles(kilometers)

#Calculates the conversion
def show_miles(km):
    
    #Kilometer to miles fomula
    miles = km * KILOMETER_CONVERSION

    #Displays newly converted miles
    print(km, 'kilometers equals', miles, 'miles.')
main()
