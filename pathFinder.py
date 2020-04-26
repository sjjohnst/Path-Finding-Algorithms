''' PATH FINDING '''

import numpy as np
import pygame as py

from variables import *

class Pathfinder:

    def __init__(self, graph):
        self.graph = graph
        self.height = len(graph)
        self.width = len(graph[0])

    def move(self,x,y,direction):
        if direction == 0:
            x+=1
        elif direction == 1:
            y+=1
        elif direction == 2:
            x-=1
        elif direction == 3:
            y-=1
        return x,y

    def isValid(self,x,y,direction):
        x,y = self.move(x,y,direction)
        if(x<0 or x>=self.width):
            return False
        if(y<0 or y>=self.height):
            return False
        if(self.graph[y][x] == 'x'):
            return False
        else:
            return True
            
    def dfsUtil(self, x, y, path):

        if(self.graph[y][x] == 'e'):
            return True

        for direction in range(4):
            a,b = self.move(x,y,direction)
            if self.isValid(x,y,direction) and [a,b] not in path:
                #print("Moving to: " + str([a,b]))
                path.append([a,b])

                if self.dfsUtil(a,b,path) == True:
                    return True

                path.pop()

        return False

    def DFS(self, start):
        x = start[0]
        y = start[1]
        path = [start]
        if self.dfsUtil(x,y,path) == True:
            return path
        else:
            return False


    def getAdjacent(self,node):
        neighbours = []
        x = node[0]
        y = node[1]

        for direction in range(4):
            if self.isValid(x,y,direction):
                a,b = self.move(x,y,direction)
                neighbours.append([a,b])

        return neighbours
    
    def BFS(self, start):
        x=start[0]
        y=start[1]
        explored = []
        queue = [[start]]

        if self.graph[y][x] == 'e':
            return queue[0]

        while queue:

            path = queue.pop(0)
            node = path[-1]

            if node not in explored:
                neighbours = self.getAdjacent(node)
                #print(neighbours)

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    x = neighbour[0]
                    y = neighbour[1]
                    if self.graph[y][x] == 'e':
                        return new_path

                explored.append(node)

        return False
'''
graph = [['s', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'x', 'e', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']]
pathfinder = Pathfinder(graph)
print(pathfinder.DFS([0,0]))
'''

