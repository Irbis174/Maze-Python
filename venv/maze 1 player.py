from game import *

while run:
    if flag:
        lvl = str(randrange(50))
        bg = pygame.image.load('image/lvl/' + lvl + '.png').convert_alpha()
        flag = False
    screen.blit(bg, (0, 0))
    screen.blit(walk_right[player_anim_cnt],(player_x ,player_y))
    if gameplay:
        player_rect = walk_left[0].get_rect(topleft = (player_x,player_y))
        square_rect = end_square.get_rect(topleft= (1307,687))

        if player_rect.colliderect(square_rect):
            cnt+=1
            gameplay = False

        screen.blit(end_square, (1307,687))
        if (bg.get_at((player_x + 5, player_y + 25)) == (255, 255, 255, 255)) and (bg.get_at((player_x + 15, player_y + 20)) == (255, 255, 255, 255)):
            player_x, player_y = move_first(player_x, player_y, player_speed)
        else:
            player_x = 0
            player_y = 10

        if player_anim_cnt == 3:
            player_anim_cnt = 0
        else:
            player_anim_cnt +=1
    else:
        scr(screen, win_lable, restart_lable, cnt)

        gameplay, player_x, player_y, flag = mouse_actions(restart_lable_rect, gameplay, player_x, player_y, flag)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    clock.tick(60)
