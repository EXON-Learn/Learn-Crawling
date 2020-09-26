import requests
from bs4 import BeautifulSoup

print("--Start--")

source = requests.get('http://anime.onnada.com/rank.php').text
soup = BeautifulSoup(source, "html.parser")


for i in range(5):
    repo_name = soup.select("body > div.layout-wrap > div > div > div.layout-line > table > tbody > tr:nth-child(" + str(i+1) + ") > td.maintitle > a").string
    print(repo_name)