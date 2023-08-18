aria_label = "유튜브에서 가장 짧은 영상! 게시자: 스토리 1년 전 26초 조회수 9,877,704회 - Shorts 동영상 재생"

# print(aria_label.rfind("조회수"))
# print(aria_label.find("조회수"))

# print(aria_label.rfind("조회수")+4)
# print(aria_label[38])

# print(aria_label.rfind("회"))

# print(aria_label[46])

# print(aria_label[38:47])

start_index = aria_label.rfind("조회수")+4
end_index = aria_label.rfind("회")
hits = aria_label[start_index:end_index]


hits=int(hits.replace(",", ""))

print(hits)