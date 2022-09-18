# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:01:54 2022

@author: sengh
"""

import os
import sys
import pathlib
import pickle
from collections import namedtuple
from datetime import datetime

import numpy as np
import apache_beam as beam
import annoy
from sklearn.random_projection import _gaussian_random_matrix 

import tensorflow.compat.v1 as tf
import tensorflow_hub as hub

import tensorflow_transform as tft

import tensorflow_transform.beam as tft_beam

print('TF version: {}'.format(tf.__version__))
print('TF-Hub version: {}'.format(hub.__version__))
print('TF-Transform version: {}'.format(tft.__version__))
print('Apache Beam version: {}'.format(beam.__version__))
