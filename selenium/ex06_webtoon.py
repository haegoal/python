from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://comic.naver.com/webtoon")

title_elements = driver.find_elements(By.CLASS_NAME, 'text')
                                                    
for title in title_elements:
    print(title.text)


time.sleep(112321)


