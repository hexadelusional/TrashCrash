import pygame
from sprites.Cloud import Cloud
from sprites.Floor import Floor

from sprites.Player import Player
from sprites.FpsDebugger import FpsDebugger
from sprites.Sky import Sky

pygame.init()

WINDOW_SIZE = (1280, 720)
icon = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Trash Crash')
pygame.display.set_icon(icon)
debug_font = pygame.font.SysFont('Arial', 20)

colliding = pygame.sprite.Group()
clouds = [Cloud(WINDOW_SIZE)]
sky = Sky(WINDOW_SIZE)

player1 = Player(700, 100)
player2 = Player(200, 100)
floor = Floor(75, WINDOW_SIZE)
left_bound = pygame.sprite.Sprite()
left_bound.rect = pygame.Rect(-100, 0, 100, WINDOW_SIZE[1])
right_bound = pygame.sprite.Sprite()
right_bound.rect = pygame.Rect(WINDOW_SIZE[0], 0, 100, WINDOW_SIZE[1])
colliding.add(left_bound)
colliding.add(right_bound)
colliding.add(player1)
colliding.add(floor)

clock = pygame.time.Clock()
fps_debugger = FpsDebugger()

# Game loop
running = True
framecount = 0
while running:
	framecount += 1
	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player1.move_right()

			if event.key == pygame.K_UP:
				player1.jump(colliding)

			if event.key == pygame.K_LEFT:
				player1.move_left()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT and player1.vel_x > 0:
				player1.stop()
			if event.key == pygame.K_LEFT and player1.vel_x < 0:
				player1.stop()

	# Clear the screen
	window.fill((0, 255, 0))

	# Secondary updates
	sky.update()
	sky.draw(window)
	if framecount % 240 == 0:
		clouds.append(Cloud(WINDOW_SIZE))
	for cloud in clouds:
		cloud.update()
		cloud.draw(window)
		if cloud.rect.right < 0:
			clouds.remove(cloud)
	# Update the game state
	player1.update(colliding)
	player2.update(colliding)
	fps_debugger.update(clock)
	# Draw game objects
	player1.draw(window)
	player2.draw(window)
	window.blit(floor.image, floor.rect)
	fps_debugger.draw(window)
	# Flip the display
	pygame.display.flip()
	# Limit the frame rate
	clock.tick(60)

pygame.quit()
