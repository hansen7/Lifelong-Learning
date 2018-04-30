from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.utils import np_utils
import numpy as np

# settings
input_dim = 400
hidden1_dim = 512
hidden1_act = 'relu'
hidden2_dim = 512
hidden2_act = 'relu'
output_dim = 10
output_act = 'softmax'
max_iteration = 50

# input data
X_train = np.array(np.genfromtxt('train_data.csv', delimiter=','))
Y_train = np.array(np.genfromtxt('train_targets.csv', delimiter=','))
X_test = np.array(np.genfromtxt('test_data.csv', delimiter=','))
#Y_test = np.array(np.genfromtxt('test_targets.csv', delimiter=','))
num_train = X_train.shape[0]
num_test = X_test.shape[0]
Y_train_vec = np.zeros((num_train, output_dim))
for i in range(num_train):
    Y_train_vec[i, int(Y_train[i])]=1

# configurate net
model = Sequential()
model.add(Dense(hidden1_dim, kernel_initializer='uniform', input_shape=(input_dim,)))
model.add(Activation(hidden1_act))
model.add(Dense(hidden2_dim, kernel_initializer='uniform', input_shape=(hidden1_dim,)))
model.add(Activation(hidden2_act))
model.add(Dense(output_dim, kernel_initializer='uniform', input_shape=(hidden2_dim,))) 
model.add(Activation(output_act))
sgd=SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X_train, Y_train_vec, epochs=max_iteration)

Y_pred = model.predict(X_test)
Y_pred = np.argmax(Y_pred, axis=1)
np.savetxt('test_predictions_library.csv', Y_pred, fmt='%d', delimiter=',')

