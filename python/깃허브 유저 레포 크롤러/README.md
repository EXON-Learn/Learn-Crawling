# 깃허브 팀 레포 크롤러
```js
import requests
from bs4 import BeautifulSoup

print("--Start--")

team = input("팀 링크를 입력해주세요. : ")
repo = int(input("크롤링할 레포의 개수를 입력해주세요. : "))
source = requests.get(team).text
soup = BeautifulSoup(source, "html.parser")


for i in range(repo):
    repo_name = soup.select("#org-repositories > div.col-12.col-md-8.d-md-inline-block > div > ul > div:nth-child(" + str(i+1) + ") > div.flex-justify-between.d-flex > div.flex-auto > h3 > a")[0].string.strip()
    print(repo_name)
```