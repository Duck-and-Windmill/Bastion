import numpy as np 
from sklearn.cluster import KMeans
from scraper import *

X = np.array()
urls = []

for i in range(0, len(dataset)):
	X.add(scraper.find_keywords(scraper.scrape(url[i])))

kmeans = KMeans(n_clusters=10, random_state=0).fit(X)