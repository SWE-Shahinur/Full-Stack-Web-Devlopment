#dictionary(key valu pair)
dec={
    "key1":"value1",#every value aginst key thakbe
    "key2":"value2",
    "key3":"value3"
}
print(dec)
print(type(dec))
print(dec["key1"],dec["key2"])

#dictionary for loop
for i,j in dec.items():#item 2 bahe vag kre
    print(i,j)


#nested valu
dics={
    "name":"shahinur",
    "age":"23",
    "address":{
        "prasant":"dhaka",
        "parmanent":{
            "dis":"comilla",
            "thana":"homna"
        }
    }

}
print(dics)
print(dics["name"],dics["address"]["parmanent"]["dis"])



#data fram student data base
df={
    "name":["shahinur","maysha","moon"],
    "dep":["swe","civil","CSE"],
    "semester":["5","8","11"]
}
for i,j in df.items():
    print(i,j)


#only value
print(df.values())

#only keys
print(df.keys())

#get(key dore kaj
print(df.get("name"))


#update
df_update={"name":"Sharmin"}
df.update(df_update)
print(df)
dics_update={"address":{"prasant":"razshahi"}}
dics.update(dics_update)
print(dics)


#slising
print("slising")
l=[1,4,2,3,5,9,8,5,7,6]
print(l[:6]) #this is slising
print(l[:])#all valu
print(l[: -1]) #last valu bad diye count korbe
print(l[:: -1])#reverce korbe
#others way
print("others way")
for i in range(6):
    print(l[i])