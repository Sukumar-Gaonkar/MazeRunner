
import mazee
import random
import math
import heapq
import time
from queue import Queue
import numpy as np

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
        startTime = time.time()
        startNode = [0, 0]
        end = [len(arenaMap) - 1, len(arenaMap) - 1]
        nVisitedNode, maxFringe, pathLength = 0, 0, 0
        visited = []
        path = []
        nodes_visited = 0
        maxFringe = 0
        shortestpathlength = -1
        # pathmap = list(map(list, arenaMap))
        pathmap = np.zeros((len(arenaMap), len(arenaMap)))
        visited = np.zeros((len(arenaMap), len(arenaMap)))
        arenaMap[len(arenaMap) - 1][len(arenaMap) - 1] = 0
        #  pathmap.fill(0)
        stack = [startNode]
        row = 0
        col = 0
        visited[0][0] = 1
        stack.append([row, col])
        while stack:
            x = stack.pop()
            # row, col = q.get()
            row = x[0]
            col = x[1]
            if row == len(arenaMap) - 1 and col == len(arenaMap) - 1:
                break
            if col + 1 < len(arenaMap) and arenaMap[row][col + 1] == 0 and visited[row][col + 1] == 0:
                stack.append([row, col + 1])
                visited[row][col + 1] = 1
                nVisitedNode = nVisitedNode + 1
                pathmap[row][col + 1] = 2
                maxFringe = max(maxFringe, len(stack))
                # print(maxFringe)
                # print(nVisitedNode)
                if row == len(arenaMap) - 1 and col + 1 == len(arenaMap) - 1:
                    break
                # print(1)
            if row + 1 < len(arenaMap) and arenaMap[row + 1][col] == 0 and visited[row + 1][col] == 0:
                stack.append([row + 1, col])
                visited[row + 1][col] = 1
                nVisitedNode = nVisitedNode + 1
                pathmap[row + 1][col] = 3
                maxFringe = max(maxFringe, len(stack))
                # print(maxFringe)
                #  print(nVisitedNode)
                if row + 1 == len(arenaMap) - 1 and col == len(arenaMap) - 1:
                    break
            #  print(1)
            if 0 <= col - 1 and arenaMap[row][col - 1] == 0 and visited[row][col - 1] == 0:
                stack.append([row, col - 1])
                visited[row][col - 1] = 1
                pathmap[row][col - 1] = 4
                nVisitedNode = nVisitedNode + 1
                maxFringe = max(maxFringe, len(stack))
                #  print(maxFringe)
                #  print(nVisitedNode)
                if row == len(arenaMap) - 1 and col - 1 == len(arenaMap) - 1:
                    break
            #  print(1)
            if 0 <= row - 1 and arenaMap[row - 1][col] == 0 and visited[row - 1][col] == 0:
                stack.append([row - 1, col])
                visited[row - 1][col] = 1
                pathmap[row - 1][col] = 1
                nVisitedNode = nVisitedNode + 1
                maxFringe = max(maxFringe, len(stack))
                #   print(maxFringe)
                #   print(nVisitedNode)
                if row - 1 == len(arenaMap) - 1 and col == len(arenaMap) - 1:
                    break
            #    print(1)

        row, col = len(arenaMap) - 1, len(arenaMap) - 1
        var = np.int(pathmap[row][col])
        if var == 0:
            return [-1, [-1], nodes_visited, maxFringe, time.time() - startTime]
        else:
            step = {3: (-1, 0), 1: (1, 0), 4: (0, 1), 2: (0, -1)}
            while True:
                if row == 0 and col == 0:
                    break
                #   print((row, col), 'go', var)
                path.append(np.int(var))

                shortestpathlength = shortestpathlength + 1
                r, c = step[var]
                row += r
                col += c
                var = pathmap[row][col]
            # print(shortestpathlength,nVisitedNode,time.time() - startTime)
            # print(path[::-1])
            return [shortestpathlength, path[::-1], nVisitedNode, maxFringe, time.time() - startTime]




    def BFS(self, arenaMap):
        # TODO: Implement Breadth First Search
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
        startTime = time.time()
        startNode = [0, 0]
        end=[len(arenaMap)-1,len(arenaMap)-1]
        nVisitedNode, maxFringe, pathLength = 0, 0, 0
        visited = []
        path=[]
        nodes_visited=0
        maxFringe=0
        shortestpathlength=-1
        #pathmap = list(map(list, arenaMap))
        pathmap = np.zeros((len(arenaMap),len(arenaMap)))
        visited=np.zeros((len(arenaMap),len(arenaMap)))
        arenaMap[len(arenaMap)-1][len(arenaMap)-1]=0
      #  pathmap.fill(0)
        q=Queue()
        row=0
        col=0
        visited[0][0]=1
        q.put((row,col))
        while not q.empty():
            row, col = q.get()
            if row==len(arenaMap)-1 and col==len(arenaMap)-1:
                break
            if col+1 < len(arenaMap) and arenaMap[row][col+1] == 0 and visited[row][col+1] ==0 :
                q.put((row, col+1))
                visited[row][col+1]=1
                nVisitedNode=nVisitedNode+1
                pathmap[row][col+1] = 2
                maxFringe = max(maxFringe, q.qsize())
               # print(maxFringe)
               # print(nVisitedNode)
                if row==len(arenaMap)-1 and col+1 ==len(arenaMap)-1:
                    break
                #print(1)
            if row+1 < len(arenaMap) and arenaMap[row+1][col] == 0 and visited[row+1][col] ==0:
                q.put((row+1, col))
                visited[row+1][col]=1
                nVisitedNode=nVisitedNode+1
                pathmap[row+1][col] = 3
                maxFringe = max(maxFringe, q.qsize())
               # print(maxFringe)
              #  print(nVisitedNode)
                if row+1==len(arenaMap)-1 and col ==len(arenaMap)-1:
                    break
              #  print(1)
            if 0 <= col-1 and arenaMap[row][col-1] == 0 and visited[row][col-1] ==0:
                q.put((row, col-1))
                visited[row][col-1]=1
                pathmap[row][col-1] = 4
                nVisitedNode=nVisitedNode+1
                maxFringe = max(maxFringe, q.qsize())
              #  print(maxFringe)
              #  print(nVisitedNode)
                if row==len(arenaMap)-1 and col-1 ==len(arenaMap)-1:
                    break
              #  print(1)
            if 0 <= row-1 and arenaMap[row-1][col] == 0 and visited[row-1][col] ==0:
                q.put((row-1, col))
                visited[row-1][col]=1
                pathmap[row-1][col] = 1
                nVisitedNode=nVisitedNode+1
                maxFringe = max(maxFringe, q.qsize())
             #   print(maxFringe)
             #   print(nVisitedNode)
                if row-1==len(arenaMap)-1 and col ==len(arenaMap)-1:
                    break
            #    print(1)


        row,col=len(arenaMap)-1,len(arenaMap)-1
        var=np.int(pathmap[row][col])
        if var==0:
            return[-1, [-1], nodes_visited, maxFringe, time.time() - startTime]
        else:
            step = {3: (-1, 0), 1: (1, 0), 4: (0, 1), 2: (0, -1)}
            while True:
                if row==0 and col==0:
                    break
             #   print((row, col), 'go', var)
                path.append(np.int(var))

                shortestpathlength=shortestpathlength+1
                r, c = step[var]
                row += r
                col += c
                var = pathmap[row][col]
            #print(shortestpathlength,nVisitedNode,time.time() - startTime)
            #print(path[::-1])
            return  [shortestpathlength,path[::-1],nVisitedNode,maxFringe,time.time() - startTime]

    def AStar(self, arenaMap, heuristicFun):
        """
            Parameters:
                arenaMap (List[List[int]]): map of arena ; 1=PathExists, 0=PathBlocked,
                heuristicFun (Function): A function that takes current state as parameter and returns an int representing the requird heuristic
            Returns:
            [
                int : shortest path length ; -1 if path not found,
                List[int] : shortest path ; 1=Up,2=Right,3=Down,4=Left,
                List[List[int]] : Nodes visited,
                int : Max fringe size
                double: Time taken
            ]
            If a path is not found, then it returns : [-1, [-1], NodesVisited, MaxFringe]

        """

        startTime = time.time()
        # visitedNodes = set()
        visitedNodes = dict()
        maxFringe, pathLength = 0, 0
        path = []

        # Each node in the PriorityQueue is a tuple of the format (priority, [row,column], [<path from source>])
        priorityQueue = []
        startNode = [0,0]
        endNode = [len(arenaMap)-1,len(arenaMap)-1]
        heapq.heappush(priorityQueue, (0, startNode, []))

        while len(priorityQueue) > 0:
            currNode = heapq.heappop(priorityQueue)
            visitedNodes[tuple(currNode[1])] = currNode[0]
            if currNode[1][0] == len(arenaMap) - 1 and currNode[1][1] == len(arenaMap) - 1:
                return [len(currNode[2]), currNode[2], len(visitedNodes), maxFringe, time.time() - startTime]
            else:

                possibleMoves = [[-1, 0], [0, 1], [1, 0], [0, -1]]      # possibleMoves = [<move up>,<move right>,<move down>,<move left>]

                for moveCode, move in enumerate(possibleMoves,1):
                    potentialNode = [currNode[1][0] + move[0], currNode[1][1] + move[1]]
                    if self.isValidNode(potentialNode, arenaMap):
                        heuristic = len(currNode[2]) + heuristicFun(potentialNode, endNode)
                        if self.isBetterNode(potentialNode, heuristic, visitedNodes, priorityQueue):
                            visitedNodes[tuple(potentialNode)] = heuristic
                            heapq.heappush(priorityQueue, (heuristic, potentialNode, currNode[2] + [moveCode]))

                maxFringe = max(maxFringe, len(priorityQueue))

        # The code will complete the while loop only if no path to the destination exists
        # The '-1' in the returned values indicate no path was found
        return [-1, [-1], len(visitedNodes), maxFringe, time.time() - startTime]

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

    def isBetterNode(self, potentialNode, heuristic, visitedNodes, priorityQueue):
        presentInVisitedNodes = tuple(potentialNode) in visitedNodes    # Boolean: Indicates if the potentialNode is present in visitedNodes
        matchingNodeInPriorityQueue = list(filter(lambda x, n=potentialNode: x[1][0] == n[0] and x[1][1] == n[1], priorityQueue))
        presentInPriorityQueue = len(matchingNodeInPriorityQueue) > 0       # Boolean: Indicates if the potentialNode is present in priorityQueue

        if not presentInPriorityQueue and not presentInVisitedNodes:
            # If the potentialNode is not present in either of the lists,
            # the it indicates this is the first time we are seeing the node
            # Thus push it to priorityQueue
            return True
        elif presentInVisitedNodes and visitedNodes[tuple(potentialNode)] > heuristic:
            # We have visited the potentialNode before, but the current path is better
            return True
        elif presentInPriorityQueue and matchingNodeInPriorityQueue[0][0] > heuristic:
            # The potentialNode is already present in priorityQueue, but the current path is better
            return True

        return False

    def isValidNode(self, node, arenaMap):
        # Check left and right wall
        return True if node[0] > -1 and node[0] < len(arenaMap) and node[1] > -1 and node[1] < len(arenaMap) and arenaMap[node[0]][node[1]] == 0 else False

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
        mazee.setup_maze(arenaMap)
        pass

    def sketchMap(self, arenaMap):
        mapString = ""
        mapString += "#" * (len(arenaMap) + 2) + "\n"
        for row in arenaMap:
            mapString +=  "#"
            for cell in row:
                mapString += str(cell)
            mapString += "#\n"

        mapString += "#" * (len(arenaMap) + 2) + "\n"
        return mapString

