def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(date1 = "2019-02-28",date2 = "2019-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-02-28",date2 = "2019-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-01-15",date2 = "2019-12-31") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-01-15",date2 = "2019-12-31") == 15: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-03-01",date2 = "2000-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-03-01",date2 = "2000-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-01",date2 = "2023-10-02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-01",date2 = "2023-10-02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2022-02-28",date2 = "2022-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2022-02-28",date2 = "2022-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-01-01",date2 = "2012-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-01-01",date2 = "2012-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-10-10",date2 = "2021-10-10") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-10-10",date2 = "2021-10-10") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-10-01",date2 = "2021-10-10") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-10-01",date2 = "2021-10-10") == 9: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-02-28",date2 = "2020-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-02-28",date2 = "2020-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1971-01-01",date2 = "2100-12-31") == 47481
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1971-01-01",date2 = "2100-12-31") == 47481: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-06-29",date2 = "2019-06-30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-06-29",date2 = "2019-06-30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-01-01",date2 = "2023-12-31") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-01-01",date2 = "2023-12-31") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-01-01",date2 = "2023-01-01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-01-01",date2 = "2023-01-01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2050-06-15",date2 = "2050-06-14") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2050-06-15",date2 = "2050-06-14") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-01",date2 = "2023-10-01") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-01",date2 = "2023-10-01") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-02-29",date2 = "2016-02-28") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-02-29",date2 = "2016-02-28") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-02-28",date2 = "2000-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-02-28",date2 = "2000-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-04-10",date2 = "2023-04-01") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-04-10",date2 = "2023-04-01") == 9: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-02-29",date2 = "2000-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-02-29",date2 = "2000-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2100-02-28",date2 = "2100-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2100-02-28",date2 = "2100-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-01",date2 = "2023-09-01") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-01",date2 = "2023-09-01") == 30: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1971-01-02",date2 = "1971-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1971-01-02",date2 = "1971-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-02-29",date2 = "2012-03-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-02-29",date2 = "2012-03-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1985-04-12",date2 = "2023-07-25") == 13983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1985-04-12",date2 = "2023-07-25") == 13983: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1972-02-29",date2 = "1972-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1972-02-29",date2 = "1972-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2017-10-01",date2 = "2018-10-01") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2017-10-01",date2 = "2018-10-01") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-06-04",date2 = "2023-06-04") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-06-04",date2 = "2023-06-04") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2004-02-28",date2 = "2004-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2004-02-28",date2 = "2004-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-06-30",date2 = "2021-09-30") == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-06-30",date2 = "2021-09-30") == 92: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2004-03-01",date2 = "2004-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2004-03-01",date2 = "2004-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2025-01-01",date2 = "2026-01-01") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2025-01-01",date2 = "2026-01-01") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-03-01",date2 = "2024-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-03-01",date2 = "2024-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-11-30",date2 = "2023-12-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-11-30",date2 = "2023-12-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2100-01-01",date2 = "2100-12-31") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2100-01-01",date2 = "2100-12-31") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-02-29",date2 = "2020-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-02-29",date2 = "2020-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2015-06-30",date2 = "2016-06-30") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2015-06-30",date2 = "2016-06-30") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1980-02-29",date2 = "1981-02-28") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1980-02-29",date2 = "1981-02-28") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2099-12-31",date2 = "2100-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2099-12-31",date2 = "2100-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-06-01",date2 = "2023-07-01") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-06-01",date2 = "2023-07-01") == 30: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2100-12-31",date2 = "2099-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2100-12-31",date2 = "2099-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-02-01",date2 = "2021-02-01") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-02-01",date2 = "2021-02-01") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-01-01",date2 = "2100-12-31") == 36889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-01-01",date2 = "2100-12-31") == 36889: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-02-29",date2 = "2017-02-28") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-02-29",date2 = "2017-02-28") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-01-31",date2 = "2020-02-29") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-01-31",date2 = "2020-02-29") == 29: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1980-02-28",date2 = "1980-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1980-02-28",date2 = "1980-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2050-11-15",date2 = "2050-11-15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2050-11-15",date2 = "2050-11-15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2099-12-30",date2 = "2100-01-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2099-12-30",date2 = "2100-01-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-11-01",date2 = "2023-11-01") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-11-01",date2 = "2023-11-01") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-06-30",date2 = "2016-06-01") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-06-30",date2 = "2016-06-01") == 29: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-02-28",date2 = "2024-02-29") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-02-28",date2 = "2024-02-29") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-01-31",date2 = "2019-02-28") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-01-31",date2 = "2019-02-28") == 28: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-01-01",date2 = "2021-12-31") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-01-01",date2 = "2021-12-31") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-02-28",date2 = "2024-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-02-28",date2 = "2024-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2004-12-31",date2 = "2005-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2004-12-31",date2 = "2005-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-06-05",date2 = "2023-06-04") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-06-05",date2 = "2023-06-04") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-02-28",date2 = "2016-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-02-28",date2 = "2016-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-04-30",date2 = "2023-05-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-04-30",date2 = "2023-05-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-12-31",date2 = "2020-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-12-31",date2 = "2020-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2025-12-31",date2 = "2026-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2025-12-31",date2 = "2026-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-06-30",date2 = "2023-07-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-06-30",date2 = "2023-07-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-02-29",date2 = "2004-02-29") == 1461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-02-29",date2 = "2004-02-29") == 1461: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-12-31",date2 = "2022-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-12-31",date2 = "2022-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-02-28",date2 = "2024-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-02-28",date2 = "2024-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2077-07-04",date2 = "2077-07-05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2077-07-04",date2 = "2077-07-05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2018-04-30",date2 = "2018-05-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2018-04-30",date2 = "2018-05-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-10-15",date2 = "2020-10-15") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-10-15",date2 = "2020-10-15") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2004-02-29",date2 = "2004-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2004-02-29",date2 = "2004-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-12-31",date2 = "2013-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-12-31",date2 = "2013-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1999-02-28",date2 = "1999-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1999-02-28",date2 = "1999-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-01",date2 = "2023-09-29") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-01",date2 = "2023-09-29") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-02-28",date2 = "2012-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-02-28",date2 = "2012-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-03-01",date2 = "2020-02-28") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-03-01",date2 = "2020-02-28") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-02-29",date2 = "2019-02-28") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-02-29",date2 = "2019-02-28") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-01-01",date2 = "2000-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-01-01",date2 = "2000-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-15",date2 = "2024-10-15") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-15",date2 = "2024-10-15") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-08-31",date2 = "2023-09-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-08-31",date2 = "2023-09-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-02-29",date2 = "2024-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-02-29",date2 = "2024-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2015-06-15",date2 = "2015-06-14") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2015-06-15",date2 = "2015-06-14") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-01-01",date2 = "2004-01-01") == 1461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-01-01",date2 = "2004-01-01") == 1461: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1999-12-31",date2 = "1971-01-01") == 10591
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1999-12-31",date2 = "1971-01-01") == 10591: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-12-31",date2 = "2025-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-12-31",date2 = "2025-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1980-06-15",date2 = "1980-07-15") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1980-06-15",date2 = "1980-07-15") == 30: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-03-01",date2 = "2023-02-28") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-03-01",date2 = "2023-02-28") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-02",date2 = "2023-10-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-02",date2 = "2023-10-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-03-01",date2 = "2020-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-03-01",date2 = "2020-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2050-06-15",date2 = "2050-07-15") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2050-06-15",date2 = "2050-07-15") == 30: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2021-06-01",date2 = "2022-06-01") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2021-06-01",date2 = "2022-06-01") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-12-31",date2 = "2023-01-01") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-12-31",date2 = "2023-01-01") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-12-31",date2 = "2020-01-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-12-31",date2 = "2020-01-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-05-31",date2 = "2023-06-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-05-31",date2 = "2023-06-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1971-01-01",date2 = "1971-01-02") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1971-01-01",date2 = "1971-01-02") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1996-02-29",date2 = "1997-02-28") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1996-02-29",date2 = "1997-02-28") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-12-31",date2 = "2024-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-12-31",date2 = "2024-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-11-11",date2 = "2020-02-29") == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-11-11",date2 = "2020-02-29") == 110: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2100-12-31",date2 = "2100-01-01") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2100-12-31",date2 = "2100-01-01") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-01-31",date2 = "2023-02-28") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-01-31",date2 = "2023-02-28") == 28: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2100-12-31",date2 = "2100-12-30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2100-12-31",date2 = "2100-12-30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-09-30",date2 = "2023-10-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-09-30",date2 = "2023-10-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-31",date2 = "2023-11-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-31",date2 = "2023-11-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-11-05",date2 = "2024-11-05") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-11-05",date2 = "2024-11-05") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-02-28",date2 = "2020-02-29") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-02-28",date2 = "2020-02-29") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1972-02-28",date2 = "1972-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1972-02-28",date2 = "1972-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-15",date2 = "2023-10-15") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-15",date2 = "2023-10-15") == 0: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-06-15",date2 = "2019-06-14") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-06-15",date2 = "2019-06-14") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1996-02-28",date2 = "1996-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1996-02-28",date2 = "1996-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1996-04-15",date2 = "1996-05-15") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1996-04-15",date2 = "1996-05-15") == 30: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1980-03-01",date2 = "1980-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1980-03-01",date2 = "1980-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-15",date2 = "2022-10-15") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-15",date2 = "2022-10-15") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-03-15",date2 = "2024-03-01") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-03-15",date2 = "2024-03-01") == 14: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-03-01",date2 = "2025-03-01") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-03-01",date2 = "2025-03-01") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-06-04",date2 = "2023-06-05") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-06-04",date2 = "2023-06-05") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2022-12-31",date2 = "2023-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2022-12-31",date2 = "2023-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-01-01",date2 = "2001-01-01") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-01-01",date2 = "2001-01-01") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-11-01",date2 = "2024-11-01") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-11-01",date2 = "2024-11-01") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1971-01-01",date2 = "1971-12-31") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1971-01-01",date2 = "1971-12-31") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2050-12-31",date2 = "2051-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2050-12-31",date2 = "2051-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2000-02-29",date2 = "1999-02-28") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2000-02-29",date2 = "1999-02-28") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2004-02-28",date2 = "2004-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2004-02-28",date2 = "2004-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-01-01",date2 = "2020-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-01-01",date2 = "2020-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-02-29",date2 = "2012-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-02-29",date2 = "2012-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2024-02-28",date2 = "2025-02-28") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2024-02-28",date2 = "2025-02-28") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2012-02-29",date2 = "2013-02-28") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2012-02-29",date2 = "2013-02-28") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2020-02-28",date2 = "2020-02-29") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2020-02-28",date2 = "2020-02-29") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-06-01",date2 = "2016-06-30") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-06-01",date2 = "2016-06-30") == 29: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2008-02-29",date2 = "2009-02-28") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2008-02-29",date2 = "2009-02-28") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-02-14",date2 = "2023-03-14") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-02-14",date2 = "2023-03-14") == 28: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-07-31",date2 = "2023-08-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-07-31",date2 = "2023-08-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1987-07-04",date2 = "1999-07-04") == 4383
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1987-07-04",date2 = "1999-07-04") == 4383: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-10-01",date2 = "2023-09-30") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-10-01",date2 = "2023-09-30") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-02-28",date2 = "2016-03-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-02-28",date2 = "2016-03-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1980-02-29",date2 = "1980-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1980-02-29",date2 = "1980-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2025-06-15",date2 = "2026-06-15") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2025-06-15",date2 = "2026-06-15") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-01-01",date2 = "2024-01-01") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-01-01",date2 = "2024-01-01") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-05-05",date2 = "2022-05-05") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-05-05",date2 = "2022-05-05") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2023-09-29",date2 = "2023-10-01") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2023-09-29",date2 = "2023-10-01") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2016-02-29",date2 = "2016-03-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2016-02-29",date2 = "2016-03-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "1999-12-31",date2 = "2000-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "1999-12-31",date2 = "2000-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date1 = "2019-09-15",date2 = "2023-09-15") == 1461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date1 = "2019-09-15",date2 = "2023-09-15") == 1461: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(date1 = "2019-02-28",date2 = "2019-03-01") == 1
    assert candidate(date1 = "2020-01-15",date2 = "2019-12-31") == 15
    assert candidate(date1 = "2000-03-01",date2 = "2000-02-29") == 1
    assert candidate(date1 = "2023-10-01",date2 = "2023-10-02") == 1
    assert candidate(date1 = "2022-02-28",date2 = "2022-03-01") == 1
    assert candidate(date1 = "2012-01-01",date2 = "2012-12-31") == 365
    assert candidate(date1 = "2021-10-10",date2 = "2021-10-10") == 0
    assert candidate(date1 = "2021-10-01",date2 = "2021-10-10") == 9
    assert candidate(date1 = "2020-02-28",date2 = "2020-03-01") == 2
    assert candidate(date1 = "1971-01-01",date2 = "2100-12-31") == 47481
    assert candidate(date1 = "2019-06-29",date2 = "2019-06-30") == 1
    assert candidate(date1 = "2023-01-01",date2 = "2023-12-31") == 364
    assert candidate(date1 = "2023-01-01",date2 = "2023-01-01") == 0
    assert candidate(date1 = "2050-06-15",date2 = "2050-06-14") == 1
    assert candidate(date1 = "2023-10-01",date2 = "2023-10-01") == 0
    assert candidate(date1 = "2016-02-29",date2 = "2016-02-28") == 1
    assert candidate(date1 = "2000-02-28",date2 = "2000-03-01") == 2
    assert candidate(date1 = "2023-04-10",date2 = "2023-04-01") == 9
    assert candidate(date1 = "2000-02-29",date2 = "2000-03-01") == 1
    assert candidate(date1 = "2100-02-28",date2 = "2100-03-01") == 1
    assert candidate(date1 = "2023-10-01",date2 = "2023-09-01") == 30
    assert candidate(date1 = "1971-01-02",date2 = "1971-01-01") == 1
    assert candidate(date1 = "2012-02-29",date2 = "2012-03-31") == 31
    assert candidate(date1 = "1985-04-12",date2 = "2023-07-25") == 13983
    assert candidate(date1 = "1972-02-29",date2 = "1972-03-01") == 1
    assert candidate(date1 = "2017-10-01",date2 = "2018-10-01") == 365
    assert candidate(date1 = "2023-06-04",date2 = "2023-06-04") == 0
    assert candidate(date1 = "2004-02-28",date2 = "2004-03-01") == 2
    assert candidate(date1 = "2021-06-30",date2 = "2021-09-30") == 92
    assert candidate(date1 = "2004-03-01",date2 = "2004-02-29") == 1
    assert candidate(date1 = "2025-01-01",date2 = "2026-01-01") == 365
    assert candidate(date1 = "2024-03-01",date2 = "2024-02-29") == 1
    assert candidate(date1 = "2023-11-30",date2 = "2023-12-01") == 1
    assert candidate(date1 = "2100-01-01",date2 = "2100-12-31") == 364
    assert candidate(date1 = "2020-02-29",date2 = "2020-03-01") == 1
    assert candidate(date1 = "2015-06-30",date2 = "2016-06-30") == 366
    assert candidate(date1 = "1980-02-29",date2 = "1981-02-28") == 365
    assert candidate(date1 = "2099-12-31",date2 = "2100-01-01") == 1
    assert candidate(date1 = "2023-06-01",date2 = "2023-07-01") == 30
    assert candidate(date1 = "2100-12-31",date2 = "2099-12-31") == 365
    assert candidate(date1 = "2020-02-01",date2 = "2021-02-01") == 366
    assert candidate(date1 = "2000-01-01",date2 = "2100-12-31") == 36889
    assert candidate(date1 = "2016-02-29",date2 = "2017-02-28") == 365
    assert candidate(date1 = "2020-01-31",date2 = "2020-02-29") == 29
    assert candidate(date1 = "1980-02-28",date2 = "1980-03-01") == 2
    assert candidate(date1 = "2050-11-15",date2 = "2050-11-15") == 0
    assert candidate(date1 = "2099-12-30",date2 = "2100-01-01") == 2
    assert candidate(date1 = "2024-11-01",date2 = "2023-11-01") == 366
    assert candidate(date1 = "2016-06-30",date2 = "2016-06-01") == 29
    assert candidate(date1 = "2023-02-28",date2 = "2024-02-29") == 366
    assert candidate(date1 = "2019-01-31",date2 = "2019-02-28") == 28
    assert candidate(date1 = "2021-01-01",date2 = "2021-12-31") == 364
    assert candidate(date1 = "2024-02-28",date2 = "2024-02-29") == 1
    assert candidate(date1 = "2004-12-31",date2 = "2005-01-01") == 1
    assert candidate(date1 = "2023-06-05",date2 = "2023-06-04") == 1
    assert candidate(date1 = "2016-02-28",date2 = "2016-02-29") == 1
    assert candidate(date1 = "2023-04-30",date2 = "2023-05-01") == 1
    assert candidate(date1 = "2019-12-31",date2 = "2020-01-01") == 1
    assert candidate(date1 = "2025-12-31",date2 = "2026-01-01") == 1
    assert candidate(date1 = "2023-06-30",date2 = "2023-07-01") == 1
    assert candidate(date1 = "2000-02-29",date2 = "2004-02-29") == 1461
    assert candidate(date1 = "2021-12-31",date2 = "2022-01-01") == 1
    assert candidate(date1 = "2024-02-28",date2 = "2024-03-01") == 2
    assert candidate(date1 = "2077-07-04",date2 = "2077-07-05") == 1
    assert candidate(date1 = "2018-04-30",date2 = "2018-05-01") == 1
    assert candidate(date1 = "2019-10-15",date2 = "2020-10-15") == 366
    assert candidate(date1 = "2004-02-29",date2 = "2004-03-01") == 1
    assert candidate(date1 = "2012-12-31",date2 = "2013-01-01") == 1
    assert candidate(date1 = "1999-02-28",date2 = "1999-03-01") == 1
    assert candidate(date1 = "2023-10-01",date2 = "2023-09-29") == 2
    assert candidate(date1 = "2012-02-28",date2 = "2012-03-01") == 2
    assert candidate(date1 = "2020-03-01",date2 = "2020-02-28") == 2
    assert candidate(date1 = "2020-02-29",date2 = "2019-02-28") == 366
    assert candidate(date1 = "2000-01-01",date2 = "2000-12-31") == 365
    assert candidate(date1 = "2023-10-15",date2 = "2024-10-15") == 366
    assert candidate(date1 = "2023-08-31",date2 = "2023-09-01") == 1
    assert candidate(date1 = "2024-02-29",date2 = "2024-03-01") == 1
    assert candidate(date1 = "2015-06-15",date2 = "2015-06-14") == 1
    assert candidate(date1 = "2000-01-01",date2 = "2004-01-01") == 1461
    assert candidate(date1 = "1999-12-31",date2 = "1971-01-01") == 10591
    assert candidate(date1 = "2024-12-31",date2 = "2025-01-01") == 1
    assert candidate(date1 = "1980-06-15",date2 = "1980-07-15") == 30
    assert candidate(date1 = "2023-03-01",date2 = "2023-02-28") == 1
    assert candidate(date1 = "2023-10-02",date2 = "2023-10-01") == 1
    assert candidate(date1 = "2020-03-01",date2 = "2020-02-29") == 1
    assert candidate(date1 = "2050-06-15",date2 = "2050-07-15") == 30
    assert candidate(date1 = "2021-06-01",date2 = "2022-06-01") == 365
    assert candidate(date1 = "2023-12-31",date2 = "2023-01-01") == 364
    assert candidate(date1 = "2019-12-31",date2 = "2020-01-31") == 31
    assert candidate(date1 = "2023-05-31",date2 = "2023-06-01") == 1
    assert candidate(date1 = "1971-01-01",date2 = "1971-01-02") == 1
    assert candidate(date1 = "1996-02-29",date2 = "1997-02-28") == 365
    assert candidate(date1 = "2023-12-31",date2 = "2024-01-01") == 1
    assert candidate(date1 = "2019-11-11",date2 = "2020-02-29") == 110
    assert candidate(date1 = "2100-12-31",date2 = "2100-01-01") == 364
    assert candidate(date1 = "2023-01-31",date2 = "2023-02-28") == 28
    assert candidate(date1 = "2100-12-31",date2 = "2100-12-30") == 1
    assert candidate(date1 = "2023-09-30",date2 = "2023-10-01") == 1
    assert candidate(date1 = "2023-10-31",date2 = "2023-11-01") == 1
    assert candidate(date1 = "2023-11-05",date2 = "2024-11-05") == 366
    assert candidate(date1 = "2019-02-28",date2 = "2020-02-29") == 366
    assert candidate(date1 = "1972-02-28",date2 = "1972-02-29") == 1
    assert candidate(date1 = "2023-10-15",date2 = "2023-10-15") == 0
    assert candidate(date1 = "2019-06-15",date2 = "2019-06-14") == 1
    assert candidate(date1 = "1996-02-28",date2 = "1996-02-29") == 1
    assert candidate(date1 = "1996-04-15",date2 = "1996-05-15") == 30
    assert candidate(date1 = "1980-03-01",date2 = "1980-02-29") == 1
    assert candidate(date1 = "2023-10-15",date2 = "2022-10-15") == 365
    assert candidate(date1 = "2024-03-15",date2 = "2024-03-01") == 14
    assert candidate(date1 = "2024-03-01",date2 = "2025-03-01") == 365
    assert candidate(date1 = "2023-06-04",date2 = "2023-06-05") == 1
    assert candidate(date1 = "2022-12-31",date2 = "2023-01-01") == 1
    assert candidate(date1 = "2000-01-01",date2 = "2001-01-01") == 366
    assert candidate(date1 = "2023-11-01",date2 = "2024-11-01") == 366
    assert candidate(date1 = "1971-01-01",date2 = "1971-12-31") == 364
    assert candidate(date1 = "2050-12-31",date2 = "2051-01-01") == 1
    assert candidate(date1 = "2000-02-29",date2 = "1999-02-28") == 366
    assert candidate(date1 = "2004-02-28",date2 = "2004-02-29") == 1
    assert candidate(date1 = "2020-01-01",date2 = "2020-12-31") == 365
    assert candidate(date1 = "2012-02-29",date2 = "2012-03-01") == 1
    assert candidate(date1 = "2024-02-28",date2 = "2025-02-28") == 366
    assert candidate(date1 = "2012-02-29",date2 = "2013-02-28") == 365
    assert candidate(date1 = "2020-02-28",date2 = "2020-02-29") == 1
    assert candidate(date1 = "2016-06-01",date2 = "2016-06-30") == 29
    assert candidate(date1 = "2008-02-29",date2 = "2009-02-28") == 365
    assert candidate(date1 = "2023-02-14",date2 = "2023-03-14") == 28
    assert candidate(date1 = "2023-07-31",date2 = "2023-08-01") == 1
    assert candidate(date1 = "1987-07-04",date2 = "1999-07-04") == 4383
    assert candidate(date1 = "2023-10-01",date2 = "2023-09-30") == 1
    assert candidate(date1 = "2016-02-28",date2 = "2016-03-01") == 2
    assert candidate(date1 = "1980-02-29",date2 = "1980-03-01") == 1
    assert candidate(date1 = "2025-06-15",date2 = "2026-06-15") == 365
    assert candidate(date1 = "2023-01-01",date2 = "2024-01-01") == 365
    assert candidate(date1 = "2023-05-05",date2 = "2022-05-05") == 365
    assert candidate(date1 = "2023-09-29",date2 = "2023-10-01") == 2
    assert candidate(date1 = "2016-02-29",date2 = "2016-03-01") == 1
    assert candidate(date1 = "1999-12-31",date2 = "2000-01-01") == 1
    assert candidate(date1 = "2019-09-15",date2 = "2023-09-15") == 1461


