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