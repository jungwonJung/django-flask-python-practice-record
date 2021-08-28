import requests    #  4번라인 코드를위해 pip 설치
from bs4 import BeautifulSoup  # 내가원하는 html 코드를 가져오기위해 beautifulsoup4 설치

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=Python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&fromage=any&limit={LIMIT}"


def get_last_page():
    
    results = requests.get(URL)
    soup = BeautifulSoup(results.text,"html.parser" )  # beautuifulsoup 사용해서 html 꺼내오는 코드
    pagination = soup.find("div", {"class" : "pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[-2]:   # 마지막 페이지 None Type 을 무시하기위해 추가
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title=html.find("h2",{"class":"title"}).find("a")["title"]   # div 가 아니라 h2 안에 title 가 있었음....

    company = html.find("span",{"class":"company"})         # soup 형태로만들어준 company 를 38 번에서는 변수에 새로운값을 지정해줌

    company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)

    else:
        company = str(company.string)
    company = company.strip()                  # strip() 괄호 안에있는 글자 "f"  면 f 를 지워주고 출력해줌 

    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]

    job_id = html.find("h2",{"class":"title"}).find("a")["id"][3:]

    return {
        "title" : title,
        "comapany" : company,
        "location" : location,
        "link" : f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"
    }



def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"scrapping page {page}")        #  scrapping page 1,2,3 카운트 되는 코드 추가
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs

