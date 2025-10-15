def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 6) == 1240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 6) == 1240: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 3,introvertsCount = 1,extrovertsCount = 2) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 3,introvertsCount = 1,extrovertsCount = 2) == 240: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 0) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 0) == 720: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 4,extrovertsCount = 0) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 4,extrovertsCount = 0) == 240: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 1,introvertsCount = 2,extrovertsCount = 1) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 1,introvertsCount = 2,extrovertsCount = 1) == 260: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 5) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 5) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 3) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 3) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 5,extrovertsCount = 0) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 5,extrovertsCount = 0) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 5,extrovertsCount = 5) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 5,extrovertsCount = 5) == 770: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 5,introvertsCount = 0,extrovertsCount = 6) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 5,introvertsCount = 0,extrovertsCount = 6) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 4) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 4) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 6,extrovertsCount = 0) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 6,extrovertsCount = 0) == 240: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 2) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 2) == 590: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 1) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 1) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 4,extrovertsCount = 3) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 4,extrovertsCount = 3) == 680: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 1) == 620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 1) == 620: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 4) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 4) == 680: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 1,extrovertsCount = 6) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 1,extrovertsCount = 6) == 640: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 6) == 1140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 6) == 1140: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 5) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 5) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 2) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 2) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 4) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 4) == 390: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 4) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 4) == 800: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 1) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 1) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 2) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 2) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 3) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 3) == 640: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 1,extrovertsCount = 4) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 1,extrovertsCount = 4) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 3) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 3) == 200: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 6) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 6) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 5,extrovertsCount = 1) == 610
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 5,extrovertsCount = 1) == 610: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 1) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 1) == 380: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 5,extrovertsCount = 1) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 5,extrovertsCount = 1) == 640: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 1) == 640
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 1) == 640: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 2,introvertsCount = 4,extrovertsCount = 2) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 2,introvertsCount = 4,extrovertsCount = 2) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 3,extrovertsCount = 3) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 3,extrovertsCount = 3) == 550: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 2,introvertsCount = 3,extrovertsCount = 2) == 470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 2,introvertsCount = 3,extrovertsCount = 2) == 470: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 4,extrovertsCount = 2) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 4,extrovertsCount = 2) == 600: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 2,introvertsCount = 2,extrovertsCount = 4) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 2,introvertsCount = 2,extrovertsCount = 4) == 550: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 6,extrovertsCount = 0) == 720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 6,extrovertsCount = 0) == 720: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 2,introvertsCount = 1,extrovertsCount = 5) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 2,introvertsCount = 1,extrovertsCount = 5) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,introvertsCount = 1,extrovertsCount = 4) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,introvertsCount = 1,extrovertsCount = 4) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 3) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 3) == 680: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 1,introvertsCount = 2,extrovertsCount = 2) == 340
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 1,introvertsCount = 2,extrovertsCount = 2) == 340: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 2) == 710
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 2) == 710: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 1,extrovertsCount = 5) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 1,extrovertsCount = 5) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 4) == 680
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 4) == 680: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 2) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 2) == 600: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,introvertsCount = 6,extrovertsCount = 2) == 840
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,introvertsCount = 6,extrovertsCount = 2) == 840: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 4,introvertsCount = 0,extrovertsCount = 6) == 520
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 4,introvertsCount = 0,extrovertsCount = 6) == 520: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 4) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 4) == 700: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 2,extrovertsCount = 2) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 2,extrovertsCount = 2) == 280: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 6,extrovertsCount = 0) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 6,extrovertsCount = 0) == 600: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 0) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 0) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 4,introvertsCount = 3,extrovertsCount = 2) == 470
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 4,introvertsCount = 3,extrovertsCount = 2) == 470: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 1,extrovertsCount = 1) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 1,extrovertsCount = 1) == 160: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 3,extrovertsCount = 3) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 3,extrovertsCount = 3) == 420: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 2) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 2) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 4) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 4) == 550: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 2) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 2) == 120: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 5) == 770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 5) == 770: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 3,extrovertsCount = 3) == 420
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 3,extrovertsCount = 3) == 420: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 0) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 0) == 600: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 2,introvertsCount = 1,extrovertsCount = 1) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 2,introvertsCount = 1,extrovertsCount = 1) == 160: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 5) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 5) == 360: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 0,extrovertsCount = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 0,extrovertsCount = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    total += 1
    try:
        result = candidate(m = 4,n = 5,introvertsCount = 5,extrovertsCount = 4) == 920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 5,introvertsCount = 5,extrovertsCount = 4) == 920: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 1) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 1) == 120: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 5,introvertsCount = 1,extrovertsCount = 1) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 5,introvertsCount = 1,extrovertsCount = 1) == 160: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 0) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 0) == 120: {e}')
    
    total += 1
    try:
        result = candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40: {e}')
    
    total += 1
    try:
        result = candidate(m = 2,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 6) == 1240
    assert candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40
    assert candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 2,n = 3,introvertsCount = 1,extrovertsCount = 2) == 240
    assert candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120
    assert candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 0) == 720
    assert candidate(m = 2,n = 2,introvertsCount = 4,extrovertsCount = 0) == 240
    assert candidate(m = 3,n = 1,introvertsCount = 2,extrovertsCount = 1) == 260
    assert candidate(m = 1,n = 1,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 5) == 360
    assert candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 3) == 560
    assert candidate(m = 5,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560
    assert candidate(m = 1,n = 5,introvertsCount = 5,extrovertsCount = 0) == 360
    assert candidate(m = 4,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480
    assert candidate(m = 2,n = 5,introvertsCount = 5,extrovertsCount = 5) == 770
    assert candidate(m = 3,n = 5,introvertsCount = 0,extrovertsCount = 6) == 520
    assert candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 4) == 560
    assert candidate(m = 2,n = 2,introvertsCount = 6,extrovertsCount = 0) == 240
    assert candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 2) == 590
    assert candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 1) == 520
    assert candidate(m = 4,n = 3,introvertsCount = 4,extrovertsCount = 3) == 680
    assert candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 1) == 620
    assert candidate(m = 5,n = 2,introvertsCount = 3,extrovertsCount = 2) == 480
    assert candidate(m = 5,n = 5,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 4) == 680
    assert candidate(m = 4,n = 4,introvertsCount = 1,extrovertsCount = 6) == 640
    assert candidate(m = 4,n = 4,introvertsCount = 6,extrovertsCount = 6) == 1140
    assert candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520
    assert candidate(m = 5,n = 5,introvertsCount = 6,extrovertsCount = 5) == 1120
    assert candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 2) == 360
    assert candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 4) == 390
    assert candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 4) == 800
    assert candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 5,n = 2,introvertsCount = 4,extrovertsCount = 1) == 520
    assert candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 3) == 560
    assert candidate(m = 2,n = 5,introvertsCount = 2,extrovertsCount = 2) == 360
    assert candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 3) == 640
    assert candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560
    assert candidate(m = 5,n = 3,introvertsCount = 1,extrovertsCount = 4) == 440
    assert candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 3,n = 2,introvertsCount = 0,extrovertsCount = 3) == 200
    assert candidate(m = 5,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480
    assert candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 6) == 520
    assert candidate(m = 3,n = 3,introvertsCount = 5,extrovertsCount = 1) == 610
    assert candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 1) == 380
    assert candidate(m = 5,n = 5,introvertsCount = 5,extrovertsCount = 1) == 640
    assert candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 4) == 560
    assert candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 1) == 640
    assert candidate(m = 4,n = 2,introvertsCount = 4,extrovertsCount = 2) == 520
    assert candidate(m = 5,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560
    assert candidate(m = 4,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560
    assert candidate(m = 3,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480
    assert candidate(m = 3,n = 3,introvertsCount = 3,extrovertsCount = 3) == 550
    assert candidate(m = 4,n = 2,introvertsCount = 3,extrovertsCount = 2) == 470
    assert candidate(m = 5,n = 3,introvertsCount = 4,extrovertsCount = 2) == 600
    assert candidate(m = 4,n = 2,introvertsCount = 2,extrovertsCount = 4) == 550
    assert candidate(m = 5,n = 3,introvertsCount = 6,extrovertsCount = 0) == 720
    assert candidate(m = 5,n = 2,introvertsCount = 0,extrovertsCount = 6) == 520
    assert candidate(m = 4,n = 2,introvertsCount = 1,extrovertsCount = 5) == 520
    assert candidate(m = 4,n = 5,introvertsCount = 1,extrovertsCount = 4) == 440
    assert candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 3) == 680
    assert candidate(m = 4,n = 1,introvertsCount = 2,extrovertsCount = 2) == 340
    assert candidate(m = 4,n = 3,introvertsCount = 5,extrovertsCount = 2) == 710
    assert candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 3) == 560
    assert candidate(m = 2,n = 5,introvertsCount = 1,extrovertsCount = 5) == 520
    assert candidate(m = 5,n = 3,introvertsCount = 3,extrovertsCount = 4) == 680
    assert candidate(m = 4,n = 4,introvertsCount = 4,extrovertsCount = 2) == 600
    assert candidate(m = 4,n = 5,introvertsCount = 6,extrovertsCount = 2) == 840
    assert candidate(m = 3,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 3,n = 4,introvertsCount = 0,extrovertsCount = 6) == 520
    assert candidate(m = 3,n = 3,introvertsCount = 4,extrovertsCount = 4) == 700
    assert candidate(m = 2,n = 2,introvertsCount = 2,extrovertsCount = 2) == 280
    assert candidate(m = 5,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 3,n = 3,introvertsCount = 6,extrovertsCount = 0) == 600
    assert candidate(m = 4,n = 3,introvertsCount = 2,extrovertsCount = 4) == 560
    assert candidate(m = 5,n = 1,introvertsCount = 5,extrovertsCount = 0) == 360
    assert candidate(m = 2,n = 4,introvertsCount = 3,extrovertsCount = 2) == 470
    assert candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 3,n = 3,introvertsCount = 1,extrovertsCount = 1) == 160
    assert candidate(m = 1,n = 5,introvertsCount = 3,extrovertsCount = 3) == 420
    assert candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 2) == 360
    assert candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 4) == 550
    assert candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 1) == 40
    assert candidate(m = 2,n = 2,introvertsCount = 0,extrovertsCount = 2) == 120
    assert candidate(m = 3,n = 3,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 3,n = 3,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 5) == 770
    assert candidate(m = 5,n = 1,introvertsCount = 3,extrovertsCount = 3) == 420
    assert candidate(m = 5,n = 2,introvertsCount = 5,extrovertsCount = 0) == 600
    assert candidate(m = 4,n = 4,introvertsCount = 2,extrovertsCount = 3) == 440
    assert candidate(m = 5,n = 1,introvertsCount = 1,extrovertsCount = 0) == 120
    assert candidate(m = 2,n = 2,introvertsCount = 1,extrovertsCount = 1) == 160
    assert candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 5) == 360
    assert candidate(m = 4,n = 4,introvertsCount = 0,extrovertsCount = 0) == 0
    assert candidate(m = 4,n = 4,introvertsCount = 3,extrovertsCount = 2) == 480
    assert candidate(m = 4,n = 5,introvertsCount = 5,extrovertsCount = 4) == 920
    assert candidate(m = 1,n = 1,introvertsCount = 1,extrovertsCount = 1) == 120
    assert candidate(m = 5,n = 5,introvertsCount = 1,extrovertsCount = 1) == 160
    assert candidate(m = 1,n = 5,introvertsCount = 1,extrovertsCount = 0) == 120
    assert candidate(m = 1,n = 5,introvertsCount = 0,extrovertsCount = 1) == 40
    assert candidate(m = 5,n = 1,introvertsCount = 0,extrovertsCount = 1) == 40
    assert candidate(m = 2,n = 5,introvertsCount = 3,extrovertsCount = 2) == 480


