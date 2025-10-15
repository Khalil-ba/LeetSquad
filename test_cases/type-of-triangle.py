def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 10]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 10]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 12]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 12]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 5]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 5]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 15, 17]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 15, 17]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 10]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 10]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 8]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 8]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 5]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 5]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 5]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 5]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 4, 7]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 4, 7]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 98]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 98]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 40]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 40]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 40, 50]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 40, 50]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 16, 20]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 16, 20]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 25]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 25]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 1]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 1]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 8]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 8]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 198]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 198]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 14]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 14]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 89]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 89]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 21, 21]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 21, 21]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 25, 30]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 25, 30]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 45]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 45]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 6]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 6]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 60]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 60]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 80]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 80]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 99, 99]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 99, 99]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 5]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 5]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 14, 15]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 14, 15]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 12, 15]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 12, 15]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 10]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 10]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 23, 23]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 23, 23]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 10, 5]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 10, 5]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 1]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 1]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 11]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 11]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 45]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 45]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 4, 6]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 4, 6]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 12, 15]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 12, 15]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 1, 1]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 1, 1]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 90]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 90]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [40, 40, 41]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [40, 40, 41]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 100]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 100]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 12, 13]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 12, 13]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 51, 100]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 51, 100]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 12, 13]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 12, 13]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 1]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 1]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 15]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 15]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 9]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 9]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 20]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 20]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 30, 59]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 30, 59]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 29]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 29]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 15]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 15]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 30]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 30]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 24, 25]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 24, 25]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 40, 41]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 40, 41]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [17, 17, 34]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [17, 17, 34]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 44, 55]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 44, 55]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 80]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 80]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 4]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 4]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 25, 49]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 25, 49]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 25]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 25]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 14, 14]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 14, 14]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 12]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 12]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 16, 20]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 16, 20]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1]) == "equilateral": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 24, 25]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 24, 25]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [51, 51, 100]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [51, 51, 100]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 8, 10]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 8, 10]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 45, 89]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 45, 89]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 10]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 10]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 100]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 100]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 3]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 3]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 40, 50]) == "scalene"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 40, 50]) == "scalene": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 33, 34]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 33, 34]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 70]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 70]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 100]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 100]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 1]) == "none"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 1]) == "none": {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 15, 25]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 15, 25]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 12]) == "isosceles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 12]) == "isosceles": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100]) == "equilateral"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100]) == "equilateral": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 2, 3]) == "isosceles"
    assert candidate(nums = [10, 10, 10]) == "equilateral"
    assert candidate(nums = [1, 1, 2]) == "none"
    assert candidate(nums = [6, 6, 10]) == "isosceles"
    assert candidate(nums = [6, 6, 12]) == "none"
    assert candidate(nums = [3, 4, 5]) == "scalene"
    assert candidate(nums = [8, 15, 17]) == "scalene"
    assert candidate(nums = [1, 2, 3]) == "none"
    assert candidate(nums = [5, 7, 10]) == "scalene"
    assert candidate(nums = [6, 6, 6]) == "equilateral"
    assert candidate(nums = [50, 50, 50]) == "equilateral"
    assert candidate(nums = [5, 5, 8]) == "isosceles"
    assert candidate(nums = [5, 7, 5]) == "isosceles"
    assert candidate(nums = [3, 3, 3]) == "equilateral"
    assert candidate(nums = [7, 10, 5]) == "scalene"
    assert candidate(nums = [4, 4, 7]) == "isosceles"
    assert candidate(nums = [99, 99, 98]) == "isosceles"
    assert candidate(nums = [5, 5, 5]) == "equilateral"
    assert candidate(nums = [25, 25, 40]) == "isosceles"
    assert candidate(nums = [30, 40, 50]) == "scalene"
    assert candidate(nums = [12, 16, 20]) == "scalene"
    assert candidate(nums = [10, 15, 25]) == "none"
    assert candidate(nums = [99, 99, 1]) == "isosceles"
    assert candidate(nums = [5, 5, 8]) == "isosceles"
    assert candidate(nums = [99, 99, 198]) == "none"
    assert candidate(nums = [7, 7, 14]) == "none"
    assert candidate(nums = [45, 45, 89]) == "isosceles"
    assert candidate(nums = [20, 21, 21]) == "isosceles"
    assert candidate(nums = [20, 25, 30]) == "scalene"
    assert candidate(nums = [45, 45, 45]) == "equilateral"
    assert candidate(nums = [3, 4, 6]) == "scalene"
    assert candidate(nums = [50, 60, 60]) == "isosceles"
    assert candidate(nums = [50, 50, 80]) == "isosceles"
    assert candidate(nums = [99, 99, 99]) == "equilateral"
    assert candidate(nums = [3, 5, 5]) == "isosceles"
    assert candidate(nums = [13, 14, 15]) == "scalene"
    assert candidate(nums = [9, 12, 15]) == "scalene"
    assert candidate(nums = [6, 6, 10]) == "isosceles"
    assert candidate(nums = [23, 23, 23]) == "equilateral"
    assert candidate(nums = [7, 10, 5]) == "scalene"
    assert candidate(nums = [5, 5, 5]) == "equilateral"
    assert candidate(nums = [9, 9, 9]) == "equilateral"
    assert candidate(nums = [100, 100, 1]) == "isosceles"
    assert candidate(nums = [6, 6, 11]) == "isosceles"
    assert candidate(nums = [45, 45, 45]) == "equilateral"
    assert candidate(nums = [9, 4, 6]) == "scalene"
    assert candidate(nums = [1, 2, 2]) == "isosceles"
    assert candidate(nums = [6, 8, 10]) == "scalene"
    assert candidate(nums = [9, 12, 15]) == "scalene"
    assert candidate(nums = [99, 1, 1]) == "none"
    assert candidate(nums = [45, 45, 90]) == "none"
    assert candidate(nums = [40, 40, 41]) == "isosceles"
    assert candidate(nums = [50, 51, 100]) == "scalene"
    assert candidate(nums = [5, 12, 13]) == "scalene"
    assert candidate(nums = [50, 51, 100]) == "scalene"
    assert candidate(nums = [2, 2, 4]) == "none"
    assert candidate(nums = [5, 12, 13]) == "scalene"
    assert candidate(nums = [100, 100, 1]) == "isosceles"
    assert candidate(nums = [10, 10, 15]) == "isosceles"
    assert candidate(nums = [5, 5, 9]) == "isosceles"
    assert candidate(nums = [10, 10, 20]) == "none"
    assert candidate(nums = [30, 30, 59]) == "isosceles"
    assert candidate(nums = [10, 10, 10]) == "equilateral"
    assert candidate(nums = [2, 2, 4]) == "none"
    assert candidate(nums = [15, 15, 29]) == "isosceles"
    assert candidate(nums = [10, 10, 15]) == "isosceles"
    assert candidate(nums = [100, 100, 100]) == "equilateral"
    assert candidate(nums = [25, 25, 30]) == "isosceles"
    assert candidate(nums = [7, 24, 25]) == "scalene"
    assert candidate(nums = [9, 40, 41]) == "scalene"
    assert candidate(nums = [17, 17, 34]) == "none"
    assert candidate(nums = [33, 44, 55]) == "scalene"
    assert candidate(nums = [50, 50, 80]) == "isosceles"
    assert candidate(nums = [3, 4, 4]) == "isosceles"
    assert candidate(nums = [25, 25, 49]) == "isosceles"
    assert candidate(nums = [10, 15, 25]) == "none"
    assert candidate(nums = [10, 14, 14]) == "isosceles"
    assert candidate(nums = [5, 7, 12]) == "none"
    assert candidate(nums = [12, 16, 20]) == "scalene"
    assert candidate(nums = [1, 1, 1]) == "equilateral"
    assert candidate(nums = [7, 24, 25]) == "scalene"
    assert candidate(nums = [51, 51, 100]) == "isosceles"
    assert candidate(nums = [6, 8, 10]) == "scalene"
    assert candidate(nums = [45, 45, 89]) == "isosceles"
    assert candidate(nums = [7, 7, 10]) == "isosceles"
    assert candidate(nums = [50, 50, 100]) == "none"
    assert candidate(nums = [1, 1, 2]) == "none"
    assert candidate(nums = [2, 2, 3]) == "isosceles"
    assert candidate(nums = [30, 40, 50]) == "scalene"
    assert candidate(nums = [33, 33, 34]) == "isosceles"
    assert candidate(nums = [50, 50, 70]) == "isosceles"
    assert candidate(nums = [1, 100, 100]) == "isosceles"
    assert candidate(nums = [1, 100, 1]) == "none"
    assert candidate(nums = [15, 15, 25]) == "isosceles"
    assert candidate(nums = [9, 9, 12]) == "isosceles"
    assert candidate(nums = [100, 100, 100]) == "equilateral"


