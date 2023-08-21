from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def scroll():
    while True:
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        if(h1==h2):
            break

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://www.youtube.com/results?search_query=메가커피")

time.sleep(2)

scroll()

title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

#제목저장리스트
title_list = []

#조회수저장리스트
hits_list = []

for title in title_elements: 
    # 유튜브 영화, 쇼츠 제외
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"):
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        if "," in hits:
            hits=int(hits.replace(",", ""))
        elif not hits:
            hits= 0
        else:
            hits=int(hits)

        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

crawling_result = {
    "title" : title_list,
    "hits" : hits_list
}

result = pd.DataFrame(crawling_result)
# result.to_csv("./result.csv", encoding="utf-8-sig")
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")



