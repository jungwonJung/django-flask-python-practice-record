import requests    #  4번라인 코드를위해 pip 설치
from bs4 import BeautifulSoup  # 내가원하는 html 코드를 가져오기위해 beautifulsoup4 설치

URL = f"https://stackoverflow.com/jobs/developer-jobs-using-python?pg"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser" )  # beautuifulsoup 사용해서 html 꺼내오는 코드
    pages = soup.find("div", {"class" : "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)

    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class" : "mb4 fc-black-800 fs-body3"}).find("a")["title"]
    company, location = html.find("h3", {"class" : "fc-black-700 fs-body1 mb4"}).find_all("span", recursive=False)
    # company = company_row[0]
    # location = company_row[1]
    print(company.get_text(strip=True), location.get_text(strip=True))
    return {'title' : title}



def extract_jobs(last_page):
    jobs = []                      # for 문 밖에 리스트 생성
    for page in range(last_page):
        result = requests.get(f"{URL}={page+1}")
        soup = BeautifulSoup(result.text,"html.parser" )
        results = soup.find_all("div", {"class" : "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs



def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs