# -*- encoding: utf-8 -*-
"""
Class Adaboost: implementation of the original AdaBoost algorithm.
k_fold_learning: k-fold cross validation using any specific learning algorithm.

"""
import numpy as np
import math
import sklearn.model_selection as sklms
import sklearn.linear_model as skllm


def save_data(arr, n_base, fold, index):
    """arr is 1D array representing the class of each sample. """
    index += 1
    
    mat = np.hstack((index.reshape(-1, 1), arr.reshape(-1, 1)))
    np.savetxt('experiments/base{:d}_fold{:d}.csv'.format(n_base, fold+1), mat, fmt='%d', delimiter=',', newline='\n')

def standardize(mat):
    mean, std = mat.mean(axis=0), mat.std(axis=0)
    return (mat - mean) / std

def k_fold_learning(x_raw, y_raw, n_folds=10, n_bases=5, base_kwargs=None):
    #--------------------------------- pre-processing
    x_std = standardize(x_raw)
    #x_std = x_raw

    #--------------------------------- n-folds training and testing
    kf = sklms.KFold(n_splits=n_folds)
    fold_generator = kf.split(x_std)
    
    for i, (train_index, test_index) in enumerate(fold_generator):
        x_train, x_test = x_std[train_index], x_std[test_index]
        y_train, y_test = y_raw[train_index], y_raw[test_index]
        
        rgsr = Adaboost(skllm.LogisticRegression, n_bases, base_kwargs)
        rgsr.fit(x_train, y_train)
        y_pred = rgsr.predict(x_test)
        print("Progress bar:  " + '[' + '= '*i + '- '*(n_folds-i) + ']')
        #print("fold {:d} accuracy: {:6.4f}".format(i, np.sum(y_pred == y_test) / len(y_test)))#discard
        
        save_data(y_pred, n_bases, i, index=test_index)


class Adaboost(object):
    def __init__(self, base_learner, n_bases, base_kwargs=None):
        self.base_learner = base_learner
        self.n_bases = n_bases
        self.base_kwargs = base_kwargs        
        
    def fit(self, X, Y):
        
        n_samples, n_features = X.shape
        n_bases = self.n_bases
        
        weights_sample = np.ones(n_samples) #TODO: only need two rows
        
        learners = []
        weights_learner = []
        
        wrong_arr = np.zeros(n_samples).astype(bool)#discard
        
        weights_sample /= n_samples # line.1

        index = np.arange(n_samples)
        
        error_count = 0
        i = 0
        while True:
            if self.base_kwargs:
                learner = self.base_learner(**self.base_kwargs) # skllm.LogisticRegression(C)
            else:
                learner = self.base_learner()
            learner.fit(X, Y, sample_weight=weights_sample) # line.3
            
            y_pred = learner.predict(X) # must be int type
            
            wrong_arr = Y != y_pred
            error_rate = np.sum(wrong_arr.astype(int) * weights_sample) # line.4           
            
            if error_rate > 0.5:    
                error_count += 1
                if error_count > 2: # if retrain 3 times and still e > 0.5, we break. zero for classic method.
                    print("break at round {:d}".format(i))
                    break # line.5
                
                self.base_kwargs['C'] *= 2 # use stronger base learner
                continue
            
            error_rate = error_rate * (1 - 1e-6) + 1e-6 #TOOD numerical issue: from [0, 1] to [1e-6, 1]
            weights_learner.append( 1./2 * math.log((1 - error_rate) / error_rate) ) # line.6  range: [0, +\infty]
            learners.append(learner)
            
            if i+1 != n_bases:
                signs = (wrong_arr).astype(int) * 2 - 1 # from (wrong, correct) to (1, -1)
                weights_sample *= np.exp(weights_learner[i] * signs) # line.7 D_{t+1} = D_t * exp(\pm \alpha_t) / normalization
                weights_sample /= np.sum(weights_sample) # normalization
            else:
                break
            i += 1
            
        self.weights_learner = np.array(weights_learner)
        self.learners = tuple(learners)
    
    def predict(self, X):
        n_samples = X.shape[0]
        
        y_pred = tuple(map(lambda learner: learner.predict(X), self.learners))
        y_pred = np.vstack(y_pred).T # shape = (n_samples, n_bases)
        
        y_pred = y_pred * 2 - 1 # from (0, 1) to (-1, 1)
        y_pred = np.sum(y_pred * self.weights_learner, axis=1) # ensemble
        
        y_pred = np.where(y_pred > 0, 1, 0) # from continuous to discrete
        
        return y_pred
        

if __name__ == "__main__":
    from time import time
    
    # fix random seed for reproducibility
    np.random.seed(369)
    
    #--------------------------------- read data
    x = np.genfromtxt('data.csv', delimiter=',', dtype=float)
    y = np.genfromtxt('targets.csv', delimiter=',', dtype=int)
    
    #--------------------------------- k-fold adaboost with different number of base learners
    for j in [1, 5, 10, 100]:
        t0 = time()
        k_fold_learning(x, y, n_folds=10, n_bases=j, base_kwargs={'C': .1})
        t1 = time()
        print("Time cost for training and predicting with {:d} base learners: {:4.2f}s\n".format(j, t1-t0))
