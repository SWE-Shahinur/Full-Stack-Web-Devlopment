#error handaling use korle system kajkra off korbe na ,but kuthai ki eror disse se ble dibe
print("welcome")
print(10/3)

try:
    #logic statement
    print("before the error")
    print(5/0)
except Exception as e:
    # what type of error
    print(e)



print("after the error")
print(100 / 5)

try:
    var = input("enter value:")
    print(type(var))
    print(var / 2)
except Exception as e:
    print(e)

print("after the second error")
print(120/6)


