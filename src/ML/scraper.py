'''
Scrape websites for text data and map into main keywords.
'''

from rake.rake import Rake
from requests import get
from libextract.api import extract

def scrape(url):
	r = get(url)
	text = list(extract(r.content))

	concat = ''
	for n in text:
		concat += str(n.text_content().encode('utf-8'))

	return concat

def find_keywords(text):
	ro = Rake("SmartStoplist.txt", 5, 2, 4)
	keywords = ro.run(text)
	return [k[0] for k in keywords]

	