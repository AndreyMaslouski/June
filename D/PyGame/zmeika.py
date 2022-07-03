# Написать игру "Змейка" в PyGame
import pygame

pygame.init()
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

dis = pygame.display.set_mode((400,300))

pygame.display.set_caption("Snake")

game_over = False

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        pygame.draw.rect(dis,blue,(200,150,10,10))
        pygame.display.update()

pygame = quit()
quit()








