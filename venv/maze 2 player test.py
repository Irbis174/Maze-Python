from game import *


while run:
    if flag:
        lvl = str(randrange(50))
        bg = pygame.image.load('image/lvl/' + lvl + '.png').convert_alpha()
        flag = False
    screen.blit(bg, (0, 0))
    screen.blit(walk_right[player_anim_cnt],(player_x,player_y))
    screen.blit(walk_left[player_anim_cnt], (player_x1, player_y1))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft = (player_x,player_y))
        player1_rect = walk_right2[0].get_rect(topleft = (player_x1,player_y1))

        if player_rect.colliderect(player1_rect):
            cnt+=1
            gameplay = False

        if (bg.get_at((player_x+5,player_y+25)) == (255, 255, 255, 255)) and (bg.get_at((player_x+15,player_y+20)) == (255, 255, 255, 255)):
           player_x,player_y = move_first(player_x,player_y,player_speed)
        else:
            player_x = 0
            player_y = 10

        if (bg.get_at((player_x1+5,player_y1+25)) == (255, 255, 255, 255)) and (bg.get_at((player_x1+15,player_y1+20)) == (255, 255, 255, 255)):
            player_x1, player_y1 = move_second(player_x1,player_y1,player_speed)
        else:
            player_x1 = 1320
            player_y1 = 680

        player_x, player_y = fix(player_x, player_y)
        player_x1, player_y1 = fix(player_x1,player_y1)

        if player_anim_cnt == 3:
            player_anim_cnt = 0
        else:
            player_anim_cnt +=1
    else:
        s

        gameplay, player_x, player_y, player_x1, player_y1, flag = mouse_actions(restart_lable_rect,gameplay,player_x,player_y,player_x1,player_y1,flag)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(60)