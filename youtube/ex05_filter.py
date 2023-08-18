from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소

driver.get("https://www.youtube.com/")


def scroll():
    while True:
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        h2 = driver.execute_script("return document.documentElement.scrollHeight")
        if(h1==h2):
            break

search = driver.find_element(By.CSS_SELECTOR, 'input#search')
search.send_keys("음메")
query_elements = driver.find_element(By.ID, 'search-icon-legacy')
query_elements.send_keys(Keys.ENTER)
time.sleep(2)
filter = driver.find_element(By.XPATH, '//*[@id="filter-button"]')
filter.click()
time.sleep(2)
title=driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
title.click()
time.sleep(2)
scroll()
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

for title in titles:
        print(title.text) 
