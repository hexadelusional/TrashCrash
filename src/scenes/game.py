from functools import partial

import pygame

from core.Scene import Scene
from sprites.Bin import Bin
from sprites.Cloud import Cloud
from sprites.Floor import Floor
from sprites.Player import Player
from sprites.Projectile import Projectile
from sprites.Platform import Platform
from sprites.Score import Score
from sprites.Sky import Sky
from core.Sound import Sound
from sprites.Trash import Trash

WINDOW_SIZE = (1280, 720)
def on_enter(scene, settings):
	print('New game started')
	# Initialize game objects
	scene.bins = [
		# Left side
		Bin(0, 570, 'red'),
		Bin(78, 570, 'blue'),
		Bin(156, 570, 'yellow'),
		# Right side
		Bin(1030, 570, 'red'),
		Bin(1122, 570, 'blue'),
		Bin(1200, 570, 'yellow')
	]
	scene.score1 = Score(WINDOW_SIZE, 'left')
	scene.score2 = Score(WINDOW_SIZE, 'right')
	scene.music = Sound()
	
	scene.sky = Sky(WINDOW_SIZE)
	scene.clouds = [Cloud(WINDOW_SIZE)]
	scene.platforms = pygame.sprite.Group()
	scene.rock_list_left = []
	scene.rock_list_right = []
	scene.trashes_left = []
	scene.trashes_right = []
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
	scene.player_platforms = scene.platforms.copy()
	scene.player_platforms.add(scene.middle_bound)
	rock_plat1 = Platform(WINDOW_SIZE[0], 0, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat1)
	scene.rock_list_left.append(rock_plat1)
	rock_plat2 = Platform(WINDOW_SIZE[0], 1, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat2)
	scene.rock_list_right.append(rock_plat2)
	rock_plat3 = Platform(WINDOW_SIZE[0], 0, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat3)
	scene.rock_list_left.append(rock_plat3)
	rock_plat4 = Platform(WINDOW_SIZE[0], 1, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat4)
	scene.rock_list_right.append(rock_plat4)
	rock_plat5 = Platform(WINDOW_SIZE[0], 0, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat5)
	scene.rock_list_left.append(rock_plat5)
	rock_plat6 = Platform(WINDOW_SIZE[0], 1, scene.rock_list_left, scene.rock_list_right)
	scene.player_platforms.add(rock_plat6)
	scene.rock_list_right.append(rock_plat6)
	# Initialize players
	scene.player1 = Player(settings['p1'].name, 1, 200, 100)
	scene.player1_controls = {
		pygame.KEYDOWN: {
			pygame.K_a: partial(scene.player1.move, scene.player_platforms, 'left'),
			pygame.K_d: partial(scene.player1.move, scene.player_platforms, 'right'),
			pygame.K_w: partial(scene.player1.jump, scene.player_platforms),
			pygame.K_e: partial(scene.player1.throw, scene.player_platforms)
		},
		pygame.KEYUP: {
			pygame.K_a: partial(scene.player1.stop, 'left'),
			pygame.K_d: partial(scene.player1.stop, 'right')
		}
	}

	scene.player2 = Player(settings['p2'].name, 2, 700, 100)
	scene.player2_controls = {
		pygame.KEYDOWN: {
			pygame.K_j: partial(scene.player2.move, scene.player_platforms, 'left'),
			pygame.K_l: partial(scene.player2.move, scene.player_platforms, 'right'),
			pygame.K_i: partial(scene.player2.jump, scene.player_platforms),
			pygame.K_o: partial(scene.player2.throw, scene.player_platforms)
		},
		pygame.KEYUP: {
			pygame.K_j: partial(scene.player2.stop, 'left'),
			pygame.K_l: partial(scene.player2.stop, 'right')
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
	scene.sky.draw(window)
	if scene.framecount % 240 == 0:
		scene.clouds.append(Cloud(WINDOW_SIZE))
	for cloud in scene.clouds:
		cloud.update()
		cloud.draw(window)
		if cloud.rect.right < 0:
			scene.clouds.remove(cloud)
	Projectile.instances.update(scene.platforms)
	for rock_plat in scene.rock_list_left + scene.rock_list_right:
		rock_plat.draw(window)
	if scene.framecount % 50 == 0 :
		if len(scene.trashes_left) < 5 or len(scene.trashes_right) < 5 :
			trash = Trash(WINDOW_SIZE[0], scene.trashes_left, scene.trashes_right)
			if not(trash.side) :
				scene.trashes_left.append(trash)
			else :
				scene.trashes_right.append(trash)
	for trash in scene.trashes_left + scene.trashes_right :
		trash.draw(window)


	# Update the game state
	scene.player1.update(scene.player_platforms)
	scene.player2.update(scene.player_platforms)
	# Draw game objects
	window.blit(scene.floor.image, scene.floor.rect)
	for bin in scene.bins:
		bin.draw(window)
	scene.player1.draw(window)
	scene.player2.draw(window)
	Projectile.instances.draw(window)
	

	scene.score1.draw(window)
	scene.score2.draw(window)

game_scene = Scene(on_enter, loop)