from random import randint
import pygame


class Bin (pygame.sprite.Sprite) :
    def __init__(self,x,y,width,height) :
        super().__init__()
        #self.image = pygame.image.load(f'assets/images/bins/{randint(0,2)}.png')
        self.image = pygame.image.load('assets/images/bins/redbin.png')
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.width = width
        self.rect.height = height
        '''
        scaled_image=pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.image.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))
        '''
        
        
    def draw(self, window):
        scaled_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        #window.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))
        window.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))
        
    def update(self):
	    self.image.blit(self.image_asset, (self.x, 0))
        
        #self.rect=pygame.Rect(3,548,90,90)
        #self.rect = pygame.Rect(x, y, 64, 64)
		#self.image = pygame.Surface(Player.SPRITE_SIZE)
  
'''def draw(self, window):
        scaled_image=pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        #window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(scaled_image, self.rect, (0, 0, self.rect.width, self.rect.height))
        '''