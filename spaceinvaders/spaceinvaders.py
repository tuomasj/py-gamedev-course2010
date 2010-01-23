# spaceinvaders.py
import pyglet
import player
from pyglet.window import key

window = pyglet.window.Window()

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

player_image = pyglet.resource.image('player.png')
player = player.Player( player_image, 320, 200)

@window.event
def on_draw():
    window.clear()
    player.draw()

def update(dt):
    # check player movement
    if keys[key.LEFT]:
        print("Left")
    if keys[key.RIGHT]:
        print("Right")

pyglet.clock.schedule_interval(update, 1 / 30.0)

pyglet.app.run()
