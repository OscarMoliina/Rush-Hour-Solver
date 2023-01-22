import pygame
from menu import *
from plan_reader import *
import constants

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.CELLS = 6
        self.BOARD_SIZE = self.CELLS * 100
        self.display = pygame.Surface((self.BOARD_SIZE, self.BOARD_SIZE))
        self.window = pygame.display.set_mode(((self.BOARD_SIZE, self.BOARD_SIZE)))
        self.font_name = 'Arcadia.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.NEGRO, self.BLANCO, self.VERDE, self.ROJO = (0, 0, 0),(255, 255, 255),(0, 255, 0),(255, 0, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.NEGRO)
            self.draw_text('Thanks for Playing', 20 , self.BOARD_SIZE/2, self.BOARD_SIZE/2)

            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running , self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
            
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.BLANCO)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)



