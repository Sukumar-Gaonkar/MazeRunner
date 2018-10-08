import time as t
import heapq
import random
from mazerunner import GameMap, SearchAlgorithms
from sortedcontainers import SortedList

# generationCount = 101
populationSize = 10
bestParentsSize = 4
mutation = 0.03
prob = 0.3
dimen = 10
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

    fitness = 0
    algorithms = ["DFS", "BFS", "A*_Euc", "A*_Man"]
    fitnessParameters = ["Path", "Nodes", "Fringe"]
    fileName = "results/hardestMap_" + t.strftime("%Y%m%d-%H%M%S") + ".csv"
    f = open(fileName, "a", 1)
    for algorithm in algorithms:
        for fitnessParameter in fitnessParameters:
            hardMaps = []   # list of tuples of the format (difficulty, <arenaMap>)
            avgDifficult, nNodesVisited, maxFringeSize= 0, 0, 0
            bestPath = []

            # Initialize Population
            population = [gameMap.genMapWithProb(dimen, prob) for i in
                          range(populationSize)]  # list of all arenaMaps
            for i in range(len(population)):
                shortestPathLength = -1
                while shortestPathLength == -1:
                    population[i] = gameMap.genMapWithProb(dimen, prob)
                    if algorithm == "DFS":
                        shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(population[i])
                    elif algorithm == "BFS":
                        shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.BFS(population[i])
                    elif algorithm == "A*_Euc":
                        shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(population[i], algos.euclideanDistance)
                    elif algorithm == "A*_Man":
                        shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(population[i], algos.manhattanDistance)

                if shortestPathLength != -1:
                    if fitnessParameter == "Path":
                        avgDifficult += shortestPathLength
                        heapq.heappush(hardMaps, (-shortestPathLength, population[i]))
                    elif fitnessParameter == "Nodes":
                        avgDifficult += nNodesVisited
                        heapq.heappush(hardMaps, (-nNodesVisited, population[i]))
                    elif fitnessParameter == "Fringe":
                        avgDifficult += maxFringeSize
                        heapq.heappush(hardMaps, (-maxFringeSize, population[i]))


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

                            if algorithm == "DFS":
                                shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(population[i])
                            elif algorithm == "BFS":
                                shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.BFS(population[i])
                            elif algorithm == "A*_Euc":
                                shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(
                                    population[i], algos.euclideanDistance)
                            elif algorithm == "A*_Man":
                                shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(
                                    population[i], algos.manhattanDistance)

                            if shortestPathLength != -1:
                                if fitnessParameter == "Path":
                                    heapq.heappush(hardMaps, (-1*shortestPathLength, offspring))
                                if fitnessParameter == "Nodes":
                                    heapq.heappush(hardMaps, (-1*nNodesVisited, offspring))
                                if fitnessParameter == "Fringe":
                                    heapq.heappush(hardMaps, (-1*maxFringeSize, offspring))

                hardMaps = [heapq.heappop(hardMaps) for x in range(populationSize)]

                for x in hardMaps:
                    avgDifficult -= x[0]
                avgDifficult = avgDifficult/populationSize
                print(algorithm, ":", fitnessParameter, "Generation: ", generationNumber, "Difficulty: ", -avgDifficult)
                print([x[0] for x in hardMaps])
                generationNumber += 1

            print("Completed  {}  Gen: {}".format(algorithm, generationNumber))
            f.write("{}: {}  Dimen: {}  Prob: {}  Mutation: {}  PopulationSize: {}\n".format(algorithm, fitnessParameter, dimen, prob, mutation, populationSize))
            f.write(str(hardMaps[0][1]))
            f.write("\n")
            print()

                # print(hardMaps[0][0])