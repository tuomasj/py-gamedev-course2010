# test.py

import statemachine

class HelloState(statemachine.AbstractState):
    def start(self, statemachine):
        print "Hello start"

    def stop(self):
        print "Hello stop"

    def update(self, dt):
        print "Hello"

class ByeState(statemachine.AbstractState):
    def start(self, statemachine):
        print "Bye start"

    def update(self, dt):
        print "Bye"

    def stop(self):
        print "Bye Stop"

sm = statemachine.StateMachine()

sm.change_state( HelloState() )
sm.update(1)
sm.push( ByeState() )
sm.update(1)



