import pygame
from constants import *

class Coche():
    def __init__(self):
        self.is_pressed = False

class Cell():
    def __init__(self, i, j):
        self.color = GRIS_CLARO
        self.row = i
        self.column = j

class Board():
    def __init__(self,game):
        self.game = game
        self.grid = [[Cell(i,j) for j in range(CELLS)] for i in range(CELLS)]
        self.lines = CELLS - 1
        self.background = pygame.Surface((HEIGHT, HEIGHT))
    
    def draw_grid(self):
        for i in range(1,LINES + 1):
            pygame.draw.line(self.game.window, 
                            GRIS_OSCURO,
                            (i * CELL_SIZE, 0),
                            (i * CELL_SIZE, HEIGHT),
                            LINES_WIDTH)
        for i in range(1,LINES + 1):
            pygame.draw.line(self.game.window, 
                            GRIS_OSCURO,
                            (0, i * CELL_SIZE),
                            (HEIGHT-1, i * CELL_SIZE),
                            LINES_WIDTH)

    def draw_backgroud(self):
        self.background.fill(GRIS_CLARO)
        self.game.window.blit(self.background, (0,0))
    
    def draw_board(self):
        self.draw_backgroud()
        self.draw_grid()