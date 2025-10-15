def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,logs = ['0:start:0', '0:end:1']) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,logs = ['0:start:0', '0:end:1']) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:end:7']) == [2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:end:7']) == [2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '2:start:3', '2:end:4', '3:start:5', '3:end:6', '0:end:7']) == [2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '2:start:3', '2:end:4', '3:start:5', '3:end:6', '0:end:7']) == [2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:end:2', '0:end:3']) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:end:2', '0:end:3']) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,logs = ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,logs = ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']) == [7, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']) == [7, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:9', '2:start:10', '2:end:12', '0:end:13']) == [7, 4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:9', '2:start:10', '2:end:12', '0:end:13']) == [7, 4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '1:start:2', '1:end:5', '0:end:6']) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '1:start:2', '1:end:5', '0:end:6']) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7']) == [4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7']) == [4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [4, 3, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [4, 3, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '1:end:7', '0:end:8', '4:start:9', '4:end:10']) == [3, 4, 2, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '1:end:7', '0:end:8', '4:start:9', '4:end:10']) == [3, 4, 2, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '5:end:6', '4:end:7', '3:end:8', '2:end:9', '1:end:10', '0:end:11']) == [2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '5:end:6', '4:end:7', '3:end:8', '2:end:9', '1:end:10', '0:end:11']) == [2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7', '3:start:8', '3:start:9', '3:end:10', '3:end:11', '2:end:12', '0:end:13']) == [4, 4, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7', '3:start:8', '3:start:9', '3:end:10', '3:end:11', '2:end:12', '0:end:13']) == [4, 4, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '6:end:7', '5:end:8', '4:end:9', '3:end:10', '2:end:11', '1:end:12', '0:end:13']) == [2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '6:end:7', '5:end:8', '4:end:9', '3:end:10', '2:end:11', '1:end:12', '0:end:13']) == [2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:end:7', '2:start:8', '2:end:9']) == [6, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:end:7', '2:start:8', '2:end:9']) == [6, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:start:9', '1:end:10', '1:end:11', '2:start:12', '2:end:13']) == [8, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:start:9', '1:end:10', '1:end:11', '2:start:12', '2:end:13']) == [8, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '4:start:10', '4:end:11']) == [1, 5, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '4:start:10', '4:end:11']) == [1, 5, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:7', '0:end:9', '1:start:10', '1:end:11', '2:start:12', '2:end:13']) == [10, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:7', '0:end:9', '1:start:10', '1:end:11', '2:start:12', '2:end:13']) == [10, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7', '2:start:8', '2:start:9', '2:end:10', '2:end:11', '0:start:12', '0:end:13']) == [4, 6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7', '2:start:8', '2:start:9', '2:end:10', '2:end:11', '0:start:12', '0:end:13']) == [4, 6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:end:9']) == [8, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:end:9']) == [8, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '0:start:6', '2:start:7', '2:end:8', '0:end:9', '0:end:10', '3:start:11', '3:end:12', '0:start:13', '0:end:14']) == [9, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '0:start:6', '2:start:7', '2:end:8', '0:end:9', '0:end:10', '3:start:11', '3:end:12', '0:start:13', '0:end:14']) == [9, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [3, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [3, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '2:start:6', '2:end:9', '0:end:10', '3:start:11', '4:start:12', '4:end:14', '3:end:15']) == [4, 3, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '2:start:6', '2:end:9', '0:end:10', '3:start:11', '4:start:12', '4:end:14', '3:end:15']) == [4, 3, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '1:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:start:8', '3:end:9', '3:end:10']) == [1, 4, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '1:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:start:8', '3:end:9', '3:end:10']) == [1, 4, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '7:start:7', '8:start:8', '9:start:9', '9:end:11', '8:end:12', '7:end:13', '6:end:14', '5:end:15', '4:end:16', '3:end:17', '2:end:18', '1:end:19', '0:end:20']) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '7:start:7', '8:start:8', '9:start:9', '9:end:11', '8:end:12', '7:end:13', '6:end:14', '5:end:15', '4:end:16', '3:end:17', '2:end:18', '1:end:19', '0:end:20']) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:start:7', '3:start:8', '3:end:9', '2:end:10', '2:end:11', '0:end:12', '4:start:13', '4:end:14', '5:start:15', '5:end:16']) == [5, 2, 4, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:start:7', '3:start:8', '3:end:9', '2:end:10', '2:end:11', '0:end:12', '4:start:13', '4:end:14', '5:start:15', '5:end:16']) == [5, 2, 4, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10']) == [1, 6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10']) == [1, 6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '2:start:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '0:end:11']) == [4, 2, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '2:start:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '0:end:11']) == [4, 2, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,logs = ['0:start:0', '0:start:2', '0:end:3', '1:start:4', '1:start:6', '1:end:7', '1:end:9', '0:end:10']) == [5, 6, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,logs = ['0:start:0', '0:start:2', '0:end:3', '1:start:4', '1:start:6', '1:end:7', '1:end:9', '0:end:10']) == [5, 6, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '0:end:6', '0:end:7', '2:start:8', '2:start:9', '2:start:10', '2:end:11', '2:end:12', '2:end:13', '0:start:14', '0:end:15']) == [6, 4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '0:end:6', '0:end:7', '2:start:8', '2:start:9', '2:start:10', '2:end:11', '2:end:12', '2:end:13', '0:start:14', '0:end:15']) == [6, 4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:6', '0:end:7']) == [8, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:6', '0:end:7']) == [8, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:start:4', '1:start:5', '2:start:6', '2:start:7', '2:end:8', '2:end:9', '1:end:10', '1:end:11', '1:end:12', '0:end:13', '0:end:14', '0:end:15', '3:start:16', '3:end:17', '4:start:18', '4:end:19', '5:start:20', '5:end:21', '6:start:22', '6:end:23']) == [6, 6, 4, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:start:4', '1:start:5', '2:start:6', '2:start:7', '2:end:8', '2:end:9', '1:end:10', '1:end:11', '1:end:12', '0:end:13', '0:end:14', '0:end:15', '3:start:16', '3:end:17', '4:start:18', '4:end:19', '5:start:20', '5:end:21', '6:start:22', '6:end:23']) == [6, 6, 4, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6']) == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6']) == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:start:8', '1:end:9', '1:end:10', '1:end:11', '2:start:12', '2:start:13', '2:start:14', '2:end:15', '2:end:16', '2:end:17', '3:start:18', '3:start:19', '3:start:20', '3:end:21', '3:end:22', '3:end:23']) == [6, 6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:start:8', '1:end:9', '1:end:10', '1:end:11', '2:start:12', '2:start:13', '2:start:14', '2:end:15', '2:end:16', '2:end:17', '3:start:18', '3:start:19', '3:start:20', '3:end:21', '3:end:22', '3:end:23']) == [6, 6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '4:start:8', '4:end:9', '1:start:10', '1:end:11', '0:end:12']) == [1, 6, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '4:start:8', '4:end:9', '1:start:10', '1:end:11', '0:end:12']) == [1, 6, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '2:start:9', '2:end:10', '0:end:11']) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '2:start:9', '2:end:10', '0:end:11']) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '0:end:6']) == [3, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '0:end:6']) == [3, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:4', '3:start:6', '3:end:8', '2:end:10', '1:end:12', '0:end:14']) == [4, 4, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:4', '3:start:6', '3:end:8', '2:end:10', '1:end:12', '0:end:14']) == [4, 4, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:start:7', '3:end:8', '3:end:9']) == [2, 2, 2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:start:7', '3:end:8', '3:end:9']) == [2, 2, 2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '1:start:11', '2:start:12', '3:start:13', '4:start:14', '4:end:15', '3:end:16', '2:end:17', '1:end:18', '0:end:19']) == [4, 4, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '1:start:11', '2:start:12', '3:start:13', '4:start:14', '4:end:15', '3:end:16', '2:end:17', '1:end:18', '0:end:19']) == [4, 4, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7']) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7']) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '0:end:7', '3:start:8', '4:start:9', '4:end:10', '3:end:11', '0:start:12', '0:end:13']) == [6, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '0:end:7', '3:start:8', '4:start:9', '4:end:10', '3:end:11', '0:start:12', '0:end:13']) == [6, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '1:end:6', '0:end:7', '0:end:8', '2:start:9', '2:end:10']) == [5, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '1:end:6', '0:end:7', '0:end:8', '2:start:9', '2:end:10']) == [5, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '0:start:6', '0:start:7', '0:end:8', '0:end:9']) == [10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '0:start:6', '0:start:7', '0:end:8', '0:end:9']) == [10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:5', '1:end:6', '0:end:7', '3:start:8', '3:start:9', '4:start:10', '4:end:12', '3:end:13', '5:start:14', '5:end:16']) == [1, 4, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:5', '1:end:6', '0:end:7', '3:start:8', '3:start:9', '4:start:10', '4:end:12', '3:end:13', '5:start:14', '5:end:16']) == [1, 4, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:end:8', '0:end:9']) == [2, 6, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:end:8', '0:end:9']) == [2, 6, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '1:end:3', '2:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '1:end:3', '2:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:end:8', '2:start:9', '2:end:10', '1:start:11', '1:end:12', '0:start:13', '0:end:14']) == [3, 4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:end:8', '2:start:9', '2:end:10', '1:start:11', '1:end:12', '0:start:13', '0:end:14']) == [3, 4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '2:start:4', '2:end:5', '1:end:6', '1:end:7', '0:end:8', '3:start:9', '3:end:10', '4:start:11', '4:end:12']) == [3, 4, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '2:start:4', '2:end:5', '1:end:6', '1:end:7', '0:end:8', '3:start:9', '3:end:10', '4:start:11', '4:end:12']) == [3, 4, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:start:5', '2:end:6', '1:start:7', '1:end:8', '0:end:9']) == [2, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:start:5', '2:end:6', '1:start:7', '1:end:8', '0:end:9']) == [2, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:end:8', '1:end:9', '2:start:10', '2:end:11']) == [6, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:end:8', '1:end:9', '2:start:10', '2:end:11']) == [6, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [4, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [4, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '0:end:10', '4:start:11', '4:end:12', '5:start:13', '5:end:14']) == [5, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '0:end:10', '4:start:11', '4:end:12', '5:start:13', '5:end:14']) == [5, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [3, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [3, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:start:10', '0:end:11']) == [4, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:start:10', '0:end:11']) == [4, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:start:8', '3:start:9', '3:end:11', '2:end:12', '2:end:13', '4:start:14', '4:end:16', '5:start:17', '5:end:19', '6:start:20', '6:end:22']) == [4, 3, 4, 3, 3, 3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:start:8', '3:start:9', '3:end:11', '2:end:12', '2:end:13', '4:start:14', '4:end:16', '5:start:17', '5:end:19', '6:start:20', '6:end:22']) == [4, 3, 4, 3, 3, 3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:start:3', '3:start:4', '3:end:5', '2:end:6', '2:end:7', '1:end:8', '0:end:9', '4:start:10', '4:end:11']) == [2, 2, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:start:3', '3:start:4', '3:end:5', '2:end:6', '2:end:7', '1:end:8', '0:end:9', '4:start:10', '4:end:11']) == [2, 2, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '4:start:8', '4:end:9', '3:end:10', '0:start:11', '1:start:12', '2:start:13', '2:end:14', '1:end:15', '0:end:16']) == [3, 6, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '4:start:8', '4:end:9', '3:end:10', '0:start:11', '1:start:12', '2:start:13', '2:end:14', '1:end:15', '0:end:16']) == [3, 6, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:end:2', '1:start:3', '1:end:4', '0:start:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [5, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:end:2', '1:start:3', '1:end:4', '0:start:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [5, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '0:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10', '3:start:11', '3:end:12', '4:start:13', '4:end:14']) == [5, 2, 4, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '0:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10', '3:start:11', '3:end:12', '4:start:13', '4:end:14']) == [5, 2, 4, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '0:start:3', '2:start:4', '2:end:5', '0:start:6', '3:start:7', '3:end:8', '0:start:9', '2:start:10', '2:end:11', '0:start:12', '1:start:13', '1:end:14', '0:end:15', '0:start:16', '2:start:17', '2:end:18', '0:end:19']) == [8, 4, 6, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '0:start:3', '2:start:4', '2:end:5', '0:start:6', '3:start:7', '3:end:8', '0:start:9', '2:start:10', '2:end:11', '0:start:12', '1:start:13', '1:end:14', '0:end:15', '0:start:16', '2:start:17', '2:end:18', '0:end:19']) == [8, 4, 6, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [6, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [6, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '1:start:8', '1:end:9', '0:end:10']) == [1, 6, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '1:start:8', '1:end:9', '0:end:10']) == [1, 6, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:end:10']) == [3, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:end:10']) == [3, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,logs = ['0:start:0', '0:end:1']) == [2]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:end:7']) == [2, 2, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '2:start:3', '2:end:4', '3:start:5', '3:end:6', '0:end:7']) == [2, 2, 2, 2]
    assert candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:end:2', '0:end:3']) == [2, 2]
    assert candidate(n = 1,logs = ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']) == [8]
    assert candidate(n = 2,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']) == [7, 1]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:9', '2:start:10', '2:end:12', '0:end:13']) == [7, 4, 3]
    assert candidate(n = 2,logs = ['0:start:0', '1:start:2', '1:end:5', '0:end:6']) == [3, 4]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7']) == [4, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [4, 3, 2]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]
    assert candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '1:end:7', '0:end:8', '4:start:9', '4:end:10']) == [3, 4, 2, 0, 2]
    assert candidate(n = 6,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '5:end:6', '4:end:7', '3:end:8', '2:end:9', '1:end:10', '0:end:11']) == [2, 2, 2, 2, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:end:7', '3:start:8', '3:start:9', '3:end:10', '3:end:11', '2:end:12', '0:end:13']) == [4, 4, 2, 4]
    assert candidate(n = 7,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '6:end:7', '5:end:8', '4:end:9', '3:end:10', '2:end:11', '1:end:12', '0:end:13']) == [2, 2, 2, 2, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:end:7', '2:start:8', '2:end:9']) == [6, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:start:9', '1:end:10', '1:end:11', '2:start:12', '2:end:13']) == [8, 4, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '4:start:10', '4:end:11']) == [1, 5, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:7', '0:end:9', '1:start:10', '1:end:11', '2:start:12', '2:end:13']) == [10, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7', '2:start:8', '2:start:9', '2:end:10', '2:end:11', '0:start:12', '0:end:13']) == [4, 6, 4]
    assert candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:start:3', '0:end:4', '0:end:5', '0:end:6', '0:end:7', '1:start:8', '1:end:9']) == [8, 2]
    assert candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '0:start:6', '2:start:7', '2:end:8', '0:end:9', '0:end:10', '3:start:11', '3:end:12', '0:start:13', '0:end:14']) == [9, 2, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [3, 4, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '2:start:6', '2:end:9', '0:end:10', '3:start:11', '4:start:12', '4:end:14', '3:end:15']) == [4, 3, 4, 2, 3]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '1:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:start:8', '3:end:9', '3:end:10']) == [1, 4, 2, 4]
    assert candidate(n = 10,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '5:start:5', '6:start:6', '7:start:7', '8:start:8', '9:start:9', '9:end:11', '8:end:12', '7:end:13', '6:end:14', '5:end:15', '4:end:16', '3:end:17', '2:end:18', '1:end:19', '0:end:20']) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
    assert candidate(n = 6,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '2:start:6', '2:start:7', '3:start:8', '3:end:9', '2:end:10', '2:end:11', '0:end:12', '4:start:13', '4:end:14', '5:start:15', '5:end:16']) == [5, 2, 4, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10']) == [1, 6, 4]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '2:start:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '0:end:11']) == [4, 2, 4, 2]
    assert candidate(n = 6,logs = ['0:start:0', '0:start:2', '0:end:3', '1:start:4', '1:start:6', '1:end:7', '1:end:9', '0:end:10']) == [5, 6, 0, 0, 0, 0]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '0:end:6', '0:end:7', '2:start:8', '2:start:9', '2:start:10', '2:end:11', '2:end:12', '2:end:13', '0:start:14', '0:end:15']) == [6, 4, 6]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '0:start:4', '0:end:5', '0:end:6', '0:end:7']) == [8, 0, 0]
    assert candidate(n = 7,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:start:4', '1:start:5', '2:start:6', '2:start:7', '2:end:8', '2:end:9', '1:end:10', '1:end:11', '1:end:12', '0:end:13', '0:end:14', '0:end:15', '3:start:16', '3:end:17', '4:start:18', '4:end:19', '5:start:20', '5:end:21', '6:start:22', '6:end:23']) == [6, 6, 4, 2, 2, 2, 2]
    assert candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '1:start:4', '1:end:5', '0:end:6']) == [1, 6]
    assert candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:start:8', '1:end:9', '1:end:10', '1:end:11', '2:start:12', '2:start:13', '2:start:14', '2:end:15', '2:end:16', '2:end:17', '3:start:18', '3:start:19', '3:start:20', '3:end:21', '3:end:22', '3:end:23']) == [6, 6, 6, 6]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '4:start:8', '4:end:9', '1:start:10', '1:end:11', '0:end:12']) == [1, 6, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '2:start:9', '2:end:10', '0:end:11']) == [4, 4, 4]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '3:start:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9']) == [2, 2, 2, 4]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '0:end:6']) == [3, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:4', '3:start:6', '3:end:8', '2:end:10', '1:end:12', '0:end:14']) == [4, 4, 4, 3, 0]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '3:start:7', '3:end:8', '3:end:9']) == [2, 2, 2, 4]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '4:start:4', '4:end:5', '3:end:6', '2:end:7', '1:end:8', '0:end:9', '0:start:10', '1:start:11', '2:start:12', '3:start:13', '4:start:14', '4:end:15', '3:end:16', '2:end:17', '1:end:18', '0:end:19']) == [4, 4, 4, 4, 4]
    assert candidate(n = 2,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '0:end:7']) == [2, 6]
    assert candidate(n = 5,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '2:start:5', '2:end:6', '0:end:7', '3:start:8', '4:start:9', '4:end:10', '3:end:11', '0:start:12', '0:end:13']) == [6, 2, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '1:end:6', '0:end:7', '0:end:8', '2:start:9', '2:end:10']) == [5, 4, 2]
    assert candidate(n = 2,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '0:start:6', '0:start:7', '0:end:8', '0:end:9']) == [10, 0]
    assert candidate(n = 6,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:5', '1:end:6', '0:end:7', '3:start:8', '3:start:9', '4:start:10', '4:end:12', '3:end:13', '5:start:14', '5:end:16']) == [1, 4, 3, 3, 3, 3]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '1:start:2', '1:start:3', '1:end:4', '1:end:5', '1:end:6', '2:start:7', '2:end:8', '0:end:9']) == [2, 6, 2]
    assert candidate(n = 3,logs = ['0:start:0', '1:start:1', '2:start:2', '1:end:3', '2:end:4', '0:end:5', '0:start:6', '1:start:7', '2:start:8', '2:end:9', '1:end:10', '0:end:11', '0:start:12', '1:start:13', '2:start:14', '2:end:15', '1:end:16', '0:end:17']) == [6, 6, 6]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '3:end:8', '2:start:9', '2:end:10', '1:start:11', '1:end:12', '0:start:13', '0:end:14']) == [3, 4, 4, 4]
    assert candidate(n = 5,logs = ['0:start:0', '0:start:1', '1:start:2', '1:start:3', '2:start:4', '2:end:5', '1:end:6', '1:end:7', '0:end:8', '3:start:9', '3:end:10', '4:start:11', '4:end:12']) == [3, 4, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '2:start:4', '2:start:5', '2:end:6', '1:start:7', '1:end:8', '0:end:9']) == [2, 4, 4]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:1', '0:start:2', '0:end:3', '0:end:4', '0:end:5', '1:start:6', '1:start:7', '1:end:8', '1:end:9', '2:start:10', '2:end:11']) == [6, 4, 2]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [4, 2, 2, 2]
    assert candidate(n = 6,logs = ['0:start:0', '0:start:1', '1:start:2', '1:end:3', '0:end:4', '0:start:5', '2:start:6', '2:end:7', '3:start:8', '3:end:9', '0:end:10', '4:start:11', '4:end:12', '5:start:13', '5:end:14']) == [5, 2, 2, 2, 2, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:start:4', '1:end:5', '0:end:6', '2:start:7', '2:end:8']) == [3, 4, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:end:3', '1:end:4', '0:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:start:10', '0:end:11']) == [4, 2, 2, 2, 2]
    assert candidate(n = 7,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:5', '0:end:6', '2:start:7', '2:start:8', '3:start:9', '3:end:11', '2:end:12', '2:end:13', '4:start:14', '4:end:16', '5:start:17', '5:end:19', '6:start:20', '6:end:22']) == [4, 3, 4, 3, 3, 3, 3]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '2:start:3', '3:start:4', '3:end:5', '2:end:6', '2:end:7', '1:end:8', '0:end:9', '4:start:10', '4:end:11']) == [2, 2, 4, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '0:end:6', '3:start:7', '4:start:8', '4:end:9', '3:end:10', '0:start:11', '1:start:12', '2:start:13', '2:end:14', '1:end:15', '0:end:16']) == [3, 6, 4, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '0:start:1', '0:end:2', '1:start:3', '1:end:4', '0:start:5', '0:end:6', '2:start:7', '2:end:8', '3:start:9', '3:end:10']) == [5, 2, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '0:start:1', '0:start:2', '1:start:3', '1:end:4', '0:end:5', '0:end:6', '2:start:7', '2:start:8', '2:end:9', '2:end:10', '3:start:11', '3:end:12', '4:start:13', '4:end:14']) == [5, 2, 4, 2, 2]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:end:2', '0:start:3', '2:start:4', '2:end:5', '0:start:6', '3:start:7', '3:end:8', '0:start:9', '2:start:10', '2:end:11', '0:start:12', '1:start:13', '1:end:14', '0:end:15', '0:start:16', '2:start:17', '2:end:18', '0:end:19']) == [8, 4, 6, 2]
    assert candidate(n = 3,logs = ['0:start:0', '0:start:2', '1:start:3', '1:end:4', '1:start:5', '1:end:6', '0:end:7', '0:start:8', '0:end:9']) == [6, 4, 0]
    assert candidate(n = 4,logs = ['0:start:0', '1:start:1', '1:start:2', '1:end:3', '2:start:4', '2:end:5', '3:start:6', '3:end:7', '1:start:8', '1:end:9', '0:end:10']) == [1, 6, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:2', '2:start:3', '2:end:4', '1:end:5', '3:start:6', '4:start:7', '4:end:8', '3:end:9', '0:end:10']) == [3, 2, 2, 2, 2]
    assert candidate(n = 5,logs = ['0:start:0', '1:start:1', '2:start:2', '3:start:3', '3:end:4', '2:end:5', '1:end:6', '0:end:7']) == [2, 2, 2, 2, 0]


