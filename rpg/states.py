# states.py

import statemachine
import pyglet
from pyglet.window import key
import game

class StartGameState(statemachine.AbstractState):
    def start(self, statemachine):
        self.statemachine = statemachine
        self.key_pressed = False
        self.label = pyglet.text.Label( text='Press key to start',
                                        x = 320,
                                        y = 240,
                                        anchor_x = 'center',
                                        anchor_y = 'center')

    def stop(self):
        del(self.label)

    def update(self, deltaTime, keys):
        if keys[key.SPACE] and not self.key_pressed:
            self.key_pressed = True
            return

        if not keys[key.SPACE] and self.key_pressed:
            self.statemachine.change_state( game.GameState() )

    def draw(self):
        self.label.draw()

class GameoverState(statemachine.AbstractState):
    def start(self, statemachine):
        self.statemachine = statemachine
        self.key_pressed = False
        self.label = pyglet.text.Label( text='Game Over!',
                                        x = 320,
                                        y = 240,
                                        anchor_x = 'center',
                                        anchor_y = 'center',
                                        font_size = 25)

    def stop(self):
        del(self.label)

    def update(self, deltaTime, keys):
        if keys[key.SPACE] and not self.key_pressed:
            self.key_pressed = True
            return

        if not keys[key.SPACE] and self.key_pressed:
            self.statemachine.change_state( StartGameState() )

    def draw(self):
        self.label.draw()


