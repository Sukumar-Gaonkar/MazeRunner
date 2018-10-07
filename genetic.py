import time as t
import heapq
import random
from mazerunner import GameMap, SearchAlgorithms
from sortedcontainers import SortedList

generationCount = 101
populationSize = 10
bestParentsSize = 4
mutation = 0.03
prob = 0.3
dimen = 100
gameMap = GameMap()
algos = SearchAlgorithms()


def genOffsprings(parent1, parent2, mutation):
    dimen = len(parent1)
    # offspring = [[(parent1[j][i] if i < dimen/2 else parent2[j][i]) for i in range(dimen)] for j in range(dimen)]
    offsprings = []
    offsprings.append([[(parent1[j][i] if i < dimen / 2 else parent2[j][i]) for i in range(dimen)] for j in range(dimen)] )                       # Left = Parent1_Left, Right = Parent2_Right
    offsprings.append([[(parent1[j][i] if i < dimen / 2 else parent2[j][i - int(dimen/2)]) for i in range(dimen)] for j in range(dimen)])     # Left = Parent1_Left, Right = Parent2_Left
    offsprings.append([[(parent1[j][int(dimen/2) + i] if i < dimen / 2 else parent2[j][i]) for i in range(dimen)] for j in range(dimen)])             # Left = Parent1_Right, Right = Parent2_Right
    offsprings.append([[(parent1[j][int(dimen/2) + i] if i < dimen / 2 else parent2[j][i - int(dimen/2)]) for i in range(dimen)] for j in range(dimen)])    # Left = Parent1_Right, Right = Parent2_Left


    # Mutation
    mutationCount = int(dimen**2 * mutation)
    for offspring in offsprings:

        for i in range(mutationCount):
            x = random.randint(0, dimen - 1)
            y = random.randint(0, dimen - 1)
            offspring[x][y] = 1 - offspring[x][y]   # Flipping '1' to '0' and '0' to '1'
            offspring[0][0] = 0
            offspring[dimen - 1][dimen - 1] = 0

    # print("Sketching")
    # print(gameMap.sketchMap(parent1))
    # print(gameMap.sketchMap(parent2))
    # print(gameMap.sketchMap(offspring))
    # print()

    return offsprings


if __name__ == "__main__":

    hardMaps = []   # list of tuples of the format (difficulty, <arenaMap>)
    avgDifficult = 0
    bestPath = []

    # Initialize Population
    population = [gameMap.genMapWithProb(dimen, prob) for i in
                  range(populationSize)]  # list of all arenaMaps
    for i in range(len(population)):
        shortestPathLength = -1
        while shortestPathLength == -1:
            population[i] = gameMap.genMapWithProb(dimen, prob)
            shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(population[i])
        avgDifficult += shortestPathLength
        heapq.heappush(hardMaps, (-shortestPathLength, population[i]))

    avgDifficult /= populationSize
    prevAvgDifficulty = 0
    # print([x[0] for x in hardMaps])
    generationNumber = 0
    while generationNumber % 10 != 0 or avgDifficult > prevAvgDifficulty:

        shortestPathLength, offspring = 0, 0
        if generationNumber % 10 == 0:
            prevAvgDifficulty = avgDifficult
        avgDifficult = 0
        for k in range(bestParentsSize):
            for l in range(k + 1, bestParentsSize):
                offsprings = genOffsprings(population[k], population[l], mutation)
                for offspring in offsprings:
                    shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(offspring)
                    if shortestPathLength != -1:
                        heapq.heappush(hardMaps, (-1*shortestPathLength, offspring))

        hardMaps = [heapq.heappop(hardMaps) for x in range(populationSize)]

        for x in hardMaps:
            avgDifficult -= x[0]
        avgDifficult = avgDifficult/populationSize
        print("Generation: ", generationNumber, "Difficulty: ", -avgDifficult)
        print([x[0] for x in hardMaps])
        generationNumber += 1

    fileName = "results/hardestMap_" + t.strftime("%Y%m%d-%H%M%S") + ".csv"
    f = open(fileName, "a", 1)
    f.write("DFS  Dimen: {}  Prob: {}  Mutation: {}  PopulationSize: {}\n".format(dimen, prob, mutation, populationSize))
    f.write(str(hardMaps[0][1]))

        # print(hardMaps[0][0])