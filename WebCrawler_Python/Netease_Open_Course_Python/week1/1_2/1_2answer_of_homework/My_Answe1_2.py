#!/usr/bin/env python
#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup


path = './index.html'

def count_stars(_all):
	stars = 0
	for i in range(1,6):
		try:
			_all.find_all("span", class_ = "glyphicon glyphicon-star" )[i]
			stars += 1
#	print "\n================\n"
		except:
			continue
	return str(stars)

infos = []

with open (path, 'r') as file:
	soup = BeautifulSoup(file.read(), 'lxml')
	_all = soup.find_all("div", class_ = "thumbnail")
#	for i in _all:
#		count_stars(i)



	for graphs, titles, prices, nrates, stars in zip(_all, _all, _all, _all, _all):
		info = {
			'graph': graphs.find_all("img")[0]["src"],
			'title': titles.find_all("a")[0].text,
			'price': prices.find_all("h4", class_ = "pull-right")[0].text,
			'nrate': nrates.find_all("p", class_ = "pull-right")[0].text,
			'star' : count_stars(stars)
		}
	#	print graphs
	#	print "\n ============= \n"
		print info
		infos.append(info)

#	print (infos)