'''import re
name=input("Enter name" )
valid =True
while valid:
    if(len(name)<2 or len(name)>16):
        break
    elif not re.search(["a=z"],name):
        break'''
'''import re
name= input("Enter your Name: ")
x = True
while x:
    if (len(name)<2 or len(name)>12):
        break
    elif not re.search("[a-z]",name):
        break
        else:
        print("Valid User Name")
        x=False
        break
if x:
    print("Not a Valid User Name. Please enter correct data.")'''

import sys
name=input("Enter your Name: ")
for name in range(1,4):
    if name.isalpha()==True:
        print("Valid Name")
    else:
        print("Invalid name")
sys.exit("Please try next startup")





'''age=input("Enter your Age: ")
if age.isdigit()==True:
    if int(age)>=18:
        print("Valid age")
    else:
        print("Invalid input age, please enter correct age.")

if age>=18:
    print("Valid age")


Mobile=input("Enter your mobile number: ")
if Mobile.isdigit()==True:
    print("Valid number.")
else:
    print("Invalid mobile number")
'''length=input("Enter the length of polygon: ")
breadth=input("Enter the breadth of polygon: ")
if length==breadth:
    print("The polygon is Square.")
else:
    print("The polygon is Rectangle.")'''