def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(senate = "RDDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDARR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDARR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDRRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDRRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRRDDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRRDDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDRRRRDDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDRRRRDDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "AAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "AAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRRDDRRDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRRDDRRDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDRRRRRRDDDDRRRRRRRRDDDRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDRRRRRRDDDDRRRRRRRRDDDRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDDRDRDRRDDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDDRDRDRRDDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDRRRRRDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDRRRRRDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRRDDRRDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRRDDRRDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDD-DDRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDD-DDRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRDDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRDDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDRRDDDRRRDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDRRDDDRRRDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRRDDDRRDDDRRDDDRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRRDDDRRDDDRRDDDRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDRRRRDDDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDRRRRDDDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDDDDRRRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDDDDRRRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDRDRDRDRDRDRDRDRD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDRDRDRDRDRDRDRDRD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDDDRRRRRRDDDDDDRRRRRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDDDRRRRRRDDDDDDRRRRRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRDDDDDDRRRRRRDDDDDDRRRRRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRDDDDDDRRRRRRDDDDDDRRRRRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDDRDDRRDDDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDDRDDRRDDDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRRRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRRRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRRDDDRRDDDRRDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRRDDDRRDDDRRDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDDDRRRDDDRRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDDDRRRDDDRRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRRDRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRRDRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDDRRRRDDDDRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDDRRRRDDDDRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRRDDDRRDDDRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRRDDDRRDDDRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRRDDDRRDDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRRDDDRRDDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAA") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAA") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDRRRRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDRRRRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRDDDDDDDDDDDDDDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRDDDDDDDDDDDDDDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDRRRRRDDDDRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDRRRRRDDDDRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "AAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "AAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRRRRRRRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRRRRRRRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRDDRRRDDRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRDDRRRDDRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDDDDRRRRRDDDDDDRRRRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDDDDRRRRRDDDDDDRRRRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRRRDRDDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRRRDRDDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDRRDDDDRRDDDDRRDDDDRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDRRDDDDRRDDDDRRDDDDRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDRRDDDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDRRDDDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDRRRDDDDRRRDDDDRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDRRRDDDDRRRDDDDRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRDRDRDRDRDRDRDRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRDRDRDRDRDRDRDRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDRRRDDDRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDRRRDDDRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRRRRDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRRRRDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRRDDDDDDRRRRRRDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRRDDDDDDRRRRRRDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRDDRRRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRDDRRRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDDRRDDRRDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDDRRDDRRDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRDRDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRDRDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDRRRDDRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDRRRDDRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDDDDDDRRRRRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDDDDDDRRRRRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDDRRRRRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDDRRRRRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDDRRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDDRRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRDDDDBBRRDDDDRRRRDDRRDDDDBB") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRDDDDBBRRDDDDRRRRDDRRDDDDBB") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDDDDDDRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDDDDDDRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "AAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "AAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRRRRRRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRRRRRRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRRRRRRRRRRDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRRRRRRRRRRDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRDDRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRDDRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDSSSSSRRRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDSSSSSRRRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRDDDDDDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRDDDDDDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDRRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDRRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDD-DDDDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDD-DDDDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDDRRDDRRDDRRDDRRDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRRRDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRRRDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDRRRRRRRRDDDDDDDDRRRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDRRRRRRRRDDDDDDDDRRRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRRRDDDDRRRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRRRDDDDRRRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDRRDDDRRDDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDRRDDDRRDDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRRDDRRRDDRRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRRDDRRRDDRRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDRRRRDDDDDRRRRDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDRRRRDDDDDRRRRDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRRRDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRRRDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDDDDDDRRRRRRRRRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDDDDDDRRRRRRRRRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDRRDDDRRDRRDDDRRDRRDDDRRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDRRDDDRRDRRDDDRRDRRDDDRRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDRDRDRDRDRDRDRDRDRD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDRDRDRDRDRDRDRDRDRD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDRDDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDRDDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRDDDDDDRRRRDDDDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRDDDDDDRRRRDDDDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDDRRRRRDDDDDDRRRRRDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDDRRRRRDDDDDDRRRRRDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDDRRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDDRRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRDRDRDRDRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRDRDRDRDRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRRDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRRDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDRRRRRRDDRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDRRRRRRDDRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDRRRDDDDRRRRRDDDDDDRRRRRDDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDRRRDDDDRRRRRDDDDDDRRRRRDDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRRDDDRRDDDRRDDDRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRRDDDRRDDDRRDDDRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDRRRRDDDDRRRRRDDDDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDRRRRDDDDRRRRRDDDDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDDDRRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDDDRRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRRRDDDDRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRRRDDDDRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRDDDDRRDDDDRRDDDDRRDDDDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRDDDDRRDDDDRRDDDDRRDDDDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDDDDDDRRRDDDRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDDDDDDRRRDDDRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDD") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDDDDDRRRRRRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDDDDDRRRRRRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRRDDDDRRRRDDDRRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRRDDDDRRRRDDDRRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRDDRRDDRRDDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRDDRRDDRRDDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDDDRRDDRRDDRRDDRRDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDDDRRDDRRDDRRDDRRDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDDRRDDRRDDRRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDDRRDDRRDDRRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DRDRDRDRDRDRDRDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DRDRDRDRDRDRDRDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDDRRRDDDDRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDDRRRDDDDRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RDDDRDDDRDDDRDDD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RDDDRDDDRDDDRDDD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDRDRDRDRDRDRD") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDRDRDRDRDRDRD") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "DDRDDDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Dire"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "DDRDDDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Dire": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRR") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRR") == "Radiant": {e}')
    
    total += 1
    try:
        result = candidate(senate = "RRRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Radiant"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(senate = "RRRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Radiant": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(senate = "RDDRDR") == "Dire"
    assert candidate(senate = "RDD") == "Dire"
    assert candidate(senate = "DDDARR") == "Dire"
    assert candidate(senate = "DRDR") == "Dire"
    assert candidate(senate = "RDDRRD") == "Radiant"
    assert candidate(senate = "RDRDRDRDRDRDRD") == "Radiant"
    assert candidate(senate = "RD") == "Radiant"
    assert candidate(senate = "DRDRDR") == "Dire"
    assert candidate(senate = "RRRDDD") == "Radiant"
    assert candidate(senate = "DDDD") == "Dire"
    assert candidate(senate = "RRDDRR") == "Radiant"
    assert candidate(senate = "DDDDRRRRRDDDDRRRR") == "Dire"
    assert candidate(senate = "RRDDDD") == "Dire"
    assert candidate(senate = "DDDDRRRR") == "Dire"
    assert candidate(senate = "RDRDRD") == "Radiant"
    assert candidate(senate = "DDRRR") == "Dire"
    assert candidate(senate = "DDDRRR") == "Dire"
    assert candidate(senate = "DDDDDDRRRRRR") == "Dire"
    assert candidate(senate = "RRDD") == "Radiant"
    assert candidate(senate = "RRRDDDDRRDDRR") == "Radiant"
    assert candidate(senate = "RRDDD") == "Radiant"
    assert candidate(senate = "DRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "DRDRDRDR") == "Dire"
    assert candidate(senate = "DDRR") == "Dire"
    assert candidate(senate = "DDRDRR") == "Dire"
    assert candidate(senate = "RRRRDDDD") == "Radiant"
    assert candidate(senate = "RRRR") == "Radiant"
    assert candidate(senate = "RRRRRRRDDDDDDD") == "Radiant"
    assert candidate(senate = "RDRD") == "Radiant"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
    assert candidate(senate = "RRDDDRRRRDDDRRDD") == "Radiant"
    assert candidate(senate = "AAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDDD") == "Dire"
    assert candidate(senate = "RDRRDDRRDDRRDD") == "Radiant"
    assert candidate(senate = "DDDDDRRRRRRDDDDRRRRRRRRDDDRRR") == "Radiant"
    assert candidate(senate = "RDDDRDRDRRDDRR") == "Dire"
    assert candidate(senate = "DDDDDDDDRRRRRDDD") == "Dire"
    assert candidate(senate = "RRDDRRDDRRDDRRDD") == "Radiant"
    assert candidate(senate = "RRRRRDDDDD-DDRRR") == "Radiant"
    assert candidate(senate = "RRRRRRRRRRDDDDDDDDDD") == "Radiant"
    assert candidate(senate = "RDRDRDRDRDRDRDRD") == "Radiant"
    assert candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRRRR") == "Radiant"
    assert candidate(senate = "DDDRRDDDRRRDDDDD") == "Dire"
    assert candidate(senate = "DDDDDDDDRRRRRR") == "Dire"
    assert candidate(senate = "RDRRDDDRRDDDRRDDDRDD") == "Dire"
    assert candidate(senate = "RRDDDDRRRRDDDDRR") == "Radiant"
    assert candidate(senate = "DRRDDDDDDRRRRRDD") == "Dire"
    assert candidate(senate = "RRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant"
    assert candidate(senate = "RRRDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Radiant"
    assert candidate(senate = "RDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire"
    assert candidate(senate = "DDRDRDRDRDRDRDRDRDRD") == "Dire"
    assert candidate(senate = "RRDDDDDDRRRRRRDDDDDDRRRRRRDDDD") == "Dire"
    assert candidate(senate = "RRRRRRDDDDDDRRRRRRDDDDDDRRRRRRDD") == "Radiant"
    assert candidate(senate = "RRDDDDDRDDRRDDDR") == "Dire"
    assert candidate(senate = "DDDDDDRRRRRRRRRR") == "Radiant"
    assert candidate(senate = "RRRDDDRRDDDRRDDDRRDDRR") == "Radiant"
    assert candidate(senate = "RRDDDDDDRRRDDDRRRRDD") == "Dire"
    assert candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant"
    assert candidate(senate = "DDDDRRRRRDRRDDDD") == "Dire"
    assert candidate(senate = "RDDDRRRRDDDDRRRR") == "Radiant"
    assert candidate(senate = "RRDRRDDDRRDDDRDD") == "Radiant"
    assert candidate(senate = "DDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDDRDD") == "Dire"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "DDDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire"
    assert candidate(senate = "RRRRRRRDDDDDDDD") == "Radiant"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "RRRDDDDRRRRRDDDD") == "Radiant"
    assert candidate(senate = "RRRDDDRRDDDRRDDDRRDD") == "Radiant"
    assert candidate(senate = "DDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAA") == "Dire"
    assert candidate(senate = "RRRRRRRRDDDDDDDDD") == "Radiant"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDDDD") == "Dire"
    assert candidate(senate = "RRRRRDDDDRRRRRDD") == "Radiant"
    assert candidate(senate = "RRRRRRRRRRDDDDDDDDDDDDDDDDDDDD") == "Dire"
    assert candidate(senate = "RRDDDDRRRRRDDDDRRRR") == "Radiant"
    assert candidate(senate = "AAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire"
    assert candidate(senate = "DDDDDDRRRRRRRRRRRRRR") == "Radiant"
    assert candidate(senate = "DDDDRRRRDDRRRDDRRRDD") == "Dire"
    assert candidate(senate = "RRRRDDDDDDRRRRRDDDDDDRRRRRDD") == "Radiant"
    assert candidate(senate = "RRDDRRRDRDDDRRDD") == "Radiant"
    assert candidate(senate = "RRDDDDRRDDDDRRDDDDRRDDDDRRDDDD") == "Dire"
    assert candidate(senate = "RRDDDRRDDDDDRRDD") == "Dire"
    assert candidate(senate = "RDDRRRDDDDRRRDDDDRRRDD") == "Dire"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDDDDDD") == "Dire"
    assert candidate(senate = "DDDDRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Dire"
    assert candidate(senate = "RRDRDRDRDRDRDRDRDRDR") == "Radiant"
    assert candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant"
    assert candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
    assert candidate(senate = "DDDDDRRRDDDRRRDD") == "Dire"
    assert candidate(senate = "DRRRRRDDDDDDD") == "Dire"
    assert candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Radiant"
    assert candidate(senate = "DDDDDDRRRRRRDDDDDDRRRRRRDDDDDD") == "Dire"
    assert candidate(senate = "RRRDDDDRRRDDRRRRRR") == "Radiant"
    assert candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
    assert candidate(senate = "DRDDRRDDRRDDRRDD") == "Dire"
    assert candidate(senate = "RDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "RRRRRRRDRDDDDDDD") == "Radiant"
    assert candidate(senate = "DDDRRRDDRRRDD") == "Dire"
    assert candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
    assert candidate(senate = "RRRRDDDDDDDDRRRRRRDDDD") == "Dire"
    assert candidate(senate = "DDRDRDRDRDRDRDRDRDRDRDRDRDRD") == "Dire"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDDRRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "DDDDDDDDDDRRRRRRRRRR") == "Dire"
    assert candidate(senate = "DRDDRRDRDRDRDR") == "Dire"
    assert candidate(senate = "DDRRDDDDBBRRDDDDRRRRDDRRDDDDBB") == "Dire"
    assert candidate(senate = "RRRRDDDDDDDDRRRR") == "Radiant"
    assert candidate(senate = "AAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAADDDDDDDDDDDDDDDAAAAAAAAAAAAAAAAAAAAA") == "Dire"
    assert candidate(senate = "DDDDRRRRDDD") == "Dire"
    assert candidate(senate = "DDRRRRRRRRDD") == "Radiant"
    assert candidate(senate = "DDDDRRRRRRRRRRRRRDDDDDDDD") == "Radiant"
    assert candidate(senate = "RRRDDDRDDRRRDDDD") == "Radiant"
    assert candidate(senate = "RRRRDDDSSSSSRRRRRR") == "Radiant"
    assert candidate(senate = "RRRRRRDDDDDDDDDDDD") == "Dire"
    assert candidate(senate = "RRRRRDDDDDRRRRDDDD") == "Radiant"
    assert candidate(senate = "DDDDRRRRRR") == "Dire"
    assert candidate(senate = "RRRRDDD-DDDDDDRRRR") == "Dire"
    assert candidate(senate = "RRRRRDDDDD") == "Radiant"
    assert candidate(senate = "RRDDDDRRDDRRDDRRDDRRDDRRDD") == "Dire"
    assert candidate(senate = "RRRRRRRRRRRRDDDDDD") == "Radiant"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRRRDDDD") == "Dire"
    assert candidate(senate = "DDDDDDDDRRRRRRRRDDDDDDDDRRRRRRRR") == "Dire"
    assert candidate(senate = "DDRRRRDDDDRRRRDD") == "Dire"
    assert candidate(senate = "RRRRRDDDRRDDDRRDDDRRDD") == "Radiant"
    assert candidate(senate = "RRDRRDDRRRDDRRDR") == "Radiant"
    assert candidate(senate = "RRRRRDDDDDRRRRDDDDDRRRRDDDDD") == "Radiant"
    assert candidate(senate = "DRRRRDDDDDDD") == "Dire"
    assert candidate(senate = "DDDDDDDDDDDDDDRRRRRRRRRRRRRR") == "Dire"
    assert candidate(senate = "RRRRRRRDDDDDDDDD") == "Radiant"
    assert candidate(senate = "RRRDRRDDDRRDRRDDDRRDRRDDDRRD") == "Radiant"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "RDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
    assert candidate(senate = "RRRDDDDRRRDDDDRRRDDDDRRRDDDDRR") == "Dire"
    assert candidate(senate = "RDRDRDRDRDRDRDRDRDRD") == "Radiant"
    assert candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "RRRDRDDDRRDD") == "Radiant"
    assert candidate(senate = "DRDRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "DDDDDDRRRRDDDDDDRRRRDDDDDDRRRR") == "Dire"
    assert candidate(senate = "RRRRRDDDDDDRRRRRDDDDDDRRRRRDDDDD") == "Radiant"
    assert candidate(senate = "RRRRDDDDRRRRDDDD") == "Radiant"
    assert candidate(senate = "RRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDD") == "Radiant"
    assert candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDD") == "Radiant"
    assert candidate(senate = "RRDRDRDRDRDRDR") == "Radiant"
    assert candidate(senate = "DDDDDDDDDDDAAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAAADDDDDDDDDAAAAAAAAAAADDDDDDDDDAAAAAAAAAAA") == "Dire"
    assert candidate(senate = "DRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "DDDDDDRRRRRRDDDDDD") == "Dire"
    assert candidate(senate = "DDDDDDRRRRRRDDRRRRR") == "Dire"
    assert candidate(senate = "DDDRRRDDDDRRRRRDDDDDDRRRRRDDDDDDD") == "Dire"
    assert candidate(senate = "DDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRR") == "Dire"
    assert candidate(senate = "RRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Radiant"
    assert candidate(senate = "DRRDDDRRDDDRRDDDRRDDDD") == "Dire"
    assert candidate(senate = "RRRRRDDDDDRRRRDDDDRRRRRDDDDDRR") == "Radiant"
    assert candidate(senate = "RRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDDDDDRRRRDDDDDD") == "Dire"
    assert candidate(senate = "DDDDDDDDDDRRRRRRR") == "Dire"
    assert candidate(senate = "DDDDRRRRDDDDRRRR") == "Dire"
    assert candidate(senate = "DDDDRRDDDDRRDDDDRRDDDDRRDDDDRR") == "Dire"
    assert candidate(senate = "RRRRRDDDDDDDDDRRRDDDRRDDDD") == "Dire"
    assert candidate(senate = "RRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDDRRRRDDDD") == "Radiant"
    assert candidate(senate = "RRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDDDDDDRRRRRRRRRRRRDDDDDDDDD") == "Radiant"
    assert candidate(senate = "DDDDDDDDRRRRRRRR") == "Dire"
    assert candidate(senate = "DDRRRDDDDRRRRDDDRRR") == "Dire"
    assert candidate(senate = "DDRRDDRRDDRRDDRR") == "Dire"
    assert candidate(senate = "RRDDDRRDDDRRDDDRRDDDRRDDDRRDDDRRDD") == "Dire"
    assert candidate(senate = "DDDDRRDDRRDDRRDDRRDD") == "Dire"
    assert candidate(senate = "DRDDRRDDRRDDRRDR") == "Dire"
    assert candidate(senate = "DRDRDRDRDRDRDRDR") == "Dire"
    assert candidate(senate = "RRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDDDRRRRDDDD") == "Dire"
    assert candidate(senate = "RRRDDDDRRRDDDDRR") == "Radiant"
    assert candidate(senate = "RDDDRDDDRDDDRDDD") == "Dire"
    assert candidate(senate = "RRDRDRDRDRDRDRDRDRDRDRDRDRDR") == "Radiant"
    assert candidate(senate = "DDRRDDRRDDRRDDRRDDRRDDRRDDRRDDRR") == "Dire"
    assert candidate(senate = "DDRDRDRDRDRDRDRD") == "Dire"
    assert candidate(senate = "DDRDDDRRDDDRRDDDRRDDDRRDDDRRDDDR") == "Dire"
    assert candidate(senate = "RRRDDDRRDDDRRDDDRRDDRRRR") == "Radiant"
    assert candidate(senate = "RRRRRDDDDRRRDDDDRRRDDDDRRRDD") == "Radiant"


