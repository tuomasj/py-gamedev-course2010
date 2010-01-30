# game.py

import statemachine
import tilelayer
import pyglet
import collision
from pyglet.window import key

PLAYER_SPEED = 70.0

class Player(pyglet.sprite.Sprite):

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

class GameState(statemachine.AbstractState):
    def start(self, sm):
        # init tilelayer
        self.layer = tilelayer.TileLayer(   'level1_20x15.map', 20, 15,
                                            'tiles.png', 32, 32)

        player_image = pyglet.image.load('player.png')
        self.player = Player(player_image, 2*32, 5*32)

    def stop(self):
        del( self.layer )

    def update(self, dt, keys):
        old_x = self.player.x
        old_y = self.player.y

        if keys[key.LEFT]:
            self.player.translate( dt * -PLAYER_SPEED, 0)
        if keys[key.RIGHT]:
            self.player.translate( dt * PLAYER_SPEED,0)
        if keys[key.DOWN]:
            self.player.translate( 0, dt * -PLAYER_SPEED)
        if keys[key.UP]:
            self.player.translate( 0, dt * PLAYER_SPEED)
        for tile in self.layer.tiles:
            if collision.check_collision(self.player, tile):
                # player collided with a tile, so let's use the old position
                self.player.x = old_x
                self.player.y = old_y
                break

    def draw(self):
        # draw tilelayer
        self.layer.draw()
        self.player.draw()


