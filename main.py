from game import *

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
