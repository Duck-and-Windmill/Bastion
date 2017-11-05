import numpy as np 
import scraper
import requests
from BeautifulSoup import BeautifulSoup
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

	for c in gen_categories:
		page = requests.get("https://www.google.com/search?q=" + c)
		soup = BeutifulSoup(page.content)
		links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
		for link in links:
			gen_categories[c].add(scraper.find_keywords(re.split(":(?=http)",link["href"].replace("/url?q=",""))))

	return gen_categories