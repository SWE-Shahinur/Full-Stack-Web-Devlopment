#file handiling
#write
file=open("file.txt",'w')
file.write("This is write file")
file.close()

#append
file=open("file.txt",'a')
file.write("it's another line")
file.close()

#file read
file=open("file.txt",'r')
for i in file.readline():
    print(i,end="")
file.close()


#OOC-CLASS,OBJECT,PRINCIPLE:ENCAPSOLUTION,INHERITANCE,ENCAPSOLUTION,POLYMORGIFM
#CLASS -class hosse object er protibimbo
#class propartise=attribute,constractor,function
class student:
    #global variable/instance
    name=''
    id=''
    nid=''
    #constractor-atrribute gula k initialize krar way
    def __init__(self,name,id,nid):
        self.name=name
        self.id=id
        self.nid=nid
    def __str__(self):
         return self.name+ ""+ self.id+ ""+ self.nid
#create an object
student=student("shahinur","2487","12345")
print('\n',student.name,student.id,student.nid)
print(student)
