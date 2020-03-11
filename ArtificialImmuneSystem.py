import random
import string
import numpy as np

# Reading files to populate list of diseases and list of past antibodies
# List of diseases
with open("AISdiseases.txt","r") as loadDiseases:
    listOfDiseases = loadDiseases.read().split(",")

# List of past antibodies
with open("AISmemoryCell.txt","r") as loadMemoryCell:
    memoryCell = loadMemoryCell.read().split(",")

# Set global variables
antigen = random.choice(listOfDiseases)
antigenLength = len(antigen)
antibodyNumber = 200
generations = 20
mutationChance = 2
memoryCellFraction = 10

# Generates a random gene out of all printable ASCII characters
def randomGene():
    return random.choice(string.printable)

# Creates antibodyNumber number of antibodies with random genes
def initialAntibodyPopulation():
    initPop = []
    for i in range(antibodyNumber):
        initPop.append(''.join(random.choice(string.printable) for i in range(antigenLength)))
    return initPop

# The affinity value, how well an antibody fits the antigen (here again as penalty)
def affinityPenaltyMetric(antibodyAttack):
    # use your code from the fitness function of the GA
    fitness = 0

    for e in range(antigenLength):
        fitness += (ord(antigen[e])-ord(antibodyAttack[e]))**2

#    for e in range(antigenLength):
#        fitness += abs(ord(antigen[e])-ord(antibodyAttack[e]))

#    fitness += antigenLength

#    for e in range(antigenLength):
#        if ord(antigen[e]) != ord(antibodyAttack[e]):
#            fitness += 1

    return fitness

# Randomly selects an antibody, weighted by their respective probability
# (higher affinity == higher probability of selection)
def weightedAntibodyChoice(listOfAntibodyAffinity):
    probs = [listOfAntibodyAffinity[i][1] for i in range(len(listOfAntibodyAffinity))]
    probs = np.array(probs)
    probs /= probs.sum()
    return listOfAntibodyAffinity[np.random.choice(len(listOfAntibodyAffinity),1,p = probs)[0]][0]

# Mutation of single antibody in 1/mutationRatio chance
def mutation(antibodyMutate, mutationRatio):
    mutatedDNA = ""
    for gene in range(antigenLength):
        mutationCheck = random.randint(0,mutationRatio)
        if mutationCheck == 1:
            mutatedDNA += randomGene()
        else:
            mutatedDNA += antibodyMutate[gene]
    return mutatedDNA


currentAntibodyPopulation = initialAntibodyPopulation()

for ik in memoryCell:
    if len(ik) == len(currentAntibodyPopulation[memoryCell.index(ik)]):
        currentAntibodyPopulation[memoryCell.index(ik)] = ik

for i in range(generations):
    lastAffinityArray = []
    for k in currentAntibodyPopulation:
        lastAffinityArray.append(affinityPenaltyMetric(k))

    # Print the antibody mutation closest to an antigen
    print("The antibody closest to the antigen at interation",i, "is ---",
       currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))],
       "--- with penalty:", min(lastAffinityArray))

    # Returns a antibody list with their respective affinity in format
    # [["antibody1", affinity1], ["antibody2", affinity2] [...] ... ]
    populationWeighted = []
    for individual in currentAntibodyPopulation:
        individualPenalty = affinityPenaltyMetric(individual)
        if individualPenalty == 0:
            antibodyFitnessPair = (individual, 1.0)
        else:
            antibodyFitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(antibodyFitnessPair)

    # New set, repopulated with newly selected and mutated antibodies
    currentAntibodyPopulation = []
    for m in range (int(antibodyNumber/2)):
        # Random selection, weighted by affinity (higher affinity == higher probability)
        bestAntibody1 = weightedAntibodyChoice(populationWeighted)
        bestAntibody2 = weightedAntibodyChoice(populationWeighted)

        # Mutation in 1/mutationChance chances
        bestAntibody1 = mutation(bestAntibody1, mutationChance)
        bestAntibody2 = mutation(bestAntibody2, mutationChance)

        # Combining the list of antibodies for next iteration
        currentAntibodyPopulation.append(bestAntibody1)
        currentAntibodyPopulation.append(bestAntibody2)

lastAffinityArray = []
for g in currentAntibodyPopulation:
    lastAffinityArray.append(affinityPenaltyMetric(g))

with open("AISmemoryCell.txt","r") as loadMemoryCell:
    newMemoryCell = loadMemoryCell.read()

if min(lastAffinityArray) < 50:
    putIntoMemory = currentAntibodyPopulation[lastAffinityArray.index(min(lastAffinityArray))]
    # Prints fittest antibody out of the resulting list
    print("Fittest String at", generations, "is:", putIntoMemory)
    newMemoryCell += "," + putIntoMemory
    with open("AISmemoryCell.txt", "w") as writeMemoryCell:
        writeMemoryCell.write(newMemoryCell)
else:
    putIntoMemory = ""
    print("No antibody to put into memory")

del memoryCell
del listOfDiseases
