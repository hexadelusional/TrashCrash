from functools import partial

import pygame

from core.Mixer import main_mixer
from core.Scene import Scene
from sprites.Bin import Bin
from sprites.Cloud import Cloud
from sprites.Floor import Floor
from sprites.Platform import Platform
from sprites.Player import Player
from sprites.Projectile import Projectile
from sprites.Score import Score
from sprites.Sky import Sky
from sprites.Timer import Timer
from sprites.Trash import Trash
from ui.Button import Button

WINDOW_SIZE = (1280, 720)
def on_enter(scene, settings):
	# Initialize game objects
	scene.bins = [
		# Left side
		Bin(0, 570, 'red', 2),
		Bin(78, 570, 'blue', 2),
		Bin(156, 570, 'yellow', 2),
		# Right side
		Bin(1030, 570, 'red', 1),
		Bin(1122, 570, 'blue', 1),
		Bin(1200, 570, 'yellow', 1)
	]
	scene.history = [
		# Format : [(trash, bin type / ground), ...]
		# Allows us to compile at the end how many trash ended-up in the right bin, wrong bin, or on the ground, for each player.
		[], # Player 1
		[] # Player 2
	]
	scene.paused = False
	scene.timer = Timer(180)
	scene.trash_group = pygame.sprite.Group()
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
			pygame.K_q: partial(scene.player1.move, scene.player_platforms, 'left'),
			pygame.K_d: partial(scene.player1.move, scene.player_platforms, 'right'),
			pygame.K_z: partial(scene.player1.jump, scene.player_platforms),
			pygame.K_e: partial(scene.player1.throw, scene.player_platforms),
		},
		pygame.KEYUP: {
			pygame.K_q: partial(scene.player1.stop, 'left'),
			pygame.K_d: partial(scene.player1.stop, 'right')
		}
	}

	scene.player2 = Player(settings['p2'].name, 2, 700, 100)
	scene.player2_controls = {
		pygame.KEYDOWN: {
			pygame.K_j: partial(scene.player2.move, scene.player_platforms, 'left'),
			pygame.K_l: partial(scene.player2.move, scene.player_platforms, 'right'),
			pygame.K_i: partial(scene.player2.jump, scene.player_platforms),
			pygame.K_o: partial(scene.player2.throw, scene.player_platforms),
		},
		pygame.KEYUP: {
			pygame.K_j: partial(scene.player2.stop, 'left'),
			pygame.K_l: partial(scene.player2.stop, 'right')
		}
	}

	scene.pause_dim = pygame.Surface(WINDOW_SIZE)
	scene.pause_dim.fill((0, 0, 0))
	scene.pause_dim.set_alpha(100)
	scene.pause_font = pygame.font.Font('assets/Grobold.ttf', 50)
	scene.pause_title = scene.pause_font.render('Paused!', True, (255, 255, 255))
	def unpause(): scene.paused = False
	scene.pause_resume = Button(490, 300, 'Resume', unpause, width=300, font_size=32)
	scene.pause_quit = Button(490, 400, 'Quit', partial(scene.switcher.switch_to, 'main_menu'), width=300, font_size=32)

	scene.framecount = 0
	main_mixer.play_music('ingame', 'assets/music/ingame.mp3', 1000)

def loop(scene, window):
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pass
		if not scene.paused:
			if event.type in scene.player1_controls:
				if event.key in scene.player1_controls[event.type]:
					scene.player1_controls[event.type][event.key]()
			if event.type in scene.player2_controls:
				if event.key in scene.player2_controls[event.type]:
					scene.player2_controls[event.type][event.key]()
			scene.player1.arrow.rotation(event)
			scene.player2.arrow.rotation(event)
		else:
			scene.pause_resume.update(event)
			scene.pause_quit.update(event)
		if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_p):
			scene.paused = not scene.paused

	# UPDATES
	if scene.paused:
		main_mixer.set_volume(0.3)
	else:
		main_mixer.set_volume(1)
		scene.framecount += 1
		if scene.framecount % 60 == 0:
			scene.timer.update()
			if scene.timer.seconds <= 0:
				scene.switcher.switch_to('endgame', {
					'history': scene.history,
					'score1': scene.player1.score.value,
					'score2': scene.player2.score.value
				})
		if scene.framecount % 240 == 0:
			scene.clouds.append(Cloud(WINDOW_SIZE))
		for cloud in scene.clouds:
			cloud.update()
			cloud.draw(window)
			if cloud.rect.right < 0:
				scene.clouds.remove(cloud)
		Projectile.instances.update(scene.platforms, scene.bins, [scene.player1, scene.player2], scene.history)
		if scene.framecount % 50 == 0 :
			if len(scene.trashes_left) < 5 or len(scene.trashes_right) < 5 :
				trash = Trash(WINDOW_SIZE[0], scene.trashes_left, scene.trashes_right)
				scene.trash_group.add(trash)
				if not(trash.side):
					scene.trashes_left.append(trash)
				else:
					scene.trashes_right.append(trash)
		trash_collision_left =  pygame.sprite.spritecollide(scene.player1, scene.trash_group, False)
		for trash in trash_collision_left :
			scene.player1.pick_trash(trash, scene.trashes_left, scene.trash_group)
		trash_collision_right = pygame.sprite.spritecollide(scene.player2, scene.trash_group, False)
		for trash in trash_collision_right :
			scene.player2.pick_trash(trash,scene.trashes_right, scene.trash_group)
		scene.player1.update(scene.player_platforms)
		scene.player2.update(scene.player_platforms)

	# DRAWING
	window.fill((173, 216, 230))
	scene.sky.draw(window)
	for cloud in scene.clouds:
		cloud.draw(window)
	for rock_plat in scene.rock_list_left + scene.rock_list_right:
		rock_plat.draw(window)
	scene.trash_group.draw(window)
	window.blit(scene.floor.image, scene.floor.rect)
	for bin in scene.bins:
		bin.draw(window)
	scene.player1.draw(window)
	scene.player2.draw(window)
	scene.player1.draw_inventory(window)
	scene.player2.draw_inventory(window)
	scene.player1.score.draw(window)
	scene.player2.score.draw(window)
	Projectile.instances.draw(window)
	scene.timer.draw(window)
	if scene.paused:
		window.blit(scene.pause_dim, (0, 0))
		window.blit(scene.pause_title, (640 - scene.pause_title.get_width() // 2, 200))
		scene.pause_resume.draw(window)
		scene.pause_quit.draw(window)
	
game_scene = Scene(on_enter, loop)