# spaceinvaders.py
import pyglet
import player
from pyglet.window import key

window = pyglet.window.Window()

keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
print("script home:" + pyglet.resource.get_script_home() )

# player_image = pyglet.resource.image('player.png')
player_image = pyglet.image.load('player.png')
player = player.Player( player_image, 320, 200)


@window.event
def on_draw():
    window.clear()
    player.draw()

def update(dt):
    # check player movement
    if keys[key.LEFT]:
        player.move_left(dt)
    if keys[key.RIGHT]:
        player.move_right(dt)

pyglet.clock.schedule_interval(update, 1 / 30.0)

pyglet.app.run()
