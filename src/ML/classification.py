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

	links = {
		"food": ['https://en.wikipedia.org/wiki/Food', 'https://en.wikipedia.org/wiki/Cooking', 'https://en.wikipedia.org/wiki/Cuisine', 'https://en.wikipedia.org/wiki/Snack'],
		"sports": ['https://en.wikipedia.org/wiki/Sport', 'https://en.wikipedia.org/wiki/Basketball', 'https://en.wikipedia.org/wiki/Tennis', 'https://en.wikipedia.org/wiki/Football', 'https://en.wikipedia.org/wiki/Swimming', 'https://en.wikipedia.org/wiki/Soccer', 'https://en.wikipedia.org/wiki/Running', 'https://en.wikipedia.org/wiki/volleyball', 'https://en.wikipedia.org/wiki/boxing', 'https://en.wikipedia.org/wiki/fitness'],
		"finance": ['https://en.wikipedia.org/wiki/Finance', 'https://en.wikipedia.org/wiki/Economics', 'https://en.wikipedia.org/wiki/Stocks', 'https://en.wikipedia.org/wiki/Business', 'https://en.wikipedia.org/wiki/Entrepreneurship', 'https://en.wikipedia.org/wiki/stock_market', 'https://en.wikipedia.org/wiki/trade', 'https://en.wikipedia.org/wiki/wall_street'],
		"music": ['https://en.wikipedia.org/wiki/music', 'https://en.wikipedia.org/wiki/music_festival', 'https://en.wikipedia.org/wiki/rap', 'https://en.wikipedia.org/wiki/hip_hop', 'https://en.wikipedia.org/wiki/rhythm'],
		"travel": ['https://en.wikipedia.org/wiki/travel', 'https://en.wikipedia.org/wiki/plane', 'https://en.wikipedia.org/wiki/resort', 'https://en.wikipedia.org/wiki/hotel', 'https://en.wikipedia.org/wiki/road_trip', 'https://en.wikipedia.org/wiki/vacation', 'https://en.wikipedia.org/wiki/city'],
		"tech": ['https://en.wikipedia.org/wiki/technology', 'https://en.wikipedia.org/wiki/innovation', 'https://en.wikipedia.org/wiki/computers', 'https://en.wikipedia.org/wiki/web_development', 'https://en.wikipedia.org/wiki/computer_programming', 'https://en.wikipedia.org/wiki/software_development', 'https://en.wikipedia.org/wiki/machines', 'https://en.wikipedia.org/wiki/artificial_intelligence', 'https://en.wikipedia.org/wiki/machine_learning'],
		"education": ['https://en.wikipedia.org/wiki/school', 'https://en.wikipedia.org/wiki/education', 'https://en.wikipedia.org/wiki/crash_course', 'https://en.wikipedia.org/wiki/university', 'https://en.wikipedia.org/wiki/college', 'https://en.wikipedia.org/wiki/class', 'https://en.wikipedia.org/wiki/learning', 'https://en.wikipedia.org/wiki/'],
		"entertainment": ['https://en.wikipedia.org/wiki/movie', 'https://en.wikipedia.org/wiki/youtube', 'https://en.wikipedia.org/wiki/television', 'https://en.wikipedia.org/wiki/shopping', 'https://en.wikipedia.org/wiki/gaming', 'https://en.wikipedia.org/wiki/videos', 'https://en.wikipedia.org/wiki/anime', 'https://en.wikipedia.org/wiki/cartoons', 'https://en.wikipedia.org/wiki/cable', 'https://en.wikipedia.org/wiki/entertainment'],
		"fashion":['https://en.wikipedia.org/wiki/clothing', 'https://en.wikipedia.org/wiki/shopping', 'https://en.wikipedia.org/wiki/fashion', 'https://en.wikipedia.org/wiki/hypebeast', 'https://en.wikipedia.org/wiki/shoes', 'https://en.wikipedia.org/wiki/brand', 'https://en.wikipedia.org/wiki/branding', 'https://en.wikipedia.org/wiki/style', 'https://en.wikipedia.org/wiki/mainstream']
	}

	for cat in gen_categories:
		page = requests.get("https://www.google.com/search?q=" + cat)
		soup = BeautifulSoup(page.content, 'lxml')
		links = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
		for link in links:
			for l in link:
				keys = scraper.find_keywords(scraper.scrape(url))
				gen_categories[cat].extend(keys)

	print(gen_categories)
	return gen_categories

index()

