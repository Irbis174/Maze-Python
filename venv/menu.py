import pygame
from random import *
import sys


class Menu:
    def __init__(self):
        self._option_surface = []
        self._callbacks = []
        self._current_option_index = 0
        def append_options(self,option,callback):
            self._options_surfaces.append(menu_label.render())
pygame.init()
def menu():
    screen_menu = display.set_mode((800,600))

    menu_run = True


    while menu_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False

        screen_menu.fill((0,0,0))
        pygame.display.update()
    pygame.quit()