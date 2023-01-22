import sys, os
from rush_hour_creator import *
from plan_reader import *
from game import *

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
