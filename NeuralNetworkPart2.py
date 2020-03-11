import numpy as np
import random
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    # To reduce the trainingNumber, we can change the above function like following
    # 1 / (1 + np.exp(2 * -x))

def sigmoidSlope(x):
    return x * (1 - x)

trainingNumber = 900

#This is the inputData and the reference of output
inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

#solvable by both networks
referenceOutput1 = np.array([[0], [0], [1], [1]])

#solvable by only malti layer one
referenceOutput2 = np.array([[0], [1], [1], [0]])


random.seed(1)
weight01_1 = 2 * np.random.random((3, 1)) - 1
weight01_2 = 2 * np.random.random((3, 1)) - 1

random.seed(42)
weight01_a = 2 * np.random.random((3, 4)) - 1
weight02_a = 2 * np.random.random((4, 1)) - 1

weight01_b = 2 * np.random.random((3, 4)) - 1
weight02_b = 2 * np.random.random((4, 1)) - 1

a = []
b = []
c = []
d = []

for i in range(trainingNumber):

    inputLayer1 = inputData
    inputLayer2 = inputData

    outPutPerceptronLayer1 = sigmoid(np.dot(inputLayer1, weight01_1))
    outPutPerceptronLayer2 = sigmoid(np.dot(inputLayer2, weight01_2))

    outputError1 = referenceOutput1 - outPutPerceptronLayer1
    outputError2 = referenceOutput2 - outPutPerceptronLayer2

    outputDelta1 = outputError1 * sigmoidSlope(outPutPerceptronLayer1)
    outputDelta2 = outputError2 * sigmoidSlope(outPutPerceptronLayer2)

    weight01_1 += np.dot(inputLayer1.T, outputDelta1)
    weight01_2 += np.dot(inputLayer2.T, outputDelta2)

    a.append(np.mean(np.abs(outputError1)))
    b.append(np.mean(np.abs(outputError2)))


for i in range(trainingNumber):

    inputLayer3 = inputData
    inputLayer4 = inputData

    hiddenLayer1 = sigmoid(np.dot(inputLayer3, weight01_a))
    hiddenLayer2 = sigmoid(np.dot(inputLayer4, weight01_b))

    outPutPerceptronLayer3 = sigmoid(np.dot(hiddenLayer1, weight02_a))
    outPutPerceptronLayer4 = sigmoid(np.dot(hiddenLayer2, weight02_b))

    outputError3 = referenceOutput1 - outPutPerceptronLayer3
    outputError4 = referenceOutput2 - outPutPerceptronLayer4

        #This is for the sentinel based or event based loop
    if(np.mean(np.abs(outputError3)) == 0.001 ) and (np.mean(np.abs(outputError4)) == 0.001):
        break

    outputDelta3 = outputError3 * sigmoidSlope(outPutPerceptronLayer3)
    outputDelta4 = outputError4 * sigmoidSlope(outPutPerceptronLayer4)

    hiddenLayerError1 = outputDelta3.dot(weight02_a.T)
    hiddenLayerError2 = outputDelta4.dot(weight02_b.T)

    hiddenLayerDelta1 = hiddenLayerError1 * sigmoidSlope(hiddenLayer1)
    hiddenLayerDelta2 = hiddenLayerError2 * sigmoidSlope(hiddenLayer2)

    weight02_a += hiddenLayer1.T.dot(outputDelta3)
    weight01_a += inputData.T.dot(hiddenLayerDelta1)

    weight02_b += hiddenLayer2.T.dot(outputDelta4)
    weight01_b += inputData.T.dot(hiddenLayerDelta2)

    c.append(np.mean(np.abs(outputError3)))
    d.append(np.mean(np.abs(outputError4)))

plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.plot(d)

plt.show()
