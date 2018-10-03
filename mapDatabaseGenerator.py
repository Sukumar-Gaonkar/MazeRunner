import time
from mazerunner import GameMap, SearchAlgorithms

noOfIterations = 10
gameMap = GameMap()
fileName = "mapDatabase_" + time.strftime("%Y%m%d-%H%M%S") + ".csv"
fileName = "results/" + fileName
f = open(fileName, "a", 1)

IDpostfix = time.strftime("%H%M%S-%d%m%Y")
f.write("mapID;Probability;MapSize;Iteration;Map\n")
counter = 0

for prob in [x/10 for x in range(1, 10)]:
    for mapSize in range(5, 51):
        for iterNo in range(1, noOfIterations + 1):
            counter += 1
            print("Probability: {0}   MapSize: {1}   Iteration: {2}".format(prob, mapSize, iterNo))
            arenaMap = gameMap.genMapWithProb(mapSize, prob)
            f.write("{0};{1};{2};{3};{4}\n".format(str(counter) + ":" + IDpostfix, prob, mapSize, iterNo, arenaMap))

print("Map Database generated : ", fileName)
