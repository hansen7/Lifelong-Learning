# -*- encoding: utf-8 -*-
import numpy as np
import math


def save_data(y_arr):
    np.savetxt('test_predictions.csv', y_arr, fmt='%s', delimiter=',', newline='\n')

def normalize(mat):
    minn, maxx = mat.min(axis=1).reshape(-1, 1), mat.max(axis=1).reshape(-1, 1)
    return (mat - minn) / (maxx - minn)

def safe_exp(x):
    MAX = 1e2
    if x > MAX:
        res = math.exp(MAX)
    else:
        res = math.exp(x)
    return res  

def sigmoid(x):
    return 1. / (1 + math.exp(-x))

def sigmoid_arr(arr):
    return 1. / (1 + np.exp(-arr))

def to_categorical(y):#TODO cite!
    n_classes = int(np.max(y)) + 1
    n = y.shape[0]
    categorical = np.zeros((n, n_classes))
    categorical[np.arange(n), y] = 1
    return categorical

def prob_to_class(prob_mat):
    """
    cate_mat : np.ndarray. 2D matrix of shape (n_samples, n_classes)
    
    """
    return prob_mat.argmax(axis=-1)

def calc_neuron_output(x, hidden_layer_weights, output_layer_weights):
    """
    hidden_layer_weights : (n_neurons, input_dim)
    output_layer_weights : (n_neurons, input_dim)
    
    """
    hidden_output = sigmoid_arr(np.dot(hidden_layer_weights, x))
    prob_output = sigmoid_arr(np.dot(output_layer_weights, hidden_output))
    return hidden_output, prob_output

def update_neuron_weights(x, y, hidden_layer_weights, output_layer_weights):
    eta = 0.1
    
    hidden_output, yhat = calc_neuron_output(x, hidden_layer_weights, output_layer_weights)
    
    # update weights of output layer
    sum_used_by_hidden_layer = 0.
    g = yhat * (1. - yhat) * (y - yhat)
    output_layer_weights += eta * np.dot(g.reshape(-1, 1), hidden_output.reshape(1, -1))# two vectors dot product to a matrix
    
    # update weights of hiddent layer
    e = hidden_output * (1. - hidden_output) * np.sum(output_layer_weights * g.reshape(-1, 1), axis=0)
    hidden_layer_weights += eta * np.dot(e.reshape(-1, 1), x.reshape(1, -1))

def bp_nn(xin, yin, epoch_tol=20, accuracy_tol=.95, stable_change=2e-3, stable_tol=3):
    """standard BP.
    layer  | dimension | activation
    input  | 400       | None
    hidden | 100       | sigmoid
    output | 10        | sigmoid
    
    loss: square loss; initial weights: uni distribution on (0.05,0.05). bias = 0
    
    Parameters
    -----------
    xin : np.ndarray. Training data sample matrix of shape (n_samples, n_features).
    yin : np.ndarray. Training data target (class) array with length n_samples.
                      Values of y are integers from 0 to n_classes).
    """
    n_samples, n_features, n_classes = xin.shape[0], xin.shape[1], int(yin.max())+1
    
    # set algorithm parameters
    hidden_dim = 100
    output_dim = 10
    
    """no activation then input layer can be ignored."""#TODO is this correct?
    
    #TODO add_constant
    y_classes = yin
    yin = to_categorical(y_classes)

    hidden_layer_neurons = np.random.rand(hidden_dim, n_features) / 10. - 5e-2
    output_layer_neurons = np.random.rand(output_dim, hidden_dim) / 10. - 5e-2
    
    # standard BP training iteration
    count, epoch = 0, 0
    epoch_accuracy_small_change_count = 0
    accuracy_last, accuracy_current = -1., 0.
    while True:
        x, y = xin[count % n_samples], yin[count % n_samples]
        update_neuron_weights(x, y, hidden_layer_neurons, output_layer_neurons)
        
        count += 1
        # calculate epoch and accuracy
        if count % n_samples == 0:
            epoch = count // n_samples
            
            # calculate predictions
            probabilities = np.empty((n_samples, n_classes))
            for i, x in enumerate(xin):
                _, probabilities[i] = calc_neuron_output(x, hidden_layer_neurons, output_layer_neurons)
            prediction = prob_to_class(probabilities)
            accuracy_last, accuracy_current = accuracy_current, np.sum(y_classes == prediction) *1. / n_samples
            print("epoch:{}, accu:{}".format(epoch, accuracy_current))
        
            if abs(accuracy_last - accuracy_current) < stable_change:
                epoch_accuracy_small_change_count += 1
            else:
                epoch_accuracy_small_change_count = 0
        
        # early stop criteria
        if ((epoch > epoch_tol) or (accuracy_current > accuracy_tol)
            or (epoch_accuracy_small_change_count == stable_tol)):
            break
    
    return hidden_layer_neurons, output_layer_neurons


if __name__ == '__main__':
    
    # fix random seed for reproducibility
    np.random.seed(7)
    
    #--------------------------------- read data
    x_train = np.genfromtxt('train_data.csv', delimiter=',', dtype=float)
    y_train = np.genfromtxt('train_targets.csv', delimiter=',', dtype=int)
    x_test = np.genfromtxt('test_data.csv', delimiter=',', dtype=float)
    #y_test = np.genfromtxt('test_targets.csv', delimiter=',', dtype=int)   
    
    #--------------------------------- check validity
    assert len(x_train) == len(y_train)
    #assert len(x_test) == len(y_test)
    
    #--------------------------------- dimensions
    n_samples, n_features, n_classes = x_train.shape[0], x_train.shape[1], int(y_train.max())+1
    print(n_samples, n_features)
    
    #--------------------------------- pre-processing
    x_train = normalize(x_train)
    x_train = np.hstack((x_train, np.ones((n_samples, 1), dtype=float)))
    x_test = normalize(x_test)
    x_test = np.hstack((x_test, np.ones((x_test.shape[0], 1), dtype=float)))

    # train model
    hidden_layer_weights, output_layer_weights = bp_nn(x_train, y_train,
                                                       epoch_tol=20+n_samples//1e3, accuracy_tol=.98, 
                                                       stable_change=15e-4, stable_tol=3)
    
    # test model
    probabilities = np.empty((len(x_test), n_classes))
    for i, x in enumerate(x_test):
        _, probabilities[i] = calc_neuron_output(x, hidden_layer_weights, output_layer_weights)
    prediction = prob_to_class(probabilities)

    # output data
    save_data(prediction)    
    
    #accuracy = np.sum(y_test == prediction) *1. / len(y_test)
    #print("test data accu:{}".format(accuracy))
    
    print("Finish. Please evaluate the result.")
    