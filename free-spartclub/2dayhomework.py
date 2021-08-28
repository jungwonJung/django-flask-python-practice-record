from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')


url = "https://search.naver.com/search.naver?&where=news&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')


articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])



for article in articles:
    title = article.select_one('dl > dt > a').text
    url =article.select_one('dl > dt > a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사',' ')
    thumbnail = article.select_one('ul > li > div > a')['href']
    ws1.append([title, url, comp, thumbnail])


driver.quit()
wb.save(filename='thumbnail.xlsx')
