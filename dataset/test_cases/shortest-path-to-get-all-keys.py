def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = ['@.b..', '###.#', 'A.B.c']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.b..', '###.#', 'A.B.c']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.b', '#.A', 'aBc']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.b', '#.A', 'aBc']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@Aa']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@Aa']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.b..', '#.A#.', 'a.c.C']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.b..', '#.A#.', 'a.c.C']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '#.#B.', '.....', 'b.cC.', '.....']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '#.#B.', '.....', 'b.cC.', '.....']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '#.###', 'b.BA.']) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '#.###', 'b.BA.']) == 10: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@........a', '........B', '.........', '.......C.', '.........', '.....D...']) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@........a', '........B', '.........', '.......C.', '.........', '.....D...']) == 9: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['aA.b', '@.B#', '....']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['aA.b', '@.B#', '....']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a..', '###.#', 'b.A.B']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a..', '###.#', 'b.A.B']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.aA', 'b.Bb', '....']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.aA', 'b.Bb', '....']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@..aA', '..B#.', '....b']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@..aA', '..B#.', '....b']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abc', '###.', 'A#B.', 'C...']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abc', '###.', 'A#B.', 'C...']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abc', '###.', 'A.BC']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abc', '###.', 'A.BC']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abcdef', '###GHI.', 'JKLMNO.', 'PQRST.', 'UVWXY.', 'Z.....']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abcdef', '###GHI.', 'JKLMNO.', 'PQRST.', 'UVWXY.', 'Z.....']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B', '......c', '......C']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.....', '.....a', '#.....', '.....b', '#.....', '.....A', '#.....', '.....B', '......c', '......C']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.abc', '###.#', 'A#B#C', 'D.E.F', 'G.H.I', 'J.K.L', 'M.N.O', 'P.Q.R', 'S.T.U', 'V.W.X', 'Y.Z.']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.abc', '###.#', 'A#B#C', 'D.E.F', 'G.H.I', 'J.K.L', 'M.N.O', 'P.Q.R', 'S.T.U', 'V.W.X', 'Y.Z.']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@..a..', '###.B.', '....C.', '#.D.E.', '....F.', '#.G.H.', '....I.', '#.J.K.', '....L.', '#.M.N.', '....O.', '#.P.Q.', '....R.', '#.S.T.', '....U.', '#.V.W.', '....X.', '#.Y.Z.', '.....']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@..a..', '###.B.', '....C.', '#.D.E.', '....F.', '#.G.H.', '....I.', '#.J.K.', '....L.', '#.M.N.', '....O.', '#.P.Q.', '....R.', '#.S.T.', '....U.', '#.V.W.', '....X.', '#.Y.Z.', '.....']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@..a..', '###.#B', '...c.C', '#####.', '..b..A']) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@..a..', '###.#B', '...c.C', '#####.', '..b..A']) == 12: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b', 'c...#', '...C.']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '.#.b.', '....A', '#..B.', '....b', 'c...#', '...C.']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.....', '.#...B', 'A...#.', '.c..#.', '.....d']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.....', '.#...B', 'A...#.', '.c..#.', '.....d']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a..', '###.#', 'b.A.B', 'C#dE.', 'f...G', '#H..i', 'j...K', 'L....']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a..', '###.#', 'b.A.B', 'C#dE.', 'f...G', '#H..i', 'j...K', 'L....']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abc', '###.', 'A.BC', 'D#..', '...E', 'f...', '#G..', 'hI..']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abc', '###.', 'A.BC', 'D#..', '...E', 'f...', '#G..', 'hI..']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'd.D.e']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'd.D.e']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###b.', 'A#B..', 'C...d', '###D.', '...eE', 'f..#.', '..F..']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###b.', 'A#B..', 'C...d', '###D.', '...eE', 'f..#.', '..F..']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a###', '.....#', 'b...A#', '....#B', '.....c', '.....C']) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a###', '.....#', 'b...A#', '....#B', '.....c', '.....C']) == 13: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.......', '......#.', 'b.....A.', '....#B..', '.......c', '......C.']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.......', '......#.', 'b.....A.', '....#B..', '.......c', '......C.']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abcdef', '###GHIJ', 'KLMNO.', 'PQRST.', 'UVWXY.', 'Z.....', '....AB', 'CDEFGH']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abcdef', '###GHIJ', 'KLMNO.', 'PQRST.', 'UVWXY.', 'Z.....', '....AB', 'CDEFGH']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a...', '#.bC..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###b.', 'A....', '#B...']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###b.', 'A....', '#B...']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.......', '..a.....', '......b.', '......B.', '......A.', '......c.', '......C.', '.......@']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.......', '..a.....', '......b.', '......B.', '......A.', '......c.', '......C.', '.......@']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.....', '.#####', '#.B.C.D', '#.E.F.G', '#.H.I.J', '#.K.L.M', '#.N.O.P', '#.Q.R.S', '#.T.U.V', '#.W.X.Y', '#.Z....', '........']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.....', '.#####', '#.B.C.D', '#.E.F.G', '#.H.I.J', '#.K.L.M', '#.N.O.P', '#.Q.R.S', '#.T.U.V', '#.W.X.Y', '#.Z....', '........']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@..aB', '###.#', '..c.C', '#####', '..bA.']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@..aB', '###.#', '..c.C', '#####', '..bA.']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.b', '##..#', '.C...', 'A###.', '....B']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.b', '##..#', '.C...', 'A###.', '....B']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abcABC', '......', '......', '......', '......', '......']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abcABC', '......', '......', '......', '......', '......']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.aBc', '###D.', 'E...F', 'G#b.H', '....I']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.aBc', '###D.', 'E...F', 'G#b.H', '....I']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D', '.efE.', '#F...', 'g....']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.B', '###.#', 'cA.BC', '###d.', '....D', '.efE.', '#F...', 'g....']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a..', '###B.', '....A', 'b....']) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a..', '###B.', '....A', 'b....']) == 11: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.abc', '###.#', 'A#B#C', 'd.e.f', 'D.E.F', '...gH', '...ih']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.abc', '###.#', 'A#B#C', 'd.e.f', 'D.E.F', '...gH', '...ih']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.b', '#.C.D', '....E', 'F.G.H', 'I.J.K', 'L.M.N', 'O.P.@']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.b', '#.C.D', '....E', 'F.G.H', 'I.J.K', 'L.M.N', 'O.P.@']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.aB', '.###', 'C#b.', 'c...', '....']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.aB', '.###', 'C#b.', 'c...', '....']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a...', '#.....', 'b.....', '#.....', '.....A', '.....B']) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a...', '#.....', 'b.....', '#.....', '.....A', '.....B']) == 6: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.aB', '###C', 'D#bE', 'F...', '.G.H']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.aB', '###C', 'D#bE', 'F...', '.G.H']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###b.', '#B...', '....A', '....b']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###b.', '#B...', '....A', '....b']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@....', '#.aB.', 'C#b.D', '.FEG.', '....H']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@....', '#.aB.', 'C#b.D', '.FEG.', '....H']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'D...d', 'E...e', 'F...f']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '###.#', 'b.A.B', '###.#', '....b', 'C...c', 'D...d', 'E...e', 'F...f']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.aBc', '##D..', 'E...C', 'F#bA.', '....G']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.aBc', '##D..', 'E...C', 'F#bA.', '....G']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a..', '#.B..', '...cA', 'd.B.c', 'A.#..']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a..', '#.B..', '...cA', 'd.B.c', 'A.#..']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@......', '###...#', '.....B.', '#####.', '.....A', '#####.', '.....c', '.....C', '.....d', '.....D']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@......', '###...#', '.....B.', '#####.', '.....A', '#####.', '.....c', '.....C', '.....d', '.....D']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@...a', '#.b.B', '#.#.#', 'A.B.a', '.B...', 'c....']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@...a', '#.b.B', '#.#.#', 'A.B.a', '.B...', 'c....']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.#.a', '#..b.', '...A.', '#..B.', '....b', 'c....', 'C...d']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.#.a', '#..b.', '...A.', '#..B.', '....b', 'c....', 'C...d']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.....', '.A.B.C', '######', '.D.E.F', '######', '.G.H.I', '######', '.J.K.L', '######', '.M.N.O', '######', '.P.Q.R', '.....@', '.....S', '.....T', '.....U', '.....V', '.....W', '.....X', '.....Y', '.....Z']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.....', '.A.B.C', '######', '.D.E.F', '######', '.G.H.I', '######', '.J.K.L', '######', '.M.N.O', '######', '.P.Q.R', '.....@', '.....S', '.....T', '.....U', '.....V', '.....W', '.....X', '.....Y', '.....Z']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL', '#...', 'M...']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@abc', '###.', 'A.BC', 'D...', '..EF', 'G...', '.H..', 'IJKL', '#...', 'M...']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.a.b', '##C..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M', '....N']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.a.b', '##C..', 'D#E.F', 'G...H', '...IJ', '....K', '....L', '....M', '....N']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['@.....', '.A.B..', '#####.', '..C.D.', 'E.F.G.', 'H.I.J.', 'K.L.M.', 'N.O.P.', 'Q.R.S.', 'T.U.V.', 'W.X.Y.', 'Z......']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['@.....', '.A.B..', '#####.', '..C.D.', 'E.F.G.', 'H.I.J.', 'K.L.M.', 'N.O.P.', 'Q.R.S.', 'T.U.V.', 'W.X.Y.', 'Z......']) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

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


