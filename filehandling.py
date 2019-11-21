#TASK 1#
'''f=open("file.txt",'w')
f.writelines("This is my\n First Line.")
f.close()
#TASK 2#
f=open("file.txt","r+")
text=f.read()
print(text)
text=input("Enter text here...")
text=input()
print(text)
f.close()
#TASK 3#

f=open("file.txt",'a')
f.writelines("\n This is Appended Text, Ok")
f.close()
#TASK 4#
with open("file.txt","r")as f:
    text=f.read()
    print(text)
#TASK 5#
f12=open("file2.txt","w")
text=input("Write here.... until you write stop,ok")
while text!='stop':
    f12.writelines(text+'\n')
    text=input()
print("You have done with Writing in file2.")
f12.close()
#TASK 6#
add=open("file3.txt","w")
text=input("Write here for file3.... until you write stop,ok")
while text!='stop':
    add.writelines(text+'\n')
    text=input()
print("You have done with Writing in file3.")
add.close()'''
#TASK 7#
f=open("file4.txt","w+")
text=f.read()
print(text)
f.writelines("\n This is writing Text, Ok")
f.seek(6)
f.close()
#TASK 8#


