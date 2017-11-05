from sklearn.svm import SVC
import numpy as np
from scraper import scrape
import data
from numpy.random import shuffle

def classify(scores):
	classes = ['food', 'sports', 'finance', 'music', 'travel', 'tech', 'education', 'entertainment', 'fashion']
	m = 0
	index = 0
	for i in range(len(scores)):
		if scores[i] > m:
			m = scores[i]
			index = i

	return classes[index]

dataset = data.Dataset(35, 1)
full_dataset = dataset.load_dataset('full')

labels = ['tech', 'tech', 'tech', 'tech', 'travel', 'sports', 'travel', 'travel', 'travel', 'travel', 
	'sports', 'sports', 'sports', 'sports', 'sports', 'music', 'music', 'music', 'music', 'food', 'food', 'food', 'food', 'entertainment', 
	'entertainment', 'entertainment', 'entertainment', 'education', 'education', 'education', 'education', 'fashion', 'fashion', 'fashion', 'fashion']

paired_data = []
for i in range(0, len(full_dataset)):
	paired_data.append((full_dataset[i], labels[i]))

shuffle(paired_data)

target = []
X  = []
for i in range(0, len(paired_data)):
	target.append(paired_data[i][1])
	X.append(paired_data[i][0])


Y = dataset.load_dataset('test')
# Z = dataset.load_dataset('validation')

target = []
for i in range(0, len(X)):
	target.append(paired_data[i][1])

clf = SVC()
clf.fit(X, target)

predictions = clf.predict(X)

test_labels = []
for items in X:
	test_labels.append(classify(items))

print(test_labels)
print(predictions)