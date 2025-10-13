# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "BD") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "AC") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASADB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCB") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']],word = "ABCESEEEFS") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "Z") == False
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "AB") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "E") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "SEE") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "AB") == True
    assert candidate(board = [['A', 'B'], ['C', 'D']],word = "CD") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ASAD") == True
    assert candidate(board = [['A']],word = "A") == True
    assert candidate(board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']],word = "ABCCED") == True
