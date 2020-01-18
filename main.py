'''MAIN DRIVER'''
import sys
import pygame as py

from variables import *
from DFS import *


def initializeGrid(graph):
    for y in range(HEIGHT):
        graph[y] = ['o' for x in range(WIDTH)]

    graph[STARTX][STARTY] = 's'
    graph[ENDY][ENDX] = 'e'

def findBoxIndex(mousex, mousey, graph):
    boxx = int(((mousex*WIDTH)/DISPLAY_WIDTH))*(graph.cellsize_x)
    boxy = int(((mousey*HEIGHT)/DISPLAY_HEIGHT))*(graph.cellsize_y)
    return boxx, boxy

def findGridIndex(mousex, mousey):
    x_pos = int(((mousex*WIDTH)/DISPLAY_WIDTH))
    y_pos = int(((mousey*HEIGHT)/DISPLAY_HEIGHT))
    return x_pos, y_pos

def drawGrid(graph, button, mousex, mousey):
    boxx, boxy = findBoxIndex(mousex, mousey, graph)
    x_pos, y_pos = findGridIndex(boxx,boxy)
    if button == 1:
        graph.graph[y_pos][x_pos] = 'x'
    elif button == 3:
        graph.graph[y_pos][x_pos] = 'o'
    print(graph.graph)

def main():

    py.init()
    window = py.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    coordinates = ['o']*HEIGHT
    initializeGrid(coordinates)
    graph = Graph(coordinates)

    mousex, mousey = py.mouse.get_pos()
    mouseDown = False

    while True:
        
        for e in py.event.get():

            if e.type == py.QUIT:
                py.quit()
                sys.exit()

            if e.type == py.KEYDOWN:

                if e.key == py.K_SPACE:
                    graph.DFS()

                if e.key == py.K_RETURN:
                    initializeGrid(graph.graph)
                    print(graph.graph)

            elif e.type == py.MOUSEMOTION:
                mousex, mousey = e.pos
                boxx, boxy = findBoxIndex(mousex, mousey, graph)

            elif e.type == py.MOUSEBUTTONDOWN:
                mouseDown = True
                #print(x_pos , y_pos)
                button = e.button

            elif e.type == py.MOUSEBUTTONUP:
                mouseDown = False
                

        if(mouseDown):
            drawGrid(graph, button, mousex, mousey)

        #graph.DFS()
        window.fill(WHITE)
        graph.drawGraph(window, boxx, boxy)
        py.display.update()


main()
