import pathlib

import pygame as pg

import pytmx, pyscroll

# Start Pygame
pg.init()

import Maps

import Sprites



# Start the screen
screen = pg.display.set_mode((640, 480))

map = Maps.Map("Assests/Map/Test.tmx")

map_group = map.get_map()

char_image = pg.image.load('Assests/Adventurer-1.5/Individual Sprites/adventurer-idle-01.png')
char_x = 0
char_y = 0

player = Sprites.Player()

map_group(player)

clock = pg.time.Clock()
fps = 60
char_speed = 2

speed_x = 0

speed_y = 0

moving = False

running = True
while running:

    for event in pg.event.get():
        # The user closed the window!
        if event.type == pg.QUIT:
            # Stop running
            running = False

    # Logic goes here

    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
        player.rect.y -= char_speed

    if keys[pg.K_DOWN]:
        player.rect.y += char_speed

    if keys[pg.K_LEFT]:
        player.rect.x -= char_speed

    if keys[pg.K_RIGHT]:
        player.rect.x += char_speed

    print(pg.sprite.spritecollide(player, map.walls))

    # Update Display

    map.center(player.rect.center)

    map.draw(screen)
    screen.blit(char_image, (char_x, char_y))

    pg.display.flip()

    clock.tick(fps)

# Close the window
pg.quit()
