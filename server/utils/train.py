#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Created on Sun April 10 02:45:05 2016
	@author: Manoj Pandey
	@handle: manojpandey
"""
# train a regression Multi-Layer Perceptron

import numpy as np
import cPickle as pickle
from math import sqrt
import pylab
import random
import os.path
from pybrain.structure import SigmoidLayer
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader


train_file = 'data/train.csv'
# validation_file = 'data/validation.csv'
output_model_file = 'model.pkl'

# hidden_size = 4
epochs = 500

# load data
# def loadData():
train = np.loadtxt(train_file, delimiter=' ')
Input = train[0:,0:3]
Output = train[0:,3:5]

# validation = np.loadtxt(validation_file, delimiter=',')
# train = np.vstack((train, validation))

# x_train = train[:, 0:-1]
# y_train = train[:, -1]
# y_train = y_train.reshape(-1, 1)

# input_size = x_train.shape[1]
# target_size = y_train.shape[1]

# prepare dataset
# def prepare dataset(input_size, target_size):
ds = SDS(Input,Output)
# ds.addSample(input_size)
# ds.setField('input', x_train)
# ds.setField('target', y_train)

# init and train
# def initTrain(input_size, hidden_size, input, output):
# net = buildNetwork(input_size, hidden_size, target_size, bias=True)
net = buildNetwork(3,  # input layer
                             4,  # hidden0
                             2,  # output
                             hiddenclass=SigmoidLayer,
                             outclass=SigmoidLayer,
                             bias=True
                             )
for i,o in zip(Input,Output):
    ds.addSample(i,o)

trainer = BackpropTrainer(net, ds)
    
print "training for {} epochs...".format(epochs)

for i in range(epochs):
    mse = trainer.train()
    rmse = sqrt(mse)
    print "training RMSE, epoch {}: {}".format(i + 1, rmse)

pickle.dump(net, open(output_model_file, 'wb'))
