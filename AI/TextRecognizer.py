import numpy as np
from Network import Network
from FCLayer import FCLayer
from ActivationLayer import ActivationLayer
from Activation import sigmoid, sigmoid_prime
from Perte import cross_entropy, cross_entropy_prime

from keras.datasets import mnist

# load MNIST dataset

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# normalize pixel values to range between 0 and 1

# Afficher la forme des tableaux
print("train_images shape:", train_images.shape)
print("train_labels shape:", train_labels.shape)

"""
# load MNIST dataset
mnist = MNIST('samples')
train_images = mnist.train_images()
train_labels = mnist.train_labels()

# normalize pixel values to range between 0 and 1
train_images = train_images / 255.0

# flatten the images into a 1D array of size 784 (28x28)
train_images = train_images.reshape(train_images.shape[0], 784)

# create one-hot encoding for the labels
train_labels_one_hot = np.zeros((train_labels.shape[0], 10))
for i in range(train_labels.shape[0]):
    train_labels_one_hot[i][train_labels[i]] = 1

# create the network
net = Network()
net.add(FCLayer(784, 128))
net.add(ActivationLayer(sigmoid, sigmoid_prime))
net.add(FCLayer(128, 10))
net.add(ActivationLayer(sigmoid, sigmoid_prime))

# set loss function and train the network
net.use(cross_entropy, cross_entropy_prime)
net.fit(train_images, train_labels_one_hot, epochs=10, batch_size=32, learning_rate=0.1)

# test the network
test_images = mnist.test_images()
test_labels = mnist.test_labels()

# normalize pixel values to range between 0 and 1
test_images = test_images / 255.0

# flatten the images into a 1D array of size 784 (28x28)
test_images = test_images.reshape(test_images.shape[0], 784)

# predict the labels for the test images
predicted_labels_one_hot = net.predict(test_images)

# convert the predicted one-hot encoded labels back to integer labels
predicted_labels = np.argmax(predicted_labels_one_hot, axis=1)

# calculate the accuracy of the network on the test set
accuracy = np.mean(predicted_labels == test_labels)
print(f"Accuracy: {accuracy}")
"""