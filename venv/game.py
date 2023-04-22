import pygame
from random import *
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1340,800))
FPS = pygame.time.Clock()
pygame.display.set_caption("Лабиринт")
pygame.display.set_icon(pygame.image.load('image/icons.png'))
cnt = 0

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
walk_left2 = walk_left
walk_right2 = walk_right

label = pygame.font.Font('fonts/Roboto-Black.ttf', 40)

win_lable = label.render('Вы выиграли!', False, (193,19,199))
restart_lable = label.render('Играть заново', False, (115,132,148))
restart_lable_rect = restart_lable.get_rect(topleft=(525, 300))


player_speed = 1
player_x = 0
player_y = 10
player_x1 = 1320
player_y1 = 680
player_anim_cnt = 0

gameplay = True
flag = True
flag1 = True
run = True

def move_first(player_x,player_y,player_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_cnt], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_cnt], (player_x, player_y))
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 1324:
        player_x += player_speed
    elif keys[pygame.K_s] and player_y < 760:
        player_y += player_speed
    elif keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    return [player_x,player_y]

def move_second(player_x,player_y,player_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        screen.blit(walk_left2[player_anim_cnt], (player_x, player_y))
    elif keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_cnt], (player_x, player_y))
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 1400:
        player_x += player_speed
    elif keys[pygame.K_DOWN] and player_y < 760:
        player_y += player_speed
    elif keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    return [player_x,player_y]

def fix(player_x,player_y):
    if player_x == 1323 and player_y < 694:
        player_x = 1320
        player_y = 680
    return [player_x,player_y]

def scr(screen,win_lable,restart_lable,cnt):
    text = label.render("Кол-во пройденных раз: " + str(cnt), True, (180, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(win_lable, (525, 250))
    screen.blit(restart_lable, restart_lable_rect)
    screen.blit(text, (100, 745))

def mouse_actions(restart_lable_rect,gameplay,player_x,player_y,player_x1,player_y1,flag):
    mouse = pygame.mouse.get_pos()
    if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        player_y = 10
        player_x = 0
        player_x1 = 1320
        player_y1 = 680
        flag = True
    return [gameplay,player_x,player_y,player_x1,player_y1,flag]

def mouse_actions(restart_lable_rect,gameplay,player_x,player_y,flag):
    mouse = pygame.mouse.get_pos()
    if restart_lable_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        player_y = 10
        player_x = 0
        flag = True
    return [gameplay,player_x,player_y,flag]