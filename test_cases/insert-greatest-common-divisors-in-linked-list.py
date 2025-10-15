def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 14, 28, 56])), list_node([7, 7, 14, 14, 28, 28, 56]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 14, 28, 56])), list_node([7, 7, 14, 14, 28, 28, 56])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([33, 51, 68])), list_node([33, 3, 51, 17, 68]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([33, 51, 68])), list_node([33, 3, 51, 17, 68])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([10, 10, 20, 10, 30, 10, 40, 10, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([10, 10, 20, 10, 30, 10, 40, 10, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 1000])), list_node([1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 1000])), list_node([1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 9, 27, 81])), list_node([3, 3, 9, 9, 27, 27, 81]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 9, 27, 81])), list_node([3, 3, 9, 9, 27, 27, 81])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([48, 18, 30])), list_node([48, 6, 18, 6, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([48, 18, 30])), list_node([48, 6, 18, 6, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300])), list_node([100, 100, 200, 100, 300]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300])), list_node([100, 100, 200, 100, 300])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 50, 25, 10])), list_node([100, 50, 50, 25, 25, 5, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 50, 25, 10])), list_node([100, 50, 50, 25, 25, 5, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3])), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3])), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7])), list_node([7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7])), list_node([7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([12, 15, 20])), list_node([12, 3, 15, 5, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([12, 15, 20])), list_node([12, 3, 15, 5, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([42, 56, 14])), list_node([42, 14, 56, 14, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([42, 56, 14])), list_node([42, 14, 56, 14, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([18, 6, 10, 3])), list_node([18, 6, 6, 2, 10, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([18, 6, 10, 3])), list_node([18, 6, 6, 2, 10, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 12, 16, 20])), list_node([8, 4, 12, 4, 16, 4, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 12, 16, 20])), list_node([8, 4, 12, 4, 16, 4, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 81, 27])), list_node([99, 9, 81, 27, 27]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 81, 27])), list_node([99, 9, 81, 27, 27])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 15, 25, 35])), list_node([5, 5, 15, 5, 25, 5, 35]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 15, 25, 35])), list_node([5, 5, 15, 5, 25, 5, 35])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25])), list_node([5, 5, 10, 5, 15, 5, 20, 5, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25])), list_node([5, 5, 10, 5, 15, 5, 20, 5, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([12, 15, 21])), list_node([12, 3, 15, 3, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([12, 15, 21])), list_node([12, 3, 15, 3, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125])), list_node([1000, 500, 500, 250, 250, 125, 125]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125])), list_node([1000, 500, 500, 250, 250, 125, 125])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 5, 8, 12])), list_node([3, 1, 5, 1, 8, 4, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 5, 8, 12])), list_node([3, 1, 5, 1, 8, 4, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([98, 49, 24, 12, 6, 3])), list_node([98, 49, 49, 1, 24, 12, 12, 6, 6, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([98, 49, 24, 12, 6, 3])), list_node([98, 49, 49, 1, 24, 12, 12, 6, 6, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([13, 17, 19, 23, 29])), list_node([13, 1, 17, 1, 19, 1, 23, 1, 29]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([13, 17, 19, 23, 29])), list_node([13, 1, 17, 1, 19, 1, 23, 1, 29])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2023, 2021, 2019, 2017, 2015])), list_node([2023, 1, 2021, 1, 2019, 1, 2017, 1, 2015]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2023, 2021, 2019, 2017, 2015])), list_node([2023, 1, 2021, 1, 2019, 1, 2017, 1, 2015])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 14, 49, 35, 70, 56])), list_node([21, 7, 14, 7, 49, 7, 35, 35, 70, 14, 56]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 14, 49, 35, 70, 56])), list_node([21, 7, 14, 7, 49, 7, 35, 35, 70, 14, 56])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([77, 49, 35, 91, 63])), list_node([77, 7, 49, 7, 35, 7, 91, 7, 63]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([77, 49, 35, 91, 63])), list_node([77, 7, 49, 7, 35, 7, 91, 7, 63])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([60, 45, 30, 15])), list_node([60, 15, 45, 15, 30, 15, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([60, 45, 30, 15])), list_node([60, 15, 45, 15, 30, 15, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([60, 30, 15, 5, 1])), list_node([60, 30, 30, 15, 15, 5, 5, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([60, 30, 15, 5, 1])), list_node([60, 30, 30, 15, 15, 5, 5, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([112, 128, 144, 160, 176])), list_node([112, 16, 128, 16, 144, 16, 160, 16, 176]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([112, 128, 144, 160, 176])), list_node([112, 16, 128, 16, 144, 16, 160, 16, 176])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([77, 14, 28, 49])), list_node([77, 7, 14, 14, 28, 7, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([77, 14, 28, 49])), list_node([77, 7, 14, 14, 28, 7, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 35, 105, 175])), list_node([21, 7, 35, 35, 105, 35, 175]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 35, 105, 175])), list_node([21, 7, 35, 35, 105, 35, 175])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 12, 18, 24])), list_node([8, 4, 12, 6, 18, 6, 24]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 12, 18, 24])), list_node([8, 4, 12, 6, 18, 6, 24])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 12, 16, 20, 24, 28])), list_node([8, 4, 12, 4, 16, 4, 20, 4, 24, 4, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 12, 16, 20, 24, 28])), list_node([8, 4, 12, 4, 16, 4, 20, 4, 24, 4, 28])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 14, 7, 49, 35, 28])), list_node([21, 7, 14, 7, 7, 7, 49, 7, 35, 7, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 14, 7, 49, 35, 28])), list_node([21, 7, 14, 7, 7, 7, 49, 7, 35, 7, 28])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([54, 27, 9, 3, 1, 3, 9, 27, 54])), list_node([54, 27, 27, 9, 9, 3, 3, 1, 1, 1, 3, 3, 9, 9, 27, 27, 54]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([54, 27, 9, 3, 1, 3, 9, 27, 54])), list_node([54, 27, 27, 9, 9, 3, 3, 1, 1, 1, 3, 3, 9, 9, 27, 27, 54])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99, 110])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99, 110])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([150, 120, 90, 60, 30, 15, 5])), list_node([150, 30, 120, 30, 90, 30, 60, 30, 30, 15, 15, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([150, 120, 90, 60, 30, 15, 5])), list_node([150, 30, 120, 30, 90, 30, 60, 30, 30, 15, 15, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([111, 222, 333, 444, 555, 666, 777, 888, 999])), list_node([111, 111, 222, 111, 333, 111, 444, 111, 555, 111, 666, 111, 777, 111, 888, 111, 999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([111, 222, 333, 444, 555, 666, 777, 888, 999])), list_node([111, 111, 222, 111, 333, 111, 444, 111, 555, 111, 666, 111, 777, 111, 888, 111, 999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 15, 5, 25])), list_node([30, 15, 15, 5, 5, 5, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 15, 5, 25])), list_node([30, 15, 15, 5, 5, 5, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([72, 48, 60, 36, 90])), list_node([72, 24, 48, 12, 60, 12, 36, 18, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([72, 48, 60, 36, 90])), list_node([72, 24, 48, 12, 60, 12, 36, 18, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([101, 103, 107, 109])), list_node([101, 1, 103, 1, 107, 1, 109]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([101, 103, 107, 109])), list_node([101, 1, 103, 1, 107, 1, 109])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([55, 110, 220, 440, 880, 1760, 3520])), list_node([55, 55, 110, 110, 220, 220, 440, 440, 880, 880, 1760, 1760, 3520]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([55, 110, 220, 440, 880, 1760, 3520])), list_node([55, 55, 110, 110, 220, 220, 440, 440, 880, 880, 1760, 1760, 3520])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([120, 80, 40, 20, 10])), list_node([120, 40, 80, 40, 40, 20, 20, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([120, 80, 40, 20, 10])), list_node([120, 40, 80, 40, 40, 20, 20, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([48, 64, 80, 96, 112, 128])), list_node([48, 16, 64, 16, 80, 16, 96, 16, 112, 16, 128]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([48, 64, 80, 96, 112, 128])), list_node([48, 16, 64, 16, 80, 16, 96, 16, 112, 16, 128])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 45, 15, 30])), list_node([100, 25, 25, 5, 45, 15, 15, 15, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 45, 15, 30])), list_node([100, 25, 25, 5, 45, 15, 15, 15, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([8, 12, 18, 24, 30])), list_node([8, 4, 12, 6, 18, 6, 24, 6, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([8, 12, 18, 24, 30])), list_node([8, 4, 12, 6, 18, 6, 24, 6, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([44, 66, 88, 110, 132])), list_node([44, 22, 66, 22, 88, 22, 110, 22, 132]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([44, 66, 88, 110, 132])), list_node([44, 22, 66, 22, 88, 22, 110, 22, 132])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([225, 150, 100, 50])), list_node([225, 75, 150, 50, 100, 50, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([225, 150, 100, 50])), list_node([225, 75, 150, 50, 100, 50, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([19, 38, 76, 152])), list_node([19, 19, 38, 38, 76, 76, 152]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([19, 38, 76, 152])), list_node([19, 19, 38, 38, 76, 76, 152])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 4, 8, 16, 32])), list_node([1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 4, 8, 16, 32])), list_node([1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([24, 36, 48, 60, 72, 84])), list_node([24, 12, 36, 12, 48, 12, 60, 12, 72, 12, 84]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([24, 36, 48, 60, 72, 84])), list_node([24, 12, 36, 12, 48, 12, 60, 12, 72, 12, 84])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([77, 14, 49, 7, 21, 35])), list_node([77, 7, 14, 7, 49, 7, 7, 7, 21, 7, 35]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([77, 14, 49, 7, 21, 35])), list_node([77, 7, 14, 7, 49, 7, 7, 7, 21, 7, 35])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 33, 66, 11, 22])), list_node([99, 33, 33, 33, 66, 11, 11, 11, 22]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 33, 66, 11, 22])), list_node([99, 33, 33, 33, 66, 11, 11, 11, 22])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([15, 30, 45, 60, 75, 90])), list_node([15, 15, 30, 15, 45, 15, 60, 15, 75, 15, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([15, 30, 45, 60, 75, 90])), list_node([15, 15, 30, 15, 45, 15, 60, 15, 75, 15, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([23, 46, 69, 92, 115, 138])), list_node([23, 23, 46, 23, 69, 23, 92, 23, 115, 23, 138]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([23, 46, 69, 92, 115, 138])), list_node([23, 23, 46, 23, 69, 23, 92, 23, 115, 23, 138])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([72, 48, 24, 12, 6])), list_node([72, 24, 48, 24, 24, 12, 12, 6, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([72, 48, 24, 12, 6])), list_node([72, 24, 48, 24, 24, 12, 12, 6, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([56, 98, 154, 224])), list_node([56, 14, 98, 14, 154, 14, 224]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([56, 98, 154, 224])), list_node([56, 14, 98, 14, 154, 14, 224])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 50, 20, 40])), list_node([100, 25, 25, 25, 50, 10, 20, 20, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 50, 20, 40])), list_node([100, 25, 25, 25, 50, 10, 20, 20, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31])), list_node([2000, 1000, 1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31])), list_node([2000, 1000, 1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 12, 18, 24, 30, 36, 42, 48, 54])), list_node([6, 6, 12, 6, 18, 6, 24, 6, 30, 6, 36, 6, 42, 6, 48, 6, 54]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 12, 18, 24, 30, 36, 42, 48, 54])), list_node([6, 6, 12, 6, 18, 6, 24, 6, 30, 6, 36, 6, 42, 6, 48, 6, 54])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([144, 72, 36, 18, 9, 3, 1])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9, 3, 3, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([144, 72, 36, 18, 9, 3, 1])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9, 3, 3, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([84, 42, 21, 105])), list_node([84, 42, 42, 21, 21, 21, 105]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([84, 42, 21, 105])), list_node([84, 42, 42, 21, 21, 21, 105])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([315, 360, 405, 450])), list_node([315, 45, 360, 45, 405, 45, 450]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([315, 360, 405, 450])), list_node([315, 45, 360, 45, 405, 45, 450])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([999, 1000, 998, 997, 996, 995])), list_node([999, 1, 1000, 2, 998, 1, 997, 1, 996, 1, 995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([999, 1000, 998, 997, 996, 995])), list_node([999, 1, 1000, 2, 998, 1, 997, 1, 996, 1, 995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([84, 105, 140, 175])), list_node([84, 21, 105, 35, 140, 35, 175]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([84, 105, 140, 175])), list_node([84, 21, 105, 35, 140, 35, 175])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 50, 25, 5])), list_node([100, 50, 50, 25, 25, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 50, 25, 5])), list_node([100, 50, 50, 25, 25, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([13, 26, 39, 52, 65])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([13, 26, 39, 52, 65])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 10, 50])), list_node([100, 25, 25, 5, 10, 10, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 10, 50])), list_node([100, 25, 25, 5, 10, 10, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([54, 24, 36, 18, 90, 60])), list_node([54, 6, 24, 12, 36, 18, 18, 18, 90, 30, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([54, 24, 36, 18, 90, 60])), list_node([54, 6, 24, 12, 36, 18, 18, 18, 90, 30, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([144, 120, 96, 72])), list_node([144, 24, 120, 24, 96, 24, 72]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([144, 120, 96, 72])), list_node([144, 24, 120, 24, 96, 24, 72])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([45, 90, 135, 180, 225, 270])), list_node([45, 45, 90, 45, 135, 45, 180, 45, 225, 45, 270]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([45, 90, 135, 180, 225, 270])), list_node([45, 45, 90, 45, 135, 45, 180, 45, 225, 45, 270])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([210, 105, 35, 7, 1])), list_node([210, 105, 105, 35, 35, 7, 7, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([210, 105, 35, 7, 1])), list_node([210, 105, 105, 35, 35, 7, 7, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 10, 5])), list_node([100, 25, 25, 5, 10, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 10, 5])), list_node([100, 25, 25, 5, 10, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 50, 75, 125])), list_node([100, 25, 25, 25, 50, 25, 75, 25, 125]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 50, 75, 125])), list_node([100, 25, 25, 25, 50, 25, 75, 25, 125])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, 250, 125, 25])), list_node([500, 250, 250, 125, 125, 25, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, 250, 125, 25])), list_node([500, 250, 250, 125, 125, 25, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([144, 108, 72, 36, 18])), list_node([144, 36, 108, 36, 72, 36, 36, 18, 18]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([144, 108, 72, 36, 18])), list_node([144, 36, 108, 36, 72, 36, 36, 18, 18])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43, 47])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43, 1, 47]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43, 47])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43, 1, 47])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([120, 180, 300, 420])), list_node([120, 60, 180, 60, 300, 60, 420]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([120, 180, 300, 420])), list_node([120, 60, 180, 60, 300, 60, 420])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([210, 231, 252, 273, 294])), list_node([210, 21, 231, 21, 252, 21, 273, 21, 294]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([210, 231, 252, 273, 294])), list_node([210, 21, 231, 21, 252, 21, 273, 21, 294])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([128, 64, 32, 16, 8, 4, 2, 1])), list_node([128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([128, 64, 32, 16, 8, 4, 2, 1])), list_node([128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([13, 26, 39, 52, 65, 78])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65, 13, 78]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([13, 26, 39, 52, 65, 78])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65, 13, 78])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([44, 55, 66, 77, 88, 99, 110])), list_node([44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([44, 55, 66, 77, 88, 99, 110])), list_node([44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([13, 13, 13, 13, 13])), list_node([13, 13, 13, 13, 13, 13, 13, 13, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([13, 13, 13, 13, 13])), list_node([13, 13, 13, 13, 13, 13, 13, 13, 13])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 33, 11, 55, 22])), list_node([99, 33, 33, 11, 11, 11, 55, 11, 22]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 33, 11, 55, 22])), list_node([99, 33, 33, 11, 11, 11, 55, 11, 22])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([17, 34, 51, 68])), list_node([17, 17, 34, 17, 51, 17, 68]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([17, 34, 51, 68])), list_node([17, 17, 34, 17, 51, 17, 68])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 27, 81, 243, 729])), list_node([9, 9, 27, 27, 81, 81, 243, 243, 729]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 27, 81, 243, 729])), list_node([9, 9, 27, 27, 81, 81, 243, 243, 729])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([72, 48, 64, 32, 16])), list_node([72, 24, 48, 16, 64, 32, 32, 16, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([72, 48, 64, 32, 16])), list_node([72, 24, 48, 16, 64, 32, 32, 16, 16])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([17, 34, 51, 68, 85])), list_node([17, 17, 34, 17, 51, 17, 68, 17, 85]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([17, 34, 51, 68, 85])), list_node([17, 17, 34, 17, 51, 17, 68, 17, 85])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([84, 56, 42, 28, 14])), list_node([84, 28, 56, 14, 42, 14, 28, 14, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([84, 56, 42, 28, 14])), list_node([84, 28, 56, 14, 42, 14, 28, 14, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([101, 202, 303, 404, 505])), list_node([101, 101, 202, 101, 303, 101, 404, 101, 505]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([101, 202, 303, 404, 505])), list_node([101, 101, 202, 101, 303, 101, 404, 101, 505])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([13, 26, 39, 52])), list_node([13, 13, 26, 13, 39, 13, 52]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([13, 26, 39, 52])), list_node([13, 13, 26, 13, 39, 13, 52])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90])), list_node([99, 1, 98, 1, 97, 1, 96, 1, 95, 1, 94, 1, 93, 1, 92, 1, 91, 1, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90])), list_node([99, 1, 98, 1, 97, 1, 96, 1, 95, 1, 94, 1, 93, 1, 92, 1, 91, 1, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([144, 72, 36, 18, 9])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([144, 72, 36, 18, 9])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 33, 11, 3])), list_node([99, 33, 33, 11, 11, 1, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 33, 11, 3])), list_node([99, 33, 33, 11, 11, 1, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([101, 103, 107, 109, 113, 127, 131, 137, 139])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113, 1, 127, 1, 131, 1, 137, 1, 139]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([101, 103, 107, 109, 113, 127, 131, 137, 139])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113, 1, 127, 1, 131, 1, 137, 1, 139])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([81, 27, 54, 108, 162])), list_node([81, 27, 27, 27, 54, 54, 108, 54, 162]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([81, 27, 54, 108, 162])), list_node([81, 27, 27, 27, 54, 54, 108, 54, 162])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([123, 246, 369, 492, 615])), list_node([123, 123, 246, 123, 369, 123, 492, 123, 615]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([123, 246, 369, 492, 615])), list_node([123, 123, 246, 123, 369, 123, 492, 123, 615])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 77, 55, 33, 11])), list_node([99, 11, 77, 11, 55, 11, 33, 11, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 77, 55, 33, 11])), list_node([99, 11, 77, 11, 55, 11, 33, 11, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([300, 150, 75, 375, 1875])), list_node([300, 150, 150, 75, 75, 75, 375, 375, 1875]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([300, 150, 75, 375, 1875])), list_node([300, 150, 150, 75, 75, 75, 375, 375, 1875])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([441, 147, 49, 7])), list_node([441, 147, 147, 49, 49, 7, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([441, 147, 49, 7])), list_node([441, 147, 147, 49, 49, 7, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 28, 35, 42, 49, 56])), list_node([21, 7, 28, 7, 35, 7, 42, 7, 49, 7, 56]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 28, 35, 42, 49, 56])), list_node([21, 7, 28, 7, 35, 7, 42, 7, 49, 7, 56])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([7, 14, 28, 56])), list_node([7, 7, 14, 14, 28, 28, 56]))
    assert is_same_list(candidate(head = list_node([33, 51, 68])), list_node([33, 3, 51, 17, 68]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50])), list_node([10, 10, 20, 10, 30, 10, 40, 10, 50]))
    assert is_same_list(candidate(head = list_node([1000, 1000])), list_node([1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([3, 9, 27, 81])), list_node([3, 3, 9, 9, 27, 27, 81]))
    assert is_same_list(candidate(head = list_node([48, 18, 30])), list_node([48, 6, 18, 6, 30]))
    assert is_same_list(candidate(head = list_node([100, 200, 300])), list_node([100, 100, 200, 100, 300]))
    assert is_same_list(candidate(head = list_node([100, 50, 25, 10])), list_node([100, 50, 50, 25, 25, 5, 10]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3])), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([7])), list_node([7]))
    assert is_same_list(candidate(head = list_node([12, 15, 20])), list_node([12, 3, 15, 5, 20]))
    assert is_same_list(candidate(head = list_node([42, 56, 14])), list_node([42, 14, 56, 14, 14]))
    assert is_same_list(candidate(head = list_node([7, 7, 7, 7])), list_node([7, 7, 7, 7, 7, 7, 7]))
    assert is_same_list(candidate(head = list_node([18, 6, 10, 3])), list_node([18, 6, 6, 2, 10, 1, 3]))
    assert is_same_list(candidate(head = list_node([8, 12, 16, 20])), list_node([8, 4, 12, 4, 16, 4, 20]))
    assert is_same_list(candidate(head = list_node([99, 81, 27])), list_node([99, 9, 81, 27, 27]))
    assert is_same_list(candidate(head = list_node([5, 15, 25, 35])), list_node([5, 5, 15, 5, 25, 5, 35]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25])), list_node([5, 5, 10, 5, 15, 5, 20, 5, 25]))
    assert is_same_list(candidate(head = list_node([12, 15, 21])), list_node([12, 3, 15, 3, 21]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125])), list_node([1000, 500, 500, 250, 250, 125, 125]))
    assert is_same_list(candidate(head = list_node([3, 5, 8, 12])), list_node([3, 1, 5, 1, 8, 4, 12]))
    assert is_same_list(candidate(head = list_node([1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([98, 49, 24, 12, 6, 3])), list_node([98, 49, 49, 1, 24, 12, 12, 6, 6, 3, 3]))
    assert is_same_list(candidate(head = list_node([13, 17, 19, 23, 29])), list_node([13, 1, 17, 1, 19, 1, 23, 1, 29]))
    assert is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99]))
    assert is_same_list(candidate(head = list_node([2023, 2021, 2019, 2017, 2015])), list_node([2023, 1, 2021, 1, 2019, 1, 2017, 1, 2015]))
    assert is_same_list(candidate(head = list_node([21, 14, 49, 35, 70, 56])), list_node([21, 7, 14, 7, 49, 7, 35, 35, 70, 14, 56]))
    assert is_same_list(candidate(head = list_node([77, 49, 35, 91, 63])), list_node([77, 7, 49, 7, 35, 7, 91, 7, 63]))
    assert is_same_list(candidate(head = list_node([60, 45, 30, 15])), list_node([60, 15, 45, 15, 30, 15, 15]))
    assert is_same_list(candidate(head = list_node([60, 30, 15, 5, 1])), list_node([60, 30, 30, 15, 15, 5, 5, 1, 1]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1]))
    assert is_same_list(candidate(head = list_node([112, 128, 144, 160, 176])), list_node([112, 16, 128, 16, 144, 16, 160, 16, 176]))
    assert is_same_list(candidate(head = list_node([77, 14, 28, 49])), list_node([77, 7, 14, 14, 28, 7, 49]))
    assert is_same_list(candidate(head = list_node([21, 35, 105, 175])), list_node([21, 7, 35, 35, 105, 35, 175]))
    assert is_same_list(candidate(head = list_node([8, 12, 18, 24])), list_node([8, 4, 12, 6, 18, 6, 24]))
    assert is_same_list(candidate(head = list_node([8, 12, 16, 20, 24, 28])), list_node([8, 4, 12, 4, 16, 4, 20, 4, 24, 4, 28]))
    assert is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77]))
    assert is_same_list(candidate(head = list_node([21, 14, 7, 49, 35, 28])), list_node([21, 7, 14, 7, 7, 7, 49, 7, 35, 7, 28]))
    assert is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([54, 27, 9, 3, 1, 3, 9, 27, 54])), list_node([54, 27, 27, 9, 9, 3, 3, 1, 1, 1, 3, 3, 9, 9, 27, 27, 54]))
    assert is_same_list(candidate(head = list_node([11, 22, 33, 44, 55, 66, 77, 88, 99, 110])), list_node([11, 11, 22, 11, 33, 11, 44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110]))
    assert is_same_list(candidate(head = list_node([150, 120, 90, 60, 30, 15, 5])), list_node([150, 30, 120, 30, 90, 30, 60, 30, 30, 15, 15, 5, 5]))
    assert is_same_list(candidate(head = list_node([111, 222, 333, 444, 555, 666, 777, 888, 999])), list_node([111, 111, 222, 111, 333, 111, 444, 111, 555, 111, 666, 111, 777, 111, 888, 111, 999]))
    assert is_same_list(candidate(head = list_node([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])), list_node([1024, 512, 512, 256, 256, 128, 128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]))
    assert is_same_list(candidate(head = list_node([30, 15, 5, 25])), list_node([30, 15, 15, 5, 5, 5, 25]))
    assert is_same_list(candidate(head = list_node([72, 48, 60, 36, 90])), list_node([72, 24, 48, 12, 60, 12, 36, 18, 90]))
    assert is_same_list(candidate(head = list_node([101, 103, 107, 109])), list_node([101, 1, 103, 1, 107, 1, 109]))
    assert is_same_list(candidate(head = list_node([55, 110, 220, 440, 880, 1760, 3520])), list_node([55, 55, 110, 110, 220, 220, 440, 440, 880, 880, 1760, 1760, 3520]))
    assert is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1]))
    assert is_same_list(candidate(head = list_node([120, 80, 40, 20, 10])), list_node([120, 40, 80, 40, 40, 20, 20, 10, 10]))
    assert is_same_list(candidate(head = list_node([48, 64, 80, 96, 112, 128])), list_node([48, 16, 64, 16, 80, 16, 96, 16, 112, 16, 128]))
    assert is_same_list(candidate(head = list_node([100, 25, 45, 15, 30])), list_node([100, 25, 25, 5, 45, 15, 15, 15, 30]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 1]))
    assert is_same_list(candidate(head = list_node([8, 12, 18, 24, 30])), list_node([8, 4, 12, 6, 18, 6, 24, 6, 30]))
    assert is_same_list(candidate(head = list_node([44, 66, 88, 110, 132])), list_node([44, 22, 66, 22, 88, 22, 110, 22, 132]))
    assert is_same_list(candidate(head = list_node([225, 150, 100, 50])), list_node([225, 75, 150, 50, 100, 50, 50]))
    assert is_same_list(candidate(head = list_node([19, 38, 76, 152])), list_node([19, 19, 38, 38, 76, 76, 152]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31, 1, 15, 1, 7, 1, 3, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 4, 8, 16, 32])), list_node([1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32]))
    assert is_same_list(candidate(head = list_node([24, 36, 48, 60, 72, 84])), list_node([24, 12, 36, 12, 48, 12, 60, 12, 72, 12, 84]))
    assert is_same_list(candidate(head = list_node([77, 14, 49, 7, 21, 35])), list_node([77, 7, 14, 7, 49, 7, 7, 7, 21, 7, 35]))
    assert is_same_list(candidate(head = list_node([99, 33, 66, 11, 22])), list_node([99, 33, 33, 33, 66, 11, 11, 11, 22]))
    assert is_same_list(candidate(head = list_node([15, 30, 45, 60, 75, 90])), list_node([15, 15, 30, 15, 45, 15, 60, 15, 75, 15, 90]))
    assert is_same_list(candidate(head = list_node([23, 46, 69, 92, 115, 138])), list_node([23, 23, 46, 23, 69, 23, 92, 23, 115, 23, 138]))
    assert is_same_list(candidate(head = list_node([72, 48, 24, 12, 6])), list_node([72, 24, 48, 24, 24, 12, 12, 6, 6]))
    assert is_same_list(candidate(head = list_node([56, 98, 154, 224])), list_node([56, 14, 98, 14, 154, 14, 224]))
    assert is_same_list(candidate(head = list_node([100, 25, 50, 20, 40])), list_node([100, 25, 25, 25, 50, 10, 20, 20, 40]))
    assert is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31])), list_node([2000, 1000, 1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31]))
    assert is_same_list(candidate(head = list_node([6, 12, 18, 24, 30, 36, 42, 48, 54])), list_node([6, 6, 12, 6, 18, 6, 24, 6, 30, 6, 36, 6, 42, 6, 48, 6, 54]))
    assert is_same_list(candidate(head = list_node([144, 72, 36, 18, 9, 3, 1])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9, 3, 3, 1, 1]))
    assert is_same_list(candidate(head = list_node([84, 42, 21, 105])), list_node([84, 42, 42, 21, 21, 21, 105]))
    assert is_same_list(candidate(head = list_node([315, 360, 405, 450])), list_node([315, 45, 360, 45, 405, 45, 450]))
    assert is_same_list(candidate(head = list_node([999, 1000, 998, 997, 996, 995])), list_node([999, 1, 1000, 2, 998, 1, 997, 1, 996, 1, 995]))
    assert is_same_list(candidate(head = list_node([84, 105, 140, 175])), list_node([84, 21, 105, 35, 140, 35, 175]))
    assert is_same_list(candidate(head = list_node([100, 50, 25, 5])), list_node([100, 50, 50, 25, 25, 5, 5]))
    assert is_same_list(candidate(head = list_node([13, 26, 39, 52, 65])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65]))
    assert is_same_list(candidate(head = list_node([100, 25, 10, 50])), list_node([100, 25, 25, 5, 10, 10, 50]))
    assert is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113]))
    assert is_same_list(candidate(head = list_node([54, 24, 36, 18, 90, 60])), list_node([54, 6, 24, 12, 36, 18, 18, 18, 90, 30, 60]))
    assert is_same_list(candidate(head = list_node([144, 120, 96, 72])), list_node([144, 24, 120, 24, 96, 24, 72]))
    assert is_same_list(candidate(head = list_node([45, 90, 135, 180, 225, 270])), list_node([45, 45, 90, 45, 135, 45, 180, 45, 225, 45, 270]))
    assert is_same_list(candidate(head = list_node([210, 105, 35, 7, 1])), list_node([210, 105, 105, 35, 35, 7, 7, 1, 1]))
    assert is_same_list(candidate(head = list_node([100, 25, 10, 5])), list_node([100, 25, 25, 5, 10, 5, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]))
    assert is_same_list(candidate(head = list_node([100, 25, 50, 75, 125])), list_node([100, 25, 25, 25, 50, 25, 75, 25, 125]))
    assert is_same_list(candidate(head = list_node([500, 250, 125, 25])), list_node([500, 250, 250, 125, 125, 25, 25]))
    assert is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200]))
    assert is_same_list(candidate(head = list_node([100, 25, 50, 125, 200])), list_node([100, 25, 25, 25, 50, 25, 125, 25, 200]))
    assert is_same_list(candidate(head = list_node([144, 108, 72, 36, 18])), list_node([144, 36, 108, 36, 72, 36, 36, 18, 18]))
    assert is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43, 47])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43, 1, 47]))
    assert is_same_list(candidate(head = list_node([120, 180, 300, 420])), list_node([120, 60, 180, 60, 300, 60, 420]))
    assert is_same_list(candidate(head = list_node([210, 231, 252, 273, 294])), list_node([210, 21, 231, 21, 252, 21, 273, 21, 294]))
    assert is_same_list(candidate(head = list_node([128, 64, 32, 16, 8, 4, 2, 1])), list_node([128, 64, 64, 32, 32, 16, 16, 8, 8, 4, 4, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([13, 26, 39, 52, 65, 78])), list_node([13, 13, 26, 13, 39, 13, 52, 13, 65, 13, 78]))
    assert is_same_list(candidate(head = list_node([44, 55, 66, 77, 88, 99, 110])), list_node([44, 11, 55, 11, 66, 11, 77, 11, 88, 11, 99, 11, 110]))
    assert is_same_list(candidate(head = list_node([13, 13, 13, 13, 13])), list_node([13, 13, 13, 13, 13, 13, 13, 13, 13]))
    assert is_same_list(candidate(head = list_node([99, 33, 11, 55, 22])), list_node([99, 33, 33, 11, 11, 11, 55, 11, 22]))
    assert is_same_list(candidate(head = list_node([17, 34, 51, 68])), list_node([17, 17, 34, 17, 51, 17, 68]))
    assert is_same_list(candidate(head = list_node([17, 19, 23, 29, 31, 37, 41, 43])), list_node([17, 1, 19, 1, 23, 1, 29, 1, 31, 1, 37, 1, 41, 1, 43]))
    assert is_same_list(candidate(head = list_node([9, 27, 81, 243, 729])), list_node([9, 9, 27, 27, 81, 81, 243, 243, 729]))
    assert is_same_list(candidate(head = list_node([72, 48, 64, 32, 16])), list_node([72, 24, 48, 16, 64, 32, 32, 16, 16]))
    assert is_same_list(candidate(head = list_node([17, 34, 51, 68, 85])), list_node([17, 17, 34, 17, 51, 17, 68, 17, 85]))
    assert is_same_list(candidate(head = list_node([84, 56, 42, 28, 14])), list_node([84, 28, 56, 14, 42, 14, 28, 14, 14]))
    assert is_same_list(candidate(head = list_node([101, 202, 303, 404, 505])), list_node([101, 101, 202, 101, 303, 101, 404, 101, 505]))
    assert is_same_list(candidate(head = list_node([13, 26, 39, 52])), list_node([13, 13, 26, 13, 39, 13, 52]))
    assert is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90])), list_node([99, 1, 98, 1, 97, 1, 96, 1, 95, 1, 94, 1, 93, 1, 92, 1, 91, 1, 90]))
    assert is_same_list(candidate(head = list_node([101, 103, 107, 109, 113])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31])), list_node([1000, 500, 500, 250, 250, 125, 125, 1, 62, 31, 31]))
    assert is_same_list(candidate(head = list_node([144, 72, 36, 18, 9])), list_node([144, 72, 72, 36, 36, 18, 18, 9, 9]))
    assert is_same_list(candidate(head = list_node([99, 33, 11, 3])), list_node([99, 33, 33, 11, 11, 1, 3]))
    assert is_same_list(candidate(head = list_node([101, 103, 107, 109, 113, 127, 131, 137, 139])), list_node([101, 1, 103, 1, 107, 1, 109, 1, 113, 1, 127, 1, 131, 1, 137, 1, 139]))
    assert is_same_list(candidate(head = list_node([81, 27, 54, 108, 162])), list_node([81, 27, 27, 27, 54, 54, 108, 54, 162]))
    assert is_same_list(candidate(head = list_node([123, 246, 369, 492, 615])), list_node([123, 123, 246, 123, 369, 123, 492, 123, 615]))
    assert is_same_list(candidate(head = list_node([99, 77, 55, 33, 11])), list_node([99, 11, 77, 11, 55, 11, 33, 11, 11]))
    assert is_same_list(candidate(head = list_node([300, 150, 75, 375, 1875])), list_node([300, 150, 150, 75, 75, 75, 375, 375, 1875]))
    assert is_same_list(candidate(head = list_node([441, 147, 49, 7])), list_node([441, 147, 147, 49, 49, 7, 7]))
    assert is_same_list(candidate(head = list_node([81, 27, 9, 3, 1])), list_node([81, 27, 27, 9, 9, 3, 3, 1, 1]))
    assert is_same_list(candidate(head = list_node([21, 28, 35, 42, 49, 56])), list_node([21, 7, 28, 7, 35, 7, 42, 7, 49, 7, 56]))


