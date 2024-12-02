"""
Prosta gra polegajca na przywróceniu całej mapy na kolor zielony.
"""

import pygame
import time
from random import randint
from typing import Final

N:Final = 6
K:Final = 2
SIDE:Final = 100


RED:Final = (255, 0, 0) #1
GREEN:Final = (0, 255, 0) #2
BLUE:Final = (0, 0, 255) #3
YELLOW:Final = (255, 255, 0) #4

tab = [[0]*N for _ in range(N)]

colors = [RED, GREEN, BLUE, YELLOW]


def draw_square(x:int, y:int) -> None:
    pygame.draw.rect(win,colors[tab[x][y]],(x*SIDE, y*SIDE, SIDE-1, SIDE-1))



def update_field(x:int, y:int):
    tab[x][y] = (tab[x][y] +1) % K
    draw_square(x, y)
    pygame.display.update()


def move(x:int, y: int):
    update_field(x, y)
    update_field((x-1) % N, y)
    update_field((x+1) % N, y)
    update_field(x, (y-1) % N)
    update_field(x, (y+1) % N)


pygame.init()

win = pygame.display.set_mode((N*SIDE, N*SIDE))
pygame.display.set_caption("Basic square game")
# win.fill((255, 255, 255)) -> set background to white

for _ in range(50):
    move(randint(0, N-1), randint(0, N-1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        #print(f'{pos=}')
        time.sleep(0.2)
        move(pos[0]//SIDE, pos[1]//SIDE)


    pygame.display.update()
