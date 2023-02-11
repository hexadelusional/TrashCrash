import pygame 
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
    
    pygame.display.update()
    clock.tick(60) #60 frames per second