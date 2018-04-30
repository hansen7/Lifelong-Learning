import numpy as np
import sklearn.model_selection as sklms
import sklearn.linear_model as skllm
import math


def read_data(fname):
    res = np.genfromtxt(fname, delimiter=',')#, skip_header=1)
    return res

def save_data(index_arr, y_arr, num):
    """Transform arr into str array then save to csv file.
    
    Parameters
    -----------
    arr : np.ndarray.
    num : int. number of target file.
    
    """
    mat = np.vstack((index_arr + 1, y_arr)).T.astype(int)
    np.savetxt('experiments/fold{}.csv'.format(num), mat, fmt='%s', delimiter=',', newline='\n')

def standardize(mat):
    mean, std = mat.mean(axis=0), mat.std(axis=0)
    return (mat - mean) / std

def benchmark_sklearn(x_raw, y_raw):
    kf = sklms.KFold(n_splits=10)
    fold_generator = kf.split(x_raw)
    
    logistic = skllm.LogisticRegression(C=1e9)
    scores = []
    for i, (train_index, test_index) in enumerate(fold_generator):
        x_train, x_test = x_raw[train_index], x_raw[test_index]
        y_train, y_test = y_raw[train_index], y_raw[test_index]
        logistic.fit(x_train, y_train)
        predict = logistic.predict(x_test)
        #save_data(test_index, predict, i+1)
        scores.append(logistic.score(x_test, y_test))
    print(np.mean(scores))    

def benchmark_sklearn_cv(x_raw, y_raw):
    logistic = skllm.LogisticRegressionCV(Cs=[1e9], cv=10, multi_class='ovr')
    logistic.fit(x_raw, y_raw)
    print(logistic.scores_[1.0].mean())

def safe_exp(x):
    MAX = 1e2
    if x > MAX:
        res = math.exp(MAX)
    else:
        res = math.exp(x)
    return res

def my_logistic_newton(x_raw, y_raw, condition_number_tol=5e5, res_tol=5.):
    #--------------------------------- pre-processing
    x_std = standardize(x_raw)    
    
    x_tilde = np.hstack((x_std, np.ones((len(x_std), 1), dtype=float)))
    n_samples, n_features = x_tilde.shape

    #--------------------------------- n-folds
    kf = sklms.KFold(n_splits=10)
    fold_generator = kf.split(x_tilde)
    
    for i, (train_index, test_index) in enumerate(fold_generator):
        x_train, x_test = x_tilde[train_index], x_tilde[test_index]
        y_train, y_test = y_raw[train_index], y_raw[test_index]

        #--------------------------------- Newton Iteration
        beta = np.zeros(n_features)
    
        def calc_p1(x, beta):
            store = safe_exp(np.dot(beta, x))
            return store / (1. + store)
        
        while True:
            p1 = np.apply_along_axis(calc_p1, 1, x_train, beta)
            tmp = (y_train - p1).reshape(len(p1), -1) * x_train # element-wise product
            partial1 = -np.sum(tmp, axis=0)
            
            calc_hessian = lambda x: np.dot(x.reshape(n_features, -1), x.reshape(-1, n_features))
            partial2_hessian = np.zeros((n_features, n_features))
            for k, sample in enumerate(x_train):
                partial2_hessian += (calc_hessian(sample) * p1[k] * (1 - p1[k]))

            condition_number = np.linalg.cond(partial2_hessian)#TODO SVD
            
            partial2_inverse = np.linalg.pinv(partial2_hessian)
            delta = - np.dot(partial2_inverse, partial1)
            
            delta_percentage = (np.abs(delta / beta)) * 100
            delta_percentage.sort()
            
            if delta_percentage[int(n_features*3/4)] < res_tol:
                print("beta change small enough. Stop iteration.")
                break
            if condition_number > condition_number_tol:
                print("condition number is large enough. Stop iteration.")
                break
            beta = beta + delta
        
        #--------------------------------- make predictions using beta
        def calc_predict(x, beta):
            return 1./ (1. + safe_exp(-np.dot(x, beta)))
        
        y_predict = np.apply_along_axis(calc_predict, 1, x_test, beta)
        y_predict = np.round(y_predict)
        save_data(test_index, y_predict, i+1)    

if __name__ == '__main__':
    
    #--------------------------------- read data
    x_raw = read_data('data.csv')
    y_raw = read_data('targets.csv')
    
    #--------------------------------- check validity
    assert len(x_raw) == len(y_raw)
    
    #--------------------------------- my_logistic_newton
    my_logistic_newton(x_raw, y_raw)
    

    #--------------------------------- use sklearn as  benchmark
    #benchmark_sklearn(x_raw, y_raw)
    #benchmark_sklearn_cv(x_raw, y_raw)

    
