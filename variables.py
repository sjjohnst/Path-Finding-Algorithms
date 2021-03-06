'''VARIABLES'''
import pygame as py

#DISPLAY SPECS
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700
DISPLAY_SPACE = DISPLAY_HEIGHT - DISPLAY_WIDTH

#BOARD SPECS
HEIGHT = 20
WIDTH = 20

BUTTON_HEIGHT = DISPLAY_HEIGHT - DISPLAY_SPACE + 10

CELLSIZE = int(DISPLAY_WIDTH / WIDTH)

#COLOURS
WHITE = (255,255,255)

BLACK = (0,0,0)
GRAY = (35, 45, 35)

GREEN = (0,255,0)
DARK_GREEN = (0,200,0)

RED = (255,0,0)
DARK_RED = (195,0,0)

BLUE = (0,0,255)
DARK_BLUE = (0,0,194)

#FONTS
BASICFONTSIZE = 30
SMLFONTSIZE = 10
BASICFONT = 'freesansbold.ttf'
