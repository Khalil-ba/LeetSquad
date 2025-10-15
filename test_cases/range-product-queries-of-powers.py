def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0], [1, 1], [0, 2]]) == [2, 8, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0], [1, 1], [0, 2]]) == [2, 8, 16]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,queries = [[0, 9], [3, 5]]) == [371842544, 4096]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,queries = [[0, 9], [3, 5]]) == [371842544, 4096]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,queries = [[0, 9], [4, 5], [2, 8]]) == [371842544, 512, 359738130]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,queries = [[0, 9], [4, 5], [2, 8]]) == [371842544, 512, 359738130]: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,queries = [[0, 0], [1, 2], [2, 2]]) == [4, 2048, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,queries = [[0, 0], [1, 2], [2, 2]]) == [4, 2048, 64]: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,queries = [[0, 2], [1, 3]]) == [32, 512]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,queries = [[0, 2], [1, 3]]) == [32, 512]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 1], [0, 2], [1, 2]]) == [4, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 1], [0, 2], [1, 2]]) == [4, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,queries = [[0, 9], [3, 5], [6, 8]]) == [371842544, 4096, 2097152]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,queries = [[0, 9], [3, 5], [6, 8]]) == [371842544, 4096, 2097152]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[0, 2], [1, 1], [0, 3]]) == [8, 1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[0, 2], [1, 1], [0, 3]]) == [8, 1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,queries = [[0, 9], [2, 6], [0, 8]]) == [371842544, 1048576, 719476260]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,queries = [[0, 9], [2, 6], [0, 8]]) == [371842544, 1048576, 719476260]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1023,queries = [[0, 9], [1, 3], [5, 7]]) == [371842544, 64, 262144]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1023,queries = [[0, 9], [1, 3], [5, 7]]) == [371842544, 64, 262144]: {e}')
    
    total += 1
    try:
        result = candidate(n = 255,queries = [[0, 7], [3, 5], [1, 2]]) == [268435456, 4096, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255,queries = [[0, 7], [3, 5], [1, 2]]) == [268435456, 4096, 8]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0], [0, 1], [0, 2]]) == [1, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0], [0, 1], [0, 2]]) == [1, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,queries = [[0, 29]]) == [371048337]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,queries = [[0, 29]]) == [371048337]: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,queries = [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,queries = [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,queries = [[0, 0]]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,queries = [[0, 0]]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727,queries = [[0, 26], [10, 15], [20, 25]]) == [867243987, 640520040, 792931211]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727,queries = [[0, 26], [10, 15], [20, 25]]) == [867243987, 640520040, 792931211]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [12, 17], [20, 21], [0, 5], [18, 22]]) == [349105660, 570065479, 23240159, 32768, 976371285]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [12, 17], [20, 21], [0, 5], [18, 22]]) == [349105660, 570065479, 23240159, 32768, 976371285]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,queries = [[0, 9], [4, 4], [2, 2], [8, 8], [0, 0]]) == [1024, 1, 1, 1, 1024]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,queries = [[0, 9], [4, 4], [2, 2], [8, 8], [0, 0]]) == [1024, 1, 1, 1, 1024]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,queries = [[0, 19], [5, 10], [15, 18]]) == [953612746, 371842544, 329376018]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,queries = [[0, 19], [5, 10], [15, 18]]) == [953612746, 371842544, 329376018]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,queries = [[0, 15], [4, 7], [10, 13], [0, 15]]) == [489373567, 4194304, 743685088, 489373567]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,queries = [[0, 15], [4, 7], [10, 13], [0, 15]]) == [489373567, 4194304, 743685088, 489373567]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823,queries = [[0, 29], [16, 22], [24, 29]]) == [549790477, 948232808, 106966330]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823,queries = [[0, 29], [16, 22], [24, 29]]) == [549790477, 948232808, 106966330]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15], [0, 29]]) == [756589216, 355395742, 948232808, 711461273, 756589216]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15], [0, 29]]) == [756589216, 355395742, 948232808, 711461273, 756589216]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999935,queries = [[0, 29], [10, 16], [20, 26]]) == [756589216, 990388602, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999935,queries = [[0, 29], [10, 16], [20, 26]]) == [756589216, 990388602, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 10], [18, 19]]) == [953612746, 640520040, 371842544, 438952513]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 10], [18, 19]]) == [953612746, 640520040, 371842544, 438952513]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,queries = [[0, 29], [15, 20], [30, 30]]) == [371048337, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,queries = [[0, 29], [15, 20], [30, 30]]) == [371048337, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215,queries = [[0, 23], [14, 18], [6, 9], [12, 15], [0, 23]]) == [511821710, 496641140, 73741817, 383381198, 511821710]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215,queries = [[0, 23], [14, 18], [6, 9], [12, 15], [0, 23]]) == [511821710, 496641140, 73741817, 383381198, 511821710]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8], [0, 19]]) == [134084614, 67049563, 589934536, 134084614]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8], [0, 19]]) == [134084614, 67049563, 589934536, 134084614]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,queries = [[0, 30], [14, 20], [7, 13], [0, 29]]) == [459478873, 744686787, 270016253, 549790477]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,queries = [[0, 30], [14, 20], [7, 13], [0, 29]]) == [459478873, 744686787, 270016253, 549790477]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567,queries = [[0, 20], [7, 12], [3, 8]]) == [975523612, 329376018, 658752036]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567,queries = [[0, 20], [7, 12], [3, 8]]) == [975523612, 329376018, 658752036]: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863,queries = [[0, 25], [12, 19], [6, 11], [0, 24]]) == [217770278, 829977023, 797922655, 322050759]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863,queries = [[0, 25], [12, 19], [6, 11], [0, 24]]) == [217770278, 829977023, 797922655, 322050759]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,queries = [[0, 29], [5, 10], [15, 20], [0, 29], [10, 15]]) == [549790477, 371842544, 243880903, 549790477, 640520040]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,queries = [[0, 29], [5, 10], [15, 20], [0, 29], [10, 15]]) == [549790477, 371842544, 243880903, 549790477, 640520040]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [5, 8], [10, 15], [17, 18], [0, 19]]) == [134084614, 67108864, 640520040, 359738130, 134084614]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [5, 8], [10, 15], [17, 18], [0, 19]]) == [134084614, 67108864, 640520040, 359738130, 134084614]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15]]) == [756589216, 355395742, 948232808, 711461273]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15]]) == [756589216, 355395742, 948232808, 711461273]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,queries = [[0, 15], [7, 10], [3, 7], [0, 14], [12, 15]]) == [489373567, 179869065, 33554432, 243880903, 383381198]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,queries = [[0, 15], [7, 10], [3, 7], [0, 14], [12, 15]]) == [489373567, 179869065, 33554432, 243880903, 383381198]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,queries = [[0, 0], [0, 9], [1, 8]]) == [1024, 1024, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,queries = [[0, 0], [0, 9], [1, 8]]) == [1024, 1024, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1047552,queries = [[0, 19], [5, 12], [15, 18]]) == [961554387, 892516375, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1047552,queries = [[0, 19], [5, 12], [15, 18]]) == [961554387, 892516375, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 14], [0, 20]]) == [953612746, 640520040, 936761609, 953612746]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 14], [0, 20]]) == [953612746, 640520040, 936761609, 953612746]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [4, 9], [10, 15]]) == [134084614, 755810045, 640520040]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [4, 9], [10, 15]]) == [134084614, 755810045, 640520040]: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,queries = [[0, 16], [6, 10], [8, 12], [14, 16]]) == [585862415, 511620083, 898961331, 371842544]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,queries = [[0, 16], [6, 10], [8, 12], [14, 16]]) == [585862415, 511620083, 898961331, 371842544]: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911,queries = [[0, 28], [3, 8], [12, 17], [0, 28], [8, 13]]) == [733922348, 589934536, 570065479, 733922348, 291172004]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911,queries = [[0, 28], [3, 8], [12, 17], [0, 28], [8, 13]]) == [733922348, 589934536, 570065479, 733922348, 291172004]: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0], [1, 1], [0, 1]]) == [1, 4, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0], [1, 1], [0, 1]]) == [1, 4, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303,queries = [[0, 21], [4, 9], [12, 16], [3, 8], [0, 21]]) == [686331837, 755810045, 270016253, 589934536, 686331837]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303,queries = [[0, 21], [4, 9], [12, 16], [3, 8], [0, 21]]) == [686331837, 755810045, 270016253, 589934536, 686331837]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,queries = [[0, 0]]) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,queries = [[0, 0]]) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,queries = [[0, 30], [18, 24], [26, 30]]) == [459478873, 846217527, 373798577]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,queries = [[0, 30], [18, 24], [26, 30]]) == [459478873, 846217527, 373798577]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,queries = [[0, 15], [3, 7], [9, 12], [0, 15], [8, 11]]) == [489373567, 33554432, 46480318, 489373567, 877905026]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,queries = [[0, 15], [3, 7], [9, 12], [0, 15], [8, 11]]) == [489373567, 33554432, 46480318, 489373567, 877905026]: {e}')
    
    total += 1
    try:
        result = candidate(n = 65535,queries = [[0, 15], [5, 10], [10, 15], [0, 15]]) == [489373567, 371842544, 640520040, 489373567]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 65535,queries = [[0, 15], [5, 10], [10, 15], [0, 15]]) == [489373567, 371842544, 640520040, 489373567]: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911,queries = [[0, 28], [14, 20], [22, 28]]) == [733922348, 744686787, 145353810]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911,queries = [[0, 28], [14, 20], [22, 28]]) == [733922348, 744686787, 145353810]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [6, 12], [14, 18]]) == [349105660, 291172004, 496641140]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [6, 12], [14, 18]]) == [349105660, 291172004, 496641140]: {e}')
    
    total += 1
    try:
        result = candidate(n = 511,queries = [[0, 8], [3, 7], [1, 4], [0, 9]]) == [719476260, 33554432, 1024, 719476260]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511,queries = [[0, 8], [3, 7], [1, 4], [0, 9]]) == [719476260, 33554432, 1024, 719476260]: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0], [0, 1], [1, 1]]) == [1, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0], [0, 1], [1, 1]]) == [1, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727,queries = [[0, 26], [5, 13], [18, 23], [10, 17], [0, 26]]) == [867243987, 993282280, 914988515, 951047217, 867243987]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727,queries = [[0, 26], [5, 13], [18, 23], [10, 17], [0, 26]]) == [867243987, 993282280, 914988515, 951047217, 867243987]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4294967295,queries = [[0, 31], [15, 25], [8, 20], [0, 32], [5, 12], [20, 24]]) == [461905191, 112151530, 605287554, 461905191, 317504065, 804188847]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4294967295,queries = [[0, 31], [15, 25], [8, 20], [0, 32], [5, 12], [20, 24]]) == [461905191, 112151530, 605287554, 461905191, 317504065, 804188847]: {e}')
    
    total += 1
    try:
        result = candidate(n = 16777215,queries = [[0, 23], [5, 10], [15, 18]]) == [511821710, 371842544, 329376018]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16777215,queries = [[0, 23], [5, 10], [15, 18]]) == [511821710, 371842544, 329376018]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8]]) == [134084614, 67049563, 589934536]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8]]) == [134084614, 67049563, 589934536]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303,queries = [[0, 21], [13, 17], [20, 21], [5, 10], [0, 21]]) == [686331837, 640520040, 23240159, 371842544, 686331837]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303,queries = [[0, 21], [13, 17], [20, 21], [5, 10], [0, 21]]) == [686331837, 640520040, 23240159, 371842544, 686331837]: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431,queries = [[0, 24], [12, 19], [6, 15], [0, 25], [3, 8], [10, 13]]) == [322050759, 829977023, 243880903, 322050759, 589934536, 743685088]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431,queries = [[0, 24], [12, 19], [6, 15], [0, 25], [3, 8], [10, 13]]) == [322050759, 829977023, 243880903, 322050759, 589934536, 743685088]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2097151,queries = [[0, 20], [8, 12], [16, 20], [10, 15], [0, 20]]) == [431750151, 898961331, 560523804, 640520040, 431750151]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2097151,queries = [[0, 20], [8, 12], [16, 20], [10, 15], [0, 20]]) == [431750151, 898961331, 560523804, 640520040, 431750151]: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431,queries = [[0, 24], [16, 20], [8, 11], [2, 5], [0, 24]]) == [322050759, 560523804, 877905026, 16384, 322050759]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431,queries = [[0, 24], [16, 20], [8, 11], [2, 5], [0, 24]]) == [322050759, 560523804, 877905026, 16384, 322050759]: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647,queries = [[0, 30], [20, 25], [15, 19], [10, 13], [0, 30]]) == [459478873, 792931211, 892516375, 743685088, 459478873]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647,queries = [[0, 30], [20, 25], [15, 19], [10, 13], [0, 30]]) == [459478873, 792931211, 892516375, 743685088, 459478873]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [11, 16], [4, 8], [0, 21]]) == [349105660, 993282280, 73741817, 686331837]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [11, 16], [4, 8], [0, 21]]) == [349105660, 993282280, 73741817, 686331837]: {e}')
    
    total += 1
    try:
        result = candidate(n = 4194303,queries = [[0, 21], [10, 15], [18, 20], [5, 8], [0, 21]]) == [686331837, 640520040, 67049563, 67108864, 686331837]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4194303,queries = [[0, 21], [10, 15], [18, 20], [5, 8], [0, 21]]) == [686331837, 640520040, 67049563, 67108864, 686331837]: {e}')
    
    total += 1
    try:
        result = candidate(n = 536870911,queries = [[0, 28], [12, 18], [20, 25], [0, 29]]) == [733922348, 243880903, 792931211, 733922348]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 536870911,queries = [[0, 28], [12, 18], [20, 25], [0, 29]]) == [733922348, 243880903, 792931211, 733922348]: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431,queries = [[0, 24], [8, 13], [16, 20]]) == [322050759, 291172004, 560523804]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431,queries = [[0, 24], [8, 13], [16, 20]]) == [322050759, 291172004, 560523804]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,queries = [[0, 29], [10, 20], [15, 25]]) == [371048337, 946258191, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,queries = [[0, 29], [10, 20], [15, 25]]) == [371048337, 946258191, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [7, 11], [14, 18], [2, 6], [0, 22]]) == [349105660, 371842544, 496641140, 1048576, 349105660]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [7, 11], [14, 18], [2, 6], [0, 22]]) == [349105660, 371842544, 496641140, 1048576, 349105660]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [8, 13], [16, 20]]) == [349105660, 291172004, 560523804]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [8, 13], [16, 20]]) == [349105660, 291172004, 560523804]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 18]]) == [953612746, 640520040, 427865320]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 18]]) == [953612746, 640520040, 427865320]: {e}')
    
    total += 1
    try:
        result = candidate(n = 511,queries = [[0, 8], [3, 6], [1, 7]]) == [719476260, 262144, 268435456]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 511,queries = [[0, 8], [3, 6], [1, 7]]) == [719476260, 262144, 268435456]: {e}')
    
    total += 1
    try:
        result = candidate(n = 34359738367,queries = [[0, 34], [17, 22], [25, 30], [0, 35]]) == [363951854, 936171702, 845845078, 363951854]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 34359738367,queries = [[0, 34], [17, 22], [25, 30], [0, 35]]) == [363951854, 936171702, 845845078, 363951854]: {e}')
    
    total += 1
    try:
        result = candidate(n = 33554431,queries = [[0, 24], [12, 18], [5, 10], [0, 9], [20, 24]]) == [322050759, 243880903, 371842544, 371842544, 804188847]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33554431,queries = [[0, 24], [12, 18], [5, 10], [0, 9], [20, 24]]) == [322050759, 243880903, 371842544, 371842544, 804188847]: {e}')
    
    total += 1
    try:
        result = candidate(n = 131071,queries = [[0, 16], [8, 12], [0, 0], [15, 16]]) == [585862415, 898961331, 1, 147483634]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 131071,queries = [[0, 16], [8, 12], [0, 0], [15, 16]]) == [585862415, 898961331, 1, 147483634]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [9, 16], [5, 11], [0, 23], [2, 7]]) == [349105660, 976371285, 533524785, 349105660, 134217728]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [9, 16], [5, 11], [0, 23], [2, 7]]) == [349105660, 976371285, 533524785, 349105660, 134217728]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048576,queries = [[0, 19], [5, 10], [15, 20]]) == [1048576, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048576,queries = [[0, 19], [5, 10], [15, 20]]) == [1048576, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 255,queries = [[0, 7], [3, 6], [1, 5], [0, 0], [7, 7]]) == [268435456, 262144, 32768, 1, 128]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 255,queries = [[0, 7], [3, 6], [1, 5], [0, 0], [7, 7]]) == [268435456, 262144, 32768, 1, 128]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [11, 14], [20, 22], [15, 18], [0, 22]]) == [349105660, 898961331, 291172004, 329376018, 349105660]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [11, 14], [20, 22], [15, 18], [0, 22]]) == [349105660, 898961331, 291172004, 329376018, 349105660]: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,queries = [[0, 28], [10, 20], [5, 15]]) == [885909558, 993282280, 369201595]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,queries = [[0, 28], [10, 20], [5, 15]]) == [885909558, 993282280, 369201595]: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727,queries = [[0, 26], [10, 16], [18, 24]]) == [867243987, 121047601, 846217527]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727,queries = [[0, 26], [10, 16], [18, 24]]) == [867243987, 121047601, 846217527]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [3, 8], [12, 15], [0, 19]]) == [134084614, 589934536, 383381198, 134084614]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [3, 8], [12, 15], [0, 19]]) == [134084614, 589934536, 383381198, 134084614]: {e}')
    
    total += 1
    try:
        result = candidate(n = 524287,queries = [[0, 18], [3, 7], [9, 14], [0, 17]]) == [134084614, 33554432, 635008130, 157921350]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 524287,queries = [[0, 18], [3, 7], [9, 14], [0, 17]]) == [134084614, 33554432, 635008130, 157921350]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1048575,queries = [[0, 19], [9, 15], [5, 10], [0, 18], [17, 19]]) == [953612746, 946258191, 371842544, 134084614, 383381198]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1048575,queries = [[0, 19], [9, 15], [5, 10], [0, 18], [17, 19]]) == [953612746, 946258191, 371842544, 134084614, 383381198]: {e}')
    
    total += 1
    try:
        result = candidate(n = 8388607,queries = [[0, 22], [10, 15], [5, 18]]) == [349105660, 640520040, 427865320]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8388607,queries = [[0, 22], [10, 15], [5, 18]]) == [349105660, 640520040, 427865320]: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]) == [1, 2, 8, 8, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]) == [1, 2, 8, 8, 4]: {e}')
    
    total += 1
    try:
        result = candidate(n = 134217727,queries = [[0, 26], [13, 18], [8, 12], [0, 27], [4, 9]]) == [867243987, 484190404, 898961331, 867243987, 755810045]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 134217727,queries = [[0, 26], [13, 18], [8, 12], [0, 27], [4, 9]]) == [867243987, 484190404, 898961331, 867243987, 755810045]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823,queries = [[0, 29], [10, 19], [15, 24], [5, 14], [0, 29]]) == [549790477, 961554387, 515607662, 936761609, 549790477]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823,queries = [[0, 29], [10, 19], [15, 24], [5, 14], [0, 29]]) == [549790477, 961554387, 515607662, 936761609, 549790477]: {e}')
    
    total += 1
    try:
        result = candidate(n = 67108863,queries = [[0, 25], [8, 14], [16, 22]]) == [217770278, 562080146, 948232808]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 67108863,queries = [[0, 25], [8, 14], [16, 22]]) == [217770278, 562080146, 948232808]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,queries = [[0, 29], [15, 20], [10, 14], [0, 9], [25, 29]]) == [371048337, 1, 946258191, 581415240, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,queries = [[0, 29], [15, 20], [10, 14], [0, 9], [25, 29]]) == [371048337, 1, 946258191, 581415240, 1]: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,queries = [[0, 29], [10, 15], [20, 25]]) == [421709488, 951047217, 536870912]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,queries = [[0, 29], [10, 15], [20, 25]]) == [421709488, 951047217, 536870912]: {e}')
    
    total += 1
    try:
        result = candidate(n = 17592186044415,queries = [[0, 41], [20, 28], [30, 35], [0, 42], [15, 25]]) == [342742191, 632009475, 515607662, 918181383, 112151530]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17592186044415,queries = [[0, 41], [20, 28], [30, 35], [0, 42], [15, 25]]) == [342742191, 632009475, 515607662, 918181383, 112151530]: {e}')
    
    total += 1
    try:
        result = candidate(n = 268435455,queries = [[0, 27], [12, 18], [20, 26]]) == [742004924, 243880903, 427865320]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 268435455,queries = [[0, 27], [12, 18], [20, 26]]) == [742004924, 243880903, 427865320]: {e}')
    
    total += 1
    try:
        result = candidate(n = 1073741823,queries = [[0, 29], [18, 23], [9, 12], [0, 5], [25, 29]]) == [549790477, 914988515, 46480318, 32768, 792931211]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1073741823,queries = [[0, 29], [18, 23], [9, 12], [0, 5], [25, 29]]) == [549790477, 914988515, 46480318, 32768, 792931211]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 10,queries = [[0, 0], [1, 1], [0, 2]]) == [2, 8, 16]
    assert candidate(n = 1023,queries = [[0, 9], [3, 5]]) == [371842544, 4096]
    assert candidate(n = 1023,queries = [[0, 9], [4, 5], [2, 8]]) == [371842544, 512, 359738130]
    assert candidate(n = 100,queries = [[0, 0], [1, 2], [2, 2]]) == [4, 2048, 64]
    assert candidate(n = 29,queries = [[0, 2], [1, 3]]) == [32, 512]
    assert candidate(n = 5,queries = [[0, 1], [0, 2], [1, 2]]) == [4, 4, 4]
    assert candidate(n = 1023,queries = [[0, 9], [3, 5], [6, 8]]) == [371842544, 4096, 2097152]
    assert candidate(n = 8,queries = [[0, 2], [1, 1], [0, 3]]) == [8, 1, 8]
    assert candidate(n = 1023,queries = [[0, 9], [2, 6], [0, 8]]) == [371842544, 1048576, 719476260]
    assert candidate(n = 1023,queries = [[0, 9], [1, 3], [5, 7]]) == [371842544, 64, 262144]
    assert candidate(n = 255,queries = [[0, 7], [3, 5], [1, 2]]) == [268435456, 4096, 8]
    assert candidate(n = 5,queries = [[0, 0], [0, 1], [0, 2]]) == [1, 4, 4]
    assert candidate(n = 1000000000,queries = [[0, 29]]) == [371048337]
    assert candidate(n = 15,queries = [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]
    assert candidate(n = 2,queries = [[0, 0]]) == [2]
    assert candidate(n = 134217727,queries = [[0, 26], [10, 15], [20, 25]]) == [867243987, 640520040, 792931211]
    assert candidate(n = 8388607,queries = [[0, 22], [12, 17], [20, 21], [0, 5], [18, 22]]) == [349105660, 570065479, 23240159, 32768, 976371285]
    assert candidate(n = 1024,queries = [[0, 9], [4, 4], [2, 2], [8, 8], [0, 0]]) == [1024, 1, 1, 1, 1024]
    assert candidate(n = 1048575,queries = [[0, 19], [5, 10], [15, 18]]) == [953612746, 371842544, 329376018]
    assert candidate(n = 65535,queries = [[0, 15], [4, 7], [10, 13], [0, 15]]) == [489373567, 4194304, 743685088, 489373567]
    assert candidate(n = 1073741823,queries = [[0, 29], [16, 22], [24, 29]]) == [549790477, 948232808, 106966330]
    assert candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15], [0, 29]]) == [756589216, 355395742, 948232808, 711461273, 756589216]
    assert candidate(n = 999999935,queries = [[0, 29], [10, 16], [20, 26]]) == [756589216, 990388602, 1]
    assert candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 10], [18, 19]]) == [953612746, 640520040, 371842544, 438952513]
    assert candidate(n = 1000000000,queries = [[0, 29], [15, 20], [30, 30]]) == [371048337, 1, 1]
    assert candidate(n = 16777215,queries = [[0, 23], [14, 18], [6, 9], [12, 15], [0, 23]]) == [511821710, 496641140, 73741817, 383381198, 511821710]
    assert candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8], [0, 19]]) == [134084614, 67049563, 589934536, 134084614]
    assert candidate(n = 2147483647,queries = [[0, 30], [14, 20], [7, 13], [0, 29]]) == [459478873, 744686787, 270016253, 549790477]
    assert candidate(n = 1234567,queries = [[0, 20], [7, 12], [3, 8]]) == [975523612, 329376018, 658752036]
    assert candidate(n = 67108863,queries = [[0, 25], [12, 19], [6, 11], [0, 24]]) == [217770278, 829977023, 797922655, 322050759]
    assert candidate(n = 2147483647,queries = [[0, 29], [5, 10], [15, 20], [0, 29], [10, 15]]) == [549790477, 371842544, 243880903, 549790477, 640520040]
    assert candidate(n = 524287,queries = [[0, 18], [5, 8], [10, 15], [17, 18], [0, 19]]) == [134084614, 67108864, 640520040, 359738130, 134084614]
    assert candidate(n = 999999935,queries = [[0, 29], [10, 20], [15, 25], [5, 15]]) == [756589216, 355395742, 948232808, 711461273]
    assert candidate(n = 65535,queries = [[0, 15], [7, 10], [3, 7], [0, 14], [12, 15]]) == [489373567, 179869065, 33554432, 243880903, 383381198]
    assert candidate(n = 1024,queries = [[0, 0], [0, 9], [1, 8]]) == [1024, 1024, 1]
    assert candidate(n = 1047552,queries = [[0, 19], [5, 12], [15, 18]]) == [961554387, 892516375, 1]
    assert candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 14], [0, 20]]) == [953612746, 640520040, 936761609, 953612746]
    assert candidate(n = 524287,queries = [[0, 18], [4, 9], [10, 15]]) == [134084614, 755810045, 640520040]
    assert candidate(n = 131071,queries = [[0, 16], [6, 10], [8, 12], [14, 16]]) == [585862415, 511620083, 898961331, 371842544]
    assert candidate(n = 536870911,queries = [[0, 28], [3, 8], [12, 17], [0, 28], [8, 13]]) == [733922348, 589934536, 570065479, 733922348, 291172004]
    assert candidate(n = 5,queries = [[0, 0], [1, 1], [0, 1]]) == [1, 4, 4]
    assert candidate(n = 4194303,queries = [[0, 21], [4, 9], [12, 16], [3, 8], [0, 21]]) == [686331837, 755810045, 270016253, 589934536, 686331837]
    assert candidate(n = 1,queries = [[0, 0]]) == [1]
    assert candidate(n = 2147483647,queries = [[0, 30], [18, 24], [26, 30]]) == [459478873, 846217527, 373798577]
    assert candidate(n = 65535,queries = [[0, 15], [3, 7], [9, 12], [0, 15], [8, 11]]) == [489373567, 33554432, 46480318, 489373567, 877905026]
    assert candidate(n = 65535,queries = [[0, 15], [5, 10], [10, 15], [0, 15]]) == [489373567, 371842544, 640520040, 489373567]
    assert candidate(n = 536870911,queries = [[0, 28], [14, 20], [22, 28]]) == [733922348, 744686787, 145353810]
    assert candidate(n = 8388607,queries = [[0, 22], [6, 12], [14, 18]]) == [349105660, 291172004, 496641140]
    assert candidate(n = 511,queries = [[0, 8], [3, 7], [1, 4], [0, 9]]) == [719476260, 33554432, 1024, 719476260]
    assert candidate(n = 3,queries = [[0, 0], [0, 1], [1, 1]]) == [1, 2, 2]
    assert candidate(n = 134217727,queries = [[0, 26], [5, 13], [18, 23], [10, 17], [0, 26]]) == [867243987, 993282280, 914988515, 951047217, 867243987]
    assert candidate(n = 4294967295,queries = [[0, 31], [15, 25], [8, 20], [0, 32], [5, 12], [20, 24]]) == [461905191, 112151530, 605287554, 461905191, 317504065, 804188847]
    assert candidate(n = 16777215,queries = [[0, 23], [5, 10], [15, 18]]) == [511821710, 371842544, 329376018]
    assert candidate(n = 524287,queries = [[0, 18], [7, 12], [3, 8]]) == [134084614, 67049563, 589934536]
    assert candidate(n = 4194303,queries = [[0, 21], [13, 17], [20, 21], [5, 10], [0, 21]]) == [686331837, 640520040, 23240159, 371842544, 686331837]
    assert candidate(n = 33554431,queries = [[0, 24], [12, 19], [6, 15], [0, 25], [3, 8], [10, 13]]) == [322050759, 829977023, 243880903, 322050759, 589934536, 743685088]
    assert candidate(n = 2097151,queries = [[0, 20], [8, 12], [16, 20], [10, 15], [0, 20]]) == [431750151, 898961331, 560523804, 640520040, 431750151]
    assert candidate(n = 33554431,queries = [[0, 24], [16, 20], [8, 11], [2, 5], [0, 24]]) == [322050759, 560523804, 877905026, 16384, 322050759]
    assert candidate(n = 2147483647,queries = [[0, 30], [20, 25], [15, 19], [10, 13], [0, 30]]) == [459478873, 792931211, 892516375, 743685088, 459478873]
    assert candidate(n = 8388607,queries = [[0, 22], [11, 16], [4, 8], [0, 21]]) == [349105660, 993282280, 73741817, 686331837]
    assert candidate(n = 4194303,queries = [[0, 21], [10, 15], [18, 20], [5, 8], [0, 21]]) == [686331837, 640520040, 67049563, 67108864, 686331837]
    assert candidate(n = 536870911,queries = [[0, 28], [12, 18], [20, 25], [0, 29]]) == [733922348, 243880903, 792931211, 733922348]
    assert candidate(n = 33554431,queries = [[0, 24], [8, 13], [16, 20]]) == [322050759, 291172004, 560523804]
    assert candidate(n = 1000000000,queries = [[0, 29], [10, 20], [15, 25]]) == [371048337, 946258191, 1]
    assert candidate(n = 8388607,queries = [[0, 22], [7, 11], [14, 18], [2, 6], [0, 22]]) == [349105660, 371842544, 496641140, 1048576, 349105660]
    assert candidate(n = 8388607,queries = [[0, 22], [8, 13], [16, 20]]) == [349105660, 291172004, 560523804]
    assert candidate(n = 1048575,queries = [[0, 19], [10, 15], [5, 18]]) == [953612746, 640520040, 427865320]
    assert candidate(n = 511,queries = [[0, 8], [3, 6], [1, 7]]) == [719476260, 262144, 268435456]
    assert candidate(n = 34359738367,queries = [[0, 34], [17, 22], [25, 30], [0, 35]]) == [363951854, 936171702, 845845078, 363951854]
    assert candidate(n = 33554431,queries = [[0, 24], [12, 18], [5, 10], [0, 9], [20, 24]]) == [322050759, 243880903, 371842544, 371842544, 804188847]
    assert candidate(n = 131071,queries = [[0, 16], [8, 12], [0, 0], [15, 16]]) == [585862415, 898961331, 1, 147483634]
    assert candidate(n = 8388607,queries = [[0, 22], [9, 16], [5, 11], [0, 23], [2, 7]]) == [349105660, 976371285, 533524785, 349105660, 134217728]
    assert candidate(n = 1048576,queries = [[0, 19], [5, 10], [15, 20]]) == [1048576, 1, 1]
    assert candidate(n = 255,queries = [[0, 7], [3, 6], [1, 5], [0, 0], [7, 7]]) == [268435456, 262144, 32768, 1, 128]
    assert candidate(n = 8388607,queries = [[0, 22], [11, 14], [20, 22], [15, 18], [0, 22]]) == [349105660, 898961331, 291172004, 329376018, 349105660]
    assert candidate(n = 500000000,queries = [[0, 28], [10, 20], [5, 15]]) == [885909558, 993282280, 369201595]
    assert candidate(n = 134217727,queries = [[0, 26], [10, 16], [18, 24]]) == [867243987, 121047601, 846217527]
    assert candidate(n = 524287,queries = [[0, 18], [3, 8], [12, 15], [0, 19]]) == [134084614, 589934536, 383381198, 134084614]
    assert candidate(n = 524287,queries = [[0, 18], [3, 7], [9, 14], [0, 17]]) == [134084614, 33554432, 635008130, 157921350]
    assert candidate(n = 1048575,queries = [[0, 19], [9, 15], [5, 10], [0, 18], [17, 19]]) == [953612746, 946258191, 371842544, 134084614, 383381198]
    assert candidate(n = 8388607,queries = [[0, 22], [10, 15], [5, 18]]) == [349105660, 640520040, 427865320]
    assert candidate(n = 7,queries = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]) == [1, 2, 8, 8, 4]
    assert candidate(n = 134217727,queries = [[0, 26], [13, 18], [8, 12], [0, 27], [4, 9]]) == [867243987, 484190404, 898961331, 867243987, 755810045]
    assert candidate(n = 1073741823,queries = [[0, 29], [10, 19], [15, 24], [5, 14], [0, 29]]) == [549790477, 961554387, 515607662, 936761609, 549790477]
    assert candidate(n = 67108863,queries = [[0, 25], [8, 14], [16, 22]]) == [217770278, 562080146, 948232808]
    assert candidate(n = 1000000000,queries = [[0, 29], [15, 20], [10, 14], [0, 9], [25, 29]]) == [371048337, 1, 946258191, 581415240, 1]
    assert candidate(n = 999999999,queries = [[0, 29], [10, 15], [20, 25]]) == [421709488, 951047217, 536870912]
    assert candidate(n = 17592186044415,queries = [[0, 41], [20, 28], [30, 35], [0, 42], [15, 25]]) == [342742191, 632009475, 515607662, 918181383, 112151530]
    assert candidate(n = 268435455,queries = [[0, 27], [12, 18], [20, 26]]) == [742004924, 243880903, 427865320]
    assert candidate(n = 1073741823,queries = [[0, 29], [18, 23], [9, 12], [0, 5], [25, 29]]) == [549790477, 914988515, 46480318, 32768, 792931211]


