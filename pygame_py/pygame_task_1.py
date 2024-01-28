import pygame

import sys

pygame.init()

display = pygame.display.set_mode((1200, 800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill((0, 0, 255))
    pygame.display.flip()
    