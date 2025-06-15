# Ashley O
# CS 1026 Assignment
# October 6th, 2021

# Import system to make sys.exit(0) halt 0 input.
import sys

process = False
# While statement to initiate loop until 0 is inputted.
while process == False:
    # Input kwh during Off Peak periods.
    offPeak = (float(input('Enter kwh during Off Peak period: ')))
   
    # if 0 is inputted for offPeak, the program halts.   
    if offPeak == 0:
        sys.exit(0)
    # Input kwh during On Peak periods.
    onPeak = (float(input('Enter kwh during On Peak period: ')))
  
    # Input kwh during Mid Peak periods and add all periods to get totalUsage value before discounts and and taxes.
    midPeak = float(input('Enter kwh during Mid Peak period: '))
  
    totalUsage = (offPeak + onPeak + midPeak)
   
    # Multiply total usage by kwh rates.
    totalUsagePrice = (offPeak * float(0.085) + onPeak * float(0.176) + midPeak * float(0.119))
   
    # totalUsage discount calculated if kwh is less than 400 and onPeak is less than 150.
    if totalUsage < 400:
        totalUsagePrice = totalUsagePrice * 0.96
       # print("totalUsagePrice w/ 400 disc", totalUsagePrice) for testing purposes
    elif onPeak < 150:
        totalUsagePrice = ((midPeak * 0.119) + (onPeak - (onPeak * 0.05))* 0.176 + (offPeak * 0.085))
        #print("totalUsagePrice w/ onpeakdiscount", totalUsagePrice) for testing purposes
# Owner's age input and discount calculation, assuming inputs are Y,y,N or N.
   
    ownerAge = str(input('Is the owner senior? (Y,y,N,n): '))
    if ownerAge == 'Y' or ownerAge == 'y':
        totalUsagePrice = totalUsagePrice * 0.89
    # If owner isn't senior, totalUsage price remains the same without the 11% discount.
    else:
        totalUsagePrice = totalUsagePrice
   
    # Tax rate is 13% or 1.13x the totalUsagePrice
    totalUsagePrice = totalUsagePrice * 1.13
    print('Electricity cost: $%.2f \n' % totalUsagePrice)
