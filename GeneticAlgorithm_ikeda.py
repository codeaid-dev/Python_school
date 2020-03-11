import random
import string
import numpy as np

target = "Your Name"
dnaLength = len(target)
populationSize = 20
generations = 5000
mutationChance = 100

def randomGene():
    return random.choice(string.printable)

def initialPopulation():
    initPop = []
    for i in range(populationSize):
        initPop.append(''.join(random.choice(string.printable) for i in range(dnaLength)))
    return initPop

def fitnessFunction(competingDNA):
    fitness = 0
    return fitness

#mutation totsuzennhenni
def mutation(competingDNA, mutationRatio):
    mutatedDNA = ""

    z = random.choice(string.printable)
    b = random.randint(0,dnaLength-1)
    c = random.randint(1,mutationRatio)

    if c == 1:
      competingDNA.replace(competingDNA[c], z)
    return mutatedDNA

def recombination(competingDNA1, competingDNA2):

    a = random.randint(0,dnaLength-1)
    DNAout1 = competingDNA1[0:a] + competingDNA2[a:9]
    DNAout2 = competingDNA2[0:a] + competingDNA1[a:9]

    return (DNAout1, DNAout2)

def weightedDNAchoice(competingDNAfitnessPairs):
    probs = [competingDNAfitnessPairs[i][1] for i in range(len(competingDNAfitnessPairs))]
    probs = np.array(probs)
    probs /= probs.sum()
    return competingDNAfitnessPairs[np.random.choice(len(competingDNAfitnessPairs), 1, p = probs)[0]][0]

currentPopulation = initialPopulation()
for i in range(generations):
    lastfitnessarray = []
    for k in currentPopulation:
        lastfitnessarray.append(fitnessFunction(k))

    print("The fittest DNA for generation", i, "is ---", currentPopulation[
            lastfitnessarray.index(min(lastfitnessarray))],
            "--- with penalty:", min(lastfitnessarray))