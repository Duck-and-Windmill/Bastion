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

	def load_dataset(self, name):
		if name == 'full':
			return self.dataset
		elif name == 'train':
			return self.train
		elif name == 'validation':
			return self.valid
		elif name == 'test':
			return self.test
		else:
			raise Exception('data.load_dataset(): Invalid dataset')
		