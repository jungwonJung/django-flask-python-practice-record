from openpyxl import Workbook


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# 여기에 코드 적기!
#####################
articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
# 반복문 이후에는 무적권 탭 신경쓰기 안될가능성 농후함

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])


for article in articles:
    title = article.select_one('dl > dt > a').text
    url =article.select_one('dl > dt > a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사',' ')
    ws1.append([title, url, comp])


driver.quit()
wb.save(filename='articles.xlsx')
