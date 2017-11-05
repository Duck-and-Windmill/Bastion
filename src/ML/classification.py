import numpy as np 
import scraper
import requests
from bs4 import BeautifulSoup
import re

def index():
	gen_categories = {
		"food": [],
		"sports": [],
		"finance": [],
		"music": [],
		"travel": [],
		"tech": [],
		"education": [],
		"entertainment": [],
		"fashion":[]
	}

	for cat in gen_categories:
		page = requests.get("https://www.google.com/search?q=" + cat)
		soup = BeautifulSoup(page.content, 'lxml')
		links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
		for link in links:
			print(link)
			url = re.split(":(?=http)",link["href"].replace("/url?q=",""))[0]
			if url[:30] == "http://www.chicagotribune.com/":
				continue
			elif url[:28] == "https://www.bostonglobe.com/":
				continue
			keys = scraper.find_keywords(scraper.scrape(url))
			gen_categories[cat].extend(keys)

	print(gen_categories)
	return gen_categories

index()