if __name__ == "__main__":
    arenaMap = GameMap().genMapWithProb(500, 0.1)
    # arenaMap = [[0,0,1,0],[0,0,1,0],[1,0,1,0],[0,1,0,0]]      # Negative Map
    # arenaMap = [[0,1,0,0],[0,0,0,1],[0,1,0,0],[0,0,0,0]]      # Positive Map
    # arenaMap = [[0,0,0,1,1],[1,0,0,0,1],[0,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]]    # Previously Failed Map
    # arenaMap = [[0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0],[1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0],[1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1],[0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1],[0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0],[0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],[0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1],[0,1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1],[0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],[0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0],[0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0],[1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1],[0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0],[1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,1],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1],[0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1],[0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1],[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0]]
    # GameMap().drawMap(arenaMap)
    print(GameMap().sketchMap(arenaMap))

    print("Numbers in 'Path' indicate directions travelled\n1=Up,2=Right,3=Down,4=Left\n")

    print("A* - Euclidean Distance")
    print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().AStar(arenaMap, SearchAlgorithms().euclideanDistance)))
    print("\nA* - Manhattan Distance")
    print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().AStar(arenaMap, SearchAlgorithms().manhattanDistance)))
    print("\nDepth First Search")
    print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().DFS(arenaMap)))
    print("\nBreadth First Search")
    print("ShortestPath: {0[0]}  Path: {0[1]}\nNodesVisited: {0[2]}  MaxFringe: {0[3]}  Time: {0[4]}s".format(SearchAlgorithms().BFS(arenaMap)))
