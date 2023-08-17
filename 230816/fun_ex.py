
num = int(input("1.세로구구단 2.가로구구단"))

def b():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i , "x", j, "=", i*j)

def c():
    for i in range(1, 10):
        print(i,"단" )
        for j in range(1, 10):
            print(i , "x", j, "=", i*j, end="  ")
            if(j==9):
                print()

def a(num):
    if num==1:
        return b()
    elif num==2:
        return c()

print(a(num))



