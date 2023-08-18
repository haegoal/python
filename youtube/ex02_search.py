from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#크롬 브라우저 실행
driver = webdriver.Chrome()
#접속할 주소
text= input("검색어입력바람>")
time.sleep(2)

driver.get("https://www.youtube.com/results?search_query=" + text)
time.sleep(5)




# search_elements = driver.find_element(By.XPATH, '//input[@id="search"]')
# # search_elements = driver.find_element(By.NAME, 'search_query')
# # search_elements = driver.find_element(By.CSS_SELECTOR, 'input#search') 특정속성은 [] ex) '[name=""]'
# query_elements = driver.find_element(By.ID, 'search-icon-legacy')

# search_elements.send_keys(text)
# query_elements.send_keys(Keys.ENTER)

# time.sleep(2)

# title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# view_elements = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]/span[1]')

# for title in title_elements:
#     print(title.text) 

# time.sleep(5)


