import pathlib

import pygame as pg

import pytmx, pyscroll


# Start Pygame
pg.init()

# Start the screen
screen = pg.display.set_mode((640,480))

running = True
while running:

    for event in pg.event.get():

        # The user closed the window!
        if event.type == pg.QUIT:

            # Stop running
            running = False

    # Logic goes here


# Close the window
pg.quit()