#!/usr/bin/env python

import numpy as np
import random

from q1_softmax import softmax
from q2_gradcheck import gradcheck_naive
from q2_sigmoid import sigmoid, sigmoid_grad

def normalizeRows(x):
    """ Row normalization function

    Implement a function that normalizes each row of a matrix to have
    unit length.
    """

    ### YOUR CODE HERE
#    print (x.sum(axis=1).reshape(-1,1))
    x = x/np.sqrt((x**2).sum(axis=1)).reshape(-1,1)
#   Equivalent Form:
    '''
    x = x/np.sqrt((x**2).sum(axis-=1, keepdims = True))

    '''
    #raise NotImplementedError
    ### END YOUR CODE

    return x


def test_normalize_rows():
    print ("Testing normalizeRows...")
    x = normalizeRows(np.array([[3.0,4.0],[1, 2]]))
    print (x)
    ans = np.array([[0.6,0.8],[0.4472136,0.89442719]])
    assert np.allclose(x, ans, rtol=1e-05, atol=1e-06)
    print ("")


def softmaxCostAndGradient(predicted, target, outputVectors, dataset):
    """ Softmax cost function for word2vec models

    Implement the cost and gradients for one predicted word vector
    and one target word vector as a building block for word2vec
    models, assuming the softmax prediction function and cross
    entropy loss.

    Arguments:
    predicted -- numpy ndarray, predicted word vector (\hat{v} in
                 the written component)
    target -- integer, the index of the target word
    outputVectors -- "output" vectors (as rows) for all tokens
            what is the meaning of the output vectors?
    dataset -- needed for negative sampling, unused here.

    Return:
    cost -- cross entropy cost for the softmax word prediction
    gradPred -- the gradient with respect to the predicted word
           vector
    grad -- the gradient with respect to all the other word
           vectors

    We will not provide starter code for this function, but feel
    free to reference the code you previously wrote for this
    assignment!
    """


#The math expression of the loss function can be found in the slides,
# to get a better understanding, I will use the same notation same as the paper assignment

    ### YOUR CODE HERE
    # y has the same shape with y_hat but all zero values, 
    # whereas the target place has a value of 1.

    #然后按照slides上的表达式 就直接求出cost
    prob = softmax(np.dot(predicted, outputVectors.T))
    cost = -np.log(prob[target])

    #这一步是用来求出 y_hat - y
    prob[target] -= 1.

    #跟推导的结果一致，
    gradPred = np.dot(prob, outputVectors)
    
    #这里我不是很清楚为什么要这么来写,这三种表达方式等价，我用的是我比较熟悉的一种
    #grad = prob[:, np.newaxis] * predicted[np.newaxis, :]
    #grad = np.outer(prob, predicted)
    grad = np.dot(prob.reshape(-1,1), predicted.reshape(1, -1))
    
    #raise NotImplementedError
    ### END YOUR CODE

    return cost, gradPred, grad


def getNegativeSamples(target, dataset, K):
    """ Samples K indexes which are not the target """

    indices = [None] * K
    for k in range(K):
        newidx = dataset.sampleTokenIdx()
        while newidx == target:
            newidx = dataset.sampleTokenIdx()
        indices[k] = newidx
    return indices


def negSamplingCostAndGradient(predicted, target, outputVectors, dataset,
                               K=10):
    """ Negative sampling cost function for word2vec models

    Implement the cost and gradients for one predicted word vector
    and one target word vector as a building block for word2vec
    models, using the negative sampling technique. K is the sample
    size.

    Note: See test_word2vec below for dataset's initialization.

    Arguments/Return Specifications: same as softmaxCostAndGradient
    """

    # Sampling of indices is done for you. Do not modify this if you
    # wish to match the autograder and receive points!
    indices = [target]
    indices.extend(getNegativeSamples(target, dataset, K))

    '''so the first space in digit stores the target'''

    ### YOUR CODE HERE
    prob =  np.dot(outputVectors, predicted)
    cost = -np.log(sigmoid(prob[target])) \
                    - np.log(sigmoid(-prob[indices[1:]])).sum()

    # prob & cost can be derived by myself easily
    
    #gradPred is partial loss function /partial Vc
    gradPred = (sigmoid(prob[target]) - 1) * outputVectors[target] \
          +  sum(-(sigmoid(-prob[indices[1:]]) - 1).reshape(-1,1) * outputVectors[indices[1:]])
    
    # grad is like partial lss funtion/ partical u   
    #grad = np.zeros_like(outputVectors)# to generate np.zeros with same shape as outputVectors
    grad = np.zeros(outputVectors.shape) #这是我更熟悉的写法
    grad[target] = (sigmoid(prob[target]) - 1) * predicted

    for k in indices[1:]:
        grad[k] += (1.0 - sigmoid(-np.dot(outputVectors[k], predicted))) * predicted

    #raise NotImplementedError
    ### END YOUR CODE

    return cost, gradPred, grad


