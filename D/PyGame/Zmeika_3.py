import pygame
from random import randrange

#основные настройки
RES = 800
SIZE = 50

x,y = randrange(SIZE,RES - SIZE,SIZE),randrange(SIZE,RES - SIZE,SIZE)
apple = randrange(SIZE,RES-SIZE,SIZE), randrange(SIZE,RES-SIZE,SIZE)
length = 1
snake = [(x,y)]
dx,dy = 0,0
fps = 60

#управление с помощью кнопок
dirs = {'W':True,'S':True,'A':True,'D':True}

score = 0
speed_count, snake_speed = 0,10

pygame.init()
surface = pygame.display.set_mode([RES,RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial',26,bold = True)
font_end = pygame.font.SysFont('Arial',66,bold = True)
img = pygame.image.load('5.jpg').convert()

# закрытие игры

def close_game():
    for event in pygame.event.get():
        if every.type == pygame.QUIT:
            exit()


