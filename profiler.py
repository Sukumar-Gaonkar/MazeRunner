import time
from mazerunner import GameMap, SearchAlgorithms

##### Configurations #####
noOfIterations = 5

gameMap = GameMap()
algos = SearchAlgorithms()
fileName = "results/profilerResults_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"
f = open(fileName, "a", 1)

############## Question 1 ##############
f.write("Algorithm;Probability;MapSize;IterationNo;ShortestPath;nNodesVisited;MaxFringe;Time;Path\n")

shortestPathLength1=0
shortestPathLength2=0
shortestPathLength3=0
shortestPathLength4=0
shortestPathLength = 0

for mapSize in range(8000, 10000, 500):
    if(shortestPathLength == -2):
                break
    for prob in [x / 10 for x in range(1, 10)]:
        if(shortestPathLength == -2):
                break
        for iterNo in range(1, noOfIterations + 1):
            arenaMap = gameMap.genMapWithProb(mapSize, prob)
            print("Probability: {0}   Mapsize: {1}   Iteration : {2}".format(prob, mapSize, iterNo))
            print(gameMap.sketchMap(arenaMap))
            print()
            shortestPathLength, path1, nNodesVisited1, maxFringeSize1, time1 = algos.AStar(arenaMap,
                                                                                           algos.euclideanDistance)
            # if (shortestPathLength != -2):
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8}\n".format("A*_Euclidean", prob, mapSize, iterNo,
                                                               shortestPathLength, nNodesVisited1, maxFringeSize1,
                                                               str(time1), path1))


            # if(shortestPathLength2 != -2):

            shortestPathLength2, path2, nNodesVisited2, maxFringeSize2, time2 = algos.AStar(arenaMap,
                                                                           algos.manhattanDistance)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8}\n".format("A*_Manhattan", prob, mapSize, iterNo,
                                                       shortestPathLength2, nNodesVisited2, maxFringeSize2,
                                                       str(time2), path2))

            if(shortestPathLength != -2):

                        shortestPathLength, path, nNodesVisited, maxFringeSize, time = algos.DFS(arenaMap)
                        f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8}\n".format("DFS", prob, mapSize, iterNo,
                                                                       shortestPathLength, nNodesVisited, maxFringeSize,
                                                                       str(time), path))

            shortestPathLength4, path4, nNodesVisited4, maxFringeSize4, time4 = algos.BFS(arenaMap)
            f.write("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}\n".format("BFS", prob, mapSize, iterNo,
                                                                       shortestPathLength4, nNodesVisited4, maxFringeSize4,
                                                                       str(time4), path4, arenaMap))
            if(shortestPathLength4 == -2):
                break

print("Results stored in : " + fileName)


