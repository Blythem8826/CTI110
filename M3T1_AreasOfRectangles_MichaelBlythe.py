#CTI-110
#M2HW1 - DISTANCE TRAVELED
#Michael Blythe
#9/10/17
#

# Input for rectangle 1
length1 = int(input('Length of rectangle 1?:'))
width1 = int(input('Width of rectangle 1?:'))

# Input for rectangle 2
length2 = int(input('Length of rectangle 2?:'))
width2 = int(input('Width of rectangle 2?:'))

# Calculations of rectangles
area1 = length1 * width1
area2 = length2 * width2

# Calculate which is greater
if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both have the same area.')
