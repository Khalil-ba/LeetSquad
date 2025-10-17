def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(buckets = 4,minutesToDie = 15,minutesToTest = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 4,minutesToDie = 15,minutesToTest = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1,minutesToDie = 1,minutesToTest = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1,minutesToDie = 1,minutesToTest = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 4,minutesToDie = 15,minutesToTest = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 4,minutesToDie = 15,minutesToTest = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1,minutesToDie = 10,minutesToTest = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1,minutesToDie = 10,minutesToTest = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 8,minutesToDie = 10,minutesToTest = 40) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 8,minutesToDie = 10,minutesToTest = 40) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 10,minutesToDie = 5,minutesToTest = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 10,minutesToDie = 5,minutesToTest = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1,minutesToDie = 10,minutesToTest = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1,minutesToDie = 10,minutesToTest = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 10,minutesToDie = 5,minutesToTest = 20) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 10,minutesToDie = 5,minutesToTest = 20) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 100,minutesToDie = 10,minutesToTest = 60) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 100,minutesToDie = 10,minutesToTest = 60) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 10,minutesToDie = 5,minutesToTest = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 10,minutesToDie = 5,minutesToTest = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 8,minutesToDie = 10,minutesToTest = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 8,minutesToDie = 10,minutesToTest = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1024,minutesToDie = 1,minutesToTest = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1024,minutesToDie = 1,minutesToTest = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 9,minutesToDie = 25,minutesToTest = 75) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 9,minutesToDie = 25,minutesToTest = 75) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 27,minutesToDie = 3,minutesToTest = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 27,minutesToDie = 3,minutesToTest = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 500,minutesToDie = 5,minutesToTest = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 500,minutesToDie = 5,minutesToTest = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 2,minutesToTest = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 2,minutesToTest = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 250,minutesToDie = 25,minutesToTest = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 250,minutesToDie = 25,minutesToTest = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 625,minutesToDie = 20,minutesToTest = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 625,minutesToDie = 20,minutesToTest = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 625,minutesToDie = 10,minutesToTest = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 625,minutesToDie = 10,minutesToTest = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 3125,minutesToDie = 5,minutesToTest = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 3125,minutesToDie = 5,minutesToTest = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 999,minutesToDie = 1,minutesToTest = 99) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 999,minutesToDie = 1,minutesToTest = 99) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 243,minutesToDie = 1,minutesToTest = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 243,minutesToDie = 1,minutesToTest = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1296,minutesToDie = 6,minutesToTest = 18) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1296,minutesToDie = 6,minutesToTest = 18) == 6: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 243,minutesToDie = 18,minutesToTest = 90) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 243,minutesToDie = 18,minutesToTest = 90) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 729,minutesToDie = 3,minutesToTest = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 729,minutesToDie = 3,minutesToTest = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 512,minutesToDie = 5,minutesToTest = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 512,minutesToDie = 5,minutesToTest = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 64,minutesToDie = 4,minutesToTest = 16) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 64,minutesToDie = 4,minutesToTest = 16) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 5,minutesToTest = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 5,minutesToTest = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 350,minutesToDie = 7,minutesToTest = 35) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 350,minutesToDie = 7,minutesToTest = 35) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 500,minutesToDie = 20,minutesToTest = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 500,minutesToDie = 20,minutesToTest = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 343,minutesToDie = 7,minutesToTest = 21) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 343,minutesToDie = 7,minutesToTest = 21) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 128,minutesToDie = 8,minutesToTest = 32) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 128,minutesToDie = 8,minutesToTest = 32) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 64,minutesToDie = 2,minutesToTest = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 64,minutesToDie = 2,minutesToTest = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 9,minutesToTest = 27) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 9,minutesToTest = 27) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 125,minutesToDie = 25,minutesToTest = 125) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 125,minutesToDie = 25,minutesToTest = 125) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 450,minutesToDie = 12,minutesToTest = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 450,minutesToDie = 12,minutesToTest = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 441,minutesToDie = 20,minutesToTest = 60) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 441,minutesToDie = 20,minutesToTest = 60) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 3125,minutesToDie = 15,minutesToTest = 60) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 3125,minutesToDie = 15,minutesToTest = 60) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 512,minutesToDie = 15,minutesToTest = 30) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 512,minutesToDie = 15,minutesToTest = 30) == 6: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 729,minutesToDie = 9,minutesToTest = 27) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 729,minutesToDie = 9,minutesToTest = 27) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 216,minutesToDie = 10,minutesToTest = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 216,minutesToDie = 10,minutesToTest = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 27,minutesToDie = 1,minutesToTest = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 27,minutesToDie = 1,minutesToTest = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 243,minutesToDie = 9,minutesToTest = 27) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 243,minutesToDie = 9,minutesToTest = 27) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1024,minutesToDie = 4,minutesToTest = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1024,minutesToDie = 4,minutesToTest = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 512,minutesToDie = 5,minutesToTest = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 512,minutesToDie = 5,minutesToTest = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 30,minutesToTest = 90) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 30,minutesToTest = 90) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 512,minutesToDie = 2,minutesToTest = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 512,minutesToDie = 2,minutesToTest = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 128,minutesToDie = 15,minutesToTest = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 128,minutesToDie = 15,minutesToTest = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 300,minutesToDie = 3,minutesToTest = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 300,minutesToDie = 3,minutesToTest = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 999,minutesToDie = 2,minutesToTest = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 999,minutesToDie = 2,minutesToTest = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 999,minutesToDie = 1,minutesToTest = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 999,minutesToDie = 1,minutesToTest = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 16,minutesToDie = 4,minutesToTest = 16) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 16,minutesToDie = 4,minutesToTest = 16) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 343,minutesToDie = 7,minutesToTest = 42) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 343,minutesToDie = 7,minutesToTest = 42) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 343,minutesToDie = 2,minutesToTest = 14) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 343,minutesToDie = 2,minutesToTest = 14) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 125,minutesToDie = 5,minutesToTest = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 125,minutesToDie = 5,minutesToTest = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 9,minutesToDie = 3,minutesToTest = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 9,minutesToDie = 3,minutesToTest = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 600,minutesToDie = 10,minutesToTest = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 600,minutesToDie = 10,minutesToTest = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 750,minutesToDie = 20,minutesToTest = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 750,minutesToDie = 20,minutesToTest = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 216,minutesToDie = 6,minutesToTest = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 216,minutesToDie = 6,minutesToTest = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 961,minutesToDie = 30,minutesToTest = 90) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 961,minutesToDie = 30,minutesToTest = 90) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 125,minutesToDie = 10,minutesToTest = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 125,minutesToDie = 10,minutesToTest = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 15,minutesToTest = 75) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 15,minutesToTest = 75) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 800,minutesToDie = 15,minutesToTest = 75) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 800,minutesToDie = 15,minutesToTest = 75) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 729,minutesToDie = 10,minutesToTest = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 729,minutesToDie = 10,minutesToTest = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 750,minutesToDie = 15,minutesToTest = 45) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 750,minutesToDie = 15,minutesToTest = 45) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 100,minutesToDie = 1,minutesToTest = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 100,minutesToDie = 1,minutesToTest = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 500,minutesToDie = 5,minutesToTest = 30) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 500,minutesToDie = 5,minutesToTest = 30) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 500,minutesToDie = 5,minutesToTest = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 500,minutesToDie = 5,minutesToTest = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1024,minutesToDie = 10,minutesToTest = 40) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1024,minutesToDie = 10,minutesToTest = 40) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 9,minutesToDie = 3,minutesToTest = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 9,minutesToDie = 3,minutesToTest = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 27,minutesToDie = 6,minutesToTest = 18) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 27,minutesToDie = 6,minutesToTest = 18) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 27,minutesToDie = 5,minutesToTest = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 27,minutesToDie = 5,minutesToTest = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 10,minutesToTest = 40) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 10,minutesToTest = 40) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 4,minutesToTest = 16) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 4,minutesToTest = 16) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 441,minutesToDie = 7,minutesToTest = 49) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 441,minutesToDie = 7,minutesToTest = 49) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 441,minutesToDie = 14,minutesToTest = 70) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 441,minutesToDie = 14,minutesToTest = 70) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 64,minutesToDie = 20,minutesToTest = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 64,minutesToDie = 20,minutesToTest = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 1,minutesToTest = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 1,minutesToTest = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 999,minutesToDie = 2,minutesToTest = 4) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 999,minutesToDie = 2,minutesToTest = 4) == 7: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 10,minutesToTest = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 10,minutesToTest = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 64,minutesToDie = 1,minutesToTest = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 64,minutesToDie = 1,minutesToTest = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 128,minutesToDie = 2,minutesToTest = 16) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 128,minutesToDie = 2,minutesToTest = 16) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 999,minutesToDie = 2,minutesToTest = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 999,minutesToDie = 2,minutesToTest = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 1024,minutesToDie = 8,minutesToTest = 32) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 1024,minutesToDie = 8,minutesToTest = 32) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 3,minutesToTest = 9) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 3,minutesToTest = 9) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 81,minutesToDie = 5,minutesToTest = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 81,minutesToDie = 5,minutesToTest = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 125,minutesToDie = 5,minutesToTest = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 125,minutesToDie = 5,minutesToTest = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 961,minutesToDie = 6,minutesToTest = 36) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 961,minutesToDie = 6,minutesToTest = 36) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 729,minutesToDie = 1,minutesToTest = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 729,minutesToDie = 1,minutesToTest = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 169,minutesToDie = 13,minutesToTest = 39) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 169,minutesToDie = 13,minutesToTest = 39) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 750,minutesToDie = 10,minutesToTest = 50) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 750,minutesToDie = 10,minutesToTest = 50) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 625,minutesToDie = 10,minutesToTest = 40) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 625,minutesToDie = 10,minutesToTest = 40) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 4,minutesToTest = 16) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 4,minutesToTest = 16) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 256,minutesToDie = 15,minutesToTest = 45) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 256,minutesToDie = 15,minutesToTest = 45) == 4: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 729,minutesToDie = 12,minutesToTest = 36) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 729,minutesToDie = 12,minutesToTest = 36) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 3125,minutesToDie = 4,minutesToTest = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 3125,minutesToDie = 4,minutesToTest = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(buckets = 200,minutesToDie = 4,minutesToTest = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(buckets = 200,minutesToDie = 4,minutesToTest = 20) == 3: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(buckets = 4,minutesToDie = 15,minutesToTest = 15) == 2
    assert candidate(buckets = 1,minutesToDie = 1,minutesToTest = 1) == 0
    assert candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 100) == 2
    assert candidate(buckets = 4,minutesToDie = 15,minutesToTest = 30) == 2
    assert candidate(buckets = 1,minutesToDie = 10,minutesToTest = 10) == 0
    assert candidate(buckets = 8,minutesToDie = 10,minutesToTest = 40) == 2
    assert candidate(buckets = 10,minutesToDie = 5,minutesToTest = 10) == 3
    assert candidate(buckets = 1,minutesToDie = 10,minutesToTest = 100) == 0
    assert candidate(buckets = 1000,minutesToDie = 1,minutesToTest = 1) == 10
    assert candidate(buckets = 10,minutesToDie = 5,minutesToTest = 20) == 2
    assert candidate(buckets = 100,minutesToDie = 10,minutesToTest = 60) == 3
    assert candidate(buckets = 10,minutesToDie = 5,minutesToTest = 25) == 2
    assert candidate(buckets = 8,minutesToDie = 10,minutesToTest = 30) == 2
    assert candidate(buckets = 1024,minutesToDie = 1,minutesToTest = 10) == 3
    assert candidate(buckets = 9,minutesToDie = 25,minutesToTest = 75) == 2
    assert candidate(buckets = 27,minutesToDie = 3,minutesToTest = 9) == 3
    assert candidate(buckets = 500,minutesToDie = 5,minutesToTest = 20) == 4
    assert candidate(buckets = 81,minutesToDie = 2,minutesToTest = 4) == 4
    assert candidate(buckets = 250,minutesToDie = 25,minutesToTest = 100) == 4
    assert candidate(buckets = 625,minutesToDie = 20,minutesToTest = 100) == 4
    assert candidate(buckets = 625,minutesToDie = 10,minutesToTest = 30) == 5
    assert candidate(buckets = 3125,minutesToDie = 5,minutesToTest = 20) == 5
    assert candidate(buckets = 999,minutesToDie = 1,minutesToTest = 99) == 2
    assert candidate(buckets = 243,minutesToDie = 1,minutesToTest = 5) == 4
    assert candidate(buckets = 1296,minutesToDie = 6,minutesToTest = 18) == 6
    assert candidate(buckets = 243,minutesToDie = 18,minutesToTest = 90) == 4
    assert candidate(buckets = 729,minutesToDie = 3,minutesToTest = 9) == 5
    assert candidate(buckets = 512,minutesToDie = 5,minutesToTest = 25) == 4
    assert candidate(buckets = 64,minutesToDie = 4,minutesToTest = 16) == 3
    assert candidate(buckets = 256,minutesToDie = 5,minutesToTest = 10) == 6
    assert candidate(buckets = 350,minutesToDie = 7,minutesToTest = 35) == 4
    assert candidate(buckets = 500,minutesToDie = 20,minutesToTest = 100) == 4
    assert candidate(buckets = 343,minutesToDie = 7,minutesToTest = 21) == 5
    assert candidate(buckets = 128,minutesToDie = 8,minutesToTest = 32) == 4
    assert candidate(buckets = 64,minutesToDie = 2,minutesToTest = 6) == 3
    assert candidate(buckets = 81,minutesToDie = 9,minutesToTest = 27) == 4
    assert candidate(buckets = 125,minutesToDie = 25,minutesToTest = 125) == 3
    assert candidate(buckets = 450,minutesToDie = 12,minutesToTest = 60) == 4
    assert candidate(buckets = 441,minutesToDie = 20,minutesToTest = 60) == 5
    assert candidate(buckets = 3125,minutesToDie = 15,minutesToTest = 60) == 5
    assert candidate(buckets = 512,minutesToDie = 15,minutesToTest = 30) == 6
    assert candidate(buckets = 729,minutesToDie = 9,minutesToTest = 27) == 5
    assert candidate(buckets = 216,minutesToDie = 10,minutesToTest = 50) == 3
    assert candidate(buckets = 27,minutesToDie = 1,minutesToTest = 3) == 3
    assert candidate(buckets = 243,minutesToDie = 9,minutesToTest = 27) == 4
    assert candidate(buckets = 1024,minutesToDie = 4,minutesToTest = 12) == 5
    assert candidate(buckets = 512,minutesToDie = 5,minutesToTest = 20) == 4
    assert candidate(buckets = 81,minutesToDie = 30,minutesToTest = 90) == 4
    assert candidate(buckets = 512,minutesToDie = 2,minutesToTest = 10) == 4
    assert candidate(buckets = 128,minutesToDie = 15,minutesToTest = 60) == 4
    assert candidate(buckets = 300,minutesToDie = 3,minutesToTest = 9) == 5
    assert candidate(buckets = 999,minutesToDie = 2,minutesToTest = 20) == 3
    assert candidate(buckets = 999,minutesToDie = 1,minutesToTest = 10) == 3
    assert candidate(buckets = 16,minutesToDie = 4,minutesToTest = 16) == 2
    assert candidate(buckets = 343,minutesToDie = 7,minutesToTest = 42) == 3
    assert candidate(buckets = 343,minutesToDie = 2,minutesToTest = 14) == 3
    assert candidate(buckets = 125,minutesToDie = 5,minutesToTest = 25) == 3
    assert candidate(buckets = 9,minutesToDie = 3,minutesToTest = 9) == 2
    assert candidate(buckets = 600,minutesToDie = 10,minutesToTest = 50) == 4
    assert candidate(buckets = 750,minutesToDie = 20,minutesToTest = 100) == 4
    assert candidate(buckets = 216,minutesToDie = 6,minutesToTest = 30) == 3
    assert candidate(buckets = 961,minutesToDie = 30,minutesToTest = 90) == 5
    assert candidate(buckets = 125,minutesToDie = 10,minutesToTest = 50) == 3
    assert candidate(buckets = 256,minutesToDie = 15,minutesToTest = 75) == 4
    assert candidate(buckets = 800,minutesToDie = 15,minutesToTest = 75) == 4
    assert candidate(buckets = 729,minutesToDie = 10,minutesToTest = 30) == 5
    assert candidate(buckets = 750,minutesToDie = 15,minutesToTest = 45) == 5
    assert candidate(buckets = 100,minutesToDie = 1,minutesToTest = 10) == 2
    assert candidate(buckets = 500,minutesToDie = 5,minutesToTest = 30) == 4
    assert candidate(buckets = 500,minutesToDie = 5,minutesToTest = 25) == 4
    assert candidate(buckets = 1024,minutesToDie = 10,minutesToTest = 40) == 5
    assert candidate(buckets = 9,minutesToDie = 3,minutesToTest = 6) == 2
    assert candidate(buckets = 27,minutesToDie = 6,minutesToTest = 18) == 3
    assert candidate(buckets = 27,minutesToDie = 5,minutesToTest = 15) == 3
    assert candidate(buckets = 256,minutesToDie = 10,minutesToTest = 40) == 4
    assert candidate(buckets = 81,minutesToDie = 4,minutesToTest = 16) == 3
    assert candidate(buckets = 441,minutesToDie = 7,minutesToTest = 49) == 3
    assert candidate(buckets = 441,minutesToDie = 14,minutesToTest = 70) == 4
    assert candidate(buckets = 64,minutesToDie = 20,minutesToTest = 100) == 3
    assert candidate(buckets = 256,minutesToDie = 1,minutesToTest = 7) == 3
    assert candidate(buckets = 999,minutesToDie = 2,minutesToTest = 4) == 7
    assert candidate(buckets = 81,minutesToDie = 10,minutesToTest = 50) == 3
    assert candidate(buckets = 64,minutesToDie = 1,minutesToTest = 6) == 3
    assert candidate(buckets = 128,minutesToDie = 2,minutesToTest = 16) == 3
    assert candidate(buckets = 999,minutesToDie = 2,minutesToTest = 100) == 2
    assert candidate(buckets = 1024,minutesToDie = 8,minutesToTest = 32) == 5
    assert candidate(buckets = 81,minutesToDie = 3,minutesToTest = 9) == 4
    assert candidate(buckets = 81,minutesToDie = 5,minutesToTest = 15) == 4
    assert candidate(buckets = 125,minutesToDie = 5,minutesToTest = 20) == 3
    assert candidate(buckets = 961,minutesToDie = 6,minutesToTest = 36) == 4
    assert candidate(buckets = 729,minutesToDie = 1,minutesToTest = 5) == 4
    assert candidate(buckets = 169,minutesToDie = 13,minutesToTest = 39) == 4
    assert candidate(buckets = 750,minutesToDie = 10,minutesToTest = 50) == 4
    assert candidate(buckets = 625,minutesToDie = 10,minutesToTest = 40) == 4
    assert candidate(buckets = 256,minutesToDie = 4,minutesToTest = 16) == 4
    assert candidate(buckets = 256,minutesToDie = 15,minutesToTest = 45) == 4
    assert candidate(buckets = 729,minutesToDie = 12,minutesToTest = 36) == 5
    assert candidate(buckets = 3125,minutesToDie = 4,minutesToTest = 20) == 5
    assert candidate(buckets = 200,minutesToDie = 4,minutesToTest = 20) == 3


