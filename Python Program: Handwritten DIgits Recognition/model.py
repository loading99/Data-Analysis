import numpy as np
import tensorflow as tf
import h5py
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils



def model():
	# load data
	(X_train, y_train), (X_test, y_test) = mnist.load_data()
	x_train, x_test = X_train / 255.0, X_test / 255.0
	
	print(x_train[0])
	print('X_train size is: ', x_train.shape)
	print('X_test size is ', x_test.shape)
	print('y_train is ', y_train[0])
	print("Training datasets...")
	
	model = tf.keras.models.Sequential([
  	tf.keras.layers.Flatten(input_shape=(28, 28)),
  	tf.keras.layers.Dense(512, activation=tf.nn.relu),
  	tf.keras.layers.Dropout(0.2),
  	tf.keras.layers.Dense(10, activation=tf.nn.softmax)
	])

	model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
	model.fit(x_train,y_train)
	print("Loss and Accuracy",model.evaluate(x_test, y_test))
	return model


#model=model()
#model.save('image_model.h5')


