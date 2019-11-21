'''num=int(input("Enter number: "))
if num%2==0:
    print("Even")
else:
    print("ODD")'''
year=int(input("Enter Year date: "))
if year%400==0:
    print("leap")
elif year%100!=0 and year%4==0:
    print("leap")
else:
    print("Not leap")






