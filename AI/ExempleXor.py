import numpy as np

from Network import Network
from FCLayer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import tanh, tanh_prime
from Perte import mse, mse_prime

# training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

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
#out = net.predict(x_train)
#print(out)

# using
finalTestedData = np.array([[[0,0]]])
# on essaie de prédire la sortie pour [0,0]
out = net.predict(finalTestedData)
print(out)