# 함수를 모두 import , 장점: 앞에 파일명 안 쓸 수 있음.
from ex01_function import *

while True:
    num = int(input("1.세로구구단 2.가로구구단 3.종료"))
    if num==1:
        b()
    elif num==2:
        c()
    elif num==3:
        print("종료합니다.")
        break
    else:
        print("잘못 선택하셨습니다.")
