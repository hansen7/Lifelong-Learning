import pandas as pd
import numpy as np
from nltk.corpus import wordnet as wn


##'panda' -- ENGLISH Word 
panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()


for item in list(panda.closure(hyper)):
	print (item)


for item in range(5):
	print ("-------\n")
