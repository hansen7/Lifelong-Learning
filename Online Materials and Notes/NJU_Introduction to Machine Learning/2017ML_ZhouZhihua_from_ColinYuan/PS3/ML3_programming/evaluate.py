import numpy as np
target=np.genfromtxt('test_targets.csv')
prediction=np.genfromtxt('test_predictions_library.csv')

print(sum(target==prediction)/prediction.shape[0])
