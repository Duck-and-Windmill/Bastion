import numpy as np 
from math import ceil
from numpy import pi, exp, cos, sin, concatenate, asarray
from numpy.random import normal, randn, choice, shuffle
from torch.autograd import Variable
from torch import FloatTensor, LongTensor
from getData import getData 
import matplotlib.pyplot as plt


class Dataset(object):
	def __init__(self, size, batch, train=0.7, val=0.1, test=0.2):
		self.dataset = getData.execute()
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
		shuffle(dataset)

		