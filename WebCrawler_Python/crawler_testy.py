from bs4 import BeautifulSoup

import requests

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

wb_data = requests.get(url) 

soup = BeautifulSoup(wb_data.text,'lxml')

#print(soup)
titles = soup.select("div.property_title > a")
imags_160 = soup.select('img[width="160"]')
cates = soup.select('div.p13n_reasoning_v2')
print(imags_160,cates)

for title,img,cate  in zip(titles, imags_160, cates):
	data = {
		'title':title.get_text(),
		'img':img.get('src'),
		'cate':list[cate.stripped_strings],
	}
	print(data)