def skipgram(currentWord, C, contextWords, tokens, inputVectors, outputVectors,
             dataset, word2vecCostAndGradient=softmaxCostAndGradient):
    """ Skip-gram model in word2vec

    Implement the skip-gram model in this function.

    Arguments:
    currentWord -- a string of the current center word
    C -- integer, context size
    contextWords -- list of no more than 2*C strings, the context words
    tokens -- a dictionary that maps words to their indices in
              the word vector list
    inputVectors -- "input" word vectors (as rows) for all tokens
    outputVectors -- "output" word vectors (as rows) for all tokens
    word2vecCostAndGradient -- the cost and gradient function for
                               a prediction vector given the target
                               word vectors, could be one of the two
                               cost functions you implemented above.

    Return:
    cost -- the cost function value for the skip-gram model
    grad -- the gradient with respect to the word vectors
    """

    cost = 0.0
    gradIn = np.zeros(inputVectors.shape)
    gradOut = np.zeros(outputVectors.shape)

    ### YOUR CODE HERE
    center_word = tokens[currentWord] # vector representation of the center word
    for context_word in contextWords:
        # index of target word
        target = tokens[context_word] # vector representation of the context word

        cost_, gradPred_, gradOut_ = word2vecCostAndGradient(inputVectors[center_word], target, outputVectors, dataset)
        #sum all the values together
        cost += cost_ 
        gradOut += gradOut_
        gradIn[center_word] += gradPred_
    ### END YOUR CODE

    return cost, gradIn, gradOut


def cbow(currentWord, C, contextWords, tokens, inputVectors, outputVectors,
         dataset, word2vecCostAndGradient=softmaxCostAndGradient):
    """CBOW model in word2vec

    Implement the continuous bag-of-words model in this function.

    Arguments/Return specifications: same as the skip-gram model

    Extra credit: Implementing CBOW is optional, but the gradient
    derivations are not. If you decide not to implement CBOW, remove
    the NotImplementedError.
    """

    cost = 0.0
    gradIn = np.zeros(inputVectors.shape)
    gradOut = np.zeros(outputVectors.shape)

    ### YOUR CODE HERE
    target = tokens[currentWord]

    # context_w correspond to the \hat{v} vector
    context_word = sum(inputVectors[tokens[w]] for w in contextWords)

    cost, gradPred, gradOut = word2vecCostAndGradient(context_word, target, outputVectors, dataset)

    gradIn = np.zeros(inputVectors.shape)
    
    for w in contextWords:
        gradIn[tokens[w]] += gradPred
    ### END YOUR CODE

    return cost, gradIn, gradOut


#############################################
# Testing functions below. DO NOT MODIFY!   #
#############################################

def word2vec_sgd_wrapper(word2vecModel, tokens, wordVectors, dataset, C,
                         word2vecCostAndGradient=softmaxCostAndGradient):
    batchsize = 50
    cost = 0.0
    grad = np.zeros(wordVectors.shape)
    N = wordVectors.shape[0]
    inputVectors = wordVectors[:int(N/2),:]
    outputVectors = wordVectors[int(N/2):,:]
    for i in range(batchsize):
        C1 = random.randint(1,C)
        centerword, context = dataset.getRandomContext(C1)

        if word2vecModel == skipgram:
            denom = 1
        else:
            denom = 1

        c, gin, gout = word2vecModel(
            centerword, C1, context, tokens, inputVectors, outputVectors,
            dataset, word2vecCostAndGradient)
        cost += c / batchsize / denom
        grad[:int(N/2), :] += gin / batchsize / denom
        grad[int(N/2):, :] += gout / batchsize / denom

    return cost, grad


def test_word2vec():
    """ Interface to the dataset for negative sampling """
    dataset = type('dummy', (), {})()
    def dummySampleTokenIdx():
        return random.randint(0, 4)

    def getRandomContext(C):
        tokens = ["a", "b", "c", "d", "e"]
        return tokens[random.randint(0,4)], \
            [tokens[random.randint(0,4)] for i in range(2*C)]
    dataset.sampleTokenIdx = dummySampleTokenIdx
    dataset.getRandomContext = getRandomContext

    random.seed(31415)
    np.random.seed(9265)
    dummy_vectors = normalizeRows(np.random.randn(10,3))
    dummy_tokens = dict([("a",0), ("b",1), ("c",2),("d",3),("e",4)])
    print ("==== Gradient check for skip-gram ====")
    gradcheck_naive(lambda vec: word2vec_sgd_wrapper(
        skipgram, dummy_tokens, vec, dataset, 5, softmaxCostAndGradient),
        dummy_vectors)
    gradcheck_naive(lambda vec: word2vec_sgd_wrapper(
        skipgram, dummy_tokens, vec, dataset, 5, negSamplingCostAndGradient),
        dummy_vectors)
    print ("\n==== Gradient check for CBOW      ====")
    gradcheck_naive(lambda vec: word2vec_sgd_wrapper(
        cbow, dummy_tokens, vec, dataset, 5, softmaxCostAndGradient),
        dummy_vectors)
    gradcheck_naive(lambda vec: word2vec_sgd_wrapper(
        cbow, dummy_tokens, vec, dataset, 5, negSamplingCostAndGradient),
        dummy_vectors)

    print ("\n=== Results ===")
    print (skipgram("c", 3, ["a", "b", "e", "d", "b", "c"],
            dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:], dataset))
    print (skipgram("c", 1, ["a", "b"],
            dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:], dataset,
            negSamplingCostAndGradient))
    print (cbow("a", 2, ["a", "b", "c", "a"],
            dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:], dataset))
    print (cbow("a", 2, ["a", "b", "a", "c"],
            dummy_tokens, dummy_vectors[:5,:], dummy_vectors[5:,:], dataset,
            negSamplingCostAndGradient))


if __name__ == "__main__":
    test_normalize_rows()
    test_word2vec()
