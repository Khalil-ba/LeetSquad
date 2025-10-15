def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve'],ids = ['a', 'a', 'b', 'b'],views = [10, 20, 20, 10]) == [['eve', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve'],ids = ['a', 'a', 'b', 'b'],views = [10, 20, 20, 10]) == [['eve', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four'],views = [5, 10, 5, 4]) == [['alice', 'one'], ['bob', 'two']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four'],views = [5, 10, 5, 4]) == [['alice', 'one'], ['bob', 'two']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['john', 'john', 'john'],ids = ['x', 'y', 'x'],views = [10, 10, 10]) == [['john', 'x']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['john', 'john', 'john'],ids = ['x', 'y', 'x'],views = [10, 10, 10]) == [['john', 'x']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'bob', 'charlie'],ids = ['a', 'b', 'c'],views = [100, 200, 300]) == [['charlie', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'bob', 'charlie'],ids = ['a', 'b', 'c'],views = [100, 200, 300]) == [['charlie', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice'],ids = ['a', 'b', 'c'],views = [1, 2, 2]) == [['alice', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice'],ids = ['a', 'b', 'c'],views = [1, 2, 2]) == [['alice', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],ids = ['id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id'],views = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [['a', 'id']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],ids = ['id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id'],views = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [['a', 'id']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie', 'dave', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 400, 500]) == [['eve', 'e']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie', 'dave', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 400, 500]) == [['eve', 'e']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank', 'frank'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['frank', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank', 'frank'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['frank', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 30, 20, 10]) == [['alice', 'z'], ['bob', 'x']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 30, 20, 10]) == [['alice', 'z'], ['bob', 'x']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 5, 4, 15]) == [['alice', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 5, 4, 15]) == [['alice', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'delta'],views = [1, 3, 2, 5, 6, 5]) == [['eve', 'epsilon']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'delta'],views = [1, 3, 2, 5, 6, 5]) == [['eve', 'epsilon']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 100, 300, 150, 150]) == [['bob', 'x']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 100, 300, 150, 150]) == [['bob', 'x']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['george', 'harry', 'george', 'harry', 'george', 'harry'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 200, 100, 200, 150, 150]) == [['harry', 'def']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['george', 'harry', 'george', 'harry', 'george', 'harry'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 200, 100, 200, 150, 150]) == [['harry', 'def']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu'],views = [10, 20, 10, 20, 30, 40, 50]) == [['alice', 'stu']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu'],views = [10, 20, 10, 20, 30, 40, 50]) == [['alice', 'stu']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'eve', 'eve', 'eve', 'dave'],ids = ['x', 'y', 'z', 'y', 'x'],views = [30, 20, 30, 40, 10]) == [['eve', 'y']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'eve', 'eve', 'eve', 'dave'],ids = ['x', 'y', 'z', 'y', 'x'],views = [30, 20, 30, 40, 10]) == [['eve', 'y']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['alice', 'v']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['alice', 'v']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 15, 10, 10, 5, 5]) == [['bob', 'two']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 15, 10, 10, 5, 5]) == [['bob', 'two']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'],views = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [['charlie', 'a9']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'],views = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [['charlie', 'a9']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [15, 25, 15, 35, 25, 15]) == [['bob', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [15, 25, 15, 35, 25, 15]) == [['bob', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['karen', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['karen', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [10, 20, 30, 40, 50, 60, 70]) == [['mike', 'seven']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [10, 20, 30, 40, 50, 60, 70]) == [['mike', 'seven']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [10, 20, 10, 10, 20]) == [['eve', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [10, 20, 10, 10, 20]) == [['eve', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['a', 'b', 'a', 'b', 'a', 'b'],ids = ['aaa', 'bbb', 'aaa', 'bbb', 'aaa', 'bbb'],views = [1, 2, 3, 4, 5, 6]) == [['b', 'bbb']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['a', 'b', 'a', 'b', 'a', 'b'],ids = ['aaa', 'bbb', 'aaa', 'bbb', 'aaa', 'bbb'],views = [1, 2, 3, 4, 5, 6]) == [['b', 'bbb']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 20, 5, 30, 20, 15]) == [['bob', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 20, 5, 30, 20, 15]) == [['bob', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg'],views = [1, 2, 1, 3, 2, 1, 2]) == [['alice', 'ggg']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg'],views = [1, 2, 1, 3, 2, 1, 2]) == [['alice', 'ggg']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 15, 5, 4, 15]) == [['bob', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 15, 5, 4, 15]) == [['bob', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['rachel', 'sam', 'rachel', 'sam', 'rachel', 'sam'],ids = ['pqr', 'stu', 'vwx', 'yza', 'bcd', 'efg'],views = [5, 5, 5, 5, 5, 5]) == [['rachel', 'bcd'], ['sam', 'efg']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['rachel', 'sam', 'rachel', 'sam', 'rachel', 'sam'],ids = ['pqr', 'stu', 'vwx', 'yza', 'bcd', 'efg'],views = [5, 5, 5, 5, 5, 5]) == [['rachel', 'bcd'], ['sam', 'efg']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 40, 50, 60]) == [['anna', 'z']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 40, 50, 60]) == [['anna', 'z']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['creatorA', 'creatorB', 'creatorC', 'creatorA', 'creatorB', 'creatorC'],ids = ['videoA', 'videoB', 'videoC', 'videoA', 'videoB', 'videoC'],views = [1000, 2000, 1500, 1000, 2500, 1500]) == [['creatorB', 'videoB']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['creatorA', 'creatorB', 'creatorC', 'creatorA', 'creatorB', 'creatorC'],ids = ['videoA', 'videoB', 'videoC', 'videoA', 'videoB', 'videoC'],views = [1000, 2000, 1500, 1000, 2500, 1500]) == [['creatorB', 'videoB']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff'],views = [1, 2, 3, 4, 5, 6]) == [['alice', 'fffff']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff'],views = [1, 2, 3, 4, 5, 6]) == [['alice', 'fffff']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['x', 'y', 'z', 'a', 'b', 'c'],views = [15, 25, 15, 35, 35, 10]) == [['bob', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['x', 'y', 'z', 'a', 'b', 'c'],views = [15, 25, 15, 35, 35, 10]) == [['bob', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'bob', 'charlie', 'dave', 'eve'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'],views = [100, 200, 300, 400, 500]) == [['eve', 'eee']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'bob', 'charlie', 'dave', 'eve'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'],views = [100, 200, 300, 400, 500]) == [['eve', 'eee']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris', 'eve', 'eve', 'eve'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven', 'eight', 'nine', 'ten'],views = [5, 10, 5, 4, 10, 15, 1, 20, 20, 5]) == [['eve', 'eight']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris', 'eve', 'eve', 'eve'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven', 'eight', 'nine', 'ten'],views = [5, 10, 5, 4, 10, 15, 1, 20, 20, 5]) == [['eve', 'eight']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank'],ids = ['a', 'b', 'a', 'c', 'b'],views = [100, 200, 300, 100, 200]) == [['frank', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank'],ids = ['a', 'b', 'a', 'c', 'b'],views = [100, 200, 300, 100, 200]) == [['frank', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 300, 100, 200, 300, 100, 200, 300]) == [['anna', 'c'], ['bob', 'c'], ['charlie', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 300, 100, 200, 300, 100, 200, 300]) == [['anna', 'c'], ['bob', 'c'], ['charlie', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'two', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'two', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],views = [10, 10, 10, 10, 10, 10, 10]) == [['eve', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],views = [10, 10, 10, 10, 10, 10, 10]) == [['eve', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'a', 'b', 'b', 'c'],views = [10, 10, 20, 20, 30]) == [['alice', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'a', 'b', 'b', 'c'],views = [10, 10, 20, 20, 30]) == [['alice', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['vid1', 'vid2', 'vid3', 'vid4', 'vid5', 'vid6', 'vid7'],views = [1, 2, 3, 4, 5, 6, 7]) == [['ivan', 'vid7']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['vid1', 'vid2', 'vid3', 'vid4', 'vid5', 'vid6', 'vid7'],views = [1, 2, 3, 4, 5, 6, 7]) == [['ivan', 'vid7']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf'],views = [10, 10, 10, 10, 10, 10]) == [['eve', 'aaa']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf'],views = [10, 10, 10, 10, 10, 10]) == [['eve', 'aaa']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'a', 'b', 'a', 'b'],views = [10, 15, 10, 20, 10, 25]) == [['bob', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'a', 'b', 'a', 'b'],views = [10, 15, 10, 20, 10, 25]) == [['bob', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 30, 40, 50, 60]) == [['bob', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 30, 40, 50, 60]) == [['bob', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['nina', 'oliver', 'nina', 'oliver', 'nina', 'oliver'],ids = ['x', 'y', 'x', 'y', 'x', 'y'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['nina', 'x'], ['oliver', 'y']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['nina', 'oliver', 'nina', 'oliver', 'nina', 'oliver'],ids = ['x', 'y', 'x', 'y', 'x', 'y'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['nina', 'x'], ['oliver', 'y']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'bob', 'charlie', 'bob', 'anna'],ids = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa'],views = [150, 250, 350, 250, 150]) == [['bob', 'bbb']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'bob', 'charlie', 'bob', 'anna'],ids = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa'],views = [150, 250, 350, 250, 150]) == [['bob', 'bbb']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],ids = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't'],views = [100, 200, 150, 300, 400, 400, 500, 600]) == [['b', 'q'], ['c', 't']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],ids = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't'],views = [100, 200, 150, 300, 400, 400, 500, 600]) == [['b', 'q'], ['c', 't']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace', 'heidi'],ids = ['film1', 'film2', 'film3', 'film4', 'film5', 'film6'],views = [500, 500, 600, 600, 700, 700]) == [['grace', 'film5'], ['heidi', 'film6']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace', 'heidi'],ids = ['film1', 'film2', 'film3', 'film4', 'film5', 'film6'],views = [500, 500, 600, 600, 700, 700]) == [['grace', 'film5'], ['heidi', 'film6']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['m', 'n', 'm', 'n', 'm', 'n'],views = [10, 20, 10, 20, 10, 20]) == [['ivan', 'n']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['m', 'n', 'm', 'n', 'm', 'n'],views = [10, 20, 10, 20, 10, 20]) == [['ivan', 'n']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 3, 15]) == [['bob', 'six']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 3, 15]) == [['bob', 'six']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [100000, 99999, 99998, 99997, 99996, 99995]) == [['alice', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [100000, 99999, 99998, 99997, 99996, 99995]) == [['alice', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'a', 'b', 'b', 'c', 'c', 'd'],views = [10, 20, 30, 20, 30, 40, 50]) == [['nina', 'd']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'a', 'b', 'b', 'c', 'c', 'd'],views = [10, 20, 30, 20, 30, 40, 50]) == [['nina', 'd']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['abc', 'bcd', 'abc', 'xyz', 'bcd', 'abc', 'xyz'],views = [10, 20, 10, 30, 20, 10, 30]) == [['alice', 'xyz']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['abc', 'bcd', 'abc', 'xyz', 'bcd', 'abc', 'xyz'],views = [10, 20, 10, 30, 20, 10, 30]) == [['alice', 'xyz']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],views = [10, 20, 10, 5, 25, 15]) == [['eve', 'beta']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],views = [10, 20, 10, 5, 25, 15]) == [['eve', 'beta']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie'],ids = ['aaaaa', 'bbbbb', 'ccccc'],views = [100000, 100000, 100000]) == [['alice', 'aaaaa'], ['bob', 'bbbbb'], ['charlie', 'ccccc']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie'],ids = ['aaaaa', 'bbbbb', 'ccccc'],views = [100000, 100000, 100000]) == [['alice', 'aaaaa'], ['bob', 'bbbbb'], ['charlie', 'ccccc']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 15, 4, 10]) == [['alice', 'three']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 15, 4, 10]) == [['alice', 'three']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 100, 100, 100, 100, 100]) == [['alice', 'abc'], ['bob', 'def'], ['charlie', 'ghi']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 100, 100, 100, 100, 100]) == [['alice', 'abc'], ['bob', 'def'], ['charlie', 'ghi']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['abc', 'abcd', 'abcde', 'abcdef'],views = [100, 100, 100, 100]) == [['dave', 'abc']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['abc', 'abcd', 'abcde', 'abcdef'],views = [100, 100, 100, 100]) == [['dave', 'abc']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['isaac', 'jack', 'isaac', 'jack', 'isaac', 'jack'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 2, 1, 2, 1, 2]) == [['jack', 'bbb']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['isaac', 'jack', 'isaac', 'jack', 'isaac', 'jack'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 2, 1, 2, 1, 2]) == [['jack', 'bbb']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven'],views = [5, 10, 5, 4, 10, 15, 1]) == [['alice', 'six']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven'],views = [5, 10, 5, 4, 10, 15, 1]) == [['alice', 'six']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['tom', 'jerry', 'spike', 'tom', 'jerry', 'spike'],ids = ['q', 'w', 'e', 'r', 't', 'y'],views = [100, 200, 150, 100, 200, 150]) == [['jerry', 't']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['tom', 'jerry', 'spike', 'tom', 'jerry', 'spike'],ids = ['q', 'w', 'e', 'r', 't', 'y'],views = [100, 200, 150, 100, 200, 150]) == [['jerry', 't']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [1, 2, 3, 4, 5, 6]) == [['karen', 'f']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [1, 2, 3, 4, 5, 6]) == [['karen', 'f']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'bbb', 'aaa', 'bbb'],views = [50, 50, 50, 50]) == [['anna', 'aaa']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'bbb', 'aaa', 'bbb'],views = [50, 50, 50, 50]) == [['anna', 'aaa']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['leo', 'leo', 'leo', 'leo', 'leo'],ids = ['z', 'y', 'x', 'w', 'v'],views = [1000, 1000, 1000, 1000, 1000]) == [['leo', 'v']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['leo', 'leo', 'leo', 'leo', 'leo'],ids = ['z', 'y', 'x', 'w', 'v'],views = [1000, 1000, 1000, 1000, 1000]) == [['leo', 'v']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['x', 'y', 'z', 'x', 'y', 'z', 'x'],views = [10, 20, 10, 30, 20, 10, 10]) == [['alice', 'x'], ['bob', 'y']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['x', 'y', 'z', 'x', 'y', 'z', 'x'],views = [10, 20, 10, 30, 20, 10, 10]) == [['alice', 'x'], ['bob', 'y']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [0, 0, 0, 0, 0, 0]) == [['alice', 'a'], ['bob', 'b'], ['charlie', 'd']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [0, 0, 0, 0, 0, 0]) == [['alice', 'a'], ['bob', 'b'], ['charlie', 'd']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 50, 200]) == [['bob', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 50, 200]) == [['bob', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['tom', 'ulysses', 'tom', 'ulysses', 'tom', 'ulysses'],ids = ['hello', 'world', 'hello', 'world', 'hello', 'world'],views = [1000, 2000, 3000, 4000, 5000, 6000]) == [['ulysses', 'world']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['tom', 'ulysses', 'tom', 'ulysses', 'tom', 'ulysses'],ids = ['hello', 'world', 'hello', 'world', 'hello', 'world'],views = [1000, 2000, 3000, 4000, 5000, 6000]) == [['ulysses', 'world']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 1, 1, 1, 1, 1]) == [['alice', 'aaa'], ['bob', 'bbb'], ['charlie', 'ccc']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 1, 1, 1, 1, 1]) == [['alice', 'aaa'], ['bob', 'bbb'], ['charlie', 'ccc']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'bob', 'bob', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 15, 10, 20, 25, 30]) == [['charlie', 'f']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'bob', 'bob', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 15, 10, 20, 25, 30]) == [['charlie', 'f']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],views = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [['nina', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],views = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [['nina', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [5, 5, 5, 5]) == [['anna', 'aaa']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [5, 5, 5, 5]) == [['anna', 'aaa']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['peter', 'peter', 'peter', 'peter', 'peter'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [500, 1000, 1000, 500, 250]) == [['peter', 'video2']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['peter', 'peter', 'peter', 'peter', 'peter'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [500, 1000, 1000, 500, 250]) == [['peter', 'video2']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 20, 10, 30, 30]) == [['alice', 'c'], ['bob', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 20, 10, 30, 30]) == [['alice', 'c'], ['bob', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'bob', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [10, 20, 30, 30, 40, 10]) == [['alice', 'e'], ['bob', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'bob', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [10, 20, 30, 30, 40, 10]) == [['alice', 'e'], ['bob', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [1000, 1000, 1000, 1000]) == [['dave', 'aaa']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [1000, 1000, 1000, 1000]) == [['dave', 'aaa']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob'],ids = ['id1', 'id1', 'id2', 'id2', 'id2'],views = [10, 20, 10, 5, 15]) == [['alice', 'id1']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob'],ids = ['id1', 'id1', 'id2', 'id2', 'id2'],views = [10, 20, 10, 5, 15]) == [['alice', 'id1']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'],views = [100, 120, 100, 130, 120, 100]) == [['alice', 'apple']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'],views = [100, 120, 100, 130, 120, 100]) == [['alice', 'apple']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['leo', 'mike', 'leo', 'mike', 'leo', 'mike', 'leo', 'mike'],ids = ['video1', 'video2', 'video3', 'video4', 'video5', 'video6', 'video7', 'video8'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['mike', 'video2']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['leo', 'mike', 'leo', 'mike', 'leo', 'mike', 'leo', 'mike'],ids = ['video1', 'video2', 'video3', 'video4', 'video5', 'video6', 'video7', 'video8'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['mike', 'video2']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['james', 'james', 'james', 'james', 'james', 'james', 'james'],ids = ['v1', 'v1', 'v1', 'v1', 'v1', 'v1', 'v1'],views = [1000, 2000, 3000, 4000, 5000, 6000, 7000]) == [['james', 'v1']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['james', 'james', 'james', 'james', 'james', 'james', 'james'],ids = ['v1', 'v1', 'v1', 'v1', 'v1', 'v1', 'v1'],views = [1000, 2000, 3000, 4000, 5000, 6000, 7000]) == [['james', 'v1']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'charlie', 'bob', 'anna', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 300, 200, 100, 300, 100, 200]) == [['bob', 'b'], ['charlie', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'charlie', 'bob', 'anna', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 300, 200, 100, 300, 100, 200]) == [['bob', 'b'], ['charlie', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'alice', 'bob', 'bob', 'bob'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno'],views = [50, 50, 60, 60, 60]) == [['bob', 'ghi']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'alice', 'bob', 'bob', 'bob'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno'],views = [50, 50, 60, 60, 60]) == [['bob', 'ghi']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],views = [500, 500, 400, 300, 500]) == [['grace', 'alpha']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],views = [500, 500, 400, 300, 500]) == [['grace', 'alpha']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'bob', 'alice', 'chris'],ids = ['a', 'b', 'c', 'a', 'd'],views = [10, 20, 20, 30, 5]) == [['alice', 'a'], ['bob', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'bob', 'alice', 'chris'],ids = ['a', 'b', 'c', 'a', 'd'],views = [10, 20, 20, 30, 5]) == [['alice', 'a'], ['bob', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'eve', 'dave', 'eve', 'dave'],ids = ['movie', 'movie', 'series', 'series', 'episode'],views = [100, 100, 200, 200, 50]) == [['dave', 'series']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'eve', 'dave', 'eve', 'dave'],ids = ['movie', 'movie', 'series', 'series', 'episode'],views = [100, 100, 200, 200, 50]) == [['dave', 'series']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 10, 15, 20, 25, 30]) == [['eve', 'f']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 10, 15, 20, 25, 30]) == [['eve', 'f']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['karen', 'leo', 'mike', 'leo', 'karen', 'mike'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [30, 40, 30, 40, 30, 40]) == [['leo', 'b']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['karen', 'leo', 'mike', 'leo', 'karen', 'mike'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [30, 40, 30, 40, 30, 40]) == [['leo', 'b']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 30, 10, 20]) == [['eve', 'z']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 30, 10, 20]) == [['eve', 'z']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['jane', 'jane', 'jane', 'jane', 'jane', 'jane'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 10, 10, 10, 10, 10]) == [['jane', 'five']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['jane', 'jane', 'jane', 'jane', 'jane', 'jane'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 10, 10, 10, 10, 10]) == [['jane', 'five']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['m', 'n', 'o', 'p', 'q', 'r'],views = [100, 200, 150, 250, 175, 225]) == [['eve', 'n'], ['frank', 'r']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['m', 'n', 'o', 'p', 'q', 'r'],views = [100, 200, 150, 250, 175, 225]) == [['eve', 'n'], ['frank', 'r']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 10]) == [['eve', 'x']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 10]) == [['eve', 'x']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['creator1', 'creator2', 'creator1', 'creator2', 'creator3'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [100000, 100000, 100000, 100000, 100000]) == [['creator1', 'video1'], ['creator2', 'video2']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['creator1', 'creator2', 'creator1', 'creator2', 'creator3'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [100000, 100000, 100000, 100000, 100000]) == [['creator1', 'video1'], ['creator2', 'video2']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob'],ids = ['a', 'b', 'c', 'a', 'b'],views = [100, 100, 150, 200, 200]) == [['bob', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob'],ids = ['a', 'b', 'c', 'a', 'b'],views = [100, 100, 150, 200, 200]) == [['bob', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [5, 10, 5, 4, 10, 5, 10]) == [['alice', 'seven']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [5, 10, 5, 4, 10, 5, 10]) == [['alice', 'seven']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 30]) == [['alice', 'y']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 30]) == [['alice', 'y']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],views = [1, 2, 3, 4, 5, 6, 7, 8]) == [['bob', 'a']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],views = [1, 2, 3, 4, 5, 6, 7, 8]) == [['bob', 'a']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['same', 'same', 'same', 'same', 'same', 'same'],views = [5, 5, 5, 5, 5, 5]) == [['mike', 'same']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['same', 'same', 'same', 'same', 'same', 'same'],views = [5, 5, 5, 5, 5, 5]) == [['mike', 'same']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['x', 'y', 'z', 'x', 'y', 'z'],ids = ['a', 'b', 'c', 'a', 'b', 'c'],views = [10, 10, 10, 20, 20, 20]) == [['x', 'a'], ['y', 'b'], ['z', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['x', 'y', 'z', 'x', 'y', 'z'],ids = ['a', 'b', 'c', 'a', 'b', 'c'],views = [10, 10, 10, 20, 20, 20]) == [['x', 'a'], ['y', 'b'], ['z', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['peter', 'quinn', 'peter', 'quinn', 'peter', 'quinn'],ids = ['zero', 'one', 'zero', 'one', 'zero', 'one'],views = [500, 600, 700, 800, 900, 1000]) == [['quinn', 'one']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['peter', 'quinn', 'peter', 'quinn', 'peter', 'quinn'],ids = ['zero', 'one', 'zero', 'one', 'zero', 'one'],views = [500, 600, 700, 800, 900, 1000]) == [['quinn', 'one']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['anna', 'v']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['anna', 'v']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 300, 150, 250, 50]) == [['bob', 'y']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 300, 150, 250, 50]) == [['bob', 'y']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['z', 'z', 'z', 'y', 'y', 'y', 'x', 'x', 'x'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 150, 300, 400, 400, 500, 600, 650]) == [['x', 'c']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['z', 'z', 'z', 'y', 'y', 'y', 'x', 'x', 'x'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 150, 300, 400, 400, 500, 600, 650]) == [['x', 'c']]: {e}')
    
    total += 1
    try:
        result = candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['abc', 'bcd', 'cba', 'xyz', 'zyx', 'bac'],views = [50, 75, 50, 100, 75, 50]) == [['alice', 'abc'], ['bob', 'bcd']]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['abc', 'bcd', 'cba', 'xyz', 'zyx', 'bac'],views = [50, 75, 50, 100, 75, 50]) == [['alice', 'abc'], ['bob', 'bcd']]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve'],ids = ['a', 'a', 'b', 'b'],views = [10, 20, 20, 10]) == [['eve', 'a']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four'],views = [5, 10, 5, 4]) == [['alice', 'one'], ['bob', 'two']]
    assert candidate(creators = ['john', 'john', 'john'],ids = ['x', 'y', 'x'],views = [10, 10, 10]) == [['john', 'x']]
    assert candidate(creators = ['anna', 'bob', 'charlie'],ids = ['a', 'b', 'c'],views = [100, 200, 300]) == [['charlie', 'c']]
    assert candidate(creators = ['alice', 'alice', 'alice'],ids = ['a', 'b', 'c'],views = [1, 2, 2]) == [['alice', 'b']]
    assert candidate(creators = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],ids = ['id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id'],views = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [['a', 'id']]
    assert candidate(creators = ['alice', 'bob', 'charlie', 'dave', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 400, 500]) == [['eve', 'e']]
    assert candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank', 'frank'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['frank', 'five']]
    assert candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 30, 20, 10]) == [['alice', 'z'], ['bob', 'x']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 5, 4, 15]) == [['alice', 'five']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]
    assert candidate(creators = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'delta'],views = [1, 3, 2, 5, 6, 5]) == [['eve', 'epsilon']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 100, 300, 150, 150]) == [['bob', 'x']]
    assert candidate(creators = ['george', 'harry', 'george', 'harry', 'george', 'harry'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 200, 100, 200, 150, 150]) == [['harry', 'def']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu'],views = [10, 20, 10, 20, 30, 40, 50]) == [['alice', 'stu']]
    assert candidate(creators = ['dave', 'eve', 'eve', 'eve', 'dave'],ids = ['x', 'y', 'z', 'y', 'x'],views = [30, 20, 30, 40, 10]) == [['eve', 'y']]
    assert candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['alice', 'v']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 15, 10, 10, 5, 5]) == [['bob', 'two']]
    assert candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'],views = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [['charlie', 'a9']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [15, 25, 15, 35, 25, 15]) == [['bob', 'five']]
    assert candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['karen', 'b']]
    assert candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [10, 20, 30, 40, 50, 60, 70]) == [['mike', 'seven']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e'],views = [10, 20, 10, 10, 20]) == [['eve', 'b']]
    assert candidate(creators = ['a', 'b', 'a', 'b', 'a', 'b'],ids = ['aaa', 'bbb', 'aaa', 'bbb', 'aaa', 'bbb'],views = [1, 2, 3, 4, 5, 6]) == [['b', 'bbb']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 20, 5, 30, 20, 15]) == [['bob', 'five']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg'],views = [1, 2, 1, 3, 2, 1, 2]) == [['alice', 'ggg']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 15, 5, 4, 15]) == [['bob', 'five']]
    assert candidate(creators = ['rachel', 'sam', 'rachel', 'sam', 'rachel', 'sam'],ids = ['pqr', 'stu', 'vwx', 'yza', 'bcd', 'efg'],views = [5, 5, 5, 5, 5, 5]) == [['rachel', 'bcd'], ['sam', 'efg']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [10, 20, 30, 40, 50, 60]) == [['anna', 'z']]
    assert candidate(creators = ['creatorA', 'creatorB', 'creatorC', 'creatorA', 'creatorB', 'creatorC'],ids = ['videoA', 'videoB', 'videoC', 'videoA', 'videoB', 'videoC'],views = [1000, 2000, 1500, 1000, 2500, 1500]) == [['creatorB', 'videoB']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['aaaaa', 'bbbbb', 'ccccc', 'ddddd', 'eeeee', 'fffff'],views = [1, 2, 3, 4, 5, 6]) == [['alice', 'fffff']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['x', 'y', 'z', 'a', 'b', 'c'],views = [15, 25, 15, 35, 35, 10]) == [['bob', 'b']]
    assert candidate(creators = ['anna', 'bob', 'charlie', 'dave', 'eve'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee'],views = [100, 200, 300, 400, 500]) == [['eve', 'eee']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris', 'eve', 'eve', 'eve'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven', 'eight', 'nine', 'ten'],views = [5, 10, 5, 4, 10, 15, 1, 20, 20, 5]) == [['eve', 'eight']]
    assert candidate(creators = ['frank', 'frank', 'frank', 'frank', 'frank'],ids = ['a', 'b', 'a', 'c', 'b'],views = [100, 200, 300, 100, 200]) == [['frank', 'a']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 300, 100, 200, 300, 100, 200, 300]) == [['anna', 'c'], ['bob', 'c'], ['charlie', 'c']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice'],ids = ['one', 'two', 'three', 'four', 'two', 'six'],views = [5, 10, 5, 4, 10, 15]) == [['alice', 'six']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],views = [10, 10, 10, 10, 10, 10, 10]) == [['eve', 'a']]
    assert candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'a', 'b', 'b', 'c'],views = [10, 10, 20, 20, 30]) == [['alice', 'c']]
    assert candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['vid1', 'vid2', 'vid3', 'vid4', 'vid5', 'vid6', 'vid7'],views = [1, 2, 3, 4, 5, 6, 7]) == [['ivan', 'vid7']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['aaa', 'aab', 'aac', 'aad', 'aae', 'aaf'],views = [10, 10, 10, 10, 10, 10]) == [['eve', 'aaa']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'a', 'b', 'a', 'b'],views = [10, 15, 10, 20, 10, 25]) == [['bob', 'b']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 30, 40, 50, 60]) == [['bob', 'c']]
    assert candidate(creators = ['nina', 'oliver', 'nina', 'oliver', 'nina', 'oliver'],ids = ['x', 'y', 'x', 'y', 'x', 'y'],views = [1000, 1000, 1000, 1000, 1000, 1000]) == [['nina', 'x'], ['oliver', 'y']]
    assert candidate(creators = ['anna', 'bob', 'charlie', 'bob', 'anna'],ids = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa'],views = [150, 250, 350, 250, 150]) == [['bob', 'bbb']]
    assert candidate(creators = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],ids = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't'],views = [100, 200, 150, 300, 400, 400, 500, 600]) == [['b', 'q'], ['c', 't']]
    assert candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace', 'heidi'],ids = ['film1', 'film2', 'film3', 'film4', 'film5', 'film6'],views = [500, 500, 600, 600, 700, 700]) == [['grace', 'film5'], ['heidi', 'film6']]
    assert candidate(creators = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],ids = ['m', 'n', 'm', 'n', 'm', 'n'],views = [10, 20, 10, 20, 10, 20]) == [['ivan', 'n']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'chris', 'bob'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [5, 10, 5, 4, 3, 15]) == [['bob', 'six']]
    assert candidate(creators = ['alice', 'alice', 'alice', 'alice', 'alice', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [100000, 99999, 99998, 99997, 99996, 99995]) == [['alice', 'a']]
    assert candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'a', 'b', 'b', 'c', 'c', 'd'],views = [10, 20, 30, 20, 30, 40, 50]) == [['nina', 'd']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['abc', 'bcd', 'abc', 'xyz', 'bcd', 'abc', 'xyz'],views = [10, 20, 10, 30, 20, 10, 30]) == [['alice', 'xyz']]
    assert candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],views = [10, 20, 10, 5, 25, 15]) == [['eve', 'beta']]
    assert candidate(creators = ['alice', 'bob', 'charlie'],ids = ['aaaaa', 'bbbbb', 'ccccc'],views = [100000, 100000, 100000]) == [['alice', 'aaaaa'], ['bob', 'bbbbb'], ['charlie', 'ccccc']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'alice'],ids = ['one', 'two', 'three', 'four', 'five'],views = [5, 10, 15, 4, 10]) == [['alice', 'three']]
    assert candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr'],views = [100, 100, 100, 100, 100, 100]) == [['alice', 'abc'], ['bob', 'def'], ['charlie', 'ghi']]
    assert candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['abc', 'abcd', 'abcde', 'abcdef'],views = [100, 100, 100, 100]) == [['dave', 'abc']]
    assert candidate(creators = ['isaac', 'jack', 'isaac', 'jack', 'isaac', 'jack'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 2, 1, 2, 1, 2]) == [['jack', 'bbb']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'chris', 'bob', 'alice', 'chris'],ids = ['one', 'two', 'three', 'four', 'two', 'six', 'seven'],views = [5, 10, 5, 4, 10, 15, 1]) == [['alice', 'six']]
    assert candidate(creators = ['tom', 'jerry', 'spike', 'tom', 'jerry', 'spike'],ids = ['q', 'w', 'e', 'r', 't', 'y'],views = [100, 200, 150, 100, 200, 150]) == [['jerry', 't']]
    assert candidate(creators = ['karen', 'karen', 'karen', 'karen', 'karen', 'karen'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [1, 2, 3, 4, 5, 6]) == [['karen', 'f']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'bbb', 'aaa', 'bbb'],views = [50, 50, 50, 50]) == [['anna', 'aaa']]
    assert candidate(creators = ['leo', 'leo', 'leo', 'leo', 'leo'],ids = ['z', 'y', 'x', 'w', 'v'],views = [1000, 1000, 1000, 1000, 1000]) == [['leo', 'v']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['x', 'y', 'z', 'x', 'y', 'z', 'x'],views = [10, 20, 10, 30, 20, 10, 10]) == [['alice', 'x'], ['bob', 'y']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [0, 0, 0, 0, 0, 0]) == [['alice', 'a'], ['bob', 'b'], ['charlie', 'd']]
    assert candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e'],views = [100, 200, 300, 50, 200]) == [['bob', 'b']]
    assert candidate(creators = ['tom', 'ulysses', 'tom', 'ulysses', 'tom', 'ulysses'],ids = ['hello', 'world', 'hello', 'world', 'hello', 'world'],views = [1000, 2000, 3000, 4000, 5000, 6000]) == [['ulysses', 'world']]
    assert candidate(creators = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],ids = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],views = [1, 1, 1, 1, 1, 1]) == [['alice', 'aaa'], ['bob', 'bbb'], ['charlie', 'ccc']]
    assert candidate(creators = ['anna', 'anna', 'bob', 'bob', 'charlie', 'charlie'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 15, 10, 20, 25, 30]) == [['charlie', 'f']]
    assert candidate(creators = ['nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina', 'nina'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],views = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [['nina', 'b']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'anna'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [5, 5, 5, 5]) == [['anna', 'aaa']]
    assert candidate(creators = ['peter', 'peter', 'peter', 'peter', 'peter'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [500, 1000, 1000, 500, 250]) == [['peter', 'video2']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'b', 'b', 'c', 'c'],views = [10, 20, 20, 10, 30, 30]) == [['alice', 'c'], ['bob', 'c']]
    assert candidate(creators = ['alice', 'alice', 'bob', 'bob', 'alice', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [10, 20, 30, 30, 40, 10]) == [['alice', 'e'], ['bob', 'c']]
    assert candidate(creators = ['dave', 'dave', 'dave', 'dave'],ids = ['aaa', 'aab', 'aac', 'aad'],views = [1000, 1000, 1000, 1000]) == [['dave', 'aaa']]
    assert candidate(creators = ['alice', 'alice', 'alice', 'bob', 'bob'],ids = ['id1', 'id1', 'id2', 'id2', 'id2'],views = [10, 20, 10, 5, 15]) == [['alice', 'id1']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig'],views = [100, 120, 100, 130, 120, 100]) == [['alice', 'apple']]
    assert candidate(creators = ['leo', 'mike', 'leo', 'mike', 'leo', 'mike', 'leo', 'mike'],ids = ['video1', 'video2', 'video3', 'video4', 'video5', 'video6', 'video7', 'video8'],views = [100, 200, 100, 200, 100, 200, 100, 200]) == [['mike', 'video2']]
    assert candidate(creators = ['james', 'james', 'james', 'james', 'james', 'james', 'james'],ids = ['v1', 'v1', 'v1', 'v1', 'v1', 'v1', 'v1'],views = [1000, 2000, 3000, 4000, 5000, 6000, 7000]) == [['james', 'v1']]
    assert candidate(creators = ['alice', 'bob', 'charlie', 'bob', 'anna', 'charlie', 'anna', 'bob'],ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],views = [100, 200, 300, 200, 100, 300, 100, 200]) == [['bob', 'b'], ['charlie', 'c']]
    assert candidate(creators = ['alice', 'alice', 'bob', 'bob', 'bob'],ids = ['abc', 'def', 'ghi', 'jkl', 'mno'],views = [50, 50, 60, 60, 60]) == [['bob', 'ghi']]
    assert candidate(creators = ['grace', 'heidi', 'grace', 'heidi', 'grace'],ids = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'],views = [500, 500, 400, 300, 500]) == [['grace', 'alpha']]
    assert candidate(creators = ['alice', 'bob', 'bob', 'alice', 'chris'],ids = ['a', 'b', 'c', 'a', 'd'],views = [10, 20, 20, 30, 5]) == [['alice', 'a'], ['bob', 'b']]
    assert candidate(creators = ['dave', 'eve', 'dave', 'eve', 'dave'],ids = ['movie', 'movie', 'series', 'series', 'episode'],views = [100, 100, 200, 200, 50]) == [['dave', 'series']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve', 'eve'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [5, 10, 15, 20, 25, 30]) == [['eve', 'f']]
    assert candidate(creators = ['karen', 'leo', 'mike', 'leo', 'karen', 'mike'],ids = ['a', 'b', 'c', 'd', 'e', 'f'],views = [30, 40, 30, 40, 30, 40]) == [['leo', 'b']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 30, 10, 20]) == [['eve', 'z']]
    assert candidate(creators = ['jane', 'jane', 'jane', 'jane', 'jane', 'jane'],ids = ['one', 'two', 'three', 'four', 'five', 'six'],views = [10, 10, 10, 10, 10, 10]) == [['jane', 'five']]
    assert candidate(creators = ['dave', 'eve', 'frank', 'dave', 'eve', 'frank'],ids = ['m', 'n', 'o', 'p', 'q', 'r'],views = [100, 200, 150, 250, 175, 225]) == [['eve', 'n'], ['frank', 'r']]
    assert candidate(creators = ['eve', 'eve', 'eve', 'eve', 'eve'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 10]) == [['eve', 'x']]
    assert candidate(creators = ['creator1', 'creator2', 'creator1', 'creator2', 'creator3'],ids = ['video1', 'video2', 'video3', 'video4', 'video5'],views = [100000, 100000, 100000, 100000, 100000]) == [['creator1', 'video1'], ['creator2', 'video2']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'bob', 'bob'],ids = ['a', 'b', 'c', 'a', 'b'],views = [100, 100, 150, 200, 200]) == [['bob', 'a']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice', 'alice'],ids = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],views = [5, 10, 5, 4, 10, 5, 10]) == [['alice', 'seven']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice'],ids = ['x', 'y', 'z', 'x', 'y'],views = [10, 20, 10, 20, 30]) == [['alice', 'y']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],ids = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],views = [1, 2, 3, 4, 5, 6, 7, 8]) == [['bob', 'a']]
    assert candidate(creators = ['mike', 'mike', 'mike', 'mike', 'mike', 'mike'],ids = ['same', 'same', 'same', 'same', 'same', 'same'],views = [5, 5, 5, 5, 5, 5]) == [['mike', 'same']]
    assert candidate(creators = ['x', 'y', 'z', 'x', 'y', 'z'],ids = ['a', 'b', 'c', 'a', 'b', 'c'],views = [10, 10, 10, 20, 20, 20]) == [['x', 'a'], ['y', 'b'], ['z', 'c']]
    assert candidate(creators = ['peter', 'quinn', 'peter', 'quinn', 'peter', 'quinn'],ids = ['zero', 'one', 'zero', 'one', 'zero', 'one'],views = [500, 600, 700, 800, 900, 1000]) == [['quinn', 'one']]
    assert candidate(creators = ['anna', 'anna', 'anna', 'anna', 'anna'],ids = ['z', 'y', 'x', 'w', 'v'],views = [5, 5, 5, 5, 5]) == [['anna', 'v']]
    assert candidate(creators = ['anna', 'bob', 'charlie', 'anna', 'bob', 'anna'],ids = ['x', 'y', 'z', 'x', 'y', 'z'],views = [100, 200, 300, 150, 250, 50]) == [['bob', 'y']]
    assert candidate(creators = ['z', 'z', 'z', 'y', 'y', 'y', 'x', 'x', 'x'],ids = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],views = [100, 200, 150, 300, 400, 400, 500, 600, 650]) == [['x', 'c']]
    assert candidate(creators = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice'],ids = ['abc', 'bcd', 'cba', 'xyz', 'zyx', 'bac'],views = [50, 75, 50, 100, 75, 50]) == [['alice', 'abc'], ['bob', 'bcd']]


