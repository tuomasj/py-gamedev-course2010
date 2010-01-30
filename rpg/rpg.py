# rpg.py
import pyglet
import statemachine
import states

window = pyglet.window.Window()
sm = statemachine.StateMachine()

sm.push( states.StartGameState() )

@window.event
def on_draw():
    window.clear()
    sm.draw()

def update(deltaTime):
    sm.update(deltaTime)

pyglet.clock.schedule_interval( update, 1 / 30.0 )
pyglet.app.run()

