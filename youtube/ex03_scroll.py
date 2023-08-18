from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소

driver.get("https://www.youtube.com/")

# java로 현재 페이지 높이값 가져오기
# 자바스크립트 실행값을 파이썬 변수로 가지고오려면 return이 필요함

def scroll():
    while True:
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        if(h1==h2):
            break

    title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

    for title in title_elements:
        print(title.text) 

    print("영상 갯수: ", len(title_elements))