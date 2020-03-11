import numpy as np

inputData = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
referenceOutput = np.array([[0,1,1,0]]).T

# Sigmoid function coded with Numpy
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Calculate the slope by using the derivative of the sigmoid function
def sigmoidSlope(x):
    return x * (1 - x)

# Random initial weights for synapses from input to first hidden layer
weights01 = 2*np.random.random((3, 4)) - 1

# Random initial weights for synapses from first hidden layer to output layer
weights02 = 2*np.random.random((4, 1)) - 1

trainingNumber = 100
for j in range(trainingNumber):
    # Set the input data for simple forword propagation
    inputLayer = inputData
    hiddenLayer = sigmoid(np.dot(inputLayer, weights01))
    outputPerceptronLayer  = sigmoid(np.dot(hiddenLayer, weights02))

    # The difference between the output perceptron layer and the reference output
    outputError = referenceOutput - outputPerceptronLayer

    # The difference between reference (outputError) output multiplied by the slope
    # of the sigmoid function at value of the output perceptron layer
    outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)

    # How much of the output error can be attributed to the
    # hidden layer values (based on the weihts)?
    # This line is the implementation of backpropagation
    hiddenLayerError = outputDelta.dot(weights02.T)

    # The error contributed by the hidden layer (hiddenLayerError) multiplied
    # by the slope of the sigmoid function at value of the hidden layer
    hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)

    weights02 += hiddenLayer.T.dot(outputDelta)
    weights01 += inputData.T.dot(hiddenLayerDelta)

print("Output values after " + str(trainingNumber) + " training iterations:")
print(np.round(outputPerceptronLayer))
