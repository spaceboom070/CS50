def faces() :
    a = int(input("enter a positive number:"))
    if a < 0:
        print("please enter a positive number")
    else:
        if a == 0:
            print("please enter a positive number")
        while a > 0:
            print(":)", end=" ")
            a = a - 1
faces()