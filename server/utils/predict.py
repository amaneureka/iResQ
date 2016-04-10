#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Created on Sun April 10 02:45:05 2016
	@author: Manoj Pandey
	@handle: manojpandey
"""

import numpy as np
import cPickle as pickle
from math import sqrt
import pylab, random
import os.path
import sys

from pybrain.structure import SigmoidLayer
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

net = NetworkReader.readFrom('model.xml')

def activate_network(Input):
	result = net.activate(Input)
	return result
 
arg = [float(x) for x in raw_input().split()]
print activate_network(arg)