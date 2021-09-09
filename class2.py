import numpy as np
intger=10
float=10.50
char='s'
string="shahinur"
boolean=True
booleans=False
print(intger,float,string,char,boolean,booleans)
print(type(intger),type(float),type(string),type(char),type(boolean),type(booleans))
#array decalre  er jonno numpy importe krece r terminnal theke likhbe : pip install numpylikhe enter click
print("***array***")
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))
print("for loop")
#loop (for and while)
for i in range(10):
    print(i)

for i in range(1,10,2):#intial,end,step size
    print(i)

for i in range(1,10):
     res=i/100
     print(res)
print("***while loop***")
#while loop a declear kore nite hoy
j=0
n=10
while(j<n):
    print(j)
    j+=1

print("******")
#codnition a true or false
if 10<100:
    print("true")
else:
    print("false")

print("user input")
a=int(input("enter number 1:"))#type casting(int,float dara type casting kra jay)
b=int(input("enter number 2:"))
if a>b:
    print("true")
else:
    print("false")

print("***nested if***")
age=int(input("enter your age:"))
if age>=18:
    print("you are eligable,do you have nid")
    nid=int(input())
    if nid==1:
        print("you can give vote")
    else:
        print("your age is perfect,but your don't have nid")
else:
    print("you are not eligible")

print("***if else leader***")
age=int(input("enter your age:"))
if age>=18:
    print("you are eligable,do you have nid")
    nid=int(input())
    passport=int(input("do you have passport"))
    if nid==1:
        print("you can give vote")
    elif passport==1:
        print("you can take permission")
    else:
        print("your age is perfect,but your don't have nid")
else:
    print("you are not eligible")