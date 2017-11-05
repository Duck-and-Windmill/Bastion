import numpy as np 
from math import ceil
from numpy import pi, exp, cos, sin, concatenate, asarray
from numpy.random import normal, randn, choice, shuffle
from torch.autograd import Variable
from torch import FloatTensor, LongTensor
from get_data import get_data 
import matplotlib.pyplot as plt


class Dataset(object):
	def __init__(self, size, batch, train=0.7, val=0.1, test=0.2):
		self.dataset = get_data.getData()
		data = self.spiral_sample(n=size)
		t = int(train*size)
		v = int(val*size)
		self.size = size
		self.batch_size = int(batch)
		self.train = data[0:t]
		self.valid = data[t:t+v]
		self.test = data[t+v:]


	def to_batched(self, dataset):
		prev = 0
		batch_set = []
		total = len(dataset)
		print("Dataset: ", dataset)

		for i in range(len(total)/self.batch_size):
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

			batch_set.append([FloatTensor(food), FloatTensor(sports), FloatTensor(finance), FloatTensor(music), 
				FloatTensor(travel), FloatTensor(tech), FloatTensor(education), FloatTensor(entertainment), FloatTensor(fashion)])

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
		