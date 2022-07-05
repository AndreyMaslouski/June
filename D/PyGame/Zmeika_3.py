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


