def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s1 = "xyyy",s2 = "yxxx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyy",s2 = "yxxx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xx",s2 = "yy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xx",s2 = "yy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyy",s2 = "xyxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyy",s2 = "xyxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxyxyxx",s2 = "xyyxyxxxyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxyxyxx",s2 = "xyyxyxxxyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxyyy",s2 = "yyyxxx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxyyy",s2 = "yyyxxx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyx",s2 = "xxyy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyx",s2 = "xxyy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yx",s2 = "xy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yx",s2 = "xy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxx",s2 = "yyyy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxx",s2 = "yyyy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yxyy",s2 = "xyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yxyy",s2 = "xyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xx",s2 = "xy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xx",s2 = "xy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yy",s2 = "xx") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yy",s2 = "xx") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyx",s2 = "xyyx") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyx",s2 = "xyyx") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yyyy",s2 = "xxxx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yyyy",s2 = "xxxx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxy",s2 = "yxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxy",s2 = "yxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxx",s2 = "xyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxx",s2 = "xyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyx",s2 = "xyxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyx",s2 = "xyxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xy",s2 = "yx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xy",s2 = "yx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxy",s2 = "yxyxyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxy",s2 = "yxyxyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyx") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyx") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxxyxxyy",s2 = "yxyyxyyxxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxxyxxyy",s2 = "yxyyxyyxxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyyxy",s2 = "yxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyyxy",s2 = "yxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxx",s2 = "yyxxxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxx",s2 = "yyxxxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyyx",s2 = "yxyxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyyx",s2 = "yxyxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxy",s2 = "yxyxyxyxyxyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxy",s2 = "yxyxyxyxyxyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxyyyxx",s2 = "yyxxxyyy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxyyyxx",s2 = "yyxxxyyy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyyyxy",s2 = "yxyyxxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyyyxy",s2 = "yxyyxxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyxy") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyxy") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyyxxy",s2 = "yxyxyxyxyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyyxxy",s2 = "yxyxyxyxyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxyyyy",s2 = "yyyxxxx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxyyyy",s2 = "yyyxxxx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyyx",s2 = "yxyxyxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyyx",s2 = "yxyxyxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyyy",s2 = "yyxxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyyy",s2 = "yyxxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxyyyyy",s2 = "yyyyyyxxxx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxyyyyy",s2 = "yyyyyyxxxx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyy",s2 = "yyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyy",s2 = "yyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxxxy",s2 = "yyxxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxxxy",s2 = "yyxxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxyyyxy",s2 = "yyxxyxxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxyyyxy",s2 = "yyxxyxxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyx",s2 = "yxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyx",s2 = "yxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxyyx",s2 = "yyxyxxxy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxyyx",s2 = "yyxyxxxy") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxxy",s2 = "yyxyyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxxy",s2 = "yyxyyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxy",s2 = "yyxyxx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxy",s2 = "yyxyxx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxy",s2 = "yxyxyy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxy",s2 = "yxyxyy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyyxy",s2 = "yxyyyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyyxy",s2 = "yxyyyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyxyx",s2 = "yxyxyxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyxyx",s2 = "yxyxyxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxyxyx",s2 = "yyxyxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxyxyx",s2 = "yyxyxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxxyxy",s2 = "yxyxyxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxxyxy",s2 = "yxyxyxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyyxyx",s2 = "xyxyxyxyxy") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyyxyx",s2 = "xyxyxyxyxy") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxy",s2 = "yyyxxx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxy",s2 = "yyyxxx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxxxyyy",s2 = "yyxxyyxyxx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxxxyyy",s2 = "yyxxyyxyxx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxx",s2 = "yyyyyy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxx",s2 = "yyyyyy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyx") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyx") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxyyyy",s2 = "yyyyxxxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxyyyy",s2 = "yyyyxxxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyx",s2 = "xyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyx",s2 = "xyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxxxx",s2 = "yyyyyyyy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxxxx",s2 = "yyyyyyyy") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxxxxxx",s2 = "yyyyyyyyyy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxxxxxx",s2 = "yyyyyyyyyy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyyx") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyyx") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyy",s2 = "yxyxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyy",s2 = "yxyxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyx",s2 = "yxyxyxyy") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyx",s2 = "yxyxyxyy") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxxxyyx",s2 = "yxyxyxxyxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxxxyyx",s2 = "yxyxyxxyxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxxyyxx",s2 = "yyxyxxyyxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxxyyxx",s2 = "yyxyxxyyxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyx") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyx") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxy",s2 = "yxyxyxyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxy",s2 = "yxyxyxyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyy",s2 = "yyxx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyy",s2 = "yyxx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxyxyxyxyxy",s2 = "yyxyxyxyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxyxyxyxyxy",s2 = "yyxyxyxyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyy",s2 = "yxyyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyy",s2 = "yxyyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyyxxyyx",s2 = "yxyxyxyxyxyy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyyxxyyx",s2 = "yxyxyxyxyxyy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyx",s2 = "xyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyx",s2 = "xyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxyyy",s2 = "yyyyxxxx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxyyy",s2 = "yyyyxxxx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyyy",s2 = "yxyxyxyxxx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyyy",s2 = "yxyxyxyxxx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yyxyyyxxxyyy",s2 = "xyxxyyxyxxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yyxyyyxxxyyy",s2 = "xyxxyyxyxxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "yxyxyxyx",s2 = "xyxyxyxy") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "yxyxyxyx",s2 = "xyxyxyxy") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxyxyx",s2 = "xyxyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxyxyx",s2 = "xyxyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxyx",s2 = "yxxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxyx",s2 = "yxxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxxxxyy",s2 = "yyxxxxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxxxxyy",s2 = "yyxxxxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyx") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyx") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyxyyx",s2 = "yyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyxyyx",s2 = "yyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxxyyyxyyx",s2 = "yyxyyxyxxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxxyyyxyyx",s2 = "yyxyyxyxxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxxyxxyxyy",s2 = "yxyxyxyxyxyyxy") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxxyxxyxyy",s2 = "yxyxyxyxyxyyxy") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxx",s2 = "yyxyxyy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxx",s2 = "yyxyxyy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyxyx",s2 = "xyxyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyxyx",s2 = "xyxyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyyy",s2 = "yxyxyxxx") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyyy",s2 = "yxyxyxxx") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyxyx",s2 = "xyxxyxyxyx") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyxyx",s2 = "xyxxyxyxyx") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyx") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyx") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyx",s2 = "yyxyxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyx",s2 = "yyxyxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyyyy",s2 = "yyyxxx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyyyy",s2 = "yyyxxx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxyx",s2 = "xyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxyx",s2 = "xyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxyxyxyxyxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxyxyxyxyxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyxyxyy",s2 = "yyxyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyxyxyy",s2 = "yyxyxyxyyx") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyx") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyx") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xyxxxy",s2 = "yxyyxy") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xyxxxy",s2 = "yxyyxy") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s1 = "xxyxyyxy",s2 = "yyxyxyyx") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s1 = "xxyxyyxy",s2 = "yyxyxyyx") == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s1 = "xyyy",s2 = "yxxx") == 3
    assert candidate(s1 = "xx",s2 = "yy") == 1
    assert candidate(s1 = "xxyy",s2 = "xyxy") == 2
    assert candidate(s1 = "xxyyxyxyxx",s2 = "xyyxyxxxyx") == 4
    assert candidate(s1 = "xxxyyy",s2 = "yyyxxx") == 4
    assert candidate(s1 = "xyyx",s2 = "xxyy") == 2
    assert candidate(s1 = "yx",s2 = "xy") == 2
    assert candidate(s1 = "xxxx",s2 = "yyyy") == 2
    assert candidate(s1 = "yxyy",s2 = "xyyx") == -1
    assert candidate(s1 = "xx",s2 = "xy") == -1
    assert candidate(s1 = "yy",s2 = "xx") == 1
    assert candidate(s1 = "xyyx",s2 = "xyyx") == 0
    assert candidate(s1 = "yyyy",s2 = "xxxx") == 2
    assert candidate(s1 = "xyxy",s2 = "yxyx") == 2
    assert candidate(s1 = "xyxx",s2 = "xyyx") == -1
    assert candidate(s1 = "xxyx",s2 = "xyxy") == -1
    assert candidate(s1 = "xy",s2 = "yx") == 2
    assert candidate(s1 = "xyxyxy",s2 = "yxyxyx") == 4
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyx") == 14
    assert candidate(s1 = "xyxxxyxxyy",s2 = "yxyyxyyxxy") == 3
    assert candidate(s1 = "xyyyxy",s2 = "yxyxyx") == -1
    assert candidate(s1 = "xxyyxx",s2 = "yyxxxy") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 16
    assert candidate(s1 = "xyxyyx",s2 = "yxyxyx") == 2
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 14
    assert candidate(s1 = "xyxyxyxyxyxy",s2 = "yxyxyxyxyxyx") == 6
    assert candidate(s1 = "xxxyyyxx",s2 = "yyxxxyyy") == 3
    assert candidate(s1 = "xyyxxyyyxy",s2 = "yxyyxxyxyx") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20
    assert candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyxy") == 6
    assert candidate(s1 = "xyyxxyyxxy",s2 = "yxyxyxyxyx") == 4
    assert candidate(s1 = "xxxyyyy",s2 = "yyyxxxx") == -1
    assert candidate(s1 = "xyyxxyyx",s2 = "yxyxyxyx") == 2
    assert candidate(s1 = "xxyyyy",s2 = "yyxxyx") == -1
    assert candidate(s1 = "xxxxxyyyyy",s2 = "yyyyyyxxxx") == -1
    assert candidate(s1 = "xxyxyxyy",s2 = "yyxyxyyx") == -1
    assert candidate(s1 = "xyxyxxxy",s2 = "yyxxyxyx") == -1
    assert candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyy") == 3
    assert candidate(s1 = "xxxyyyxy",s2 = "yyxxyxxy") == 2
    assert candidate(s1 = "xyyx",s2 = "yxyx") == 2
    assert candidate(s1 = "xxyyxyyx",s2 = "yyxyxxxy") == 4
    assert candidate(s1 = "xxyxxy",s2 = "yyxyyx") == 3
    assert candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyy") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyx") == 8
    assert candidate(s1 = "xxyyxy",s2 = "yyxyxx") == 2
    assert candidate(s1 = "xyxyxy",s2 = "yxyxyy") == -1
    assert candidate(s1 = "xyxxyyxy",s2 = "yxyyyxyx") == -1
    assert candidate(s1 = "xxyxyxyxyx",s2 = "yxyxyxyxyx") == -1
    assert candidate(s1 = "xxyyxyxyx",s2 = "yyxyxyxyx") == -1
    assert candidate(s1 = "yxyxyxyxyx",s2 = "xyxyxyxyyx") == 4
    assert candidate(s1 = "xyxxyxxyxy",s2 = "yxyxyxyxyx") == -1
    assert candidate(s1 = "xyxyxyyxyx",s2 = "xyxyxyxyxy") == 2
    assert candidate(s1 = "xxxxxy",s2 = "yyyxxx") == 3
    assert candidate(s1 = "xxyyxxxyyy",s2 = "yyxxyyxyxx") == 4
    assert candidate(s1 = "xxxxxx",s2 = "yyyyyy") == 3
    assert candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyx") == 6
    assert candidate(s1 = "xxxxxyyyy",s2 = "yyyyxxxyx") == -1
    assert candidate(s1 = "xxyx",s2 = "xyyx") == -1
    assert candidate(s1 = "xxxxxxxx",s2 = "yyyyyyyy") == 4
    assert candidate(s1 = "xxxxxxxxxx",s2 = "yyyyyyyyyy") == 5
    assert candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyyx") == 3
    assert candidate(s1 = "xyxxyy",s2 = "yxyxyx") == 2
    assert candidate(s1 = "xxyxyxyx",s2 = "yxyxyxyy") == 1
    assert candidate(s1 = "xyxyxxxyyx",s2 = "yxyxyxxyxy") == -1
    assert candidate(s1 = "xxyyxxyyxx",s2 = "yyxyxxyyxy") == 3
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyx") == 10
    assert candidate(s1 = "xyxyxyxy",s2 = "yxyxyxyx") == 4
    assert candidate(s1 = "xxyy",s2 = "yyxx") == 2
    assert candidate(s1 = "xxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyyx") == -1
    assert candidate(s1 = "xxyyxyxyxyxyxy",s2 = "yyxyxyxyxyxyyx") == -1
    assert candidate(s1 = "xyxyy",s2 = "yxyyx") == 2
    assert candidate(s1 = "xyyxxyyxxyyx",s2 = "yxyxyxyxyxyy") == -1
    assert candidate(s1 = "xxyxyxyx",s2 = "xyxyxyyx") == -1
    assert candidate(s1 = "xxxxxyyy",s2 = "yyyyxxxx") == -1
    assert candidate(s1 = "xyxyxyxyyy",s2 = "yxyxyxyxxx") == 5
    assert candidate(s1 = "yyxyyyxxxyyy",s2 = "xyxxyyxyxxyx") == -1
    assert candidate(s1 = "yxyxyxyx",s2 = "xyxyxyxy") == 4
    assert candidate(s1 = "xyxxyxyxyx",s2 = "xyxyxyxyyx") == -1
    assert candidate(s1 = "xyxxyxyx",s2 = "yxxyxyyx") == -1
    assert candidate(s1 = "xxxxxxyy",s2 = "yyxxxxyx") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyx") == 12
    assert candidate(s1 = "xxyyxyyx",s2 = "yyxyxyyx") == -1
    assert candidate(s1 = "xxxyyyxyyx",s2 = "yyxyyxyxxy") == -1
    assert candidate(s1 = "xxyxxyxyxy",s2 = "yxyxyxyxyx") == -1
    assert candidate(s1 = "xyxxyxxyxxyxyy",s2 = "yxyxyxyxyxyyxy") == 5
    assert candidate(s1 = "xxyxyxx",s2 = "yyxyxyy") == -1
    assert candidate(s1 = "xxyxyxyxyx",s2 = "xyxyxyxyyx") == -1
    assert candidate(s1 = "xyxyxyyy",s2 = "yxyxyxxx") == 5
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18
    assert candidate(s1 = "xxyxyxyxyx",s2 = "xyxxyxyxyx") == 2
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 18
    assert candidate(s1 = "xyyxxyxyxy",s2 = "yxyxyxyxyx") == 4
    assert candidate(s1 = "xxyxyx",s2 = "yyxyxy") == 3
    assert candidate(s1 = "xxyyyy",s2 = "yyyxxx") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyx") == 20
    assert candidate(s1 = "xyxxyxyx",s2 = "xyxyxyyx") == -1
    assert candidate(s1 = "xyxyxyxyxy",s2 = "yxyxyxyxyy") == -1
    assert candidate(s1 = "xyxxyxxyx",s2 = "yxyxyxyxy") == 3
    assert candidate(s1 = "xyxxyxyxyxyxyxyxyxyxyxyxyxyx",s2 = "xyxyxyxyxyxyxyxyxyxyxyxyxyxy") == -1
    assert candidate(s1 = "xxyxyxyxyy",s2 = "yyxyxyxyyx") == -1
    assert candidate(s1 = "xyxyxyxyxyxyxyxy",s2 = "yxyxyxyxyxyxyxyx") == 8
    assert candidate(s1 = "xyxxxy",s2 = "yxyyxy") == 3
    assert candidate(s1 = "xxyxyyxy",s2 = "yyxyxyyx") == -1


