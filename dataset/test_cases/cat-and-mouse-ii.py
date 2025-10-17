def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(grid = ['...M.', '.F#C.', '.....'],catJump = 2,mouseJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['...M.', '.F#C.', '.....'],catJump = 2,mouseJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', 'C.F..'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', 'C.F..'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['C.......', '........', '........', '........', '........', '........', '........', '.......M'],catJump = 5,mouseJump = 5) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['C.......', '........', '........', '........', '........', '........', '........', '.......M'],catJump = 5,mouseJump = 5) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '#F.C.#.'],catJump = 2,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '#F.C.#.'],catJump = 2,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.F.C.', '.....'],catJump = 1,mouseJump = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.F.C.', '.....'],catJump = 1,mouseJump = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '.F.C.'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '.F.C.'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['####F', '#C...', 'M....'],catJump = 1,mouseJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['####F', '#C...', 'M....'],catJump = 1,mouseJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '..F....', '....C..'],catJump = 3,mouseJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '..F....', '....C..'],catJump = 3,mouseJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['MC..F', '.....', '.....'],catJump = 2,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['MC..F', '.....', '.....'],catJump = 2,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.C...F'],catJump = 1,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M...F', '#..C.', '......'],catJump = 2,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M...F', '#..C.', '......'],catJump = 2,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['MC..F', '#####'],catJump = 2,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['MC..F', '#####'],catJump = 2,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'C......'],catJump = 5,mouseJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'C......'],catJump = 5,mouseJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M...', '....', '#...', 'C.F.'],catJump = 1,mouseJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M...', '....', '#...', 'C.F.'],catJump = 1,mouseJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '#C.F.', '.....', '.....'],catJump = 3,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '#C.F.', '.....', '.....'],catJump = 3,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M...#', '...C.', '.....', '.....', '..F..'],catJump = 2,mouseJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M...#', '...C.', '.....', '.....', '..F..'],catJump = 2,mouseJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '.....', '..C..', '...F.'],catJump = 1,mouseJump = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '.....', '..C..', '...F.'],catJump = 1,mouseJump = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '....C.'],catJump = 4,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '....C.'],catJump = 4,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M...F', '.#C.#', '...#.', '.....', '....#'],catJump = 2,mouseJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M...F', '.#C.#', '...#.', '.....', '....#'],catJump = 2,mouseJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '.......', '....#..', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '.......', '....#..', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '.....', '...C.', '..#F.'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '.....', '...C.', '..#F.'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 2,mouseJump = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 2,mouseJump = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '.....#C', '......#', '.......', '#F.....', '.......'],catJump = 3,mouseJump = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '.....#C', '......#', '.......', '#F.....', '.......'],catJump = 3,mouseJump = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.......', '.M.....', '.#C..#.', '.#F..#.', '.#.....', '.#.....', '.......'],catJump = 4,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.......', '.M.....', '.#C..#.', '.#F..#.', '.#.....', '.#.....', '.......'],catJump = 4,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.......', '........', '........', '........', '........', '.....C..', '........', '........', '.......F'],catJump = 4,mouseJump = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.......', '........', '........', '........', '........', '.....C..', '........', '........', '.......F'],catJump = 4,mouseJump = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M...F', '..#C.', '.....', '.....', '.....'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M...F', '..#C.', '.....', '.....', '.....'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M........', '........#', '.........', '#........', '........C', '.........', '.......F.'],catJump = 7,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M........', '........#', '.........', '#........', '........C', '.........', '.......F.'],catJump = 7,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.......', '.#....#', '.#....#', '.#C.M#.', '.#....#', '.#....#', '.......'],catJump = 3,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.......', '.#....#', '.#....#', '.#C.M#.', '.#....#', '.#....#', '.......'],catJump = 3,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.#....#', '..#F...', '#......', '......C'],catJump = 4,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.#....#', '..#F...', '#......', '......C'],catJump = 4,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['######', '#M...#', '#.#F#.', '#.....', '######'],catJump = 2,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['######', '#M...#', '#.#F#.', '#.....', '######'],catJump = 2,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.......', '........', '.####...', '.....#..', '......#F', '........', '........', '.....C..'],catJump = 2,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.......', '........', '.####...', '.....#..', '......#F', '........', '........', '.....C..'],catJump = 2,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '.......', '......#', '....C..', '.......', '....F..'],catJump = 4,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '......C..', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 7,mouseJump = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '......C..', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 7,mouseJump = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '...C.', '#####', '....F'],catJump = 2,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '...C.', '#####', '....F'],catJump = 2,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '.....', '.....', '#....', 'C....', '..F..'],catJump = 4,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '.....', '.....', '#....', 'C....', '..F..'],catJump = 4,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '....C', '....F', '.....'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '....C', '....F', '.....'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '........C', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 5,mouseJump = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '........C', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 5,mouseJump = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '..C...'],catJump = 4,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.....', '......', '......', '......', '......', '......', '...F..', '..C...'],catJump = 4,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....#.', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', '.F....C'],catJump = 3,mouseJump = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....#.', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', '.F....C'],catJump = 3,mouseJump = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.#C..', '..#F.', '.....'],catJump = 3,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.......', '.......', '.......', '...C...', '...M...', '.......', '...F...'],catJump = 5,mouseJump = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.......', '.......', '.......', '...C...', '...M...', '.......', '...F...'],catJump = 5,mouseJump = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M..#....', '......#.', '......#C', '......#.', '......#.', '......F.', '........'],catJump = 3,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M..#....', '......#.', '......#C', '......#.', '......#.', '......F.', '........'],catJump = 3,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 2,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 2,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....F...', '.#..#....', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....F...', '.#..#....', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.F....', '......C', '......#', '........', '........'],catJump = 3,mouseJump = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.F....', '......C', '......#', '........', '........'],catJump = 3,mouseJump = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 1,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.####', '..F..', '....C'],catJump = 1,mouseJump = 1) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'C........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 8,mouseJump = 8) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'C........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........'],catJump = 8,mouseJump = 8) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '.F.C.', '.....', '.....'],catJump = 3,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '.F.C.', '.....', '.....'],catJump = 3,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '#....', '..C..', '....F', '.....'],catJump = 2,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '#....', '..C..', '....F', '.....'],catJump = 2,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'F......'],catJump = 3,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.......', '.#....#', '.#....#', '.#.....', '.#....#', '.#....#', 'F......'],catJump = 3,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M......', '.......', '.......', '....C..', '.......', '.......', '......F'],catJump = 2,mouseJump = 3) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M......', '.......', '.......', '....C..', '.......', '.......', '......F'],catJump = 2,mouseJump = 3) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['.........', '.........', '.........', '.........', '........C', '........M', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 6,mouseJump = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['.........', '.........', '.........', '.........', '........C', '........M', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', '.........', 'F........'],catJump = 6,mouseJump = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M.......', '........', '........', '...F....', '........', '........', '........', '.......C'],catJump = 6,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M.......', '........', '........', '...F....', '........', '........', '........', '.......C'],catJump = 6,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '#..C.', '...#F', '....#', '.....'],catJump = 2,mouseJump = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '#..C.', '...#F', '....#', '.....'],catJump = 2,mouseJump = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(grid = ['M....', '.....', '#....', '..C..', '...F.'],catJump = 3,mouseJump = 1) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(grid = ['M....', '.....', '#....', '..C..', '...F.'],catJump = 3,mouseJump = 1) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

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


