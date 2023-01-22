import pygame
from constants import *

class Coche():
    def __init__(self):
        self.is_pressed = False

class Cell():
    def __init__(self, i, j):
        self.color = GRIS_CLARO

class Board():
    def __init__(self,game):
        self.grid = [[Cell(i,j) for j in range(CELLS)] for i in range(CELLS)]
        self.background = pygame.Surface((HEIGHT, HEIGHT))
    
    def draw_grid(self):
        pass

    def draw_backgroud(self):
        self.background.fill(GRIS_CLARO)
    
    def draw_board(self):
        self.draw_grid()
        self.draw_backgroud()