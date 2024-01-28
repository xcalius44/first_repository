import pygame
import sys

class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ship.bmp").convert()
        self.image.set_colorkey((230, 230, 230)) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("rocket")
background_color = (255, 255, 255)
rocket = Rocket(width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(background_color)
    screen.blit(rocket.image, rocket.rect)
    pygame.display.flip()
    