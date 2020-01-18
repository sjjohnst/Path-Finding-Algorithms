''' DFS CLASS '''

import numpy as np
import pygame as py

from variables import *

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.path = []
        self.height = len(graph)
        self.width = len(graph[0])
        self.cellsize_x = int(DISPLAY_HEIGHT / self.width)
        self.cellsize_y = int(DISPLAY_WIDTH / self.height)
    
    def drawGraph(self, surface, boxx, boxy):
        for x in range(0, DISPLAY_WIDTH, self.cellsize_x):
            py.draw.line(surface, BLACK, (x,0), (x,DISPLAY_HEIGHT))

        for y in range(0, DISPLAY_HEIGHT, self.cellsize_y):
            py.draw.line(surface, BLACK, (0,y), (DISPLAY_WIDTH,y))

        for y_pos in range(self.height):
            for x_pos in range(self.width):

                box = self.graph[y_pos][x_pos]
                board_x = x_pos * self.cellsize_x
                board_y = y_pos * self.cellsize_x
                square = py.Rect(board_x, board_y,
                                self.cellsize_x, self.cellsize_y)

                if(box == 'P'):
                    py.draw.rect(surface, BLUE, square)

                elif(box == 'e'):
                    py.draw.rect(surface, RED, square)

                elif(box == 'x'):
                    py.draw.rect(surface, BLACK, square)

                elif(box == 's'):
                    py.draw.rect(surface, GREEN, square)
                    
        py.draw.rect(surface, BLUE, (boxx, boxy, self.cellsize_x, self.cellsize_y), 2)

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

        if([x,y] in self.path):
            return False

        else:
            return True
            


    def dfsUtil(self, x, y):

        if(self.graph[y][x] == 'e'):
            return True

        for direction in range(4):

            if self.isValid(x,y,direction):
                a,b = self.move(x,y,direction)
                self.path.append([a,b])

                if self.dfsUtil(a,b) == True:
                    return True

                self.path.pop()

        return False

    def DFS(self):
        x = STARTX
        y = STARTY
        if self.dfsUtil(x,y) == True:
            #print("Solution Exists")
            self.updateBoard()
            #print(self.graph)
        else:
            print("No Solution")

    def updateBoard(self):
        for coordinate in self.path:
            x = coordinate[0]
            y = coordinate[1]
            if (self.graph[y][x] == 'e'):
                continue
            self.graph[y][x] = 'P'

        self.path.clear()


