#today class list,set,tuple
#list a multiple data input kra jay
l=[1,2.5,'shahinur']
print(l)
print(type(l))

for i in l:
    print(type(i))
    print(i)

#index valu find out
print(l[1])
print(type(l[1]))

#append(last er dike valu add kre sob smoy)
l.append('akter')
print(l)


#insert(index number use kra hoy)index dre insert
l.insert(2,"name")
print(l)


#index(valu onujayi index number print korbe)
print(l.index('shahinur'))

#count(value ta koibar ase ta return kre)
print(l.count(2.5))

#pop-valu tule neoa hoy
print(l.pop())
print(l)

print(l.pop(1))#index
print(l)


#sorting
j=[3,1,2,9,3,8,0,5,7,6]
print('before sorting',j)
j.sort()
print("after sorting",j)

#reverse
j.reverse()
print(j)

#remove-valu wise remove kora
j.remove(9)
print(j)


#nested list
print("nested list")
k=[[1,2,[9,8]],[6,7],[4,3,5]]
print(k[0])
print(k[1])
print(k[0][1])
print(k[0][2])



#mutable(valu changr kra jay)(list hosse mutable)
print("mutable")
k[0]=10
print(k)


#tuple(unmutable(valu change kra jay na)
print(tuple)
m=(1,3,3,2,5,6)
print(m)
print(m[0])
print(m.index(5))
print(m.count(3))

#set(imutable),no index,set uniqe valu niye kajkore/akei data bar bar dibe na
n={6,5,7,1,3,2,4,8,9}
print(type(n))
print(n)
n.add(10)
print(n)
n2={5,6,7,8,9}
print(n.union(n2))
print(n.intersection(n2))
print(n2.issubset(n))