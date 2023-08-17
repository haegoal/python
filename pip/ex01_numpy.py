import numpy as np

#배열
arr = np.array([3, 5, 4, 1, 6, 2, 7])

print(arr)

#정렬
arr = np.sort(arr)
print(arr)

arr = np.sort(arr)[::-1]
print(arr)


#합침
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr3 = np.concatenate([arr1, arr2])
print(arr3)

#배열 연산
arr11 = arr1 + 10
print(arr11)

# 슬라이싱 / 시작은 포함, 끝은 제외
arr4 = np.array([1,2,3,4,5,6,7,8,9])
print(arr4[:2])
print(arr4[1:2])
print(arr4[3:8])
print(arr4[6:])
print(arr4[4:7])
