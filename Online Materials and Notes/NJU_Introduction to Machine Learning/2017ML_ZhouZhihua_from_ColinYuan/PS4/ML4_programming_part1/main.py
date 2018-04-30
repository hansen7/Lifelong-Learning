import numpy as np
from sklearn.svm import SVC

def predict(Xt, model):
	sv = model.support_vectors_
	n_sv = sv.shape[0]
	alpha = model.dual_coef_
	gamma = model.gamma
	b = model.intercept_
	n_xt = Xt.shape[0]
	pred = np.zeros(n_xt)
	for i in range(n_xt):
		sum = 0
		for j in range(n_sv):
			d = Xt[i, :]-sv[j, :]
			sum = sum + alpha[0, j] * np.exp(-gamma * np.dot(d, d.T))
		if sum + b > 0:
			pred[i] = 1
		else:
			pred[i] = 0

	return pred;