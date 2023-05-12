from functools import partial
from random import randint

import pygame

from core.Scene import Scene
from sprites.Bin import Bin
from sprites.Cloud import Cloud
from sprites.Floor import Floor
from sprites.Player import Player
from sprites.Projectile import Projectile
from sprites.RockPlat import MyRockPlatform
from sprites.Sky import Sky

WINDOW_SIZE = (1280, 720)
def on_enter(scene, settings):
	print('New game started')
	# Initialize game objects
	scene.bin1 = Bin(0, 550, 110, 110, pygame.image.load('assets/images/bins/redbin.png'))
	scene.bin1.rect = pygame.Rect(scene.bin1)
	scene.bin2 = Bin(100, 550, 100, 110, pygame.image.load('assets/images/bins/bluebin.png'))
	scene.bin2.rect = pygame.Rect(scene.bin2)
	scene.bin3 = Bin(175, 550, 125, 118, pygame.image.load('assets/images/bins/yellowbin.png'))
	scene.bin3.rect = pygame.Rect(scene.bin3)
	scene.bin4 = Bin(955, 550, 125, 118, pygame.image.load('assets/images/bins/yellowbin.png'))
	scene.bin4.rect = pygame.Rect(scene.bin4)
	scene.bin5 = Bin(1078, 550, 100, 110, pygame.image.load('assets/images/bins/bluebin.png'))
	scene.bin5.rect = pygame.Rect(scene.bin5)
	scene.bin6 = Bin(1175, 550, 110, 110, pygame.image.load('assets/images/bins/redbin.png'))
	scene.bin6.rect = pygame.Rect(scene.bin6)

	scene.sky = Sky(WINDOW_SIZE)
	scene.clouds = [Cloud(WINDOW_SIZE)]
	scene.platforms = pygame.sprite.Group()
	scene.rock_list = []
	scene.floor = Floor(75, WINDOW_SIZE)
	scene.left_bound = pygame.sprite.Sprite()
	scene.left_bound.rect = pygame.Rect(-100, 0, 100, WINDOW_SIZE[1])
	scene.right_bound = pygame.sprite.Sprite()
	scene.right_bound.rect = pygame.Rect(WINDOW_SIZE[0], 0, 100, WINDOW_SIZE[1])
	scene.middle_bound = pygame.sprite.Sprite()
	scene.middle_bound.rect = pygame.Rect(WINDOW_SIZE[0] / 2 - 5, 0, 10, WINDOW_SIZE[1])

	scene.platforms.add(scene.left_bound)
	scene.platforms.add(scene.right_bound)
	scene.platforms.add(scene.floor)
	scene.platforms.add(scene.bin1)
	scene.platforms.add(scene.bin2)
	scene.platforms.add(scene.bin3)
	scene.platforms.add(scene.bin4)
	scene.platforms.add(scene.bin5)
	scene.platforms.add(scene.bin6)
	scene.player_platforms = scene.platforms.copy()
	scene.player_platforms.add(scene.middle_bound)
	# Initialize players
	scene.player1 = Player('pink', 1, 700, 100)
	scene.player1_controls = {
		pygame.KEYDOWN: {
			pygame.K_j: partial(scene.player1.move, scene.platforms, 'left'),
			pygame.K_l: partial(scene.player1.move, scene.platforms, 'right'),
			pygame.K_i: partial(scene.player1.jump, scene.platforms),
			pygame.K_o: partial(scene.player1.throw, scene.platforms)
		},
		pygame.KEYUP: {
			pygame.K_j: partial(scene.player1.stop, 'left'),
			pygame.K_l: partial(scene.player1.stop, 'right')
		}
	}
	scene.player2 = Player('white', 2, 200, 100)
	scene.player2_controls = {
		pygame.KEYDOWN: {
			pygame.K_a: partial(scene.player2.move, scene.platforms, 'left'),
			pygame.K_d: partial(scene.player2.move, scene.platforms, 'right'),
			pygame.K_w: partial(scene.player2.jump, scene.platforms),
			pygame.K_e: partial(scene.player2.throw, scene.platforms)
		},
		pygame.KEYUP: {
			pygame.K_a: partial(scene.player2.stop, 'left'),
			pygame.K_d: partial(scene.player2.stop, 'right')
		}
	}
	scene.framecount = 0

def loop(scene, window):
	# Clear the screen
	window.fill((173, 216, 230))

	scene.framecount += 1
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pass
		if event.type in scene.player1_controls:
			if event.key in scene.player1_controls[event.type]:
				scene.player1_controls[event.type][event.key]()
		if event.type in scene.player2_controls:
			if event.key in scene.player2_controls[event.type]:
				scene.player2_controls[event.type][event.key]()
		scene.player1.arrow.rotation(event)
		scene.player2.arrow.rotation(event)

	# Secondary updates
	#sky.update()
	scene.sky.draw(window)
	if scene.framecount % 240 == 0:
		scene.clouds.append(Cloud(WINDOW_SIZE))
	for cloud in scene.clouds:
		cloud.update()
		cloud.draw(window)
		if cloud.rect.right < 0:
			scene.clouds.remove(cloud)
	Projectile.instances.update(scene.platforms)
	if scene.framecount % 280 == 0 :
		if len(scene.rock_list) < 5 :
			val = randint(0,1)
			x = [WINDOW_SIZE[0],0][val]
			y = randint(350, 600)
			dir = [-1,1][val]
			width = randint(200,250)
			plat_img = pygame.image.load('assets/images/rock_platforms/1.png')
			rock_plat = MyRockPlatform(plat_img, dir, x, y, width)
			scene.player_platforms.add(rock_plat)
			scene.rock_list.append(rock_plat)
	for rock_plat in scene.rock_list :
		rock_plat.update(WINDOW_SIZE[0])
		rock_plat.draw(window)

	# Update the game state
	scene.player1.update(scene.player_platforms)
	scene.player2.update(scene.player_platforms)
	# Draw game objects
	scene.player1.draw(window)
	scene.player2.draw(window)
	Projectile.instances.draw(window)
	window.blit(scene.floor.image, scene.floor.rect)
	scene.bin1.draw(window)
	scene.bin2.draw(window)
	scene.bin3.draw(window)
	scene.bin4.draw(window)
	scene.bin5.draw(window)
	scene.bin6.draw(window)

game_scene = Scene(on_enter, loop)