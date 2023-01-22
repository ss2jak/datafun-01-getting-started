"""
Complete the script.
"""
#Domain:Trinidad
#Temperature(celcius) determines when we will go to beach this weekend

import math

#Get 3 tenperatures in Celsius from user
temp1=input("what will the temperature be on friday?")
temp2=input("what will the temperature be on saturday?")
temp3=input("what will the temperature be on sunday?")

#Assign each variable(temp) to float
temp1=float(temp1)
temp2=float(temp2)
temp3=float(temp3)
temps=[temp1,temp2,temp3]

#sum
sum=temp1+temp2+temp3
sum

#average
average=sum/3  
average

#smallest(min) and largest(max)
coldest=min(temps)
hottest=max(temps)


#product
product=temp1*temp2+temp3
product

#range
print('range:',min(temps), '-', max(temps))

#friday temp
if temp1 < 27:
    print("No beach today, water won't be warm enough")
elif temp1 == 27:
    print("Not sure about beach today")
else:
    print("Let's go to the beach!")

#saturday temp
if temp2 < 27:
    print("No beach today, water won't be warm enough")
elif temp2 == 27:
    print("Not sure about beach today")
else:
    print("Let's go to the beach!")

#sunday temp
if temp3 < 27:
    print("No beach today, water won't be warm enough")
elif temp3 == 27:
    print("Not sure about beach today")
else:
    print("Let's go to the beach!")



















