import numpy as np
from get_data import getData
import matplotlib.pyplot as plt

class Dataset(object):
	def __init__(self, size, batch, dataset = getData()[0], train=0.7, val=0.0, test=0.3):
		self.dataset = dataset
		train = int(train*size)
		valid = int(val*size)
		self.size = size
		self.batch_size = int(batch)
		self.train = self.dataset[0:train]
		# self.valid = self.dataset[t:t+v]
		self.test = self.dataset[train:]

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
		