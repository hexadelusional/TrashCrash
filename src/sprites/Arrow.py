import pygame
from PIL import Image



class Arrow():
    def __init__(self, x, y, player):
        self.value = 0
        self.direction = 4
        self.max_value = 100
        self.rect = pygame.Rect(x, y, 80, 100)
        self.player = player
        self.image = pygame.image.load('assets/images/arrow.png')
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.angle = 0
        self.is_rotating = True



    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_rotation(self, event):
        if event.type == pygame.KEYDOWN:
            if self.player == 1 and event.key == pygame.K_z or self.player == 2 and event.key == pygame.K_i:
                self.angle -= 2
            if self.player == 2 and event.key == pygame.K_s or self.player == 2 and event.key == pygame.K_k:
                self.angle += 2




            orig_rect = self.rect
            rot_image = pygame.transform.rotate(self.image, self.angle)
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()
            self.image = rot_image
            self.rect = rot_rect





    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.value += self.direction
        if self.value >= self.max_value:
            self.value = self.max_value
            self.direction *= -1
        elif self.value <= 0:
            self.value = 0
            self.direction *= -1



