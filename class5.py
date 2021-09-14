#Function
#custom function
def fun_name():
    return "custom function" #value store korbe

def another_function():
    print("another function") #value store kre na/return kre na print

print(fun_name())
another_function()

def send_number():
    return 190298194
number=send_number()
print(number)


#parameter passing(parameter bolte variable declare korbo and parameter a valu dite
def cgpa(num):
    return num
my_cgpa=cgpa(3.31)
print("MY CGPA IS:",my_cgpa)

#function,dictioary
def myget(key):
    dic={
        "name":"shahinur",
        "age":"23"
    }
    valu=dic[key]
    return valu
name=myget("age")
print(name)



#sum function
def mysum(a,b):
    return a+b
print(mysum(10,30))