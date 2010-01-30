# game.py

import statemachine
import tilelayer

class GameState(statemachine.AbstractState):
    def start(self, sm):
        # init tilelayer
        self.layer = tilelayer.TileLayer( 'level1_64x48.map', 64, 48, 'tiles.png', 32, 32)

    def stop(self):
        del( self.layer )

    def update(self, dt, keys):
        pass

    def draw(self):
        # draw tilelayer
        self.layer.draw()
