def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTFFFF",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTFFFF",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFF",k = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFF",k = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTFFTFT",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTFFTFT",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTF",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTF",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTFFT",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTFFT",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTTFFTTFF",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTTFFTTFF",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTFFTFF",k = 2) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTFFTFF",k = 2) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTF",k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTF",k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "T",k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "T",k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTFFTFF",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTFFTFF",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFF",k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFF",k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTF",k = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTF",k = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFT",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFT",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTTFTT",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTTFTT",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TF TFT TFTF",k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TF TFT TFTF",k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFF",k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFF",k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFT",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFT",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFT",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFT",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTFFT",k = 1) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTFFT",k = 1) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTFTTTTT",k = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTFTTTTT",k = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTT",k = 0) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTT",k = 0) == 6: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTT",k = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTT",k = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTT",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTT",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTFFTFFT",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTFFTFFT",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFFTFFT",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFFTFFT",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTT",k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTT",k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFT",k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFT",k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFF",k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFF",k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFF",k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFF",k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFF",k = 0) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFF",k = 0) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFFFF",k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFFFF",k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 38: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFF",k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFF",k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 8) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 8) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 43: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 25) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 25) == 51: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFTFTFTFTFTFTFTFT",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFTFTFTFTFTFTFTFT",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 24: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFFTFTF",k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFFTFTF",k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFFFFFFFFTTTTTTTTTT",k = 6) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFFFFFFFFTTTTTTTTTT",k = 6) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFT",k = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFT",k = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 8) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 8) == 17: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 21) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 21) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 32: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTTTT",k = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTTTT",k = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFT",k = 7) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFT",k = 7) == 23: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFTTTTTTTTT",k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFTTTTTTTTT",k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTTFTTFTTFFTFTTFFT",k = 11) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTTFTTFTTFFTFTTFFT",k = 11) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTTFFFFFFFFTTTTTTTTT",k = 9) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTTFFFFFFFFTTTTTTTTT",k = 9) == 25: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTF",k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTF",k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 10) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 10) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTTTTTTFT",k = 2) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTTTTTTFT",k = 2) == 13: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 0) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 0) == 44: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFFFFTTTFFTFTFFF",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFFFFTTTFFTFTFFF",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 41: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTTTFTTFTTFTTFTTFT",k = 7) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTTTFTTFTTFTTFTTFT",k = 7) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTF",k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTF",k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFTTTFFFFTTTTFF",k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFTTTFFFFTTTTFF",k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFFFFFFFTTTTTTTTTTTTFFFFFFF",k = 8) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFFFFFFFTTTTTTTTTTTTFFFFFFF",k = 8) == 22: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFFFTTTFFFTTTFFF",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFFFTTTFFFTTTFFF",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFTTTTTTTTTTTTTT",k = 10) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFTTTTTTTTTTTTTT",k = 10) == 23: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFT",k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFT",k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFTFTFTFT",k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFTFTFTFT",k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTTFFTTFFTTFFTTFF",k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTTFFTTFFTTFFTTFF",k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTFFFFFFFFFFFFTTTTTTTTTTTT",k = 15) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTFFFFFFFFFFFFTTTTTTTTTTTT",k = 15) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFT",k = 12) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFT",k = 12) == 22: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTFFFFFFFFFFFFFFFFF",k = 11) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTFFFFFFFFFFFFFFFFF",k = 11) == 27: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFFTFFTFFTFFTFFTFF",k = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFFTFFTFFTFFTFFTFF",k = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFTTTTT",k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFTTTTT",k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFTFTFFTTFTFT",k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFTFTFFTTFTFT",k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFTFTFTFTFTFTF",k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFTFTFTFTFTFTF",k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTT",k = 15) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTT",k = 15) == 17: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTFTFTFTFFTFTFTFT",k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTFTFTFTFFTFTFTFT",k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTFFFFF",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTFFFFF",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTT",k = 8) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTT",k = 8) == 38: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTTTTTT",k = 12) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTTTTTT",k = 12) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTFFTFFTFFFF",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTFFTFFTFFFF",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTFFTTFFTT",k = 5) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTFFTTFFTT",k = 5) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFFFFTTTFFFFTTTFFFFTTT",k = 6) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFFFFTTTFFFFTTTFFFFTTT",k = 6) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFTTFFTFFTFFTT",k = 7) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFTTFFTFFTFFTT",k = 7) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTTFFFTTF",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTTFFFTTF",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFF",k = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFF",k = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTTTFTFTFTFTFFTFTF",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTTTFTFTFTFTFFTFTF",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTFFFFFFFFFF",k = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTFFFFFFFFFF",k = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 36: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFFFFTTTTFTTTFFTTT",k = 7) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFFFFTTTTFTTTFFTTT",k = 7) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFTFTFTFTFTFTFT",k = 8) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFTFTFTFTFTFTFT",k = 8) == 17: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFFTFTFTFTFFFT",k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFFTFTFTFTFFFT",k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 38: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 25) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 25) == 32: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 31: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 20) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 20) == 41: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTFFTTTTFFTT",k = 4) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTFFTTTTFFTT",k = 4) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 0) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 0) == 48: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTFTFFTFTFFTFTFFTFT",k = 5) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTFTFFTFTFFTFTFFTFT",k = 5) == 14: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFFFFFFFFFFFFFFFFT",k = 3) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFFFFFFFFFFFFFFFFT",k = 3) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTFFTFFTFFTFF",k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTFFTFFTFFTFF",k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFTTTTTTTTFFFFFFFFTTTTTTTT",k = 8) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFTTTTTTTTFFFFFFFFTTTTTTTT",k = 8) == 24: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTFTTTTTFTTTTTFTTTTT",k = 7) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTFTTTTTFTTTTTFTTTTT",k = 7) == 24: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFFFFFFTTTTTTTTTT",k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFFFFFFTTTTTTTTTT",k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 15) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 15) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 25) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 25) == 30: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTTFTTFTTFFTFTTFFTFFTFTTFTT",k = 22) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTTFTTFTTFFTFTTFFTFFTFTTFTT",k = 22) == 27: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFFFFFFFFFFFFFFFFF",k = 10) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFFFFFFFFFFFFFFFFF",k = 10) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 18) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 18) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 10) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 10) == 21: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTT",k = 15) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTT",k = 15) == 22: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFTTFFTFFTFFTFFT",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFTTFFTFFTFFTFFT",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTFFFFF",k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTFFFFF",k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTFFFTTTFFFTTTFFFTTTFFFTTTFFTFTFFTT",k = 15) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTFFFTTTFFFTTTFFFTTTFFFTTTFFTFTFFTT",k = 15) == 32: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTTFFTTFFTTFFTT",k = 9) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTTFFTTFFTTFFTT",k = 9) == 19: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTTTTTFTFTFT",k = 6) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTTTTTFTFTFT",k = 6) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFF",k = 15) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFF",k = 15) == 17: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFT",k = 8) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFT",k = 8) == 17: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 12) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 12) == 28: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTFFTTFFTTFF",k = 4) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTFFTTFFTTFF",k = 4) == 12: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 25: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFFFFFFTTTTTTTT",k = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFFFFFFTTTTTTTT",k = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTT",k = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTT",k = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFT",k = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFT",k = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 29: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 24) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 24) == 32: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTTTTTTTTTTTTTTTTT",k = 1) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTTTTTTTTTTTTTTTTT",k = 1) == 20: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFFTFTFFTFFTFTFFTFFTFFTTFFTFTFFTFFTFFTFFTFTFFTFF",k = 6) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFFTFTFFTFFTFTFFTFFTFFTTFFTFTFFTFFTFFTFFTFTFFTFF",k = 6) == 19: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 24: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFF",k = 15) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFF",k = 15) == 24: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(answerKey = "TTTTFFFF",k = 2) == 6
    assert candidate(answerKey = "FFFFFF",k = 3) == 6
    assert candidate(answerKey = "TFFTFFTFFTFT",k = 3) == 10
    assert candidate(answerKey = "TFTFTFTF",k = 2) == 5
    assert candidate(answerKey = "FFTFFT",k = 2) == 6
    assert candidate(answerKey = "FFTTFFTTFF",k = 5) == 10
    assert candidate(answerKey = "FFTFFTFF",k = 2) == 8
    assert candidate(answerKey = "TFTFTFTFTF",k = 4) == 9
    assert candidate(answerKey = "T",k = 1) == 1
    assert candidate(answerKey = "FFTFFTFF",k = 3) == 8
    assert candidate(answerKey = "TTFF",k = 2) == 4
    assert candidate(answerKey = "TFTFTFTF",k = 4) == 8
    assert candidate(answerKey = "FTFTFTFT",k = 2) == 5
    assert candidate(answerKey = "TTFTTFTT",k = 1) == 5
    assert candidate(answerKey = "TF TFT TFTF",k = 3) == 10
    assert candidate(answerKey = "FFFFFFFF",k = 5) == 8
    assert candidate(answerKey = "FFFFFFT",k = 2) == 7
    assert candidate(answerKey = "FTFTFTFTFTFT",k = 5) == 11
    assert candidate(answerKey = "TTTTFFT",k = 1) == 5
    assert candidate(answerKey = "TTTTTTFTTTTT",k = 2) == 12
    assert candidate(answerKey = "TTTTTT",k = 0) == 6
    assert candidate(answerKey = "TTTTT",k = 0) == 5
    assert candidate(answerKey = "TFFTFFTT",k = 3) == 7
    assert candidate(answerKey = "TTTTFFTFFT",k = 3) == 8
    assert candidate(answerKey = "FTFFTFFT",k = 3) == 8
    assert candidate(answerKey = "TTTTTTTT",k = 3) == 8
    assert candidate(answerKey = "TFFT",k = 1) == 3
    assert candidate(answerKey = "FFFFFFF",k = 3) == 7
    assert candidate(answerKey = "FFFFF",k = 3) == 5
    assert candidate(answerKey = "FFFFF",k = 0) == 5
    assert candidate(answerKey = "TFFFFF",k = 2) == 6
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 38
    assert candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 4) == 9
    assert candidate(answerKey = "FFFFFFFFFFFFFFFF",k = 10) == 16
    assert candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 8) == 16
    assert candidate(answerKey = "TTTTTTTFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 43
    assert candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 5) == 16
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 25) == 51
    assert candidate(answerKey = "TFFTFTFTFTFTFTFTFTFT",k = 10) == 20
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTT",k = 15) == 24
    assert candidate(answerKey = "TTFTFTFFTFTF",k = 4) == 10
    assert candidate(answerKey = "TFFFFFFFFFTTTTTTTTTT",k = 6) == 16
    assert candidate(answerKey = "TTFTFTFTFT",k = 4) == 10
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 8) == 17
    assert candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 21) == 28
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 10) == 20
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 32
    assert candidate(answerKey = "FFFFFFFFTTTTTTTT",k = 5) == 13
    assert candidate(answerKey = "TFFTFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFFTFT",k = 7) == 23
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 28
    assert candidate(answerKey = "FFFFFFFFFTTTTTTTTT",k = 5) == 14
    assert candidate(answerKey = "FTTFTTFTTFFTFTTFFT",k = 11) == 18
    assert candidate(answerKey = "FFFFFFFFTTTTTTFFFFFFFFTTTTTTTTT",k = 9) == 25
    assert candidate(answerKey = "TFTFTFTFTFTFTFTF",k = 10) == 16
    assert candidate(answerKey = "TTTTTTTTTTTTTTTT",k = 10) == 16
    assert candidate(answerKey = "FFFFFFFFTTTTTTTTTTFT",k = 2) == 13
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 0) == 44
    assert candidate(answerKey = "TTTFFFFTTTFFTFTFFF",k = 3) == 9
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 41
    assert candidate(answerKey = "FTTTFTTFTTFTTFTTFT",k = 7) == 18
    assert candidate(answerKey = "TFTFTFTFTF",k = 5) == 10
    assert candidate(answerKey = "FFFTTTFFFFTTTTFF",k = 5) == 12
    assert candidate(answerKey = "TTFFFFFFFFTTTTTTTTTTTTFFFFFFF",k = 8) == 22
    assert candidate(answerKey = "TTTFFFTTTFFFTTTFFF",k = 5) == 11
    assert candidate(answerKey = "FFFFFFFFFTTTTTTTTTTTTTT",k = 10) == 23
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFT",k = 2) == 5
    assert candidate(answerKey = "TTFTFTFTFTFTFTFT",k = 5) == 12
    assert candidate(answerKey = "FFTTFFTTFFTTFFTTFF",k = 10) == 18
    assert candidate(answerKey = "TTTTFFFFFFFFFFFFTTTTTTTTTTTT",k = 15) == 28
    assert candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFT",k = 12) == 22
    assert candidate(answerKey = "TTTTTTTTTTFFFFFFFFFFFFFFFFF",k = 11) == 27
    assert candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 5) == 14
    assert candidate(answerKey = "FTFFTFFTFFTFFTFFTFF",k = 10) == 19
    assert candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 7) == 16
    assert candidate(answerKey = "FFFFFFFFFTTTTT",k = 5) == 14
    assert candidate(answerKey = "TFFTFTFTFFTTFTFT",k = 3) == 9
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 6) == 13
    assert candidate(answerKey = "TTTFTFTFTFTFTFTF",k = 6) == 15
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTT",k = 15) == 17
    assert candidate(answerKey = "FFTFTFTFTFFTFTFTFT",k = 6) == 15
    assert candidate(answerKey = "FFFFFFFFTTTTTFFFFF",k = 4) == 12
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTT",k = 8) == 38
    assert candidate(answerKey = "FFFFFFFFTTTTTTTTTT",k = 12) == 18
    assert candidate(answerKey = "TTTTTTFFTFFTFFFF",k = 4) == 12
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTF",k = 9) == 18
    assert candidate(answerKey = "TTTTTTTTTTFFTTFFTT",k = 5) == 18
    assert candidate(answerKey = "TTTFFFFTTTFFFFTTTFFFFTTT",k = 6) == 18
    assert candidate(answerKey = "TTFFTTFFTFFTFFTT",k = 7) == 15
    assert candidate(answerKey = "FFTTFFFTTF",k = 2) == 7
    assert candidate(answerKey = "FFFFFFFF",k = 0) == 8
    assert candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 6) == 15
    assert candidate(answerKey = "TTFTTTFTFTFTFTFFTFTF",k = 4) == 12
    assert candidate(answerKey = "TTTTTTTTTTFFFFFFFFFF",k = 8) == 18
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 36
    assert candidate(answerKey = "TTTFFFFTTTTFTTTFFTTT",k = 7) == 20
    assert candidate(answerKey = "TFFTFTFTFTFTFTFTFT",k = 8) == 17
    assert candidate(answerKey = "TTFFFTFTFTFTFFFT",k = 6) == 15
    assert candidate(answerKey = "FTFTFTFTFTFTFTFT",k = 5) == 11
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 20) == 38
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 25) == 32
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 31
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 20) == 41
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFT",k = 9) == 18
    assert candidate(answerKey = "TTTTTFFTTTTFFTT",k = 4) == 15
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 15) == 28
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 0) == 48
    assert candidate(answerKey = "FFTFTFFTFTFFTFTFFTFT",k = 5) == 14
    assert candidate(answerKey = "TTFFFFFFFFFFFFFFFFFT",k = 3) == 20
    assert candidate(answerKey = "TFFTFFTFFTFFTFFTFF",k = 10) == 18
    assert candidate(answerKey = "FFFFFFFFTTTTTTTTFFFFFFFFTTTTTTTT",k = 8) == 24
    assert candidate(answerKey = "TTTTTTFTTTTTFTTTTTFTTTTT",k = 7) == 24
    assert candidate(answerKey = "TFFFFFFFTTTTTTTTTT",k = 10) == 18
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTFTF",k = 15) == 20
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 25) == 30
    assert candidate(answerKey = "FTTFTTFTTFFTFTTFFTFFTFTTFTT",k = 22) == 27
    assert candidate(answerKey = "TTFFFFFFFFFFFFFFFFFF",k = 10) == 20
    assert candidate(answerKey = "FFFFFFFFFTTTTTTT",k = 7) == 16
    assert candidate(answerKey = "TFTFTFTFTFTFTFTFTFTFTFTFTFTF",k = 18) == 28
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 10) == 21
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTT",k = 15) == 22
    assert candidate(answerKey = "FFTTFFTFFTFFTFFT",k = 4) == 12
    assert candidate(answerKey = "TTTTTFFFFF",k = 2) == 7
    assert candidate(answerKey = "TTTFFFTTTFFFTTTFFFTTTFFFTTTFFTFTFFTT",k = 15) == 32
    assert candidate(answerKey = "TFFTFFTTFFTTFFTTFFTT",k = 9) == 19
    assert candidate(answerKey = "FTFTFTTTTTFTFTFT",k = 6) == 16
    assert candidate(answerKey = "TTTTTTTTTTTTTTTTTTTTTTTTTTTT",k = 20) == 28
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFF",k = 15) == 17
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFT",k = 8) == 17
    assert candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFTFFTFFT",k = 12) == 28
    assert candidate(answerKey = "TTTTFFTTFFTTFF",k = 4) == 12
    assert candidate(answerKey = "FTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 25
    assert candidate(answerKey = "TFFFFFFFTTTTTTTT",k = 7) == 16
    assert candidate(answerKey = "TTTTTTTTTT",k = 0) == 10
    assert candidate(answerKey = "TFFTFFTFFTFFTFFTFFTFFT",k = 7) == 21
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFF",k = 20) == 29
    assert candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFTFTFTFTFT",k = 24) == 32
    assert candidate(answerKey = "TTFTTTTTTTTTTTTTTTTT",k = 1) == 20
    assert candidate(answerKey = "TTFFTFTFFTFFTFTFFTFFTFFTTFFTFTFFTFFTFFTFFTFTFFTFF",k = 6) == 19
    assert candidate(answerKey = "TTFTFTFTFTFTFTFTFTFTFTFT",k = 12) == 24
    assert candidate(answerKey = "TTTTTTTTTFFFFFFF",k = 6) == 15
    assert candidate(answerKey = "FFFFFFFFFFFFFFFFFFFFFFFF",k = 15) == 24


