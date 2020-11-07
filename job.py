from indeed import extract_indeed_pages


max_indeed_pages = extract_indeed_pages()

print(max_indeed_pages)

# import requests    #  4번라인 코드를위해 pip 설치
# from bs4 import BeautifulSoup  # 내가원하는 html 코드를 가져오기위해 beautifulsoup4 설치

# indeed_results = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=Python&l=")

# indeed_soup = BeautifulSoup(indeed_results.text,"html.parser" )


# pagination = indeed_soup.find("div", {"class" : "pagination"})

# links = pagination.find_all('a')

# pages = []
# for link in links[:-1]:   # 마지막 페이지 None Type 을 무시하기위해 추가
#     pages.append(int(link.string))

# max_page = pages[-1]

# indeed.py 에 정리하고 재설정 

