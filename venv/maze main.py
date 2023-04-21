import pygame
from random import *
import sys


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1350,750))
FPS = pygame.time.Clock()
pygame.display.set_caption("Лабиринт")
coin = pygame.image.load('image/1.png').convert_alpha()
pygame.display.set_icon(pygame.image.load('image/icons.png'))

end_square = pygame.image.load('image/end.png').convert_alpha()

walk_right = [
    pygame.image.load('image/right/1-.png').convert_alpha(),
    pygame.image.load('image/right/2-.png').convert_alpha(),
    pygame.image.load('image/right/3-.png').convert_alpha(),
    pygame.image.load('image/right/4-.png').convert_alpha()
]
walk_left = [
    pygame.image.load('image/left/1-.png').convert_alpha(),
    pygame.image.load('image/left/2-.png').convert_alpha(),
    pygame.image.load('image/left/3-.png').convert_alpha(),
    pygame.image.load('image/left/4-.png').convert_alpha()
]

label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
win_lable = label.render('Вы выиграли!', False, (193,19,199))
restart_lable = label.render('Играть заново', False, (115,132,148))
restart_lable_rect = restart_lable.get_rect(topleft=(525, 300))


player_speed = 1
player_x = 1
player_y = 10
player_anim_cnt = 0

coin_x=0
coin_y=0
cnt_money = 0

gameplay = True
flag = True
flag1 = True
run = True

while run:
    if flag:
        lvl = str(randrange(11))
        bg = pygame.image.load('image/lvl/' + lvl + '.png').convert_alpha()
        flag = False
    screen.blit(bg, (0, 0))
    screen.blit(walk_right[player_anim_cnt],(player_x ,player_y))
    if gameplay:
        player_rect = walk_left[0].get_rect(topleft = (player_x,player_y))
        square_rect = end_square.get_rect(topleft= (1307,687))

        if player_rect.colliderect(square_rect):
            gameplay = False

        screen.blit(end_square, (1307,687))
        if (bg.get_at((player_x+5,player_y+25)) == (255, 255, 255, 255)) and (bg.get_at((player_x+15,player_y+20)) == (255, 255, 255, 255)):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                screen.blit(walk_right[player_anim_cnt], (player_x, player_y))
            elif  keys[pygame.K_a]:
                screen.blit(walk_left[player_anim_cnt], (player_x, player_y))
            if keys[pygame.K_a] and player_x > 0 :
                player_x -= player_speed
            elif keys[pygame.K_d] and player_x < 1360:
                player_x += player_speed
            elif keys[pygame.K_s] and player_y < 760:
                player_y += player_speed
            elif keys[pygame.K_w] and player_y > 0:
                player_y -= player_speed
        else:
            player_y = 10
            player_x = 0

        if player_anim_cnt == 3:
            player_anim_cnt = 0
        else:
            player_anim_cnt +=1
    else:
        screen.fill((87,88,89))
        screen.blit(win_lable, (525, 250))
        screen.blit(restart_lable, restart_lable_rect)

        mouse = pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_y = 10
            player_x = 0
            flag = True
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(60)
