def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 5,primes = [2, 7, 11]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,primes = [2, 7, 11]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,primes = [2, 11, 13, 17, 19]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,primes = [2, 11, 13, 17, 19]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,primes = [2, 3, 5, 7]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,primes = [2, 3, 5, 7]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,primes = [3, 5, 7]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,primes = [3, 5, 7]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,primes = [2, 3, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,primes = [2, 3, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,primes = [2, 11, 13, 17, 19]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,primes = [2, 11, 13, 17, 19]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,primes = [2, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,primes = [2, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,primes = [2, 7, 13, 19]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,primes = [2, 7, 13, 19]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,primes = [2, 3, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,primes = [2, 3, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 136: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,primes = [3, 5, 7, 11, 13]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,primes = [3, 5, 7, 11, 13]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 384: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,primes = [2, 11, 13, 17, 19]) == 8704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,primes = [2, 11, 13, 17, 19]) == 8704: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 1365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 1365: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]) == 519
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]) == 519: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [2, 5, 11, 13, 17]) == 272
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [2, 5, 11, 13, 17]) == 272: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3773
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3773: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7, 11]) == 280
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7, 11]) == 280: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,primes = [2, 5, 7, 11, 13, 17, 19]) == 1444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,primes = [2, 5, 7, 11, 13, 17, 19]) == 1444: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 399: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,primes = [2, 3, 5, 7, 11]) == 14975037
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,primes = [2, 3, 5, 7, 11]) == 14975037: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 12780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 12780: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 637: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 141797760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 141797760: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]) == 424
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]) == 424: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [2, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [2, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 418: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 8170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 8170: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 578: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [29, 31, 37, 41, 43, 47]) == 48749
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [29, 31, 37, 41, 43, 47]) == 48749: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [11, 13, 17, 19, 23]) == 83521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [11, 13, 17, 19, 23]) == 83521: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 3483
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 3483: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 3, 5, 7, 11]) == 8960
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 3, 5, 7, 11]) == 8960: {e}')
    
    total += 1
    try:
        result = candidate(n = 30000,primes = [2, 5, 11, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 3950350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30000,primes = [2, 5, 11, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 3950350: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 285: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 5474
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 5474: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 540: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 294980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 294980: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3751
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3751: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 224: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,primes = [3, 5, 7, 11, 13, 17, 19]) == 1683
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,primes = [3, 5, 7, 11, 13, 17, 19]) == 1683: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [3, 5, 7, 13, 19, 23]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [3, 5, 7, 13, 19, 23]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 230
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 230: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [11, 13, 17, 19, 23]) == 6859
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [11, 13, 17, 19, 23]) == 6859: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 94794
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 94794: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 40560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 40560: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 383826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 383826: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 850: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,primes = [2, 5, 7, 11, 13, 17, 19]) == 48400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,primes = [2, 5, 7, 11, 13, 17, 19]) == 48400: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 351: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718: {e}')
    
    total += 1
    try:
        result = candidate(n = 125,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 442
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 125,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 442: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 182: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 4437
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 4437: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 253: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 231: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 5, 11, 13, 17, 19, 23, 29, 31, 37]) == 6256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 5, 11, 13, 17, 19, 23, 29, 31, 37]) == 6256: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,primes = [2, 3, 5, 7]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,primes = [2, 3, 5, 7]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,primes = [2, 3, 5, 7]) == 1152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,primes = [2, 3, 5, 7]) == 1152: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]) == 817
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]) == 817: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,primes = [2, 5, 7, 11, 13, 17, 19]) == 845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,primes = [2, 5, 7, 11, 13, 17, 19]) == 845: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,primes = [2, 3, 5]) == 51200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,primes = [2, 3, 5]) == 51200000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 928: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 50000,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 17610759
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50000,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 17610759: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 11616
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 11616: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 2457
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 2457: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [5, 11, 13, 17, 19, 23, 29, 31, 37]) == 1375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [5, 11, 13, 17, 19, 23, 29, 31, 37]) == 1375: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(n = 20000,primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 2610239
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20000,primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 2610239: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1323: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [3, 7, 11, 13, 17, 19]) == 507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [3, 7, 11, 13, 17, 19]) == 507: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 697
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 697: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,primes = [3, 7, 11, 13, 17]) == 833
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,primes = [3, 7, 11, 13, 17]) == 833: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 5,primes = [2, 7, 11]) == 8
    assert candidate(n = 5,primes = [2, 11, 13, 17, 19]) == 11
    assert candidate(n = 3,primes = [2, 3, 5, 7]) == 3
    assert candidate(n = 15,primes = [3, 5, 7]) == 81
    assert candidate(n = 10,primes = [2, 3, 5]) == 12
    assert candidate(n = 20,primes = [2, 11, 13, 17, 19]) == 88
    assert candidate(n = 2,primes = [2, 7]) == 2
    assert candidate(n = 12,primes = [2, 7, 13, 19]) == 32
    assert candidate(n = 1,primes = [2, 3, 5]) == 1
    assert candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 136
    assert candidate(n = 20,primes = [3, 5, 7, 11, 13]) == 75
    assert candidate(n = 25,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]) == 56
    assert candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 384
    assert candidate(n = 150,primes = [2, 11, 13, 17, 19]) == 8704
    assert candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]) == 1365
    assert candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397]) == 519
    assert candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 30
    assert candidate(n = 50,primes = [2, 5, 11, 13, 17]) == 272
    assert candidate(n = 10,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 10
    assert candidate(n = 500,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3773
    assert candidate(n = 100,primes = [2, 3, 5, 7, 11]) == 280
    assert candidate(n = 200,primes = [2, 5, 7, 11, 13, 17, 19]) == 1444
    assert candidate(n = 2,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409]) == 2
    assert candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 104
    assert candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 399
    assert candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 700
    assert candidate(n = 5000,primes = [2, 3, 5, 7, 11]) == 14975037
    assert candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 12780
    assert candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 637
    assert candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 141797760
    assert candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]) == 100
    assert candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]) == 424
    assert candidate(n = 30,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 30
    assert candidate(n = 75,primes = [2, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == 418
    assert candidate(n = 5000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 8170
    assert candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 578
    assert candidate(n = 50,primes = [29, 31, 37, 41, 43, 47]) == 48749
    assert candidate(n = 120,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 144
    assert candidate(n = 100,primes = [11, 13, 17, 19, 23]) == 83521
    assert candidate(n = 300,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 3483
    assert candidate(n = 500,primes = [2, 3, 5, 7, 11]) == 8960
    assert candidate(n = 30000,primes = [2, 5, 11, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 3950350
    assert candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 285
    assert candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 5474
    assert candidate(n = 300,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 540
    assert candidate(n = 100000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 294980
    assert candidate(n = 100,primes = [2, 3, 5, 7]) == 450
    assert candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 3751
    assert candidate(n = 60,primes = [2, 7, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 224
    assert candidate(n = 150,primes = [3, 5, 7, 11, 13, 17, 19]) == 1683
    assert candidate(n = 50,primes = [3, 5, 7, 13, 19, 23]) == 351
    assert candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 230
    assert candidate(n = 50,primes = [11, 13, 17, 19, 23]) == 6859
    assert candidate(n = 20000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 94794
    assert candidate(n = 15000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]) == 40560
    assert candidate(n = 50000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]) == 383826
    assert candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 100
    assert candidate(n = 250,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]) == 250
    assert candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 850
    assert candidate(n = 1000,primes = [2, 5, 7, 11, 13, 17, 19]) == 48400
    assert candidate(n = 200,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 351
    assert candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718
    assert candidate(n = 125,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 442
    assert candidate(n = 150,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]) == 182
    assert candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 40
    assert candidate(n = 1000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 4437
    assert candidate(n = 80,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 253
    assert candidate(n = 75,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 231
    assert candidate(n = 10000,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 42718
    assert candidate(n = 100,primes = [2, 3, 5, 7, 11, 13, 17, 19]) == 156
    assert candidate(n = 80,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 200
    assert candidate(n = 500,primes = [2, 5, 11, 13, 17, 19, 23, 29, 31, 37]) == 6256
    assert candidate(n = 100,primes = [2, 3, 5, 7]) == 450
    assert candidate(n = 40,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]) == 40
    assert candidate(n = 150,primes = [2, 3, 5, 7]) == 1152
    assert candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 95
    assert candidate(n = 250,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]) == 817
    assert candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 76
    assert candidate(n = 150,primes = [2, 5, 7, 11, 13, 17, 19]) == 845
    assert candidate(n = 1000,primes = [2, 3, 5]) == 51200000
    assert candidate(n = 500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 928
    assert candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == 75
    assert candidate(n = 50000,primes = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 17610759
    assert candidate(n = 7500,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) == 11616
    assert candidate(n = 25,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == 25
    assert candidate(n = 300,primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]) == 2457
    assert candidate(n = 75,primes = [5, 11, 13, 17, 19, 23, 29, 31, 37]) == 1375
    assert candidate(n = 75,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 82
    assert candidate(n = 20000,primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]) == 2610239
    assert candidate(n = 750,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == 1323
    assert candidate(n = 15,primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]) == 15
    assert candidate(n = 50,primes = [3, 7, 11, 13, 17, 19]) == 507
    assert candidate(n = 200,primes = [2, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]) == 697
    assert candidate(n = 50,primes = [2, 5, 7, 11, 13, 17, 19, 23, 29]) == 112
    assert candidate(n = 50,primes = [3, 7, 11, 13, 17]) == 833


