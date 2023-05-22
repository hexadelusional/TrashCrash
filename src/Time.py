import pygame
import time

# Window size
WINDOW_SIZE = (1280, 720)

# backgrounds
mountains_1 = pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount1.png'), WINDOW_SIZE)
mountains_2 = pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount2.png'), WINDOW_SIZE)
mountains_3 = pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount3.png'), WINDOW_SIZE)
mountains_4 = pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount4.png'), WINDOW_SIZE)
mountains_5 = pygame.transform.scale(pygame.image.load('assets/images/fond_1/mount5.png'), WINDOW_SIZE)



### MAIN
pygame.init()
icon = pygame.image.load('assets/icon.png')
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Trash Crash')
pygame.display.set_icon(icon)
debug_font = pygame.font.SysFont('Arial', 20)

# Variables to manage the background change
background_delay = 36000# milliseconds
background_time  = 0    # when the background last changed
backgrounds = [mountains_1, mountains_2, mountains_3, mountains_4, mountains_5]
background_index = 0     # index of the currently used background

# Main loop
clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True

    # Re-draw the screen background from the list after a delay
    time_now = pygame.time.get_ticks()
    if ( time_now > background_time + background_delay ):
        # switch to the next background
        background_time = time_now
        background_index += 1
        # if we're out of backgrounds, start back at the head of the list
        if ( background_index >= len( backgrounds ) ):
            background_index = 0

    # Draw the background
    window.blit( backgrounds[background_index], (0, 0))
    print(background_index)
    pygame.display.flip()


    # Update the window, but not more than 60fps
    clock.tick_busy_loop( 60 )

pygame.quit()
