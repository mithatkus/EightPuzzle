#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Mithat Kus
# email: mthtks@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Alim Kura
# partner's email: ackura@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    def __init__(self, depth_limit):
        """ constructs a new Searcher object  
        """
        self.depth_limit = depth_limit
        self.states = []
        self.num_tested = 0
        
    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the 
            Searcher‘s list of untested states
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ takes a State object called state and returns True if the called 
            Searcher should add state to its list of untested states, and 
            False otherwise
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        return True
    
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes 
            the elements of new_states one at a time
        """
        for s in new_states:   
            if self.should_add(s) == True:
                self.add_state(s)


    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified 
            initial state init_state and ends when the goal state is found or
            when the Searcher runs out of untested states
        """
        
        self.add_state(init_state)
        
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                succ = s.generate_successors()
                self.add_states(succ)
            
        return None

    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
       
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    
    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher
        """
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s
    


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """ takes a State object called state, and that computes and returns an 
        estimate of how many additional moves are needed to get from state to \
        the goal state 
    """
    num = state.board.num_misplaced()
    return num

def h2(state):
    """ takes a State object called state, and that computes 
    and returns an estimate of how many additional moves are needed
    by assigning points to the numbers. """
    
    points = state.board.points_misplaced()
    
    return points


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ constructs a new GreedySearcher object 
        """
        super().__init__(-1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
        
    def add_state(self, state):
        """ overrides (i.e., replaces) the add_state method that is inherited 
            from Searcher 
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ overrides (i.e., replaces) the next_state method that is inherited
            from Searcher
        """
        ch = max(self.states)
        self.states.remove(ch)
        return ch[1]



    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        
        return -1 * (self.heuristic(state) + state.num_moves)
    
    
        
         
    
    

