import pygame
pygame.init()

#window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 80
SEPARATION_SIZE = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Trash Crash by CAMPIfeur')

#background
sky = pygame.image.load('fond_1/sky1.png')
mountains = pygame.image.load('fond_1/mount1.png')
sky = pygame.transform.scale(sky,(1280,720))
mountains = pygame.transform.scale(mountains,(1280,720))
#sky = sky.convert()
#mountains = mountains.convert()

pos1 = 10
pos2 = SCREEN_WIDTH - PLAYER_WIDTH - 10
dir1 = 0
dir2 = 0

playing = True
while playing:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		if event.type in [pygame.KEYUP, pygame.KEYDOWN]:
			n = 1 if event.type == pygame.KEYDOWN else -1
			match (event.key):
				case pygame.K_q:
					dir1 -= n
				case pygame.K_d:
					dir1 += n
				case pygame.K_j:
					dir2 -= n
				case pygame.K_l:
					dir2 += n

	screen.blit(sky,(0,0)) #blit means block image transfer
	screen.blit(mountains, (0,0))

	pos1 += dir1
	pos2 += dir2
	left_limit = SCREEN_WIDTH / 2 - SEPARATION_SIZE / 2
	right_limit = SCREEN_WIDTH / 2 + SEPARATION_SIZE / 2
	if (pos1 <= 0):
		pos1 = 0
	if (pos1 + PLAYER_WIDTH >= left_limit):
		pos1 = left_limit - PLAYER_WIDTH
	if (pos2 <= right_limit):
		pos2 = right_limit
	if (pos2 + PLAYER_WIDTH >= SCREEN_WIDTH):
		pos2 = SCREEN_WIDTH - PLAYER_WIDTH

	player1 = pygame.Rect(pos1, 720 - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
	player2 = pygame.Rect(pos2, 720 - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

	separation = pygame.Rect(SCREEN_WIDTH/2 - SEPARATION_SIZE / 2, 0, SEPARATION_SIZE, SCREEN_HEIGHT)

	pygame.draw.rect(screen, (255, 0, 0), player1)
	pygame.draw.rect(screen, (0, 0, 255), player2)
	pygame.draw.rect(screen, (0,255,0), separation)

	pygame.display.flip()


pygame.quit()
