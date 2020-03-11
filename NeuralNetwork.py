import numpy as np

inputData = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
referenceOutput = np.array([[0,0,1,1]]).T

# Sigmoid function coded with Numpy
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    #return 1 / (1 + np.exp(-(0.5 * x)))

# Calculate the slope by using the derivative of the sigmoid function
def sigmoidSlope(x):
    return x * (1 - x)
    #return x * (x > 0)
    #return 1 - sigmoid(x) * sigmoid(x) # 勾配下降法

# Weights of the synopses connecting input and output layer are randomly
# initialized with mean 0
weights01 = 2*np.random.random((3,1)) - 1

trainingNumber = 10
for i in range(trainingNumber):
    # Set the input data for simple forword propagation
    inputLayer = inputData

    # Apply Sigmoid Function to the dot product of two arrays
    outputPerceptronLayer = sigmoid(np.dot(inputLayer, weights01))

    # The difference between the output perceptron layer and the reference output
    outputError = referenceOutput - outputPerceptronLayer

    # The difference between reference (outputError) output multiplied by the slope
    # of the sigmoid function at value of the output perceptron layer
    outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)

    # Updating the weights
    weights01 += np.dot(inputLayer.T, outputDelta)

print("Output values after " + str(trainingNumber) + " training iterations:")
print(outputPerceptronLayer)