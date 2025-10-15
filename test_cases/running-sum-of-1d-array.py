def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 2, -3, 4, -5]) == [-1, 1, -2, 2, -3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 2, -3, 4, -5]) == [-1, 1, -2, 2, -3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5]) == [-5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5]) == [-5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 2, -3, 4]) == [0, -1, 1, -2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 2, -3, 4]) == [0, -1, 1, -2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4]) == [1, 3, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4]) == [1, 3, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0]) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0]) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4]) == [-1, -3, -6, -10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4]) == [-1, -3, -6, -10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000]) == [-1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000]) == [-1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000]) == [1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000]) == [1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -500, 250, -125, 62.5, -31.25, 15.625, -7.8125, 3.90625, -1.953125, 0.9765625, -0.48828125, 0.244140625, -0.1220703125, 0.06103515625]) == [1000, 500, 750, 625, 687.5, 656.25, 671.875, 664.0625, 667.96875, 666.015625, 666.9921875, 666.50390625, 666.748046875, 666.6259765625, 666.68701171875]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -500, 250, -125, 62.5, -31.25, 15.625, -7.8125, 3.90625, -1.953125, 0.9765625, -0.48828125, 0.244140625, -0.1220703125, 0.06103515625]) == [1000, 500, 750, 625, 687.5, 656.25, 671.875, 664.0625, 667.96875, 666.015625, 666.9921875, 666.50390625, 666.748046875, 666.6259765625, 666.68701171875]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525, 600, 680, 765, 855, 950, 1050]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525, 600, 680, 765, 855, 950, 1050]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500, 6600, 7800, 9100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500, 6600, 7800, 9100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 11, 111, 1111, 11111, 111111, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 11, 111, 1111, 11111, 111111, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120, -136, -153, -171, -190, -210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120, -136, -153, -171, -190, -210]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [5, 20, 45, 80, 125, 180, 245, 320, 405, 500, 605]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [5, 20, 45, 80, 125, 180, 245, 320, 405, 500, 605]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, -50, -100, 150, 200, -250, 300, -350, 400]) == [100, 150, 100, 0, 150, 350, 100, 400, 50, 450]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, -50, -100, 150, 200, -250, 300, -350, 400]) == [100, 150, 100, 0, 150, 350, 100, 400, 50, 450]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, 500000, -250000, 125000, -62500]) == [-1000000, -500000, -750000, -625000, -687500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, 500000, -250000, 125000, -62500]) == [-1000000, -500000, -750000, -625000, -687500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]) == [1000, 0, 2000, 0, 3000, 0, 4000, 0, 5000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]) == [1000, 0, 2000, 0, 3000, 0, 4000, 0, 5000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == [10, 0, 20, 0, 30, 0, 40, 0, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == [10, 0, 20, 0, 30, 0, 40, 0, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111]) == [999999, 1888887, 2666664, 3333330, 3888885, 4333329, 4666662, 4888884, 4999995]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111]) == [999999, 1888887, 2666664, 3333330, 3888885, 4333329, 4666662, 4888884, 4999995]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 39, 57, 74, 90, 105, 119, 132, 144, 155, 165, 174, 182, 189, 195, 200, 204, 207, 209, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 39, 57, 74, 90, 105, 119, 132, 144, 155, 165, 174, 182, 189, 195, 200, 204, 207, 209, 210]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30]) == [10, 0, 20, 0, 30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30]) == [10, 0, 20, 0, 30, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, -2000, -3000, -4000, -5000, -6000, -7000, -8000, -9000, -10000]) == [-1000, -3000, -6000, -10000, -15000, -21000, -28000, -36000, -45000, -55000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, -2000, -3000, -4000, -5000, -6000, -7000, -8000, -9000, -10000]) == [-1000, -3000, -6000, -10000, -15000, -21000, -28000, -36000, -45000, -55000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000]) == [500000, 0, 500000, 0, 500000, 0, 500000, 0, 500000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000]) == [500000, 0, 500000, 0, 500000, 0, 500000, 0, 500000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 15, -15, 25, -25]) == [5, 0, 15, 0, 25, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 15, -15, 25, -25]) == [5, 0, 15, 0, 25, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -500000, 500000, -250000, 250000]) == [1000000, 500000, 1000000, 750000, 1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -500000, 500000, -250000, 250000]) == [1000000, 500000, 1000000, 750000, 1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == [10000, 30000, 60000, 100000, 150000, 210000, 280000, 360000, 450000, 550000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == [10000, 30000, 60000, 100000, 150000, 210000, 280000, 360000, 450000, 550000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 29, 42, 54, 65, 75, 84, 92, 99, 105, 110, 114, 117, 119, 120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 29, 42, 54, 65, 75, 84, 92, 99, 105, 110, 114, 117, 119, 120]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995]) == [-1000000, -1999999, -2999997, -3999994, -4999990, -5999985]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995]) == [-1000000, -1999999, -2999997, -3999994, -4999990, -5999985]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000, -2500000]) == [500000, 1000000, 1500000, 2000000, 2500000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000, -2500000]) == [500000, 1000000, 1500000, 2000000, 2500000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000]) == [1000000, 0, 500000, 0, 250000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000]) == [1000000, 0, 500000, 0, 250000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == [10, -10, 20, -20, 30, -30, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == [10, -10, 20, -20, 30, -30, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == [1000000, 3000000, 6000000, 10000000, 15000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == [1000000, 3000000, 6000000, 10000000, 15000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -500000, 250000, -125000, 62500]) == [1000000, 500000, 750000, 625000, 687500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -500000, 250000, -125000, 62500]) == [1000000, 500000, 750000, 625000, 687500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 1, -999998, 2, -999997, 3]) == [999999, 1000000, 2, 4, -999993, -999990]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 1, -999998, 2, -999997, 3]) == [999999, 1000000, 2, 4, -999993, -999990]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000, -6000000, -7000000, -8000000, -9000000, -10000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000, -21000000, -28000000, -36000000, -45000000, -55000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000, -6000000, -7000000, -8000000, -9000000, -10000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000, -21000000, -28000000, -36000000, -45000000, -55000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 2000, -3000, 4000, -5000, 6000, -7000, 8000, -9000, 10000]) == [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 2000, -3000, 4000, -5000, 6000, -7000, 8000, -9000, 10000]) == [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, -234567, 345678, -456789, 567890, -678901, 789012, -890123, 901234]) == [123456, -111111, 234567, -222222, 345668, -333233, 455779, -434344, 466890]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, -234567, 345678, -456789, 567890, -678901, 789012, -890123, 901234]) == [123456, -111111, 234567, -222222, 345668, -333233, 455779, -434344, 466890]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == [999999, 1999997, 2999994, 3999990, 4999985, 5999979, 6999972, 7999964, 8999955, 9999945]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == [999999, 1999997, 2999994, 3999990, 4999985, 5999979, 6999972, 7999964, 8999955, 9999945]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == [100, 199, 297, 394, 490, 585, 679, 772, 864, 955, 1045, 1134, 1222, 1309, 1395, 1480, 1564, 1647, 1729, 1810]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == [100, 199, 297, 394, 490, 585, 679, 772, 864, 955, 1045, 1134, 1222, 1309, 1395, 1480, 1564, 1647, 1729, 1810]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-999999, -888888, -777777, -666666, -555555, -444444, -333333, -222222, -111111]) == [-999999, -1888887, -2666664, -3333330, -3888885, -4333329, -4666662, -4888884, -4999995]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-999999, -888888, -777777, -666666, -555555, -444444, -333333, -222222, -111111]) == [-999999, -1888887, -2666664, -3333330, -3888885, -4333329, -4666662, -4888884, -4999995]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, -1500000, 2000000, -2500000, 3000000, -3500000]) == [1000000, 1500000, 0, 2000000, -500000, 2500000, -1000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, -1500000, 2000000, -2500000, 3000000, -3500000]) == [1000000, 1500000, 0, 2000000, -500000, 2500000, -1000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000]) == [1000000, 0, 2000000, 0, 3000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000]) == [1000000, 0, 2000000, 0, 3000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 250000, -125000, 62500, -31250, 15625, -7812, 3906, -1953]) == [500000, 750000, 625000, 687500, 656250, 671875, 664063, 667969, 666016]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 250000, -125000, 62500, -31250, 15625, -7812, 3906, -1953]) == [500000, 750000, 625000, 687500, 656250, 671875, 664063, 667969, 666016]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000000, -1000000, -1000000, -1000000]) == [-1000000, -2000000, -3000000, -4000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000000, -1000000, -1000000, -1000000]) == [-1000000, -2000000, -3000000, -4000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3]) == [1, 0, 2, 0, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3]) == [1, 0, 2, 0, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700, 800, 900]) == [100, 300, 600, 1000, 1500, 0, 600, 1300, 2100, 3000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700, 800, 900]) == [100, 300, 600, 1000, 1500, 0, 600, 1300, 2100, 3000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764, 10945, 17710]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764, 10945, 17710]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999]) == [999999, 0, 999999, 0, 999999, 0, 999999, 0, 999999, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999]) == [999999, 0, 999999, 0, 999999, 0, 999999, 0, 999999, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [1000, 3000, 6000, 10000, 15000, 21000, 28000, 36000, 45000, 55000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [1000, 3000, 6000, 10000, 15000, 21000, 28000, 36000, 45000, 55000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150]) == [-10, -30, -60, -100, -150, -210, -280, -360, -450, -550, -660, -780, -910, -1050, -1200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150]) == [-10, -30, -60, -100, -150, -210, -280, -360, -450, -550, -660, -780, -910, -1050, -1200]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == [500, 900, 1200, 1400, 1500, 1500, 1400, 1200, 900, 500, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == [500, 900, 1200, 1400, 1500, 1500, 1400, 1200, 900, 500, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 25, -12, 6, -3, 1, 0, -1, 3, -6, 12, -24, 48, -96, 192, -384, 768, -1536, 3072]) == [100, 50, 75, 63, 69, 66, 67, 67, 66, 69, 63, 75, 51, 99, 3, 195, -189, 579, -957, 2115]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 25, -12, 6, -3, 1, 0, -1, 3, -6, 12, -24, 48, -96, 192, -384, 768, -1536, 3072]) == [100, 50, 75, 63, 69, 66, 67, 67, 66, 69, 63, 75, 51, 99, 3, 195, -189, 579, -957, 2115]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == [1, 1, 0, 2, 2, 0, 3, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == [1, 1, 0, 2, 2, 0, 3, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == [1000000, 3000000, 6000000, 10000000, 15000000, 21000000, 28000000, 36000000, 45000000, 55000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == [1000000, 3000000, 6000000, 10000000, 15000000, 21000000, 28000000, 36000000, 45000000, 55000000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991, -999990]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991, -999990]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -19, -27, -34, -40, -45, -49, -52, -54, -55]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -19, -27, -34, -40, -45, -49, -52, -54, -55]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 2, -3, 4, -5]) == [-1, 1, -2, 2, -3]
    assert candidate(nums = [-5]) == [-5]
    assert candidate(nums = [0, -1, 2, -3, 4]) == [0, -1, 1, -2, 2]
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]
    assert candidate(nums = [1]) == [1]
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]
    assert candidate(nums = [1, 2, 3, 4]) == [1, 3, 6, 10]
    assert candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert candidate(nums = [0, 0, 0, 0]) == [0, 0, 0, 0]
    assert candidate(nums = [-1, -2, -3, -4]) == [-1, -3, -6, -10]
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]
    assert candidate(nums = [-1000000]) == [-1000000]
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]
    assert candidate(nums = [5]) == [5]
    assert candidate(nums = [1000000]) == [1000000]
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000]) == [1000000, 0, 1000000, 0]
    assert candidate(nums = [3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert candidate(nums = [1000, -500, 250, -125, 62.5, -31.25, 15.625, -7.8125, 3.90625, -1.953125, 0.9765625, -0.48828125, 0.244140625, -0.1220703125, 0.06103515625]) == [1000, 500, 750, 625, 687.5, 656.25, 671.875, 664.0625, 667.96875, 666.015625, 666.9921875, 666.50390625, 666.748046875, 666.6259765625, 666.68701171875]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == [5, 15, 30, 50, 75, 105, 140, 180, 225, 275, 330, 390, 455, 525, 600, 680, 765, 855, 950, 1050]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500, 6600, 7800, 9100]
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 11, 111, 1111, 11111, 111111, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111, 1111112, 1111111]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120, -136, -153, -171, -190, -210]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == [5, 20, 45, 80, 125, 180, 245, 320, 405, 500, 605]
    assert candidate(nums = [100, 50, -50, -100, 150, 200, -250, 300, -350, 400]) == [100, 150, 100, 0, 150, 350, 100, 400, 50, 450]
    assert candidate(nums = [-1000000, 500000, -250000, 125000, -62500]) == [-1000000, -500000, -750000, -625000, -687500]
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == [-1, -3, -6, -10, -15, -21, -28, -36, -45, -55, -66, -78, -91, -105, -120]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    assert candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000]
    assert candidate(nums = [1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]) == [1000, 0, 2000, 0, 3000, 0, 4000, 0, 5000, 0]
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50]) == [10, 0, 20, 0, 30, 0, 40, 0, 50, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 19, 27, 34, 40, 45, 49, 52, 54, 55]
    assert candidate(nums = [999999, 888888, 777777, 666666, 555555, 444444, 333333, 222222, 111111]) == [999999, 1888887, 2666664, 3333330, 3888885, 4333329, 4666662, 4888884, 4999995]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [20, 39, 57, 74, 90, 105, 119, 132, 144, 155, 165, 174, 182, 189, 195, 200, 204, 207, 209, 210]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [10, -10, 20, -20, 30, -30]) == [10, 0, 20, 0, 30, 0]
    assert candidate(nums = [-1000, -2000, -3000, -4000, -5000, -6000, -7000, -8000, -9000, -10000]) == [-1000, -3000, -6000, -10000, -15000, -21000, -28000, -36000, -45000, -55000]
    assert candidate(nums = [500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000, 500000, -500000]) == [500000, 0, 500000, 0, 500000, 0, 500000, 0, 500000, 0]
    assert candidate(nums = [5, -5, 15, -15, 25, -25]) == [5, 0, 15, 0, 25, 0]
    assert candidate(nums = [1000000, -1000000, 1000000, -1000000, 1000000]) == [1000000, 0, 1000000, 0, 1000000]
    assert candidate(nums = [1000000, -500000, 500000, -250000, 250000]) == [1000000, 500000, 1000000, 750000, 1000000]
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == [10000, 30000, 60000, 100000, 150000, 210000, 280000, 360000, 450000, 550000]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [15, 29, 42, 54, 65, 75, 84, 92, 99, 105, 110, 114, 117, 119, 120]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert candidate(nums = [-1000000, -999999, -999998, -999997, -999996, -999995]) == [-1000000, -1999999, -2999997, -3999994, -4999990, -5999985]
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, -2500000]) == [500000, 1000000, 1500000, 2000000, 2500000, 0]
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    assert candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [10, 30, 60, 100, 150, 210, 280, 360, 450, 550]
    assert candidate(nums = [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1000000, -1000000, 500000, -500000, 250000, -250000]) == [1000000, 0, 500000, 0, 250000, 0]
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000]) == [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]
    assert candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4]
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70]) == [10, -10, 20, -20, 30, -30, 40]
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000]) == [1000000, 3000000, 6000000, 10000000, 15000000]
    assert candidate(nums = [1000000, -500000, 250000, -125000, 62500]) == [1000000, 500000, 750000, 625000, 687500]
    assert candidate(nums = [1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0]
    assert candidate(nums = [999999, 1, -999998, 2, -999997, 3]) == [999999, 1000000, 2, 4, -999993, -999990]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [-1000000, -2000000, -3000000, -4000000, -5000000, -6000000, -7000000, -8000000, -9000000, -10000000]) == [-1000000, -3000000, -6000000, -10000000, -15000000, -21000000, -28000000, -36000000, -45000000, -55000000]
    assert candidate(nums = [-1000, 2000, -3000, 4000, -5000, 6000, -7000, 8000, -9000, 10000]) == [-1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]
    assert candidate(nums = [123456, -234567, 345678, -456789, 567890, -678901, 789012, -890123, 901234]) == [123456, -111111, 234567, -222222, 345668, -333233, 455779, -434344, 466890]
    assert candidate(nums = [999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990]) == [999999, 1999997, 2999994, 3999990, 4999985, 5999979, 6999972, 7999964, 8999955, 9999945]
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == [100, 199, 297, 394, 490, 585, 679, 772, 864, 955, 1045, 1134, 1222, 1309, 1395, 1480, 1564, 1647, 1729, 1810]
    assert candidate(nums = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1]) == [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
    assert candidate(nums = [-999999, -888888, -777777, -666666, -555555, -444444, -333333, -222222, -111111]) == [-999999, -1888887, -2666664, -3333330, -3888885, -4333329, -4666662, -4888884, -4999995]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    assert candidate(nums = [1000000, 500000, -1500000, 2000000, -2500000, 3000000, -3500000]) == [1000000, 1500000, 0, 2000000, -500000, 2500000, -1000000]
    assert candidate(nums = [1000000, -1000000, 2000000, -2000000, 3000000, -3000000]) == [1000000, 0, 2000000, 0, 3000000, 0]
    assert candidate(nums = [500000, 250000, -125000, 62500, -31250, 15625, -7812, 3906, -1953]) == [500000, 750000, 625000, 687500, 656250, 671875, 664063, 667969, 666016]
    assert candidate(nums = [0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8]
    assert candidate(nums = [-1000000, -1000000, -1000000, -1000000]) == [-1000000, -2000000, -3000000, -4000000]
    assert candidate(nums = [1, -1, 2, -2, 3, -3]) == [1, 0, 2, 0, 3, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, -1500, 600, 700, 800, 900]) == [100, 300, 600, 1000, 1500, 0, 600, 1300, 2100, 3000]
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0]
    assert candidate(nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]) == [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764, 10945, 17710]
    assert candidate(nums = [999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999]) == [999999, 0, 999999, 0, 999999, 0, 999999, 0, 999999, 0]
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == [1000, 3000, 6000, 10000, 15000, 21000, 28000, 36000, 45000, 55000]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
    assert candidate(nums = [-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150]) == [-10, -30, -60, -100, -150, -210, -280, -360, -450, -550, -660, -780, -910, -1050, -1200]
    assert candidate(nums = [500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500]) == [500, 900, 1200, 1400, 1500, 1500, 1400, 1200, 900, 500, 0]
    assert candidate(nums = [100, -50, 25, -12, 6, -3, 1, 0, -1, 3, -6, 12, -24, 48, -96, 192, -384, 768, -1536, 3072]) == [100, 50, 75, 63, 69, 66, 67, 67, 66, 69, 63, 75, 51, 99, 3, 195, -189, 579, -957, 2115]
    assert candidate(nums = [1, 0, -1, 2, 0, -2, 3, 0, -3]) == [1, 1, 0, 2, 2, 0, 3, 3, 0]
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]) == [1000000, 3000000, 6000000, 10000000, 15000000, 21000000, 28000000, 36000000, 45000000, 55000000]
    assert candidate(nums = [999999, -999998, 999997, -999996, 999995, -999994, 999993, -999992, 999991, -999990]) == [999999, 1, 999998, 2, 999997, 3, 999996, 4, 999995, 5]
    assert candidate(nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -19, -27, -34, -40, -45, -49, -52, -54, -55]
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]


