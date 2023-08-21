import pandas as pd

student_number = [1, 2, 3, 4, 5]
score_java = pd.Series([98, 76, 60, 85, 80], index=student_number)
score_python = pd.Series([88, 92, 100, 55, 70], index=student_number)

result = score_java + score_python


score_js = pd.Series([30, 20, 10, 40, 50] , index=[3, 2, 1, 4, 5])

# print(score_js)

# print(score_js.sort_index())

result = score_java + score_python + score_js

print(result.sort_index(ascending=False))

print(result.sort_values())