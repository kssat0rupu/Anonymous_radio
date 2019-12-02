# 匿名ラジオの動画タイトルを集めるプログラム
# リンク : https://www.youtube.com/channel/UClSsb_e0HDQ-w7XuwNPgGqQ
# 集めた結果は"thema.csv"に保存する
import requests
from bs4 import BeautifulSoup
import sys
import csv

r = requests.get("https://www.youtube.com/channel/UClSsb_e0HDQ-w7XuwNPgGqQ/videos")
q = requests.get("https://www.youtube.com/channel/UClSsb_e0HDQ-w7XuwNPgGqQ/videos?view=0&sort=da&flow=grid")

#print(r.text)
#print(q.text)

#soup = BeautifulSoup(r.content, "html.parser")
soup_1 = BeautifulSoup(q.content, "html.parser")

real_page_tags = soup_1.find_all("h3")
for tag in real_page_tags:
    print(tag.text)

with open('thema.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') 
    list = []
    for tag in real_page_tags:
        list.append(tag.text)
    writer.writerow(list)
#sys.exit()
'''
real_page_tags = soup.find_all("h3")
for tag in real_page_tags:
    #print(tag.text)

print(soup.find_all("h3", "yt-lockup"))
'''