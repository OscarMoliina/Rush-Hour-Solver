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
        self.grid = [[Cell(i,j) for j in range(1,CELLS+1)] for i in range(1,CELLS+1)]
        self.background = pygame.Surface((HEIGHT, HEIGHT))
        self.cars_space = pygame.Surface((WIDTH-HEIGHT, HEIGHT))
        self.exit = pygame.Surface((30,CELL_SIZE))
        self.option_selected = False
        self.option1 = 'Horizontal 2'
        self.option2 = 'Horizontal 3'
        self.option3 = 'Vertical 2'
        self.option4 = 'Vertical 3'
    
    def draw_grid(self):
        for i in range(1,LINES + 1):
            pygame.draw.line(self.game.display, 
                            GRIS_CLARO,
                            (i * CELL_SIZE, 0),
                            (i * CELL_SIZE, HEIGHT),
                            LINES_WIDTH)
        for i in range(1,LINES + 1):
            pygame.draw.line(self.game.display, 
                            GRIS_CLARO,
                            (0, i * CELL_SIZE),
                            (HEIGHT-1, i * CELL_SIZE),
                            LINES_WIDTH)
        self.exit.fill(ROJO)
        
        self.game.display.blit(self.exit, (HEIGHT,CELL_SIZE+1))
        self.game.draw_text('Exit', 20, HEIGHT + 12, CELL_SIZE + CELL_SIZE // 2, -90)

    def draw_options(self):
        pass

    def draw_backgroud(self):
        self.background.fill(TURQUESA)
        self.game.display.blit(self.background, (0,0))
    
    def draw_board(self):
        self.draw_backgroud()
        self.draw_grid()
        self.draw_options()