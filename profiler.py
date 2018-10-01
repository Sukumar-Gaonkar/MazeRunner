import time
from mazerunner import GameMap, SearchAlgorithms

##### Configurations #####
noOfIterations = 15

gameMap = GameMap()
algos = SearchAlgorithms()
fileName = "results/profilerResults_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"
f = open(fileName, "a", 1)

############## Question 1 ##############
f.write("Probability,MapSize,IterationNo,ShortestPath,NodesVisited,MaxFringe,Time\n")


for prob in [x/10 for x in range(1, 10)]:
    for mapSize in range(5, 10):
        for iterNo in range(1, noOfIterations + 1):
            arenaMap = gameMap.genMapWithProb(mapSize, prob)
            print("Probability: {0}   Mapsize: {1}   Iteration : {2}".format(prob, mapSize, iterNo))
            print(gameMap.sketchMap(arenaMap))
            print()
            shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(arenaMap, algos.euclideanDistance)
            # f.write("Prob: {0}  Mapsize: {1}  Iter No : {2}\n".format(prob, mapSize, iterNo))
            # f.write("ShortestPath: {0} NodesVisited: {1}  MaxFringe: {2}  Time: {3}s\n\n".format(shortestPathLength, nNodesVisited, maxFringeSize, time))
            f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(prob,mapSize,iterNo,shortestPathLength,nNodesVisited, maxFringeSize,str(time)))

print("Results stored in : " + fileName)