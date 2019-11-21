name="Arjun"
age=20
place="Itahari"
'''def sum1():
    a=int(input("Enter the a value: "))
    b=int(input("Enter the b value: "))
    print("The sum= ",a+b)'''
def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
choose=input(print('Calculator\n 1-sum\n 2-mul\n 3-div'))
if choose=='1':
    sum()
if choose=='2':
    mul()
if choose=='3':
    div()
if __name__=='__main__':
    a=int(input("Enter the a value: "))
    b=int(input("Enter the b value: "))
    print("Sum: ",a+b)
    print("mul: ",a*b)
    print("div: ",a/b)


text='Thank You. '