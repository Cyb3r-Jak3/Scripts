import pygame, sys
from pygame.locals import *

pygame.init()

winSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('Hello World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = winSurface.get_rect().centerx
textRect.centery = winSurface.get_rect().centery

winSurface.fill(WHITE)

pygame.draw.polygon(winSurface, GREEN, ((146, 0),(291, 106),(236, 277),(56, 277),(0, 106)))

pygame.draw.line(winSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(winSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(winSurface, BLUE, (60, 120), (120, 120), 4)

pygame.draw.circle(winSurface, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(winSurface, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(winSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

pixArray = pygame.PixelArray(winSurface)
pixArray[480][380] = BLACK
del pixArray

winSurface.blit(text, textRect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
