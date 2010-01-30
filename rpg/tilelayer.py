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
        tile_image = pyglet.image.load( tile_filename )

        # split image into list of images
        tile_region = tile_image.get_region(0,0, tile_image.width, tile_image.height)

        cols = tile_image.width / tile_width
        rows = tile_image.height / tile_height

        tile_sequence = pyglet.image.ImageGrid( tile_region, rows, cols, tile_width, tile_height).get_texture_sequence()

        max_tiles = len(tile_sequence) - 1

        # generate sprites for each tile
        for y in range(map_height):
            for x in range(map_width):
                # compensate flipped y-coordinate and get tile index
                tile = max_tiles - self.map[ y * map_width + x]
                # create sprite using one of the tile sequence images
                sprite = pyglet.sprite.Sprite( tile_sequence[tile], x*32, y*32)
                self.tiles.append( sprite )

    def draw(self):
        for tile in self.tiles:
            tile.draw()




