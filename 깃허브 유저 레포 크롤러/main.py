import requests
from bs4 import BeautifulSoup

print("--Start--")

team = input("유저 링크를 입력해주세요. : ") + "?tab=repositories"
repo = int(input("크롤링할 레포의 개수를 입력해주세요. : "))
source = requests.get(team).text
soup = BeautifulSoup(source, "html.parser")


for i in range(repo):
    repo_name = soup.select("#user-repositories-list > ul > li:nth-child(" + str(i+1) + ") > div.col-10.col-lg-9.d-inline-block > div.d-inline-block.mb-1 > h3 > a")[0].string.strip()
    print(repo_name)