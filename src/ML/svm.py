from sklearn.svm import SVC
import numpy as np
from scraper import scrape
import data

dataset = data.Dataset(100, 1)

X = dataset.load_dataset('train')
Y = dataset.load_dataset('test')

print("X dataset: ", X)
print("Y dataset: ", Y)

clf = SVC()
clf.fit(X, Y)
