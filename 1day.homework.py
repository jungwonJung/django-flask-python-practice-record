import dload

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EB%B3%B4%EB%8D%94%EC%BD%9C%EB%A6%AC") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################
thumbnails = soup.select('#imgList > div > a > img')


i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'img.homework/1{i}.jpg')
    i += 1


driver.quit() # 끝나면 닫아주기