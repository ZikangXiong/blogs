from keras.datasets import mnist
import numpy as np


def read_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    return (x_train, y_train), (x_test, y_test)


def add_noise(x, eps=0.5):
    noise = eps * np.random.random_sample(x.shape)
    return x + noise
