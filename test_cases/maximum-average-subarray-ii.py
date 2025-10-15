def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5],k = 3) == -2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5],k = 3) == -2.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 3) == 3333.3333302289248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 3) == 3333.3333302289248: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 12, -5, -6, 50, 3],k = 4) == 12.749995231628418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 12, -5, -6, 50, 3],k = 4) == 12.749995231628418: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5],k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5],k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 0, 4, 3, 3],k = 2) == 3.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 0, 4, 3, 3],k = 2) == 3.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 8) == 1150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 8) == 1150.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 3) == -2000.0000074505806
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 3) == -2000.0000074505806: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10],k = 10) == 0.3636355400085449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10],k = 10) == 0.3636355400085449: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100],k = 10) == 549.9999970197678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100],k = 10) == 549.9999970197678: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 6) == 1428.5714272409678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 6) == 1428.5714272409678: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 69.99999642372131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 69.99999642372131: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 699.9999977648258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 699.9999977648258: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 20) == 15.499996185302734
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 20) == 15.499996185302734: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 4) == 0.9999942779541016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 4) == 0.9999942779541016: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 20, -30, 40, -50, 60, -70, 80, -90],k = 6) == 7.142856419086456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 20, -30, 40, -50, 60, -70, 80, -90],k = 6) == 7.142856419086456: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 15) == 12.933327674865723
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 15) == 12.933327674865723: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6) == 2.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6) == 2.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 4) == 13.99999886751175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 4) == 13.99999886751175: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 1.4285659790039062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 1.4285659790039062: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 115.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 115.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 5) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 5) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 129.99999523162842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 129.99999523162842: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, -3, 2, 1, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16],k = 7) == 1.8571383953094482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, -3, 2, 1, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16],k = 7) == 1.8571383953094482: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 0.9999942779541016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 0.9999942779541016: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 12.999999523162842
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 12.999999523162842: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 1999.9999925494194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 1999.9999925494194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 1) == 1499.9999947845936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 1) == 1499.9999947845936: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 15) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 15) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 4) == 0.1999969482421875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 4) == 0.1999969482421875: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 3) == 16.66666269302368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 3) == 16.66666269302368: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 11.999998092651367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 11.999998092651367: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 799.9999985098839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 799.9999985098839: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == -2.500002861022949
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == -2.500002861022949: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 5) == 1999.9999925494194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 5) == 1999.9999925494194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1, 2],k = 4) == 0.9999980926513672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1, 2],k = 4) == 0.9999980926513672: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 3) == 1.6666603088378906
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 3) == 1.6666603088378906: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 5) == 1.9999980926513672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 5) == 1.9999980926513672: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 1, 2, 8, 7, 6, 3, 4, 9],k = 4) == 6.166664123535156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 1, 2, 8, 7, 6, 3, 4, 9],k = 4) == 6.166664123535156: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1000, 500, -2000, 1500, -3000, 2500, -4000, 3500, -5000],k = 5) == 99.99999683350325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1000, 500, -2000, 1500, -3000, 2500, -4000, 3500, -5000],k = 5) == 99.99999683350325: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],k = 5) == 15.999999940395355
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],k = 5) == 15.999999940395355: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 17.999993562698364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 17.999993562698364: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10) == -10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10) == -10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000, -10000],k = 5) == 1399.9999929219484
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000, -10000],k = 5) == 1399.9999929219484: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == -2.000004768371582
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == -2.000004768371582: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 8) == 1.2222163677215576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 8) == 1.2222163677215576: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 6) == 1249.999999254942
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 6) == 1249.999999254942: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-100, 100, -100, 100, -100, 100, -100, 100, -100, 100],k = 6) == 14.28571343421936
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-100, 100, -100, 100, -100, 100, -100, 100, -100, 100],k = 6) == 14.28571343421936: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -3.0000009536743164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -3.0000009536743164: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000],k = 3) == 3999.9999944120646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000],k = 3) == 3999.9999944120646: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 899.9999992549419
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 899.9999992549419: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 119.99999761581421
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 119.99999761581421: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 100) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 100) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 16.999993324279785
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 16.999993324279785: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 100) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 100) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == 0.0666656494140625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == 0.0666656494140625: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 8) == 1.4999961853027344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 8) == 1.4999961853027344: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 3) == 2.666663646697998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 3) == 2.666663646697998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 4.499999046325684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 4.499999046325684: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30],k = 15) == -8.00000548362732
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30],k = 15) == -8.00000548362732: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 5) == 2.59999680519104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 5) == 2.59999680519104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 10.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 10.5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 4) == 1999.9999925494194
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 4) == 1999.9999925494194: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, -50, 200, -150, 300, -250, 400, -350, 500, -450],k = 5) == 119.99999433755875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, -50, 200, -150, 300, -250, 400, -350, 500, -450],k = 5) == 119.99999433755875: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 30) == 35.499995946884155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 30) == 35.499995946884155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 15.499999046325684
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 15.499999046325684: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, -5, 20, -100, 30, 40, -20, 50, 60, -30],k = 6) == 21.66666030883789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, -5, 20, -100, 30, 40, -20, 50, 60, -30],k = 6) == 21.66666030883789: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 37.99999988079071
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 37.99999988079071: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 5.999998092651367
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 5.999998092651367: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 0.1999969482421875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 0.1999969482421875: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == 0.11110687255859375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == 0.11110687255859375: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3) == 0.3333282470703125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3) == 0.3333282470703125: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 2) == -1.5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 7.999999046325684
    assert candidate(nums = [-1, -2, -3, -4, -5],k = 3) == -2.0
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000],k = 3) == 3333.3333302289248
    assert candidate(nums = [1, 12, -5, -6, 50, 3],k = 4) == 12.749995231628418
    assert candidate(nums = [5],k = 1) == 5
    assert candidate(nums = [4, 0, 4, 3, 3],k = 2) == 3.5
    assert candidate(nums = [10, 20, 30, 40, 50],k = 3) == 40.0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 8) == 1150.0
    assert candidate(nums = [-10000, -9000, -8000, -7000, -6000, -5000, -4000, -3000, -2000, -1000],k = 3) == -2000.0000074505806
    assert candidate(nums = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10],k = 10) == 0.3636355400085449
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, -1000, -900, -800, -700, -600, -500, -400, -300, -200, -100],k = 10) == 549.9999970197678
    assert candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 6) == 1428.5714272409678
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 7) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 7) == 69.99999642372131
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10000) == 10000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 7) == 699.9999977648258
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 20) == 15.499996185302734
    assert candidate(nums = [5, -5, 5, -5, 5, -5, 5, -5, 5, -5],k = 4) == 0.9999942779541016
    assert candidate(nums = [10, -5, 20, -30, 40, -50, 60, -70, 80, -90],k = 6) == 7.142856419086456
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19],k = 15) == 12.933327674865723
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],k = 6) == 2.5
    assert candidate(nums = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100],k = 4) == 13.99999886751175
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 7) == 1.4285659790039062
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 55.0
    assert candidate(nums = [50, 20, 30, 10, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 8) == 115.0
    assert candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 5) == 5000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 15) == 129.99999523162842
    assert candidate(nums = [5, -3, 2, 1, -2, 3, -1, 4, -5, 6, -7, 8, -9, 10, -11, 12, -13, 14, -15, 16],k = 7) == 1.8571383953094482
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 5) == 0.9999942779541016
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 15) == 12.999999523162842
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 4) == 1999.9999925494194
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 1) == 1499.9999947845936
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 15) == 10000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 4) == 0.1999969482421875
    assert candidate(nums = [10, -10, 20, -20, 30, -30, 40, -40, 50, -50],k = 3) == 16.66666269302368
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 7) == 11.999998092651367
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1) == 0
    assert candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 5) == 1999.9999925494194
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 799.9999985098839
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 4) == -2.500002861022949
    assert candidate(nums = [10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000],k = 5) == 1999.9999925494194
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [1, 2, -1, 2, -1, 2, -1, 2, -1, 2],k = 4) == 0.9999980926513672
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5],k = 3) == 1.6666603088378906
    assert candidate(nums = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10],k = 5) == 1.9999980926513672
    assert candidate(nums = [10, 5, 1, 2, 8, 7, 6, 3, 4, 9],k = 4) == 6.166664123535156
    assert candidate(nums = [-1000, 500, -2000, 1500, -3000, 2500, -4000, 3500, -5000],k = 5) == 99.99999683350325
    assert candidate(nums = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100],k = 5) == 15.999999940395355
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 25) == 17.999993562698364
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == 5
    assert candidate(nums = [-10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000, -10000],k = 10) == -10000
    assert candidate(nums = [1000, 2000, 3000, -4000, 5000, -6000, 7000, -8000, 9000, -10000],k = 5) == 1399.9999929219484
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 3) == -2.000004768371582
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 8) == 1.2222163677215576
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 6) == 1249.999999254942
    assert candidate(nums = [-100, 100, -100, 100, -100, 100, -100, 100, -100, 100],k = 6) == 14.28571343421936
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 5) == -3.0000009536743164
    assert candidate(nums = [5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000],k = 3) == 3999.9999944120646
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 3) == 899.9999992549419
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 7) == 119.99999761581421
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 100) == 0.0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 30) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 16.999993324279785
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10) == 1
    assert candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 100) == 5000
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 15) == 0.0666656494140625
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 1
    assert candidate(nums = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 8) == 1.4999961853027344
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],k = 3) == 2.666663646697998
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10],k = 10) == 4.499999046325684
    assert candidate(nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30],k = 15) == -8.00000548362732
    assert candidate(nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15],k = 5) == 2.59999680519104
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 20) == 10.5
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 5) == 0
    assert candidate(nums = [-10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000, 10000],k = 4) == 1999.9999925494194
    assert candidate(nums = [100, -50, 200, -150, 300, -250, 400, -350, 500, -450],k = 5) == 119.99999433755875
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 30) == 35.499995946884155
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 2) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 15.499999046325684
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 50) == 0
    assert candidate(nums = [10, -5, 20, -100, 30, 40, -20, 50, 60, -30],k = 6) == 21.66666030883789
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 25) == 37.99999988079071
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 15) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 20) == 5.999998092651367
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],k = 10) == 10000
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 5) == 0.1999969482421875
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10) == 0
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 8) == 0.11110687255859375
    assert candidate(nums = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],k = 3) == 0.3333282470703125


