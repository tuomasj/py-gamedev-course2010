# player.py
import pyglet.sprite

PLAYER_SPEED = 40

class Player(pyglet.sprite.Sprite):

    def move_left(self, dt):
        self.x -= PLAYER_SPEED * dt

    def move_right(self, dt):
        self.x += PLAYER_SPEED * dt


