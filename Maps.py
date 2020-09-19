import pathlib

import pyscroll
from pytmx import load_pygame



class Map:

    def __init__(self, path):

        self.tmx_data = load_pygame(path)

        self.map_data = pyscroll.TiledMapData(self.tmx_data)

        for object in self.tmx_data.objects:
            # name, type, visisble, width, height, x, y, properties, rotation, parent, image
            print(object)

    def get_map(self):
        screen_size = (600, 300)
        map_layer = pyscroll.BufferedRenderer(self.map_data, screen_size)

        map_layer.zoom = 2.0

        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=4)

        return group


