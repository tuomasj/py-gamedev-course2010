# spaceinvaders.py
import pyglet

import player

window = pyglet.window.Window()

player_image = pyglet.resource.image('player.png')
player = player.Player( player_image, 320, 200)

@window.event
def on_draw():
    window.clear()
    player.draw()

def update(dt):
    pass

pyglet.clock.schedule_interval(update, 1 / 30.0)

pyglet.app.run()
