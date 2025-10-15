def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(destination = [3, 3],k = 5) == "HVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 3],k = 5) == "HVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [2, 3],k = 1) == "HHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [2, 3],k = 1) == "HHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [4, 4],k = 10) == "HHVVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [4, 4],k = 10) == "HHVVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 3],k = 10) == "HVVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 3],k = 10) == "HVVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [2, 3],k = 2) == "HHVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [2, 3],k = 2) == "HHVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [2, 3],k = 3) == "HHVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [2, 3],k = 3) == "HHVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [4, 4],k = 20) == "HVHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [4, 4],k = 20) == "HVHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [4, 5],k = 10) == "HHHVVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [4, 5],k = 10) == "HHHVVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 1) == "HHHHHHHHHHHHHHHVVVVVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 1) == "HHHHHHHHHHHHHHHVVVVVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 2],k = 4) == "HVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 2],k = 4) == "HVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 4],k = 5) == "HHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 4],k = 5) == "HHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 5],k = 100) == "HVVHHVVHVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 5],k = 100) == "HVVHHVVHVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 2],k = 1) == "HHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 2],k = 1) == "HHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 10],k = 175) == "HVHHHHHHVVHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 10],k = 175) == "HVHHHHHHVVHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 8],k = 1716) == "HHVVVVVVVHHHHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 8],k = 1716) == "HHVVVVVVVHHHHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 12],k = 50000) == "HHHHHVVVVVVVHVVHHVHHVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 12],k = 50000) == "HHHHHVVVVVVVHVVHHVHHVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 5],k = 2000) == "HVVHVVVVVVVHVVVVVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 5],k = 2000) == "HVVHVVVVVVVHVVVVVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [9, 5],k = 252) == "HVHHVVVVHVHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [9, 5],k = 252) == "HVHHVVVVHVHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 7],k = 1000) == "VVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 7],k = 1000) == "VVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 9],k = 300) == "HHHHHVVVVHHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 9],k = 300) == "HHHHHVVVVHHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [9, 7],k = 5678) == "VHHVHVHVVHVHVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [9, 7],k = 5678) == "VHHVHVHVVHVHVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 5000) == "HHHHVHVVVVVVVVHHHHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 5000) == "HHHHVHVVVVVVVVHHHHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [9, 9],k = 1000) == "HHHHVHVHVVVVVVVHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [9, 9],k = 1000) == "HHHHVHVHVVVVVVVHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 4],k = 15) == "HVHVHVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 4],k = 15) == "HVHVHVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [14, 10],k = 5000) == "HHHHHVHVVVVVHVHVHVHVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [14, 10],k = 5000) == "HHHHHVHVVVVVHVHVHVHVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 500000) == "HHHHHHVHHHHVVVVVHHVHHVVVVHVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 500000) == "HHHHHHVHHHHVVVVVHHVHHVVVVHVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 12],k = 250) == "HHHHHHHHVHVVHVVVVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 12],k = 250) == "HHHHHHHHVHVVHVVVVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 40116600) == "HVHHHVHVHVVHHVVHHVVVVHVHHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 40116600) == "HVHHHVHVHVVHHVVHHVVVVHVHHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 5],k = 1234) == "HVVVHVVHVVVVHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 5],k = 1234) == "HVVVHVVHVVVVHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 15],k = 3003) == "HHHHHVVVVVHHHHHHHHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 15],k = 3003) == "HHHHHVVVVVHHHHHHHHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 8],k = 500) == "HHHHVHHVVVVHVVHVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 8],k = 500) == "HHHHVHHVVVVHVVHVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 6],k = 150) == "HHVHVHHVHVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 6],k = 150) == "HHVHVHHVHVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 7],k = 123) == "VVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 7],k = 123) == "VVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [13, 7],k = 4000) == "HHVHVVVVVVHHVHVVHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [13, 7],k = 4000) == "HHVHVVVVVVHHVHVVHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 12],k = 100000) == "HHHHVVHVVVVHHHHVVHVHVHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 12],k = 100000) == "HHHHVVHVVVVHHHHVVHVHVHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [2, 13],k = 150) == "VVVVVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [2, 13],k = 150) == "VVVVVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 500) == "HHHHHHVHVVVVVVVHVHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 500) == "HHHHHHVHVVVVVVVHVHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 5],k = 30) == "HHHVVVVHVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 5],k = 30) == "HHHVVVVHVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 6],k = 500) == "VHHHVVHHVHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 6],k = 500) == "VHHHVVHHVHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [9, 9],k = 10000) == "HHVVVHHVHVHHVVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [9, 9],k = 10000) == "HHVVVHHVHVHHVVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 7],k = 120) == "HHHVHVHVVVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 7],k = 120) == "HHHVHVHVVVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 9],k = 500) == "HHHHVHHHHVVVVHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 9],k = 500) == "HHHHVHHHHVVVVHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 1000000) == "HHHHHHVVHVVVVHVVVVHHHVHVVVHHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 1000000) == "HHHHHHVVHVVVVHVVVVHHHVHVVVHHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [1, 15],k = 1) == "HHHHHHHHHHHHHHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [1, 15],k = 1) == "HHHHHHHHHHHHHHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 10000) == "HHHVHHVVVVVVVHVHHHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 10000) == "HHHVHHVVVVVVVHVHHHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 8],k = 3000) == "HVVHVHVVHHHHVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 8],k = 3000) == "HVVHVHVVHHHHVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 10],k = 100) == "HHHVHHVHHHHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 10],k = 100) == "HHHVHHVHHHHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 8],k = 5000) == "HHHVVVVHHVVHVVHVVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 8],k = 5000) == "HHHVVVVHHVVHVVHVVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 50000) == "HVHHVHHVVVVVHHHVHVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 50000) == "HVHHVHHVVVVVHHHVHVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 7],k = 343) == "HHVHHHVHVVVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 7],k = 343) == "HHVHHHVHVVVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 8],k = 1000) == "HHVHHVVVVVHHVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 8],k = 1000) == "HHVHHVVVVVHHVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 4],k = 50) == "HVVVHVHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 4],k = 50) == "HVVVHVHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 8],k = 2000) == "HVHHVHVHVHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 8],k = 2000) == "HVHHVHVHVHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [3, 12],k = 200) == "HHHVHHVHVHHHHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [3, 12],k = 200) == "HHHVHHVHVHHHHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 14],k = 10000) == "HHHVHHVVVHVVHHHHHHHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 14],k = 10000) == "HHHVHHVVVHVVHHHHHHHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 9],k = 15000) == "VHHVHHVVVHHHVVHHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 9],k = 15000) == "VHHVHHVVVHHHVVHHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 4],k = 250) == "HVVVHVHVVVVHVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 4],k = 250) == "HVVVHVHVVVVHVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 8],k = 1234) == "HHVHVVVVHHHHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 8],k = 1234) == "HHVHVVVVHHHHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 7],k = 3456) == "VHHVHVHVVHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 7],k = 3456) == "VHHVHVHVVHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [13, 2],k = 100) == "VVVVVVVVVVVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [13, 2],k = 100) == "VVVVVVVVVVVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [11, 11],k = 6000) == "HHHHHVHVHVVVVHVVHVHVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [11, 11],k = 6000) == "HHHHHVHVHVVVVHVVHVHVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 7],k = 200) == "HHHVHVVVVHVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 7],k = 200) == "HHHVHVVVVHVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 12345) == "HHHHHHHHHHVVVVHVVVVVHVVHHVVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 12345) == "HHHHHHHHHHVVVVHVVVVVHVVHHVVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 12],k = 3456) == "HHHHHVHHVHVHVVHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 12],k = 3456) == "HHHHHVHHVHVHVVHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 9],k = 300) == "HHHHVHVHVVVHVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 9],k = 300) == "HHHHVHVHVVVHVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [14, 6],k = 5000) == "HVHVVVVVHVHVHVHVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [14, 6],k = 5000) == "HVHVVVVVHVHVHVHVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 6],k = 8316) == "VVVVVVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 6],k = 8316) == "VVVVVVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 12],k = 123456) == "HHHHVVVVVVHHVHHHVHVHHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 12],k = 123456) == "HHHHVVVVVVHHVHHHVHVHHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [10, 10],k = 12870) == "HHHVHVVVVVHHVVVHHHVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [10, 10],k = 12870) == "HHHVHVVVVVHHVVVHHHVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [14, 6],k = 98765) == "VVVVVVVVVVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [14, 6],k = 98765) == "VVVVVVVVVVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 6],k = 150) == "HHHVVVVVHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 6],k = 150) == "HHHVVVVVHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [7, 6],k = 300) == "HHVVVVHHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [7, 6],k = 300) == "HHVVVVHHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 8],k = 2500) == "HHHVHVVHHVVVHVVHVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 8],k = 2500) == "HHHVHVVHHVVVHVVHVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 6],k = 120) == "HHVVVHVHVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 6],k = 120) == "HHVVVHVHVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 7],k = 500) == "HVHHHVVHHVHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 7],k = 500) == "HVHHHVVHHVHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [9, 7],k = 200) == "HHHHVVVVVHVVVVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [9, 7],k = 200) == "HHHHVVVVVHVVVVHH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 6],k = 500) == "HVHHHHVVVVHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 6],k = 500) == "HVHHHHVVVVHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 15],k = 6435678) == "HHHHVVVHHHVHHVVVVHVVHHHVHVHVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 15],k = 6435678) == "HHHHVVVHHHVHHVVVVHVVHHHVHVHVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [4, 12],k = 500) == "HHHVHHHHHHHVHHVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [4, 12],k = 500) == "HHHVHHHHHHHVHHVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [8, 7],k = 650) == "HHVHVHVHVHHVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [8, 7],k = 650) == "HHVHVHVHVHHVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 7],k = 123) == "HHHVHVVHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 7],k = 123) == "HHHVHVVHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [12, 3],k = 200) == "VVHVVVHHVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [12, 3],k = 200) == "VVHVVVHHVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 12],k = 500) == "HHHHHVHHHVHHHVVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 12],k = 500) == "HHHHHVHHHVHHHVVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [5, 7],k = 30) == "HHHHVHVHVVVH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [5, 7],k = 30) == "HHHHVHVHVVVH": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 4],k = 45) == "HVHVVVHVHV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 4],k = 45) == "HVHVVVHVHV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [15, 1],k = 1) == "HVVVVVVVVVVVVVVV"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [15, 1],k = 1) == "HVVVVVVVVVVVVVVV": {e}')
    
    total += 1
    try:
        result = candidate(destination = [6, 8],k = 300) == "HHHVHVHVVVHVHH"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(destination = [6, 8],k = 300) == "HHHVHVHVVVHVHH": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(destination = [3, 3],k = 5) == "HVHHVV"
    assert candidate(destination = [2, 3],k = 1) == "HHHVV"
    assert candidate(destination = [4, 4],k = 10) == "HHVVHHVV"
    assert candidate(destination = [3, 3],k = 10) == "HVVVHH"
    assert candidate(destination = [2, 3],k = 2) == "HHVHV"
    assert candidate(destination = [2, 3],k = 3) == "HHVVH"
    assert candidate(destination = [4, 4],k = 20) == "HVHVHHVV"
    assert candidate(destination = [4, 5],k = 10) == "HHHVVHHVV"
    assert candidate(destination = [15, 15],k = 1) == "HHHHHHHHHHHHHHHVVVVVVVVVVVVVVV"
    assert candidate(destination = [3, 2],k = 4) == "HVVVH"
    assert candidate(destination = [3, 4],k = 5) == "HHVHHVV"
    assert candidate(destination = [5, 5],k = 100) == "HVVHHVVHVH"
    assert candidate(destination = [3, 2],k = 1) == "HHVVV"
    assert candidate(destination = [3, 10],k = 175) == "HVHHHHHHVVHHH"
    assert candidate(destination = [7, 8],k = 1716) == "HHVVVVVVVHHHHHH"
    assert candidate(destination = [12, 12],k = 50000) == "HHHHHVVVVVVVHVVHHVHHVVHH"
    assert candidate(destination = [15, 5],k = 2000) == "HVVHVVVVVVVHVVVVVVHH"
    assert candidate(destination = [9, 5],k = 252) == "HVHHVVVVHVHVVV"
    assert candidate(destination = [5, 7],k = 1000) == "VVVVVVVVVVVV"
    assert candidate(destination = [7, 9],k = 300) == "HHHHHVVVVHHVHHVV"
    assert candidate(destination = [9, 7],k = 5678) == "VHHVHVHVVHVHVVVH"
    assert candidate(destination = [10, 10],k = 5000) == "HHHHVHVVVVVVVVHHHHHV"
    assert candidate(destination = [9, 9],k = 1000) == "HHHHVHVHVVVVVVVHHH"
    assert candidate(destination = [3, 4],k = 15) == "HVHVHVH"
    assert candidate(destination = [14, 10],k = 5000) == "HHHHHVHVVVVVHVHVHVHVVVVV"
    assert candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH"
    assert candidate(destination = [15, 15],k = 500000) == "HHHHHHVHHHHVVVVVHHVHHVVVVHVVVV"
    assert candidate(destination = [8, 12],k = 250) == "HHHHHHHHVHVVHVVVVVHH"
    assert candidate(destination = [15, 15],k = 40116600) == "HVHHHVHVHVVHHVVHHVVVVHVHHHVVHV"
    assert candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV"
    assert candidate(destination = [12, 5],k = 1234) == "HVVVHVVHVVVVHVVHV"
    assert candidate(destination = [5, 15],k = 3003) == "HHHHHVVVVVHHHHHHHHHH"
    assert candidate(destination = [12, 8],k = 500) == "HHHHVHHVVVVHVVHVVVVV"
    assert candidate(destination = [7, 6],k = 150) == "HHVHVHHVHVVVV"
    assert candidate(destination = [3, 7],k = 123) == "VVVVVVVVVV"
    assert candidate(destination = [13, 7],k = 4000) == "HHVHVVVVVVHHVHVVHVVV"
    assert candidate(destination = [12, 12],k = 100000) == "HHHHVVHVVVVHHHHVVHVHVHVV"
    assert candidate(destination = [2, 13],k = 150) == "VVVVVVVVVVVVVVV"
    assert candidate(destination = [10, 10],k = 500) == "HHHHHHVHVVVVVVVHVHHV"
    assert candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH"
    assert candidate(destination = [7, 5],k = 30) == "HHHVVVVHVVVH"
    assert candidate(destination = [6, 6],k = 500) == "VHHHVVHHVHVV"
    assert candidate(destination = [9, 9],k = 10000) == "HHVVVHHVHVHHVVHHVV"
    assert candidate(destination = [6, 7],k = 120) == "HHHVHVHVVVVHH"
    assert candidate(destination = [8, 9],k = 500) == "HHHHVHHHHVVVVHVVV"
    assert candidate(destination = [15, 15],k = 1000000) == "HHHHHHVVHVVVVHVVVVHHHVHVVVHHHV"
    assert candidate(destination = [1, 15],k = 1) == "HHHHHHHHHHHHHHHV"
    assert candidate(destination = [10, 10],k = 10000) == "HHHVHHVVVVVVVHVHHHHV"
    assert candidate(destination = [10, 10],k = 1000) == "HHHHHHVVVVVVVVVHVHHH"
    assert candidate(destination = [7, 8],k = 3000) == "HVVHVHVVHHHHVVH"
    assert candidate(destination = [3, 10],k = 100) == "HHHVHHVHHHHHV"
    assert candidate(destination = [12, 8],k = 5000) == "HHHVVVVHHVVHVVHVVVVH"
    assert candidate(destination = [10, 5],k = 200) == "HHVVVHVVVVVVHHV"
    assert candidate(destination = [10, 10],k = 50000) == "HVHHVHHVVVVVHHHVHVHV"
    assert candidate(destination = [7, 7],k = 343) == "HHVHHHVHVVVVVH"
    assert candidate(destination = [7, 8],k = 1000) == "HHVHHVVVVVHHVHH"
    assert candidate(destination = [5, 4],k = 50) == "HVVVHVHHV"
    assert candidate(destination = [7, 8],k = 2000) == "HVHHVHVHVHHVVHV"
    assert candidate(destination = [3, 12],k = 200) == "HHHVHHVHVHHHHHH"
    assert candidate(destination = [6, 14],k = 10000) == "HHHVHHVVVHVVHHHHHHHH"
    assert candidate(destination = [8, 9],k = 15000) == "VHHVHHVVVHHHVVHHV"
    assert candidate(destination = [12, 4],k = 250) == "HVVVHVHVVVVHVVVV"
    assert candidate(destination = [7, 8],k = 1234) == "HHVHVVVVHHHHHVV"
    assert candidate(destination = [8, 7],k = 3456) == "VHHVHVHVVHHVVHV"
    assert candidate(destination = [13, 2],k = 100) == "VVVVVVVVVVVHHVV"
    assert candidate(destination = [11, 11],k = 6000) == "HHHHHVHVHVVVVHVVHVHVHV"
    assert candidate(destination = [7, 7],k = 200) == "HHHVHVVVVHVVHH"
    assert candidate(destination = [15, 15],k = 12345) == "HHHHHHHHHHVVVVHVVVVVHVVHHVVVVH"
    assert candidate(destination = [8, 12],k = 3456) == "HHHHHVHHVHVHVVHHVVHV"
    assert candidate(destination = [6, 9],k = 300) == "HHHHVHVHVVVHVHH"
    assert candidate(destination = [14, 6],k = 5000) == "HVHVVVVVHVHVHVHVVVVV"
    assert candidate(destination = [10, 6],k = 8316) == "VVVVVVVVVVVVVVVV"
    assert candidate(destination = [15, 15],k = 10000) == "HHHHHHHHHHVVVHVHVVVHVVVHVVVVVH"
    assert candidate(destination = [12, 12],k = 123456) == "HHHHVVVVVVHHVHHHVHVHHVVV"
    assert candidate(destination = [10, 10],k = 12870) == "HHHVHVVVVVHHVVVHHHVH"
    assert candidate(destination = [14, 6],k = 98765) == "VVVVVVVVVVVVVVVVVVVV"
    assert candidate(destination = [8, 6],k = 150) == "HHHVVVVVHVHHVV"
    assert candidate(destination = [7, 6],k = 300) == "HHVVVVHHVHHVV"
    assert candidate(destination = [12, 8],k = 2500) == "HHHVHVVHHVVVHVVHVVVV"
    assert candidate(destination = [5, 6],k = 120) == "HHVVVHVHVHH"
    assert candidate(destination = [6, 7],k = 500) == "HVHHHVVHHVHVV"
    assert candidate(destination = [9, 7],k = 200) == "HHHHVVVVVHVVVVHH"
    assert candidate(destination = [8, 6],k = 500) == "HVHHHHVVVVHVVV"
    assert candidate(destination = [15, 15],k = 6435678) == "HHHHVVVHHHVHHVVVVHVVHHHVHVHVVV"
    assert candidate(destination = [4, 12],k = 500) == "HHHVHHHHHHHVHHVV"
    assert candidate(destination = [8, 7],k = 650) == "HHVHVHVHVHHVVVV"
    assert candidate(destination = [6, 7],k = 123) == "HHHVHVVHHVVHV"
    assert candidate(destination = [12, 3],k = 200) == "VVHVVVHHVVVVVVV"
    assert candidate(destination = [5, 12],k = 500) == "HHHHHVHHHVHHHVVHV"
    assert candidate(destination = [5, 7],k = 30) == "HHHHVHVHVVVH"
    assert candidate(destination = [6, 4],k = 45) == "HVHVVVHVHV"
    assert candidate(destination = [15, 1],k = 1) == "HVVVVVVVVVVVVVVV"
    assert candidate(destination = [6, 8],k = 300) == "HHHVHVHVVVHVHH"


