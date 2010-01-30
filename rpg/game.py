# game.py

import statemachine
import tilelayer
import pyglet
import collision
from pyglet.window import key
import random

PLAYER_SPEED = 70.0

class Player(pyglet.sprite.Sprite):

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def check_collision(self, objs):
        for obj in objs:
            if collision.check_collision(self, obj):
                return True
        return False

class TinyMonster(Player):
    def update(self, dt):
        dir = random.randint(0,4)
        if dir == 0:
            # left
            self.translate( -10 * dt, 0)
        if dir == 1:
            # right
            self.translate( 10 * dt, 0)


class GameState(statemachine.AbstractState):
    def start(self, sm):
        # init tilelayer
        self.layer = tilelayer.TileLayer(   'level1_20x15.map', 20, 15,
                                            'tiles.png', 32, 32)

        player_image = pyglet.image.load('player.png')
        self.player = Player(player_image, 2*32, 5*32)

        self.monster = TinyMonster(player_image, 2*32, 9*32)

    def stop(self):
        del( self.layer )

    def update(self, dt, keys):
        self.monster.update(dt)
        self.update_player(dt, keys)

    def update_player(self, dt, keys):
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

        if self.player.check_collision(self.layer.tiles):
            # player collided with a tile, so let's use the old position
            self.player.x = old_x
            self.player.y = old_y

    def draw(self):
        # draw tilelayer
        self.layer.draw()
        self.player.draw()
        self.monster.draw()


