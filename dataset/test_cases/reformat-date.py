def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(date = "15th Aug 2022") == "2022-08-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "15th Aug 2022") == "2022-08-15": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Aug 1999") == "1999-08-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Aug 1999") == "1999-08-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Mar 1987") == "1987-03-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Mar 1987") == "1987-03-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Nov 2022") == "2022-11-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Nov 2022") == "2022-11-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Mar 2020") == "2020-03-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Mar 2020") == "2020-03-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "15th Nov 2000") == "2000-11-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "15th Nov 2000") == "2000-11-15": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Mar 2010") == "2010-03-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Mar 2010") == "2010-03-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "31st Dec 2100") == "2100-12-31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "31st Dec 2100") == "2100-12-31": {e}')
    
    total += 1
    try:
        result = candidate(date = "25th Dec 2000") == "2000-12-25"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "25th Dec 2000") == "2000-12-25": {e}')
    
    total += 1
    try:
        result = candidate(date = "11th Sep 2023") == "2023-09-11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "11th Sep 2023") == "2023-09-11": {e}')
    
    total += 1
    try:
        result = candidate(date = "15th Nov 1999") == "1999-11-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "15th Nov 1999") == "1999-11-15": {e}')
    
    total += 1
    try:
        result = candidate(date = "15th Nov 2020") == "2020-11-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "15th Nov 2020") == "2020-11-15": {e}')
    
    total += 1
    try:
        result = candidate(date = "11th Mar 2000") == "2000-03-11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "11th Mar 2000") == "2000-03-11": {e}')
    
    total += 1
    try:
        result = candidate(date = "5th Sep 1899") == "1899-09-05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "5th Sep 1899") == "1899-09-05": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Apr 2015") == "2015-04-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Apr 2015") == "2015-04-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "26th May 1960") == "1960-05-26"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "26th May 1960") == "1960-05-26": {e}')
    
    total += 1
    try:
        result = candidate(date = "11th Sep 1999") == "1999-09-11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "11th Sep 1999") == "1999-09-11": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 1900") == "1900-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 1900") == "1900-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "20th Oct 2052") == "2052-10-20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "20th Oct 2052") == "2052-10-20": {e}')
    
    total += 1
    try:
        result = candidate(date = "6th Jun 1933") == "1933-06-06"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "6th Jun 1933") == "1933-06-06": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Mar 2015") == "2015-03-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Mar 2015") == "2015-03-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "1st Jan 1900") == "1900-01-01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1st Jan 1900") == "1900-01-01": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 1996") == "1996-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 1996") == "1996-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "29th Feb 2004") == "2004-02-29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "29th Feb 2004") == "2004-02-29": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Feb 2020") == "2020-02-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Feb 2020") == "2020-02-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "11th Sep 2020") == "2020-09-11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "11th Sep 2020") == "2020-09-11": {e}')
    
    total += 1
    try:
        result = candidate(date = "29th Feb 2000") == "2000-02-29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "29th Feb 2000") == "2000-02-29": {e}')
    
    total += 1
    try:
        result = candidate(date = "8th Feb 1987") == "1987-02-08"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "8th Feb 1987") == "1987-02-08": {e}')
    
    total += 1
    try:
        result = candidate(date = "31st Jan 2100") == "2100-01-31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "31st Jan 2100") == "2100-01-31": {e}')
    
    total += 1
    try:
        result = candidate(date = "5th Nov 1999") == "1999-11-05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "5th Nov 1999") == "1999-11-05": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Sep 1965") == "1965-09-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Sep 1965") == "1965-09-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "27th Jun 2012") == "2012-06-27"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "27th Jun 2012") == "2012-06-27": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Nov 2010") == "2010-11-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Nov 2010") == "2010-11-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "19th Dec 2099") == "2099-12-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "19th Dec 2099") == "2099-12-19": {e}')
    
    total += 1
    try:
        result = candidate(date = "31st May 2023") == "2023-05-31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "31st May 2023") == "2023-05-31": {e}')
    
    total += 1
    try:
        result = candidate(date = "31st Dec 2099") == "2099-12-31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "31st Dec 2099") == "2099-12-31": {e}')
    
    total += 1
    try:
        result = candidate(date = "4th Mar 2003") == "2003-03-04"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "4th Mar 2003") == "2003-03-04": {e}')
    
    total += 1
    try:
        result = candidate(date = "24th Jun 2050") == "2050-06-24"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "24th Jun 2050") == "2050-06-24": {e}')
    
    total += 1
    try:
        result = candidate(date = "23rd Apr 2040") == "2040-04-23"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "23rd Apr 2040") == "2040-04-23": {e}')
    
    total += 1
    try:
        result = candidate(date = "27th Sep 2077") == "2077-09-27"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "27th Sep 2077") == "2077-09-27": {e}')
    
    total += 1
    try:
        result = candidate(date = "6th Mar 2077") == "2077-03-06"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "6th Mar 2077") == "2077-03-06": {e}')
    
    total += 1
    try:
        result = candidate(date = "18th Jun 2050") == "2050-06-18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "18th Jun 2050") == "2050-06-18": {e}')
    
    total += 1
    try:
        result = candidate(date = "10th Oct 2033") == "2033-10-10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "10th Oct 2033") == "2033-10-10": {e}')
    
    total += 1
    try:
        result = candidate(date = "29th Apr 1999") == "1999-04-29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "29th Apr 1999") == "1999-04-29": {e}')
    
    total += 1
    try:
        result = candidate(date = "25th Oct 2050") == "2050-10-25"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "25th Oct 2050") == "2050-10-25": {e}')
    
    total += 1
    try:
        result = candidate(date = "14th May 2005") == "2005-05-14"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "14th May 2005") == "2005-05-14": {e}')
    
    total += 1
    try:
        result = candidate(date = "23rd Oct 2005") == "2005-10-23"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "23rd Oct 2005") == "2005-10-23": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Apr 2047") == "2047-04-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Apr 2047") == "2047-04-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "19th Aug 2076") == "2076-08-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "19th Aug 2076") == "2076-08-19": {e}')
    
    total += 1
    try:
        result = candidate(date = "21st Jun 1972") == "1972-06-21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "21st Jun 1972") == "1972-06-21": {e}')
    
    total += 1
    try:
        result = candidate(date = "18th May 1950") == "1950-05-18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "18th May 1950") == "1950-05-18": {e}')
    
    total += 1
    try:
        result = candidate(date = "4th Nov 2035") == "2035-11-04"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "4th Nov 2035") == "2035-11-04": {e}')
    
    total += 1
    try:
        result = candidate(date = "29th Feb 2020") == "2020-02-29"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "29th Feb 2020") == "2020-02-29": {e}')
    
    total += 1
    try:
        result = candidate(date = "9th Sep 1987") == "1987-09-09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "9th Sep 1987") == "1987-09-09": {e}')
    
    total += 1
    try:
        result = candidate(date = "31st Jan 1980") == "1980-01-31"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "31st Jan 1980") == "1980-01-31": {e}')
    
    total += 1
    try:
        result = candidate(date = "18th Sep 2089") == "2089-09-18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "18th Sep 2089") == "2089-09-18": {e}')
    
    total += 1
    try:
        result = candidate(date = "21st Aug 1955") == "1955-08-21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "21st Aug 1955") == "1955-08-21": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Nov 1969") == "1969-11-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Nov 1969") == "1969-11-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "27th Oct 2075") == "2075-10-27"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "27th Oct 2075") == "2075-10-27": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Nov 2021") == "2021-11-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Nov 2021") == "2021-11-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "18th Jul 1950") == "1950-07-18"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "18th Jul 1950") == "1950-07-18": {e}')
    
    total += 1
    try:
        result = candidate(date = "12th Aug 2022") == "2022-08-12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "12th Aug 2022") == "2022-08-12": {e}')
    
    total += 1
    try:
        result = candidate(date = "19th Dec 2021") == "2021-12-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "19th Dec 2021") == "2021-12-19": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Jul 1970") == "1970-07-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Jul 1970") == "1970-07-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "7th Dec 2099") == "2099-12-07"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "7th Dec 2099") == "2099-12-07": {e}')
    
    total += 1
    try:
        result = candidate(date = "9th Jun 2040") == "2040-06-09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "9th Jun 2040") == "2040-06-09": {e}')
    
    total += 1
    try:
        result = candidate(date = "21st Nov 2050") == "2050-11-21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "21st Nov 2050") == "2050-11-21": {e}')
    
    total += 1
    try:
        result = candidate(date = "16th May 2067") == "2067-05-16"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "16th May 2067") == "2067-05-16": {e}')
    
    total += 1
    try:
        result = candidate(date = "14th Oct 1960") == "1960-10-14"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "14th Oct 1960") == "1960-10-14": {e}')
    
    total += 1
    try:
        result = candidate(date = "25th Dec 1984") == "1984-12-25"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "25th Dec 1984") == "1984-12-25": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Sep 2050") == "2050-09-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Sep 2050") == "2050-09-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 2000") == "2000-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 2000") == "2000-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "15th Aug 2024") == "2024-08-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "15th Aug 2024") == "2024-08-15": {e}')
    
    total += 1
    try:
        result = candidate(date = "5th Oct 2100") == "2100-10-05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "5th Oct 2100") == "2100-10-05": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Aug 2022") == "2022-08-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Aug 2022") == "2022-08-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "21st Sep 1989") == "1989-09-21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "21st Sep 1989") == "1989-09-21": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Mar 2015") == "2015-03-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Mar 2015") == "2015-03-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "12th Mar 2021") == "2021-03-12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "12th Mar 2021") == "2021-03-12": {e}')
    
    total += 1
    try:
        result = candidate(date = "13th Dec 2033") == "2033-12-13"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "13th Dec 2033") == "2033-12-13": {e}')
    
    total += 1
    try:
        result = candidate(date = "13th Aug 1984") == "1984-08-13"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "13th Aug 1984") == "1984-08-13": {e}')
    
    total += 1
    try:
        result = candidate(date = "3rd Mar 2030") == "2030-03-03"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "3rd Mar 2030") == "2030-03-03": {e}')
    
    total += 1
    try:
        result = candidate(date = "13th Aug 2023") == "2023-08-13"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "13th Aug 2023") == "2023-08-13": {e}')
    
    total += 1
    try:
        result = candidate(date = "10th Oct 1899") == "1899-10-10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "10th Oct 1899") == "1899-10-10": {e}')
    
    total += 1
    try:
        result = candidate(date = "17th Mar 1925") == "1925-03-17"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "17th Mar 1925") == "1925-03-17": {e}')
    
    total += 1
    try:
        result = candidate(date = "21st Dec 1900") == "1900-12-21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "21st Dec 1900") == "1900-12-21": {e}')
    
    total += 1
    try:
        result = candidate(date = "4th Mar 1921") == "1921-03-04"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "4th Mar 1921") == "1921-03-04": {e}')
    
    total += 1
    try:
        result = candidate(date = "24th Jun 1998") == "1998-06-24"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "24th Jun 1998") == "1998-06-24": {e}')
    
    total += 1
    try:
        result = candidate(date = "22nd Jul 2034") == "2034-07-22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "22nd Jul 2034") == "2034-07-22": {e}')
    
    total += 1
    try:
        result = candidate(date = "25th Jun 2023") == "2023-06-25"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "25th Jun 2023") == "2023-06-25": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Nov 2045") == "2045-11-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Nov 2045") == "2045-11-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Apr 2000") == "2000-04-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Apr 2000") == "2000-04-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 1999") == "1999-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 1999") == "1999-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Jan 1901") == "1901-01-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Jan 1901") == "1901-01-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "1st Mar 2024") == "2024-03-01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "1st Mar 2024") == "2024-03-01": {e}')
    
    total += 1
    try:
        result = candidate(date = "5th Jul 1955") == "1955-07-05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "5th Jul 1955") == "1955-07-05": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 2001") == "2001-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 2001") == "2001-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "9th Dec 2030") == "2030-12-09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "9th Dec 2030") == "2030-12-09": {e}')
    
    total += 1
    try:
        result = candidate(date = "5th Oct 1987") == "1987-10-05"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "5th Oct 1987") == "1987-10-05": {e}')
    
    total += 1
    try:
        result = candidate(date = "10th Mar 2012") == "2012-03-10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "10th Mar 2012") == "2012-03-10": {e}')
    
    total += 1
    try:
        result = candidate(date = "7th Jun 2080") == "2080-06-07"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "7th Jun 2080") == "2080-06-07": {e}')
    
    total += 1
    try:
        result = candidate(date = "9th Jul 1987") == "1987-07-09"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "9th Jul 1987") == "1987-07-09": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 1901") == "1901-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 1901") == "1901-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "7th Jul 2021") == "2021-07-07"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "7th Jul 2021") == "2021-07-07": {e}')
    
    total += 1
    try:
        result = candidate(date = "7th Nov 1969") == "1969-11-07"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "7th Nov 1969") == "1969-11-07": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Mar 1990") == "1990-03-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Mar 1990") == "1990-03-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "28th Feb 2004") == "2004-02-28"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "28th Feb 2004") == "2004-02-28": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Apr 2077") == "2077-04-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Apr 2077") == "2077-04-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "30th Apr 2100") == "2100-04-30"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "30th Apr 2100") == "2100-04-30": {e}')
    
    total += 1
    try:
        result = candidate(date = "12th Sep 1995") == "1995-09-12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "12th Sep 1995") == "1995-09-12": {e}')
    
    total += 1
    try:
        result = candidate(date = "2nd Apr 2023") == "2023-04-02"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "2nd Apr 2023") == "2023-04-02": {e}')
    
    total += 1
    try:
        result = candidate(date = "17th Oct 2061") == "2061-10-17"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(date = "17th Oct 2061") == "2061-10-17": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(date = "15th Aug 2022") == "2022-08-15"
    assert candidate(date = "22nd Aug 1999") == "1999-08-22"
    assert candidate(date = "3rd Mar 1987") == "1987-03-03"
    assert candidate(date = "3rd Nov 2022") == "2022-11-03"
    assert candidate(date = "2nd Mar 2020") == "2020-03-02"
    assert candidate(date = "15th Nov 2000") == "2000-11-15"
    assert candidate(date = "2nd Mar 2010") == "2010-03-02"
    assert candidate(date = "31st Dec 2100") == "2100-12-31"
    assert candidate(date = "25th Dec 2000") == "2000-12-25"
    assert candidate(date = "11th Sep 2023") == "2023-09-11"
    assert candidate(date = "15th Nov 1999") == "1999-11-15"
    assert candidate(date = "15th Nov 2020") == "2020-11-15"
    assert candidate(date = "11th Mar 2000") == "2000-03-11"
    assert candidate(date = "5th Sep 1899") == "1899-09-05"
    assert candidate(date = "3rd Apr 2015") == "2015-04-03"
    assert candidate(date = "26th May 1960") == "1960-05-26"
    assert candidate(date = "11th Sep 1999") == "1999-09-11"
    assert candidate(date = "28th Feb 1900") == "1900-02-28"
    assert candidate(date = "20th Oct 2052") == "2052-10-20"
    assert candidate(date = "6th Jun 1933") == "1933-06-06"
    assert candidate(date = "2nd Mar 2015") == "2015-03-02"
    assert candidate(date = "1st Jan 1900") == "1900-01-01"
    assert candidate(date = "28th Feb 1996") == "1996-02-28"
    assert candidate(date = "29th Feb 2004") == "2004-02-29"
    assert candidate(date = "2nd Feb 2020") == "2020-02-02"
    assert candidate(date = "11th Sep 2020") == "2020-09-11"
    assert candidate(date = "29th Feb 2000") == "2000-02-29"
    assert candidate(date = "8th Feb 1987") == "1987-02-08"
    assert candidate(date = "31st Jan 2100") == "2100-01-31"
    assert candidate(date = "5th Nov 1999") == "1999-11-05"
    assert candidate(date = "22nd Sep 1965") == "1965-09-22"
    assert candidate(date = "27th Jun 2012") == "2012-06-27"
    assert candidate(date = "30th Nov 2010") == "2010-11-30"
    assert candidate(date = "19th Dec 2099") == "2099-12-19"
    assert candidate(date = "31st May 2023") == "2023-05-31"
    assert candidate(date = "31st Dec 2099") == "2099-12-31"
    assert candidate(date = "4th Mar 2003") == "2003-03-04"
    assert candidate(date = "24th Jun 2050") == "2050-06-24"
    assert candidate(date = "23rd Apr 2040") == "2040-04-23"
    assert candidate(date = "27th Sep 2077") == "2077-09-27"
    assert candidate(date = "6th Mar 2077") == "2077-03-06"
    assert candidate(date = "18th Jun 2050") == "2050-06-18"
    assert candidate(date = "10th Oct 2033") == "2033-10-10"
    assert candidate(date = "29th Apr 1999") == "1999-04-29"
    assert candidate(date = "25th Oct 2050") == "2050-10-25"
    assert candidate(date = "14th May 2005") == "2005-05-14"
    assert candidate(date = "23rd Oct 2005") == "2005-10-23"
    assert candidate(date = "30th Apr 2047") == "2047-04-30"
    assert candidate(date = "19th Aug 2076") == "2076-08-19"
    assert candidate(date = "21st Jun 1972") == "1972-06-21"
    assert candidate(date = "18th May 1950") == "1950-05-18"
    assert candidate(date = "4th Nov 2035") == "2035-11-04"
    assert candidate(date = "29th Feb 2020") == "2020-02-29"
    assert candidate(date = "9th Sep 1987") == "1987-09-09"
    assert candidate(date = "31st Jan 1980") == "1980-01-31"
    assert candidate(date = "18th Sep 2089") == "2089-09-18"
    assert candidate(date = "21st Aug 1955") == "1955-08-21"
    assert candidate(date = "30th Nov 1969") == "1969-11-30"
    assert candidate(date = "27th Oct 2075") == "2075-10-27"
    assert candidate(date = "3rd Nov 2021") == "2021-11-03"
    assert candidate(date = "18th Jul 1950") == "1950-07-18"
    assert candidate(date = "12th Aug 2022") == "2022-08-12"
    assert candidate(date = "19th Dec 2021") == "2021-12-19"
    assert candidate(date = "3rd Jul 1970") == "1970-07-03"
    assert candidate(date = "7th Dec 2099") == "2099-12-07"
    assert candidate(date = "9th Jun 2040") == "2040-06-09"
    assert candidate(date = "21st Nov 2050") == "2050-11-21"
    assert candidate(date = "16th May 2067") == "2067-05-16"
    assert candidate(date = "14th Oct 1960") == "1960-10-14"
    assert candidate(date = "25th Dec 1984") == "1984-12-25"
    assert candidate(date = "22nd Sep 2050") == "2050-09-22"
    assert candidate(date = "28th Feb 2000") == "2000-02-28"
    assert candidate(date = "15th Aug 2024") == "2024-08-15"
    assert candidate(date = "5th Oct 2100") == "2100-10-05"
    assert candidate(date = "22nd Aug 2022") == "2022-08-22"
    assert candidate(date = "21st Sep 1989") == "1989-09-21"
    assert candidate(date = "22nd Mar 2015") == "2015-03-22"
    assert candidate(date = "12th Mar 2021") == "2021-03-12"
    assert candidate(date = "13th Dec 2033") == "2033-12-13"
    assert candidate(date = "13th Aug 1984") == "1984-08-13"
    assert candidate(date = "3rd Mar 2030") == "2030-03-03"
    assert candidate(date = "13th Aug 2023") == "2023-08-13"
    assert candidate(date = "10th Oct 1899") == "1899-10-10"
    assert candidate(date = "17th Mar 1925") == "1925-03-17"
    assert candidate(date = "21st Dec 1900") == "1900-12-21"
    assert candidate(date = "4th Mar 1921") == "1921-03-04"
    assert candidate(date = "24th Jun 1998") == "1998-06-24"
    assert candidate(date = "22nd Jul 2034") == "2034-07-22"
    assert candidate(date = "25th Jun 2023") == "2023-06-25"
    assert candidate(date = "30th Nov 2045") == "2045-11-30"
    assert candidate(date = "30th Apr 2000") == "2000-04-30"
    assert candidate(date = "28th Feb 1999") == "1999-02-28"
    assert candidate(date = "2nd Jan 1901") == "1901-01-02"
    assert candidate(date = "1st Mar 2024") == "2024-03-01"
    assert candidate(date = "5th Jul 1955") == "1955-07-05"
    assert candidate(date = "28th Feb 2001") == "2001-02-28"
    assert candidate(date = "9th Dec 2030") == "2030-12-09"
    assert candidate(date = "5th Oct 1987") == "1987-10-05"
    assert candidate(date = "10th Mar 2012") == "2012-03-10"
    assert candidate(date = "7th Jun 2080") == "2080-06-07"
    assert candidate(date = "9th Jul 1987") == "1987-07-09"
    assert candidate(date = "28th Feb 1901") == "1901-02-28"
    assert candidate(date = "7th Jul 2021") == "2021-07-07"
    assert candidate(date = "7th Nov 1969") == "1969-11-07"
    assert candidate(date = "2nd Mar 1990") == "1990-03-02"
    assert candidate(date = "28th Feb 2004") == "2004-02-28"
    assert candidate(date = "30th Apr 2077") == "2077-04-30"
    assert candidate(date = "30th Apr 2100") == "2100-04-30"
    assert candidate(date = "12th Sep 1995") == "1995-09-12"
    assert candidate(date = "2nd Apr 2023") == "2023-04-02"
    assert candidate(date = "17th Oct 2061") == "2061-10-17"


