num = int(input("숫자를 입력하세요"))

if(num % 2 ==0 and num>0):
    print("짝수입니다.")
elif num % 2 !=0 and num>0:
    print("홀수입니다.")
else:
    print("0이상의 숫자만입력해주세요")