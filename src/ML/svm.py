from sklearn.svm import SVC
import numpy as np
from scraper import scrape, 
import data

self.dataset = Dataset(500, 8)

X = data.load_dataset('train')
Y = data.load_dataset('test')

clf = SVC()
clf.fit(X, Y)
