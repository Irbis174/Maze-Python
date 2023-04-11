import pygame

screen = pygame.display.set_mode((800,600))


def get_rects(file):
    res = []
    file = open(file, 'r').readlines()
    file = [i.replace('\n', '') for i in file]
    for y in range(len(file)):
        for x in range(len(file[0])):
            if file[y][x] == '1':
                res.append((x * 50, y * 50, 50, 50))
    return res


pygame.init()
rects = get_rects('lvl1')
while True:
    for i in rects:
        pygame.draw.rect(screen, (0, 0, 0), i)
    screen.display.update()
