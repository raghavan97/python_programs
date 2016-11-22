from pympler import tracker
import gc
import sys
import abc

#tracker
tr = None

class State(object):
    """
    Abstract Base Class used to represent various states.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, previous_state):
        self.previous_state = previous_state

    @abc.abstractmethod
    def next(self):
        """
        Return the next state.

        :return: An instance of a State.
        """

class StateA(State):
    def __init__(self, prev):
        super(StateA, self).__init__(prev)
        self.boo = dict()

    def next(self):
        next_state =  StateA(self)
        return next_state



def init_tracker():
    global tr
    # initialize the pympler summary tracker
    gc.collect()
    tr = tracker.SummaryTracker()

def show_tracker():
    # print the difference in objects from pympler tracker object
    # which is the memory leak
    print '-----------'
    gc.collect()
    tr.print_diff()
    sys.stdout.flush()


init_tracker()

# Perform the loop to use the state objects 5000 times
init_state = StateA(None)
curr_state = init_state
i = 0
while i < 25000:
    new_state = curr_state.next()
    i += 1

    # to plug the memory leak enable the following line
    # del curr_state.previous_state

    curr_state = new_state

    # show increase once every 5000
    if i % 5000 == 0:
        show_tracker()
