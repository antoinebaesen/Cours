import numpy as np

from Network import Network
from FCLayer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import tanh, tanh_prime
from Perte import mse, mse_prime

# training data for a multiplication
x_train = np.array([[[1,1]], [[1,2]], [[2,1]], [[2,2]], [[3,1]], [[3,2]], [[4,1]], [[4,2]], [[5,1]], [[5,2]]])
y_train = np.array([[[1]], [[2]], [[2]], [[4]], [[3]], [[6]], [[4]], [[8]], [[5]], [[10]]])

# network
net = Network()
net.add(FCLayer(2, 3))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(3, 1))
net.add(ActivationLayer(tanh, tanh_prime))

# train
net.use(mse, mse_prime)
net.fit(x_train, y_train, epochs=1000, learning_rate=0.1)

# test
out = net.predict(x_train)
print(out)