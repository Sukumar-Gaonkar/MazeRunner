import heapq
import random
from mazerunner import GameMap, SearchAlgorithms
from sortedcontainers import SortedList

populationSize = 10
mutation = 0.03
prob = 0.3
dimen = 100
gameMap = GameMap()
algos = SearchAlgorithms()


def genOffsprings(parent1, parent2, mutation):
    dimen = len(parent1)
    offspring = [[(parent1[j][i] if i < dimen/2 else parent2[j][i]) for i in range(dimen)] for j in range(dimen)]

    # Mutation
    for i in range(int(dimen**2 * mutation)):
        x = random.randint(0, dimen - 1)
        y = random.randint(0, dimen - 1)
        offspring[x][y] = 1 - offspring[x][y]   # Flipping '1' to '0' and '0' to '1'
    return offspring


if __name__ == "__main__":

    hardMaps = []   # list of tuples of the format (difficulty, <arenaMap>)
    avgDifficult = 0

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
    prevAvgDifficulty = avgDifficult + 1
    print([x[0] for x in hardMaps])

    while (avgDifficult - prevAvgDifficulty) < 0:
        shortestPathLength, offspring = 0, 0
        prevAvgDifficulty = avgDifficult
        avgDifficult = 0
        print([x[0] for x in hardMaps])
        for i in range(populationSize):
            for j in range(i + 1, populationSize):
                offspring = genOffsprings(population[i], population[j], mutation)

                shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(population[i])
                if shortestPathLength != -1:
                    heapq.heappush(hardMaps, (-1*shortestPathLength, offspring))
        hardMaps = [heapq.heappop(hardMaps) for x in range(populationSize)]

        for x in hardMaps:
            avgDifficult += x[0]
        avgDifficult = avgDifficult/populationSize
        print(avgDifficult)


        # print(hardMaps[0][0])