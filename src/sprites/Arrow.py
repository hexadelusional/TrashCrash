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



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x - int(self.image.get_width() / 2), self.rect.y - int(self.image.get_height() / 2)))

    def rotation(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if self.player == 2 and event.key == pygame.K_z or self.player == 1 and event.key == pygame.K_i:
                self.angle += 6
            if self.player == 2 and event.key == pygame.K_s or self.player == 1 and event.key == pygame.K_k:
                self.angle -= 6
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

    """
    def rotation(self, x, y, screen):
        self.rect.x = x
        self.rect.y = y
        self.value += self.direction
        if self.value >= self.max_value:
            self.value = self.max_value
            self.direction *= -1
        elif self.value <= 0:
            self.value = 0
            self.direction *= -1
        angle = 0
        keys = pygame.key.get_pressed()
        if self.player == 1 and keys[pygame.K_z] or self.player == 2 and keys[pygame.K_i]:
            self.angle -= 2
        if self.player == 2 and keys[pygame.K_s] or self.player == 2 and keys[pygame.K_k]:
            self.angle += 2
        image = pygame.transform.rotate(self.image, angle)
        screen.blit(image, (x - int(image.get_width() / 2), y - int(image.get_height() / 2)))


"""

