import requests
from bs4 import BeautifulSoup
import re

vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
# 全てのaタグを抽出
elems = soup.find_all(href=re.compile("http://www.vgmusic.com/"))

for elem in elems:
  print(elem.contents[0])
  print(elem.attrs['href'])
