
import pygame as py
from functions import *


class Graph:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.graph = self.createGraph()

    def createGraph(self, height=HEIGHT, width=WIDTH):
        graph = []
        row = []
        for y in range(height):
            row = ['o' for x in range(width)]
            graph.append(row)

        startx = self.start[0]
        starty = self.start[1]
        endx = self.end[0]
        endy = self.end[1]

        graph[starty][startx] = 's'
        graph[endx][endy] = 'e'

        return graph

    def findIndex(self, elem):
        for i, x in enumerate(self.graph):
            if elem in x:
                return [i, x.index(elem)]
        return False

    def changeCell(self, mousex, mousey, elem):
        boxx = int(mousex / CELLSIZE)
        boxy = int(mousey / CELLSIZE)
        if boxy >= len(self.graph):
            return
        if boxx >= len(self.graph[0]):
            return

        #Changing start/end
        if elem == 's' or elem == 'e':

            self.clearPath()

            if elem == 's':
                self.start = [boxx,boxy]
            if elem == 'e':
                self.end = [boxx,boxy]

            coord = self.findIndex(elem)
            if coord:
                a = coord[1]
                b = coord[0]
                self.graph[b][a] = 'o'
                self.graph[boxy][boxx] = elem

            else:
                self.graph[boxy][boxx] = elem

        #Changing to wall/empty
        else:
            self.graph[boxy][boxx] = elem

    def addPath(self, solution):
        for coord in solution:
            if coord != self.start and coord != self.end:
                x = coord[0]
                y = coord[1]
                self.graph[y][x] = 'P'

    def clear(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                elem = self.graph[y][x]
                if elem != 'e' and elem != 's':
                    self.graph[y][x] = 'o'

    def clearPath(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                elem = self.graph[y][x]
                if elem == 'P':
                    self.graph[y][x] = 'o'

    def drawBox(self, x, y, colour, surface):
        py.draw.rect(surface, colour, (x, y, CELLSIZE, CELLSIZE))

    def draw(self, surface):

        for x in range(CELLSIZE, DISPLAY_WIDTH, CELLSIZE):
            py.draw.line(surface, BLACK, (x, 0), (x, DISPLAY_HEIGHT - DISPLAY_SPACE))

        for y in range(0, DISPLAY_WIDTH + CELLSIZE, CELLSIZE):
            py.draw.line(surface, BLACK, (0, y), (DISPLAY_WIDTH, y))

        for y in range(HEIGHT):
            b = y * CELLSIZE
            for x in range(WIDTH):
                a = x * CELLSIZE
                if self.graph[y][x] == 'e':
                    self.drawBox(a, b, RED, surface)
                if self.graph[y][x] == 's':
                    self.drawBox(a, b, GREEN, surface)
                if self.graph[y][x] == 'P':
                    self.drawBox(a, b, BLUE, surface)
                if self.graph[y][x] == 'x':
                    self.drawBox(a, b, BLACK, surface)


class Button:

    def __init__(self, x, y, width, height, colour1, colour2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.current = colour1
        self.colour1 = colour1
        self.colour2 = colour2
        self.hover = False

    def drawButton(self, mousex, mousey, surface):
        self.changeColor(mousex, mousey)
        py.draw.rect(surface, self.current, (self.x, self.y, self.width, self.height))

    def changeColor(self, mousex, mousey):
        if mousex > self.x and mousex < self.x + self.width and mousey > self.y and mousey < self.y + self.height:
            self.hover = True
            self.current = self.colour2

        else:
            self.hover = False
            self.current = self.colour1


class Message:

    def __init__(self, message, x, y, font):
        self.message = message
        self.x = x
        self.y = y
        self.font = font
        self.text = font.render(self.message, True, BLACK, WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)

    def display(self, surface):
        surface.blit(self.text, self.textRect, special_flags=py.BLEND_RGBA_MULT)

    def newMessage(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, BLACK, WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
