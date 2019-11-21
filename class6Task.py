#TASK 1#
#program that copies content of one file to other file#
print("copies content of one file to other file")
with open('file.txt')as f:
    with open('file1.txt','w')as f1:
        for line in f:
            f1.write(line)


#TASK 2#
#Program that corrects the given text into..#
print("\n")
print("Program that corrects the given text into..")

f=open('file.txt','w')
with open('filea.txt','r') as f1:
    text=f1.read()
    print(text)
    d = len(text)
    for i in range(0,d):
        #print(text[i])
        #print(n)
        if text[i]=="-":
            f.writelines(" ")
        else:
            f.writelines(text[i])
f.close()



#TASK 3.Finding Prime numbers using list comprehension#
print("\n")
print("Finding Prime numbers using list comprehension")
lst=[x for x in range(2,10) if all(x%y!=0 for y in range(2,x)   )  ]
print(lst)



#TASK 3. find prime nos.#
print("\n")
print("find prime nos.   normal understanding")
lst_com=[x for x in range(2500)]
print(lst_com)
def num(n):
    #for x in lst_gen:
    num=n
    if num> 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
            else:
                print(n, "is a prime number")
    else:
        print("yes")

a=int(input("Enter number: "))
num(a)


#TASK 4#
#write a program that uses map to convert a list of temp in fahrenheit to celsius.#
print("\n")
print("write a program that uses map to convert a list of temp in fahrenheit to celsius.")

def fah(c):
    f=((9/5)*(c+32))
    return f
cel=[23,100,28,45,65]
calcf=(map(fah,cel))
flist=list(calcf)
print(flist)




#TASK 5#
#program creating 3 Types of Errors and write except statement for them..#
print("\n")
print("program creating 3 Types of Errors and write except statement for them..")

try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a+b
    d=a/b
    e="arjun"
    if b==1:
        f=e+2
    print(c)
    print(d)

except ZeroDivisionError:
    print("cant divide by zero")
except TypeError:
    print("Type Error")
except ValueError:
    print("value error")






#TASK 6#
#Program to create a USER DEFINED ERROR whenever the string is less than 3#
print("\n")
print("Program to create a USER DEFINED ERROR whenever the string is less than 3")

class LowStringError(Exception):
    def __init__(self):
        super(LowStringError,self).__init__("The user input string must be greater than 3.")

st=input("Enter the value:")
if int(st)<3:
    raise LowStringError
else:
    print("ACCEPTED")



