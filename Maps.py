import pathlib

import pyscroll
from pytmx import load_pygame
from Sprites import Wall


class Map:

    def __init__(self, path):

        self.tmx_data = load_pygame(path)

        self.map_data = pyscroll.TiledMapData(self.tmx_data)
        self.walls = []
        for object in self.tmx_data.objects:
            # name, type, visible, width, height, x, y, properties, rotation, parent, image
            print(object)

            if object.name == "wall":
                wall = Wall(object.x, object.y, object.width, object.height)
                self.walls.append(wall)

    def get_map(self):
        screen_size = (640, 480)
        map_layer = pyscroll.BufferedRenderer(self.map_data, screen_size)

        map_layer.zoom = 1.0

        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)

        return group



