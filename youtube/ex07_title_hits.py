from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://www.youtube.com")

time.sleep(2)

title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in title_elements: 
    if title.get_attribute("aria-label"):
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        hits=int(hits.replace(",", ""))
        print("제목", title.text)
        print("조회수", hits)


