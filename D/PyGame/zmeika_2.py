# Написать игру "Змейка" в PyGame
# Продолжить разработку игры. Доработать еду для змейки(змейка увеличивается при поедании чего-нибудь)
#
# По желанию добавить:
#
# -Фон
#
# -Счётчик очков


import pygame
import sys
import random

pygame.init()
white = (255, 255, 255)
blue = (0, 0, 255)
blue_1 = (204, 255, 255)
Red = (224,0,0)
Header_Color = (0,204,153)
Snake_Color = (0,102,0)
red = (224, 0, 0)

Size_Block = 20
Frame_Color = (0, 255, 204)
Count_Blocks = 20
Header_Margin = 70
Margin = 1
size = [Size_Block*Count_Blocks + 2*Size_Block + Margin*Count_Blocks,
        Size_Block * Count_Blocks + 2 * Size_Block + Margin * Count_Blocks + Header_Margin]
print(size)

dis = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")
timer = pygame.time.Clock()

class SnakeBlock:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<Size_Block and 0<=self.y<Size_Block

    def __eg__(self,other):
        return isinstance(other,SnakeBlock) and self.x == other.x and self.y == other.y

def get_random_empty_block():
    x = random.randint(0,Count_Blocks-1)
    y = random.randint(0,Count_Blocks - 1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0,Count_Blocks-1)
        empty_block.y = random.randint(0,Count_Blocks - 1)
    return empty_block

def draw_block(color,row,column):
    pygame.draw.rect(dis, color, [Size_Block + column * Size_Block + Margin * (column + 1),
                                  Header_Margin + Size_Block + row * Size_Block + Margin * (row + 1),
                                  Size_Block,
                                  Size_Block])


game_over = False

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

snake_blocks= [SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]
apple = get_random_empty_block()
d_row = 0
d_col = 1
total = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col !=0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col !=0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row !=0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row!=0:
                d_row = 0
                d_col = 1

    dis.fill(Frame_Color)
    pygame.draw.rect(dis, Header_Color, [0, 0, size[0], Header_Margin])
    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True


    for row in range(Count_Blocks):
        for column in range(Count_Blocks):
            if (row + column) % 2 == 0:
                color = blue_1
            else:
                color = white

            draw_block(color,row,column)

    head = snake_blocks[-1]
    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()
    draw_block(Red,apple.x,apple.y)
    for block in snake_blocks:
        draw_block(Snake_Color,block.x,block.y)

    if apple == head:
        total +=1
        snake_blocks.append(apple)
        apple = get_random_empty_block()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)


    pygame.display.flip()
    timer.tick(3)

# while True > if apple==head

    x1 += x1_change
    y1 += y1_change

    pygame.display.flip()

    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame = quit()
quit()
