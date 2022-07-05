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
import pygame_menu

pygame.init()

white = (255, 255, 255)
blue = (204, 255, 255)
Red = (224, 0, 0)
Header_Color = (0, 204, 153)
Snake_Color = (0, 102, 0)

Size_Block = 20
Frame_Color = (0, 255, 204)
Count_Blocks = 20
Header_Margin = 70
Margin = 1
size = [Size_Block * Count_Blocks + 2 * Size_Block + Margin * Count_Blocks,
        Size_Block * Count_Blocks + 2 * Size_Block + Margin * Count_Blocks + Header_Margin]
print(size)

dis = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x< Count_Blocks and 0<= self.y<Count_Blocks

    def __eg__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def get_randon_empty_block():
    x = random.randint(0, Count_Blocks-1)
    y = random.randint(0, Count_Blocks - 1)
    empty_block = SnakeBlock(x,y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, Count_Blocks - 1)
        empty_block.y = random.randint(0, Count_Blocks - 1)
    return empty_block


def draw_block(color, row, column):
    pygame.draw.rect(dis, color, [Size_Block + column * Size_Block + Margin * (column + 1),
                                  Header_Margin + Size_Block + row * Size_Block + Margin * (row + 1),
                                  Size_Block,
                                  Size_Block])




snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = get_randon_empty_block()
d_row  = 0
d_col = 1
total = 0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col!=0:
                d_row = 0
                d_col = -10
            elif event.key == pygame.K_DOWN and d_col!=0:
                d_row = 0
                d_col = 10
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = -10
                d_col = 0
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 10
                d_col = 0

    dis.fill(Frame_Color)
    pygame.draw.rect(dis, Header_Color, [0, 0, size[0], Header_Margin])

    text_total = courier.render(f"Total: {total}", 0, white)
    text_speed = courier.render(f"Speed: {speed}", 0, white)
    dis.blit(text_total, (Size_Block, Size_Block))
    dis.blit(text_speed, (Size_Block + 230, Size_Block))

    for row in range(Count_Blocks):
        for column in range(Count_Blocks):
            if (row + column) % 2 == 0:
                color = blue
            else:
                color = white

            draw_block(color, row, column)

    head = snake_blocks[-1]
    if not head.is_inside():
        print('crash')
        pygame.quit()
        sys.exit()

    draw_block(Red, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(Snake_Color, block.x, block.y)

    pygame.display.flip()
    if apple == head:
        total+= 1
        speed = total // 5 + 1
        snake_blocks.append(apple)
        apple = get_randon_empty_block()

    d_row
    d_col
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)


    if new_head in snake_blocks:
        print('crash yourself')
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    timer.tick(3 + speed)

# def set_difficulty(value,difficulty):
#     pass
# def start_the_game():
#     pass
#
# menu = pygame_menu.Menu(300,400,'Welcome',
#                    theme=pygame_menu.themes.THEME_BLUE)
#
# menu.add_text_input('Name: ', default = 'John Doe')
# menu.add_selector('Difficulty: ', [('Hard',1), ('Easy',2)],onchange=set_difficulty)
# menu.add_button('Play',start_the_game)
# menu.add_button('Quit',pygame_menu.events.EXIT)
#
# menu.mainloop(dis)

# pygame = quit()
# quit()
