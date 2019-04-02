import pygame

pygame.init()
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 

size = (400, 500)
screen = pygame.display.set_mode(size)
 

done = True
clock = pygame.time.Clock()
 

while done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
             done = False
 
    screen.fill(WHITE)

    clock.tick(60)

    update = pygame.display.flip()
 
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
 

    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
 
 

 
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
 

    font = pygame.font.SysFont('Calibri', 25, True, False)
 

    text = font.render("My text", True, BLACK)
 
    screen.blit(text, [250, 250])
 
 
    
 
    update
    
pygame.quit()

