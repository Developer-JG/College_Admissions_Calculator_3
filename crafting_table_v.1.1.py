from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('URL')
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)

list = []
for link in bsObject.find_all("td"):
    list.append((link.text.strip()))

print(list)
