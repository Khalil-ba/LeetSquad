def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1]) == "1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1]) == "1": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 30, 34, 5, 9]) == "9534330"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 30, 34, 5, 9]) == "9534330": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2]) == "210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2]) == "210": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111311, 1113]) == "1113111311"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111311, 1113]) == "1113111311": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000]) == "101001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000]) == "101001000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999]) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999]) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 30, 34, 5, 9, 10]) == "953433010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 30, 34, 5, 9, 10]) == "953433010": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50]) == "5040302010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50]) == "5040302010": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(nums = [34323, 3432]) == "343234323"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34323, 3432]) == "343234323": {e}')
    
    total += 1
    try:
        result = candidate(nums = [121, 12]) == "12121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [121, 12]) == "12121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1]) == "110100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1]) == "110100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == "1101001000100001000001000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == "1101001000100001000001000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 1212, 12121]) == "12121212121121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 1212, 12121]) == "12121212121121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 1234, 123, 12, 1]) == "123451234123121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 1234, 123, 12, 1]) == "123451234123121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [233, 23, 2]) == "233232"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [233, 23, 2]) == "233232": {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 111, 1111, 11111]) == "11111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 111, 1111, 11111]) == "11111111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 12, 121, 1212, 1]) == "1231212121211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 12, 121, 1212, 1]) == "1231212121211": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 12121, 1212]) == "12121212121121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 12121, 1212]) == "12121212121121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 3, 333, 3333]) == "3333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 3, 333, 3333]) == "3333333333": {e}')
    
    total += 1
    try:
        result = candidate(nums = [82, 828, 8282, 82828]) == "82882828828282"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [82, 828, 8282, 82828]) == "82882828828282": {e}')
    
    total += 1
    try:
        result = candidate(nums = [233, 23, 2333]) == "233323323"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [233, 23, 2333]) == "233323323": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99989796959493929190"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99989796959493929190": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 3, 34, 5, 9, 31]) == "953433130"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 3, 34, 5, 9, 31]) == "953433130": {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 565, 5656, 56565]) == "56565656565565"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 565, 5656, 56565]) == "56565656565565": {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 212, 2121]) == "212212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 212, 2121]) == "212212121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == "110100100010000100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == "110100100010000100000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 1211]) == "121211211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 1211]) == "121211211": {e}')
    
    total += 1
    try:
        result = candidate(nums = [34323, 3432, 343, 34]) == "34343343234323"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34323, 3432, 343, 34]) == "34343343234323": {e}')
    
    total += 1
    try:
        result = candidate(nums = [830, 8308]) == "8308830"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [830, 8308]) == "8308830": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 10000, 100, 1]) == "1100100001000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 10000, 100, 1]) == "1100100001000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 98, 9, 9876]) == "9989879876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 98, 9, 9876]) == "9989879876": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 30, 34, 5, 9, 300, 303]) == "9534330330300"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 30, 34, 5, 9, 300, 303]) == "9534330330300": {e}')
    
    total += 1
    try:
        result = candidate(nums = [830, 83, 83083]) == "8383083830"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [830, 83, 83083]) == "8383083830": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1]) == "1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1]) == "1000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 99, 9, 100, 10]) == "99999910100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 99, 9, 100, 10]) == "99999910100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000]) == "10100100010000100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000]) == "10100100010000100000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 21, 121, 122, 212, 211]) == "2122121112212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 21, 121, 122, 212, 211]) == "2122121112212121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 900, 9000, 90000, 900000, 9000000, 90000000]) == "90900900090000900000900000090000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 900, 9000, 90000, 900000, 9000000, 90000000]) == "90900900090000900000900000090000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [34323, 3432]) == "343234323"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34323, 3432]) == "343234323": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1]) == "1101001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1]) == "1101001000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == "1000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == "1000000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 454, 4545, 45454]) == "45454545454454"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 454, 4545, 45454]) == "45454545454454": {e}')
    
    total += 1
    try:
        result = candidate(nums = [839, 8399, 83998, 83983]) == "83998839983983983"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [839, 8399, 83998, 83983]) == "83998839983983983": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(nums = [789, 7897, 78978, 789789, 7897897, 78978978]) == "789789789789789787897897789787897"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [789, 7897, 78978, 789789, 7897897, 78978978]) == "789789789789789787897897789787897": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 333, 3333, 33333]) == "33333333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 333, 3333, 33333]) == "33333333333333": {e}')
    
    total += 1
    try:
        result = candidate(nums = [830, 83, 834, 835, 832]) == "83835834832830"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [830, 83, 834, 835, 832]) == "83835834832830": {e}')
    
    total += 1
    try:
        result = candidate(nums = [55, 555, 5, 5555, 55555]) == "555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [55, 555, 5, 5555, 55555]) == "555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 1]) == "10000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 1]) == "10000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 111, 1111, 11111, 111111, 1111111]) == "111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 111, 1111, 11111, 111111, 1111111]) == "111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 10, 1, 100]) == "110110100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 10, 1, 100]) == "110110100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 22, 222, 2222, 22222, 222222, 2222222, 22222222]) == "222222222222222222222222222222222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 22, 222, 2222, 22222, 222222, 2222222, 22222222]) == "222222222222222222222222222222222222": {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 98, 9, 999, 99, 998, 9989]) == "999999998999898987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 98, 9, 999, 99, 998, 9989]) == "999999998999898987": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 1213, 12131]) == "12131213112121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 1213, 12131]) == "12131213112121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111311, 1113, 11113, 11131, 111]) == "11131113111131111113111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111311, 1113, 11113, 11131, 111]) == "11131113111131111113111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111111111, 111111111, 11111111, 1111111, 111111, 11111, 1111, 111, 11, 1]) == "1111111111111111111111111111111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111111111, 111111111, 11111111, 1111111, 111111, 11111, 1111, 111, 11, 1]) == "1111111111111111111111111111111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1000, 10, 1]) == "1101001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1000, 10, 1]) == "1101001000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 55, 555, 5555, 55555]) == "555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 55, 555, 5555, 55555]) == "555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777": {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654321, 98765432, 9876543, 987654, 98765, 9876, 987, 98, 9]) == "998987987698765987654987654398765432987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654321, 98765432, 9876543, 987654, 98765, 9876, 987, 98, 9]) == "998987987698765987654987654398765432987654321": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1]) == "1000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1]) == "1000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == "999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == "999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 12121, 1212, 1]) == "121212121211211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 12121, 1212, 1]) == "121212121211211": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777]) == "7777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777]) == "7777777777": {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 212, 2121, 211]) == "212212121211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 212, 2121, 211]) == "212212121211": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 999, 99, 9]) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 999, 99, 9]) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 343, 3434]) == "343434343"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 343, 3434]) == "343434343": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 70, 707, 77, 700]) == "77770770700"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 70, 707, 77, 700]) == "77770770700": {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 1234, 12345, 123456]) == "123456123451234123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 1234, 12345, 123456]) == "123456123451234123": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 9999, 99999]) == "999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 9999, 99999]) == "999999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111, 111, 11, 1]) == "1111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111, 111, 11, 1]) == "1111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 34, 3, 98, 9, 76, 45, 6]) == "998766453431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 34, 3, 98, 9, 76, 45, 6]) == "998766453431": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 98, 989, 9898]) == "9989989898"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 98, 989, 9898]) == "9989989898": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 9, 999, 9999]) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 9, 999, 9999]) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [300, 30, 3]) == "330300"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [300, 30, 3]) == "330300": {e}')
    
    total += 1
    try:
        result = candidate(nums = [987, 98, 9]) == "998987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987, 98, 9]) == "998987": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 89, 898, 8989, 89898, 898989]) == "898989898989898988988"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 89, 898, 8989, 89898, 898989]) == "898989898989898988988": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 101, 1011, 10111]) == "10111101110110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 101, 1011, 10111]) == "10111101110110": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "98765432110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "98765432110": {e}')
    
    total += 1
    try:
        result = candidate(nums = [345, 3453, 34534]) == "345345343453"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [345, 3453, 34534]) == "345345343453": {e}')
    
    total += 1
    try:
        result = candidate(nums = [555, 55, 5]) == "555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555, 55, 5]) == "555555": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121]) == "12121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121]) == "12121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 44, 444, 4444]) == "44444444440"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 44, 444, 4444]) == "44444444440": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 11, 1111, 11111, 1]) == "111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 11, 1111, 11111, 1]) == "111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 909, 9090]) == "909909090"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 909, 9090]) == "909909090": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 10, 100, 1]) == "1101001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 10, 100, 1]) == "1101001000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [67, 676, 6767, 67676, 676767, 6767676]) == "676767676767676767667676676"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [67, 676, 6767, 67676, 676767, 6767676]) == "676767676767676767667676676": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "98765432110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "98765432110": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == "7777777777777777777777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == "7777777777777777777777777777": {e}')
    
    total += 1
    try:
        result = candidate(nums = [830, 8308, 830830, 83083]) == "830883083830830830"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [830, 8308, 830830, 83083]) == "830883083830830830": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 1]) == "1101001000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 1]) == "1101001000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 23, 4, 2]) == "4232201"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 23, 4, 2]) == "4232201": {e}')
    
    total += 1
    try:
        result = candidate(nums = [78, 787, 7878, 78787]) == "78787878787787"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [78, 787, 7878, 78787]) == "78787878787787": {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 212, 2121, 21212]) == "21221212212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 212, 2121, 21212]) == "21221212212121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111311, 1113, 11, 11131111, 11111113, 11113111]) == "111311131111131111111131111111111311"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111311, 1113, 11, 11131111, 11111113, 11113111]) == "111311131111131111111131111111111311": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 50, 500, 5000, 50000, 500000, 5000000, 50000000]) == "550500500050000500000500000050000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 50, 500, 5000, 50000, 500000, 5000000, 50000000]) == "550500500050000500000500000050000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890]) == "890789678567456345234123"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890]) == "890789678567456345234123": {e}')
    
    total += 1
    try:
        result = candidate(nums = [824, 82, 8]) == "882824"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [824, 82, 8]) == "882824": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 30, 34, 5, 9, 300, 303, 33, 333]) == "953433333330330300"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 30, 34, 5, 9, 300, 303, 33, 333]) == "953433333330330300": {e}')
    
    total += 1
    try:
        result = candidate(nums = [79, 798, 797, 7987]) == "798798779797"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [79, 798, 797, 7987]) == "798798779797": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "908070605040302010100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "908070605040302010100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == "1101001000100001000001000000100000001000000001000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == "1101001000100001000001000000100000001000000001000000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 101, 1011, 10111]) == "110111101110110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 101, 1011, 10111]) == "110111101110110": {e}')
    
    total += 1
    try:
        result = candidate(nums = [88, 888, 8888, 88888, 888888, 8888888, 88888888]) == "88888888888888888888888888888888888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [88, 888, 8888, 88888, 888888, 8888888, 88888888]) == "88888888888888888888888888888888888": {e}')
    
    total += 1
    try:
        result = candidate(nums = [83, 838, 8383, 83838]) == "83883838838383"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [83, 838, 8383, 83838]) == "83883838838383": {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 200, 2000, 20000]) == "20200200020000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 200, 2000, 20000]) == "20200200020000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 0]) == "9999999999999999999999999999999999999999999990"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 0]) == "9999999999999999999999999999999999999999999990": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 303, 3003, 3]) == "3303303003"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 303, 3003, 3]) == "3303303003": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30033, 300, 3, 3003]) == "3300333003300"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30033, 300, 3, 3003]) == "3300333003300": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1000, 10000, 100000, 1]) == "1100100010000100000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1000, 10000, 100000, 1]) == "1100100010000100000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [56, 565, 566]) == "56656565"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [56, 565, 566]) == "56656565": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 66, 666, 6666, 66666, 666666, 6666666, 66666666, 666666666, 6666666666]) == "6666666666666666666666666666666666666666666666666666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 66, 666, 6666, 66666, 666666, 6666666, 66666666, 666666666, 6666666666]) == "6666666666666666666666666666666666666666666666666666666": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 11, 1]) == "111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 11, 1]) == "111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 1231, 12312, 12, 121, 1212]) == "123123121231121212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 1231, 12312, 12, 121, 1212]) == "123123121231121212121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 1211, 12111]) == "12121121112111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 1211, 12111]) == "12121121112111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [432, 4324, 43, 43243, 4]) == "443432443243432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [432, 4324, 43, 43243, 4]) == "443432443243432": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 11, 1, 1111]) == "1111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 11, 1, 1111]) == "1111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 330, 3330, 333]) == "333333330330"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 330, 3330, 333]) == "333333330330": {e}')
    
    total += 1
    try:
        result = candidate(nums = [824, 8247]) == "8248247"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [824, 8247]) == "8248247": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999]) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999]) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 1, 1, 1, 0]) == "1110000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 1, 1, 1, 0]) == "1110000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 23, 4, 25]) == "42523201"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 23, 4, 25]) == "42523201": {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "8642018161412100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "8642018161412100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [21, 212, 2121, 21212]) == "21221212212121"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [21, 212, 2121, 21212]) == "21221212212121": {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 44, 444, 4444, 44444, 444444, 4444444, 44444444]) == "444444444444444444444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 44, 444, 4444, 44444, 444444, 4444444, 44444444]) == "444444444444444444444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111311, 1113, 11, 1111, 1]) == "11131113111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111311, 1113, 11, 1111, 1]) == "11131113111111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1, 101, 110, 111, 11, 1001]) == "111111110101101001100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1, 101, 110, 111, 11, 1001]) == "111111110101101001100": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 34, 3, 98, 9, 76, 45, 67]) == "9987667453431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 34, 3, 98, 9, 76, 45, 67]) == "9987667453431": {e}')
    
    total += 1
    try:
        result = candidate(nums = [54, 546, 548, 60]) == "6054854654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [54, 546, 548, 60]) == "6054854654": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 333, 3333, 33333, 3]) == "333333333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 333, 3333, 33333, 3]) == "333333333333333": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == "1101001000100001000001000000100000001000000001000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == "1101001000100001000001000000100000001000000001000000000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000]) == "10100100010000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000]) == "10100100010000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 1]) == "9999999999999999999999999999999999999999999991"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 1]) == "9999999999999999999999999999999999999999999991": {e}')
    
    total += 1
    try:
        result = candidate(nums = [66, 666, 6666, 66666, 666666, 6666666, 66666666]) == "66666666666666666666666666666666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [66, 666, 6666, 66666, 666666, 6666666, 66666666]) == "66666666666666666666666666666666666": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000]) == "110100100010000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000]) == "110100100010000": {e}')
    
    total += 1
    try:
        result = candidate(nums = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 6828, 5662, 6699, 10, 7896, 8626, 3462, 2000, 7988, 626, 6670, 4224, 2996]) == "9609938862682479887896697368286699667062657035662560743984224346229962000139910"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 6828, 5662, 6699, 10, 7896, 8626, 3462, 2000, 7988, 626, 6670, 4224, 2996]) == "9609938862682479887896697368286699667062657035662560743984224346229962000139910": {e}')
    
    total += 1
    try:
        result = candidate(nums = [233, 322, 32]) == "32322233"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [233, 322, 32]) == "32322233": {e}')
    
    total += 1
    try:
        result = candidate(nums = [32, 323, 3232, 32323]) == "32332323323232"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [32, 323, 3232, 32323]) == "32332323323232": {e}')
    
    total += 1
    try:
        result = candidate(nums = [647, 64, 646, 6476]) == "647664764664"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [647, 64, 646, 6476]) == "647664764664": {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 11, 1]) == "111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 11, 1]) == "111111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 20, 200, 2000, 20000]) == "202002000200001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 20, 200, 2000, 20000]) == "202002000200001": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 121, 1211, 12111, 121111, 1]) == "121211211121111211111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 121, 1211, 12111, 121111, 1]) == "121211211121111211111": {e}')
    
    total += 1
    try:
        result = candidate(nums = [333, 33, 3]) == "333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [333, 33, 3]) == "333333": {e}')
    
    total += 1
    try:
        result = candidate(nums = [824, 8247]) == "8248247"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [824, 8247]) == "8248247": {e}')
    
    total += 1
    try:
        result = candidate(nums = [35, 353, 3535, 35353, 353535, 3535353, 35353535]) == "35353535353535353535353535335353353"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [35, 353, 3535, 35353, 353535, 3535353, 35353535]) == "35353535353535353535353535335353353": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [0, 0]) == "0"
    assert candidate(nums = [1]) == "1"
    assert candidate(nums = [3, 30, 34, 5, 9]) == "9534330"
    assert candidate(nums = [10, 2]) == "210"
    assert candidate(nums = [111311, 1113]) == "1113111311"
    assert candidate(nums = [10, 100, 1000]) == "101001000"
    assert candidate(nums = [9, 99, 999, 9999]) == "9999999999"
    assert candidate(nums = [3, 30, 34, 5, 9, 10]) == "953433010"
    assert candidate(nums = [10, 20, 30, 40, 50]) == "5040302010"
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210"
    assert candidate(nums = [34323, 3432]) == "343234323"
    assert candidate(nums = [121, 12]) == "12121"
    assert candidate(nums = [100, 10, 1]) == "110100"
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000]) == "1101001000100001000001000000"
    assert candidate(nums = [12, 121, 1212, 12121]) == "12121212121121"
    assert candidate(nums = [12345, 1234, 123, 12, 1]) == "123451234123121"
    assert candidate(nums = [233, 23, 2]) == "233232"
    assert candidate(nums = [11, 111, 1111, 11111]) == "11111111111111"
    assert candidate(nums = [123, 12, 121, 1212, 1]) == "1231212121211"
    assert candidate(nums = [12, 121, 12121, 1212]) == "12121212121121"
    assert candidate(nums = [33, 3, 333, 3333]) == "3333333333"
    assert candidate(nums = [82, 828, 8282, 82828]) == "82882828828282"
    assert candidate(nums = [233, 23, 2333]) == "233323323"
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99989796959493929190"
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == "9876543210"
    assert candidate(nums = [30, 3, 34, 5, 9, 31]) == "953433130"
    assert candidate(nums = [56, 565, 5656, 56565]) == "56565656565565"
    assert candidate(nums = [21, 212, 2121]) == "212212121"
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == "110100100010000100000"
    assert candidate(nums = [12, 121, 1211]) == "121211211"
    assert candidate(nums = [34323, 3432, 343, 34]) == "34343343234323"
    assert candidate(nums = [830, 8308]) == "8308830"
    assert candidate(nums = [1000000, 10000, 100, 1]) == "1100100001000000"
    assert candidate(nums = [987, 98, 9, 9876]) == "9989879876"
    assert candidate(nums = [3, 30, 34, 5, 9, 300, 303]) == "9534330330300"
    assert candidate(nums = [830, 83, 83083]) == "8383083830"
    assert candidate(nums = [0, 0, 0, 1]) == "1000"
    assert candidate(nums = [999, 99, 9, 100, 10]) == "99999910100"
    assert candidate(nums = [10, 100, 1000, 10000, 100000]) == "10100100010000100000"
    assert candidate(nums = [12, 21, 121, 122, 212, 211]) == "2122121112212121"
    assert candidate(nums = [90, 900, 9000, 90000, 900000, 9000000, 90000000]) == "90900900090000900000900000090000000"
    assert candidate(nums = [34323, 3432]) == "343234323"
    assert candidate(nums = [1000, 100, 10, 1]) == "1101001000"
    assert candidate(nums = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) == "1000000000"
    assert candidate(nums = [45, 454, 4545, 45454]) == "45454545454454"
    assert candidate(nums = [839, 8399, 83998, 83983]) == "83998839983983983"
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
    assert candidate(nums = [789, 7897, 78978, 789789, 7897897, 78978978]) == "789789789789789787897897789787897"
    assert candidate(nums = [33, 333, 3333, 33333]) == "33333333333333"
    assert candidate(nums = [830, 83, 834, 835, 832]) == "83835834832830"
    assert candidate(nums = [55, 555, 5, 5555, 55555]) == "555555555555555"
    assert candidate(nums = [0, 0, 0, 0, 1]) == "10000"
    assert candidate(nums = [11, 111, 1111, 11111, 111111, 1111111]) == "111111111111111111111111111"
    assert candidate(nums = [101, 10, 1, 100]) == "110110100"
    assert candidate(nums = [2, 22, 222, 2222, 22222, 222222, 2222222, 22222222]) == "222222222222222222222222222222222222"
    assert candidate(nums = [987, 98, 9, 999, 99, 998, 9989]) == "999999998999898987"
    assert candidate(nums = [12, 121, 1213, 12131]) == "12131213112121"
    assert candidate(nums = [111311, 1113, 11113, 11131, 111]) == "11131113111131111113111"
    assert candidate(nums = [1111111111, 111111111, 11111111, 1111111, 111111, 11111, 1111, 111, 11, 1]) == "1111111111111111111111111111111111111111111111111111111"
    assert candidate(nums = [100, 1000, 10, 1]) == "1101001000"
    assert candidate(nums = [5, 55, 555, 5555, 55555]) == "555555555555555"
    assert candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777"
    assert candidate(nums = [987654321, 98765432, 9876543, 987654, 98765, 9876, 987, 98, 9]) == "998987987698765987654987654398765432987654321"
    assert candidate(nums = [0, 0, 0, 1]) == "1000"
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == "999999999999999999999"
    assert candidate(nums = [12, 121, 12121, 1212, 1]) == "121212121211211"
    assert candidate(nums = [7, 77, 777, 7777]) == "7777777777"
    assert candidate(nums = [21, 212, 2121, 211]) == "212212121211"
    assert candidate(nums = [9999, 999, 99, 9]) == "9999999999"
    assert candidate(nums = [34, 343, 3434]) == "343434343"
    assert candidate(nums = [7, 70, 707, 77, 700]) == "77770770700"
    assert candidate(nums = [123, 1234, 12345, 123456]) == "123456123451234123"
    assert candidate(nums = [999, 9999, 99999]) == "999999999999"
    assert candidate(nums = [1111, 111, 11, 1]) == "1111111111"
    assert candidate(nums = [1, 34, 3, 98, 9, 76, 45, 6]) == "998766453431"
    assert candidate(nums = [9, 98, 989, 9898]) == "9989989898"
    assert candidate(nums = [99, 9, 999, 9999]) == "9999999999"
    assert candidate(nums = [300, 30, 3]) == "330300"
    assert candidate(nums = [987, 98, 9]) == "998987"
    assert candidate(nums = [8, 89, 898, 8989, 89898, 898989]) == "898989898989898988988"
    assert candidate(nums = [10, 101, 1011, 10111]) == "10111101110110"
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "98765432110"
    assert candidate(nums = [345, 3453, 34534]) == "345345343453"
    assert candidate(nums = [555, 55, 5]) == "555555"
    assert candidate(nums = [12, 121]) == "12121"
    assert candidate(nums = [7, 77, 777, 7777, 77777]) == "777777777777777"
    assert candidate(nums = [0, 4, 44, 444, 4444]) == "44444444440"
    assert candidate(nums = [111, 11, 1111, 11111, 1]) == "111111111111111"
    assert candidate(nums = [90, 909, 9090]) == "909909090"
    assert candidate(nums = [1000, 10, 100, 1]) == "1101001000"
    assert candidate(nums = [67, 676, 6767, 67676, 676767, 6767676]) == "676767676767676767667676676"
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "98765432110"
    assert candidate(nums = [7, 77, 777, 7777, 77777, 777777, 7777777]) == "7777777777777777777777777777"
    assert candidate(nums = [830, 8308, 830830, 83083]) == "830883083830830830"
    assert candidate(nums = [1000, 100, 10, 1]) == "1101001000"
    assert candidate(nums = [1, 20, 23, 4, 2]) == "4232201"
    assert candidate(nums = [78, 787, 7878, 78787]) == "78787878787787"
    assert candidate(nums = [21, 212, 2121, 21212]) == "21221212212121"
    assert candidate(nums = [111311, 1113, 11, 11131111, 11111113, 11113111]) == "111311131111131111111131111111111311"
    assert candidate(nums = [5, 50, 500, 5000, 50000, 500000, 5000000, 50000000]) == "550500500050000500000500000050000000"
    assert candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890]) == "890789678567456345234123"
    assert candidate(nums = [824, 82, 8]) == "882824"
    assert candidate(nums = [3, 30, 34, 5, 9, 300, 303, 33, 333]) == "953433333330330300"
    assert candidate(nums = [79, 798, 797, 7987]) == "798798779797"
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "908070605040302010100"
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == "1101001000100001000001000000100000001000000001000000000"
    assert candidate(nums = [1, 10, 101, 1011, 10111]) == "110111101110110"
    assert candidate(nums = [88, 888, 8888, 88888, 888888, 8888888, 88888888]) == "88888888888888888888888888888888888"
    assert candidate(nums = [83, 838, 8383, 83838]) == "83883838838383"
    assert candidate(nums = [20, 200, 2000, 20000]) == "20200200020000"
    assert candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 0]) == "9999999999999999999999999999999999999999999990"
    assert candidate(nums = [30, 303, 3003, 3]) == "3303303003"
    assert candidate(nums = [30033, 300, 3, 3003]) == "3300333003300"
    assert candidate(nums = [100, 1000, 10000, 100000, 1]) == "1100100010000100000"
    assert candidate(nums = [56, 565, 566]) == "56656565"
    assert candidate(nums = [6, 66, 666, 6666, 66666, 666666, 6666666, 66666666, 666666666, 6666666666]) == "6666666666666666666666666666666666666666666666666666666"
    assert candidate(nums = [111, 11, 1]) == "111111"
    assert candidate(nums = [123, 1231, 12312, 12, 121, 1212]) == "123123121231121212121"
    assert candidate(nums = [12, 121, 1211, 12111]) == "12121121112111"
    assert candidate(nums = [432, 4324, 43, 43243, 4]) == "443432443243432"
    assert candidate(nums = [111, 11, 1, 1111]) == "1111111111"
    assert candidate(nums = [33, 330, 3330, 333]) == "333333330330"
    assert candidate(nums = [824, 8247]) == "8248247"
    assert candidate(nums = [9, 99, 999, 9999]) == "9999999999"
    assert candidate(nums = [0, 0, 0, 1, 1, 1, 0]) == "1110000"
    assert candidate(nums = [1, 20, 23, 4, 25]) == "42523201"
    assert candidate(nums = [0, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "8642018161412100"
    assert candidate(nums = [21, 212, 2121, 21212]) == "21221212212121"
    assert candidate(nums = [4, 44, 444, 4444, 44444, 444444, 4444444, 44444444]) == "444444444444444444444444444444444444"
    assert candidate(nums = [111311, 1113, 11, 1111, 1]) == "11131113111111111"
    assert candidate(nums = [100, 10, 1, 101, 110, 111, 11, 1001]) == "111111110101101001100"
    assert candidate(nums = [1, 34, 3, 98, 9, 76, 45, 67]) == "9987667453431"
    assert candidate(nums = [54, 546, 548, 60]) == "6054854654"
    assert candidate(nums = [33, 333, 3333, 33333, 3]) == "333333333333333"
    assert candidate(nums = [1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == "1101001000100001000001000000100000001000000001000000000"
    assert candidate(nums = [10, 100, 1000, 10000]) == "10100100010000"
    assert candidate(nums = [999999999, 99999999, 9999999, 999999, 99999, 9999, 999, 99, 9, 1]) == "9999999999999999999999999999999999999999999991"
    assert candidate(nums = [66, 666, 6666, 66666, 666666, 6666666, 66666666]) == "66666666666666666666666666666666666"
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == "110100100010000"
    assert candidate(nums = [824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 6828, 5662, 6699, 10, 7896, 8626, 3462, 2000, 7988, 626, 6670, 4224, 2996]) == "9609938862682479887896697368286699667062657035662560743984224346229962000139910"
    assert candidate(nums = [233, 322, 32]) == "32322233"
    assert candidate(nums = [32, 323, 3232, 32323]) == "32332323323232"
    assert candidate(nums = [647, 64, 646, 6476]) == "647664764664"
    assert candidate(nums = [111, 11, 1]) == "111111"
    assert candidate(nums = [1, 20, 200, 2000, 20000]) == "202002000200001"
    assert candidate(nums = [12, 121, 1211, 12111, 121111, 1]) == "121211211121111211111"
    assert candidate(nums = [333, 33, 3]) == "333333"
    assert candidate(nums = [824, 8247]) == "8248247"
    assert candidate(nums = [35, 353, 3535, 35353, 353535, 3535353, 35353535]) == "35353535353535353535353535335353353"


