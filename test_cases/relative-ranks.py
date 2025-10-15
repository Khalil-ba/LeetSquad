def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(score = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [0, 1000000]) == ['Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [0, 1000000]) == ['Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 90, 95, 80, 75]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 90, 95, 80, 75]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [10, 3, 8, 9, 4]) == ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [10, 3, 8, 9, 4]) == ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100]) == ['Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100]) == ['Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [40, 10, 30, 20]) == ['Gold Medal', '4', 'Silver Medal', 'Bronze Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [40, 10, 30, 20]) == ['Gold Medal', '4', 'Silver Medal', 'Bronze Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [42]) == ['Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [42]) == ['Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [20, 10, 30, 50, 40]) == ['4', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [20, 10, 30, 50, 40]) == ['4', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [40, 10, 20, 30]) == ['Gold Medal', '4', 'Bronze Medal', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [40, 10, 20, 30]) == ['Gold Medal', '4', 'Bronze Medal', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [33, 27, 22, 15, 6]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [33, 27, 22, 15, 6]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1]) == ['Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1]) == ['Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 2, 3, 4, 5]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 2, 3, 4, 5]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5, 20, 15, 10, 25]) == ['5', 'Silver Medal', 'Bronze Medal', '4', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5, 20, 15, 10, 25]) == ['5', 'Silver Medal', 'Bronze Medal', '4', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [3, 1, 2]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [3, 1, 2]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == ['13', '15', '14', '11', '12', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == ['13', '15', '14', '11', '12', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [34, 7, 23, 32, 5, 62]) == ['Silver Medal', '5', '4', 'Bronze Medal', '6', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [34, 7, 23, 32, 5, 62]) == ['Silver Medal', '5', '4', 'Bronze Medal', '6', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']: {e}')
    
    total += 1
    try:
        result = candidate(score = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [50, 20, 30, 10, 40, 60]) == ['Silver Medal', '5', '4', '6', 'Bronze Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [50, 20, 30, 10, 40, 60]) == ['Silver Medal', '5', '4', '6', 'Bronze Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000000, 999999, 999998, 999997, 999996]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000000, 999999, 999998, 999997, 999996]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [789, 654, 321, 987, 456, 123, 890, 567, 234]) == ['Bronze Medal', '4', '7', 'Gold Medal', '6', '9', 'Silver Medal', '5', '8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [789, 654, 321, 987, 456, 123, 890, 567, 234]) == ['Bronze Medal', '4', '7', 'Gold Medal', '6', '9', 'Silver Medal', '5', '8']: {e}')
    
    total += 1
    try:
        result = candidate(score = [12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 90, 95, 85, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5', '6', '7', '8', '9', '10', '11']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 90, 95, 85, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5', '6', '7', '8', '9', '10', '11']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [23, 34, 12, 45, 56, 78, 89, 90, 101, 112, 134, 145, 156, 167, 178]) == ['14', '13', '15', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [23, 34, 12, 45, 56, 78, 89, 90, 101, 112, 134, 145, 156, 167, 178]) == ['14', '13', '15', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [8, 6, 7, 5, 3, 0, 9, 10, 12, 14, 13, 11, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30]) == ['23', '25', '24', '26', '27', '28', '22', '21', '19', '17', '18', '20', '16', '14', '15', '13', '11', '12', '10', '8', '9', '7', '5', '6', '4', 'Silver Medal', 'Bronze Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [8, 6, 7, 5, 3, 0, 9, 10, 12, 14, 13, 11, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30]) == ['23', '25', '24', '26', '27', '28', '22', '21', '19', '17', '18', '20', '16', '14', '15', '13', '11', '12', '10', '8', '9', '7', '5', '6', '4', 'Silver Medal', 'Bronze Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [33, 11, 44, 22, 55, 66, 77, 88, 99, 100]) == ['8', '10', '7', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [33, 11, 44, 22, 55, 66, 77, 88, 99, 100]) == ['8', '10', '7', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == ['100', '99', '98', '97', '96', '95', '94', '93', '92', '91', '90', '89', '88', '87', '86', '85', '84', '83', '82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71', '70', '69', '68', '67', '66', '65', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == ['100', '99', '98', '97', '96', '95', '94', '93', '92', '91', '90', '89', '88', '87', '86', '85', '84', '83', '82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71', '70', '69', '68', '67', '66', '65', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [3456, 1234, 7890, 4567, 8901, 2345, 5678]) == ['5', '7', 'Silver Medal', '4', 'Gold Medal', '6', 'Bronze Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [3456, 1234, 7890, 4567, 8901, 2345, 5678]) == ['5', '7', 'Silver Medal', '4', 'Gold Medal', '6', 'Bronze Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [54321, 65432, 76543, 87654, 98765, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [54321, 65432, 76543, 87654, 98765, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45']: {e}')
    
    total += 1
    try:
        result = candidate(score = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 99999, 9999, 999, 99, 9]) == ['13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 99999, 9999, 999, 99, 9]) == ['13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100000, 1, 10000, 1000, 100, 10, 0]) == ['Gold Medal', '6', 'Silver Medal', 'Bronze Medal', '4', '5', '7']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100000, 1, 10000, 1000, 100, 10, 0]) == ['Gold Medal', '6', 'Silver Medal', 'Bronze Medal', '4', '5', '7']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5, 20, 15, 10, 25, 30, 35, 40, 45, 50]) == ['10', '7', '8', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5, 20, 15, 10, 25, 30, 35, 40, 45, 50]) == ['10', '7', '8', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [42, 23, 35, 56, 78, 89, 12, 34, 56, 78, 90, 101, 112, 134, 145]) == ['11', '14', '12', '9', '7', '6', '15', '13', '10', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [42, 23, 35, 56, 78, 89, 12, 34, 56, 78, 90, 101, 112, 134, 145]) == ['11', '14', '12', '9', '7', '6', '15', '13', '10', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000000, 0, 500000, 250000, 750000, 125000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000000, 0, 500000, 250000, 750000, 125000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [23, 15, 45, 67, 89, 12, 34]) == ['5', '6', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '7', '4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [23, 15, 45, 67, 89, 12, 34]) == ['5', '6', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '7', '4']: {e}')
    
    total += 1
    try:
        result = candidate(score = [999, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009, 100010]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [999, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009, 100010]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [99, 34, 23, 44, 55, 12, 67, 89, 100]) == ['Silver Medal', '7', '8', '6', '5', '9', '4', 'Bronze Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [99, 34, 23, 44, 55, 12, 67, 89, 100]) == ['Silver Medal', '7', '8', '6', '5', '9', '4', 'Bronze Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5, 999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]) == ['9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5, 999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]) == ['9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 1000, 10, 100, 10000]) == ['5', 'Silver Medal', '4', 'Bronze Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 1000, 10, 100, 10000]) == ['5', 'Silver Medal', '4', 'Bronze Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [88, 77, 66, 55, 44, 33, 22, 11]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [88, 77, 66, 55, 44, 33, 22, 11]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']: {e}')
    
    total += 1
    try:
        result = candidate(score = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == ['7', '10', '6', '11', 'Bronze Medal', 'Gold Medal', '9', 'Silver Medal', '4', '8', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == ['7', '10', '6', '11', 'Bronze Medal', 'Gold Medal', '9', 'Silver Medal', '4', '8', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [30, 40, 20, 10, 50, 60, 70, 80, 90, 100]) == ['8', '7', '9', '10', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [30, 40, 20, 10, 50, 60, 70, 80, 90, 100]) == ['8', '7', '9', '10', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [5]) == ['Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [5]) == ['Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == ['11', '7', 'Bronze Medal', '12', '10', '9', '8', '6', '5', '4', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == ['11', '7', 'Bronze Medal', '12', '10', '9', '8', '6', '5', '4', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [85, 67, 92, 78, 99, 56, 88, 77, 100, 95]) == ['6', '9', '4', '7', 'Silver Medal', '10', '5', '8', 'Gold Medal', 'Bronze Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [85, 67, 92, 78, 99, 56, 88, 77, 100, 95]) == ['6', '9', '4', '7', 'Silver Medal', '10', '5', '8', 'Gold Medal', 'Bronze Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [23, 45, 12, 67, 34, 89, 90, 11, 2, 3, 5, 7, 9, 13, 15, 17, 19, 21, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == ['42', '30', '48', '19', '36', '7', '6', '49', '54', '53', '52', '51', '50', '47', '46', '45', '44', '43', '41', '40', '39', '38', '37', '35', '34', '33', '32', '31', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [23, 45, 12, 67, 34, 89, 90, 11, 2, 3, 5, 7, 9, 13, 15, 17, 19, 21, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == ['42', '30', '48', '19', '36', '7', '6', '49', '54', '53', '52', '51', '50', '47', '46', '45', '44', '43', '41', '40', '39', '38', '37', '35', '34', '33', '32', '31', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [88, 1, 56, 91, 67, 29, 42, 74, 35, 81, 100, 23, 64, 50, 79, 38, 95, 47, 61, 85]) == ['4', '20', '12', 'Bronze Medal', '9', '18', '15', '8', '17', '6', 'Gold Medal', '19', '10', '13', '7', '16', 'Silver Medal', '14', '11', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [88, 1, 56, 91, 67, 29, 42, 74, 35, 81, 100, 23, 64, 50, 79, 38, 95, 47, 61, 85]) == ['4', '20', '12', 'Bronze Medal', '9', '18', '15', '8', '17', '6', 'Gold Medal', '19', '10', '13', '7', '16', 'Silver Medal', '14', '11', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 1000000, 500000, 250000, 750000, 100000, 600000, 300000, 800000, 400000, 900000]) == ['11', 'Gold Medal', '6', '9', '4', '10', '5', '8', 'Bronze Medal', '7', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 1000000, 500000, 250000, 750000, 100000, 600000, 300000, 800000, 400000, 900000]) == ['11', 'Gold Medal', '6', '9', '4', '10', '5', '8', 'Bronze Medal', '7', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 10000, 1000, 100, 10, 100000, 1000000]) == ['7', 'Bronze Medal', '4', '5', '6', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 10000, 1000, 100, 10, 100000, 1000000]) == ['7', 'Bronze Medal', '4', '5', '6', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 100, 1000, 10000, 100000]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 100, 1000, 10000, 100000]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9]) == ['19', '17', '15', '13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12', '14', '16', '18']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9]) == ['19', '17', '15', '13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12', '14', '16', '18']: {e}')
    
    total += 1
    try:
        result = candidate(score = [8, 1, 3, 7, 4, 6, 5, 2]) == ['Gold Medal', '8', '6', 'Silver Medal', '5', 'Bronze Medal', '4', '7']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [8, 1, 3, 7, 4, 6, 5, 2]) == ['Gold Medal', '8', '6', 'Silver Medal', '5', 'Bronze Medal', '4', '7']: {e}')
    
    total += 1
    try:
        result = candidate(score = [78, 56, 34, 12, 90, 67, 45, 23, 89, 10]) == ['Bronze Medal', '5', '7', '9', 'Gold Medal', '4', '6', '8', 'Silver Medal', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [78, 56, 34, 12, 90, 67, 45, 23, 89, 10]) == ['Bronze Medal', '5', '7', '9', 'Gold Medal', '4', '6', '8', 'Silver Medal', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [9, 3, 15, 12, 6, 24, 18, 30, 27, 21]) == ['8', '10', '6', '7', '9', 'Bronze Medal', '5', 'Gold Medal', 'Silver Medal', '4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [9, 3, 15, 12, 6, 24, 18, 30, 27, 21]) == ['8', '10', '6', '7', '9', 'Bronze Medal', '5', 'Gold Medal', 'Silver Medal', '4']: {e}')
    
    total += 1
    try:
        result = candidate(score = [7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']: {e}')
    
    total += 1
    try:
        result = candidate(score = [87, 68, 94, 78, 85, 91, 89, 76, 82, 93]) == ['5', '10', 'Gold Medal', '8', '6', 'Bronze Medal', '4', '9', '7', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [87, 68, 94, 78, 85, 91, 89, 76, 82, 93]) == ['5', '10', 'Gold Medal', '8', '6', 'Bronze Medal', '4', '9', '7', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050]) == ['21', '19', '20', '17', '18', '15', '16', '13', '14', '11', '12', '9', '10', '7', '8', '5', '6', 'Bronze Medal', '4', 'Gold Medal', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050]) == ['21', '19', '20', '17', '18', '15', '16', '13', '14', '11', '12', '9', '10', '7', '8', '5', '6', 'Bronze Medal', '4', 'Gold Medal', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']: {e}')
    
    total += 1
    try:
        result = candidate(score = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']: {e}')
    
    total += 1
    try:
        result = candidate(score = [999999, 0, 500000, 250000, 750000, 100000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [999999, 0, 500000, 250000, 750000, 100000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [987, 654, 321, 123, 456, 789, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == ['Silver Medal', '7', '12', '14', '9', '4', '15', '13', '11', '10', '8', '6', '5', 'Bronze Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [987, 654, 321, 123, 456, 789, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == ['Silver Medal', '7', '12', '14', '9', '4', '15', '13', '11', '10', '8', '6', '5', 'Bronze Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000]) == ['50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000]) == ['50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [50, 20, 30, 10, 40]) == ['Gold Medal', '4', 'Bronze Medal', '5', 'Silver Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [50, 20, 30, 10, 40]) == ['Gold Medal', '4', 'Bronze Medal', '5', 'Silver Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']: {e}')
    
    total += 1
    try:
        result = candidate(score = [42, 24, 66, 100, 35, 90, 28, 72, 55, 88]) == ['7', '10', '5', 'Gold Medal', '8', 'Silver Medal', '9', '4', '6', 'Bronze Medal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(score = [42, 24, 66, 100, 35, 90, 28, 72, 55, 88]) == ['7', '10', '5', 'Gold Medal', '8', 'Silver Medal', '9', '4', '6', 'Bronze Medal']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(score = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
    assert candidate(score = [0, 1000000]) == ['Silver Medal', 'Gold Medal']
    assert candidate(score = [100, 90, 95, 80, 75]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5']
    assert candidate(score = [10, 3, 8, 9, 4]) == ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
    assert candidate(score = [100]) == ['Gold Medal']
    assert candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [40, 10, 30, 20]) == ['Gold Medal', '4', 'Silver Medal', 'Bronze Medal']
    assert candidate(score = [42]) == ['Gold Medal']
    assert candidate(score = [20, 10, 30, 50, 40]) == ['4', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal']
    assert candidate(score = [40, 10, 20, 30]) == ['Gold Medal', '4', 'Bronze Medal', 'Silver Medal']
    assert candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']
    assert candidate(score = [33, 27, 22, 15, 6]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
    assert candidate(score = [1]) == ['Gold Medal']
    assert candidate(score = [1, 2, 3, 4, 5]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [5, 20, 15, 10, 25]) == ['5', 'Silver Medal', 'Bronze Medal', '4', 'Gold Medal']
    assert candidate(score = [3, 1, 2]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal']
    assert candidate(score = [3, 1, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == ['13', '15', '14', '11', '12', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [34, 7, 23, 32, 5, 62]) == ['Silver Medal', '5', '4', 'Bronze Medal', '6', 'Gold Medal']
    assert candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    assert candidate(score = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [50, 20, 30, 10, 40, 60]) == ['Silver Medal', '5', '4', '6', 'Bronze Medal', 'Gold Medal']
    assert candidate(score = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
    assert candidate(score = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1000000, 999999, 999998, 999997, 999996]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
    assert candidate(score = [789, 654, 321, 987, 456, 123, 890, 567, 234]) == ['Bronze Medal', '4', '7', 'Gold Medal', '6', '9', 'Silver Medal', '5', '8']
    assert candidate(score = [12345, 12346, 12347, 12348, 12349, 12350, 12351, 12352, 12353, 12354]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [100, 90, 95, 85, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Bronze Medal', 'Silver Medal', '4', '5', '6', '7', '8', '9', '10', '11']
    assert candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [23, 34, 12, 45, 56, 78, 89, 90, 101, 112, 134, 145, 156, 167, 178]) == ['14', '13', '15', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [8, 6, 7, 5, 3, 0, 9, 10, 12, 14, 13, 11, 15, 17, 16, 18, 20, 19, 21, 23, 22, 24, 26, 25, 27, 29, 28, 30]) == ['23', '25', '24', '26', '27', '28', '22', '21', '19', '17', '18', '20', '16', '14', '15', '13', '11', '12', '10', '8', '9', '7', '5', '6', '4', 'Silver Medal', 'Bronze Medal', 'Gold Medal']
    assert candidate(score = [33, 11, 44, 22, 55, 66, 77, 88, 99, 100]) == ['8', '10', '7', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == ['100', '99', '98', '97', '96', '95', '94', '93', '92', '91', '90', '89', '88', '87', '86', '85', '84', '83', '82', '81', '80', '79', '78', '77', '76', '75', '74', '73', '72', '71', '70', '69', '68', '67', '66', '65', '64', '63', '62', '61', '60', '59', '58', '57', '56', '55', '54', '53', '52', '51', '50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [3456, 1234, 7890, 4567, 8901, 2345, 5678]) == ['5', '7', 'Silver Medal', '4', 'Gold Medal', '6', 'Bronze Medal']
    assert candidate(score = [54321, 65432, 76543, 87654, 98765, 43210, 32109, 21098, 10987, 9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098, 987, 876, 765, 654, 543, 432, 321, 210, 109, 98, 87, 76, 65, 54, 43, 32, 21, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45']
    assert candidate(score = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 999999, 99999, 9999, 999, 99, 9]) == ['13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12']
    assert candidate(score = [100000, 1, 10000, 1000, 100, 10, 0]) == ['Gold Medal', '6', 'Silver Medal', 'Bronze Medal', '4', '5', '7']
    assert candidate(score = [5, 20, 15, 10, 25, 30, 35, 40, 45, 50]) == ['10', '7', '8', '9', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [42, 23, 35, 56, 78, 89, 12, 34, 56, 78, 90, 101, 112, 134, 145]) == ['11', '14', '12', '9', '7', '6', '15', '13', '10', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1000000, 999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']
    assert candidate(score = [1000000, 0, 500000, 250000, 750000, 125000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']
    assert candidate(score = [23, 15, 45, 67, 89, 12, 34]) == ['5', '6', 'Bronze Medal', 'Silver Medal', 'Gold Medal', '7', '4']
    assert candidate(score = [999, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 100000, 100001, 100002, 100003, 100004, 100005, 100006, 100007, 100008, 100009, 100010]) == ['30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [99, 34, 23, 44, 55, 12, 67, 89, 100]) == ['Silver Medal', '7', '8', '6', '5', '9', '4', 'Bronze Medal', 'Gold Medal']
    assert candidate(score = [300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    assert candidate(score = [5, 999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]) == ['9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1, 1000, 10, 100, 10000]) == ['5', 'Silver Medal', '4', 'Bronze Medal', 'Gold Medal']
    assert candidate(score = [88, 77, 66, 55, 44, 33, 22, 11]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']
    assert candidate(score = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == ['7', '10', '6', '11', 'Bronze Medal', 'Gold Medal', '9', 'Silver Medal', '4', '8', '5']
    assert candidate(score = [30, 40, 20, 10, 50, 60, 70, 80, 90, 100]) == ['8', '7', '9', '10', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [5]) == ['Gold Medal']
    assert candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == ['11', '7', 'Bronze Medal', '12', '10', '9', '8', '6', '5', '4', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [85, 67, 92, 78, 99, 56, 88, 77, 100, 95]) == ['6', '9', '4', '7', 'Silver Medal', '10', '5', '8', 'Gold Medal', 'Bronze Medal']
    assert candidate(score = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [23, 45, 12, 67, 34, 89, 90, 11, 2, 3, 5, 7, 9, 13, 15, 17, 19, 21, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == ['42', '30', '48', '19', '36', '7', '6', '49', '54', '53', '52', '51', '50', '47', '46', '45', '44', '43', '41', '40', '39', '38', '37', '35', '34', '33', '32', '31', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1000000, 0, 500000, 250000, 750000]) == ['Gold Medal', '5', 'Bronze Medal', '4', 'Silver Medal']
    assert candidate(score = [88, 1, 56, 91, 67, 29, 42, 74, 35, 81, 100, 23, 64, 50, 79, 38, 95, 47, 61, 85]) == ['4', '20', '12', 'Bronze Medal', '9', '18', '15', '8', '17', '6', 'Gold Medal', '19', '10', '13', '7', '16', 'Silver Medal', '14', '11', '5']
    assert candidate(score = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [1, 1000000, 500000, 250000, 750000, 100000, 600000, 300000, 800000, 400000, 900000]) == ['11', 'Gold Medal', '6', '9', '4', '10', '5', '8', 'Bronze Medal', '7', 'Silver Medal']
    assert candidate(score = [1, 10000, 1000, 100, 10, 100000, 1000000]) == ['7', 'Bronze Medal', '4', '5', '6', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1, 100, 1000, 10000, 100000]) == ['5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9]) == ['19', '17', '15', '13', '11', '9', '7', '5', 'Bronze Medal', 'Gold Medal', 'Silver Medal', '4', '6', '8', '10', '12', '14', '16', '18']
    assert candidate(score = [8, 1, 3, 7, 4, 6, 5, 2]) == ['Gold Medal', '8', '6', 'Silver Medal', '5', 'Bronze Medal', '4', '7']
    assert candidate(score = [78, 56, 34, 12, 90, 67, 45, 23, 89, 10]) == ['Bronze Medal', '5', '7', '9', 'Gold Medal', '4', '6', '8', 'Silver Medal', '10']
    assert candidate(score = [9, 3, 15, 12, 6, 24, 18, 30, 27, 21]) == ['8', '10', '6', '7', '9', 'Bronze Medal', '5', 'Gold Medal', 'Silver Medal', '4']
    assert candidate(score = [7, 6, 5, 4, 3, 2, 1, 0]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8']
    assert candidate(score = [87, 68, 94, 78, 85, 91, 89, 76, 82, 93]) == ['5', '10', 'Gold Medal', '8', '6', 'Bronze Medal', '4', '9', '7', 'Silver Medal']
    assert candidate(score = [100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550, 700, 650, 800, 750, 900, 850, 1000, 950, 1100, 1050]) == ['21', '19', '20', '17', '18', '15', '16', '13', '14', '11', '12', '9', '10', '7', '8', '5', '6', 'Bronze Medal', '4', 'Gold Medal', 'Silver Medal']
    assert candidate(score = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10']
    assert candidate(score = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    assert candidate(score = [999999, 0, 500000, 250000, 750000, 100000]) == ['Gold Medal', '6', 'Bronze Medal', '4', 'Silver Medal', '5']
    assert candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == ['10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [987, 654, 321, 123, 456, 789, 111, 222, 333, 444, 555, 666, 777, 888, 999]) == ['Silver Medal', '7', '12', '14', '9', '4', '15', '13', '11', '10', '8', '6', '5', 'Bronze Medal', 'Gold Medal']
    assert candidate(score = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000, 48000, 49000, 50000]) == ['50', '49', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [50, 20, 30, 10, 40]) == ['Gold Medal', '4', 'Bronze Medal', '5', 'Silver Medal']
    assert candidate(score = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == ['15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', 'Bronze Medal', 'Silver Medal', 'Gold Medal']
    assert candidate(score = [42, 24, 66, 100, 35, 90, 28, 72, 55, 88]) == ['7', '10', '5', 'Gold Medal', '8', 'Silver Medal', '9', '4', '6', 'Bronze Medal']


