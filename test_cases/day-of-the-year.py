def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(date = "2017-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2017-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-01-09") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-01-09") == 9: {e}')
    
    total += 1
    try:
        result = candidate(date = "1900-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1900-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2000-03-01") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2000-03-01") == 61: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-08-20") == 232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-08-20") == 232: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-30") == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-30") == 181: {e}')
    
    total += 1
    try:
        result = candidate(date = "1900-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1900-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-15") == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-15") == 166: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-02-10") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-02-10") == 41: {e}')
    
    total += 1
    try:
        result = candidate(date = "1901-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1901-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2000-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2000-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-15") == 319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-15") == 319: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-05-25") == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-05-25") == 145: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "2016-03-01") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2016-03-01") == 61: {e}')
    
    total += 1
    try:
        result = candidate(date = "2021-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2021-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-08-22") == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-08-22") == 234: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "1900-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1900-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2016-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2016-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-17") == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-17") == 198: {e}')
    
    total += 1
    try:
        result = candidate(date = "1999-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1999-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-15") == 349
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-15") == 349: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-09-05") == 248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-09-05") == 248: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-21") == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-21") == 172: {e}')
    
    total += 1
    try:
        result = candidate(date = "2023-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2023-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-12-31") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-12-31") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-06-30") == 181
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-06-30") == 181: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-09-30") == 273
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-09-30") == 273: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-25") == 206
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-25") == 206: {e}')
    
    total += 1
    try:
        result = candidate(date = "2023-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2023-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-10-15") == 288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-10-15") == 288: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-15") == 227
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-15") == 227: {e}')
    
    total += 1
    try:
        result = candidate(date = "2004-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2004-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-03-15") == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-03-15") == 74: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-18") == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-18") == 199: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-19") == 353
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-19") == 353: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-03-20") == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-03-20") == 79: {e}')
    
    total += 1
    try:
        result = candidate(date = "2021-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2021-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "1996-06-30") == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1996-06-30") == 182: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-05") == 217
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-05") == 217: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-25") == 176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-25") == 176: {e}')
    
    total += 1
    try:
        result = candidate(date = "1900-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1900-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-20") == 354
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-20") == 354: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2024-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2024-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-05") == 339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-05") == 339: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-05") == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-05") == 156: {e}')
    
    total += 1
    try:
        result = candidate(date = "2001-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2001-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2017-04-30") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2017-04-30") == 120: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2017-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2017-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-05-31") == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-05-31") == 151: {e}')
    
    total += 1
    try:
        result = candidate(date = "2016-12-31") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2016-12-31") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-10-10") == 283
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-10-10") == 283: {e}')
    
    total += 1
    try:
        result = candidate(date = "2012-06-17") == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2012-06-17") == 169: {e}')
    
    total += 1
    try:
        result = candidate(date = "2024-06-30") == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2024-06-30") == 182: {e}')
    
    total += 1
    try:
        result = candidate(date = "2000-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2000-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-04-25") == 115
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-04-25") == 115: {e}')
    
    total += 1
    try:
        result = candidate(date = "2004-03-01") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2004-03-01") == 61: {e}')
    
    total += 1
    try:
        result = candidate(date = "2023-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2023-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "1987-07-04") == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1987-07-04") == 185: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-06-10") == 161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-06-10") == 161: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-10-31") == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-10-31") == 304: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-10") == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-10") == 222: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-01-31") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-01-31") == 31: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-30") == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-30") == 364: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-07-24") == 205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-07-24") == 205: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-10") == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-10") == 191: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-22") == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-22") == 234: {e}')
    
    total += 1
    try:
        result = candidate(date = "2023-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2023-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-10") == 314
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-10") == 314: {e}')
    
    total += 1
    try:
        result = candidate(date = "2021-11-11") == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2021-11-11") == 315: {e}')
    
    total += 1
    try:
        result = candidate(date = "2024-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2024-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2021-03-01") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2021-03-01") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-10-05") == 278
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-10-05") == 278: {e}')
    
    total += 1
    try:
        result = candidate(date = "1955-10-31") == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1955-10-31") == 304: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-01") == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-01") == 335: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-05-15") == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-05-15") == 135: {e}')
    
    total += 1
    try:
        result = candidate(date = "1899-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1899-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "2000-01-01") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2000-01-01") == 1: {e}')
    
    total += 1
    try:
        result = candidate(date = "2100-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2100-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "1904-02-28") == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1904-02-28") == 59: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-03-30") == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-03-30") == 89: {e}')
    
    total += 1
    try:
        result = candidate(date = "1999-12-31") == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1999-12-31") == 365: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-30") == 334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-30") == 334: {e}')
    
    total += 1
    try:
        result = candidate(date = "2012-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2012-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-15") == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-15") == 196: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-04-30") == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-04-30") == 120: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-31") == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-31") == 243: {e}')
    
    total += 1
    try:
        result = candidate(date = "1904-12-31") == 366
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1904-12-31") == 366: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-07-15") == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-07-15") == 197: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-09-27") == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-09-27") == 270: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-01-02") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-01-02") == 2: {e}')
    
    total += 1
    try:
        result = candidate(date = "1916-04-15") == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1916-04-15") == 106: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-03-31") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-03-31") == 90: {e}')
    
    total += 1
    try:
        result = candidate(date = "2024-03-01") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2024-03-01") == 61: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-05-20") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-05-20") == 140: {e}')
    
    total += 1
    try:
        result = candidate(date = "2018-08-31") == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2018-08-31") == 243: {e}')
    
    total += 1
    try:
        result = candidate(date = "1904-02-29") == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1904-02-29") == 60: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-04-01") == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-04-01") == 91: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-20") == 324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-20") == 324: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-09-15") == 258
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-09-15") == 258: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-10-12") == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-10-12") == 285: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-09-10") == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-09-10") == 253: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-25") == 359
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-25") == 359: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-01") == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-01") == 305: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-08-09") == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-08-09") == 221: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-03-25") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-03-25") == 84: {e}')
    
    total += 1
    try:
        result = candidate(date = "2020-03-01") == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2020-03-01") == 61: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-12-10") == 344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-12-10") == 344: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-05") == 309
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-05") == 309: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-07-31") == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-07-31") == 212: {e}')
    
    total += 1
    try:
        result = candidate(date = "2019-11-08") == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2019-11-08") == 312: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(date = "2017-03-01") == 60
    assert candidate(date = "2019-01-09") == 9
    assert candidate(date = "1900-02-28") == 59
    assert candidate(date = "2000-03-01") == 61
    assert candidate(date = "2018-08-20") == 232
    assert candidate(date = "2019-06-30") == 181
    assert candidate(date = "1900-12-31") == 365
    assert candidate(date = "2019-06-15") == 166
    assert candidate(date = "2019-02-10") == 41
    assert candidate(date = "1901-01-01") == 1
    assert candidate(date = "2000-02-29") == 60
    assert candidate(date = "2019-11-15") == 319
    assert candidate(date = "2019-05-25") == 145
    assert candidate(date = "2019-12-31") == 365
    assert candidate(date = "2016-03-01") == 61
    assert candidate(date = "2021-01-01") == 1
    assert candidate(date = "2018-08-22") == 234
    assert candidate(date = "2020-02-29") == 60
    assert candidate(date = "1900-01-01") == 1
    assert candidate(date = "2016-02-29") == 60
    assert candidate(date = "2019-07-17") == 198
    assert candidate(date = "1999-02-28") == 59
    assert candidate(date = "2019-12-15") == 349
    assert candidate(date = "2019-09-05") == 248
    assert candidate(date = "2019-06-21") == 172
    assert candidate(date = "2023-02-28") == 59
    assert candidate(date = "2020-12-31") == 366
    assert candidate(date = "2018-06-30") == 181
    assert candidate(date = "2019-09-30") == 273
    assert candidate(date = "2019-07-25") == 206
    assert candidate(date = "2023-01-01") == 1
    assert candidate(date = "2019-10-15") == 288
    assert candidate(date = "2019-08-15") == 227
    assert candidate(date = "2004-02-29") == 60
    assert candidate(date = "2018-03-15") == 74
    assert candidate(date = "2019-03-01") == 60
    assert candidate(date = "2019-07-18") == 199
    assert candidate(date = "2019-12-19") == 353
    assert candidate(date = "2019-03-20") == 79
    assert candidate(date = "2021-12-31") == 365
    assert candidate(date = "1996-06-30") == 182
    assert candidate(date = "2019-08-05") == 217
    assert candidate(date = "2019-06-25") == 176
    assert candidate(date = "1900-03-01") == 60
    assert candidate(date = "2019-12-20") == 354
    assert candidate(date = "2018-03-01") == 60
    assert candidate(date = "2024-02-29") == 60
    assert candidate(date = "2019-12-05") == 339
    assert candidate(date = "2019-06-05") == 156
    assert candidate(date = "2001-02-28") == 59
    assert candidate(date = "2017-04-30") == 120
    assert candidate(date = "2018-02-28") == 59
    assert candidate(date = "2019-01-01") == 1
    assert candidate(date = "2017-01-01") == 1
    assert candidate(date = "2019-05-31") == 151
    assert candidate(date = "2016-12-31") == 366
    assert candidate(date = "2019-10-10") == 283
    assert candidate(date = "2012-06-17") == 169
    assert candidate(date = "2024-06-30") == 182
    assert candidate(date = "2000-02-28") == 59
    assert candidate(date = "2019-04-25") == 115
    assert candidate(date = "2004-03-01") == 61
    assert candidate(date = "2023-12-31") == 365
    assert candidate(date = "1987-07-04") == 185
    assert candidate(date = "2019-06-10") == 161
    assert candidate(date = "2019-10-31") == 304
    assert candidate(date = "2019-08-10") == 222
    assert candidate(date = "2019-01-31") == 31
    assert candidate(date = "2019-12-30") == 364
    assert candidate(date = "2018-07-24") == 205
    assert candidate(date = "2020-01-01") == 1
    assert candidate(date = "2019-07-10") == 191
    assert candidate(date = "2019-02-28") == 59
    assert candidate(date = "2019-08-22") == 234
    assert candidate(date = "2023-03-01") == 60
    assert candidate(date = "2019-11-10") == 314
    assert candidate(date = "2021-11-11") == 315
    assert candidate(date = "2024-02-28") == 59
    assert candidate(date = "2021-03-01") == 60
    assert candidate(date = "2019-10-05") == 278
    assert candidate(date = "1955-10-31") == 304
    assert candidate(date = "2020-02-28") == 59
    assert candidate(date = "2019-12-01") == 335
    assert candidate(date = "2019-05-15") == 135
    assert candidate(date = "1899-12-31") == 365
    assert candidate(date = "2000-01-01") == 1
    assert candidate(date = "2100-02-28") == 59
    assert candidate(date = "1904-02-28") == 59
    assert candidate(date = "2019-03-30") == 89
    assert candidate(date = "1999-12-31") == 365
    assert candidate(date = "2019-11-30") == 334
    assert candidate(date = "2012-02-29") == 60
    assert candidate(date = "2019-07-15") == 196
    assert candidate(date = "2019-04-30") == 120
    assert candidate(date = "2019-08-31") == 243
    assert candidate(date = "1904-12-31") == 366
    assert candidate(date = "2020-07-15") == 197
    assert candidate(date = "2019-09-27") == 270
    assert candidate(date = "2019-01-02") == 2
    assert candidate(date = "1916-04-15") == 106
    assert candidate(date = "2019-03-31") == 90
    assert candidate(date = "2024-03-01") == 61
    assert candidate(date = "2019-05-20") == 140
    assert candidate(date = "2018-08-31") == 243
    assert candidate(date = "1904-02-29") == 60
    assert candidate(date = "2019-04-01") == 91
    assert candidate(date = "2019-11-20") == 324
    assert candidate(date = "2019-09-15") == 258
    assert candidate(date = "2019-10-12") == 285
    assert candidate(date = "2019-09-10") == 253
    assert candidate(date = "2019-12-25") == 359
    assert candidate(date = "2019-11-01") == 305
    assert candidate(date = "2019-08-09") == 221
    assert candidate(date = "2019-03-25") == 84
    assert candidate(date = "2020-03-01") == 61
    assert candidate(date = "2019-12-10") == 344
    assert candidate(date = "2019-11-05") == 309
    assert candidate(date = "2019-07-31") == 212
    assert candidate(date = "2019-11-08") == 312


