def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 100,y = 1) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 1) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 100) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 100) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 10) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 10) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 4,y = 11) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,y = 11) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 7) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 7) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 1) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 1) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 100) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 100) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 1) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 1) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 65,y = 48) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 65,y = 48) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 90,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 90,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 99) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 99) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 75,y = 75) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 75,y = 75) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 22,y = 33) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 22,y = 33) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 27,y = 8) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 27,y = 8) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 80) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 80) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 75,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 75,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 50) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 50) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 60) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 60) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 33,y = 27) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 33,y = 27) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 100) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 100) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 25) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 25) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 80,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 80,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 17) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 17) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 25) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 25) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 99,y = 1) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99,y = 1) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 2) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 2) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 33,y = 66) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 33,y = 66) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 60) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 60) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 95) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 95) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 25) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 25) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 70) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 70) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 55,y = 55) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 55,y = 55) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 15) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 15) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 25) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 25) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 33,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 33,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 45,y = 55) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45,y = 55) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 10) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 10) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 15) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 15) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 70) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 70) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 3) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 3) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 75) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 75) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 99,y = 99) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99,y = 99) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 14) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 14) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 99,y = 100) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 99,y = 100) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 60,y = 40) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 60,y = 40) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 100) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 100) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 90) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 90) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 100,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 100,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 15) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 15) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 25) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 25) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 75) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 75) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 100) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 100) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 42,y = 13) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 42,y = 13) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 75,y = 10) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 75,y = 10) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 40) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 40) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 8) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 8) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 80,y = 30) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 80,y = 30) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 3) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 3) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 50) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 50) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 2) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 2) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 0) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 0) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 6,y = 2) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,y = 2) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 6) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 6) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 2) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 2) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 10) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 10) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 15) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 15) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 3) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 3) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 10) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 10) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 9,y = 12) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,y = 12) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 25) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 25) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 7) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 7) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 9,y = 9) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 9,y = 9) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 75,y = 11) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 75,y = 11) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 6,y = 3) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,y = 3) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 2) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 2) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 20) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 5) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 5) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 6,y = 8) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,y = 8) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 15) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 15) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 15) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 15) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 6,y = 9) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,y = 9) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 6,y = 6) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 6,y = 6) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 3) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 3) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 8,y = 8) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 8,y = 8) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20) == "Alice": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 100,y = 1) == "Bob"
    assert candidate(x = 1,y = 100) == "Alice"
    assert candidate(x = 1,y = 10) == "Alice"
    assert candidate(x = 4,y = 11) == "Bob"
    assert candidate(x = 2,y = 7) == "Alice"
    assert candidate(x = 5,y = 5) == "Alice"
    assert candidate(x = 10,y = 1) == "Bob"
    assert candidate(x = 100,y = 100) == "Alice"
    assert candidate(x = 1,y = 1) == "Bob"
    assert candidate(x = 3,y = 5) == "Alice"
    assert candidate(x = 50,y = 50) == "Bob"
    assert candidate(x = 30,y = 50) == "Bob"
    assert candidate(x = 65,y = 48) == "Bob"
    assert candidate(x = 10,y = 30) == "Alice"
    assert candidate(x = 20,y = 5) == "Alice"
    assert candidate(x = 90,y = 5) == "Alice"
    assert candidate(x = 15,y = 20) == "Alice"
    assert candidate(x = 30,y = 30) == "Alice"
    assert candidate(x = 1,y = 99) == "Alice"
    assert candidate(x = 75,y = 75) == "Bob"
    assert candidate(x = 22,y = 33) == "Bob"
    assert candidate(x = 27,y = 8) == "Bob"
    assert candidate(x = 20,y = 80) == "Bob"
    assert candidate(x = 75,y = 5) == "Alice"
    assert candidate(x = 5,y = 50) == "Alice"
    assert candidate(x = 30,y = 60) == "Alice"
    assert candidate(x = 33,y = 27) == "Bob"
    assert candidate(x = 10,y = 100) == "Bob"
    assert candidate(x = 25,y = 25) == "Bob"
    assert candidate(x = 80,y = 20) == "Alice"
    assert candidate(x = 25,y = 30) == "Alice"
    assert candidate(x = 8,y = 17) == "Bob"
    assert candidate(x = 30,y = 25) == "Bob"
    assert candidate(x = 99,y = 1) == "Bob"
    assert candidate(x = 5,y = 2) == "Bob"
    assert candidate(x = 33,y = 66) == "Bob"
    assert candidate(x = 5,y = 60) == "Alice"
    assert candidate(x = 5,y = 95) == "Alice"
    assert candidate(x = 15,y = 25) == "Bob"
    assert candidate(x = 15,y = 70) == "Alice"
    assert candidate(x = 55,y = 55) == "Alice"
    assert candidate(x = 10,y = 15) == "Alice"
    assert candidate(x = 25,y = 50) == "Bob"
    assert candidate(x = 20,y = 25) == "Bob"
    assert candidate(x = 33,y = 50) == "Bob"
    assert candidate(x = 20,y = 30) == "Alice"
    assert candidate(x = 45,y = 55) == "Alice"
    assert candidate(x = 10,y = 10) == "Bob"
    assert candidate(x = 5,y = 10) == "Bob"
    assert candidate(x = 5,y = 20) == "Alice"
    assert candidate(x = 20,y = 15) == "Alice"
    assert candidate(x = 30,y = 70) == "Alice"
    assert candidate(x = 7,y = 3) == "Bob"
    assert candidate(x = 25,y = 75) == "Bob"
    assert candidate(x = 99,y = 99) == "Bob"
    assert candidate(x = 7,y = 14) == "Alice"
    assert candidate(x = 99,y = 100) == "Alice"
    assert candidate(x = 60,y = 40) == "Bob"
    assert candidate(x = 25,y = 100) == "Alice"
    assert candidate(x = 5,y = 90) == "Alice"
    assert candidate(x = 100,y = 50) == "Bob"
    assert candidate(x = 25,y = 20) == "Alice"
    assert candidate(x = 50,y = 30) == "Alice"
    assert candidate(x = 5,y = 15) == "Alice"
    assert candidate(x = 3,y = 25) == "Alice"
    assert candidate(x = 10,y = 75) == "Bob"
    assert candidate(x = 50,y = 100) == "Alice"
    assert candidate(x = 42,y = 13) == "Alice"
    assert candidate(x = 50,y = 5) == "Alice"
    assert candidate(x = 75,y = 10) == "Bob"
    assert candidate(x = 15,y = 40) == "Bob"
    assert candidate(x = 3,y = 8) == "Bob"
    assert candidate(x = 80,y = 30) == "Alice"
    assert candidate(x = 8,y = 3) == "Bob"
    assert candidate(x = 20,y = 50) == "Bob"
    assert candidate(x = 30,y = 5) == "Alice"
    assert candidate(x = 10,y = 2) == "Bob"
    assert candidate(x = 15,y = 0) == "Bob"
    assert candidate(x = 6,y = 2) == "Bob"
    assert candidate(x = 10,y = 20) == "Alice"
    assert candidate(x = 7,y = 6) == "Alice"
    assert candidate(x = 7,y = 2) == "Bob"
    assert candidate(x = 20,y = 10) == "Bob"
    assert candidate(x = 8,y = 15) == "Alice"
    assert candidate(x = 5,y = 3) == "Bob"
    assert candidate(x = 3,y = 10) == "Bob"
    assert candidate(x = 9,y = 12) == "Alice"
    assert candidate(x = 50,y = 25) == "Bob"
    assert candidate(x = 1,y = 20) == "Alice"
    assert candidate(x = 7,y = 7) == "Alice"
    assert candidate(x = 9,y = 9) == "Bob"
    assert candidate(x = 75,y = 11) == "Bob"
    assert candidate(x = 6,y = 3) == "Bob"
    assert candidate(x = 8,y = 2) == "Bob"
    assert candidate(x = 50,y = 20) == "Alice"
    assert candidate(x = 8,y = 5) == "Alice"
    assert candidate(x = 6,y = 8) == "Bob"
    assert candidate(x = 1,y = 15) == "Alice"
    assert candidate(x = 0,y = 15) == "Bob"
    assert candidate(x = 6,y = 9) == "Bob"
    assert candidate(x = 6,y = 6) == "Alice"
    assert candidate(x = 3,y = 3) == "Bob"
    assert candidate(x = 8,y = 8) == "Bob"
    assert candidate(x = 20,y = 20) == "Alice"


