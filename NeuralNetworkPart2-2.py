import numpy as np
import random
import matplotlib.pyplot as plt

# How many times you want to do it.
trainingNumber = 900

# Sigmoid function coded with Numpy
def sigmoid(x):
     return 1 / (1 + np.exp(-x))

# Calculate the slope by using the derivative of the sigmoid function
def sigmoidSlope(x):
     return x * (1 - x)



# put 4 by 3 matrixs
inputData = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

# Can slove both
referenceOutput0 = np.array([[0],[0],[1],[1]])

#  Multilayer can only slove
referenceOutput1 = np.array([[0],[1],[1],[0]])

f =[]
s =[]
t =[]
l =[]

random.seed(1)

# Weights of the synapses connecting input and output Layer are randomly
# initialized with mean 0
weights01_A = 2*np.random.random((3, 1)) - 1
weights01_B = 2*np.random.random((3, 1)) - 1


for i in range(trainingNumber):

# Set the input data for simple forward propagation 
    inputLayer0 = inputData
    inputLayer1 = inputData

 #  Apply Sigmoid Function to the dot product of two arrays  
    outPutPerceptronLayer0 = sigmoid(np.dot(inputLayer0, weights01_A))
    outPutPerceptronLayer1 = sigmoid(np.dot(inputLayer1, weights01_B))

# The difference between the output perception Layer and the reference output
    outputError0 = referenceOutput0 - outPutPerceptronLayer0
    outputError1 = referenceOutput1 - outPutPerceptronLayer1

# The difference between refernce (outputError) output multiplied by the slope
# of the sigmoid function at value of the output perceptron Layer
    outputDelta0 = outputError0 * sigmoidSlope(outPutPerceptronLayer0)
    outputDelta1 = outputError1 * sigmoidSlope(outPutPerceptronLayer1)

# Updating the weights
    weights01_A += np.dot(inputLayer0.T, outputDelta0)

# append which means add
    f.append(np.mean(np.abs(outputError0)))

# Updating the weights
    weights01_B += np.dot(inputLayer1.T, outputDelta1)

# append which means add
    s.append(np.mean(np.abs(outputError1)))

    


random.seed(42)

# Random initial weights for synapses from input to first hiden Layer
weights01_a = 2 * np.random.random((3, 4)) - 1
# Random initial weights for synapses from first hidden Layer to output Layer
weights02_a = 2 * np.random.random((4, 1)) - 1

# Random initial weights for synapses from input to first hiden Layer
weights01_b = 2 * np.random.random((3, 4)) - 1
# Random initial weights for synapses from first hidden Layer to output Layer
weights02_b = 2 * np.random.random((4, 1)) - 1


for e in range(trainingNumber):

# Set the input data for all Layers as forward propagtion
    inputLayer2 = inputData
    inputLayer3 = inputData

    hiddenLayer0 = sigmoid(np.dot(inputLayer2, weights01_a))
    hiddenLayer1 = sigmoid(np.dot(inputLayer3, weights01_b))

    outPutPerceptronLayer2 = sigmoid(np.dot(hiddenLayer0, weights02_a))
    outPutPerceptronLayer3 = sigmoid(np.dot(hiddenLayer1, weights02_b))

# The difference between the output perceptron Layer and the reference output
    outputError2 = referenceOutput0 - outPutPerceptronLayer2
    outputError3 = referenceOutput1 - outPutPerceptronLayer3

 # When a loop occurs in event or a sentinel based loop
    if(np.mean(np.abs(outputError2)) == 0.001 )and(np.mean(np.abs(outputError3)) == 0.001):
        break

# The difference from the reference output (outputError) multiplied
# by the slope of the sigmoid function at value of the output perceptron Layer
    outputDelta2 = outputError2 * sigmoidSlope(outPutPerceptronLayer2)
    outputDelta3 = outputError3 * sigmoidSlope(outPutPerceptronLayer3)

# How much of the output error can be attributed to the 
# hidden Layer values (based on the weights)?
# This line is the implementation of backpropagation
    hiddenLayerError0 = outputDelta2.dot(weights02_a.T)
    hiddenLayerError1 = outputDelta3.dot(weights02_b.T)

# The error contributed by the hidden Layer (hiddenLayerError) multiplied
# by the slope of the sigmoid function at value of the hidden Layer
    hiddenLayerDelta0 = hiddenLayerError0 * sigmoidSlope(hiddenLayer0)
    hiddenLayerDelta1 = hiddenLayerError1 * sigmoidSlope(hiddenLayer1)

    weights02_a += hiddenLayer0.T.dot(outputDelta2)
    weights01_a += inputData.T.dot(hiddenLayerDelta0)

# append which means add
    t.append(np.mean(np.abs(outputError2)))

    weights02_b += hiddenLayer1.T.dot(outputDelta3)
    weights01_b += inputData.T.dot(hiddenLayerDelta1)

# append which means add
    l.append(np.mean(np.abs(outputError3)))

#plt.plot(f)
#plt.plot(s)
plt.plot(t)
plt.plot(l)
plt.show()
