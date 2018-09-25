import random
import math
import heapq
import time


class SearchAlgorithms:
    def DFS(self, arenaMap):
        # TODO: Implement Depth First Search
        """
            Parameters:
                arenaMap (List[List[int]]): map of arena ; 0=PathExists, 1=PathBlocked
            Returns:
            [
                int : shortest path length ; -1 if path not found,
                List[int] : shortest path ; 1=Up,2=Right,3=Down,4=Left,
                int : Number of Nodes visited,
                int : Max fringe size
                double: Time taken
            ]
            If a path is not found, then it returns : [-1, [-1], NodesVisited, MaxFringe]

        """
        pass

    def BFS(self, arenaMap):
        # TODO: Implement Breadth First Search
        """
            Parameters:
                arenaMap (List[List[int]]): map of arena ; 1=PathExists, 0=PathBlocked
            Returns:
            [
                int : shortest path length ; -1 if path not found,
                List[int] : shortest path ; 1=Up,2=Right,3=Down,4=Left,
                int : Number of Nodes visited,
                int : Max fringe size
                double: Time taken
            ]
            If a path is not found, then it returns : [-1, [-1], NodesVisited, MaxFringe]

        """
        pass

    def AStar(self, arenaMap, heuristicFun):
        """
            Parameters:
                arenaMap (List[List[int]]): map of arena ; 1=PathExists, 0=PathBlocked,
                heuristicFun (Function): A function that takes current state as parameter and returns an int representing the requird heuristic
            Returns:
            [
                int : shortest path length ; -1 if path not found,
                List[int] : shortest path ; 1=Up,2=Right,3=Down,4=Left,
                int : Number of Nodes visited,
                int : Max fringe size
                double: Time taken
            ]
            If a path is not found, then it returns : [-1, [-1], NodesVisited, MaxFringe]

        """

        startTime = time.time()
        startNode = [0, 0]
        nVisitedNode, maxFringe, pathLength = 0, 0, 0
        path = []

        # Each node in the PriorityQueue is a tuple of the format (priority, [row,column], [<path from source>])
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, startNode, []))

        while len(priorityQueue) > 0:
            currNode = heapq.heappop(priorityQueue)
            # print(currNode[1])
            if currNode[1][0] == len(arenaMap) - 1 and currNode[1][1] == len(arenaMap) - 1:
                return [len(currNode[2]), currNode[2], nVisitedNode, maxFringe, time.time() - startTime]
            else:
                nVisitedNode += 1

                # Move to the right if possible
                if currNode[1][1] < len(arenaMap) - 1 and arenaMap[currNode[1][0]][currNode[1][1] + 1] == 0:
                    heapq.heappush(priorityQueue,
                                   (currNode[0] + 1, [currNode[1][0], currNode[1][1] + 1], currNode[2] + [2]))    # 2=right

                # Move to down if possible
                if currNode[1][0] < len(arenaMap) - 1 and arenaMap[currNode[1][0] + 1][currNode[1][1]] == 0:
                    heapq.heappush(priorityQueue,
                                   (currNode[0] + 1, [currNode[1][0] + 1, currNode[1][1]], currNode[2] + [3]))   # 3=down

                # Move to the left if possible
                if currNode[1][1] > 0 and arenaMap[currNode[1][0]][currNode[1][1] - 1] == 0:
                    heapq.heappush(priorityQueue,
                                   (currNode[0] + 1, [currNode[1][0], currNode[1][1] - 1], currNode[2] + [4]))   # 4=left

                # Move to up if possible
                if currNode[1][0] > 0 and arenaMap[currNode[1][0] - 1][currNode[1][1]] == 0:
                    heapq.heappush(priorityQueue,
                                   (currNode[0] + 1, [currNode[1][0] - 1, currNode[1][1]], currNode[2] + [1]))   # 1=up

                maxFringe = max(maxFringe, len(priorityQueue))

        # The code will complete the while loop only if no path to the destination exists
        # The '-1' in the returned values indicate no path was found
        return [-1, [-1], nVisitedNode, maxFringe, time.time() - startTime]

    def euclideanDistance(self, src, dest):
        """
            Parameters:
                src ([r,c]) : [r,c] indicate the location of the first element
                dest ([r,c]) : [r,c] indicate the location of the second element

            Returns:
                int : Euclidean Distance between 'sc' and 'dset'
        """

        return math.sqrt((src[0]-dest[0])**2 + (src[1]-dest[1])**2)

    def manhattanDistance(self, src, dest):
        """
            Parameters:
                src ([r,c]) : [r,c] indicate the location of the first element
                dest ([r,c]) : [r,c] indicate the location of the second element

            Returns:
                int : Manhattan Distance between 'sc' and 'dset'
        """
        return abs(src[0] - dest[0]) + abs(src[1] - dest[1])


class GameMap:

    def genMapWithProb(self, dimen, prob=0.2):
        map = [[1 if random.random() < prob else 0 for j in range(dimen)] for i in range(dimen)]
        map[0][0] = 0
        map[dimen-1][dimen-1] = 0
        return map

    def genMapForDFS(self, maximizingFactor):
        """
            Parameters:
                maximizingFactor (String) : 'PathLength' or 'NodesVisited' or 'FringeSize'
            Returns:
                List[List[int]] : generated GameMap
        """
        pass

    def genMapForDFS(self, maximizingFactor):
        pass

    def genMapForDFS(self, maximizingFactor):
        pass

    def drawMap(self, arenaMap):
        print("#" * (len(arenaMap) + 2))
        for row in arenaMap:
            print("#", end="")
            for cell in row:
                print(cell, end="")
            print("#")

        print("#" * (len(arenaMap) + 2))


arenaMap = GameMap().genMapWithProb(4, 0.3)
GameMap().drawMap(arenaMap)

print("Numbers in 'Path' indicate directions travelled\n1=Up,2=Right,3=Down,4=Left\n")

print("A* - Euclidean Distance")
print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().AStar(arenaMap, SearchAlgorithms.euclideanDistance)))
print("\nA* - Manhattan Distance")
print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().AStar(arenaMap, SearchAlgorithms.manhattanDistance)))
