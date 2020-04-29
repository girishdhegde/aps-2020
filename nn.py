import numpy as np 
import matplotlib.pyplot as plt  
import random
import math


class neural_network:

	def __init__(self,shape,learning_rate = 0.0000000001):
		self.alpha = learning_rate
		self.weights = []
		self.shape = shape
		self.layers  = len(self.shape)
		self.neurons = [] 
		self.activations = []
		self.temp = []
		self.gradients = []
		self.hypothesis_errors = []
		self.errors = []
		self.initialize()


	#function to initialize weights,biases,neurons
	def initialize(self):
		# bias included in weights matrix
		#a extra bias neuron with value 1 is added to each layer

		#initialize weights matrix 
		for layer in range(self.layers - 1):
			self.neurons.append([])
			self.temp.append([])
			self.weights.append([])
			for in_neurons in range(self.shape[layer]+1):
				(self.weights[layer]).append([])
				for out_neurons in range(self.shape[layer+1]):
					sign = random.choice([-1,1])
					(self.weights[layer][in_neurons]).append(random.random() * sign)
			
		#initialize neurons
		self.neurons.append([])
		self.temp.append([])
			
		for i,n_neurons in enumerate(self.shape):
			for j in range(n_neurons+1):
				(self.neurons[i].append(1))
				(self.temp[i].append(1))

		#output layer needs no bias neuron
		#self.neurons[-1].remove(1)


	def feed_forward(self,inputs):
		#update neurons matrix input layer
		self.neurons[0][1:] = inputs
		self.temp[0][1:] = inputs
		#self.neurons[0][:len(self.neurons[0])-1] = inputs
		#print(self.neurons)

		#activation = neuron*weight + bias
		for layer in range(self.layers  - 1):
			self.neurons[layer+1][1:] = np.matmul(np.array(self.neurons[layer]) , np.array(self.weights[layer]))
			#print(self.neurons[layer+1][1:])
			#print(np.array(self.neurons[layer]))
			#print(np.array(self.weights[layer]))
		self.activations = (self.neurons).copy()
		
		#passing through activation function

		for i,layer in enumerate(self.neurons[1:]):
			for j,neuron in enumerate(layer[1:]):
				self.temp[i+1][j+1] = self.activation_function(neuron)

		self.neurons =  self.temp

		#return all layer activations,outputs and final hypothesis
		return [self.activations,self.neurons,self.neurons[-1][1:]]	

	def backpropagate(self,errors):###########################################################################################################################################
		delta = np.array(errors**0.5)
		delta = delta * (np.array(self.neurons[-1][1:]) - np.array(self.neurons[-1][1:])**2 ) 
		self.errors.append(delta)
		#print(delta)
		for layer in range(1,self.layers-1):
			#print("layer:",self.layers-layer-1)
			tempdelta = np.matmul(np.array(self.errors[layer-1]) , (np.array(self.weights[-layer][1:]).T))
			#print(tempdelta,tempdelta.shape)
			self.errors.append(tempdelta * (np.array(self.neurons[self.layers-1-layer][1:]) - (np.array(self.neurons[self.layers-1-layer][1:]))**2 ))

		self.calc_gradients()
		self.gradient_descent()

		return self.errors


	def calc_gradients(self):################################################################################################################################################
		for layer in range(self.layers-1):
			#print("test",np.array(self.neurons[layer]).T,np.array(self.errors[self.layers-2-layer]).T)
			a = []
			a.append(self.neurons[layer])
			b = []
			b.append(self.errors[self.layers-2-layer])
			self.gradients.append(np.matmul(np.array(a).T,np.array(b)).T)
		#print(self.gradients)
	

	def activation_function(self,z):
		#sigmoid 
		return (1/(1+math.exp(-z)))


	def derivative_function(self,fn):
		#derivative of sigmoid
		return fn*(1-fn)

	def calc_errors(self,outputs):
		temp1 = ((np.array(self.neurons[-1][1:]) - np.array(outputs))**2)
		self.hypothesis_errors = temp1
		return [temp1,(np.sum(temp1))/(2*self.shape[-1])]

	def gradient_descent(self):
		for layer in range(self.layers-1):
			self.weights[layer] = (self.weights[layer] - (self.alpha * np.array(self.gradients[layer])).T)
		#print(self.weights) 

net = neural_network([2,6,4])
for i in range(500000):
	#print("weights :",np.array(net.weights))
	#print("neurons:",net.neurons)
	net.feed_forward([5,7])
	e = net.calc_errors([1,0,0,1])
	b = net.backpropagate(e[0])
	print(i)
print("\noutputs:",(net.feed_forward([5,7]))[-1])