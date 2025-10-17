def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(primeOne = 19,primeTwo = 23) == 395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 19,primeTwo = 23) == 395: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 5,primeTwo = 7) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 5,primeTwo = 7) == 23: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 2,primeTwo = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 2,primeTwo = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 11,primeTwo = 17) == 159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 11,primeTwo = 17) == 159: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 7,primeTwo = 13) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 7,primeTwo = 13) == 71: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 13,primeTwo = 17) == 191
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 13,primeTwo = 17) == 191: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 3,primeTwo = 11) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 3,primeTwo = 11) == 19: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 157,primeTwo = 163) == 25271
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 157,primeTwo = 163) == 25271: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 31,primeTwo = 61) == 1799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 31,primeTwo = 61) == 1799: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 109,primeTwo = 151) == 16199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 109,primeTwo = 151) == 16199: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 191,primeTwo = 193) == 36479
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 191,primeTwo = 193) == 36479: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 331,primeTwo = 353) == 116159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 331,primeTwo = 353) == 116159: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 53,primeTwo = 59) == 3015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 53,primeTwo = 59) == 3015: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 79,primeTwo = 83) == 6395
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 79,primeTwo = 83) == 6395: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 353,primeTwo = 359) == 126015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 353,primeTwo = 359) == 126015: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 47,primeTwo = 71) == 3219
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 47,primeTwo = 71) == 3219: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 173,primeTwo = 199) == 34055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 173,primeTwo = 199) == 34055: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 373,primeTwo = 379) == 140615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 373,primeTwo = 379) == 140615: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 29,primeTwo = 31) == 839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 29,primeTwo = 31) == 839: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 3,primeTwo = 13) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 3,primeTwo = 13) == 23: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 389,primeTwo = 397) == 153647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 389,primeTwo = 397) == 153647: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 73,primeTwo = 97) == 6911
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 73,primeTwo = 97) == 6911: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 103,primeTwo = 107) == 10811
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 103,primeTwo = 107) == 10811: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 47,primeTwo = 53) == 2391
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 47,primeTwo = 53) == 2391: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 71,primeTwo = 79) == 5459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 71,primeTwo = 79) == 5459: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 131,primeTwo = 139) == 17939
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 131,primeTwo = 139) == 17939: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 11,primeTwo = 29) == 279
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 11,primeTwo = 29) == 279: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 71,primeTwo = 73) == 5039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 71,primeTwo = 73) == 5039: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 31,primeTwo = 37) == 1079
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 31,primeTwo = 37) == 1079: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 149,primeTwo = 151) == 22199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 149,primeTwo = 151) == 22199: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 107,primeTwo = 109) == 11447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 107,primeTwo = 109) == 11447: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 61,primeTwo = 67) == 3959
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 61,primeTwo = 67) == 3959: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 179,primeTwo = 191) == 33819
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 179,primeTwo = 191) == 33819: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 101,primeTwo = 103) == 10199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 101,primeTwo = 103) == 10199: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 509,primeTwo = 521) == 264159
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 509,primeTwo = 521) == 264159: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 211,primeTwo = 223) == 46619
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 211,primeTwo = 223) == 46619: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 89,primeTwo = 97) == 8447
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 89,primeTwo = 97) == 8447: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 151,primeTwo = 179) == 26699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 151,primeTwo = 179) == 26699: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 41,primeTwo = 47) == 1839
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 41,primeTwo = 47) == 1839: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 229,primeTwo = 233) == 52895
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 229,primeTwo = 233) == 52895: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 401,primeTwo = 409) == 163199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 401,primeTwo = 409) == 163199: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 191,primeTwo = 223) == 42179
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 191,primeTwo = 223) == 42179: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 227,primeTwo = 251) == 56499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 227,primeTwo = 251) == 56499: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 109,primeTwo = 113) == 12095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 109,primeTwo = 113) == 12095: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 131,primeTwo = 137) == 17679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 131,primeTwo = 137) == 17679: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 23,primeTwo = 29) == 615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 23,primeTwo = 29) == 615: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 233,primeTwo = 239) == 55215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 233,primeTwo = 239) == 55215: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 421,primeTwo = 431) == 180599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 421,primeTwo = 431) == 180599: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 701,primeTwo = 719) == 502599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 701,primeTwo = 719) == 502599: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 23,primeTwo = 41) == 879
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 23,primeTwo = 41) == 879: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 97,primeTwo = 101) == 9599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 97,primeTwo = 101) == 9599: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 7,primeTwo = 19) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 7,primeTwo = 19) == 107: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 41,primeTwo = 43) == 1679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 41,primeTwo = 43) == 1679: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 907,primeTwo = 911) == 824459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 907,primeTwo = 911) == 824459: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 17,primeTwo = 23) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 17,primeTwo = 23) == 351: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 163,primeTwo = 167) == 26891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 163,primeTwo = 167) == 26891: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 331,primeTwo = 337) == 110879
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 331,primeTwo = 337) == 110879: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 37,primeTwo = 41) == 1439
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 37,primeTwo = 41) == 1439: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 241,primeTwo = 251) == 59999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 241,primeTwo = 251) == 59999: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 59,primeTwo = 83) == 4755
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 59,primeTwo = 83) == 4755: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 263,primeTwo = 271) == 70739
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 263,primeTwo = 271) == 70739: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 139,primeTwo = 149) == 20423
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 139,primeTwo = 149) == 20423: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 113,primeTwo = 127) == 14111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 113,primeTwo = 127) == 14111: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 233,primeTwo = 263) == 60783
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 233,primeTwo = 263) == 60783: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 101,primeTwo = 131) == 12999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 101,primeTwo = 131) == 12999: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 29,primeTwo = 53) == 1455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 29,primeTwo = 53) == 1455: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 113,primeTwo = 149) == 16575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 113,primeTwo = 149) == 16575: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 809,primeTwo = 821) == 662559
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 809,primeTwo = 821) == 662559: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 151,primeTwo = 157) == 23399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 151,primeTwo = 157) == 23399: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 281,primeTwo = 293) == 81759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 281,primeTwo = 293) == 81759: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 239,primeTwo = 271) == 64259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 239,primeTwo = 271) == 64259: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 53,primeTwo = 61) == 3119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 53,primeTwo = 61) == 3119: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 101,primeTwo = 109) == 10799
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 101,primeTwo = 109) == 10799: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 59,primeTwo = 61) == 3479
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 59,primeTwo = 61) == 3479: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 43,primeTwo = 47) == 1931
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 43,primeTwo = 47) == 1931: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 601,primeTwo = 617) == 369599
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 601,primeTwo = 617) == 369599: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 83,primeTwo = 89) == 7215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 83,primeTwo = 89) == 7215: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 137,primeTwo = 167) == 22575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 137,primeTwo = 167) == 22575: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 311,primeTwo = 313) == 96719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 311,primeTwo = 313) == 96719: {e}')
    
    total += 1
    try:
        result = candidate(primeOne = 179,primeTwo = 181) == 32039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(primeOne = 179,primeTwo = 181) == 32039: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(primeOne = 19,primeTwo = 23) == 395
    assert candidate(primeOne = 5,primeTwo = 7) == 23
    assert candidate(primeOne = 2,primeTwo = 5) == 3
    assert candidate(primeOne = 11,primeTwo = 17) == 159
    assert candidate(primeOne = 7,primeTwo = 13) == 71
    assert candidate(primeOne = 13,primeTwo = 17) == 191
    assert candidate(primeOne = 3,primeTwo = 11) == 19
    assert candidate(primeOne = 157,primeTwo = 163) == 25271
    assert candidate(primeOne = 31,primeTwo = 61) == 1799
    assert candidate(primeOne = 109,primeTwo = 151) == 16199
    assert candidate(primeOne = 191,primeTwo = 193) == 36479
    assert candidate(primeOne = 331,primeTwo = 353) == 116159
    assert candidate(primeOne = 53,primeTwo = 59) == 3015
    assert candidate(primeOne = 79,primeTwo = 83) == 6395
    assert candidate(primeOne = 353,primeTwo = 359) == 126015
    assert candidate(primeOne = 47,primeTwo = 71) == 3219
    assert candidate(primeOne = 173,primeTwo = 199) == 34055
    assert candidate(primeOne = 373,primeTwo = 379) == 140615
    assert candidate(primeOne = 29,primeTwo = 31) == 839
    assert candidate(primeOne = 3,primeTwo = 13) == 23
    assert candidate(primeOne = 389,primeTwo = 397) == 153647
    assert candidate(primeOne = 73,primeTwo = 97) == 6911
    assert candidate(primeOne = 103,primeTwo = 107) == 10811
    assert candidate(primeOne = 47,primeTwo = 53) == 2391
    assert candidate(primeOne = 71,primeTwo = 79) == 5459
    assert candidate(primeOne = 131,primeTwo = 139) == 17939
    assert candidate(primeOne = 11,primeTwo = 29) == 279
    assert candidate(primeOne = 71,primeTwo = 73) == 5039
    assert candidate(primeOne = 31,primeTwo = 37) == 1079
    assert candidate(primeOne = 149,primeTwo = 151) == 22199
    assert candidate(primeOne = 107,primeTwo = 109) == 11447
    assert candidate(primeOne = 61,primeTwo = 67) == 3959
    assert candidate(primeOne = 179,primeTwo = 191) == 33819
    assert candidate(primeOne = 101,primeTwo = 103) == 10199
    assert candidate(primeOne = 509,primeTwo = 521) == 264159
    assert candidate(primeOne = 211,primeTwo = 223) == 46619
    assert candidate(primeOne = 89,primeTwo = 97) == 8447
    assert candidate(primeOne = 151,primeTwo = 179) == 26699
    assert candidate(primeOne = 41,primeTwo = 47) == 1839
    assert candidate(primeOne = 229,primeTwo = 233) == 52895
    assert candidate(primeOne = 401,primeTwo = 409) == 163199
    assert candidate(primeOne = 191,primeTwo = 223) == 42179
    assert candidate(primeOne = 227,primeTwo = 251) == 56499
    assert candidate(primeOne = 109,primeTwo = 113) == 12095
    assert candidate(primeOne = 131,primeTwo = 137) == 17679
    assert candidate(primeOne = 23,primeTwo = 29) == 615
    assert candidate(primeOne = 233,primeTwo = 239) == 55215
    assert candidate(primeOne = 421,primeTwo = 431) == 180599
    assert candidate(primeOne = 701,primeTwo = 719) == 502599
    assert candidate(primeOne = 23,primeTwo = 41) == 879
    assert candidate(primeOne = 97,primeTwo = 101) == 9599
    assert candidate(primeOne = 7,primeTwo = 19) == 107
    assert candidate(primeOne = 41,primeTwo = 43) == 1679
    assert candidate(primeOne = 907,primeTwo = 911) == 824459
    assert candidate(primeOne = 17,primeTwo = 23) == 351
    assert candidate(primeOne = 163,primeTwo = 167) == 26891
    assert candidate(primeOne = 331,primeTwo = 337) == 110879
    assert candidate(primeOne = 37,primeTwo = 41) == 1439
    assert candidate(primeOne = 241,primeTwo = 251) == 59999
    assert candidate(primeOne = 59,primeTwo = 83) == 4755
    assert candidate(primeOne = 263,primeTwo = 271) == 70739
    assert candidate(primeOne = 139,primeTwo = 149) == 20423
    assert candidate(primeOne = 113,primeTwo = 127) == 14111
    assert candidate(primeOne = 233,primeTwo = 263) == 60783
    assert candidate(primeOne = 101,primeTwo = 131) == 12999
    assert candidate(primeOne = 29,primeTwo = 53) == 1455
    assert candidate(primeOne = 113,primeTwo = 149) == 16575
    assert candidate(primeOne = 809,primeTwo = 821) == 662559
    assert candidate(primeOne = 151,primeTwo = 157) == 23399
    assert candidate(primeOne = 281,primeTwo = 293) == 81759
    assert candidate(primeOne = 239,primeTwo = 271) == 64259
    assert candidate(primeOne = 53,primeTwo = 61) == 3119
    assert candidate(primeOne = 101,primeTwo = 109) == 10799
    assert candidate(primeOne = 59,primeTwo = 61) == 3479
    assert candidate(primeOne = 43,primeTwo = 47) == 1931
    assert candidate(primeOne = 601,primeTwo = 617) == 369599
    assert candidate(primeOne = 83,primeTwo = 89) == 7215
    assert candidate(primeOne = 137,primeTwo = 167) == 22575
    assert candidate(primeOne = 311,primeTwo = 313) == 96719
    assert candidate(primeOne = 179,primeTwo = 181) == 32039


