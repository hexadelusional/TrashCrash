import pygame
#from PIL import Image



class Arrow():
    def __init__(self, x, y, player):
        super().__init__()
        self.value = 0
        self.direction = 4
        self.max_value = 100
        self.angle = 0
        self.player = player
        self.original_image = pygame.transform.scale(pygame.image.load('assets/images/arrow.png'), (80, 100))
        self.image = self.original_image
        self.rect = self.original_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_rotation_angle = 0

    def draw(self, screen, mirror):
        if mirror:
            image = pygame.transform.flip(self.image, True, False)
            screen.blit(image, (self.rect.x - int(self.image.get_width() / 2), self.rect.y - int(self.image.get_height() / 2)))
        else:
            screen.blit(self.image, (self.rect.x - int(self.image.get_width() / 2), self.rect.y - int(self.image.get_height() / 2)))

    def rotation(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if self.player == 1 and event.key == pygame.K_z or self.player == 2 and event.key == pygame.K_i:
                self.current_rotation_angle = 1 if event.type == pygame.KEYDOWN else 0
            if self.player == 1 and event.key == pygame.K_s or self.player == 2 and event.key == pygame.K_k:
                self.current_rotation_angle= -1 if event.type == pygame.KEYDOWN else 0
        self.angle += self.current_rotation_angle * 6
        if self.angle < 0:
            self.angle = 0
        if self.angle > 90:
            self.angle = 90
        self.image = pygame.transform.rotate(self.original_image, self.angle)


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

