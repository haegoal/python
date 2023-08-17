from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("http://www.naver.com")

query_element = driver.find_element(By.XPATH, '//*[@id="query"]')
search_element = driver.find_element(By.XPATH, '//*[@id="sform"]/fieldset/button')

query_element.send_keys("오늘의 날씨")
search_element.click()
time.sleep(100)


