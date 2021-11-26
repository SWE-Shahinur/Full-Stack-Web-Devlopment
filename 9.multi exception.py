try:
    number=int(input("enter: "))
    print(number/0)
except ValueError as e:
    print(e,"number is value not int")
except TypeError as e:
    print(e,"number is bigger then 100")
except ZeroDivisionError as e:
    print("form zerodivision error section")
except Exception as e:
    print(e)