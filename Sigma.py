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
  
    for e in range(dnaLength):
        fitness =(ord(target[e])-ord(competingDNA[e]))**2
        fitness += fitness

    for e in range(dnaLength):
        fitness = abs(ord(target[e])-ord(competingDNA[e]))
        fitness += fitness

    fitness += dnaLength

    return fitness



def mutation(competingDNA, mutationRatio):
    mutatedDNA = ""
    # I put a that choose from character in a and choose one word random from sentence in b and input 1/100 in c.
    a = randomGene()
    b = random.randint(0,len(competingDNA)-1)
    c = random.randint(1,mutationRatio)
    #When it was 1 then it will be mutated gene.
    if c == 1:
        mutatedDNA = competingDNA[:b] + a + competingDNA[b+1:]
        return mutatedDNA
    else:
        return competingDNA

def recombination(competingDNA1, competingDNA2):
    # Choose one word random from sentence.
    a = random.randint(0,len(competingDNA1)-1)
    #This sentence is that first place competingDNA1 and second is competingDNA2.
    DNAout1 = competingDNA1[:a] + competingDNA2[a:]
     #This sentence is that first place competingDNA2 and second is competingDNA1.
    DNAout2 = competingDNA2[:a] + competingDNA1[a:]
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

    # Prints the generation number and its current fittest DNA string
    print("The fittest DNA for generation", i, "is ---", currentPopulation[
            lastfitnessarray.index(min(lastfitnessarray))],
            "--- with penalty:", min(lastfitnessarray))
    # Returns a new population with their respective fitness in format
    # [ ["dnastr1:", penalty1], ["dnastr2", penalty2] [...] ... ]
    populationWeighted = []
    for individual in currentPopulation:
        individualPenalty = fitnessFunction(individual)
        if individualPenalty == 0:
            DNAfitnessPair = (individual, 1.0)
        else:
            DNAfitnessPair = (individual, 1.0/individualPenalty)
        populationWeighted.append(DNAfitnessPair)

    # Reset population and repopulate with newly selected, recombined, and mutated DNA
    currentPopulation = []
    for m in range(int(populationSize/2)):
        # Random selection, weighted by fitness (higher fitness == higher probobility)
        fittestDNA1 = weightedDNAchoice(populationWeighted)
        fittestDNA2 = weightedDNAchoice(populationWeighted)
        # Recombination or crossover
        fittestDNA1, fittestDNA2 = recombination(fittestDNA1, fittestDNA2)
        # Mutarion in 1/mutationChance chances
        fittestDNA1 = mutation(fittestDNA1, mutationChance)
        fittestDNA2 = mutation(fittestDNA2, mutationChance)
        # Combining the population for next iteration
        currentPopulation.append(fittestDNA1)
        currentPopulation.append(fittestDNA2)
# Creates on array of penalty value for each DNA in population
lastfitnessarray = []
for g in currentPopulation:
    lastfitnessarray.append(fitnessFunction(g))
# Prints fittest DNA out of the resulting population
print("Fittest String at", generations, "is:",
        currentPopulation[lastfitnessarray.index(min(lastfitnessarray))])