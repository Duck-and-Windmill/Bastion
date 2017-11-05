from sklearn.svm import SVC
import numpy as np
from scraper import scrape
import data
from numpy.random import shuffle

dataset = data.Dataset(35, 1)
full_dataset = dataset.load_dataset('full')

labels = ['tech', 'tech', 'tech', 'tech', 'travel', 'sports', 'travel', 'travel', 'travel', 'travel', 
	'sports', 'sports', 'sports', 'sports', 'sports', 'music', 'music', 'music', 'music', 'food', 'food', 'food', 'food', 'entertainment', 
	'entertainment', 'entertainment', 'entertainment', 'education', 'education', 'education', 'education', 'fashion', 'fashion', 'fashion', 'fashion']

paired_data = []
for i in range(0, len(full_dataset)):
	paired_data.append((full_dataset[i], labels[i]))

shuffle(dataset)

X = dataset.load_dataset('train')
Y = dataset.load_dataset('test')
Z = dataset.load_dataset('validation')

print("X dataset: ", X)
print("Y dataset: ", Y)
print("Z dataset: ", Z)

target = []
for i in range(0, len(X)):
	

clf = SVC()
clf.fit(X, target)

predictions = clf.predict(Y)

print(predictions)