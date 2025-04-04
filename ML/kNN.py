# Implementation of k-Nearest Neighbours algorithm from scratch
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class kNN:
	def __init__(self, k=3):
		self.k = k

	def fit(self, X, y):
		self.X_train = X
		self.y_train = y

	def predict(self, X):
		predicted_labels = [self._predict(x) for x in X]
		return np.array(predicted_labels)

	def _predict(self, x):
		# Compute distances between x and all examples in the training set
		distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
		# Sort by distance and return indices of the first k neighbors
		k_indices = np.argsort(distances)[:self.k]
		# Extract the labels of the k nearest neighbor training samples
		k_nearest_labels = [self.y_train[i] for i in k_indices]
		# Return the most common class label
		most_common = Counter(k_nearest_labels).most_common(1)
		return most_common[0][0]
	
	def evaluate(self, X_test, y_test):
		predictions = self.predict(X_test)
		return accuracy_score(y_test, predictions)
	
	def __repr__(self):
		return f"kNN(k={self.k})"
	
def main():
	# Load the built-in iris dataset
	df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
	df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
	X = df.iloc[:, :-1].values
	y = df.iloc[:, -1].values

	# Split the data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

	# Instantiate the model
	k = 3
	model = kNN(k=k)
	model.fit(X_train, y_train)
	
	# Evaluate the model
	accuracy = model.evaluate(X_test, y_test)
	print(f'Accuracy: {accuracy:.2f}')

if __name__ == '__main__':
	main()