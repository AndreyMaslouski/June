# Написать игру "Змейка" в PyGame
# Продолжить разработку игры. Доработать еду для змейки(змейка увеличивается при поедании чего-нибудь)
#
# По желанию добавить:
#
# -Фон
#
# -Счётчик очков


import pygame

pygame.init()
white = (255, 255, 255)
blue = (0, 0, 255)
blue_1 = (204, 255, 255)
Header_Color = (0,204,153)
red = (255, 0, 0)

Size_Block = 20
Frame_Color = (0, 255, 204)
Count_Blocks = 20
Header_Margin = 70
Margin = 1
size = [Size_Block*Count_Blocks + 2*Size_Block + Margin*Count_Blocks,
        Size_Block * Count_Blocks + 2 * Size_Block + Margin * Count_Blocks + Header_Margin]
print(size)

dis = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Snake")

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

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()

    dis.fill(Frame_Color)
    pygame.draw.rect(dis, Header_Color, [0, 0, size[0], Header_Margin])

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    dis.fill(Frame_Color)
    pygame.draw.rect(dis, Header_Color, [0, 0, size[0], Header_Margin])

    for row in range(Count_Blocks):
        for column in range(Count_Blocks):
            if (row + column) % 2 == 0:
                color = blue_1
            else:
                color = white

            draw_block(color,row,column)
            # pygame.draw.rect(dis, color, [Size_Block + column * Size_Block + Margin * (column+1),
            #                               Header_Margin + Size_Block + row*Size_Block + Margin * (row+1),
            #                               Size_Block,
            #                               Size_Block])

    pygame.display.flip()

    x1 += x1_change
    y1 += y1_change

    pygame.display.flip()

    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)

pygame = quit()
quit()
