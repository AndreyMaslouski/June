# Написать игру "Змейка" в PyGame
import pygame

pygame.init()
dis = pygame.display.set_mode((400,300))

pygame.display.set_caption("Snake")

blue = (0,0,255)
red = (255,0,0)

game_over = True

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True




