# spaceinvaders.py
import pyglet

import player
import monster
import bullet

from pyglet.window import key

window = pyglet.window.Window()

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

monsters = monster.MonsterContainer(10,5)

# player_image = pyglet.resource.image('player.png')
player_image = pyglet.image.load('player.png')
player = player.Player( player_image, 320, 10)

# create bullet
laser = bullet.Bullet()

@window.event
def on_draw():
    window.clear()
    player.draw()
    monsters.draw()

def update(dt):
    # check player movement
    if keys[key.LEFT]:
        player.move_left(dt)
    if keys[key.RIGHT]:
        player.move_right(dt)

    # if player presses SPACE, shoot one laser
    if keys[key.SPACE]:
        laser.shoot( player.x, player.y )

    # move monsters
    monsters.update( dt )

    # move laser
    laser.update(dt)


pyglet.clock.schedule_interval(update, 1 / 30.0)

pyglet.app.run()











