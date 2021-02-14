# 匿名ラジオの動画タイトルを集めるプログラム
# リンク : https://www.youtube.com/channel/UClSsb_e0HDQ-w7XuwNPgGqQ/videos?view=0&sort=da&flow=grid
# 集めた結果は"thema.csv"に保存する
import csv
import sys

from requests_html import HTMLSession

url = 'https://www.youtube.com/channel/UClSsb_e0HDQ-w7XuwNPgGqQ/videos?view=0&sort=da&flow=grid'

session = HTMLSession()
r = session.get(url)
r.html.render()

real_page_tags = r.html.find('h3')
for tag in real_page_tags:
    print(tag.text)

with open('thema.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') 
    list = []
    for tag in real_page_tags:
        list.append(tag.text)
    writer.writerow(list)
