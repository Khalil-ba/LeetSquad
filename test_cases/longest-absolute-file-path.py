def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20: {e}')
    
    total += 1
    try:
        result = candidate(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32: {e}')
    
    total += 1
    try:
        result = candidate(input = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(input = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(input = "file1.txt\nfile2.txt\nlongfile.txt") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(input = "file1.txt\nfile2.txt\nlongfile.txt") == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
    assert candidate(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
    assert candidate(input = "a") == 0
    assert candidate(input = "file1.txt\nfile2.txt\nlongfile.txt") == 12


