# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0,5,157)
LIGHT_GREEN = (111,255,109)
GREEN = (0, 255, 0)
DARK_GREEN = (0,102,2)
LIGHT_RED = (255, 111, 97)
RED = (255, 0, 0)
DARK_RED = (137, 2, 0)
LIGHT_CYAN = (0, 255, 255)
CYAN = (0, 133, 244)
DARK_CYAN = (0,65,132)
GREENISH_YELLOW = (181,255,14)
YELLOW = (255, 255, 0)
DARK_YELLOW = (168, 165, 0)
ORANGE = (255, 116, 3)
DARK_ORANGE = (143, 64, 0 )
PURPLE = (117, 0, 244)
DARK_PURPLE = (64, 0, 113)
PINK = (240, 0, 236)
DARK_PINK = (168, 0, 166)
BROWN = (150, 75, 0)
LIGHT_GRAY = (210, 210, 210)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

pygame.init()


janela = pygame.display.set_mode((700,600))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((WHITE))

    # desenhando na superfície
    pygame.draw.ellipse(janela, BLUE, [10, 10, 20, 80])
    pygame.draw.ellipse(janela, GREEN, [50, 60, 30, 120])
    pygame.draw.ellipse(janela, GRAY, [100, 80, 50, 40])
    pygame.draw.ellipse(janela, DARK_PURPLE, [160, 100, 60, 150])
    pygame.draw.ellipse(janela, LIGHT_RED, [30, 180, 50, 110])
    pygame.draw.ellipse(janela, DARK_RED, [250, 120, 100, 150])
    pygame.draw.ellipse(janela, DARK_BLUE, [300, 5, 140, 70])
    pygame.draw.ellipse(janela, LIGHT_GRAY, [150, 5, 80, 30])
    pygame.draw.ellipse(janela, DARK_PINK, [400, 70, 60, 100])
    pygame.draw.ellipse(janela, DARK_GREEN, [400, 180, 50, 110])
    pygame.draw.ellipse(janela, LIGHT_CYAN, [100, 270, 160, 50])
    pygame.draw.ellipse(janela, GREENISH_YELLOW, [240, 40, 40, 90])
    pygame.draw.ellipse(janela, DARK_GRAY, [300, 270, 80, 130])
    pygame.draw.ellipse(janela, PURPLE, [380, 350, 190, 70])
    pygame.display.flip()




