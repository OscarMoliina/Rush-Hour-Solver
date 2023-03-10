import pygame
from resources import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.window = pygame.display.set_mode(((WIDTH, HEIGHT)))
        self.font_name = 'resources/Arcadia.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.board = Board(self)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY or self.BACK_KEY:
                self.playing = False
            self.display.fill(NEGRO)
            
            self.board.draw_board()
            
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
            
    def draw_text(self, text, size, x, y, rotation):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, BLANCO)
        if rotation != 0:
            text_surface = pygame.transform.rotate(text_surface,rotation)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)



