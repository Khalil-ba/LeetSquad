def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 506
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 506: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 3, 8, 9, 2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 3, 8, 9, 2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 320
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 320: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 8, 3, 10, 1, 3, 3, 9, 5]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 8, 3, 10, 1, 3, 3, 9, 5]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1, 2, 3, 1000000000]) == 2000000003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1, 2, 3, 1000000000]) == 2000000003: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 3, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 3, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(power = [7, 1, 6, 6]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [7, 1, 6, 6]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82]) == 415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82]) == 415: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2650: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 6, 8, 10, 11, 13, 15, 17, 18, 20]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 6, 8, 10, 11, 13, 15, 17, 18, 20]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1111111111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1111111111: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84]) == 1218
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84]) == 1218: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 117: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22]) == 612
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22]) == 612: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1045
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1045: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 3250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 3250: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]) == 970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]) == 970: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 157
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 157: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982, 999999980, 999999978, 999999976, 999999974, 999999972, 999999970, 999999968, 999999966, 999999964, 999999962]) == 9999999820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982, 999999980, 999999978, 999999976, 999999974, 999999972, 999999970, 999999968, 999999966, 999999964, 999999962]) == 9999999820: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 255: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 777
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 777: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982]) == 4999999960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982]) == 4999999960: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 3999999982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 3999999982: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992]) == 2999999988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992]) == 2999999988: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988]) == 3999999976
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988]) == 3999999976: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 5, 9, 10, 11, 14, 18, 20, 21, 23, 27, 28, 30, 31, 34, 38, 40, 41, 43]) == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 5, 9, 10, 11, 14, 18, 20, 21, 23, 27, 28, 30, 31, 34, 38, 40, 41, 43]) == 251: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]) == 1225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]) == 1225: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1000000000, 2, 999999998, 3, 999999996, 4, 999999994, 5, 999999992, 6, 999999990, 7, 999999988, 8, 999999986, 9, 999999984, 10, 999999982]) == 4999999982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1000000000, 2, 999999998, 3, 999999996, 4, 999999994, 5, 999999992, 6, 999999990, 7, 999999988, 8, 999999986, 9, 999999984, 10, 999999982]) == 4999999982: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 480: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41, 43, 46, 48, 51, 53, 56, 58, 61, 63]) == 429
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41, 43, 46, 48, 51, 53, 56, 58, 61, 63]) == 429: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 55, 55]) == 650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 55, 55]) == 650: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 4650
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 4650: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993]) == 3000000006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993]) == 3000000006: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 551
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 551: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 1395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 1395: {e}')
    
    total += 1
    try:
        result = candidate(power = [1000000000, 1000000000, 1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992]) == 4999999991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1000000000, 1000000000, 1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992]) == 4999999991: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 239: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 1890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 1890: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]) == 1717
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]) == 1717: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]) == 1236
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]) == 1236: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(power = [10, 12, 10, 14, 12, 16, 14, 18, 16, 20, 18, 22, 20, 24, 22, 26, 24, 28, 26, 30]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [10, 12, 10, 14, 12, 16, 14, 18, 16, 20, 18, 22, 20, 24, 22, 26, 24, 28, 26, 30]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 221: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(power = [9, 2, 8, 3, 7, 4, 6, 5, 1, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [9, 2, 8, 3, 7, 4, 6, 5, 1, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 235: {e}')
    
    total += 1
    try:
        result = candidate(power = [3, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [3, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) == 1625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) == 1625: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(power = [1, 3, 6, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33, 35, 38, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75]) == 604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [1, 3, 6, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33, 35, 38, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75]) == 604: {e}')
    
    total += 1
    try:
        result = candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(power = [5, 5, 5, 5, 5]) == 25
    assert candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]) == 506
    assert candidate(power = [5, 3, 8, 9, 2]) == 16
    assert candidate(power = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]) == 320
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
    assert candidate(power = [3, 8, 3, 10, 1, 3, 3, 9, 5]) == 22
    assert candidate(power = [10, 20, 30, 40, 50]) == 150
    assert candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60
    assert candidate(power = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5000000000
    assert candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 60
    assert candidate(power = [10, 20, 30, 40, 50]) == 150
    assert candidate(power = [1000000000, 1, 2, 3, 1000000000]) == 2000000003
    assert candidate(power = [1, 1, 3, 4]) == 6
    assert candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
    assert candidate(power = [7, 1, 6, 6]) == 13
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 22
    assert candidate(power = [5, 5, 5, 5]) == 20
    assert candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13]) == 24
    assert candidate(power = [1000000000, 1000000000, 1000000000, 1000000000]) == 4000000000
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 55
    assert candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 550
    assert candidate(power = [1, 10, 19, 28, 37, 46, 55, 64, 73, 82]) == 415
    assert candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 2650
    assert candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(power = [5, 6, 8, 10, 11, 13, 15, 17, 18, 20]) == 66
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 77
    assert candidate(power = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 1111111111
    assert candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74]) == 950
    assert candidate(power = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84]) == 1218
    assert candidate(power = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 18
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 117
    assert candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 6, 7, 8, 9, 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22]) == 612
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210
    assert candidate(power = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1045
    assert candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]) == 3250
    assert candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 21000
    assert candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 44
    assert candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]) == 970
    assert candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 1050
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 120
    assert candidate(power = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5]) == 157
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
    assert candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982, 999999980, 999999978, 999999976, 999999974, 999999972, 999999970, 999999968, 999999966, 999999964, 999999962]) == 9999999820
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 44
    assert candidate(power = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]) == 66
    assert candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 255
    assert candidate(power = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18]) == 42
    assert candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]) == 777
    assert candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]) == 190
    assert candidate(power = [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]) == 990
    assert candidate(power = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12]) == 66
    assert candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988, 999999986, 999999984, 999999982]) == 4999999960
    assert candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5500
    assert candidate(power = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991, 999999990]) == 3999999982
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 210
    assert candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992]) == 2999999988
    assert candidate(power = [1000000000, 999999998, 999999996, 999999994, 999999992, 999999990, 999999988]) == 3999999976
    assert candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 150
    assert candidate(power = [1, 2, 5, 9, 10, 11, 14, 18, 20, 21, 23, 27, 28, 30, 31, 34, 38, 40, 41, 43]) == 251
    assert candidate(power = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]) == 1225
    assert candidate(power = [1, 1000000000, 2, 999999998, 3, 999999996, 4, 999999994, 5, 999999992, 6, 999999990, 7, 999999988, 8, 999999986, 9, 999999984, 10, 999999982]) == 4999999982
    assert candidate(power = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == 480
    assert candidate(power = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31, 33, 36, 38, 41, 43, 46, 48, 51, 53, 56, 58, 61, 63]) == 429
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325
    assert candidate(power = [10, 10, 15, 15, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 45, 45, 50, 50, 55, 55]) == 650
    assert candidate(power = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]) == 90
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 1, 3, 5, 7, 9]) == 220
    assert candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 105
    assert candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]) == 2325
    assert candidate(power = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15]) == 69
    assert candidate(power = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]) == 345
    assert candidate(power = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 4650
    assert candidate(power = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997, 5, 999999996, 6, 999999995, 7, 999999994, 8, 999999993]) == 3000000006
    assert candidate(power = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 551
    assert candidate(power = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 73
    assert candidate(power = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 147
    assert candidate(power = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]) == 1395
    assert candidate(power = [1000000000, 1000000000, 1000000000, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992]) == 4999999991
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]) == 239
    assert candidate(power = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135, 144, 153, 162, 171, 180]) == 1890
    assert candidate(power = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]) == 1717
    assert candidate(power = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]) == 1236
    assert candidate(power = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 465
    assert candidate(power = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90
    assert candidate(power = [10, 12, 10, 14, 12, 16, 14, 18, 16, 20, 18, 22, 20, 24, 22, 26, 24, 28, 26, 30]) == 210
    assert candidate(power = [5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 221
    assert candidate(power = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 90
    assert candidate(power = [9, 2, 8, 3, 7, 4, 6, 5, 1, 10, 19, 11, 18, 12, 17, 13, 16, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165
    assert candidate(power = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 165
    assert candidate(power = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 30
    assert candidate(power = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 2100
    assert candidate(power = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]) == 235
    assert candidate(power = [3, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 325
    assert candidate(power = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 100
    assert candidate(power = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) == 1625
    assert candidate(power = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 28
    assert candidate(power = [1, 3, 6, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33, 35, 38, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75]) == 604
    assert candidate(power = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 12000


