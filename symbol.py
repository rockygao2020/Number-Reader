import os
import numpy as np
import numpy.linalg as npla

import matplotlib.pyplot as plt
from matplotlib import cm
#from mpl_toolkits.mplot3d import axes3d

def vectorize_img(image_path):
	'''Find vector of a 20x20 image; returns a 400-vector of all grayscale values of pixels'''
	img = plt.imread(image_path)	
	M = np.float64(img[:,:,0])
	assert M.shape[0] == 20, "Row (height) is not 20 pixels"
	assert M.shape[1] == 20, "Col (width) is not 20 pixels"
	return M.flatten()

def find_residual(image_vector, basis):
	'''Find the residual between the image vector and the projection of aforementioned
	   image vector onto the space spanned by the basis of ONE digit(symbol) object

	   Note: The each col in basis has a size = size of image vector

	   Ex: If using basis for 3, we are finding how much the image vector deviates from
	       all other vectors that were used for testing the number 3. Then the smaller the 
	       deviation/residul, the more likely our image is a 3'''

	rows, cols = basis.shape
	projection_vector = np.zeros(rows)
	for col in range(cols):
		projection_vector += ( np.dot(image_vector, basis[:,col]) ) * basis[:,col]

	residual = npla.norm(projection_vector - image_vector)

	return residual


def categorize_img(image_vector, symbol_list):
	'''Given 400-size image vector and list of symbol objects(with completed bases),
	   Classify image into one of the symbols, using singular value decomposition and
	   projection tricks'''
	
	#Edge Case
	size = len(symbol_list)
	assert size > 0, "Symbol List Empty. Cannot classify given image."
	assert symbol_list[0].getHasBasis, f"Basis for {0} Undefined."

	#Create list to store residuals
	residuals = [None] * size

	#Set up Initial Guess to be the first object
	closest_symbol = symbol_list[0]
	min_res = find_residual(image_vector, symbol_list[0].getBasis())
	residuals[0] = min_res

	for i in range(1, size):
		assert symbol_list[i].getHasBasis, f"Basis for {i} Undefined."
		res = find_residual(image_vector, symbol_list[i].getBasis())
		residuals[i] = res
		if res < min_res:
			min_res = res
			closest_symbol = symbol_list[i]

	return closest_symbol, min_res, residuals


class Symbol:
	'''Denotes the existence of a symbol that algorithm can recognize'''

	def __init__(self, new_name, new_basis=None):
		self.name = new_name
		self.basis = new_basis
		if isinstance(new_basis, np.ndarray):
			self.hasBasis = True
		else:
			self.hasBasis = False

	def getName(self):
		return self.name

	def getBasis(self):
		return self.basis

	def getHasBasis(self):
		return  self.hasBasis

	def setBasis(self, new_basis):
		'''Changes the basis; if null basis, change boolean'''
		if isinstance(new_basis, np.ndarray):
			self.hasBasis = True
		else:
			self.hasBasis = False
		self.basis = new_basis

	def readTestCases(self, test_size, test_file):
		'''Reads a decided number of test cases, from a test file
		   Determines the sample cases' basis
		   Calls setBasis() to change the symbol's basis accordingly
		   Note: Usually the amount of basis vectors = test_size, as it's just the Rank of sample_matrix	
		   Note: Required for image samples to be 20x20 pixels
		   '''

		# List holds all vectorized (size 400) images; later reshape(k, 400)
		# Each row holds 20x20 = 400 pixels reprersenting one sample image, for a total of 
		# k = test_size number of samples; we will transpose this matrix later
		# sample_list = [image 1, image 2, image 3, ... image k]
		sample_list = []

		for filename in os.listdir(test_file):
			img = plt.imread(f'{test_file}\\{filename}')
			
			M = np.float64(img[:,:,0])
			assert M.shape[0] == 20, "Row (height) is not 20 pixels"
			assert M.shape[1] == 20, "Col (width) is not 20 pixels"
			sample_list.append(M.flatten())

		sample_matrix = np.array(sample_list).reshape(test_size, 400)
		sample_matrix = sample_matrix.T

		assert sample_matrix.shape == (400, test_size)

		U, sigma, Vt = npla.svd(sample_matrix, full_matrices=False)

		'''Testing only
		print(f'SAMPLE MATRIX SIZE = {sample_matrix.shape}')
		print(sample_matrix)
		print(f'BASIS SIZE = {U.shape}')
		print(U)'''

		self.setBasis(U)







