from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://www.youtube.com")

time.sleep(2)

title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
view_elements = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

for title in title_elements:
    # print(title.text) #inner HTML값
    print(title.tag_name)  #해당 요소의 태그 이름
    print(title.get_attribute("aria-label")) #해당 요소의 ""값 가져오기



