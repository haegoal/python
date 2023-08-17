import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

#한글
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

# plt.plot([1, 2, 3, 4], [3,6,10,12])

# "o"는 만나는 곳끼리 점, o-는 선과 점, o--는 점선
plt.plot([1, 2, 3, 4], [3,6,10,12], "o-")

plt.xlabel("x 축")
plt.ylabel("y 축")
plt.show()