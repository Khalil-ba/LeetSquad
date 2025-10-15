def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(day = 31,month = 12,year = 2100) == "Friday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 31,month = 12,year = 2100) == "Friday": {e}')
    
    total += 1
    try:
        result = candidate(day = 15,month = 8,year = 1993) == "Sunday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 15,month = 8,year = 1993) == "Sunday": {e}')
    
    total += 1
    try:
        result = candidate(day = 10,month = 9,year = 2023) == "Sunday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 10,month = 9,year = 2023) == "Sunday": {e}')
    
    total += 1
    try:
        result = candidate(day = 18,month = 7,year = 1999) == "Sunday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 18,month = 7,year = 1999) == "Sunday": {e}')
    
    total += 1
    try:
        result = candidate(day = 31,month = 8,year = 2019) == "Saturday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 31,month = 8,year = 2019) == "Saturday": {e}')
    
    total += 1
    try:
        result = candidate(day = 4,month = 7,year = 2023) == "Tuesday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 4,month = 7,year = 2023) == "Tuesday": {e}')
    
    total += 1
    try:
        result = candidate(day = 25,month = 12,year = 2023) == "Monday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 25,month = 12,year = 2023) == "Monday": {e}')
    
    total += 1
    try:
        result = candidate(day = 29,month = 2,year = 2004) == "Sunday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 29,month = 2,year = 2004) == "Sunday": {e}')
    
    total += 1
    try:
        result = candidate(day = 1,month = 1,year = 1971) == "Friday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 1,month = 1,year = 1971) == "Friday": {e}')
    
    total += 1
    try:
        result = candidate(day = 29,month = 2,year = 2000) == "Tuesday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 29,month = 2,year = 2000) == "Tuesday": {e}')
    
    total += 1
    try:
        result = candidate(day = 28,month = 2,year = 1900) == "Wednesday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 28,month = 2,year = 1900) == "Wednesday": {e}')
    
    total += 1
    try:
        result = candidate(day = 14,month = 2,year = 2000) == "Monday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 14,month = 2,year = 2000) == "Monday": {e}')
    
    total += 1
    try:
        result = candidate(day = 31,month = 10,year = 1984) == "Wednesday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 31,month = 10,year = 1984) == "Wednesday": {e}')
    
    total += 1
    try:
        result = candidate(day = 1,month = 3,year = 1999) == "Monday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 1,month = 3,year = 1999) == "Monday": {e}')
    
    total += 1
    try:
        result = candidate(day = 14,month = 3,year = 2047) == "Thursday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 14,month = 3,year = 2047) == "Thursday": {e}')
    
    total += 1
    try:
        result = candidate(day = 15,month = 6,year = 2050) == "Wednesday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 15,month = 6,year = 2050) == "Wednesday": {e}')
    
    total += 1
    try:
        result = candidate(day = 30,month = 4,year = 2020) == "Thursday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 30,month = 4,year = 2020) == "Thursday": {e}')
    
    total += 1
    try:
        result = candidate(day = 7,month = 11,year = 2025) == "Friday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 7,month = 11,year = 2025) == "Friday": {e}')
    
    total += 1
    try:
        result = candidate(day = 1,month = 9,year = 2001) == "Saturday"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(day = 1,month = 9,year = 2001) == "Saturday": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(day = 31,month = 12,year = 2100) == "Friday"
    assert candidate(day = 15,month = 8,year = 1993) == "Sunday"
    assert candidate(day = 10,month = 9,year = 2023) == "Sunday"
    assert candidate(day = 18,month = 7,year = 1999) == "Sunday"
    assert candidate(day = 31,month = 8,year = 2019) == "Saturday"
    assert candidate(day = 4,month = 7,year = 2023) == "Tuesday"
    assert candidate(day = 25,month = 12,year = 2023) == "Monday"
    assert candidate(day = 29,month = 2,year = 2004) == "Sunday"
    assert candidate(day = 1,month = 1,year = 1971) == "Friday"
    assert candidate(day = 29,month = 2,year = 2000) == "Tuesday"
    assert candidate(day = 28,month = 2,year = 1900) == "Wednesday"
    assert candidate(day = 14,month = 2,year = 2000) == "Monday"
    assert candidate(day = 31,month = 10,year = 1984) == "Wednesday"
    assert candidate(day = 1,month = 3,year = 1999) == "Monday"
    assert candidate(day = 14,month = 3,year = 2047) == "Thursday"
    assert candidate(day = 15,month = 6,year = 2050) == "Wednesday"
    assert candidate(day = 30,month = 4,year = 2020) == "Thursday"
    assert candidate(day = 7,month = 11,year = 2025) == "Friday"
    assert candidate(day = 1,month = 9,year = 2001) == "Saturday"


