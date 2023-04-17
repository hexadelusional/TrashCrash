import pygame
import math

pygame.init()

class Arrow:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("arrow.png") # load the arrow image
        self.rect = self.image.get_rect() # get the rectangle of the image
        self.angle = 0 # set the initial angle to 0
        self.is_rotating = True # set the initial state of rotation to True

    def rotate(self):
        self.angle += 5 # increment the angle by 5 degrees
        self.image = pygame.transform.rotate(pygame.image.load("arrow.png"), self.angle) # rotate the image by the angle
        self.rect = self.image.get_rect(center=self.rect.center) # adjust the rectangle to the rotated image

    def draw(self):
        self.screen.blit(self.image, self.rect) # draw the arrow image on the screen

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h: # if the "h" key is pressed
                self.is_rotating = False # stop the rotation

# set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Arrow")

# create an arrow object
arrow = Arrow(screen)

# game loop
clock = pygame.time.Clock()
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        arrow.handle_events(event) # handle events for the arrow object

    # rotate and draw the arrow
    if arrow.is_rotating:
        arrow.rotate()
    arrow.draw()

    # update the screen
    pygame.display.update()

    # add a delay to the game loop
    clock.tick(60) # set the frame rate to 60 frames per second
