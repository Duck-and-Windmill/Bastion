from sklearn.svm import SVC
import numpy as np
from scraper import scrape
import data

dataset = data.Dataset(35, 1)

X = dataset.load_dataset('train')
Y = dataset.load_dataset('test')
Z = dataset.load_dataset('validation')

print("X dataset: ", X)
print("Y dataset: ", Y)
print("Z dataset: ", Z)

clf = SVC()
clf.fit(X, Z)
