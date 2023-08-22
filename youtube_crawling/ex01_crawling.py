from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

okt = Okt()

def scroll():
    while True:
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        if(h1==h2):
            break

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/feed/trending")

time.sleep(2)

scroll()

title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

title_list = []

hits_list = []

for title in title_elements: 
    if title.get_attribute("aria-label") and title.text:
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits=int(hits.replace(",", ""))
  
        title_list.append(title.text)
        hits_list.append(hits)

word_list=[]
for text in title_list:
    for word, tag in okt.pos(text):
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

word_list_count = Counter(word_list)

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(5):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
plt.bar(words, counts)
plt.show()

wc = WordCloud(font_path='malgun')

result = wc.generate_from_frequencies(word_list_count)


plt.axis('off') 
plt.imshow(result)
plt.show()
wc.to_file('wordcloud_result.png')

result = pd.DataFrame(
    {
        "제목": title_list,
        "조회수":hits_list
    },
)

result.sort_values(by="조회수", ascending=False).to_csv("./result.csv", encoding="UTF-8-sig")