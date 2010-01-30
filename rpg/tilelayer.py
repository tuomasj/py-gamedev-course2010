# tilelayer.py
import pyglet

class TileLayer():
    def __init__(self, map_filename, map_width, map_height,
                 tile_filename, tile_width, tile_height):

        # generate datas structure
        self.map = []
        self.tiles = []

        # load map data
        f = open(map_filename, 'rb')
        for i in range(map_width * map_height):
            tile = ord( f.read(1) )
            self.map.append( tile )
        f.close()

        # load tile image

        # split image into list of images

        # generate sprites for each tile
        for y in range(map_height):
            for x in range(map_width):
                tile = self.map[ y * map_width + x]
                label = pyglet.text.Label(  text = str(tile),
                                            x = x*tile_width,
                                            y = y*tile_height)
                self.tiles.append( label )

    def draw(self):
        for tile in self.tiles:
            tile.draw()




