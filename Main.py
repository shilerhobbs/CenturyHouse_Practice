import pathlib

import pygame as pg

import pytmx, pyscroll


# Start Pygame
pg.init()

# Start the screen
screen = pg.display.set_mode((640, 480))


char_image = pg.image.load('Assests/Adventurer-1.5/Individual Sprites/adventurer-idle-01.png')
charX = 0
charY = 0




running = True
while running:

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:

            if event.key == 273:
                charY -= 2
                print("up")
            if event.key == 274:
                charY += 2
                print("down")
            if event.key == 275:
                charX += 2
                print("right")
            if event.key == 276:
                charX -= 2
                print("left")

        # The user closed the window!
        if event.type == pg.QUIT:

            # Stop running
            running = False

    # Logic goes here

    screen.fill((0, 0, 0))
    screen.blit(char_image, (charX, charY))

    # Update Display

    pg.display.flip()


# Close the window
pg.quit()
