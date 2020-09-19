import pathlib

import pygame as pg

import pytmx, pyscroll


# Start Pygame
pg.init()

# Start the screen
screen = pg.display.set_mode((640, 480))


char_image = pg.image.load('Assests/Adventurer-1.5/Individual Sprites/adventurer-idle-01.png')
char_x = 0
char_y = 0


char_speed = 2

speed_x = 0

speed_y = 0

moving = False



running = True
while running:

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:

            if event.key == 273:
                speed_y -= char_speed
                print("up")
            elif event.key == 274:
                speed_y += char_speed
                print("down")
            else:
                speed_y = 0

            if event.key == 275:
                speed_x += char_speed
                print("right")
            elif event.key == 276:
                speed_x -= char_speed
                print("left")
            else:
                speed_x = 0

        # The user closed the window!
        if event.type == pg.QUIT:

            # Stop running
            running = False

    # Logic goes here

    screen.fill((0, 0, 0))


    char_x += speed_x
    char_y += speed_y
    screen.blit(char_image, (char_x, char_y))

    # Update Display

    pg.display.flip()


# Close the window
pg.quit()
