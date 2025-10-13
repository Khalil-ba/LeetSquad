# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(pizza = ['A', 'A', 'A'],k = 3) == 1
    assert candidate(pizza = ['AA', 'AA'],k = 2) == 2
    assert candidate(pizza = ['A.A', 'A.A', 'A.A'],k = 4) == 6
    assert candidate(pizza = ['A.A', 'A.A', 'A.A'],k = 5) == 0
    assert candidate(pizza = ['...', '...', '...', '...', '...', '...', 'AAA'],k = 4) == 0
    assert candidate(pizza = ['AAA', '...', 'AAA'],k = 2) == 4
    assert candidate(pizza = ['A..', 'A..', '...'],k = 1) == 1
    assert candidate(pizza = ['AAA', 'AAA', 'AAA'],k = 4) == 12
    assert candidate(pizza = ['AA.', 'AA.', '..A'],k = 2) == 4
    assert candidate(pizza = ['AAA', 'AAA', 'AAA'],k = 2) == 4
    assert candidate(pizza = ['A..', 'AA.', '...'],k = 3) == 1
    assert candidate(pizza = ['A.A', '.A.', 'A.A'],k = 2) == 4
    assert candidate(pizza = ['A..', 'A..'],k = 2) == 1
    assert candidate(pizza = ['A.A', 'A.A'],k = 2) == 3
    assert candidate(pizza = ['...', '...', '...'],k = 1) == 0
    assert candidate(pizza = ['A..', 'AAA', '...'],k = 3) == 3
    assert candidate(pizza = ['AAAAA', 'AA.AA', 'AA.AA', 'AA.AA', 'AAAAA'],k = 5) == 346
    assert candidate(pizza = ['AAAA', 'A.AA', 'AA.A', 'AAAA'],k = 4) == 56
    assert candidate(pizza = ['A.A.A', 'A....', 'A.A.A'],k = 3) == 21
    assert candidate(pizza = ['A.A', 'A.A', 'A.A'],k = 3) == 9
    assert candidate(pizza = ['A...A', '.....', 'A...A', '.....', 'A...A'],k = 3) == 36
    assert candidate(pizza = ['...A', '...A', '...A'],k = 2) == 2
    assert candidate(pizza = ['A...', '....', '....', 'A...'],k = 2) == 3
    assert candidate(pizza = ['A...A', '.A.A.', 'A...A', '.A.A.', 'A...A'],k = 5) == 198
    assert candidate(pizza = ['A.A', '.A.', 'A.A'],k = 3) == 10
    assert candidate(pizza = ['A.A', '.A.', 'A.A', '.A.', 'A.A'],k = 3) == 23
    assert candidate(pizza = ['A..A.', 'A..A.', 'A..A.', 'A..A.', 'A..A.'],k = 3) == 30
    assert candidate(pizza = ['AAAAAA', 'A...A.', 'A...A.', 'A...A.', 'AAAAAA'],k = 4) == 212
    assert candidate(pizza = ['AAAAA', '.....', 'AAAAA', '.....', 'AAAAA'],k = 3) == 42
    assert candidate(pizza = ['A...A', '.....', '.....', 'A...A'],k = 3) == 24
    assert candidate(pizza = ['A.A.A.A.A', '.A.A.A.A.', 'A.A.A.A.A', '.A.A.A.A.', 'A.A.A.A.A'],k = 5) == 1955
    assert candidate(pizza = ['AAAA', 'AAAA', 'AAAA', 'AAAA'],k = 5) == 78
    assert candidate(pizza = ['A.A.A', 'A.A.A', 'A.A.A'],k = 2) == 6
    assert candidate(pizza = ['A.A.A', 'A.A.A', 'A.A.A'],k = 3) == 21
    assert candidate(pizza = ['A.A.A.A', 'A.A.A.A', 'A.A.A.A'],k = 4) == 98
    assert candidate(pizza = ['AAAA', 'AAAA', 'AAAA'],k = 3) == 16
    assert candidate(pizza = ['A', 'A', 'A', 'A', 'A'],k = 3) == 6
    assert candidate(pizza = ['A..', '...', 'A..', '...', 'A..'],k = 3) == 4
    assert candidate(pizza = ['AA.AA', 'A...A', 'A...A', 'AA.AA'],k = 3) == 32
    assert candidate(pizza = ['A.....A', 'A.....A', 'A.....A', 'A.....A', 'A.....A'],k = 2) == 10
    assert candidate(pizza = ['AA.', 'A..', '.AA'],k = 2) == 4
    assert candidate(pizza = ['A.A.A', 'A...A', 'A.A.A'],k = 3) == 21
    assert candidate(pizza = ['A....A', '......', '......', 'A....A'],k = 4) == 0
    assert candidate(pizza = ['AAA..', 'AAA..', 'AAA..'],k = 3) == 10
    assert candidate(pizza = ['...A', '...A', 'A...', 'A...'],k = 2) == 6
    assert candidate(pizza = ['A.A.A', 'A.A.A', 'A.A.A', 'A.A.A', 'A.A.A'],k = 4) == 124
    assert candidate(pizza = ['A....', '.....', '.....', '.....', 'A....'],k = 2) == 4
    assert candidate(pizza = ['A...', '.A..', '..A.', '...A'],k = 4) == 8
    assert candidate(pizza = ['.A.A.', 'A.A.A', '.A.A.', 'A.A.A', '.A.A.'],k = 6) == 256
    assert candidate(pizza = ['AAAAA', 'A...A', 'A...A', 'A...A', 'AAAAA'],k = 5) == 346
    assert candidate(pizza = ['A....', '.....', '.....', '.....', '.....'],k = 4) == 0
    assert candidate(pizza = ['A.A.A.A', '.A.A.A.', 'A.A.A.A'],k = 3) == 40
    assert candidate(pizza = ['A.A.A.A', 'A.A.A.A', 'A.A.A.A', 'A.A.A.A', 'A.A.A.A', 'A.A.A.A', 'A.A.A.A', 'A.A.A.A'],k = 8) == 15387
    assert candidate(pizza = ['A...', '.A.A', '....', 'A...'],k = 2) == 6
    assert candidate(pizza = ['A.A.A.A', '.A.A.', 'A.A.A.A', '.A.A.', 'A.A.A.A'],k = 6) == 0
    assert candidate(pizza = ['........', '...A....', '........', '........', '........', '........', '........', '........'],k = 2) == 0
    assert candidate(pizza = ['.A..A.', 'A..A..', '.A..A.', 'A..A..', '.A..A.'],k = 3) == 42
    assert candidate(pizza = ['A..A', '....', 'A..A', '....'],k = 3) == 12
    assert candidate(pizza = ['A.A.A', '.A.A.', 'A.A.A'],k = 3) == 23
    assert candidate(pizza = ['A.A.A.A', '.A.A.A.', 'A.A.A.A', '.A.A.A.'],k = 3) == 51
    assert candidate(pizza = ['AAAAA', 'A...A', 'A...A', 'A...A', 'AAAAA'],k = 4) == 152
    assert candidate(pizza = ['A......', 'A......', 'A......', '.......', '.......', '.......'],k = 2) == 2
    assert candidate(pizza = ['A.A', 'A.A', 'A.A', 'A.A', 'A.A'],k = 4) == 40
    assert candidate(pizza = ['A.A.A', 'A...A', 'A...A', 'A...A', 'A.A.A'],k = 5) == 209
    assert candidate(pizza = ['AAAAA', 'AAAAA', '.....', '.....', '.....'],k = 3) == 14
    assert candidate(pizza = ['A.A.A', '.A.A.', 'A.A.A'],k = 4) == 46
    assert candidate(pizza = ['A.A.A', '.....', 'A.A.A', '.....', 'A.A.A'],k = 5) == 96
    assert candidate(pizza = ['A.A.A.A', '.A.A.A.', 'A.A.A.A', '.A.A.A.', 'A.A.A.A', '.A.A.A.', 'A.A.A.A', '.A.A.A.'],k = 6) == 8692
    assert candidate(pizza = ['A.A..', '.A.A.', '..A.A'],k = 3) == 17
    assert candidate(pizza = ['A....', '.A...', '..A..'],k = 3) == 4
    assert candidate(pizza = ['A....', '..A..', '....A', '.....', '.....'],k = 4) == 0
    assert candidate(pizza = ['A.A.A.A', '.....', 'A.A.A.A', '.....', 'A.A.A.A'],k = 5) == 0
