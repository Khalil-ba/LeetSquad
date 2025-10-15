def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = "36789",k = 1000) == "36789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "36789",k = 1000) == "36789": {e}')
    
    total += 1
    try:
        result = candidate(num = "100",k = 1) == "010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "100",k = 1) == "010": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 9) == "0987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 9) == "0987654321": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 100) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 100) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "222111333",k = 10) == "111222333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "222111333",k = 10) == "111222333": {e}')
    
    total += 1
    try:
        result = candidate(num = "4321",k = 4) == "1342"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "4321",k = 4) == "1342": {e}')
    
    total += 1
    try:
        result = candidate(num = "3452345",k = 3) == "2345345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3452345",k = 3) == "2345345": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333",k = 5) == "111222333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333",k = 5) == "111222333": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 5) == "4987653210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 5) == "4987653210": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789",k = 0) == "123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789",k = 0) == "123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "102030405060708090",k = 20) == "000001023456708090"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "102030405060708090",k = 20) == "000001023456708090": {e}')
    
    total += 1
    try:
        result = candidate(num = "29431",k = 2) == "23941"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "29431",k = 2) == "23941": {e}')
    
    total += 1
    try:
        result = candidate(num = "59585756555453525150",k = 100) == "01234555555556987555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "59585756555453525150",k = 100) == "01234555555556987555": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999",k = 50) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999",k = 50) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "9487653210",k = 10) == "0498765321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9487653210",k = 10) == "0498765321": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 9) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 9) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "5397268410",k = 15) == "0235796841"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5397268410",k = 15) == "0235796841": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555",k = 25) == "111222333444555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555",k = 25) == "111222333444555": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432101234567890",k = 50) == "00112987654323456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432101234567890",k = 50) == "00112987654323456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "5432109876",k = 10) == "0145329876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5432109876",k = 10) == "0145329876": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234321",k = 5) == "1123432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234321",k = 5) == "1123432": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999888888888877777777776666666666",k = 100) == "6668999999999988888888877777777776666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999888888888877777777776666666666",k = 100) == "6668999999999988888888877777777776666666": {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000000000000000000001",k = 1) == "0000000000000000000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000000000000000000001",k = 1) == "0000000000000000000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = "198765432",k = 20) == "123479865"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "198765432",k = 20) == "123479865": {e}')
    
    total += 1
    try:
        result = candidate(num = "54321098765432109876543210",k = 50) == "00012453987654321987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "54321098765432109876543210",k = 50) == "00012453987654321987654321": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432101234567890",k = 100) == "00112233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432101234567890",k = 100) == "00112233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(num = "5432109876",k = 30) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5432109876",k = 30) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "5943281760",k = 15) == "0159432876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5943281760",k = 15) == "0159432876": {e}')
    
    total += 1
    try:
        result = candidate(num = "19876543210",k = 10) == "01987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "19876543210",k = 10) == "01987654321": {e}')
    
    total += 1
    try:
        result = candidate(num = "77665544332211009988",k = 100) == "00112233447766559988"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "77665544332211009988",k = 100) == "00112233447766559988": {e}')
    
    total += 1
    try:
        result = candidate(num = "543210987654321098765432109876543210",k = 200) == "000011112222345498765398765439876543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "543210987654321098765432109876543210",k = 200) == "000011112222345498765398765439876543": {e}')
    
    total += 1
    try:
        result = candidate(num = "5946132780",k = 15) == "0145963278"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5946132780",k = 15) == "0145963278": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321012345678909876543210",k = 1000) == "000111222333444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321012345678909876543210",k = 1000) == "000111222333444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(num = "342134213421",k = 15) == "112234343421"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "342134213421",k = 15) == "112234343421": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 30) == "0123987654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 30) == "0123987654": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 10) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 10) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 15) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 15) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "999999999999999999999999",k = 1000000) == "999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999999999999999999999999",k = 1000000) == "999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "44444444444444444444",k = 1000) == "44444444444444444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "44444444444444444444",k = 1000) == "44444444444444444444": {e}')
    
    total += 1
    try:
        result = candidate(num = "87654321098765432109",k = 200) == "00112233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "87654321098765432109",k = 200) == "00112233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(num = "999888777666555444333222111000",k = 1000) == "000111222333444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "999888777666555444333222111000",k = 1000) == "000111222333444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210987654321098765432109876543210",k = 200) == "0000111122369875498765439876543298765432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210987654321098765432109876543210",k = 200) == "0000111122369875498765439876543298765432": {e}')
    
    total += 1
    try:
        result = candidate(num = "5555555555",k = 100) == "5555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5555555555",k = 100) == "5555555555": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432109876543210",k = 25) == "01289765439876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432109876543210",k = 25) == "01289765439876543210": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 45) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 45) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 0) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 0) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890123456789012345678901234567890",k = 500) == "0000111122223333444455556666777788889999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890123456789012345678901234567890",k = 500) == "0000111122223333444455556666777788889999": {e}')
    
    total += 1
    try:
        result = candidate(num = "55555555555555555555555555555555",k = 10000) == "55555555555555555555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "55555555555555555555555555555555",k = 10000) == "55555555555555555555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678901234567890",k = 100) == "00112233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678901234567890",k = 100) == "00112233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(num = "1010101010101010101010101010101010101010",k = 50) == "0000000001111101111110101010101010101010"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1010101010101010101010101010101010101010",k = 50) == "0000000001111101111110101010101010101010": {e}')
    
    total += 1
    try:
        result = candidate(num = "9438527610",k = 10) == "0493852761"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9438527610",k = 10) == "0493852761": {e}')
    
    total += 1
    try:
        result = candidate(num = "987654321098765432109876543210",k = 1000) == "000111222333444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "987654321098765432109876543210",k = 1000) == "000111222333444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(num = "5432198760",k = 20) == "0123458976"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5432198760",k = 20) == "0123458976": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210123456789098765432101234567890",k = 300) == "0000111122223333444479865567899876556789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210123456789098765432101234567890",k = 300) == "0000111122223333444479865567899876556789": {e}')
    
    total += 1
    try:
        result = candidate(num = "2134567890",k = 5) == "1234506789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "2134567890",k = 5) == "1234506789": {e}')
    
    total += 1
    try:
        result = candidate(num = "3333222211110000",k = 50) == "0000332332221111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "3333222211110000",k = 50) == "0000332332221111": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890987654321",k = 25) == "0112345678998765432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890987654321",k = 25) == "0112345678998765432": {e}')
    
    total += 1
    try:
        result = candidate(num = "0000000001",k = 5) == "0000000001"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "0000000001",k = 5) == "0000000001": {e}')
    
    total += 1
    try:
        result = candidate(num = "1098765432",k = 20) == "0123489765"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1098765432",k = 20) == "0123489765": {e}')
    
    total += 1
    try:
        result = candidate(num = "111112222233333444445555566666777778888899999",k = 500) == "111112222233333444445555566666777778888899999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111112222233333444445555566666777778888899999",k = 500) == "111112222233333444445555566666777778888899999": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678909876543210",k = 50) == "00112345657899876432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678909876543210",k = 50) == "00112345657899876432": {e}')
    
    total += 1
    try:
        result = candidate(num = "1432214321",k = 10) == "1122343421"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1432214321",k = 10) == "1122343421": {e}')
    
    total += 1
    try:
        result = candidate(num = "12341234123412341234",k = 50) == "11111222223434343434"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12341234123412341234",k = 50) == "11111222223434343434": {e}')
    
    total += 1
    try:
        result = candidate(num = "111222333444555666777888999",k = 300) == "111222333444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "111222333444555666777888999",k = 300) == "111222333444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(num = "333222111000999888777666555444333222111000",k = 500) == "000000111111222222333333444555666779899887"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333222111000999888777666555444333222111000",k = 500) == "000000111111222222333333444555666779899887": {e}')
    
    total += 1
    try:
        result = candidate(num = "9999999999999999999999999999999999999999",k = 100000) == "9999999999999999999999999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9999999999999999999999999999999999999999",k = 100000) == "9999999999999999999999999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1111111111111111111111111111111",k = 30000) == "1111111111111111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1111111111111111111111111111111",k = 30000) == "1111111111111111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(num = "6482319570",k = 8) == "1264839570"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "6482319570",k = 8) == "1264839570": {e}')
    
    total += 1
    try:
        result = candidate(num = "5999888777666555444333222111000",k = 100) == "0004599988877766655544333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5999888777666555444333222111000",k = 100) == "0004599988877766655544333222111": {e}')
    
    total += 1
    try:
        result = candidate(num = "94321",k = 3) == "29431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "94321",k = 3) == "29431": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234321",k = 3) == "1223431"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234321",k = 3) == "1223431": {e}')
    
    total += 1
    try:
        result = candidate(num = "87654321098765432109",k = 50) == "00115876432987654329"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "87654321098765432109",k = 50) == "00115876432987654329": {e}')
    
    total += 1
    try:
        result = candidate(num = "8765432109",k = 100) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "8765432109",k = 100) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "555555555555555555555555",k = 100000) == "555555555555555555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "555555555555555555555555",k = 100000) == "555555555555555555555555": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789876543212345678987654321",k = 150) == "111222233334456789876545678987654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789876543212345678987654321",k = 150) == "111222233334456789876545678987654": {e}')
    
    total += 1
    try:
        result = candidate(num = "54321098765432109876",k = 100) == "00112233445566778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "54321098765432109876",k = 100) == "00112233445566778899": {e}')
    
    total += 1
    try:
        result = candidate(num = "432101234",k = 10) == "011432234"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "432101234",k = 10) == "011432234": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 30) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 30) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 50) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 50) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "1987654320",k = 15) == "0139876542"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1987654320",k = 15) == "0139876542": {e}')
    
    total += 1
    try:
        result = candidate(num = "5142369870",k = 15) == "0123456987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5142369870",k = 15) == "0123456987": {e}')
    
    total += 1
    try:
        result = candidate(num = "444333222111000",k = 50) == "000134344322211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "444333222111000",k = 50) == "000134344322211": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432109876543210",k = 20) == "01698754329876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432109876543210",k = 20) == "01698754329876543210": {e}')
    
    total += 1
    try:
        result = candidate(num = "9457836120",k = 8) == "1495783620"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9457836120",k = 8) == "1495783620": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 10000) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 10000) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "9632147850",k = 12) == "0296314785"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9632147850",k = 12) == "0296314785": {e}')
    
    total += 1
    try:
        result = candidate(num = "10987654321",k = 10) == "01189765432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "10987654321",k = 10) == "01189765432": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234543210",k = 25) == "0112233445"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234543210",k = 25) == "0112233445": {e}')
    
    total += 1
    try:
        result = candidate(num = "1221331223",k = 20) == "1112222333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1221331223",k = 20) == "1112222333": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 50) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 50) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "8642013579",k = 20) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "8642013579",k = 20) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "11111111111111111111",k = 10000) == "11111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "11111111111111111111",k = 10000) == "11111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(num = "192837465546738291",k = 50) == "112233458976546789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "192837465546738291",k = 50) == "112233458976546789": {e}')
    
    total += 1
    try:
        result = candidate(num = "9438276510",k = 10) == "0493827651"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9438276510",k = 10) == "0493827651": {e}')
    
    total += 1
    try:
        result = candidate(num = "123456789012345678901234567890",k = 100) == "000111222345678394567893456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "123456789012345678901234567890",k = 100) == "000111222345678394567893456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678901234567890",k = 20) == "01123456278934567890"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678901234567890",k = 20) == "01123456278934567890": {e}')
    
    total += 1
    try:
        result = candidate(num = "333222111",k = 20) == "111323322"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "333222111",k = 20) == "111323322": {e}')
    
    total += 1
    try:
        result = candidate(num = "9876543210",k = 25) == "0128976543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "9876543210",k = 25) == "0128976543": {e}')
    
    total += 1
    try:
        result = candidate(num = "98765432109876543210",k = 100) == "00112233458976987654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "98765432109876543210",k = 100) == "00112233458976987654": {e}')
    
    total += 1
    try:
        result = candidate(num = "000111222333444555666777888999",k = 50) == "000111222333444555666777888999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "000111222333444555666777888999",k = 50) == "000111222333444555666777888999": {e}')
    
    total += 1
    try:
        result = candidate(num = "1234567890",k = 25) == "0123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "1234567890",k = 25) == "0123456789": {e}')
    
    total += 1
    try:
        result = candidate(num = "5432109876",k = 15) == "0123459876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "5432109876",k = 15) == "0123459876": {e}')
    
    total += 1
    try:
        result = candidate(num = "010203040506070809",k = 30) == "000000001234560789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "010203040506070809",k = 30) == "000000001234560789": {e}')
    
    total += 1
    try:
        result = candidate(num = "99999999999999999999",k = 1000) == "99999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "99999999999999999999",k = 1000) == "99999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(num = "99887766554433221100",k = 50) == "00299887766554433211"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "99887766554433221100",k = 50) == "00299887766554433211": {e}')
    
    total += 1
    try:
        result = candidate(num = "12345678900987654321",k = 50) == "00112234567889976543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = "12345678900987654321",k = 50) == "00112234567889976543": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = "36789",k = 1000) == "36789"
    assert candidate(num = "100",k = 1) == "010"
    assert candidate(num = "9876543210",k = 9) == "0987654321"
    assert candidate(num = "9876543210",k = 100) == "0123456789"
    assert candidate(num = "222111333",k = 10) == "111222333"
    assert candidate(num = "4321",k = 4) == "1342"
    assert candidate(num = "3452345",k = 3) == "2345345"
    assert candidate(num = "111222333",k = 5) == "111222333"
    assert candidate(num = "9876543210",k = 5) == "4987653210"
    assert candidate(num = "123456789",k = 0) == "123456789"
    assert candidate(num = "102030405060708090",k = 20) == "000001023456708090"
    assert candidate(num = "29431",k = 2) == "23941"
    assert candidate(num = "59585756555453525150",k = 100) == "01234555555556987555"
    assert candidate(num = "9999999999",k = 50) == "9999999999"
    assert candidate(num = "9487653210",k = 10) == "0498765321"
    assert candidate(num = "1234567890",k = 9) == "0123456789"
    assert candidate(num = "5397268410",k = 15) == "0235796841"
    assert candidate(num = "111222333444555",k = 25) == "111222333444555"
    assert candidate(num = "98765432101234567890",k = 50) == "00112987654323456789"
    assert candidate(num = "5432109876",k = 10) == "0145329876"
    assert candidate(num = "1234321",k = 5) == "1123432"
    assert candidate(num = "9999999999888888888877777777776666666666",k = 100) == "6668999999999988888888877777777776666666"
    assert candidate(num = "0000000000000000000000001",k = 1) == "0000000000000000000000001"
    assert candidate(num = "198765432",k = 20) == "123479865"
    assert candidate(num = "54321098765432109876543210",k = 50) == "00012453987654321987654321"
    assert candidate(num = "98765432101234567890",k = 100) == "00112233445566778899"
    assert candidate(num = "5432109876",k = 30) == "0123456789"
    assert candidate(num = "5943281760",k = 15) == "0159432876"
    assert candidate(num = "19876543210",k = 10) == "01987654321"
    assert candidate(num = "77665544332211009988",k = 100) == "00112233447766559988"
    assert candidate(num = "543210987654321098765432109876543210",k = 200) == "000011112222345498765398765439876543"
    assert candidate(num = "5946132780",k = 15) == "0145963278"
    assert candidate(num = "987654321012345678909876543210",k = 1000) == "000111222333444555666777888999"
    assert candidate(num = "342134213421",k = 15) == "112234343421"
    assert candidate(num = "9876543210",k = 30) == "0123987654"
    assert candidate(num = "1234567890",k = 10) == "0123456789"
    assert candidate(num = "1234567890",k = 15) == "0123456789"
    assert candidate(num = "999999999999999999999999",k = 1000000) == "999999999999999999999999"
    assert candidate(num = "44444444444444444444",k = 1000) == "44444444444444444444"
    assert candidate(num = "87654321098765432109",k = 200) == "00112233445566778899"
    assert candidate(num = "999888777666555444333222111000",k = 1000) == "000111222333444555666777888999"
    assert candidate(num = "9876543210987654321098765432109876543210",k = 200) == "0000111122369875498765439876543298765432"
    assert candidate(num = "5555555555",k = 100) == "5555555555"
    assert candidate(num = "98765432109876543210",k = 25) == "01289765439876543210"
    assert candidate(num = "9876543210",k = 45) == "0123456789"
    assert candidate(num = "9876543210",k = 0) == "9876543210"
    assert candidate(num = "1234567890123456789012345678901234567890",k = 500) == "0000111122223333444455556666777788889999"
    assert candidate(num = "55555555555555555555555555555555",k = 10000) == "55555555555555555555555555555555"
    assert candidate(num = "12345678901234567890",k = 100) == "00112233445566778899"
    assert candidate(num = "1010101010101010101010101010101010101010",k = 50) == "0000000001111101111110101010101010101010"
    assert candidate(num = "9438527610",k = 10) == "0493852761"
    assert candidate(num = "987654321098765432109876543210",k = 1000) == "000111222333444555666777888999"
    assert candidate(num = "5432198760",k = 20) == "0123458976"
    assert candidate(num = "9876543210123456789098765432101234567890",k = 300) == "0000111122223333444479865567899876556789"
    assert candidate(num = "2134567890",k = 5) == "1234506789"
    assert candidate(num = "3333222211110000",k = 50) == "0000332332221111"
    assert candidate(num = "1234567890987654321",k = 25) == "0112345678998765432"
    assert candidate(num = "0000000001",k = 5) == "0000000001"
    assert candidate(num = "1098765432",k = 20) == "0123489765"
    assert candidate(num = "111112222233333444445555566666777778888899999",k = 500) == "111112222233333444445555566666777778888899999"
    assert candidate(num = "12345678909876543210",k = 50) == "00112345657899876432"
    assert candidate(num = "1432214321",k = 10) == "1122343421"
    assert candidate(num = "12341234123412341234",k = 50) == "11111222223434343434"
    assert candidate(num = "111222333444555666777888999",k = 300) == "111222333444555666777888999"
    assert candidate(num = "333222111000999888777666555444333222111000",k = 500) == "000000111111222222333333444555666779899887"
    assert candidate(num = "9999999999999999999999999999999999999999",k = 100000) == "9999999999999999999999999999999999999999"
    assert candidate(num = "1111111111111111111111111111111",k = 30000) == "1111111111111111111111111111111"
    assert candidate(num = "6482319570",k = 8) == "1264839570"
    assert candidate(num = "5999888777666555444333222111000",k = 100) == "0004599988877766655544333222111"
    assert candidate(num = "94321",k = 3) == "29431"
    assert candidate(num = "1234321",k = 3) == "1223431"
    assert candidate(num = "87654321098765432109",k = 50) == "00115876432987654329"
    assert candidate(num = "8765432109",k = 100) == "0123456789"
    assert candidate(num = "555555555555555555555555",k = 100000) == "555555555555555555555555"
    assert candidate(num = "123456789876543212345678987654321",k = 150) == "111222233334456789876545678987654"
    assert candidate(num = "54321098765432109876",k = 100) == "00112233445566778899"
    assert candidate(num = "432101234",k = 10) == "011432234"
    assert candidate(num = "1234567890",k = 30) == "0123456789"
    assert candidate(num = "9876543210",k = 50) == "0123456789"
    assert candidate(num = "1987654320",k = 15) == "0139876542"
    assert candidate(num = "5142369870",k = 15) == "0123456987"
    assert candidate(num = "444333222111000",k = 50) == "000134344322211"
    assert candidate(num = "98765432109876543210",k = 20) == "01698754329876543210"
    assert candidate(num = "9457836120",k = 8) == "1495783620"
    assert candidate(num = "9876543210",k = 10000) == "0123456789"
    assert candidate(num = "9632147850",k = 12) == "0296314785"
    assert candidate(num = "10987654321",k = 10) == "01189765432"
    assert candidate(num = "1234543210",k = 25) == "0112233445"
    assert candidate(num = "1221331223",k = 20) == "1112222333"
    assert candidate(num = "1234567890",k = 50) == "0123456789"
    assert candidate(num = "8642013579",k = 20) == "0123456789"
    assert candidate(num = "11111111111111111111",k = 10000) == "11111111111111111111"
    assert candidate(num = "192837465546738291",k = 50) == "112233458976546789"
    assert candidate(num = "9438276510",k = 10) == "0493827651"
    assert candidate(num = "123456789012345678901234567890",k = 100) == "000111222345678394567893456789"
    assert candidate(num = "12345678901234567890",k = 20) == "01123456278934567890"
    assert candidate(num = "333222111",k = 20) == "111323322"
    assert candidate(num = "9876543210",k = 25) == "0128976543"
    assert candidate(num = "98765432109876543210",k = 100) == "00112233458976987654"
    assert candidate(num = "000111222333444555666777888999",k = 50) == "000111222333444555666777888999"
    assert candidate(num = "1234567890",k = 25) == "0123456789"
    assert candidate(num = "5432109876",k = 15) == "0123459876"
    assert candidate(num = "010203040506070809",k = 30) == "000000001234560789"
    assert candidate(num = "99999999999999999999",k = 1000) == "99999999999999999999"
    assert candidate(num = "99887766554433221100",k = 50) == "00299887766554433211"
    assert candidate(num = "12345678900987654321",k = 50) == "00112234567889976543"


