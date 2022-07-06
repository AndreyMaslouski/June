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

# игра
while True:

    #  Отрисовка змеи и яблок
    [pygame.draw.rect(surface,pygame.Color('green'),(i,j,SIZE - 1, SIZE-1)) for i,j in snake]
    pygame.draw.rect(surface,pygame.Color('red'),(*apple,SIZE,SIZE))

    # Отрисовка очков
    render_score = font_score.render(f'SCORE: {score}',1,pygame.Color('orange'))
    surface.blit(render_score,(5,5))

    # Движение змеи
    speed_count +=1
    if not speed_count % snake_speed:
        x +=dx*SIZE
        y +=dy*SIZE
        snake.append((x,y))
        snake = snake[-length:]

    # Поедание еды
    if snake[-1] == apple:
        apple = randrange(SIZE),RES - SIZE,SIZE),randrange(SIZE),RES - SIZE,SIZE)
        length +=1
        score +=1
        snake_speed -=1
        snake_speed = max(snake_speed,4)

    #  Конец игры
    if x<0 or x>RES-SIZE or y<0 or y>RES-SIZE or len(snake) !=len(set(snake)):


