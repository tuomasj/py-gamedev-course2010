# tilelayer.py
import pyglet

class TileLayer():
    def __init__(self, map_filename, map_width, map_height,
                 tile_filename, tile_width, tile_height):

        self.map_width = map_width
        self.map_height = map_height
        self.tile_width = tile_width
        self.tile_height = tile_height
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
                tile = self.map[ y * map_width + x]
                # if tile is 0 (black), let's skip it
                if tile != 0:
                    # create sprite using one of the tile sequence images
                    # compensate flipped y-axis in tile index
                    sprite = pyglet.sprite.Sprite( tile_sequence[max_tiles-tile], 1.0 * x * self.tile_width, 1.0 * y * self.tile_height)
                    self.tiles.append( sprite )
        self.set_position(0,0)

    def draw(self):
        for tile in self.tiles:
            tile.draw()

    def set_position(self, pos_x, pos_y):
        tile_index = 0
        for y in range(self.map_height):
            for x in range(self.map_width):
                index = y * self.map_width + x
                # if tile is empty, skip it
                if self.map[ index ] == 0:
                    continue
                # set new position for sprite using separate index
                tile = self.tiles[ tile_index ]
                tile.x = 1.0 * x * self.tile_width + float(pos_x)
                tile.y = 1.0 * y * self.tile_height + float(pos_y)
                # increment the index which is used for tiles
                tile_index += 1

    def translate(self, dx, dy):
        for tile in self.tiles:
            tile.x += dx
            tile.y += dy





