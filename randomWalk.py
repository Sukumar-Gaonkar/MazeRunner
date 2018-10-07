
from mazerunner import GameMap, SearchAlgorithms

prob = 0.3
dimen = 40
gameMap = GameMap()
algos = SearchAlgorithms()

arenaMap = gameMap.genMapWithProb(prob, dimen)
