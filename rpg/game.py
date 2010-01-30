# game.py

import statemachine
import tilelayer
import pyglet

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
        self.player = Player(player_image, 0,0)


    def stop(self):
        del( self.layer )

    def update(self, dt, keys):
        if keys[key.LEFT]:
            self.player.translate( dt * -PLAYER_SPEED, 0)
        if keys[key.RIGHT]:
            self.player.translate( dt * PLAYER_SPEED,0)
        if keys[key.DOWN]:
            self.player.translate( 0, dt * -PLAYER_SPEED)
        if keys[key.UP]:
            self.player.translate( 0, dt * PLAYER_SPEED)


    def draw(self):
        # draw tilelayer
        self.layer.draw()
        self.player.draw()


