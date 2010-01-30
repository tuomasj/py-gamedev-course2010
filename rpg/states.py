# states.py

import statemachine
import pyglet

class StartGameState(statemachine.AbstractState):
    def start(self, statemachine):
        self.label = pyglet.text.Label( text='Press key to start',
                                        x = 320,
                                        y = 240,
                                        anchor_x = 'center',
                                        anchor_y = 'center')

    def stop(self):
        del(self.label)

    def update(self, deltaTime):
        pass

    def draw(self):
        self.label.draw()
