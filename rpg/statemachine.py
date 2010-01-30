# statemachine.py

class AbstractState():

    def start(self, statemachine):
        pass

    def stop(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

class StateMachine():

    def __init__(self):
        self.states = []
        self.current_state = None

    def __del__(self):
        self.stop_all_states()

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)

    def draw(self):
        if self.current_state:
            self.current_state.draw()

    def change_state(self, new_state):
        # stop all previous states
        self.stop_all_states()
	    # start new state
        self.push( new_state )

    def push(self, new_state):
        new_state.start( self )
        self.states.append( new_state )
        self.current_state = new_state

    def pop(self):
        self.current_state.stop()
        self.states.pop()
        self.current_state = self.states[ -1 ]
        self.current_state.start( self )

    def stop_all_states(self):
        for state in self.states[::-1]:
            state.stop()
        del( self.states[:] )












