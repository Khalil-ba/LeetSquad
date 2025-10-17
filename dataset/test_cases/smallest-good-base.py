def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = "4681") == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "4681") == "8": {e}')
    
    total += 1
    try:
        result = candidate(n = "9") == "8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9") == "8": {e}')
    
    total += 1
    try:
        result = candidate(n = "104729") == "104728"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "104729") == "104728": {e}')
    
    total += 1
    try:
        result = candidate(n = "15") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "15") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "218") == "217"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "218") == "217": {e}')
    
    total += 1
    try:
        result = candidate(n = "13") == "3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "13") == "3": {e}')
    
    total += 1
    try:
        result = candidate(n = "81") == "80"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "81") == "80": {e}')
    
    total += 1
    try:
        result = candidate(n = "7") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "7") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "3") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "3") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "4") == "3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "4") == "3": {e}')
    
    total += 1
    try:
        result = candidate(n = "121") == "3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "121") == "3": {e}')
    
    total += 1
    try:
        result = candidate(n = "8") == "7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8") == "7": {e}')
    
    total += 1
    try:
        result = candidate(n = "21") == "4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "21") == "4": {e}')
    
    total += 1
    try:
        result = candidate(n = "1023") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1023") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "255") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "255") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "91") == "9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "91") == "9": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000") == "999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000") == "999": {e}')
    
    total += 1
    try:
        result = candidate(n = "999") == "998"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999") == "998": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000") == "999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000") == "999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "2187") == "2186"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2187") == "2186": {e}')
    
    total += 1
    try:
        result = candidate(n = "100") == "99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100") == "99": {e}')
    
    total += 1
    try:
        result = candidate(n = "343") == "18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "343") == "18": {e}')
    
    total += 1
    try:
        result = candidate(n = "1801088541") == "1801088540"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1801088541") == "1801088540": {e}')
    
    total += 1
    try:
        result = candidate(n = "2222222222222222222") == "2222222222222222221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2222222222222222222") == "2222222222222222221": {e}')
    
    total += 1
    try:
        result = candidate(n = "14348907") == "14348906"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "14348907") == "14348906": {e}')
    
    total += 1
    try:
        result = candidate(n = "59048") == "59047"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "59048") == "59047": {e}')
    
    total += 1
    try:
        result = candidate(n = "1125899906842623") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1125899906842623") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "100000000") == "99999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "100000000") == "99999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "79228162514264337593543950336") == "79228162514264337593543950335"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "79228162514264337593543950336") == "79228162514264337593543950335": {e}')
    
    total += 1
    try:
        result = candidate(n = "348678440099710752") == "348678440099710751"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "348678440099710752") == "348678440099710751": {e}')
    
    total += 1
    try:
        result = candidate(n = "222222222222222222") == "222222222222222221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "222222222222222222") == "222222222222222221": {e}')
    
    total += 1
    try:
        result = candidate(n = "1234567890123456789") == "1234567890123456788"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1234567890123456789") == "1234567890123456788": {e}')
    
    total += 1
    try:
        result = candidate(n = "617673396283947") == "617673396283946"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "617673396283947") == "617673396283946": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000") == "999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000") == "999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321") == "987654320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321") == "987654320": {e}')
    
    total += 1
    try:
        result = candidate(n = "298023223876953125") == "298023223876953124"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "298023223876953125") == "298023223876953124": {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432109876543") == "98765432109876542"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432109876543") == "98765432109876542": {e}')
    
    total += 1
    try:
        result = candidate(n = "3486784401") == "3486784400"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "3486784401") == "3486784400": {e}')
    
    total += 1
    try:
        result = candidate(n = "8191") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8191") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "19683") == "19682"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "19683") == "19682": {e}')
    
    total += 1
    try:
        result = candidate(n = "12345678987654321") == "12345678987654320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "12345678987654321") == "12345678987654320": {e}')
    
    total += 1
    try:
        result = candidate(n = "68719476736") == "68719476735"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "68719476736") == "68719476735": {e}')
    
    total += 1
    try:
        result = candidate(n = "549755813888") == "549755813887"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "549755813888") == "549755813887": {e}')
    
    total += 1
    try:
        result = candidate(n = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == "99999999999999999999999999999999999999999999999999999999999999999999999999999999998"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == "99999999999999999999999999999999999999999999999999999999999999999999999999999999998": {e}')
    
    total += 1
    try:
        result = candidate(n = "3125") == "3124"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "3125") == "3124": {e}')
    
    total += 1
    try:
        result = candidate(n = "555555555555555555") == "555555555555555554"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "555555555555555555") == "555555555555555554": {e}')
    
    total += 1
    try:
        result = candidate(n = "281474976710656") == "281474976710655"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "281474976710656") == "281474976710655": {e}')
    
    total += 1
    try:
        result = candidate(n = "10000000000000000000000000000000000000000000000000000") == "9999999999999999999999999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "10000000000000000000000000000000000000000000000000000") == "9999999999999999999999999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "18446744073709551615") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "18446744073709551615") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "18014398509481984") == "18014398509481983"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "18014398509481984") == "18014398509481983": {e}')
    
    total += 1
    try:
        result = candidate(n = "193836733056657") == "193836733056656"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "193836733056657") == "193836733056656": {e}')
    
    total += 1
    try:
        result = candidate(n = "387420488") == "387420487"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "387420488") == "387420487": {e}')
    
    total += 1
    try:
        result = candidate(n = "8916100448256") == "8916100448255"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "8916100448256") == "8916100448255": {e}')
    
    total += 1
    try:
        result = candidate(n = "98765432109876543210987654321") == "98765432109876543210987654320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "98765432109876543210987654321") == "98765432109876543210987654320": {e}')
    
    total += 1
    try:
        result = candidate(n = "6789101112131415161718192021222324252627282930") == "6789101112131415161718192021222324252627282929"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "6789101112131415161718192021222324252627282930") == "6789101112131415161718192021222324252627282929": {e}')
    
    total += 1
    try:
        result = candidate(n = "68719476735") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "68719476735") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "2357947691") == "2357947690"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2357947691") == "2357947690": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "4095") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "4095") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "65535") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "65535") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "16777216") == "16777215"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "16777216") == "16777215": {e}')
    
    total += 1
    try:
        result = candidate(n = "65537") == "65536"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "65537") == "65536": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111") == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111") == "10": {e}')
    
    total += 1
    try:
        result = candidate(n = "4398046511104") == "4398046511103"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "4398046511104") == "4398046511103": {e}')
    
    total += 1
    try:
        result = candidate(n = "111111111111111111") == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "111111111111111111") == "10": {e}')
    
    total += 1
    try:
        result = candidate(n = "823543") == "823542"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "823543") == "823542": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789101112131415") == "123456789101112131414"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789101112131415") == "123456789101112131414": {e}')
    
    total += 1
    try:
        result = candidate(n = "101110111") == "101110110"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "101110111") == "101110110": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111111111111") == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111111111111") == "10": {e}')
    
    total += 1
    try:
        result = candidate(n = "38127987654321") == "38127987654320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "38127987654321") == "38127987654320": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111111111111111111111111") == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111111111111111111111111") == "10": {e}')
    
    total += 1
    try:
        result = candidate(n = "161051") == "161050"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "161051") == "161050": {e}')
    
    total += 1
    try:
        result = candidate(n = "4294967295") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "4294967295") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "2305843009213693952") == "2305843009213693951"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2305843009213693952") == "2305843009213693951": {e}')
    
    total += 1
    try:
        result = candidate(n = "1134903170") == "1134903169"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1134903170") == "1134903169": {e}')
    
    total += 1
    try:
        result = candidate(n = "797161") == "3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "797161") == "3": {e}')
    
    total += 1
    try:
        result = candidate(n = "59049") == "59048"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "59049") == "59048": {e}')
    
    total += 1
    try:
        result = candidate(n = "678223072849") == "678223072848"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "678223072849") == "678223072848": {e}')
    
    total += 1
    try:
        result = candidate(n = "134217728") == "134217727"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "134217728") == "134217727": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999998") == "999999999999999997"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999998") == "999999999999999997": {e}')
    
    total += 1
    try:
        result = candidate(n = "2000000000000000000") == "1999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "2000000000000000000") == "1999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999997") == "999999999999999996"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999997") == "999999999999999996": {e}')
    
    total += 1
    try:
        result = candidate(n = "9223372036854775807") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9223372036854775807") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789012345678") == "123456789012345677"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789012345678") == "123456789012345677": {e}')
    
    total += 1
    try:
        result = candidate(n = "987654321987654321") == "987654321987654320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "987654321987654321") == "987654321987654320": {e}')
    
    total += 1
    try:
        result = candidate(n = "515377520732011329") == "515377520732011328"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "515377520732011329") == "515377520732011328": {e}')
    
    total += 1
    try:
        result = candidate(n = "387420489") == "387420488"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "387420489") == "387420488": {e}')
    
    total += 1
    try:
        result = candidate(n = "282429536481") == "282429536480"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "282429536481") == "282429536480": {e}')
    
    total += 1
    try:
        result = candidate(n = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "57896044618658097711785492504343953926634992332820282019728792003956564819948"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "57896044618658097711785492504343953926634992332820282019728792003956564819948": {e}')
    
    total += 1
    try:
        result = candidate(n = "268435455") == "2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "268435455") == "2": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999") == "999999998"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999") == "999999998": {e}')
    
    total += 1
    try:
        result = candidate(n = "9811") == "9810"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "9811") == "9810": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789") == "123456788"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789") == "123456788": {e}')
    
    total += 1
    try:
        result = candidate(n = "3689348814741910323") == "3689348814741910322"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "3689348814741910323") == "3689348814741910322": {e}')
    
    total += 1
    try:
        result = candidate(n = "5555555555555555555") == "5555555555555555554"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "5555555555555555555") == "5555555555555555554": {e}')
    
    total += 1
    try:
        result = candidate(n = "999999999999999981") == "999999999999999980"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "999999999999999981") == "999999999999999980": {e}')
    
    total += 1
    try:
        result = candidate(n = "1024") == "1023"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1024") == "1023": {e}')
    
    total += 1
    try:
        result = candidate(n = "1010101010101010101") == "100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1010101010101010101") == "100": {e}')
    
    total += 1
    try:
        result = candidate(n = "1111111111111111112") == "1111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1111111111111111112") == "1111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(n = "555555555555555555555555555555") == "555555555555555555555555555554"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "555555555555555555555555555555") == "555555555555555555555555555554": {e}')
    
    total += 1
    try:
        result = candidate(n = "1000000000000000001") == "1000000000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1000000000000000001") == "1000000000000000000": {e}')
    
    total += 1
    try:
        result = candidate(n = "78364164096") == "78364164095"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "78364164096") == "78364164095": {e}')
    
    total += 1
    try:
        result = candidate(n = "123456789012345678901234567890") == "123456789012345678901234567889"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "123456789012345678901234567890") == "123456789012345678901234567889": {e}')
    
    total += 1
    try:
        result = candidate(n = "1125899906842624") == "1125899906842623"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = "1125899906842624") == "1125899906842623": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = "4681") == "8"
    assert candidate(n = "9") == "8"
    assert candidate(n = "104729") == "104728"
    assert candidate(n = "15") == "2"
    assert candidate(n = "218") == "217"
    assert candidate(n = "13") == "3"
    assert candidate(n = "81") == "80"
    assert candidate(n = "7") == "2"
    assert candidate(n = "3") == "2"
    assert candidate(n = "4") == "3"
    assert candidate(n = "121") == "3"
    assert candidate(n = "8") == "7"
    assert candidate(n = "21") == "4"
    assert candidate(n = "1023") == "2"
    assert candidate(n = "255") == "2"
    assert candidate(n = "91") == "9"
    assert candidate(n = "1000") == "999"
    assert candidate(n = "999") == "998"
    assert candidate(n = "1000000000000000000") == "999999999999999999"
    assert candidate(n = "2187") == "2186"
    assert candidate(n = "100") == "99"
    assert candidate(n = "343") == "18"
    assert candidate(n = "1801088541") == "1801088540"
    assert candidate(n = "2222222222222222222") == "2222222222222222221"
    assert candidate(n = "14348907") == "14348906"
    assert candidate(n = "59048") == "59047"
    assert candidate(n = "1125899906842623") == "2"
    assert candidate(n = "100000000") == "99999999"
    assert candidate(n = "79228162514264337593543950336") == "79228162514264337593543950335"
    assert candidate(n = "348678440099710752") == "348678440099710751"
    assert candidate(n = "222222222222222222") == "222222222222222221"
    assert candidate(n = "1234567890123456789") == "1234567890123456788"
    assert candidate(n = "617673396283947") == "617673396283946"
    assert candidate(n = "1000000000") == "999999999"
    assert candidate(n = "987654321") == "987654320"
    assert candidate(n = "298023223876953125") == "298023223876953124"
    assert candidate(n = "98765432109876543") == "98765432109876542"
    assert candidate(n = "3486784401") == "3486784400"
    assert candidate(n = "8191") == "2"
    assert candidate(n = "19683") == "19682"
    assert candidate(n = "12345678987654321") == "12345678987654320"
    assert candidate(n = "68719476736") == "68719476735"
    assert candidate(n = "549755813888") == "549755813887"
    assert candidate(n = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999") == "99999999999999999999999999999999999999999999999999999999999999999999999999999999998"
    assert candidate(n = "3125") == "3124"
    assert candidate(n = "555555555555555555") == "555555555555555554"
    assert candidate(n = "281474976710656") == "281474976710655"
    assert candidate(n = "10000000000000000000000000000000000000000000000000000") == "9999999999999999999999999999999999999999999999999999"
    assert candidate(n = "18446744073709551615") == "2"
    assert candidate(n = "18014398509481984") == "18014398509481983"
    assert candidate(n = "193836733056657") == "193836733056656"
    assert candidate(n = "387420488") == "387420487"
    assert candidate(n = "8916100448256") == "8916100448255"
    assert candidate(n = "98765432109876543210987654321") == "98765432109876543210987654320"
    assert candidate(n = "6789101112131415161718192021222324252627282930") == "6789101112131415161718192021222324252627282929"
    assert candidate(n = "68719476735") == "2"
    assert candidate(n = "2357947691") == "2357947690"
    assert candidate(n = "1000000000000000000000000000000") == "999999999999999999999999999999"
    assert candidate(n = "4095") == "2"
    assert candidate(n = "65535") == "2"
    assert candidate(n = "16777216") == "16777215"
    assert candidate(n = "65537") == "65536"
    assert candidate(n = "111111111") == "10"
    assert candidate(n = "4398046511104") == "4398046511103"
    assert candidate(n = "111111111111111111") == "10"
    assert candidate(n = "823543") == "823542"
    assert candidate(n = "123456789101112131415") == "123456789101112131414"
    assert candidate(n = "101110111") == "101110110"
    assert candidate(n = "1111111111111111111") == "10"
    assert candidate(n = "38127987654321") == "38127987654320"
    assert candidate(n = "1111111111111111111111111111111") == "10"
    assert candidate(n = "161051") == "161050"
    assert candidate(n = "4294967295") == "2"
    assert candidate(n = "2305843009213693952") == "2305843009213693951"
    assert candidate(n = "1134903170") == "1134903169"
    assert candidate(n = "797161") == "3"
    assert candidate(n = "59049") == "59048"
    assert candidate(n = "678223072849") == "678223072848"
    assert candidate(n = "134217728") == "134217727"
    assert candidate(n = "999999999999999998") == "999999999999999997"
    assert candidate(n = "2000000000000000000") == "1999999999999999999"
    assert candidate(n = "999999999999999997") == "999999999999999996"
    assert candidate(n = "9223372036854775807") == "2"
    assert candidate(n = "123456789012345678") == "123456789012345677"
    assert candidate(n = "987654321987654321") == "987654321987654320"
    assert candidate(n = "515377520732011329") == "515377520732011328"
    assert candidate(n = "387420489") == "387420488"
    assert candidate(n = "282429536481") == "282429536480"
    assert candidate(n = "57896044618658097711785492504343953926634992332820282019728792003956564819949") == "57896044618658097711785492504343953926634992332820282019728792003956564819948"
    assert candidate(n = "268435455") == "2"
    assert candidate(n = "999999999") == "999999998"
    assert candidate(n = "9811") == "9810"
    assert candidate(n = "123456789") == "123456788"
    assert candidate(n = "3689348814741910323") == "3689348814741910322"
    assert candidate(n = "5555555555555555555") == "5555555555555555554"
    assert candidate(n = "999999999999999981") == "999999999999999980"
    assert candidate(n = "1024") == "1023"
    assert candidate(n = "1010101010101010101") == "100"
    assert candidate(n = "1111111111111111112") == "1111111111111111111"
    assert candidate(n = "555555555555555555555555555555") == "555555555555555555555555555554"
    assert candidate(n = "1000000000000000001") == "1000000000000000000"
    assert candidate(n = "78364164096") == "78364164095"
    assert candidate(n = "123456789012345678901234567890") == "123456789012345678901234567889"
    assert candidate(n = "1125899906842624") == "1125899906842623"


