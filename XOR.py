#Import the necessary library
import numpy as np 
import math
#np.random.seed(0)
#TODO: write the sigmoid function sig(x) = 1/(1+e^-x)
def sigmoid (x):
    z = 1/(1 + np.exp(-x))
    return z
#TODO: write the derivative of sigmoid function sig'(x) = x * (1-x)
def sigmoid_derivative(x):
    return  x * (1-x)
#Set the Input datasets
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
#Set the expected output
expected_output = np.array([[0],[1],[1],[0]])
#TODO:Set the epoch as 10000
epochs = 10000
#TODO:Set the learning rate as 0.1
lr = 0.1
#TODO: Set the number of neuron at input layer, hidden layer and output layers as 2, 2, 1 respectively
inputLayerNeurons = 2
hiddenLayerNeurons = 2 
outputLayerNeurons = 1
#Random weights and bias initialization
#TODO: Initialize the uniform distribution to hiddent weight as (inputLayerNeurons,hiddenLayerNeurons)
hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
#TODO: Initialize the uniform distribution to hiddent bias as (1,hiddenLayerNeurons)
hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
#TODO: Initialize the uniform distribution to output weight as (hiddenLayerNeurons,outputLayerNeurons)
output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
#TODO: Initialize the uniform distribution to output bias as (1,outputLayerNeurons)
output_bias = np.random.uniform(size=(1,outputLayerNeurons))
#Display the hidden_weights, hidden_bias, output_weights, and output_bias
print("Initial hidden weights: ",end='')
print(*hidden_weights)
print("Initial hidden biases: ",end='')
print(*hidden_bias)
print("Initial output weights: ",end='')
print(*output_weights)
print("Initial output biases: ",end='')
print(*output_bias)
#Training algorithm
#TODO: Iterate over epochs
for _ in range(epochs):
	#Forward Propagation
    #TODO: Perform the dot operations between inputs and hidden_weights. Use np.dot() function
	hidden_layer_activation = np.dot(inputs,hidden_weights)
	hidden_layer_activation += hidden_bias
    #TODO: Call the sigmoid method for hidden_layer_activation
	hidden_layer_output = sigmoid(hidden_layer_activation)
    
    #TODO: Perform the dot operations between hidden_layer_output and output_weights. Use np.dot() function
	output_layer_activation = np.dot(hidden_layer_output,output_weights)
	output_layer_activation += output_bias
    #TODO: Call the sigmoid method for output_layer_activation
	predicted_output = sigmoid(output_layer_activation)

	#Backpropagation
    #TODO: Calculate the error by performing (expected_output - predicted_output)
	error = expected_output - predicted_output
    #TODO: Calculate the derivate of predicted output by performing error * sigmoid_derivative(predicted_output)
	d_predicted_output = error * sigmoid_derivative(predicted_output)
	
	error_hidden_layer = d_predicted_output.dot(output_weights.T)
    
    #TODO: Calculate the derivate of hidden layer by performing error_hidden_layer * sigmoid_derivative(hidden_layer_output)
	d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

	#Updating Weights and Biases
    #TODO: Update the output weights as output_weights = output_weights + hidden_layer_output.T.dot(d_predicted_output) * lr
	output_weights = output_weights + hidden_layer_output.T.dot(d_predicted_output) * lr
	output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
    #TODO: Update the hidden weights as hidden_weights = height_weights + inputs.T.dot(d_hidden_layer) * lr
	hidden_weights = hidden_weights + inputs.T.dot(d_hidden_layer) * lr
	hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr
    #Display the hidden_weights, hidden_bias, output_weights and output_bias after training
print("Final hidden weights: ",end='')
print(*hidden_weights)
print("Final hidden bias: ",end='')
print(*hidden_bias)
print("Final output weights: ",end='')
print(*output_weights)
print("Final output bias: ",end='')
print(*output_bias)
#Finally, display the predicted output
print("\nOutput from neural network after 10,000 epochs: ",end='')
print(*predicted_output)
