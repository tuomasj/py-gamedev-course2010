# game.py

import statemachine
import tilelayer
import pyglet
import collision
from pyglet.window import key
import random

import states

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

    def __init__(self, image, x, y):
        Player.__init__(self, image, x, y)
        self.randomize_direction()
        self.speed = 50.0
        self.timer = 0

    def update(self, dt, tiles):
        self.timer -= dt
        if self.timer < 0:
            self.randomize_direction()
        else:
            self.move_monster(dt, tiles)

    def randomize_direction(self):
        self.direction = random.randint(0,3)
        self.timer = random.random() + 0.5

    def move_monster(self, dt, tiles):
        old_x = self.x
        old_y = self.y
        if self.direction == 0:
            # left
            self.translate( -self.speed * dt, 0)
        if self.direction == 1:
            # right
            self.translate( self.speed * dt, 0)
        if self.direction == 2:
            # up
            self.translate( 0, self.speed * dt)
        if self.direction == 3:
            # down
            self.translate( 0, -self.speed * dt)
        if self.check_collision( tiles ):
            self.x = old_x
            self.y = old_y
            self.randomize_direction()

class GameState(statemachine.AbstractState):
    def start(self, sm):

        # put statemachine into class-variable for later use
        self.sm = sm

        # init tilelayer
        self.layer = tilelayer.TileLayer(   'level1_20x15.map', 20, 15,
                                            'tiles.png', 32, 32)

        # init level goal
        goal_image = pyglet.image.load('goal.png')
        self.goal = pyglet.sprite.Sprite(goal_image, 18*32, 7*32)

        # init player
        player_image = pyglet.image.load('player.png')
        self.player = Player(player_image, 2*32, 5*32)

        # init monsters
        self.monsters = []
        for i in range(5):
            self.monsters.append( TinyMonster(player_image, 18*32, 7*32) )

    def stop(self):
        del( self.layer )
        del( self.player )
        del( self.goal )
        del( self.monsters )

    def update(self, dt, keys):
        # update all monsters
        for monster in self.monsters:
            monster.update(dt, self.layer.tiles)

        # update player
        self.update_player(dt, keys)

        # check if monsters collides with player
        for monster in self.monsters:
            if collision.check_collision(self.player, monster):
                self.sm.change_state( states.GameoverState() )
                return

        # is level end reached?
        if collision.check_collision(self.player, self.goal):
            self.sm.change_state( game.LevelCompletedState() )
            return

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
        self.goal.draw()
        self.player.draw()
        # draw all monsters
        for monster in self.monsters:
            monster.draw()


