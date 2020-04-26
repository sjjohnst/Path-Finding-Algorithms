'''MAIN DRIVER'''


import pygame as py
import time

from variables import*
from functions import*
from pathFinder import *
from classes import *

def main():

    py.init()
    window = py.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    py.display.set_caption('Path Finder')
    font = py.font.Font(BASICFONT, BASICFONTSIZE)
    smFont = py.font.Font(BASICFONT, 10)

    start = [0,0]
    end = [19,19]
    board = Graph(start, end)
    pathfinder = Pathfinder(board.graph)
    noPath = Message("No Solution", 450, BUTTON_HEIGHT+10, font)

    clearButton = Button(10, BUTTON_HEIGHT, 80, 80, DARK_RED, RED)
    pathButton = Button(110, BUTTON_HEIGHT, 80, 80, DARK_BLUE, BLUE)
    BFS = Button(210, BUTTON_HEIGHT, 80, 80, DARK_GREEN, GREEN)

    clearText = Message("Clear", 50, BUTTON_HEIGHT+30, font)
    solveText = Message("Solve", 250, BUTTON_HEIGHT+30, font)

    drawing = False
    noSolution = False

    while True:
        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.KEYDOWN:

                mousex, mousey = py.mouse.get_pos()
                boxx = int(mousex/CELLSIZE)
                boxy = int(mousey/CELLSIZE)
                
                if event.key == py.K_SPACE:
                    start = [boxx,boxy]
                    board.changeCell(mousex, mousey, 's')

                if event.key == py.K_RETURN:
                    end = [boxx,boxy]
                    board.changeCell(mousex, mousey, 'e')

            if event.type == py.MOUSEBUTTONDOWN:
                mousex, mousey = py.mouse.get_pos()
                boxx = int(mousex/CELLSIZE)
                boxy = int(mousey/CELLSIZE)

                if event.button == 1:
                    element = 'x'
                    drawing = True

                if event.button == 3:
                   element = 'o'
                   drawing = True

                if clearButton.hover:
                    board.clear()

                if pathButton.hover:
                    board.clearPath()
                    noSolution = False

                if BFS.hover:
                    board.clearPath()
                    path = pathfinder.BFS(start)
                    if path:
                        board.addPath(path)
                        noSolution = False

                    else:
                        noSolution = True

            if event.type == py.MOUSEBUTTONUP:
                drawing = False

        mousex, mousey = py.mouse.get_pos()

        if drawing:
            board.changeCell(mousex, mousey, element)

        pathfinder.graph = board.graph
        window.fill(WHITE)

        if noSolution:
            noPath.display(window)

        #BUTTONS
        clearButton.drawButton(mousex, mousey, window)
        pathButton.drawButton(mousex, mousey, window)
        BFS.drawButton(mousex, mousey, window)
        clearText.display(window)
        solveText.display(window)
        
    
        board.draw(window)
        py.display.update()


main()
