import sys

import pygame
from functools import partial
from sprites.Cloud import Cloud
from sprites.Floor import Floor
from sprites.Gauge import Gauge

from sprites.Player import Player
from sprites.FpsDebugger import FpsDebugger
from sprites.Projectile import Projectile
from sprites.Sky import Sky
from sprites.Bin import Bin



# Initialize game window
mainClock = pygame.time.Clock()
pygame.init()
WINDOW_SIZE = (1280, 720)
icon = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Trash Crash')
pygame.display.set_icon(icon)
debug_font = pygame.font.SysFont('Arial', 20)

# Initialize game objects
bin1 = pygame.sprite.Sprite()
bin1 = Bin(0, 550, 110, 110, pygame.image.load('assets/images/bins/redbin.png'))
bin1.rect = pygame.Rect(bin1)
bin2 = pygame.sprite.Sprite()
bin2 = Bin(100, 550, 100, 110, pygame.image.load('assets/images/bins/bluebin.png'))
bin2.rect = pygame.Rect(bin2)
bin3 = pygame.sprite.Sprite()
bin3 = Bin(175, 550, 125, 118, pygame.image.load('assets/images/bins/yellowbin.png'))
bin3.rect = pygame.Rect(bin3)
bin4 = pygame.sprite.Sprite()
bin4 = Bin(955, 550, 125, 118, pygame.image.load('assets/images/bins/yellowbin.png'))
bin4.rect = pygame.Rect(bin4)
bin5 = pygame.sprite.Sprite()
bin5 = Bin(1078, 550, 100, 110, pygame.image.load('assets/images/bins/bluebin.png'))
bin5.rect = pygame.Rect(bin5)
bin6 = pygame.sprite.Sprite()
bin6 = Bin(1175, 550, 110, 110, pygame.image.load('assets/images/bins/redbin.png'))
bin6.rect = pygame.Rect(bin6)

sky = Sky(WINDOW_SIZE)
clouds = [Cloud(WINDOW_SIZE)]
platforms = pygame.sprite.Group()
floor = Floor(75, WINDOW_SIZE)
left_bound = pygame.sprite.Sprite()
left_bound.rect = pygame.Rect(-100, 0, 100, WINDOW_SIZE[1])
right_bound = pygame.sprite.Sprite()
right_bound.rect = pygame.Rect(WINDOW_SIZE[0], 0, 100, WINDOW_SIZE[1])
middle_bound = pygame.sprite.Sprite()
middle_bound.rect = pygame.Rect(WINDOW_SIZE[0] / 2 - 5, 0, 10, WINDOW_SIZE[1])

test_platform = pygame.sprite.Sprite()
test_platform.rect = pygame.Rect(150, 400, 400, 15)
test_platform.image = pygame.image.load('assets/images/dark_platform.png')

platforms.add(test_platform)
platforms.add(left_bound)
platforms.add(right_bound)
platforms.add(floor)
platforms.add(bin1)
platforms.add(bin2)
platforms.add(bin3)
platforms.add(bin4)
platforms.add(bin5)
platforms.add(bin6)
player_platforms = platforms.copy()
player_platforms.add(middle_bound)

# Initialize players
player1 = Player('pink', 1, 700, 100)
player1_controls = {
    pygame.KEYDOWN: {
        pygame.K_j: partial(player1.move, platforms, 'left'),
        pygame.K_l: partial(player1.move, platforms, 'right'),
        pygame.K_i: partial(player1.jump, platforms),
        pygame.K_o: partial(player1.throw, platforms)
    },
    pygame.KEYUP: {
        pygame.K_j: partial(player1.stop, 'left'),
        pygame.K_l: partial(player1.stop, 'right')
    }
}
player2 = Player('white', 2, 200, 100)
player2_controls = {
    pygame.KEYDOWN: {
        pygame.K_a: partial(player2.move, platforms, 'left'),
        pygame.K_d: partial(player2.move, platforms, 'right'),
        pygame.K_w: partial(player2.jump, platforms),
        pygame.K_e: partial(player2.throw, platforms)
    },
    pygame.KEYUP: {
        pygame.K_a: partial(player2.stop, 'left'),
        pygame.K_d: partial(player2.stop, 'right')
    }
}

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

        if event.type in player1_controls:
            if event.key in player1_controls[event.type]:
                player1_controls[event.type][event.key]()
        if event.type in player2_controls:
            if event.key in player2_controls[event.type]:
                player2_controls[event.type][event.key]()
        player1.arrow.rotation(event, window)
        player2.arrow.rotation(event, window)

    # Clear the screen
    window.fill((173,216,230))

    # Secondary updates
    # sky.update()
    sky.draw(window)
    if framecount % 240 == 0:
        clouds.append(Cloud(WINDOW_SIZE))
    for cloud in clouds:
        cloud.update()
        cloud.draw(window)
        if cloud.rect.right < 0:
            clouds.remove(cloud)
    Projectile.instances.update(platforms)
    # Update the game state
    player1.update(player_platforms)
    player2.update(player_platforms)
    fps_debugger.update(clock)
    # Draw game objects
    window.blit(test_platform.image, test_platform.rect)
    player1.draw(window)
    player2.draw(window)
    Projectile.instances.draw(window)
    window.blit(floor.image, floor.rect)
    fps_debugger.draw(window)

    bin1.draw(window)
    bin2.draw(window)
    bin3.draw(window)
    bin4.draw(window)
    bin5.draw(window)
    bin6.draw(window)



    #the arrow
    """
    img = pygame.image.load('assets/images/arrow.png')

    angle = 0

    mx, my = 200, 200
    keys = pygame.key.get_pressed()
    if player1.id == 1 and keys[pygame.K_z] or player2.id == 2 and keys[pygame.K_i]:
        angle += 6
    if player1.id == 1 and keys[pygame.K_s] or player2.id == 2 and keys[pygame.K_k]:
        angle -= 6
    img_copy = pygame.transform.rotate(img, angle)
    window.blit(img_copy, (mx - int(img_copy.get_width() / 2), my - int(img_copy.get_height() / 2)))
    pygame.display.update()
    mainClock.tick(60)
    """


    # Flip the display
    pygame.display.flip()


pygame.quit()