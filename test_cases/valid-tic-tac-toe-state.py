# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['X  ', 'X  ', 'X  ']) == False
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['XXX', '   ', 'O O']) == True
    assert candidate(board = ['X  ', ' O ', '    ']) == True
    assert candidate(board = ['XOX', 'XOX', 'XOX']) == False
    assert candidate(board = ['OXX', 'XOX', 'OXO']) == False
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['XOX', 'OXO', '   ']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' X ', '  X']) == False
    assert candidate(board = ['XXO', 'OOX', 'OXO']) == False
    assert candidate(board = ['X  ', 'XO ', ' X ']) == False
    assert candidate(board = ['XXX', '   ', 'OOO']) == False
    assert candidate(board = ['XOX', 'O O', 'XOX']) == True
    assert candidate(board = ['XOX', 'OOO', 'XOX']) == False
    assert candidate(board = ['XO ', 'OX ', 'OXO']) == False
    assert candidate(board = ['X  ', ' O ', 'XOX']) == True
    assert candidate(board = ['XX ', 'OO ', '   ']) == True
    assert candidate(board = ['XOO', 'XOX', 'OOX']) == False
    assert candidate(board = ['XX ', 'OOX', 'XOX']) == False
    assert candidate(board = ['XXO', 'XOX', 'OOX']) == False
    assert candidate(board = ['OOO', 'XOX', 'XXO']) == False
    assert candidate(board = ['XOX', 'O O', '   ']) == False
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XOX', 'OOX', 'XOX']) == False
    assert candidate(board = ['OOO', 'OOO', 'OOO']) == False
    assert candidate(board = ['OXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XOO', 'XOX', 'OXO']) == False
    assert candidate(board = ['   ', 'XOX', '   ']) == True
    assert candidate(board = ['X  ', ' O ', '  O']) == False
    assert candidate(board = ['XOO', 'OXO', 'XOX']) == False
    assert candidate(board = ['XOX', 'XOX', 'OOO']) == False
    assert candidate(board = ['XXO', 'OXO', 'OXO']) == False
    assert candidate(board = ['XOO', 'XOX', 'XOX']) == False
    assert candidate(board = ['XXX', 'OOO', '   ']) == False
    assert candidate(board = ['XXX', 'OOO', '   ']) == False
    assert candidate(board = ['XOX', 'OXO', 'XO ']) == False
    assert candidate(board = ['OOO', 'X X', 'XOX']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['   ', 'XXX', '   ']) == False
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' X ', '  X']) == False
    assert candidate(board = ['XOO', 'XOO', 'XOO']) == False
    assert candidate(board = ['X  ', ' O ', '  X']) == True
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['OXX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'OXO']) == False
    assert candidate(board = ['XXX', 'OOO', 'XXX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XXO', 'OOX', 'XOX']) == True
    assert candidate(board = ['XXO', 'OXO', 'XOX']) == True
    assert candidate(board = ['X  ', ' O ', '  O']) == False
    assert candidate(board = ['X  ', ' O ', ' X ']) == True
    assert candidate(board = ['X  ', 'OOO', 'X  ']) == False
    assert candidate(board = ['XOX', 'OXX', 'OXO']) == True
    assert candidate(board = ['X  ', ' O ', 'X  ']) == True
    assert candidate(board = ['XOO', 'XOX', 'OXO']) == False
    assert candidate(board = ['X O', 'X O', 'X O']) == False
    assert candidate(board = ['XXX', '   ', '   ']) == False
    assert candidate(board = ['XXO', 'XOX', 'OOO']) == False
    assert candidate(board = ['XXO', 'XOX', 'OXO']) == False
    assert candidate(board = ['XOX', 'OXO', 'OOX']) == False
    assert candidate(board = ['O  ', 'O  ', 'O  ']) == False
    assert candidate(board = ['XXO', 'OXO', 'OOX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True
    assert candidate(board = ['XX ', 'OOX', 'X  ']) == False
    assert candidate(board = ['   ', '   ', 'XXX']) == False
    assert candidate(board = ['OOO', '   ', '   ']) == False
    assert candidate(board = ['X  ', ' O ', '  X']) == True
    assert candidate(board = ['   ', '   ', 'XXX']) == False
    assert candidate(board = ['O  ', ' O ', '  O']) == False
    assert candidate(board = ['XO ', 'OX ', '   ']) == True
    assert candidate(board = ['XOX', 'OXO', 'XOX']) == True
    assert candidate(board = ['XO ', 'OXO', 'OXO']) == False
    assert candidate(board = ['X  ', '   ', '  O']) == True
    assert candidate(board = ['O  ', '   ', '   ']) == False
    assert candidate(board = ['XOX', ' X ', '   ']) == False
    assert candidate(board = ['XXX', 'XXX', 'XXX']) == False
    assert candidate(board = ['X  ', 'X  ', 'X  ']) == False
    assert candidate(board = ['OOO', '   ', 'XXX']) == False
    assert candidate(board = ['O  ', ' O ', '  O']) == False
    assert candidate(board = ['XOX', 'XOX', 'XOX']) == False
    assert candidate(board = ['   ', '   ', '   ']) == True
