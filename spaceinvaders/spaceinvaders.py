# spaceinvaders.py

import pyglet

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()

def update(dt):
    pass

pyglet.clock.schedule_interval(update, 1 / 30.0)

pyglet.app.run()
