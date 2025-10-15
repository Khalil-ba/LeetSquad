def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(expression = "56+78") == "(56+78)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "56+78") == "(56+78)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5+6") == "(5+6)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5+6") == "(5+6)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3+8") == "(3+8)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3+8") == "(3+8)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "111+222") == "1(11+22)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "111+222") == "1(11+22)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3+2") == "(3+2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3+2") == "(3+2)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5+678") == "(5+67)8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5+678") == "(5+67)8": {e}')
    
    total += 1
    try:
        result = candidate(expression = "247+38") == "2(47+38)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "247+38") == "2(47+38)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3+12") == "(3+1)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3+12") == "(3+1)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "11+11") == "1(1+1)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "11+11") == "1(1+1)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "8+9") == "(8+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "8+9") == "(8+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+2") == "(1+2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+2") == "(1+2)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+456") == "1(23+45)6"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+456") == "1(23+45)6": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+9") == "(9+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+9") == "(9+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12+34") == "1(2+3)4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12+34") == "1(2+3)4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "88+11") == "8(8+1)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "88+11") == "8(8+1)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "999+999") == "(999+999)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "999+999") == "(999+999)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+9") == "(1+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+9") == "(1+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "333+444") == "(333+444)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "333+444") == "(333+444)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "555+666") == "(555+666)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "555+666") == "(555+666)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+99") == "(9+99)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+99") == "(9+99)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+1") == "(9+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+1") == "(9+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5+9") == "(5+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5+9") == "(5+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+1") == "(1+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+1") == "(1+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "10+1") == "1(0+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "10+1") == "1(0+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12+3") == "1(2+3)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12+3") == "1(2+3)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "555+555") == "(555+555)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "555+555") == "(555+555)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+4") == "1(23+4)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+4") == "1(23+4)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+876") == "(9+87)6"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+876") == "(9+87)6": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12345+6789") == "1(2345+6789)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12345+6789") == "1(2345+6789)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "56+789") == "(56+789)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "56+789") == "(56+789)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1111+2222") == "1(111+222)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1111+2222") == "1(111+222)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+4567") == "1(23+456)7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+4567") == "1(23+456)7": {e}')
    
    total += 1
    try:
        result = candidate(expression = "6666+7777") == "(6666+7777)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "6666+7777") == "(6666+7777)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9999+1") == "9(999+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9999+1") == "9(999+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12+345") == "1(2+34)5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12+345") == "1(2+34)5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "567+89") == "(567+89)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "567+89") == "(567+89)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "8+7654") == "(8+765)4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "8+7654") == "(8+765)4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "987+654") == "(987+654)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "987+654") == "(987+654)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "33+44") == "(33+44)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "33+44") == "(33+44)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1234+56789") == "1(234+5678)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1234+56789") == "1(234+5678)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "7000+8000") == "(7000+8)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "7000+8000") == "(7000+8)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "99+11") == "9(9+1)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "99+11") == "9(9+1)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "333+666") == "(333+666)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "333+666") == "(333+666)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "345+678") == "(345+678)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "345+678") == "(345+678)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "50+50") == "(50+5)0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "50+50") == "(50+5)0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+45") == "1(23+45)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+45") == "1(23+45)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5+55") == "(5+5)5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5+55") == "(5+5)5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "678+9") == "6(78+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "678+9") == "6(78+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12+345678") == "1(2+34)5678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12+345678") == "1(2+34)5678": {e}')
    
    total += 1
    try:
        result = candidate(expression = "900000+100000") == "(900000+1)00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "900000+100000") == "(900000+1)00000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "10+20") == "(10+2)0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "10+20") == "(10+2)0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "12+3456789") == "1(2+34)56789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "12+3456789") == "1(2+34)56789": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123456+789012") == "1(23456+78901)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123456+789012") == "1(23456+78901)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "99+88") == "(99+88)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "99+88") == "(99+88)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "56+7890") == "(56+789)0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "56+7890") == "(56+789)0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+1234") == "(9+123)4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+1234") == "(9+123)4": {e}')
    
    total += 1
    try:
        result = candidate(expression = "55555+66666") == "(55555+66666)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "55555+66666") == "(55555+66666)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1234+56") == "1(234+56)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1234+56") == "1(234+56)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "678+90123") == "(678+9012)3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "678+90123") == "(678+9012)3": {e}')
    
    total += 1
    try:
        result = candidate(expression = "44+555") == "(44+55)5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "44+555") == "(44+55)5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+87654321") == "(9+8765432)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+87654321") == "(9+8765432)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "2222+3333") == "2(222+333)3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "2222+3333") == "2(222+333)3": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+999") == "(1+99)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+999") == "(1+99)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9876+5432") == "(9876+5432)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9876+5432") == "(9876+5432)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "4321+9") == "43(21+9)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "4321+9") == "43(21+9)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5678+910") == "(5678+91)0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5678+910") == "(5678+91)0": {e}')
    
    total += 1
    try:
        result = candidate(expression = "987654+321098") == "(987654+321098)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "987654+321098") == "(987654+321098)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "100000+200000") == "(100000+2)00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "100000+200000") == "(100000+2)00000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3000+4000") == "(3000+4)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3000+4000") == "(3000+4)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "300000+400000") == "(300000+4)00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "300000+400000") == "(300000+4)00000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "100+100") == "(100+1)00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "100+100") == "(100+1)00": {e}')
    
    total += 1
    try:
        result = candidate(expression = "10+999") == "1(0+9)99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "10+999") == "1(0+9)99": {e}')
    
    total += 1
    try:
        result = candidate(expression = "500000+600000") == "(500000+6)00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "500000+600000") == "(500000+6)00000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5432+1") == "543(2+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5432+1") == "543(2+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+9999") == "(1+999)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+9999") == "(1+999)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3456+789") == "3(456+789)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3456+789") == "3(456+789)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5555+666") == "5(555+666)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5555+666") == "5(555+666)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+6") == "1(23+6)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+6") == "1(23+6)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "8888+9999") == "(8888+9999)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "8888+9999") == "(8888+9999)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "213+456") == "(213+456)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "213+456") == "(213+456)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "23+4567") == "(23+456)7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "23+4567") == "(23+456)7": {e}')
    
    total += 1
    try:
        result = candidate(expression = "100+200") == "(100+2)00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "100+200") == "(100+2)00": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+8765432") == "(9+876543)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+8765432") == "(9+876543)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "111+111") == "1(11+11)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "111+111") == "1(11+11)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "77777+88888") == "(77777+88888)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "77777+88888") == "(77777+88888)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "99+1") == "9(9+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "99+1") == "9(9+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "3+9999") == "(3+999)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "3+9999") == "(3+999)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "234+567") == "(234+567)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "234+567") == "(234+567)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "2+9999") == "(2+999)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "2+9999") == "(2+999)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "4321+876") == "4(321+876)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "4321+876") == "4(321+876)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9000+1000") == "(9000+1)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9000+1000") == "(9000+1)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "11+111") == "1(1+11)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "11+111") == "1(1+11)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5+6789") == "(5+678)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5+6789") == "(5+678)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+23456") == "(1+2)3456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+23456") == "(1+2)3456": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1098+231") == "1(098+23)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1098+231") == "1(098+23)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "999+1") == "9(99+1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "999+1") == "9(99+1)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "4444+5555") == "(4444+5555)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "4444+5555") == "(4444+5555)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "55+55") == "(55+55)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "55+55") == "(55+55)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "777+888") == "(777+888)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "777+888") == "(777+888)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "98765+4321") == "9(8765+432)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "98765+4321") == "9(8765+432)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "654+321") == "6(54+32)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "654+321") == "6(54+32)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "77+88") == "(77+88)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "77+88") == "(77+88)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "33333+44444") == "(33333+44444)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "33333+44444") == "(33333+44444)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "222+333") == "2(22+33)3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "222+333") == "2(22+33)3": {e}')
    
    total += 1
    try:
        result = candidate(expression = "2+987654321") == "(2+98765432)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "2+987654321") == "(2+98765432)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+45678") == "1(23+4567)8"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+45678") == "1(23+4567)8": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9+8765") == "(9+876)5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9+8765") == "(9+876)5": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5678+123") == "5(678+123)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5678+123") == "5(678+123)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1234+567") == "1(234+567)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1234+567") == "1(234+567)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "234+56789") == "(234+5678)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "234+56789") == "(234+5678)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "987654+321") == "987(654+32)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "987654+321") == "987(654+32)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "876+54") == "(876+54)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "876+54") == "(876+54)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123456+789") == "1(23456+789)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123456+789") == "1(23456+789)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "2000+1000") == "(2000+1)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "2000+1000") == "(2000+1)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "99999+11111") == "9(9999+1111)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "99999+11111") == "9(9999+1111)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "9876+543") == "(9876+543)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "9876+543") == "(9876+543)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "5000+6000") == "(5000+6)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "5000+6000") == "(5000+6)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "789+12") == "7(89+12)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "789+12") == "7(89+12)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1111+1111") == "1(111+111)1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1111+1111") == "1(111+111)1": {e}')
    
    total += 1
    try:
        result = candidate(expression = "700000+800000") == "(700000+8)00000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "700000+800000") == "(700000+8)00000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "55+5") == "5(5+5)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "55+5") == "5(5+5)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1+99999") == "(1+9999)9"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1+99999") == "(1+9999)9": {e}')
    
    total += 1
    try:
        result = candidate(expression = "11+22") == "1(1+2)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "11+22") == "1(1+2)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "321+654") == "(321+654)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "321+654") == "(321+654)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "55+66") == "(55+66)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "55+66") == "(55+66)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "56789+12") == "5(6789+12)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "56789+12") == "5(6789+12)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1000+2000") == "(1000+2)000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1000+2000") == "(1000+2)000": {e}')
    
    total += 1
    try:
        result = candidate(expression = "1234+5678") == "1(234+5678)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "1234+5678") == "1(234+5678)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "11111+22222") == "1(1111+2222)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "11111+22222") == "1(1111+2222)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "6+66") == "(6+6)6"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "6+66") == "(6+6)6": {e}')
    
    total += 1
    try:
        result = candidate(expression = "54321+6789") == "5(4321+6789)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "54321+6789") == "5(4321+6789)": {e}')
    
    total += 1
    try:
        result = candidate(expression = "123+456789") == "1(23+456)789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "123+456789") == "1(23+456)789": {e}')
    
    total += 1
    try:
        result = candidate(expression = "54+32") == "5(4+3)2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "54+32") == "5(4+3)2": {e}')
    
    total += 1
    try:
        result = candidate(expression = "21+89") == "(21+89)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "21+89") == "(21+89)": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(expression = "56+78") == "(56+78)"
    assert candidate(expression = "5+6") == "(5+6)"
    assert candidate(expression = "3+8") == "(3+8)"
    assert candidate(expression = "111+222") == "1(11+22)2"
    assert candidate(expression = "3+2") == "(3+2)"
    assert candidate(expression = "5+678") == "(5+67)8"
    assert candidate(expression = "247+38") == "2(47+38)"
    assert candidate(expression = "3+12") == "(3+1)2"
    assert candidate(expression = "11+11") == "1(1+1)1"
    assert candidate(expression = "8+9") == "(8+9)"
    assert candidate(expression = "1+2") == "(1+2)"
    assert candidate(expression = "123+456") == "1(23+45)6"
    assert candidate(expression = "9+9") == "(9+9)"
    assert candidate(expression = "12+34") == "1(2+3)4"
    assert candidate(expression = "88+11") == "8(8+1)1"
    assert candidate(expression = "999+999") == "(999+999)"
    assert candidate(expression = "1+9") == "(1+9)"
    assert candidate(expression = "333+444") == "(333+444)"
    assert candidate(expression = "555+666") == "(555+666)"
    assert candidate(expression = "9+99") == "(9+99)"
    assert candidate(expression = "9+1") == "(9+1)"
    assert candidate(expression = "5+9") == "(5+9)"
    assert candidate(expression = "1+1") == "(1+1)"
    assert candidate(expression = "10+1") == "1(0+1)"
    assert candidate(expression = "12+3") == "1(2+3)"
    assert candidate(expression = "555+555") == "(555+555)"
    assert candidate(expression = "123+4") == "1(23+4)"
    assert candidate(expression = "9+876") == "(9+87)6"
    assert candidate(expression = "12345+6789") == "1(2345+6789)"
    assert candidate(expression = "56+789") == "(56+789)"
    assert candidate(expression = "1111+2222") == "1(111+222)2"
    assert candidate(expression = "123+4567") == "1(23+456)7"
    assert candidate(expression = "6666+7777") == "(6666+7777)"
    assert candidate(expression = "9999+1") == "9(999+1)"
    assert candidate(expression = "12+345") == "1(2+34)5"
    assert candidate(expression = "567+89") == "(567+89)"
    assert candidate(expression = "8+7654") == "(8+765)4"
    assert candidate(expression = "987+654") == "(987+654)"
    assert candidate(expression = "33+44") == "(33+44)"
    assert candidate(expression = "1234+56789") == "1(234+5678)9"
    assert candidate(expression = "7000+8000") == "(7000+8)000"
    assert candidate(expression = "99+11") == "9(9+1)1"
    assert candidate(expression = "333+666") == "(333+666)"
    assert candidate(expression = "345+678") == "(345+678)"
    assert candidate(expression = "50+50") == "(50+5)0"
    assert candidate(expression = "123+45") == "1(23+45)"
    assert candidate(expression = "5+55") == "(5+5)5"
    assert candidate(expression = "678+9") == "6(78+9)"
    assert candidate(expression = "12+345678") == "1(2+34)5678"
    assert candidate(expression = "900000+100000") == "(900000+1)00000"
    assert candidate(expression = "10+20") == "(10+2)0"
    assert candidate(expression = "12+3456789") == "1(2+34)56789"
    assert candidate(expression = "123456+789012") == "1(23456+78901)2"
    assert candidate(expression = "99+88") == "(99+88)"
    assert candidate(expression = "56+7890") == "(56+789)0"
    assert candidate(expression = "9+1234") == "(9+123)4"
    assert candidate(expression = "55555+66666") == "(55555+66666)"
    assert candidate(expression = "1234+56") == "1(234+56)"
    assert candidate(expression = "678+90123") == "(678+9012)3"
    assert candidate(expression = "44+555") == "(44+55)5"
    assert candidate(expression = "9+87654321") == "(9+8765432)1"
    assert candidate(expression = "2222+3333") == "2(222+333)3"
    assert candidate(expression = "1+999") == "(1+99)9"
    assert candidate(expression = "9876+5432") == "(9876+5432)"
    assert candidate(expression = "4321+9") == "43(21+9)"
    assert candidate(expression = "5678+910") == "(5678+91)0"
    assert candidate(expression = "987654+321098") == "(987654+321098)"
    assert candidate(expression = "100000+200000") == "(100000+2)00000"
    assert candidate(expression = "3000+4000") == "(3000+4)000"
    assert candidate(expression = "300000+400000") == "(300000+4)00000"
    assert candidate(expression = "100+100") == "(100+1)00"
    assert candidate(expression = "10+999") == "1(0+9)99"
    assert candidate(expression = "500000+600000") == "(500000+6)00000"
    assert candidate(expression = "5432+1") == "543(2+1)"
    assert candidate(expression = "1+9999") == "(1+999)9"
    assert candidate(expression = "3456+789") == "3(456+789)"
    assert candidate(expression = "5555+666") == "5(555+666)"
    assert candidate(expression = "123+6") == "1(23+6)"
    assert candidate(expression = "8888+9999") == "(8888+9999)"
    assert candidate(expression = "213+456") == "(213+456)"
    assert candidate(expression = "23+4567") == "(23+456)7"
    assert candidate(expression = "100+200") == "(100+2)00"
    assert candidate(expression = "9+8765432") == "(9+876543)2"
    assert candidate(expression = "111+111") == "1(11+11)1"
    assert candidate(expression = "77777+88888") == "(77777+88888)"
    assert candidate(expression = "99+1") == "9(9+1)"
    assert candidate(expression = "3+9999") == "(3+999)9"
    assert candidate(expression = "234+567") == "(234+567)"
    assert candidate(expression = "2+9999") == "(2+999)9"
    assert candidate(expression = "4321+876") == "4(321+876)"
    assert candidate(expression = "9000+1000") == "(9000+1)000"
    assert candidate(expression = "11+111") == "1(1+11)1"
    assert candidate(expression = "5+6789") == "(5+678)9"
    assert candidate(expression = "1+23456") == "(1+2)3456"
    assert candidate(expression = "1098+231") == "1(098+23)1"
    assert candidate(expression = "999+1") == "9(99+1)"
    assert candidate(expression = "4444+5555") == "(4444+5555)"
    assert candidate(expression = "55+55") == "(55+55)"
    assert candidate(expression = "777+888") == "(777+888)"
    assert candidate(expression = "98765+4321") == "9(8765+432)1"
    assert candidate(expression = "654+321") == "6(54+32)1"
    assert candidate(expression = "77+88") == "(77+88)"
    assert candidate(expression = "33333+44444") == "(33333+44444)"
    assert candidate(expression = "222+333") == "2(22+33)3"
    assert candidate(expression = "2+987654321") == "(2+98765432)1"
    assert candidate(expression = "123+45678") == "1(23+4567)8"
    assert candidate(expression = "9+8765") == "(9+876)5"
    assert candidate(expression = "5678+123") == "5(678+123)"
    assert candidate(expression = "1234+567") == "1(234+567)"
    assert candidate(expression = "234+56789") == "(234+5678)9"
    assert candidate(expression = "987654+321") == "987(654+32)1"
    assert candidate(expression = "876+54") == "(876+54)"
    assert candidate(expression = "123456+789") == "1(23456+789)"
    assert candidate(expression = "2000+1000") == "(2000+1)000"
    assert candidate(expression = "99999+11111") == "9(9999+1111)1"
    assert candidate(expression = "9876+543") == "(9876+543)"
    assert candidate(expression = "5000+6000") == "(5000+6)000"
    assert candidate(expression = "789+12") == "7(89+12)"
    assert candidate(expression = "1111+1111") == "1(111+111)1"
    assert candidate(expression = "700000+800000") == "(700000+8)00000"
    assert candidate(expression = "55+5") == "5(5+5)"
    assert candidate(expression = "1+99999") == "(1+9999)9"
    assert candidate(expression = "11+22") == "1(1+2)2"
    assert candidate(expression = "321+654") == "(321+654)"
    assert candidate(expression = "55+66") == "(55+66)"
    assert candidate(expression = "56789+12") == "5(6789+12)"
    assert candidate(expression = "1000+2000") == "(1000+2)000"
    assert candidate(expression = "1234+5678") == "1(234+5678)"
    assert candidate(expression = "11111+22222") == "1(1111+2222)2"
    assert candidate(expression = "6+66") == "(6+6)6"
    assert candidate(expression = "54321+6789") == "5(4321+6789)"
    assert candidate(expression = "123+456789") == "1(23+456)789"
    assert candidate(expression = "54+32") == "5(4+3)2"
    assert candidate(expression = "21+89") == "(21+89)"


