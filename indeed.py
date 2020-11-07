import requests    #  4번라인 코드를위해 pip 설치
from bs4 import BeautifulSoup  # 내가원하는 html 코드를 가져오기위해 beautifulsoup4 설치

START = 10
URL = f"https://kr.indeed.com/jobs?q=Python&start={10}"


def extract_indeed_pages():
    
    results = requests.get(URL)
    soup = BeautifulSoup(results.text,"html.parser" )
    pagination = soup.find("div", {"class" : "pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:   # 마지막 페이지 None Type 을 무시하기위해 추가
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        print(f"start={page*START}")