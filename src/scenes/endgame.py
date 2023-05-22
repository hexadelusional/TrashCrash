import pygame

from core.Scene import Scene
from core.Mixer import main_mixer
pygame.font.init()

title_font = pygame.font.Font('assets/Grobold.ttf', 100)
text_font = pygame.font.Font('assets/Grobold.ttf', 24)
big_figures_font = pygame.font.Font('assets/digital.ttf', 60)
figures_font = pygame.font.Font('assets/digital.ttf', 24)

def on_enter(scene, data):
	main_mixer.play_music('endgame', 'assets/music/endgame.mp3')
	history = data['history']
	score1 = data['score1']
	score2 = data['score2']
	
	scene.bg = pygame.image.load('assets/ui/menu_background.png')
	
	title =  'Player 1 wins!' if score1 > score2 else 'Player 2 wins!' if score2 > score1 else 'It\'s a Draw!'
	scene.title = title_font.render(title, True, (255, 255, 255))
	scene.text = text_font.render('Press Enter to return to the main menu', True, (255, 255, 255))
	scene.scores = big_figures_font.render(f'{score1} • {score2}', True, (255, 255, 255))

	scene.right_text = text_font.render('Trash thrown in the right bins:', True, (255, 255, 255))
	scene.wrong_text = text_font.render('Trash thrown in the wrong bins:', True, (255, 255, 255))
	scene.ground_text = text_font.render('Trash thrown on the ground:', True, (255, 255, 255))
	scene.totle_text = text_font.render('Total:', True, (255, 255, 255))

	# Player 1
	right = wrong = ground = 0
	for item in history[0]:
		if item[1] == 'ground':
			ground += 1
		elif item[0].bin == item[1]:
			right += 1
		else:
			wrong += 1
	total = right + wrong + ground
	scene.right1 = figures_font.render(f'{right}', True, (255, 255, 255))
	scene.wrong1 = figures_font.render(f'{wrong}', True, (255, 255, 255))
	scene.ground1 = figures_font.render(f'{ground}', True, (255, 255, 255))
	scene.total1 = figures_font.render(f'{total}', True, (255, 255, 255))
	# Player 2
	right = wrong = ground = 0
	for item in history[1]:
		if item[1] == 'ground':
			ground += 1
		elif item[0].bin == item[1]:
			right += 1
		else:
			wrong += 1
	total = right + wrong + ground
	scene.right2 = figures_font.render(f'{right}', True, (255, 255, 255))
	scene.wrong2 = figures_font.render(f'{wrong}', True, (255, 255, 255))
	scene.ground2 = figures_font.render(f'{ground}', True, (255, 255, 255))
	scene.total2 = figures_font.render(f'{total}', True, (255, 255, 255))

def on_loop(scene, window):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
				scene.switcher.switch_to('main_menu')
				return
	
	window.blit(scene.bg, (0, 0))
	w = scene.title.get_width()
	window.blit(scene.title, (640 - w // 2, 150))
	w = scene.scores.get_width()
	window.blit(scene.scores, (640 - w // 2, 270))
	w = scene.text.get_width()
	window.blit(scene.text, (640 - w // 2, 340))

	window.blit(scene.right_text, (410, 420))
	window.blit(scene.wrong_text, (410, 460))
	window.blit(scene.ground_text, (410, 500))
	window.blit(scene.totle_text, (410, 540))

	window.blit(scene.right1, (800, 420))
	window.blit(scene.wrong1, (800, 460))
	window.blit(scene.ground1, (800, 500))
	window.blit(scene.total1, (800, 540))

	window.blit(scene.right2, (850, 420))
	window.blit(scene.wrong2, (850, 460))
	window.blit(scene.ground2, (850, 500))
	window.blit(scene.total2, (850, 540))

endgame_scene = Scene(on_enter, on_loop)