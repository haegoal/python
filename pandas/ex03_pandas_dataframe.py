import pandas as pd

scores = pd.DataFrame(
    [
        [96, 76, 60, 85, 80],
        [88, 92, 100, 20, 70],
        [10, 20, 30, 40, 50]
    ]
)

scored = pd.DataFrame(
    [
        [96, 76, 60, 85, 80],
        [88, 92, 100, 20, 70],
        [10, 20, 30, 40, 50] 
    ],
    index=["java", "python", "js"]
)

# print(scored)

student_number = [1, 2, 3, 4, 5]

scored = pd.DataFrame(
    {
        "java": [96, 76, 60, 85, 80],
        "python" : [88, 92, 100, 20, 70],
        "js": [10, 20, 30, 40, 50] 
    },
    index=student_number
)


scored["이름"] = ["김파이", "이파이", "박파이", "최파이", "정파이"]
scored.loc[6] = [80, 80, 80, "조파이"]
print(scored)

#transpose 는 행열 체인지
scores = pd.DataFrame(
    {
        "이름" : ["김파이", "이파이", "박파이", "최파이", "정파이"],
        "java": [96, 76, 60, 85, 80],
        "python" : [88, 92, 100, 20, 70],
        "js": [10, 20, 30, 40, 50] 
    },
    index=student_number
)

print(scores.sort_values(by="이름", ascending=True))
#첫 두줄 출력
print(scores.head(2))
# 끝 두줄 출력
print(scores.tail(2))

scores.to_csv("./scores.csv", encoding="UTF-8-sig")


# 딕셔너리 > DataFrame
# scores_dict = {
#    "java": [96, 76, 60, 85, 80],
#     "python" : [88, 92, 100 , 20, 70],
#     "js": [10, 20, 30, 40, 50]  
# }

# scores = pd.DataFrame(scores_dict)

# scores["이름"] = ["김파이", "이파이", "박파이", "최파이", "정파이"]
# print(scores)

# scores.loc[6] = [80, 80, 80, "조파이"]

# print(scores)