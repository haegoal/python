from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
driver.get("https://prod.danawa.com/list/?cate=112758&shortcutKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81")

title_elements = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

for title in title_elements:
    print(title.text)




time.sleep(100)


