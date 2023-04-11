import numpy as np

# loss function and its derivative
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2));

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size;

def cross_entropy(y_true, y_pred):
    epsilon = 1e-12 # small value to avoid division by zero
    y_pred = np.clip(y_pred, epsilon, 1. - epsilon) # clip to avoid numerical instability
    return -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

"""
def cross_entropy_prime(y_true, y_pred):
    epsilon = 1e-12 # small value to avoid division by zero
    y_pred = np.clip(y_pred, epsilon, 1. - epsilon) # clip to avoid numerical instability
    return (y_pred - y_true) / ((1 - y_pred) * y_pred)
"""

def cross_entropy_prime(y_true, y_pred):
    epsilon = 1e-12
    y_pred = np.clip(y_pred, epsilon, 1. - epsilon)
    return -(y_true / y_pred) + (1 - y_true) / (1 - y_pred)