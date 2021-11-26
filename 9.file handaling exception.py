try:
    file = open("test.txt", "r")
    for i in file:
        print(i, end='')

except Exception as e:
    print(e)

finally:
    if file.name == 'test.txt':
        print("file already exit")
    else:
        print("there is no test.txt file, so we are create this file")
        file = open("test.txt", "w")

