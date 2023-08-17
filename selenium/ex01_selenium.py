from selenium import webdriver
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("http://www.google.co.kr")
time.sleep(5)