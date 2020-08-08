# 파이썬 네이버 실시간 검색어 크롤링 예제
import requests
from bs4 import BeautifulSoup

print("--Start--")
 
source = requests.get("https://github.com/microsoft").text
soup = BeautifulSoup(source, "html.parser")


for i in range(6):
    hotKeys = soup.select("#org-repositories > div.col-12.col-md-8.d-md-inline-block > div > ul > div:nth-child(" + str(i+1) + ") > div.flex-justify-between.d-flex > div.flex-auto > h3 > a")[0].string.strip()
 
    print(hotKeys)