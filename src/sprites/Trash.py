import pygame
from random import randint

trash_list = [
	{"name" : "Apple_core", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Apple_core.png'),(50,30))}, 
	{"name" : "Banana", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Banana.png'),(45,18)) },
	{"name" : "Box", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Box.png'),(50, 50)) },
	{"name" : "Bread", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Bread.png'),(44,25)) },
	{"name" : "Bulb", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Bulb.png'),(60,25)) },
	{"name" : "Can", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Can.png'),(20,50)) },
	{"name" : "Cig_Butt", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Cig_Butt.png'),(56,20) )},
	{"name" : "Glass_Bottle", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Glass_bottle.png'),(15,58)) },
	{"name" : "Glass", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Glass.png'),(35,50) )},
	{"name" : "Gum", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Gum.png'),(30,20)) },
	{"name" : "Jar", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Jar.png'),(32,50) )},
	{"name" : "Kiwi", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Kiwi.png'),(56,56) )},
	{"name" : "Laundry_bottle", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Laundry_Bottle.png'),(42,55)) },
	{"name" : "Lighter", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Lighter.png'),(16,54) )},
	{"name" : "Mask", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Mask.png'),(70,50) )},
	{"name" : "Mercury_battery", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Mercury_battery.png'),(60,30)) },
	{"name" : "Milk", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Milk.png'),(30,64) )},
	{"name" : "Mug", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Mug.png'), (40, 40))},
	{"name" : "Newspaper", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Newspaper.png'),(38,20)) },
	{"name" : "Oil_bottle", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Oil_Bottle.png'),(33,40)) },
	{"name" : "Orange", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Orange.png'),(32,24) )},
	{"name" : "Paint_Bomb", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Paint_Bomb.png'), (60, 20))},
	{"name" : "Papaya", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Papaya.png'),(42,26)) },
	{"name" : "Paper_Bag", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Paper_Bag.png'),(25,35)) },
	{"name" : "Perfume", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Perfume.png'),(48,52) )},
	{"name" : "Pizza_Box", "bin" : "blue", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Pizza_Box.png'),(40,25)) },
	{"name" : "Plastic_Bag", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Plastic_Bag.png'),(36,28)) },
	{"name" : "Plastic_Bottle", "bin" : "yellow", "img" : pygame.image.load('assets/images/Trash_PNG/Plastic_Bottle.png') },
	{"name" : "Plastic_cup", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Plastic_cup.png'),(46,30)) },
	{"name" : "Poly_Box", "bin" : "yellow", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Poly_Box.png'),(42,40)) },
	{"name" : "Raspberry", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Apple_core.png'),(44,48)) },
	{"name" : "Soda_can", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Soda_can.png'),(21,36)) },
	{"name" : "Watermelon", "bin" : "red", "img" : pygame.transform.scale(pygame.image.load('assets/images/Trash_PNG/Watermelon.png'),(33,34)) }

]

class Trash(pygame.sprite.Sprite):
    def __init__(self, window_width, trashes_left, trashes_right):
        super().__init__()
        val = randint(0,len(trash_list)-1)
        bounds = [(270, (window_width//2) - 10), ((window_width//2) + 10, window_width - 270)]
        if len(trashes_left) < 5 and len(trashes_right) < 5 :
            self.side = randint(0,1)
        elif len(trashes_left) < 5 :
            self.side = 0
        else : 
            self.side = 1 
        self.image = trash_list[val]["img"]
        self.rect = self.image.get_rect()
        self.bin = trash_list[val]["bin"]
        self.rect.x = randint(bounds[self.side][0], bounds[self.side][1])
        self.rect.y = 645 - self.rect.height
        

    def draw(self, window):
        window.blit(self.image, self.rect)