import pygame
from constants import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = WIDTH / 2, HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,35,35)

    def draw_cursor(self):
        self.game.draw_text('*', OPCION, self.cursor_rect.x, self.cursor_rect.y)
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_keys()
    
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + OPCION + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 2 * OPCION + 60
        self.cursor_rect.midtop = (self.startx + CURSOR_OFFSET, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(NEGRO)
            self.game.draw_text('Main Menu', TITULO, WIDTH / 2, HEIGHT / 2 - ALTURA_TITULO)
            self.game.draw_text('Start Game', OPCION, self.startx, self.starty)
            self.game.draw_text('Options', OPCION, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', OPCION, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()
    
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + CURSOR_OFFSET, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + CURSOR_OFFSET, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + CURSOR_OFFSET, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + CURSOR_OFFSET, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + CURSOR_OFFSET, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + CURSOR_OFFSET, self.optionsy)
                self.state = 'Options'
        
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False    #Per aturar la funció display_menu()


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + OPCION
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 2 * OPCION + 30
        self.cursor_rect.midtop = (self.volx + CURSOR_OFFSET, self.voly)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(NEGRO)
            self.game.draw_text('Options', TITULO, WIDTH / 2, HEIGHT / 2 - ALTURA_TITULO)
            self.game.draw_text('Volume', OPCION, self.volx, self.voly)
            self.game.draw_text('Controls', OPCION, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()
    
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + CURSOR_OFFSET, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + CURSOR_OFFSET, self.voly)

        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(NEGRO)
            self.game.draw_text('Credits', TITULO, WIDTH / 2, HEIGHT / 2 - ALTURA_TITULO)
            self.game.draw_text('Made by Òscar Molina', OPCION, WIDTH / 2, HEIGHT / 2 + 10)
            self.blit_screen()



