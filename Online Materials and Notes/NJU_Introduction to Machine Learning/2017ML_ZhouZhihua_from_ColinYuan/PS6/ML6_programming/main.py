import numpy as np
from numpy import random as npr
npr.seed(0)
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

X_data = np.genfromtxt('data.csv', delimiter=',')
y_data = np.genfromtxt('targets.csv')

def AdaBoost_reweight(X_train, y_train, X_test, y_test, T):
	lrs = []
	for i in range(T):
		lrs.append(LogisticRegression())
	num_train = X_train.shape[0]
	num_test = X_test.shape[0]
	d = np.ones(num_train) / num_train
	output = np.zeros(num_test)
	for i, lr in enumerate(lrs):
		lr.fit(X_train, y_train, sample_weight=d)
		y_train_pred = lr.predict(X_train)
		error_rate = np.float(sum(y_train_pred != y_train)) / num_train
		if error_rate > 0.5:
			break
		error_rate = error_rate + 1e-9	# to prevent dividing 0
		alpha = 0.5 * np.log((1-error_rate)/error_rate)
		y_test_pred = lr.predict(X_test)
		output = output + alpha * y_test_pred
		sign = (y_train == y_train_pred) * (-1) + (y_train != y_train_pred) * 1
		d = d * (np.exp(alpha*sign))
		d = d / sum(d)
	return (output >= 0) * 1 + (output < 0) * (-1)

def AdaBoost_resample(X_train, y_train, X_test, y_test, T):
	lrs = []
	for i in range(T):
		lrs.append(LogisticRegression())
	num_train = X_train.shape[0]
	num_test = X_test.shape[0]
	d = np.ones(num_train) / num_train
	output = np.zeros(num_test)
	for i, lr in enumerate(lrs):
		idx = npr.choice(num_train, np.int(num_train), p=d, replace=True)
		lr.fit(X_train[idx], y_train[idx])
		y_train_pred = lr.predict(X_train)
		error_rate = np.float(sum(y_train_pred != y_train)) / num_train
		if error_rate > 0.5:
			break
		error_rate = error_rate + 1e-9	# to prevent dividing 0
		alpha = 0.5 * np.log((1-error_rate)/error_rate)
		y_test_pred = lr.predict(X_test)
		output = output + alpha * y_test_pred
		sign = (y_train == y_train_pred) * (-1) + (y_train != y_train_pred) * 1
		d = d * (np.exp(alpha*sign))
		d = d / sum(d)
	return (output >= 0) * 1 + (output < 0) * (-1)

for T in [1, 5, 10, 100]:
	cv = KFold(n_splits=10).split(y_data)
	for i, (train_idx, test_idx) in enumerate(cv):
		X_train = X_data[train_idx]
		y_train = y_data[train_idx]
		X_test = X_data[test_idx]
		y_test = y_data[test_idx]
		y_train[y_train == 0] = -1
		y_test[y_test == 0] = -1

		res = np.empty((y_test.shape[0], 2))
		res[:,0] = test_idx + 1
		res[:,1] = AdaBoost_resample(X_train, y_train, X_test, y_test, T)
		res[res[:,1] == -1,1] = 0
		np.savetxt('experiments/base{}_fold{}.csv'.format(T, i+1), res, fmt='%d', delimiter=',')
