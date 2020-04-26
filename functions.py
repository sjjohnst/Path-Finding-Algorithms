''' FUNCTIONS '''
import sys
import pygame as py

from variables import *

''' GRAPH FUNCTIONS '''
def initializeGraph(start, end):
    graph = []
    row = []
    for y in range(HEIGHT):
        row = ['o' for x in range(WIDTH)]
        graph.append(row)

    startx = start[0]
    starty = start[1]
    endx = end[0]
    endy = end[1]

    graph[starty][startx] = 's'
    graph[endx][endy] = 'e'

    return graph

def findIndex(List, elem):
    for i, x in enumerate(List):
        if elem in x:
            return [i, x.index(elem)]
    return False

def moveStartOrEnd(x,y,graph,elem):
    coord = findIndex(graph, elem)
    if coord:
        a = coord[1]
        b = coord[0]
        graph[b][a] = 'o'
        graph[y][x] = elem

    else:
        graph[y][x] = elem

def changeCell(mousex, mousey, graph, elem):
    boxx = int(mousex/CELLSIZE)
    boxy = int(mousey/CELLSIZE)
    graph[boxy][boxx] = elem

def addPath(graph,start,end,solution):
    for coord in solution:
        if coord != start and coord != end:
            x = coord[0]
            y = coord[1]
            graph[y][x] = 'P'

def clearGraph(graph):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            elem = graph[y][x]
            if elem != 'e' and elem != 's':
                graph[y][x] = 'o'

def clearPath(graph):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            elem = graph[y][x]
            if elem == 'P':
                graph[y][x] = 'o'
    
''' DRAWING BOARD '''

def drawBox(x,y,colour,surface):
    py.draw.rect(surface, colour, (x,y,CELLSIZE,CELLSIZE))

def drawBoard(surface, graph):

    for x in range(CELLSIZE, DISPLAY_WIDTH, CELLSIZE):
        py.draw.line(surface, BLACK, (x,0), (x,DISPLAY_HEIGHT-DISPLAY_SPACE))

    for y in range(0, DISPLAY_WIDTH + CELLSIZE, CELLSIZE):
        py.draw.line(surface, BLACK, (0,y),(DISPLAY_WIDTH,y))
    
    for y in range(HEIGHT):
        b = y*CELLSIZE
        for x in range(WIDTH):
            a = x*CELLSIZE
            if graph[y][x] == 'e':
                drawBox(a,b,RED,surface)
            if graph[y][x] == 's':
                drawBox(a,b,GREEN,surface)
            if graph[y][x] == 'P':
                drawBox(a,b,BLUE,surface)
            if graph[y][x] == 'x':
                drawBox(a,b,BLACK,surface)
