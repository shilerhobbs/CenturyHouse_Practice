import pathlib

import pygame as pg

import pytmx, pyscroll


# Start Pygame
pg.init()

# Start the screen
screen = pg.display.set_mode((640, 480))


char_image = pg.image.load('Assests/Adventurer-1.5/Individual Sprites/adventurer-idle-01.png')


running = True
while running:

    for event in pg.event.get():

        # The user closed the window!
        if event.type == pg.QUIT:

            # Stop running
            running = False

    # Logic goes here

    screen.blit(char_image, (20, 20))

    # Update Display

    pg.display.flip()


# Close the window
pg.quit()
