#!/usr/bin/env python

import random
<<<<<<< HEAD

import numpy as np
import matplotlib
import time

from q3_sgd import *
from q3_word2vec import (word2vec_sgd_wrapper, negSamplingCostAndGradient,
                                                 skipgram)
from utils.treebank import StanfordSentiment

matplotlib.use('agg')
import matplotlib.pyplot as plt

=======
import numpy as np
from utils.treebank import StanfordSentiment
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import time

from q3_word2vec import *
from q3_sgd import *
>>>>>>> parent of 885ef88... delete unsuccessful trial

# Reset the random seed to make sure that everyone gets the same results
random.seed(314)
dataset = StanfordSentiment()
tokens = dataset.tokens()
nWords = len(tokens)

# We are going to train 10-dimensional vectors for this assignment
dimVectors = 10

# Context size
C = 5

# Reset the random seed to make sure that everyone gets the same results
random.seed(31415)
np.random.seed(9265)

<<<<<<< HEAD
startTime = time.time()
wordVectors = np.concatenate(
    ((np.random.rand(nWords, dimVectors) - 0.5) /
     dimVectors, np.zeros((nWords, dimVectors))),
    axis=0)

word2vec = lambda vec: word2vec_sgd_wrapper(skipgram, tokens, vec, dataset, C,
                                            negSamplingCostAndGradient)
wordVectors = sgd(word2vec, x0=wordVectors, step=0.3, iterations=40000, postprocessing=None,
                  useSaved=True, PRINT_EVERY=10)
# Note that normalization is not called here. This is not a bug,
# normalizing during training loses the notion of length.

print("sanity check: cost at convergence should be around or below 10")
print("training took %d seconds" % (time.time() - startTime))

# concatenate the input and output word vectors
wordVectors = np.concatenate((wordVectors[:nWords, :], wordVectors[nWords:, :]), axis=0)
# wordVectors = wordVectors[:nWords,:] + wordVectors[nWords:,:]

visualizeWords = [
    "the", "a", "an", ",", ".", "?", "!", "``", "''", "--",
=======
startTime=time.time()
wordVectors = np.concatenate(
    ((np.random.rand(nWords, dimVectors) - 0.5) /
       dimVectors, np.zeros((nWords, dimVectors))),
    axis=0)
print(wordVectors.shape)
wordVectors = sgd(
    lambda vec: word2vec_sgd_wrapper(skipgram, tokens, vec, dataset, C,
        negSamplingCostAndGradient),
    wordVectors, 0.3, 40000, None, True, PRINT_EVERY=10)
# Note that normalization is not called here. This is not a bug,
# normalizing during training loses the notion of length.

print ("sanity check: cost at convergence should be around or below 10")
print ("training took %d seconds" % (time.time() - startTime))

# concatenate the input and output word vectors
wordVectors = np.concatenate(
    (wordVectors[:nWords,:], wordVectors[nWords:,:]),
    axis=0)
# wordVectors = wordVectors[:nWords,:] + wordVectors[nWords:,:]

visualizeWords = [
    'the', 'a', "an", ",", ".", "?", "!", "``", "''", "--",
>>>>>>> parent of 885ef88... delete unsuccessful trial
    "good", "great", "cool", "brilliant", "wonderful", "well", "amazing",
    "worth", "sweet", "enjoyable", "boring", "bad", "waste", "dumb",
    "annoying"]

visualizeIdx = [tokens[word] for word in visualizeWords]
visualizeVecs = wordVectors[visualizeIdx, :]
temp = (visualizeVecs - np.mean(visualizeVecs, axis=0))
covariance = 1.0 / len(visualizeIdx) * temp.T.dot(temp)
<<<<<<< HEAD
U, S, V = np.linalg.svd(covariance)
coord = temp.dot(U[:, 0:2])

for i in range(len(visualizeWords)):
    plt.text(coord[i, 0], coord[i, 1], visualizeWords[i],
             bbox=dict(facecolor='green', alpha=0.1))

plt.xlim((np.min(coord[:, 0]), np.max(coord[:, 0])))
plt.ylim((np.min(coord[:, 1]), np.max(coord[:, 1])))

plt.savefig('q3_word_vectors.png')
=======
U,S,V = np.linalg.svd(covariance)
coord = temp.dot(U[:,0:2])

plt.figure()
for i in range(len(visualizeWords)):
    plt.text(coord[i,0], coord[i,1], visualizeWords[i],
        bbox=dict(facecolor='green', alpha=0.1))

plt.xlim((np.min(coord[:,0]), np.max(coord[:,0])))
plt.ylim((np.min(coord[:,1]), np.max(coord[:,1])))

plt.savefig('q3_word_vectors.png')
>>>>>>> parent of 885ef88... delete unsuccessful trial
