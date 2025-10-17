def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = 10,types = [[2, 5], [1, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,types = [[2, 5], [1, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 1,types = [[1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1,types = [[1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 30,types = [[5, 10], [3, 5], [2, 15]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 30,types = [[5, 10], [3, 5], [2, 15]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(target = 750,types = [[50, 15], [50, 25], [50, 35]]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 750,types = [[50, 15], [50, 25], [50, 35]]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,types = [[2, 5], [3, 10], [4, 20]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,types = [[2, 5], [3, 10], [4, 20]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 5,types = [[50, 1], [50, 2], [50, 5]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 5,types = [[50, 1], [50, 2], [50, 5]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,types = [[10, 1], [5, 2]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,types = [[10, 1], [5, 2]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(target = 100,types = [[10, 5], [10, 10], [10, 15], [10, 20]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 100,types = [[10, 5], [10, 10], [10, 15], [10, 20]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,types = [[2, 5], [2, 10], [3, 15]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,types = [[2, 5], [2, 10], [3, 15]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(target = 6,types = [[6, 1], [3, 2], [2, 3]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 6,types = [[6, 1], [3, 2], [2, 3]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(target = 10,types = [[10, 1], [5, 2], [3, 3]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 10,types = [[10, 1], [5, 2], [3, 3]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,types = [[1, 10], [2, 5], [3, 2]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,types = [[1, 10], [2, 5], [3, 2]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,types = [[100, 10], [100, 20], [100, 30], [100, 40]]) == 8037
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,types = [[100, 10], [100, 20], [100, 30], [100, 40]]) == 8037: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 18,types = [[6, 1], [3, 2], [2, 3]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 18,types = [[6, 1], [3, 2], [2, 3]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 20,types = [[5, 10], [3, 5], [2, 2]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 20,types = [[5, 10], [3, 5], [2, 2]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[20, 10], [30, 20], [40, 30], [10, 50]]) == 721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[20, 10], [30, 20], [40, 30], [10, 50]]) == 721: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[20, 10], [20, 15], [20, 20], [20, 25], [20, 30]]) == 6939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[20, 10], [20, 15], [20, 20], [20, 25], [20, 30]]) == 6939: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[50, 3], [50, 6], [50, 9], [50, 12], [50, 15]]) == 165604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[50, 3], [50, 6], [50, 9], [50, 12], [50, 15]]) == 165604: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[20, 5], [20, 10], [20, 15], [20, 20], [20, 25]]) == 12066
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[20, 5], [20, 10], [20, 15], [20, 20], [20, 25]]) == 12066: {e}')
    
    total += 1
    try:
        result = candidate(target = 650,types = [[40, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35], [1, 40]]) == 56729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 650,types = [[40, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35], [1, 40]]) == 56729: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[25, 5], [30, 10], [35, 15], [40, 20], [45, 25], [50, 30], [55, 35], [60, 40], [65, 45], [70, 50], [75, 55]]) == 124162326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[25, 5], [30, 10], [35, 15], [40, 20], [45, 25], [50, 30], [55, 35], [60, 40], [65, 45], [70, 50], [75, 55]]) == 124162326: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25]]) == 59531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25]]) == 59531: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 50], [50, 100], [50, 150], [50, 200]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 50], [50, 100], [50, 150], [50, 200]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(target = 999,types = [[49, 1], [49, 2], [49, 3], [49, 4], [49, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999,types = [[49, 1], [49, 2], [49, 3], [49, 4], [49, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 650,types = [[30, 20], [30, 21], [30, 22], [30, 23], [30, 24]]) == 2012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 650,types = [[30, 20], [30, 21], [30, 22], [30, 23], [30, 24]]) == 2012: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[25, 28], [25, 29], [25, 30], [25, 31], [25, 32]]) == 624
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[25, 28], [25, 29], [25, 30], [25, 31], [25, 32]]) == 624: {e}')
    
    total += 1
    try:
        result = candidate(target = 200,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[30, 10], [20, 20], [40, 30], [10, 40], [30, 50]]) == 674
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[30, 10], [20, 20], [40, 30], [10, 40], [30, 50]]) == 674: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[50, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35]]) == 2734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[50, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35]]) == 2734: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30]]) == 124635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30]]) == 124635: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 692188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 692188: {e}')
    
    total += 1
    try:
        result = candidate(target = 550,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50]]) == 4654
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 550,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50]]) == 4654: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45], [15, 50], [15, 55], [15, 60], [15, 65], [15, 70], [15, 75]]) == 129491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45], [15, 50], [15, 55], [15, 60], [15, 65], [15, 70], [15, 75]]) == 129491: {e}')
    
    total += 1
    try:
        result = candidate(target = 950,types = [[100, 9], [100, 18], [100, 27], [100, 36], [100, 45]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 950,types = [[100, 9], [100, 18], [100, 27], [100, 36], [100, 45]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[30, 5], [30, 10], [30, 15], [30, 20], [30, 25], [30, 30], [30, 35], [30, 40], [30, 45], [30, 50], [30, 55], [30, 60]]) == 6856397
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[30, 5], [30, 10], [30, 15], [30, 20], [30, 25], [30, 30], [30, 35], [30, 40], [30, 45], [30, 50], [30, 55], [30, 60]]) == 6856397: {e}')
    
    total += 1
    try:
        result = candidate(target = 650,types = [[50, 10], [60, 20], [70, 30], [80, 40], [90, 50], [100, 60], [110, 70]]) == 65012
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 650,types = [[50, 10], [60, 20], [70, 30], [80, 40], [90, 50], [100, 60], [110, 70]]) == 65012: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[10, 80], [20, 40], [30, 20], [40, 10], [50, 5]]) == 26045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[10, 80], [20, 40], [30, 20], [40, 10], [50, 5]]) == 26045: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 1], [50, 2], [50, 4], [50, 8]]) == 6711
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 1], [50, 2], [50, 4], [50, 8]]) == 6711: {e}')
    
    total += 1
    try:
        result = candidate(target = 350,types = [[25, 5], [25, 15], [25, 25], [25, 35]]) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 350,types = [[25, 5], [25, 15], [25, 25], [25, 35]]) == 530: {e}')
    
    total += 1
    try:
        result = candidate(target = 550,types = [[15, 10], [15, 20], [15, 30], [15, 40], [15, 50], [15, 60], [15, 70]]) == 22303
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 550,types = [[15, 10], [15, 20], [15, 30], [15, 40], [15, 50], [15, 60], [15, 70]]) == 22303: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 2426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 2426: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[15, 20], [25, 30], [10, 40], [20, 50]]) == 574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[15, 20], [25, 30], [10, 40], [20, 50]]) == 574: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50], [25, 60]]) == 17893
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50], [25, 60]]) == 17893: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[20, 10], [30, 15], [40, 25], [50, 30]]) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[20, 10], [30, 15], [40, 25], [50, 30]]) == 276: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 34142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 34142: {e}')
    
    total += 1
    try:
        result = candidate(target = 350,types = [[15, 7], [15, 14], [15, 21], [15, 28], [15, 35]]) == 2610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 350,types = [[15, 7], [15, 14], [15, 21], [15, 28], [15, 35]]) == 2610: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[50, 5], [50, 10], [50, 15], [50, 20]]) == 19178
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[50, 5], [50, 10], [50, 15], [50, 20]]) == 19178: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25]]) == 3432
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25]]) == 3432: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 12306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 12306: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[50, 5], [50, 15], [50, 25], [50, 35], [50, 45], [50, 55]]) == 11092
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[50, 5], [50, 15], [50, 25], [50, 35], [50, 45], [50, 55]]) == 11092: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,types = [[20, 50], [15, 60], [10, 70], [5, 80], [10, 90]]) == 451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,types = [[20, 50], [15, 60], [10, 70], [5, 80], [10, 90]]) == 451: {e}')
    
    total += 1
    try:
        result = candidate(target = 650,types = [[50, 10], [40, 20], [30, 30], [20, 40], [10, 50], [5, 60], [3, 70], [2, 80], [1, 90]]) == 157298
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 650,types = [[50, 10], [40, 20], [30, 30], [20, 40], [10, 50], [5, 60], [3, 70], [2, 80], [1, 90]]) == 157298: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25], [25, 30], [25, 35], [25, 40], [25, 45], [25, 50]]) == 56776700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25], [25, 30], [25, 35], [25, 40], [25, 45], [25, 50]]) == 56776700: {e}')
    
    total += 1
    try:
        result = candidate(target = 999,types = [[30, 5], [20, 10], [40, 20], [30, 25]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999,types = [[30, 5], [20, 10], [40, 20], [30, 25]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[20, 25], [30, 50], [25, 75], [40, 100], [30, 125]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[20, 25], [30, 50], [25, 75], [40, 100], [30, 125]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[15, 5], [25, 10], [35, 15], [45, 20]]) == 2461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[15, 5], [25, 10], [35, 15], [45, 20]]) == 2461: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13], [50, 17], [50, 19]]) == 53354051
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13], [50, 17], [50, 19]]) == 53354051: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[25, 4], [25, 8], [25, 12], [25, 16], [25, 20]]) == 27739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[25, 4], [25, 8], [25, 12], [25, 16], [25, 20]]) == 27739: {e}')
    
    total += 1
    try:
        result = candidate(target = 550,types = [[45, 15], [55, 25], [65, 35], [75, 45], [85, 55], [95, 65]]) == 2608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 550,types = [[45, 15], [55, 25], [65, 35], [75, 45], [85, 55], [95, 65]]) == 2608: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13]]) == 433268
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13]]) == 433268: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[20, 1], [30, 2], [20, 3], [10, 4], [10, 5], [5, 6]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[20, 1], [30, 2], [20, 3], [10, 4], [10, 5], [5, 6]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[30, 10], [40, 20], [50, 30], [60, 40], [70, 50], [80, 60]]) == 5852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[30, 10], [40, 20], [50, 30], [60, 40], [70, 50], [80, 60]]) == 5852: {e}')
    
    total += 1
    try:
        result = candidate(target = 650,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 9472
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 650,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 9472: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 18680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 18680: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[5, 50], [10, 100], [15, 150], [20, 200], [25, 250]]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[5, 50], [10, 100], [15, 150], [20, 200], [25, 250]]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 909681426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 909681426: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[25, 20], [25, 30], [25, 40], [25, 50]]) == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[25, 20], [25, 30], [25, 40], [25, 50]]) == 258: {e}')
    
    total += 1
    try:
        result = candidate(target = 350,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50], [20, 60], [20, 70], [20, 80]]) == 4950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 350,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50], [20, 60], [20, 70], [20, 80]]) == 4950: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[50, 20], [30, 15], [20, 10], [10, 5]]) == 1129
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[50, 20], [30, 15], [20, 10], [10, 5]]) == 1129: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687: {e}')
    
    total += 1
    try:
        result = candidate(target = 450,types = [[15, 30], [20, 25], [25, 20], [30, 15], [35, 10]]) == 5753
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 450,types = [[15, 30], [20, 25], [25, 20], [30, 15], [35, 10]]) == 5753: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[30, 10], [20, 15], [10, 20], [5, 25]]) == 535
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[30, 10], [20, 15], [10, 20], [5, 25]]) == 535: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45]]) == 108177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45]]) == 108177: {e}')
    
    total += 1
    try:
        result = candidate(target = 200,types = [[20, 10], [20, 20], [20, 30], [20, 40]]) == 108
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200,types = [[20, 10], [20, 20], [20, 30], [20, 40]]) == 108: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[30, 25], [40, 50], [20, 75]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[30, 25], [40, 50], [20, 75]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[20, 10], [30, 20], [10, 30], [20, 40]]) == 1725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[20, 10], [30, 20], [10, 30], [20, 40]]) == 1725: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[20, 25], [20, 30], [20, 35], [20, 40], [20, 45]]) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[20, 25], [20, 30], [20, 35], [20, 40], [20, 45]]) == 520: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[100, 9], [100, 10], [100, 11], [100, 12], [100, 13]]) == 199590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[100, 9], [100, 10], [100, 11], [100, 12], [100, 13]]) == 199590: {e}')
    
    total += 1
    try:
        result = candidate(target = 550,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25], [65, 30], [75, 35], [85, 40], [95, 45], [105, 50]]) == 8359201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 550,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25], [65, 30], [75, 35], [85, 40], [95, 45], [105, 50]]) == 8359201: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 12], [50, 14], [50, 16], [50, 18], [50, 20]]) == 14453
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 12], [50, 14], [50, 16], [50, 18], [50, 20]]) == 14453: {e}')
    
    total += 1
    try:
        result = candidate(target = 999,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10], [50, 11], [50, 12], [50, 13], [50, 14], [50, 15]]) == 805840421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 999,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10], [50, 11], [50, 12], [50, 13], [50, 14], [50, 15]]) == 805840421: {e}')
    
    total += 1
    try:
        result = candidate(target = 550,types = [[40, 5], [40, 10], [40, 15], [30, 20], [20, 25], [10, 30]]) == 249864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 550,types = [[40, 5], [40, 10], [40, 15], [30, 20], [20, 25], [10, 30]]) == 249864: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40], [5, 50]]) == 13462
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40], [5, 50]]) == 13462: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[30, 5], [30, 15], [30, 25], [30, 35], [30, 45], [30, 55], [30, 65], [30, 75], [30, 85], [30, 95]]) == 5111100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[30, 5], [30, 15], [30, 25], [30, 35], [30, 45], [30, 55], [30, 65], [30, 75], [30, 85], [30, 95]]) == 5111100: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[60, 20], [70, 40], [80, 60], [90, 80]]) == 632
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[60, 20], [70, 40], [80, 60], [90, 80]]) == 632: {e}')
    
    total += 1
    try:
        result = candidate(target = 850,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]]) == 117144248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 850,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]]) == 117144248: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[50, 1], [50, 3], [50, 5], [50, 7], [50, 9]]) == 485554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[50, 1], [50, 3], [50, 5], [50, 7], [50, 9]]) == 485554: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 79630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 79630: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[30, 15], [30, 25], [30, 35], [30, 45], [30, 55]]) == 2386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[30, 15], [30, 25], [30, 35], [30, 45], [30, 55]]) == 2386: {e}')
    
    total += 1
    try:
        result = candidate(target = 1000,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 1000,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[25, 30], [35, 45], [45, 60], [50, 75]]) == 414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[25, 30], [35, 45], [45, 60], [50, 75]]) == 414: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[60, 5], [60, 6], [60, 7], [60, 8], [60, 9]]) == 27971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[60, 5], [60, 6], [60, 7], [60, 8], [60, 9]]) == 27971: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [25, 7], [25, 8]]) == 683239099
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [25, 7], [25, 8]]) == 683239099: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[20, 5], [30, 10], [10, 15]]) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[20, 5], [30, 10], [10, 15]]) == 116: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 3765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 3765: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[30, 10], [20, 20], [10, 30], [5, 40]]) == 858
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[30, 10], [20, 20], [10, 30], [5, 40]]) == 858: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[10, 2], [20, 3], [30, 5], [40, 7], [50, 11]]) == 18034
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[10, 2], [20, 3], [30, 5], [40, 7], [50, 11]]) == 18034: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[50, 1], [50, 2], [50, 5], [50, 10]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[50, 1], [50, 2], [50, 5], [50, 10]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[50, 15], [40, 25], [30, 35], [20, 45], [10, 55], [5, 65]]) == 19430
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[50, 15], [40, 25], [30, 35], [20, 45], [10, 55], [5, 65]]) == 19430: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50]]) == 1583
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50]]) == 1583: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 2270071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 2270071: {e}')
    
    total += 1
    try:
        result = candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 48055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 48055: {e}')
    
    total += 1
    try:
        result = candidate(target = 400,types = [[80, 5], [80, 10], [80, 15], [80, 20], [80, 25]]) == 20282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 400,types = [[80, 5], [80, 10], [80, 15], [80, 20], [80, 25]]) == 20282: {e}')
    
    total += 1
    try:
        result = candidate(target = 700,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 11867
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 700,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 11867: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 19837096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 19837096: {e}')
    
    total += 1
    try:
        result = candidate(target = 250,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 57127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 250,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 57127: {e}')
    
    total += 1
    try:
        result = candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 3041
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 3041: {e}')
    
    total += 1
    try:
        result = candidate(target = 950,types = [[5, 100], [10, 50], [15, 33], [20, 25], [25, 20], [30, 16], [35, 14], [40, 12], [45, 11], [50, 10]]) == 240007134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 950,types = [[5, 100], [10, 50], [15, 33], [20, 25], [25, 20], [30, 16], [35, 14], [40, 12], [45, 11], [50, 10]]) == 240007134: {e}')
    
    total += 1
    try:
        result = candidate(target = 200,types = [[10, 5], [10, 10], [10, 15], [10, 20], [10, 25]]) == 1003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 200,types = [[10, 5], [10, 10], [10, 15], [10, 20], [10, 25]]) == 1003: {e}')
    
    total += 1
    try:
        result = candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687: {e}')
    
    total += 1
    try:
        result = candidate(target = 300,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 203
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 300,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 203: {e}')
    
    total += 1
    try:
        result = candidate(target = 900,types = [[20, 5], [30, 10], [40, 15], [10, 20], [10, 25]]) == 21573
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 900,types = [[20, 5], [30, 10], [40, 15], [10, 20], [10, 25]]) == 21573: {e}')
    
    total += 1
    try:
        result = candidate(target = 750,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 450083451
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = 750,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 450083451: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = 10,types = [[2, 5], [1, 3]]) == 1
    assert candidate(target = 1,types = [[1, 1]]) == 1
    assert candidate(target = 30,types = [[5, 10], [3, 5], [2, 15]]) == 5
    assert candidate(target = 750,types = [[50, 15], [50, 25], [50, 35]]) == 119
    assert candidate(target = 20,types = [[2, 5], [3, 10], [4, 20]]) == 3
    assert candidate(target = 10,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 3
    assert candidate(target = 5,types = [[50, 1], [50, 2], [50, 5]]) == 4
    assert candidate(target = 10,types = [[10, 1], [5, 2]]) == 6
    assert candidate(target = 100,types = [[10, 5], [10, 10], [10, 15], [10, 20]]) == 90
    assert candidate(target = 20,types = [[2, 5], [2, 10], [3, 15]]) == 3
    assert candidate(target = 6,types = [[6, 1], [3, 2], [2, 3]]) == 7
    assert candidate(target = 10,types = [[10, 1], [5, 2], [3, 3]]) == 14
    assert candidate(target = 20,types = [[1, 10], [2, 5], [3, 2]]) == 1
    assert candidate(target = 1000,types = [[100, 10], [100, 20], [100, 30], [100, 40]]) == 8037
    assert candidate(target = 20,types = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) == 0
    assert candidate(target = 18,types = [[6, 1], [3, 2], [2, 3]]) == 1
    assert candidate(target = 20,types = [[5, 10], [3, 5], [2, 2]]) == 2
    assert candidate(target = 500,types = [[20, 10], [30, 20], [40, 30], [10, 50]]) == 721
    assert candidate(target = 500,types = [[20, 10], [20, 15], [20, 20], [20, 25], [20, 30]]) == 6939
    assert candidate(target = 450,types = [[50, 3], [50, 6], [50, 9], [50, 12], [50, 15]]) == 165604
    assert candidate(target = 400,types = [[20, 5], [20, 10], [20, 15], [20, 20], [20, 25]]) == 12066
    assert candidate(target = 650,types = [[40, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35], [1, 40]]) == 56729
    assert candidate(target = 700,types = [[25, 5], [30, 10], [35, 15], [40, 20], [45, 25], [50, 30], [55, 35], [60, 40], [65, 45], [70, 50], [75, 55]]) == 124162326
    assert candidate(target = 800,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25]]) == 59531
    assert candidate(target = 600,types = [[50, 50], [50, 100], [50, 150], [50, 200]]) == 34
    assert candidate(target = 999,types = [[49, 1], [49, 2], [49, 3], [49, 4], [49, 5]]) == 0
    assert candidate(target = 650,types = [[30, 20], [30, 21], [30, 22], [30, 23], [30, 24]]) == 2012
    assert candidate(target = 700,types = [[25, 28], [25, 29], [25, 30], [25, 31], [25, 32]]) == 624
    assert candidate(target = 200,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 90
    assert candidate(target = 300,types = [[30, 10], [20, 20], [40, 30], [10, 40], [30, 50]]) == 674
    assert candidate(target = 300,types = [[50, 10], [30, 15], [20, 20], [10, 25], [5, 30], [2, 35]]) == 2734
    assert candidate(target = 600,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30]]) == 124635
    assert candidate(target = 600,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 0
    assert candidate(target = 250,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 692188
    assert candidate(target = 550,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50]]) == 4654
    assert candidate(target = 250,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45], [15, 50], [15, 55], [15, 60], [15, 65], [15, 70], [15, 75]]) == 129491
    assert candidate(target = 950,types = [[100, 9], [100, 18], [100, 27], [100, 36], [100, 45]]) == 0
    assert candidate(target = 450,types = [[30, 5], [30, 10], [30, 15], [30, 20], [30, 25], [30, 30], [30, 35], [30, 40], [30, 45], [30, 50], [30, 55], [30, 60]]) == 6856397
    assert candidate(target = 650,types = [[50, 10], [60, 20], [70, 30], [80, 40], [90, 50], [100, 60], [110, 70]]) == 65012
    assert candidate(target = 800,types = [[10, 80], [20, 40], [30, 20], [40, 10], [50, 5]]) == 26045
    assert candidate(target = 600,types = [[50, 1], [50, 2], [50, 4], [50, 8]]) == 6711
    assert candidate(target = 350,types = [[25, 5], [25, 15], [25, 25], [25, 35]]) == 530
    assert candidate(target = 550,types = [[15, 10], [15, 20], [15, 30], [15, 40], [15, 50], [15, 60], [15, 70]]) == 22303
    assert candidate(target = 900,types = [[10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10]]) == 0
    assert candidate(target = 700,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 2426
    assert candidate(target = 800,types = [[15, 20], [25, 30], [10, 40], [20, 50]]) == 574
    assert candidate(target = 600,types = [[25, 10], [25, 20], [25, 30], [25, 40], [25, 50], [25, 60]]) == 17893
    assert candidate(target = 300,types = [[20, 10], [30, 15], [40, 25], [50, 30]]) == 276
    assert candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90]]) == 34142
    assert candidate(target = 350,types = [[15, 7], [15, 14], [15, 21], [15, 28], [15, 35]]) == 2610
    assert candidate(target = 800,types = [[50, 5], [50, 10], [50, 15], [50, 20]]) == 19178
    assert candidate(target = 250,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25]]) == 3432
    assert candidate(target = 700,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 12306
    assert candidate(target = 450,types = [[50, 5], [50, 15], [50, 25], [50, 35], [50, 45], [50, 55]]) == 11092
    assert candidate(target = 1000,types = [[20, 50], [15, 60], [10, 70], [5, 80], [10, 90]]) == 451
    assert candidate(target = 650,types = [[50, 10], [40, 20], [30, 30], [20, 40], [10, 50], [5, 60], [3, 70], [2, 80], [1, 90]]) == 157298
    assert candidate(target = 700,types = [[25, 5], [25, 10], [25, 15], [25, 20], [25, 25], [25, 30], [25, 35], [25, 40], [25, 45], [25, 50]]) == 56776700
    assert candidate(target = 999,types = [[30, 5], [20, 10], [40, 20], [30, 25]]) == 0
    assert candidate(target = 400,types = [[20, 25], [30, 50], [25, 75], [40, 100], [30, 125]]) == 101
    assert candidate(target = 500,types = [[15, 5], [25, 10], [35, 15], [45, 20]]) == 2461
    assert candidate(target = 700,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13], [50, 17], [50, 19]]) == 53354051
    assert candidate(target = 400,types = [[25, 4], [25, 8], [25, 12], [25, 16], [25, 20]]) == 27739
    assert candidate(target = 550,types = [[45, 15], [55, 25], [65, 35], [75, 45], [85, 55], [95, 65]]) == 2608
    assert candidate(target = 1000,types = [[50, 1], [50, 3], [50, 7], [50, 11], [50, 13]]) == 433268
    assert candidate(target = 250,types = [[20, 1], [30, 2], [20, 3], [10, 4], [10, 5], [5, 6]]) == 35
    assert candidate(target = 450,types = [[30, 10], [40, 20], [50, 30], [60, 40], [70, 50], [80, 60]]) == 5852
    assert candidate(target = 650,types = [[50, 10], [50, 20], [50, 30], [50, 40], [50, 50]]) == 9472
    assert candidate(target = 800,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 18680
    assert candidate(target = 700,types = [[5, 50], [10, 100], [15, 150], [20, 200], [25, 250]]) == 52
    assert candidate(target = 450,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 909681426
    assert candidate(target = 500,types = [[25, 20], [25, 30], [25, 40], [25, 50]]) == 258
    assert candidate(target = 350,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50], [20, 60], [20, 70], [20, 80]]) == 4950
    assert candidate(target = 400,types = [[50, 20], [30, 15], [20, 10], [10, 5]]) == 1129
    assert candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687
    assert candidate(target = 450,types = [[15, 30], [20, 25], [25, 20], [30, 15], [35, 10]]) == 5753
    assert candidate(target = 500,types = [[30, 10], [20, 15], [10, 20], [5, 25]]) == 535
    assert candidate(target = 300,types = [[15, 5], [15, 10], [15, 15], [15, 20], [15, 25], [15, 30], [15, 35], [15, 40], [15, 45]]) == 108177
    assert candidate(target = 200,types = [[20, 10], [20, 20], [20, 30], [20, 40]]) == 108
    assert candidate(target = 800,types = [[30, 25], [40, 50], [20, 75]]) == 101
    assert candidate(target = 900,types = [[20, 10], [30, 20], [10, 30], [20, 40]]) == 1725
    assert candidate(target = 500,types = [[20, 25], [20, 30], [20, 35], [20, 40], [20, 45]]) == 520
    assert candidate(target = 900,types = [[100, 9], [100, 10], [100, 11], [100, 12], [100, 13]]) == 199590
    assert candidate(target = 550,types = [[15, 5], [25, 10], [35, 15], [45, 20], [55, 25], [65, 30], [75, 35], [85, 40], [95, 45], [105, 50]]) == 8359201
    assert candidate(target = 600,types = [[50, 12], [50, 14], [50, 16], [50, 18], [50, 20]]) == 14453
    assert candidate(target = 999,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10], [50, 11], [50, 12], [50, 13], [50, 14], [50, 15]]) == 805840421
    assert candidate(target = 550,types = [[40, 5], [40, 10], [40, 15], [30, 20], [20, 25], [10, 30]]) == 249864
    assert candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40], [5, 50]]) == 13462
    assert candidate(target = 900,types = [[30, 5], [30, 15], [30, 25], [30, 35], [30, 45], [30, 55], [30, 65], [30, 75], [30, 85], [30, 95]]) == 5111100
    assert candidate(target = 800,types = [[60, 20], [70, 40], [80, 60], [90, 80]]) == 632
    assert candidate(target = 850,types = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]]) == 117144248
    assert candidate(target = 800,types = [[50, 1], [50, 3], [50, 5], [50, 7], [50, 9]]) == 485554
    assert candidate(target = 600,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 79630
    assert candidate(target = 700,types = [[30, 15], [30, 25], [30, 35], [30, 45], [30, 55]]) == 2386
    assert candidate(target = 1000,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5]]) == 0
    assert candidate(target = 900,types = [[25, 30], [35, 45], [45, 60], [50, 75]]) == 414
    assert candidate(target = 300,types = [[60, 5], [60, 6], [60, 7], [60, 8], [60, 9]]) == 27971
    assert candidate(target = 400,types = [[25, 1], [25, 2], [25, 3], [25, 4], [25, 5], [25, 6], [25, 7], [25, 8]]) == 683239099
    assert candidate(target = 300,types = [[20, 5], [30, 10], [10, 15]]) == 116
    assert candidate(target = 250,types = [[50, 5], [50, 10], [50, 15], [50, 20], [50, 25]]) == 3765
    assert candidate(target = 600,types = [[30, 10], [20, 20], [10, 30], [5, 40]]) == 858
    assert candidate(target = 300,types = [[10, 2], [20, 3], [30, 5], [40, 7], [50, 11]]) == 18034
    assert candidate(target = 900,types = [[50, 1], [50, 2], [50, 5], [50, 10]]) == 1
    assert candidate(target = 900,types = [[50, 15], [40, 25], [30, 35], [20, 45], [10, 55], [5, 65]]) == 19430
    assert candidate(target = 400,types = [[20, 10], [20, 20], [20, 30], [20, 40], [20, 50]]) == 1583
    assert candidate(target = 400,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6]]) == 2270071
    assert candidate(target = 500,types = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]]) == 48055
    assert candidate(target = 400,types = [[80, 5], [80, 10], [80, 15], [80, 20], [80, 25]]) == 20282
    assert candidate(target = 700,types = [[40, 10], [50, 20], [60, 30], [70, 40], [80, 50]]) == 11867
    assert candidate(target = 300,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7]]) == 19837096
    assert candidate(target = 250,types = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]]) == 57127
    assert candidate(target = 800,types = [[40, 10], [30, 20], [20, 30], [10, 40]]) == 3041
    assert candidate(target = 950,types = [[5, 100], [10, 50], [15, 33], [20, 25], [25, 20], [30, 16], [35, 14], [40, 12], [45, 11], [50, 10]]) == 240007134
    assert candidate(target = 200,types = [[10, 5], [10, 10], [10, 15], [10, 20], [10, 25]]) == 1003
    assert candidate(target = 600,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 209801687
    assert candidate(target = 300,types = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 203
    assert candidate(target = 900,types = [[20, 5], [30, 10], [40, 15], [10, 20], [10, 25]]) == 21573
    assert candidate(target = 750,types = [[50, 1], [50, 2], [50, 3], [50, 4], [50, 5], [50, 6], [50, 7], [50, 8], [50, 9], [50, 10]]) == 450083451


