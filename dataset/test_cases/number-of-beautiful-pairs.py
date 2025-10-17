def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 12, 45, 56]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 12, 45, 56]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 14, 25, 78]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 14, 25, 78]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 202]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 202]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 31, 17, 71]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 31, 17, 71]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [78, 89, 90, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [78, 89, 90, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 12, 45]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 12, 45]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 23, 34, 45, 56]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 23, 34, 45, 56]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 21, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 21, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 1, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 1, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 97, 79, 92]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 97, 79, 92]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 14, 25, 77]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 14, 25, 77]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 876, 765, 654, 543]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 876, 765, 654, 543]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 6543, 3210, 1234]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 6543, 3210, 1234]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98, 17, 31, 44]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98, 17, 31, 44]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [991, 992, 993, 994, 995, 996, 997, 998, 999]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [991, 992, 993, 994, 995, 996, 997, 998, 999]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 876, 765, 654, 543, 432, 321, 210, 109]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 876, 765, 654, 543, 432, 321, 210, 109]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 21, 13, 31, 14, 41, 15, 51, 16, 61]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 21, 13, 31, 14, 41, 15, 51, 16, 61]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 21, 33, 40, 55]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 21, 33, 40, 55]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 6543, 3210, 123, 456, 789]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 6543, 3210, 123, 456, 789]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 73, 17, 79, 97, 37, 71, 13, 39]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 73, 17, 79, 97, 37, 71, 13, 39]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2468, 1357, 8642, 7531, 9753]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2468, 1357, 8642, 7531, 9753]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [22, 44, 88, 16, 32, 64]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [22, 44, 88, 16, 32, 64]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 76, 53, 20, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 76, 53, 20, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 54321, 98765, 56789, 13579]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 54321, 98765, 56789, 13579]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [135, 246, 357, 468, 579, 681, 792, 813, 924]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [135, 246, 357, 468, 579, 681, 792, 813, 924]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 23, 34, 45, 56, 67, 78, 89, 91]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 23, 34, 45, 56, 67, 78, 89, 91]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9989, 9988, 9987, 9986]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9989, 9988, 9987, 9986]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 34, 56, 78, 90, 21, 43, 65, 87, 99]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 34, 56, 78, 90, 21, 43, 65, 87, 99]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 9101, 1112, 1314]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 9101, 1112, 1314]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 654, 321, 111, 222]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 654, 321, 111, 222]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 112, 131]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 112, 131]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 2020, 3030, 4040]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 2020, 3030, 4040]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 9101, 11213, 141516]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 9101, 11213, 141516]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6789, 5678, 4567, 3456, 2345, 1234]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6789, 5678, 4567, 3456, 2345, 1234]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 76, 54, 32, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 76, 54, 32, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 202]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 202]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 5432, 1234, 5678, 9012]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 5432, 1234, 5678, 9012]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10101, 20202, 30303, 40404, 50505, 60606, 70707, 80808, 90909]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10101, 20202, 30303, 40404, 50505, 60606, 70707, 80808, 90909]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 21, 34, 43, 56, 65, 78, 87, 90]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 21, 34, 43, 56, 65, 78, 87, 90]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8888, 7777, 6666, 5555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8888, 7777, 6666, 5555]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 6543, 3210, 9876, 6543]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 6543, 3210, 9876, 6543]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 888, 777, 666, 555, 444]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 888, 777, 666, 555, 444]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2357, 1113, 1719, 2329, 3137]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2357, 1113, 1719, 2329, 3137]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [135, 246, 357, 468, 579]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [135, 246, 357, 468, 579]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 29, 39, 49, 59, 69, 79, 89, 97, 98, 96, 95, 94, 93, 92, 91]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 29, 39, 49, 59, 69, 79, 89, 97, 98, 96, 95, 94, 93, 92, 91]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 4321, 5678, 8765, 9012]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 4321, 5678, 8765, 9012]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 4321, 5678, 8765, 9876]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 4321, 5678, 8765, 9876]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 203, 305, 407, 509]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 203, 305, 407, 509]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 8765, 7654, 6543, 5432]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 8765, 7654, 6543, 5432]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [234, 345, 456, 567, 678, 789, 890, 901]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [234, 345, 456, 567, 678, 789, 890, 901]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13, 31, 37, 73, 79, 97]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13, 31, 37, 73, 79, 97]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 6543, 3210, 9870]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 6543, 3210, 9870]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 321, 456, 654, 789, 987, 246, 642]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 321, 456, 654, 789, 987, 246, 642]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1009, 2008, 3007, 4006, 5005]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1009, 2008, 3007, 4006, 5005]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 97, 75, 53, 31, 19, 98, 87]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 97, 75, 53, 31, 19, 98, 87]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 224, 335, 446, 557]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 224, 335, 446, 557]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 234, 357, 479, 591]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 234, 357, 479, 591]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [23, 32, 45, 54, 67, 76, 89, 98, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [23, 32, 45, 54, 67, 76, 89, 98, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 2223, 3335, 4447]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 2223, 3335, 4447]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 9101, 1121, 2132, 3143]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 9101, 1121, 2132, 3143]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13579, 24680, 97531, 86420, 1029384756]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13579, 24680, 97531, 86420, 1029384756]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [911, 822, 733, 644, 555, 466]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [911, 822, 733, 644, 555, 466]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [13579, 2468, 97531, 86420, 7539, 6428, 5317, 4206]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [13579, 2468, 97531, 86420, 7539, 6428, 5317, 4206]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876, 5432, 3210, 1098, 7654]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876, 5432, 3210, 1098, 7654]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [19, 28, 37, 46, 55, 64, 73, 82, 91]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [19, 28, 37, 46, 55, 64, 73, 82, 91]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [89, 97, 103, 107, 109]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [89, 97, 103, 107, 109]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111222, 222333, 333444, 444555, 555666, 666777, 777888, 888999, 999111]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111222, 222333, 333444, 444555, 555666, 666777, 777888, 888999, 999111]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 54321, 90876, 23456]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 54321, 90876, 23456]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 654, 321, 123, 456, 789]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 654, 321, 123, 456, 789]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9998, 7775, 5552, 3337, 1111]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9998, 7775, 5552, 3337, 1111]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1023, 4567, 8910, 1123]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1023, 4567, 8910, 1123]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 200, 300, 400]) == 3
    assert candidate(nums = [34, 23, 12, 45, 56]) == 5
    assert candidate(nums = [33, 14, 25, 78]) == 5
    assert candidate(nums = [123, 456, 789, 101, 202]) == 9
    assert candidate(nums = [13, 31, 17, 71]) == 6
    assert candidate(nums = [78, 89, 90, 12]) == 3
    assert candidate(nums = [111, 222, 333, 444]) == 5
    assert candidate(nums = [34, 23, 12, 45]) == 4
    assert candidate(nums = [12, 23, 34, 45, 56]) == 6
    assert candidate(nums = [1, 2, 3, 4, 5]) == 9
    assert candidate(nums = [11, 21, 12]) == 2
    assert candidate(nums = [2, 5, 1, 4]) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 27
    assert candidate(nums = [29, 97, 79, 92]) == 4
    assert candidate(nums = [123, 456, 789, 101]) == 6
    assert candidate(nums = [33, 14, 25, 77]) == 6
    assert candidate(nums = [987, 876, 765, 654, 543]) == 6
    assert candidate(nums = [9876, 6543, 3210, 1234]) == 2
    assert candidate(nums = [98, 17, 31, 44]) == 6
    assert candidate(nums = [991, 992, 993, 994, 995, 996, 997, 998, 999]) == 21
    assert candidate(nums = [987, 876, 765, 654, 543, 432, 321, 210, 109]) == 20
    assert candidate(nums = [12, 21, 13, 31, 14, 41, 15, 51, 16, 61]) == 41
    assert candidate(nums = [15, 21, 33, 40, 55]) == 8
    assert candidate(nums = [13, 26, 39, 52, 65, 78, 91]) == 17
    assert candidate(nums = [111, 222, 333, 444, 555]) == 9
    assert candidate(nums = [9876, 6543, 3210, 123, 456, 789]) == 3
    assert candidate(nums = [31, 73, 17, 79, 97, 37, 71, 13, 39]) == 23
    assert candidate(nums = [2468, 1357, 8642, 7531, 9753]) == 9
    assert candidate(nums = [22, 44, 88, 16, 32, 64]) == 3
    assert candidate(nums = [89, 76, 53, 20, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55
    assert candidate(nums = [12345, 54321, 98765, 56789, 13579]) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 128
    assert candidate(nums = [135, 246, 357, 468, 579, 681, 792, 813, 924]) == 25
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321]) == 11
    assert candidate(nums = [12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123]) == 25
    assert candidate(nums = [12, 23, 34, 45, 56, 67, 78, 89, 91]) == 27
    assert candidate(nums = [1234, 2345, 3456, 4567, 5678]) == 7
    assert candidate(nums = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9989, 9988, 9987, 9986]) == 40
    assert candidate(nums = [12, 34, 56, 78, 90, 21, 43, 65, 87, 99]) == 34
    assert candidate(nums = [1234, 5678, 9101, 1112, 1314]) == 10
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 27
    assert candidate(nums = [987, 654, 321, 111, 222]) == 9
    assert candidate(nums = [123, 456, 789, 101, 112, 131]) == 14
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1010, 2020, 3030, 4040]) == 34
    assert candidate(nums = [1234, 5678, 9101, 11213, 141516]) == 8
    assert candidate(nums = [25, 50, 75, 100, 125]) == 4
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84]) == 73
    assert candidate(nums = [6789, 5678, 4567, 3456, 2345, 1234]) == 8
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 27
    assert candidate(nums = [89, 76, 54, 32, 10]) == 3
    assert candidate(nums = [123, 456, 789, 101, 202]) == 9
    assert candidate(nums = [9876, 5432, 1234, 5678, 9012]) == 10
    assert candidate(nums = [10101, 20202, 30303, 40404, 50505, 60606, 70707, 80808, 90909]) == 27
    assert candidate(nums = [12, 21, 34, 43, 56, 65, 78, 87, 90]) == 19
    assert candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 24
    assert candidate(nums = [8888, 7777, 6666, 5555]) == 5
    assert candidate(nums = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111]) == 27
    assert candidate(nums = [9876, 6543, 3210, 9876, 6543]) == 0
    assert candidate(nums = [999, 888, 777, 666, 555, 444]) == 11
    assert candidate(nums = [2357, 1113, 1719, 2329, 3137]) == 10
    assert candidate(nums = [135, 246, 357, 468, 579]) == 8
    assert candidate(nums = [29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 57
    assert candidate(nums = [19, 29, 39, 49, 59, 69, 79, 89, 97, 98, 96, 95, 94, 93, 92, 91]) == 85
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 8
    assert candidate(nums = [1234, 4321, 5678, 8765, 9012]) == 6
    assert candidate(nums = [1234, 4321, 5678, 8765, 9876]) == 6
    assert candidate(nums = [101, 203, 305, 407, 509]) == 9
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432]) == 6
    assert candidate(nums = [234, 345, 456, 567, 678, 789, 890, 901]) == 16
    assert candidate(nums = [13, 31, 37, 73, 79, 97]) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 76
    assert candidate(nums = [9876, 6543, 3210, 9870]) == 0
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 27
    assert candidate(nums = [123, 321, 456, 654, 789, 987, 246, 642]) == 16
    assert candidate(nums = [1009, 2008, 3007, 4006, 5005]) == 8
    assert candidate(nums = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]) == 59
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098]) == 19
    assert candidate(nums = [89, 97, 75, 53, 31, 19, 98, 87]) == 23
    assert candidate(nums = [113, 224, 335, 446, 557]) == 8
    assert candidate(nums = [101, 234, 357, 479, 591]) == 9
    assert candidate(nums = [23, 32, 45, 54, 67, 76, 89, 98, 10]) == 15
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 27
    assert candidate(nums = [1111, 2223, 3335, 4447]) == 6
    assert candidate(nums = [1234, 5678, 9101, 1121, 2132, 3143]) == 14
    assert candidate(nums = [13579, 24680, 97531, 86420, 1029384756]) == 5
    assert candidate(nums = [911, 822, 733, 644, 555, 466]) == 10
    assert candidate(nums = [13579, 2468, 97531, 86420, 7539, 6428, 5317, 4206]) == 18
    assert candidate(nums = [9876, 5432, 3210, 1098, 7654]) == 8
    assert candidate(nums = [19, 28, 37, 46, 55, 64, 73, 82, 91]) == 27
    assert candidate(nums = [89, 97, 103, 107, 109]) == 8
    assert candidate(nums = [111, 222, 333, 444, 555, 666]) == 11
    assert candidate(nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]) == 27
    assert candidate(nums = [111222, 222333, 333444, 444555, 555666, 666777, 777888, 888999, 999111]) == 27
    assert candidate(nums = [101, 202, 303, 404, 505]) == 9
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 27
    assert candidate(nums = [12, 24, 36, 48, 60, 72, 84, 96]) == 12
    assert candidate(nums = [12345, 67890, 54321, 90876, 23456]) == 7
    assert candidate(nums = [11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999]) == 27
    assert candidate(nums = [987, 654, 321, 123, 456, 789]) == 6
    assert candidate(nums = [9998, 7775, 5552, 3337, 1111]) == 9
    assert candidate(nums = [1023, 4567, 8910, 1123]) == 5


