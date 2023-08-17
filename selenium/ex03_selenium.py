from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("http://www.naver.com")

login_btn = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')


login_btn.click()

time.sleep(10)


