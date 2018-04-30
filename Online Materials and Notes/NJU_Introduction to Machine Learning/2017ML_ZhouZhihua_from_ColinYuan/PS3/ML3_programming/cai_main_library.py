from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.utils import np_utils
import numpy as np

model = Sequential()
model.add(Dense(512, activation='relu', input_dim=400))
model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])

train_X = np.genfromtxt('train_data.csv', delimiter=',', dtype=np.float64)
train_y = np.genfromtxt('train_targets.csv', delimiter=',', dtype=np.int)
test_X = np.genfromtxt('test_data.csv', delimiter=',', dtype=np.float64)
train_y = np_utils.to_categorical(train_y)
model.fit(train_X, train_y, epochs=50, batch_size=128)

y_pred=model.predict(test_X)
y_pred=np.argmax(y_pred,axis=1)
np.savetxt('test_predictions_library.csv', y_pred, fmt='%d', delimiter=',')
