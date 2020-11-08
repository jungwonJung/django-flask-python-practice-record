import requests    #  4번라인 코드를위해 pip 설치
from bs4 import BeautifulSoup  # 내가원하는 html 코드를 가져오기위해 beautifulsoup4 설치

URL = f"https://stackoverflow.com/jobs?tl=python&pg=2"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser" )  # beautuifulsoup 사용해서 html 꺼내오는 코드
    pages = soup.find("div", {"class" : "pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_last_page()
    return []