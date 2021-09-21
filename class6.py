#custom fution
#buil in function
def getsom(a,b,c,d):
    return a,b,c,d
print(getsom(1,2,3,4))

def getsum(*args): #*args diye isse moto valu nite parbo
    return args,args
print(getsum(3,4,5,6,7,8,9,10))

#dictionary value
def getsume(**kwargs):#isse moto neoa jay
    return kwargs
print(getsume(a=12,b=15,c=30))



#function er maddome function k call
def getsome(a):
    return a
def setsome(a):
    print(getsome(a))

setsome(10)

#or
def getsome(a):
    return a
def setsome(a):
    b=getsome(a)
    print(b)

setsome(10)


#buidin dunction
#sum-iteration function
print(sum([1,2,3,4,5]))#onekgula aksahe jugkre dey

#itaration function->range (build in)
for i in range(5):
    print(i)
#genarator function/custom itaration
def myrange(val):
    for i in range(0,val):
        yield i   #genarator function tai yield
for i in myrange(5):
    print("genarator",i)



#single akta akta value jokhn dorkar hbe
def myrange(val):
    for i in range(0,val):
        yield i
val=myrange(5)
print(next(val))
print(next(val))
print(next(val))

#map function
def farenhite(t):
    return (float(9)/5*t+32)
def celcious(t):
    return (float(9)/5*t-32)
temp=[12,34,21,45,54,65,76,87]
print(list(map(farenhite,temp)))
print(list(map(celcious,temp)))

#reduce function- use for serise sum
from functools import reduce
def getsum(a,b):
    return a+b
print(reduce(getsum,temp))


#lamda function-singleline function toiri te help kre
getnumber=lambda a:a*a  #perameter,value
print(getnumber(10))
print(reduce(lambda a,b:a+b,temp))

getnumberIfGraterthen100=lambda a:a if a>100 else "a is smaller then 100"
print(getnumberIfGraterthen100(10))