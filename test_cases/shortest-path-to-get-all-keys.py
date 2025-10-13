# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = ['@.b..', '###.#', 'A.B.c']) == -1
    assert candidate(grid = ['@.b', '#.A', 'aBc']) == 8
    assert candidate(grid = ['@Aa']) == -1
    assert candidate(grid = ['@.b..', '#.A#.', 'a.c.C']) == 8
    assert candidate(grid = ['@...a', '#.#B.', '.....', 'b.cC.', '.....']) == 11
    assert candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b']) == -1
    assert candidate(grid = ['@...a', '#.###', 'b.BA.']) == 10
    assert candidate(grid = ['@........a', '........B', '.........', '.......C.', '.........', '.....D...']) == 9
    assert candidate(grid = ['aA.b', '@.B#', '....']) == 4
    assert candidate(grid = ['@.a..', '###.#', 'b.A.B']) == 8
    assert candidate(grid = ['@.aA', 'b.Bb', '....']) == -1
    assert candidate(grid = ['@..aA', '..B#.', '....b']) == 6
    assert candidate(grid = ['@abc', '###.', 'A#B.', 'C...']) == 3
    assert candidate(grid = ['@abc', '###.', 'A.BC']) == 3
    assert candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B']) == 8
    assert candidate(grid = ['@abcdef', '###GHI.', 'JKLMNO.', 'PQRST.', 'UVWXY.', 'Z.....']) == 6
    assert candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B', '......c', '......C']) == -1
    assert candidate(grid = ['@.abc', '###.#', 'A#B#C', 'D.E.F', 'G.H.I', 'J.K.L', 'M.N.O', 'P.Q.R', 'S.T.U', 'V.W.X', 'Y.Z.']) == 4
    assert candidate(grid = ['@..a..', '###.B.', '....C.', '#.D.E.', '....F.', '#.G.H.', '....I.', '#.J.K.', '....L.', '#.M.N.', '....O.', '#.P.Q.', '....R.', '#.S.T.', '....U.', '#.V.W.', '....X.', '#.Y.Z.', '.....']) == 3
    assert candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K']) == 3
    assert candidate(grid = ['@..a..', '###.#B', '...c.C', '#####.', '..b..A']) == 12
    assert candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b', 'c...#', '...C.']) == -1
    assert candidate(grid = ['@.....', '.#...B', 'A...#.', '.c..#.', '.....d']) == -1
    assert candidate(grid = ['@.a..', '###.#', 'b.A.B', 'C#dE.', 'f...G', '#H..i', 'j...K', 'L....']) == -1
    assert candidate(grid = ['@abc', '###.', 'A.BC', 'D#..', '...E', 'f...', '#G..', 'hI..']) == -1
    assert candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'd.D.e']) == -1
    assert candidate(grid = ['@...a', '###b.', 'A#B..', 'C...d', '###D.', '...eE', 'f..#.', '..F..']) == -1
    assert candidate(grid = ['@.a###', '.....#', 'b...A#', '....#B', '.....c', '.....C']) == 13
    assert candidate(grid = ['@.......', '......#.', 'b.....A.', '....#B..', '.......c', '......C.']) == -1
    assert candidate(grid = ['@abcdef', '###GHIJ', 'KLMNO.', 'PQRST.', 'UVWXY.', 'Z.....', '....AB', 'CDEFGH']) == 6
    assert candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M']) == 3
    assert candidate(grid = ['@...a', '###b.', 'A....', '#B...']) == 6
    assert candidate(grid = ['@.......', '..a.....', '......b.', '......B.', '......A.', '......c.', '......C.', '.......@']) == 11
    assert candidate(grid = ['@.a.....', '.#####', '#.B.C.D', '#.E.F.G', '#.H.I.J', '#.K.L.M', '#.N.O.P', '#.Q.R.S', '#.T.U.V', '#.W.X.Y', '#.Z....', '........']) == 2
    assert candidate(grid = ['@..aB', '###.#', '..c.C', '#####', '..bA.']) == -1
    assert candidate(grid = ['@.a.b', '##..#', '.C...', 'A###.', '....B']) == 4
    assert candidate(grid = ['@abcABC', '......', '......', '......', '......', '......']) == 3
    assert candidate(grid = ['@.aBc', '###D.', 'E...F', 'G#b.H', '....I']) == -1
    assert candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D']) == -1
    assert candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D', '.efE.', '#F...', 'g....']) == -1
    assert candidate(grid = ['@.a..', '###B.', '....A', 'b....']) == 11
    assert candidate(grid = ['@.abc', '###.#', 'A#B#C', 'd.e.f', 'D.E.F', '...gH', '...ih']) == -1
    assert candidate(grid = ['@.a.b', '#.C.D', '....E', 'F.G.H', 'I.J.K', 'L.M.N', 'O.P.@']) == 4
    assert candidate(grid = ['@.aB', '.###', 'C#b.', 'c...', '....']) == -1
    assert candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c']) == -1
    assert candidate(grid = ['@.a...', '#.....', 'b.....', '#.....', '.....A', '.....B']) == 6
    assert candidate(grid = ['@.aB', '###C', 'D#bE', 'F...', '.G.H']) == -1
    assert candidate(grid = ['@...a', '###b.', '#B...', '....A', '....b']) == -1
    assert candidate(grid = ['@....', '#.aB.', 'C#b.D', '.FEG.', '....H']) == 4
    assert candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'D...d', 'E...e', 'F...f']) == -1
    assert candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL']) == 3
    assert candidate(grid = ['@.aBc', '##D..', 'E...C', 'F#bA.', '....G']) == -1
    assert candidate(grid = ['@.a..', '#.B..', '...cA', 'd.B.c', 'A.#..']) == -1
    assert candidate(grid = ['@......', '###...#', '.....B.', '#####.', '.....A', '#####.', '.....c', '.....C', '.....d', '.....D']) == -1
    assert candidate(grid = ['@...a', '#.b.B', '#.#.#', 'A.B.a', '.B...', 'c....']) == -1
    assert candidate(grid = ['@.#.a', '#..b.', '...A.', '#..B.', '....b', 'c....', 'C...d']) == -1
    assert candidate(grid = ['@.....', '.A.B.C', '######', '.D.E.F', '######', '.G.H.I', '######', '.J.K.L', '######', '.M.N.O', '######', '.P.Q.R', '.....@', '.....S', '.....T', '.....U', '.....V', '.....W', '.....X', '.....Y', '.....Z']) == 0
    assert candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL', '#...', 'M...']) == 3
    assert candidate(grid = ['@.a.b', '##C..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M', '....N']) == 4
    assert candidate(grid = ['@.....', '.A.B..', '#####.', '..C.D.', 'E.F.G.', 'H.I.J.', 'K.L.M.', 'N.O.P.', 'Q.R.S.', 'T.U.V.', 'W.X.Y.', 'Z......']) == 0
