# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = ['...M.', '.F#C.', '.....'],catJump = 2,mouseJump = 2) == True
    assert candidate(grid = ['M....', '.....', 'C.F..'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['C.......', '........', '........', '........', '........', '........', '........', '.......M'],catJump = 5,mouseJump = 5) == False
    assert candidate(grid = ['M......', '#F.C.#.'],catJump = 2,mouseJump = 3) == False
    assert candidate(grid = ['M....', '.F.C.', '.....'],catJump = 1,mouseJump = 1) == True
    assert candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 1) == False
    assert candidate(grid = ['M....', '.....', '.F.C.'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 4) == True
    assert candidate(grid = ['####F', '#C...', 'M....'],catJump = 1,mouseJump = 2) == True
    assert candidate(grid = ['M......', '.......', '..F....', '....C..'],catJump = 3,mouseJump = 4) == True
    assert candidate(grid = ['MC..F', '.....', '.....'],catJump = 2,mouseJump = 2) == False
    assert candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 3) == False
    assert candidate(grid = ['M...F', '#..C.', '......'],catJump = 2,mouseJump = 1) == False
    assert candidate(grid = ['MC..F', '#####'],catJump = 2,mouseJump = 2) == False
    assert candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'C......'],catJump = 5,mouseJump = 3) == True
    assert candidate(grid = ['M...', '....', '#...', 'C.F.'],catJump = 1,mouseJump = 3) == True
    assert candidate(grid = ['M....', '.....', '#C.F.', '.....', '.....'],catJump = 3,mouseJump = 2) == False
    assert candidate(grid = ['M...#', '...C.', '.....', '.....', '..F..'],catJump = 2,mouseJump = 2) == True
    assert candidate(grid = ['M....', '.....', '.....', '..C..', '...F.'],catJump = 1,mouseJump = 4) == True
    assert candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '....C.'],catJump = 4,mouseJump = 2) == False
    assert candidate(grid = ['M...F', '.#C.#', '...#.', '.....', '....#'],catJump = 2,mouseJump = 3) == True
    assert candidate(grid = ['M......', '.......', '.......', '....#..', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False
    assert candidate(grid = ['M....', '.....', '.....', '...C.', '..#F.'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 2,mouseJump = 4) == False
    assert candidate(grid = ['M......', '.......', '.....#C', '......#', '.......', '#F.....', '.......'],catJump = 3,mouseJump = 3) == True
    assert candidate(grid = ['.......', '.M.....', '.#C..#.', '.#F..#.', '.#.....', '.#.....', '.......'],catJump = 4,mouseJump = 2) == False
    assert candidate(grid = ['M.......', '........', '........', '........', '........', '.....C..', '........', '........', '.......F'],catJump = 4,mouseJump = 4) == False
    assert candidate(grid = ['M...F', '..#C.', '.....', '.....', '.....'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M........', '........#', '.........', '#........', '........C', '.........', '.......F.'],catJump = 7,mouseJump = 2) == False
    assert candidate(grid = ['.......', '.#....#', '.#....#', '.#C.M#.', '.#....#', '.#....#', '.......'],catJump = 3,mouseJump = 3) == False
    assert candidate(grid = ['M......', '.#....#', '..#F...', '#......', '......C'],catJump = 4,mouseJump = 1) == False
    assert candidate(grid = ['######', '#M...#', '#.#F#.', '#.....', '######'],catJump = 2,mouseJump = 3) == False
    assert candidate(grid = ['M.......', '........', '.####...', '.....#..', '......#F', '........', '........', '.....C..'],catJump = 2,mouseJump = 1) == False
    assert candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False
    assert candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '......C..', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 7,mouseJump = 7) == True
    assert candidate(grid = ['M....', '.....', '...C.', '#####', '....F'],catJump = 2,mouseJump = 1) == False
    assert candidate(grid = ['M....', '.....', '.....', '.....', '#....', 'C....', '..F..'],catJump = 4,mouseJump = 3) == False
    assert candidate(grid = ['M....', '.....', '....C', '....F', '.....'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '........C', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 5,mouseJump = 5) == True
    assert candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '..C...'],catJump = 4,mouseJump = 2) == False
    assert candidate(grid = ['M....#.', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', '.F....C'],catJump = 3,mouseJump = 4) == False
    assert candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 2) == False
    assert candidate(grid = ['.......', '.......', '.......', '...C...', '...M...', '.......', '...F...'],catJump = 5,mouseJump = 5) == True
    assert candidate(grid = ['M..#....', '......#.', '......#C', '......#.', '......#.', '......F.', '........'],catJump = 3,mouseJump = 3) == False
    assert candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 2,mouseJump = 1) == False
    assert candidate(grid = ['M....F...', '.#..#....', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M.F....', '......C', '......#', '........', '........'],catJump = 3,mouseJump = 2) == True
    assert candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 1,mouseJump = 1) == False
    assert candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'C........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 8,mouseJump = 8) == False
    assert candidate(grid = ['M....', '.....', '.F.C.', '.....', '.....'],catJump = 3,mouseJump = 3) == False
    assert candidate(grid = ['M....', '#....', '..C..', '....F', '.....'],catJump = 2,mouseJump = 2) == False
    assert candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'F......'],catJump = 3,mouseJump = 3) == False
    assert candidate(grid = ['M......', '.......', '.......', '....C..', '.......', '.......', '......F'],catJump = 2,mouseJump = 3) == False
    assert candidate(grid = ['.........', '.........', '.........', '.........', '........C', '........M', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 6,mouseJump = 6) == True
    assert candidate(grid = ['M.......', '........', '........', '...F....', '........', '........', '........', '.......C'],catJump = 6,mouseJump = 2) == False
    assert candidate(grid = ['M....', '#..C.', '...#F', '....#', '.....'],catJump = 2,mouseJump = 2) == False
    assert candidate(grid = ['M....', '.....', '#....', '..C..', '...F.'],catJump = 3,mouseJump = 1) == False
