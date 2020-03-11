import random
import math
import matplotlib.pyplot as plt
import numpy as np

def errorFunction(x):
    return sum([5 * (x[i] - 20)**2 for i in range(len(x))])
    #return sum([50 * math.sin(x[i]) + x[i]**2 + 100 for i in range(len(x))]) # for Function2
    #return sum([15 * math.sin(x[i] / 5)**2 * 75 * math.cos(x[i] / 13) * 3 * math.sin(x[i] / 7) + x[i]**2 + 300 for i in range(len(x))]) # for Function3

def function1(min, max):
    x_variable = np.linspace(min, max)
    y_variable = 5 * (x_variable - 20) ** 2

    plt.plot(x_variable, y_variable)
    plt.show()

# A class of a computer agent, here also called "particle"
class individualParticle:
    def __init__(self, x0):
        self.individualPosition = []
        self.individualVelocity = []
        self.individualBestPosition = []
        self.individualBestError = -1
        self.individualError = -1

        for i in range(0, numStartingLocation):
            self.individualVelocity.append(random.uniform(-1, 1))
            self.individualPosition.append(x0[i])

    # Evaluate the current fitness of the computer agents
    def evaluate(self, costFunction):
        self.individualError = costFunction(self.individualPosition)

        # The current position of the agent is compared with the individual best and updated if necessary
        if self.individualError < self.individualBestError or self.individualBestError == -1:
            self.individualBestPosition = self.individualPosition
            self.individualBestError = self.individualError

    # Calculate the new agent's velocity
    def update_velocity(self, groupsBestPosition):
        w = 0.5     # Inertia weight of previous velocity
        c1 = 1      # Cognitive constant (distance from the the individual's known best position)
        c2 = 2       # Social constant (distance from the the group's known best position)

        # Random numbers to compensate for cognitive and social constants
        for i in range(0, numStartingLocation):
            r1 = random.random()
            r2 = random.random()
            # Updating cognitive velocity and social velocity
            cognitiveVelocity = c1 * r1 * (self.individualBestPosition[i] - self.individualPosition[i])
            socialVelocity = c2 * r2 * (groupsBestPosition[i] - self.individualPosition[i])
            self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVelocity + socialVelocity

    # Update the position fo each agent based on the new velocity updates
    def positionUpdate(self, bounds):
        for i in range(0, numStartingLocation):
            self.individualPosition[i] = self.individualPosition[i] + self.individualVelocity[i]
            # Compensate maximum position ?
            if self.individualPosition[i] > bounds[i][1]:
                self.individualPosition[i] = bounds[i][1]
            # Compensate minimum position ?
            if self.individualPosition[i] < bounds[i][0]:
                self.individualPosition[i] = bounds[i][0]

def particleSwarmOptimization(costFunction, x0, bounds, num_particles, maxiter):
    # Initialize the swarm
    global numStartingLocation
    numStartingLocation = len(x0)
    print(numStartingLocation)
    bestGroupError = -1
    groupsBestPosition = []
    swarm = []
    a = []

    for i in range(0, num_particles):
        swarm.append(individualParticle(x0))

    # Loop to start the optimization process
    for i in range(0, maxiter):
        # Evaluate each agent's fitness
        for j in range(0, num_particles):
            swarm[j].evaluate(costFunction)

            # Which agent has the best position (minimum error) in the swarm ?
            if swarm[j].individualError < bestGroupError or bestGroupError == -1:
                groupsBestPosition = list(swarm[j].individualPosition)
                bestGroupError = float(swarm[j].individualError)

        # Update velocities and positions inside the swarm
        for j in range(0, num_particles):
            swarm[j].update_velocity(groupsBestPosition)
            swarm[j].positionUpdate(bounds)

        a.append(groupsBestPosition)

    # Print the final results with error
    print('After running the swarm of computer agents, the group\'s best porision is ' +
       str(groupsBestPosition) + " with an error of " + str(bestGroupError))

    #plt.plot(a)
    #plt.show()
    function1(groupsBestPosition[0], groupsBestPosition[1])

initialStartingPosition = [-15, 15]
minMaxBounds = [(-100, 100), (-100, 100)]
particleSwarmOptimization(errorFunction, initialStartingPosition, minMaxBounds,
                          num_particles = 150, maxiter = 30)