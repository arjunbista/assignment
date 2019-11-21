#TASK 1#
#The Import statement accessing user file#
from user import name,age,place,sum,text
print(name)
print(age)
print(place)
a=sum(2,3)
print("The sum is: ",a)
text='THis is main file, ok.'
print(text)
import user
print(user.text)
