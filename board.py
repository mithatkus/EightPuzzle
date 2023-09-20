#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Mithat Kus
# email: mthtks@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Alim Kura
# partner's email: ackura@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3*r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """ Returns a string representation of a Board object
        """
        
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if r == self.blank_r and c == self.blank_c:
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
                
        return s
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction in
            which the blank should move, and attempts to modify the contents 
            of the called Board object accordingly
        """
        new_c = self.blank_c
        new_r = self.blank_r
        
        if direction == 'left':
            new_c -= 1
        elif direction == 'right':
            new_c += 1
        elif direction == 'up':
            new_r -= 1
        elif direction == 'down':
            new_r += 1
        else:
            return False
            
        if new_r not in range(3) or new_c not in range(3):
            return False
        else:
            
            self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][new_c]
            self.tiles[new_r][new_c] = '0'
            
            self.blank_r = new_r
            self.blank_c = new_c
            return True
            
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the current
            contents of the called Board object’s tiles attribute 
        """
        s = ''   
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += str(self.tiles[r][c])
        
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the
            called object 
        """
        dup = self.digit_string()
        
        new = Board(dup)
        
        return new
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object 
            that are not where they should be in the goal state
        """
        
        count = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    count += 0
                elif self.tiles[r][c] != GOAL_TILES[r][c]:
                    count += 1
                    
        return count
    
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) 
            have the same values for the tiles attribute, and False otherwise 
        """
        
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    def points_misplaced(self):
        """ returns the points assigned to the Board object.
        (Required horizontal and vertical moves are worth 1 point) """
        
        points = 0

        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    points += 0
                elif self.tiles[r][c] == '1':
                    points += (abs(r-0) + abs(c-1))                    
                elif self.tiles[r][c] == '2':
                    points += (abs(r-0) + abs(c-2))
                elif self.tiles[r][c] == '3':
                    points += (abs(r-1) + abs(c-0))                    
                elif self.tiles[r][c] == '4':
                    points += (abs(r-1) + abs(c-1))                    
                elif self.tiles[r][c] == '5':
                    points += (abs(r-1) + abs(c-2))
                elif self.tiles[r][c] == '6':
                    points += (abs(r-2) + abs(c-0))
                elif self.tiles[r][c] == '7':
                    points += (abs(r-2) + abs(c-1))
                elif self.tiles[r][c] == '8':
                    points += (abs(r-2) + abs(c-2))
                    
        return points
                    
                
