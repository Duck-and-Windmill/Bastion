import numpy as np
from get_data import getData
import matplotlib.pyplot as plt

class Dataset(object):
	def __init__(self, size, batch, train=0.7, val=0.1, test=0.2):
		self.dataset = getData()
		t = int(train*size)
		v = int(val*size)
		self.size = size
		self.batch_size = int(batch)
		self.train = self.dataset[0:t]
		self.valid = self.dataset[t:t+v]
		self.test = self.dataset[t+v:]


	def to_batched(self, dataset):
		prev = 0
		batch_set = []
		total = len(dataset)
		print("Dataset: ", dataset)

		for i in range(int(total/self.batch_size)):
			points = dataset[prev:prev+self.batch_size] if prev+self.batch_size < total else dataset[prev:]
			food = []
			sports = []
			finance = []
			music = []
			travel = []
			tech = []
			education = []
			entertainment = []
			fashion = []

			for(a, b, c, d, e, f, g, h, i) in points:
				food.append(a)
				sports.append(b)
				finance.append(c)
				music.append(d)
				travel.append(e)
				tech.append(f)
				education.append(g)
				entertainment.append(h)
				fashion.append(i)
			prev += self.batch_size

			batch_set.append(food)
			batch_set.append(sports)
			batch_set.append(finance)
			batch_set.append(music)
			batch_set.append(travel)
			batch_set.append(tech)
			batch_set.append(education)
			batch_set.append(entertainment)
			batch_set.append(fashion)

		return batch_set


	def load_dataset(self, name):
		if name == 'train':
			return self.to_batched(self.train)
		elif name == 'validation':
			return self.to_batched(self.valid)
		elif name == 'test':
			return self.to_batched(self.test)
		else:
			raise Exception('data.load_dataset(): Invalid dataset')
		