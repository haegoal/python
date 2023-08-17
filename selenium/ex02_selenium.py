from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("http://www.example.com")

# find_element는 여러개의 요소중에 첫번쨰 걸리는것만 가지고옴
#find_elements는 여러개요소 타입 리스트
p_element = driver.find_element(By.TAG_NAME, 'p')
print(p_element)
print(type(p_element))
print(p_element.text)


