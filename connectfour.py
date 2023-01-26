#
# Yuting Shi 
#
# AI Player for use in Connect Four  
#

import random  

class Board:
    """ 
    a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        """
        Board object constructor
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         
        for row in range(self.height):
            s += '|'  
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n' 
        s += ('-'*(self.width*2 + 1))
        s += '\n' 
        for num in range(self.width):
            s += ' ' + str(num%10) 
        s += '\n' 
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        row = self.height - 1
        while True:
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
            else: 
                row -= 1
           
    def reset(self):
        """
        resets the Board objects on which it is called
        sets all of the slots on the board to a space character
        """
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = ' '
 
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'  
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self, col):
        """
        returns True if it is valid to place a checker in col on Board object
        otherwise returns False
        """ 
        if col in range(0, self.width):
            for row in range(self.height):
                if self.slots[row][col] == ' ':
                    return True 
                return False
        else: 
            return False
        
    def is_full(self):
        """
        returns True if the Board object is completely full
        returns False otherwise
        """
        for cols in range(self.width):
            if self.can_add_to(cols) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """
        removes the top checker from column col of Board object
        if column is empty, method does nothing
        """
        while True:
            for row in range(self.height):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '
                    break 
            break 
    
    def is_win_for(self, checker):
        """
        takes parameter checker that is either a 'X' or 'O'
        returns True if there are four consecutive slots containing checker on board
        returns False if none
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
               return True
        return False
               
    def is_horizontal_win(self, checker):
        """ 
        Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True
        return False 
    
    def is_vertical_win(self, checker):
        """
        checks for a vertical win for specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col] == checker and \
                self.slots[row + 2][col] == checker and \
                self.slots[row + 3][col] == checker:
                    return True
        return False 
    
    def is_down_diagonal_win(self, checker):
        """
        checks for a diagonal down from left to right win for specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col + 1] == checker and \
                self.slots[row + 2][col + 2] == checker and \
                self.slots[row + 3][col + 3] == checker:
                    return True
        return False 
    
    def is_up_diagonal_win(self, checker):
        """
        checks for a diagonal down from left to right win for specified checker
        """
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col - 1] == checker and \
                self.slots[row + 2][col - 2] == checker and \
                self.slots[row + 3][col - 3] == checker:
                    return True
        return False 


class Player:
    """
    class that represents a player of the connect four game
    checker represents X or O
    num_moves counts how many moves player has made
    """
    def __init__(self, checker):
        """
        constructor of Player objects
        """
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """
        returns a string representing a Player object
        should indicate which checker the Player object is using
        """
        string = "Player " + self.checker
        return string
    
    def opponent_checker(self):
        """
        returns a one-character string representing the Player objects
        opponent. 
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """
        accepts a Board object b as a parameter
        returns the column where the player wants to make the next move
        """
        while True:
            usercol = int(input("Enter a column: "))
            if usercol in range(0, b.width): 
                self.num_moves += 1
                return usercol
            else:
                print('Try again!')
            
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
        
def process_move(p, b):
    """
    takes inputs Player object p and Board object b
    function performs all of the steps involved in processing a move by
    player p on board b
    """
    print(p.__repr__() + "'s turn")
    turn = p.next_move(b)
    b.add_checker(p.checker, turn)
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(p.__repr__() + ' wins in ' + str(p.num_moves) + ' moves')
        print('Congratulations!')
    elif b.is_full():
        print ("It's a tie!")
        return True 
    else:
        return False 
    
    
class RandomPlayer(Player):
    """
    class for objects of unintelligent computer players 
    that chooses at random from the available columns
    """
    
    def next_move(self, b):
        """
        chooses a random empty slot for the next move
        """ 
        self.num_moves += 1
        columns = []
        for cols in range(b.width):
            if b.can_add_to(cols):
                columns += [cols]
        return random.choice(columns)        


class AIPlayer(Player):
    """
    class of objects of  “intelligent” computer players 
    one that uses techniques from artificial intelligence (AI) 
    to choose its next move
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """
        constructor of objects of AIPlayer
        """
        assert(checker == 'X' or checker =='O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak =='RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak=tiebreak
        self. lookahead = lookahead
        
    def __repr__(self):
        """
        returns string that represents AIPlayer object
        """
        string = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return string
    
    def max_score_column(self, scores):
        """
        takes inputs a list scores containing scores for each column in board
        returns the index of the column with the highest score
        if columns are tied, it uses tiebreak 
        """
        maximum = max(scores)
        listmoves = []
        for cols in range(len(scores)):
            if scores[cols] == maximum:
                listmoves += [cols]
        if self.tiebreak == 'RANDOM':
            return random.choice(listmoves)
        elif self.tiebreak == 'LEFT':
            return listmoves[0]
        elif self.tiebreak == 'RIGHT':
            return listmoves[-1]
        
    def scores_for(self, b):
        """
        takes a Board object b and determines AI Player's score for columns in b
        each column is assigned -1, 0, 50, or 100 
        """
        scores = [0] * b.width
        for cols in range(b.width):
            if b.can_add_to(cols) == False:
                scores[cols] = -1
            elif b.is_win_for(self.opponent_checker()):
                scores[cols] = 0 
            elif b.is_win_for(self.checker):
                scores[cols] = 100
            elif self.lookahead == 0:
                scores[cols] = 50
            else:
                b.add_checker(self.checker, cols)
                player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                otherscore = player.scores_for(b)
                if max(otherscore) == 0:
                    scores[cols] = 100
                elif max(otherscore) == 100:
                    scores[cols] = 0
                else: 
                    scores[cols] = 50
                b.remove_checker(cols)
        return scores
    
    def next_move(self, b):
        """
        returns AIPlayer's next best possible move
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        nextmove = self.max_score_column(scores)
        return nextmove
                    
    


































