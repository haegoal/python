from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://www.youtube.com/feed/trending")

time.sleep(2)

title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

#제목저장리스트
title_list = []

#조회수저장리스트
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

crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# result.to_csv("./result.csv", encoding="utf-8-sig")
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")
