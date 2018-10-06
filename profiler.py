import time
from mazerunner import GameMap, SearchAlgorithms

##### Configurations #####
noOfIterations = 15

gameMap = GameMap()
algos = SearchAlgorithms()
fileName = "results/profilerResults_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"
f = open(fileName, "a", 1)

############## Question 1 ##############
f.write("Algorithm;Probability;MapSize;IterationNo;ShortestPath;nNodesVisited;MaxFringe;Time;Path;ArenaMap\n")

for prob in [x/10 for x in range(1, 10)]:
    for mapSize in range(20, 40):
        for iterNo in range(1, noOfIterations + 1):
            arenaMap = gameMap.genMapWithProb(mapSize, prob)
            print("Probability: {0}   Mapsize: {1}   Iteration : {2}".format(prob, mapSize, iterNo))
            print(gameMap.sketchMap(arenaMap))
            print()
            shortestPathLength, path, nodesVisited, maxFringeSize, time = algos.AStar(arenaMap, algos.euclideanDistance)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}\n".format("A*_Euclidean", prob, mapSize, iterNo,
                                                                   shortestPathLength, nodesVisited, maxFringeSize,
                                                                   str(time), path, arenaMap, nodesVisited))

            shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.AStar(arenaMap,
                                                                                       algos.manhattanDistance)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}\n".format("A*_Manhattan", prob, mapSize, iterNo,
                                                                   shortestPathLength, nodesVisited, maxFringeSize,
                                                                   str(time), path, arenaMap, nodesVisited))

            shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(arenaMap)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}\n".format("BFS", prob, mapSize, iterNo,
                                                                       shortestPathLength, nodesVisited, maxFringeSize,
                                                                       str(time), path, arenaMap, nodesVisited))

            shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.BFS(arenaMap)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}\n".format("DFS", prob, mapSize, iterNo,
                                                                       shortestPathLength, nodesVisited, maxFringeSize,
                                                                       str(time), path, arenaMap, nodesVisited))

print("Results stored in : " + fileName)
