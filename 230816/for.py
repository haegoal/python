list3 = ["python", "java", ["java, type"]]
list1 = [1,2,3]
list2= ["가","나","다"]

for i in list3:
    print(i, end="             ")
    print(i, end="\n")

for i, j in zip(list1, list2):
    print(i, j)