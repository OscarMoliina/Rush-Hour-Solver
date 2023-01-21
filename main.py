import os
import timeit
import sys
import pygame, rush_hour_creator, plan_reader

CELLS = 6
BOARD_SIZE = CELLS * 100

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

MARGEN = 5

pygame.init()
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Rush-Hour Planner")

reloj = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(NEGRO)

    reloj.tick(60)
    pygame.display.flip()
    
pygame.quit()
