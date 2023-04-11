import numpy as np

# activation function and its derivative
def tanh(x):
    return np.tanh(x);

def tanh_prime(x):
    return 1-np.tanh(x)**2;

# Sigmoid est une fonction qui prend en entrée un nombre réel et qui renvoie un nombre réel compris entre 0 et 1
# Elle sert à normaliser les valeurs de sortie de la fonction de coût
def sigmoid(x):
    return 1/(1+np.exp(-x));

# Sigmoid prime est la dérivée de la fonction sigmoid
def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x));
