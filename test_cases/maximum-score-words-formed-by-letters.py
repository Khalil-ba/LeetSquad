def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['xxxz', 'ax', 'bx', 'cx'],letters = ['z', 'a', 'b', 'c', 'x', 'x', 'x'],score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xxxz', 'ax', 'bx', 'cx'],letters = ['z', 'a', 'b', 'c', 'x', 'x', 'x'],score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(words = ['leetcode'],letters = ['l', 'e', 't', 'c', 'o', 'd'],score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['leetcode'],letters = ['l', 'e', 't', 'c', 'o', 'd'],score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'cat', 'dad', 'good'],letters = ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'],score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'cat', 'dad', 'good'],letters = ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'],score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 659
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 659: {e}')
    
    total += 1
    try:
        result = candidate(words = ['dynamic', 'programming', 'complexity', 'analysis'],letters = ['d', 'y', 'n', 'a', 'm', 'i', 'c', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'm', 'p', 'l', 'e', 'x', 'i', 't', 'y', 'a', 'n', 'a', 'l', 'y', 's', 'i', 's'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dynamic', 'programming', 'complexity', 'analysis'],letters = ['d', 'y', 'n', 'a', 'm', 'i', 'c', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'm', 'p', 'l', 'e', 'x', 'i', 't', 'y', 'a', 'n', 'a', 'l', 'y', 's', 'i', 's'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 184: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quartz', 'pearl', 'opal'],letters = ['q', 'u', 'a', 'r', 't', 'z', 'p', 'e', 'a', 'r', 'l', 'o', 'p', 'a', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quartz', 'pearl', 'opal'],letters = ['q', 'u', 'a', 'r', 't', 'z', 'p', 'e', 'a', 'r', 'l', 'o', 'p', 'a', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'code', 'python', 'challenge'],letters = ['a', 'c', 'd', 'e', 'e', 'g', 'h', 'i', 'l', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 'r', 's', 't', 'u', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'code', 'python', 'challenge'],letters = ['a', 'c', 'd', 'e', 'e', 'g', 'h', 'i', 'l', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 'r', 's', 't', 'u', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['university', 'college', 'school'],letters = ['u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y', 'c', 'o', 'l', 'l', 'e', 'g', 'e', 's', 'c', 'h', 'o', 'o', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['university', 'college', 'school'],letters = ['u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y', 'c', 'o', 'l', 'l', 'e', 'g', 'e', 's', 'c', 'h', 'o', 'o', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'example', 'test'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'e', 'a', 'm', 'p', 'l', 'e', 't', 'e', 's', 't', 'c', 'o', 'm', 'p', 'l', 'e', 'x'],score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]) == 2280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'example', 'test'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'e', 'a', 'm', 'p', 'l', 'e', 't', 'e', 's', 't', 'c', 'o', 'm', 'p', 'l', 'e', 'x'],score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]) == 2280: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'elephant', 'giraffe', 'hippo'],letters = ['a', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'l', 'n', 'o', 'p', 'p', 'r', 'r', 's', 't', 'u', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'elephant', 'giraffe', 'hippo'],letters = ['a', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'l', 'n', 'o', 'p', 'p', 'r', 'r', 's', 't', 'u', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(words = ['kangaroo', 'koala', 'hippopotamus'],letters = ['k', 'a', 'n', 'g', 'a', 'r', 'o', 'o', 'o', 'o', 'l', 'i', 'p', 'p', 'o', 't', 'a', 'm', 'u', 's'],score = [8, 1, 13, 3, 1, 1, 1, 1, 1, 1, 4, 1, 5, 9, 7, 6, 5, 3, 0, 9, 0, 5, 5, 0, 0, 0]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['kangaroo', 'koala', 'hippopotamus'],letters = ['k', 'a', 'n', 'g', 'a', 'r', 'o', 'o', 'o', 'o', 'l', 'i', 'p', 'p', 'o', 't', 'a', 'm', 'u', 's'],score = [8, 1, 13, 3, 1, 1, 1, 1, 1, 1, 4, 1, 5, 9, 7, 6, 5, 3, 0, 9, 0, 5, 5, 0, 0, 0]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'performance', 'scalability', 'expert', 'knowledge', 'skill'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y', 'e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 118
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'performance', 'scalability', 'expert', 'knowledge', 'skill'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y', 'e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 118: {e}')
    
    total += 1
    try:
        result = candidate(words = ['onomatopoeia', 'palindrome', 'multifarious'],letters = ['o', 'n', 'o', 'm', 'a', 't', 'o', 'p', 'o', 'e', 'i', 'a', 'p', 'a', 'l', 'i', 'n', 'd', 'r', 'o', 'm', 'e', 'm', 'u', 'l', 't', 'i', 'f', 'a', 'r', 'i', 'o', 'u', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['onomatopoeia', 'palindrome', 'multifarious'],letters = ['o', 'n', 'o', 'm', 'a', 't', 'o', 'p', 'o', 'e', 'i', 'a', 'p', 'a', 'l', 'i', 'n', 'd', 'r', 'o', 'm', 'e', 'm', 'u', 'l', 't', 'i', 'f', 'a', 'r', 'i', 'o', 'u', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'abcde', 'abcdef', 'abcdefg'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'abcde', 'abcdef', 'abcdefg'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'performance', 'efficiency'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 'e', 'f', 'f', 'i', 'c', 'i', 'e', 'n', 'c', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'performance', 'efficiency'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 'e', 'f', 'f', 'i', 'c', 'i', 'e', 'n', 'c', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'alabama', 'tennessee'],letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i', 'a', 'l', 'a', 'b', 'a', 'm', 'a', 't', 'e', 'n', 'n', 'e', 's', 's', 'e'],score = [3, 1, 9, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 5, 5, 0, 2, 3, 9]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'alabama', 'tennessee'],letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i', 'a', 'l', 'a', 'b', 'a', 'm', 'a', 't', 'e', 'n', 'n', 'e', 's', 's', 'e'],score = [3, 1, 9, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 5, 5, 0, 2, 3, 9]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zzzz', 'zzz', 'zz', 'z'],letters = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zzzz', 'zzz', 'zz', 'z'],letters = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 260: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'datastructure', 'machinelearning'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'm', 'a', 'c', 'h', 'i', 'n', 'e', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'datastructure', 'machinelearning'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'm', 'a', 'c', 'h', 'i', 'n', 'e', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(words = ['amazing', 'zebra', 'apple'],letters = ['a', 'm', 'a', 'z', 'i', 'n', 'g', 'z', 'e', 'b', 'r', 'a', 'a', 'p', 'p', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['amazing', 'zebra', 'apple'],letters = ['a', 'm', 'a', 'z', 'i', 'n', 'g', 'z', 'e', 'b', 'r', 'a', 'a', 'p', 'p', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 274
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 274: {e}')
    
    total += 1
    try:
        result = candidate(words = ['syzygy', 'zygote', 'zygomycete'],letters = ['s', 'y', 'z', 'y', 'g', 'y', 'z', 'y', 'g', 'o', 't', 'e', 'z', 'y', 'g', 'o', 'm', 'y', 'c', 'e', 't', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['syzygy', 'zygote', 'zygomycete'],letters = ['s', 'y', 'z', 'y', 'g', 'y', 'z', 'y', 'g', 'o', 't', 'e', 'z', 'y', 'g', 'o', 'm', 'y', 'c', 'e', 't', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'monkey', 'giraffe'],letters = ['z', 'e', 'r', 'b', 'a', 'o', 'n', 'k', 'm', 'y', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [1, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'monkey', 'giraffe'],letters = ['z', 'e', 'r', 'b', 'a', 'o', 'n', 'k', 'm', 'y', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [1, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure', 'software'],letters = ['a', 'a', 'a', 'c', 'd', 'd', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'o', 'r', 's', 's', 's', 't', 'u', 'w', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure', 'software'],letters = ['a', 'a', 'a', 'c', 'd', 'd', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'o', 'r', 's', 's', 's', 't', 'u', 'w', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 301: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacaxi', 'kiwi', 'pineapple'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'i', 'k', 'i', 'w', 'i', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacaxi', 'kiwi', 'pineapple'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'i', 'k', 'i', 'w', 'i', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(words = ['kitten', 'puppy', 'dog', 'cat'],letters = ['a', 'c', 'd', 'd', 'd', 'g', 'k', 'n', 'o', 'p', 'p', 'p', 'p', 'p', 't', 'u', 'y', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['kitten', 'puppy', 'dog', 'cat'],letters = ['a', 'c', 'd', 'd', 'd', 'g', 'k', 'n', 'o', 'p', 'p', 'p', 'p', 'p', 't', 'u', 'y', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'python', 'java'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'python', 'java'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'h', 'i', 'l', 'n', 'n', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'h', 'i', 'l', 'n', 'n', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'elephant', 'giraffe'],letters = ['z', 'e', 'b', 'r', 'a', 'e', 'l', 'p', 'h', 'a', 'n', 't', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [5, 1, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'elephant', 'giraffe'],letters = ['z', 'e', 'b', 'r', 'a', 'e', 'l', 'p', 'h', 'a', 'n', 't', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [5, 1, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 'u', 'u', 'x', 'y', 'y', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 'u', 'u', 'x', 'y', 'y', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complexity', 'theory', 'graph', 'tree'],letters = ['a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 's', 't', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complexity', 'theory', 'graph', 'tree'],letters = ['a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 's', 't', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 249: {e}')
    
    total += 1
    try:
        result = candidate(words = ['expert', 'knowledge', 'skill'],letters = ['e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['expert', 'knowledge', 'skill'],letters = ['e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'b', 'b', 'c', 'c', 'e', 'e', 'h', 'n', 'n', 'p', 'p', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 5, 9, 7]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'b', 'b', 'c', 'c', 'e', 'e', 'h', 'n', 'n', 'p', 'p', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 5, 9, 7]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'contest', 'challenge'],letters = ['p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'n', 't', 'e', 's', 't', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [3, 5, 1, 3, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 8, 7, 5, 4, 4, 3, 7, 2, 9, 4]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'contest', 'challenge'],letters = ['p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'n', 't', 'e', 's', 't', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [3, 5, 1, 3, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 8, 7, 5, 4, 4, 3, 7, 2, 9, 4]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'extraordinary', 'amazing'],letters = ['f', 'a', 'n', 't', 'a', 's', 't', 'i', 'c', 'e', 'x', 't', 'r', 'o', 'd', 'i', 'n', 'a', 'r', 'y', 'a', 'm', 'a', 'z', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'extraordinary', 'amazing'],letters = ['f', 'a', 'n', 't', 'a', 's', 't', 'i', 'c', 'e', 'x', 't', 'r', 'o', 'd', 'i', 'n', 'a', 'r', 'y', 'a', 'm', 'a', 'z', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(words = ['complex', 'challenging', 'problems', 'solutions'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'i', 'n', 'g', 'p', 'r', 'o', 'b', 'l', 'e', 'm', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['complex', 'challenging', 'problems', 'solutions'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'i', 'n', 'g', 'p', 'r', 'o', 'b', 'l', 'e', 'm', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(words = ['backtracking', 'heuristic', 'algorithm', 'search'],letters = ['b', 'a', 'c', 'k', 't', 'r', 'a', 'c', 'k', 'i', 'n', 'g', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 's', 'e', 'a', 'r', 'c', 'h'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['backtracking', 'heuristic', 'algorithm', 'search'],letters = ['b', 'a', 'c', 'k', 't', 'r', 'a', 'c', 'k', 'i', 'n', 'g', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 's', 'e', 'a', 'r', 'c', 'h'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(words = ['fantastic', 'breathtaking', 'transformation', 'unbelievable'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'r', 'r', 's', 't', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['fantastic', 'breathtaking', 'transformation', 'unbelievable'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'r', 'r', 's', 't', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'java', 'csharp', 'javascript'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'j', 'k', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'q', 'r', 's', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'java', 'csharp', 'javascript'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'j', 'k', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'q', 'r', 's', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'algorithm', 'data', 'structure'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 't', 'u', 'v', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'algorithm', 'data', 'structure'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 't', 'u', 'v', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'xylophone', 'quartz', 'jigsaw'],letters = ['a', 'a', 'e', 'g', 'h', 'i', 'j', 'j', 'k', 'l', 'o', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'xylophone', 'quartz', 'jigsaw'],letters = ['a', 'a', 'e', 'g', 'h', 'i', 'j', 'j', 'k', 'l', 'o', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(words = ['wizard', 'oracle', 'sorcerer'],letters = ['w', 'i', 'z', 'a', 'r', 'd', 'o', 'r', 'a', 'c', 'l', 'e', 's', 'o', 'r', 'c', 'e', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['wizard', 'oracle', 'sorcerer'],letters = ['w', 'i', 'z', 'a', 'r', 'd', 'o', 'r', 'a', 'c', 'l', 'e', 's', 'o', 'r', 'c', 'e', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [4, 5, 1, 2, 4, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [4, 5, 1, 2, 4, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(words = ['greedy', 'algorithm', 'optimization', 'heuristic'],letters = ['g', 'r', 'e', 'e', 'd', 'y', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['greedy', 'algorithm', 'optimization', 'heuristic'],letters = ['g', 'r', 'e', 'e', 'd', 'y', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'code', 'hackathon', 'python'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'd', 'e', 'h', 'a', 'c', 'k', 'a', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'code', 'hackathon', 'python'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'd', 'e', 'h', 'a', 'c', 'k', 'a', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(words = ['orange', 'grape', 'apple', 'banana'],letters = ['a', 'a', 'a', 'b', 'e', 'g', 'n', 'n', 'n', 'o', 'p', 'r', 'r', 'r', 's', 't', 'u', 'u', 'u', 'u', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['orange', 'grape', 'apple', 'banana'],letters = ['a', 'a', 'a', 'b', 'e', 'g', 'n', 'n', 'n', 'o', 'p', 'r', 'r', 'r', 's', 't', 'u', 'u', 'u', 'u', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(words = ['interview', 'question', 'programming', 'challenge'],letters = ['i', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [1, 2, 3, 4, 5, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['interview', 'question', 'programming', 'challenge'],letters = ['i', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [1, 2, 3, 4, 5, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 175: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abacax', 'banana', 'cherry'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y', 'a', 'b', 'a', 'c', 'a', 'x'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abacax', 'banana', 'cherry'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y', 'a', 'b', 'a', 'c', 'a', 'x'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 142: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'x', 'y', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 9, 7, 5, 3, 2, 1, 6, 4, 2, 9, 7, 5, 3, 2, 1, 6, 4, 2]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'x', 'y', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 9, 7, 5, 3, 2, 1, 6, 4, 2, 9, 7, 5, 3, 2, 1, 6, 4, 2]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abracadabra', 'alakazam', 'sorcery', 'spellbound'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'i', 'l', 'l', 'l', 'm', 'o', 'o', 'o', 'p', 'r', 'r', 'r', 's', 's', 't', 'u', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abracadabra', 'alakazam', 'sorcery', 'spellbound'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'i', 'l', 'l', 'l', 'm', 'o', 'o', 'o', 'p', 'r', 'r', 'r', 's', 's', 't', 'u', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghij', 'klmnopqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghij', 'klmnopqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefghij', 'jihgfedcba', 'mnopqrstuv'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefghij', 'jihgfedcba', 'mnopqrstuv'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'n', 'n', 'r', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'n', 'n', 'r', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'resource', 'constraint', 'solution'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e', 'c', 'o', 'n', 's', 't', 'r', 'a', 'i', 'n', 't', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'resource', 'constraint', 'solution'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e', 'c', 'o', 'n', 's', 't', 'r', 'a', 'i', 'n', 't', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 169: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcdefg', 'hijklmnop', 'qrstuvwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcdefg', 'hijklmnop', 'qrstuvwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(words = ['quantum', 'computing', 'artificial', 'intelligence'],letters = ['q', 'u', 'a', 'n', 't', 'u', 'm', 'c', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g', 'a', 'r', 't', 'i', 'f', 'i', 'c', 'i', 'a', 'l', 'i', 'n', 't', 'e', 'l', 'l', 'i', 'g', 'e', 'n', 'c', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quantum', 'computing', 'artificial', 'intelligence'],letters = ['q', 'u', 'a', 'n', 't', 'u', 'm', 'c', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g', 'a', 'r', 't', 'i', 'f', 'i', 'c', 'i', 'a', 'l', 'i', 'n', 't', 'e', 'l', 'l', 'i', 'g', 'e', 'n', 'c', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'challenge', 'solution'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'challenge', 'solution'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabbcc', 'ddeeff', 'gghhii'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabbcc', 'ddeeff', 'gghhii'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'g', 'h', 'i', 'n', 'n', 'p', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'g', 'h', 'i', 'n', 'n', 'p', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'grape', 'orange'],letters = ['a', 'a', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'g', 'r', 'a', 'p', 'e', 'o', 'r', 'a', 'n', 'g', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'grape', 'orange'],letters = ['a', 'a', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'g', 'r', 'a', 'p', 'e', 'o', 'r', 'a', 'n', 'g', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(words = ['xylophone', 'violin', 'guitar'],letters = ['x', 'y', 'l', 'o', 'p', 'h', 'o', 'n', 'e', 'v', 'i', 'o', 'l', 'i', 'n', 'g', 'u', 'i', 't', 'a', 'r'],score = [8, 24, 12, 15, 15, 19, 6, 9, 8, 4, 4, 8, 9, 9, 5, 14, 9, 7, 8, 6, 5, 7, 4, 6, 10, 10]) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xylophone', 'violin', 'guitar'],letters = ['x', 'y', 'l', 'o', 'p', 'h', 'o', 'n', 'e', 'v', 'i', 'o', 'l', 'i', 'n', 'g', 'u', 'i', 't', 'a', 'r'],score = [8, 24, 12, 15, 15, 19, 6, 9, 8, 4, 4, 8, 9, 9, 5, 14, 9, 7, 8, 6, 5, 7, 4, 6, 10, 10]) == 166: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'is', 'fun', 'and', 'educational'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'p', 'p', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'is', 'fun', 'and', 'educational'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'p', 'p', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(words = ['optimization', 'performance', 'scalability'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['optimization', 'performance', 'scalability'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(words = ['zebra', 'giraffe', 'hippo'],letters = ['z', 'e', 'b', 'r', 'a', 'g', 'i', 'r', 'a', 'f', 'f', 'e', 'h', 'i', 'p', 'p', 'o'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zebra', 'giraffe', 'hippo'],letters = ['z', 'e', 'b', 'r', 'a', 'g', 'i', 'r', 'a', 'f', 'f', 'e', 'h', 'i', 'p', 'p', 'o'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'h', 'e', 'r', 'r', 'y', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'h', 'e', 'r', 'r', 'y', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcd', 'dcba', 'bacd', 'cadb'],letters = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcd', 'dcba', 'bacd', 'cadb'],letters = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'python', 'java', 'code'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'c', 'o', 'd', 'e'],score = [3, 1, 3, 7, 2, 2, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'python', 'java', 'code'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'c', 'o', 'd', 'e'],score = [3, 1, 3, 7, 2, 2, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 3, 2, 2, 1, 2, 3, 5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 4, 2, 4, 1, 6, 2, 5, 3, 5]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 3, 2, 2, 1, 2, 3, 5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 4, 2, 4, 1, 6, 2, 5, 3, 5]) == 59: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['xxxz', 'ax', 'bx', 'cx'],letters = ['z', 'a', 'b', 'c', 'x', 'x', 'x'],score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]) == 27
    assert candidate(words = ['leetcode'],letters = ['l', 'e', 't', 'c', 'o', 'd'],score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(words = ['dog', 'cat', 'dad', 'good'],letters = ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'],score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 23
    assert candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 659
    assert candidate(words = ['dynamic', 'programming', 'complexity', 'analysis'],letters = ['d', 'y', 'n', 'a', 'm', 'i', 'c', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'm', 'p', 'l', 'e', 'x', 'i', 't', 'y', 'a', 'n', 'a', 'l', 'y', 's', 'i', 's'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 184
    assert candidate(words = ['quartz', 'pearl', 'opal'],letters = ['q', 'u', 'a', 'r', 't', 'z', 'p', 'e', 'a', 'r', 'l', 'o', 'p', 'a', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
    assert candidate(words = ['programming', 'code', 'python', 'challenge'],letters = ['a', 'c', 'd', 'e', 'e', 'g', 'h', 'i', 'l', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 'r', 's', 't', 'u', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
    assert candidate(words = ['university', 'college', 'school'],letters = ['u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y', 'c', 'o', 'l', 'l', 'e', 'g', 'e', 's', 'c', 'h', 'o', 'o', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
    assert candidate(words = ['complex', 'example', 'test'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'e', 'a', 'm', 'p', 'l', 'e', 't', 'e', 's', 't', 'c', 'o', 'm', 'p', 'l', 'e', 'x'],score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]) == 2280
    assert candidate(words = ['zebra', 'elephant', 'giraffe', 'hippo'],letters = ['a', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'l', 'n', 'o', 'p', 'p', 'r', 'r', 's', 't', 'u', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 13
    assert candidate(words = ['kangaroo', 'koala', 'hippopotamus'],letters = ['k', 'a', 'n', 'g', 'a', 'r', 'o', 'o', 'o', 'o', 'l', 'i', 'p', 'p', 'o', 't', 'a', 'm', 'u', 's'],score = [8, 1, 13, 3, 1, 1, 1, 1, 1, 1, 4, 1, 5, 9, 7, 6, 5, 3, 0, 9, 0, 5, 5, 0, 0, 0]) == 47
    assert candidate(words = ['optimization', 'performance', 'scalability', 'expert', 'knowledge', 'skill'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y', 'e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 118
    assert candidate(words = ['onomatopoeia', 'palindrome', 'multifarious'],letters = ['o', 'n', 'o', 'm', 'a', 't', 'o', 'p', 'o', 'e', 'i', 'a', 'p', 'a', 'l', 'i', 'n', 'd', 'r', 'o', 'm', 'e', 'm', 'u', 'l', 't', 'i', 'f', 'a', 'r', 'i', 'o', 'u', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56
    assert candidate(words = ['abcd', 'abcde', 'abcdef', 'abcdefg'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 74
    assert candidate(words = ['optimization', 'performance', 'efficiency'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 'e', 'f', 'f', 'i', 'c', 'i', 'e', 'n', 'c', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 66
    assert candidate(words = ['mississippi', 'alabama', 'tennessee'],letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i', 'a', 'l', 'a', 'b', 'a', 'm', 'a', 't', 'e', 'n', 'n', 'e', 's', 's', 'e'],score = [3, 1, 9, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 5, 5, 0, 2, 3, 9]) == 88
    assert candidate(words = ['zzzz', 'zzz', 'zz', 'z'],letters = ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 260
    assert candidate(words = ['algorithm', 'datastructure', 'machinelearning'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'm', 'a', 'c', 'h', 'i', 'n', 'e', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 65
    assert candidate(words = ['amazing', 'zebra', 'apple'],letters = ['a', 'm', 'a', 'z', 'i', 'n', 'g', 'z', 'e', 'b', 'r', 'a', 'a', 'p', 'p', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 38
    assert candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 274
    assert candidate(words = ['syzygy', 'zygote', 'zygomycete'],letters = ['s', 'y', 'z', 'y', 'g', 'y', 'z', 'y', 'g', 'o', 't', 'e', 'z', 'y', 'g', 'o', 'm', 'y', 'c', 'e', 't', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 56
    assert candidate(words = ['zebra', 'monkey', 'giraffe'],letters = ['z', 'e', 'r', 'b', 'a', 'o', 'n', 'k', 'm', 'y', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [1, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0]) == 12
    assert candidate(words = ['algorithm', 'data', 'structure', 'software'],letters = ['a', 'a', 'a', 'c', 'd', 'd', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'o', 'r', 's', 's', 's', 't', 'u', 'w', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 15
    assert candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 301
    assert candidate(words = ['abacaxi', 'kiwi', 'pineapple'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'i', 'k', 'i', 'w', 'i', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 41
    assert candidate(words = ['kitten', 'puppy', 'dog', 'cat'],letters = ['a', 'c', 'd', 'd', 'd', 'g', 'k', 'n', 'o', 'p', 'p', 'p', 'p', 'p', 't', 'u', 'y', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
    assert candidate(words = ['hello', 'world', 'python', 'java'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 26
    assert candidate(words = ['algorithm', 'data', 'structure'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 33
    assert candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'h', 'i', 'l', 'n', 'n', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5
    assert candidate(words = ['zebra', 'elephant', 'giraffe'],letters = ['z', 'e', 'b', 'r', 'a', 'e', 'l', 'p', 'h', 'a', 'n', 't', 'g', 'i', 'r', 'a', 'f', 'f', 'e'],score = [5, 1, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 36
    assert candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 'u', 'u', 'x', 'y', 'y', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 32
    assert candidate(words = ['complexity', 'theory', 'graph', 'tree'],letters = ['a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 's', 't', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 19
    assert candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 249
    assert candidate(words = ['expert', 'knowledge', 'skill'],letters = ['e', 'x', 'p', 'e', 'r', 't', 'k', 'n', 'o', 'w', 'l', 'e', 'd', 'g', 'e', 's', 'k', 'i', 'l', 'l'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 45
    assert candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'b', 'b', 'c', 'c', 'e', 'e', 'h', 'n', 'n', 'p', 'p', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 5, 9, 7]) == 17
    assert candidate(words = ['programming', 'contest', 'challenge'],letters = ['p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'n', 't', 'e', 's', 't', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [3, 5, 1, 3, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 8, 7, 5, 4, 4, 3, 7, 2, 9, 4]) == 60
    assert candidate(words = ['fantastic', 'extraordinary', 'amazing'],letters = ['f', 'a', 'n', 't', 'a', 's', 't', 'i', 'c', 'e', 'x', 't', 'r', 'o', 'd', 'i', 'n', 'a', 'r', 'y', 'a', 'm', 'a', 'z', 'i', 'n', 'g'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 39
    assert candidate(words = ['complex', 'challenging', 'problems', 'solutions'],letters = ['c', 'o', 'm', 'p', 'l', 'e', 'x', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'i', 'n', 'g', 'p', 'r', 'o', 'b', 'l', 'e', 'm', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 54
    assert candidate(words = ['backtracking', 'heuristic', 'algorithm', 'search'],letters = ['b', 'a', 'c', 'k', 't', 'r', 'a', 'c', 'k', 'i', 'n', 'g', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 's', 'e', 'a', 'r', 'c', 'h'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 165
    assert candidate(words = ['fantastic', 'breathtaking', 'transformation', 'unbelievable'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'p', 'r', 'r', 's', 't', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 25
    assert candidate(words = ['python', 'java', 'csharp', 'javascript'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'j', 'k', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'q', 'r', 's', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 38
    assert candidate(words = ['optimization', 'algorithm', 'data', 'structure'],letters = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'g', 'h', 'i', 'i', 'l', 'm', 'n', 'o', 'o', 'p', 'p', 'r', 's', 't', 't', 'u', 'v', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 20
    assert candidate(words = ['zebra', 'xylophone', 'quartz', 'jigsaw'],letters = ['a', 'a', 'e', 'g', 'h', 'i', 'j', 'j', 'k', 'l', 'o', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 41
    assert candidate(words = ['wizard', 'oracle', 'sorcerer'],letters = ['w', 'i', 'z', 'a', 'r', 'd', 'o', 'r', 'a', 'c', 'l', 'e', 's', 'o', 'r', 'c', 'e', 'r', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 27
    assert candidate(words = ['hello', 'world', 'python', 'code'],letters = ['h', 'e', 'l', 'l', 'o', 'w', 'r', 'd', 'p', 'y', 't', 'h', 'o', 'n', 'c', 'o', 'd', 'e'],score = [4, 5, 1, 2, 4, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 190
    assert candidate(words = ['abcdefg', 'hijklmn', 'opqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
    assert candidate(words = ['greedy', 'algorithm', 'optimization', 'heuristic'],letters = ['g', 'r', 'e', 'e', 'd', 'y', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'h', 'e', 'u', 'r', 'i', 's', 't', 'i', 'c'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 188
    assert candidate(words = ['programming', 'code', 'hackathon', 'python'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'o', 'd', 'e', 'h', 'a', 'c', 'k', 'a', 't', 'h', 'o', 'n', 'p', 'y', 't', 'h', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 67
    assert candidate(words = ['orange', 'grape', 'apple', 'banana'],letters = ['a', 'a', 'a', 'b', 'e', 'g', 'n', 'n', 'n', 'o', 'p', 'r', 'r', 'r', 's', 't', 'u', 'u', 'u', 'u', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 8
    assert candidate(words = ['interview', 'question', 'programming', 'challenge'],letters = ['i', 'n', 't', 'e', 'r', 'v', 'i', 'e', 'w', 'q', 'u', 'e', 's', 't', 'i', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e'],score = [1, 2, 3, 4, 5, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]) == 175
    assert candidate(words = ['abacax', 'banana', 'cherry'],letters = ['a', 'b', 'a', 'c', 'a', 'x', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y', 'a', 'b', 'a', 'c', 'a', 'x'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 142
    assert candidate(words = ['xylophone', 'guitar', 'piano', 'drums'],letters = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'e', 'e', 'e', 'f', 'g', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'q', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'x', 'y', 'y', 'z', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 9, 7, 5, 3, 2, 1, 6, 4, 2, 9, 7, 5, 3, 2, 1, 6, 4, 2]) == 39
    assert candidate(words = ['abracadabra', 'alakazam', 'sorcery', 'spellbound'],letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'i', 'l', 'l', 'l', 'm', 'o', 'o', 'o', 'p', 'r', 'r', 'r', 's', 's', 't', 'u', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 18
    assert candidate(words = ['supercalifragilisticexpialidocious', 'antidisestablishmentarianism', 'floccinaucinihilipilification'],letters = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's', 'a', 'n', 't', 'i', 'd', 'i', 's', 'e', 't', 'a', 'b', 'l', 'i', 's', 'h', 'm', 'e', 'n', 't', 'a', 'r', 'i', 'a', 'n', 'i', 's', 'm', 'f', 'l', 'o', 'c', 'c', 'i', 'n', 'a', 'u', 'c', 'i', 'n', 'i', 'h', 'i', 'l', 'i', 'p', 'i', 'l', 'i', 'f', 'i', 'c', 'a', 't', 'i', 'o', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 10]) == 112
    assert candidate(words = ['abcdefghij', 'klmnopqrstu', 'vwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 74
    assert candidate(words = ['abcdefghij', 'jihgfedcba', 'mnopqrstuv'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]) == 110
    assert candidate(words = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 90
    assert candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'n', 'n', 'r', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 14
    assert candidate(words = ['optimization', 'resource', 'constraint', 'solution'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e', 'c', 'o', 'n', 's', 't', 'r', 'a', 'i', 'n', 't', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 169
    assert candidate(words = ['abcdefg', 'hijklmnop', 'qrstuvwxyz'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 351
    assert candidate(words = ['quantum', 'computing', 'artificial', 'intelligence'],letters = ['q', 'u', 'a', 'n', 't', 'u', 'm', 'c', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g', 'a', 'r', 't', 'i', 'f', 'i', 'c', 'i', 'a', 'l', 'i', 'n', 't', 'e', 'l', 'l', 'i', 'g', 'e', 'n', 'c', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 79
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136
    assert candidate(words = ['programming', 'challenge', 'solution'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 28
    assert candidate(words = ['aabbcc', 'ddeeff', 'gghhii'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],score = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 18
    assert candidate(words = ['apple', 'banana', 'cherry', 'date'],letters = ['a', 'b', 'c', 'd', 'e', 'e', 'e', 'g', 'h', 'i', 'n', 'n', 'p', 'p', 'r', 't', 'u'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 5
    assert candidate(words = ['apple', 'banana', 'grape', 'orange'],letters = ['a', 'a', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'g', 'r', 'a', 'p', 'e', 'o', 'r', 'a', 'n', 'g', 'e'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 24
    assert candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34
    assert candidate(words = ['xylophone', 'violin', 'guitar'],letters = ['x', 'y', 'l', 'o', 'p', 'h', 'o', 'n', 'e', 'v', 'i', 'o', 'l', 'i', 'n', 'g', 'u', 'i', 't', 'a', 'r'],score = [8, 24, 12, 15, 15, 19, 6, 9, 8, 4, 4, 8, 9, 9, 5, 14, 9, 7, 8, 6, 5, 7, 4, 6, 10, 10]) == 166
    assert candidate(words = ['programming', 'is', 'fun', 'and', 'educational'],letters = ['a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g', 'h', 'i', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'p', 'p', 'p', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 5]) == 30
    assert candidate(words = ['optimization', 'performance', 'scalability'],letters = ['o', 'p', 't', 'i', 'm', 'i', 'z', 'a', 't', 'i', 'o', 'n', 'p', 'e', 'r', 'f', 'o', 'r', 'm', 'a', 'n', 'c', 'e', 's', 'c', 'a', 'l', 'a', 'b', 'i', 'l', 'i', 't', 'y'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 4, 8, 8, 10]) == 73
    assert candidate(words = ['abcd', 'efgh', 'ijkl', 'mnop'],letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 136
    assert candidate(words = ['zebra', 'giraffe', 'hippo'],letters = ['z', 'e', 'b', 'r', 'a', 'g', 'i', 'r', 'a', 'f', 'f', 'e', 'h', 'i', 'p', 'p', 'o'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 2, 4, 2, 4, 1, 2]) == 34
    assert candidate(words = ['apple', 'banana', 'cherry'],letters = ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'h', 'e', 'r', 'r', 'y', 'n'],score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]) == 14
    assert candidate(words = ['abcd', 'dcba', 'bacd', 'cadb'],letters = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]) == 40
    assert candidate(words = ['programming', 'python', 'java', 'code'],letters = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'c', 'o', 'd', 'e'],score = [3, 1, 3, 7, 2, 2, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1, 4, 6, 5, 3, 5, 1, 3, 7, 2, 1]) == 89
    assert candidate(words = ['algorithm', 'data', 'structure', 'code'],letters = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', 'd', 'a', 't', 'a', 's', 't', 'r', 'u', 'c', 't', 'u', 'r', 'e', 'c', 'o', 'd', 'e'],score = [1, 3, 2, 2, 1, 2, 3, 5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 4, 2, 4, 1, 6, 2, 5, 3, 5]) == 59


