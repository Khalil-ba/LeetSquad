def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [113, 221]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 221]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 217, 228]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 217, 228]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 219, 220, 311, 322, 413, 424, 435]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 219, 220, 311, 322, 413, 424, 435]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 217, 228, 315, 324, 333, 342]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 217, 228, 315, 324, 333, 342]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 219, 228, 311, 322, 336, 344, 418]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 219, 228, 311, 322, 336, 344, 418]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439, 440]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439, 440]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 229, 311, 325, 337, 419, 425, 432, 446]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 229, 311, 325, 337, 419, 425, 432, 446]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 212, 221, 319, 328]) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 212, 221, 319, 328]) == 37: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 211, 223, 315, 320, 412]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 211, 223, 315, 320, 412]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 215, 226, 317, 328, 419]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 215, 226, 317, 328, 419]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 211, 228, 316, 323, 414, 421]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 211, 228, 316, 323, 414, 421]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 227, 316, 325]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 227, 316, 325]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 219, 229, 310, 320, 410, 420]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 219, 229, 310, 320, 410, 420]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 213, 222, 310, 320, 410]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 213, 222, 310, 320, 410]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 211, 221, 310, 321, 332, 343, 411]) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 211, 221, 310, 321, 332, 343, 411]) == 47: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 215, 312, 324, 416]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 215, 312, 324, 416]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 219, 228, 317, 326, 335, 344]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 219, 228, 317, 326, 335, 344]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 210, 220]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 210, 220]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 347]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 347]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 221, 314, 325, 336, 347, 418, 429, 431, 442]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 221, 314, 325, 336, 347, 418, 429, 431, 442]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 227, 316, 325, 334, 343]) == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 227, 316, 325, 334, 343]) == 84: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 215, 224, 310, 320, 410, 420, 430, 440]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 215, 224, 310, 320, 410, 420, 430, 440]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 210, 220, 312, 321, 410]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 210, 220, 312, 321, 410]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 416, 427]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 416, 427]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 219, 221, 312, 328, 417, 422, 439, 446]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 219, 221, 312, 328, 417, 422, 439, 446]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 210, 220, 310, 320, 330, 340, 410, 420, 430, 440]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 210, 220, 310, 320, 330, 340, 410, 420, 430, 440]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 215, 312, 324]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 215, 312, 324]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 215, 221]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 215, 221]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 219, 228, 314, 322, 333, 341, 415, 429, 436, 442]) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 219, 228, 314, 322, 333, 341, 415, 429, 436, 442]) == 96: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 214, 222, 316, 327, 331, 345, 419, 428, 434, 443]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 214, 222, 316, 327, 331, 345, 419, 428, 434, 443]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475]) == 164
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475]) == 164: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 214, 225, 316, 327, 338, 349, 410, 421, 432, 443, 454, 465, 476, 487]) == 148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 214, 225, 316, 327, 338, 349, 410, 421, 432, 443, 454, 465, 476, 487]) == 148: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 211, 229, 313, 324, 335, 346, 417, 422, 438]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 211, 229, 313, 324, 335, 346, 417, 422, 438]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 211, 229, 314, 326, 335, 342, 418, 427, 431, 449]) == 116
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 211, 229, 314, 326, 335, 342, 418, 427, 431, 449]) == 116: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 211, 229, 316, 324, 333, 342, 417, 428, 439, 441]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 211, 229, 316, 324, 333, 342, 417, 428, 439, 441]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 216, 227, 314, 323, 338, 415, 429, 436]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 216, 227, 314, 323, 338, 415, 429, 436]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 213, 227, 311, 329, 332, 346, 418, 424, 433, 441]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 213, 227, 311, 329, 332, 346, 418, 424, 433, 441]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 212, 228, 311, 323, 335, 347, 414, 426, 432, 448]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 212, 228, 311, 323, 335, 347, 414, 426, 432, 448]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 219, 225, 318, 324, 333, 347, 411, 422, 439, 446, 458, 464, 473, 485]) == 154
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 219, 225, 318, 324, 333, 347, 411, 422, 439, 446, 458, 464, 473, 485]) == 154: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 211, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 211, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 217, 224, 311, 322, 333, 344, 415, 426, 437, 448]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 217, 224, 311, 322, 333, 344, 415, 426, 437, 448]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 216, 225, 312, 323, 334, 349, 418, 421, 436, 447]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 216, 225, 312, 323, 334, 349, 418, 421, 436, 447]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 212, 226, 319, 327, 338, 345, 413, 424, 435, 446]) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 212, 226, 319, 327, 338, 345, 413, 424, 435, 446]) == 113: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 215, 222, 316, 324, 337, 341, 413, 428, 435, 449, 452, 464, 477]) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 215, 222, 316, 324, 337, 341, 413, 428, 435, 449, 452, 464, 477]) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 217, 228, 319, 325, 336, 347, 411, 422, 433, 444, 455, 466, 477, 488]) == 198
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 217, 228, 319, 325, 336, 347, 411, 422, 433, 444, 455, 466, 477, 488]) == 198: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 210, 221, 312, 323, 334, 345, 416, 427, 438, 449, 350, 361, 372, 383]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 210, 221, 312, 323, 334, 345, 416, 427, 438, 449, 350, 361, 372, 383]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 211, 225, 316, 327, 338, 349, 413, 422, 431, 448]) == 83
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 211, 225, 316, 327, 338, 349, 413, 422, 431, 448]) == 83: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 214, 228, 312, 326, 339, 341, 417, 423, 435, 444, 459, 462, 478, 486]) == 168
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 214, 228, 312, 326, 339, 341, 417, 423, 435, 444, 459, 462, 478, 486]) == 168: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 218, 226, 319, 323, 331, 345, 412, 427, 434, 448, 456, 463, 479, 481]) == 188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 218, 226, 319, 323, 331, 345, 412, 427, 434, 448, 456, 463, 479, 481]) == 188: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 214, 226, 318, 329, 333, 345, 412, 421, 437, 444]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 214, 226, 318, 329, 333, 345, 412, 421, 437, 444]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446, 455, 464, 473]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446, 455, 464, 473]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449, 458, 467, 476]) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449, 458, 467, 476]) == 182: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 218, 229, 310, 321, 332, 343, 414, 425, 436, 447]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 218, 229, 310, 321, 332, 343, 414, 425, 436, 447]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 211, 223, 312, 328, 336, 414, 429, 435, 441]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 211, 223, 312, 328, 336, 414, 429, 435, 441]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 225, 317, 324, 336, 343, 411, 422, 433, 444, 455, 466, 477, 488]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 225, 317, 324, 336, 343, 411, 422, 433, 444, 455, 466, 477, 488]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 219, 220, 311, 322, 333, 344, 415, 426, 437, 448, 359, 360, 451, 462]) == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 219, 220, 311, 322, 333, 344, 415, 426, 437, 448, 359, 360, 451, 462]) == 137: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 218, 224, 312, 325, 331, 347, 419, 423, 436, 448]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 218, 224, 312, 325, 331, 347, 419, 423, 436, 448]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 211, 222, 313, 316, 325, 328, 414, 427, 439, 443]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 211, 222, 313, 316, 325, 328, 414, 427, 439, 443]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 212, 228, 319, 323, 336, 341, 417, 425, 432, 448]) == 107
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 212, 228, 319, 323, 336, 341, 417, 425, 432, 448]) == 107: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 213, 229, 315, 326, 338, 344, 411, 422, 433, 447]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 213, 229, 315, 326, 338, 344, 411, 422, 433, 447]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 225, 318, 329, 411, 422, 433, 444]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 225, 318, 329, 411, 422, 433, 444]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474]) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474]) == 88: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 219, 223, 312, 317, 321, 328, 415, 426, 434, 438]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 219, 223, 312, 317, 321, 328, 415, 426, 434, 438]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 217, 225, 313, 329, 332, 346, 411, 422, 435, 444]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 217, 225, 313, 329, 332, 346, 411, 422, 435, 444]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 216, 227, 318, 329, 332, 341, 413, 424, 435, 446]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 216, 227, 318, 329, 332, 341, 413, 424, 435, 446]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464, 475, 486]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464, 475, 486]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 213, 222, 311, 325, 336, 347, 418, 429, 431, 442, 453, 464, 475, 486]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 213, 222, 311, 325, 336, 347, 418, 429, 431, 442, 453, 464, 475, 486]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 219, 228, 317, 324, 333, 342, 416, 425, 434, 443]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 219, 228, 317, 324, 333, 342, 416, 425, 434, 443]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 213, 224, 311, 322, 333, 344, 416, 427, 438, 449]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 213, 224, 311, 322, 333, 344, 416, 427, 438, 449]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 218, 224, 311, 323, 332, 346, 419, 428, 437, 445]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 218, 224, 311, 323, 332, 346, 419, 428, 437, 445]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 216, 224, 317, 321, 338, 342, 419, 425, 436, 444, 453, 467, 478, 489]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 216, 224, 317, 321, 338, 342, 419, 425, 436, 444, 453, 467, 478, 489]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 213, 227, 319, 322, 338, 341, 415, 424, 437, 446, 453, 469, 478, 482]) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 213, 227, 319, 322, 338, 341, 415, 424, 437, 446, 453, 469, 478, 482]) == 172: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474]) == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474]) == 146: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 337, 418, 429, 430, 441]) == 73
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 337, 418, 429, 430, 441]) == 73: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 215, 223, 318, 321, 337, 342, 416, 424, 439, 445, 453, 468, 472, 481]) == 138
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 215, 223, 318, 321, 337, 342, 416, 424, 439, 445, 453, 468, 472, 481]) == 138: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 214, 223, 312, 321, 336, 345, 414, 423, 432, 441]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 214, 223, 312, 321, 336, 345, 414, 423, 432, 441]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(nums = [116, 211, 221, 311, 321, 331, 341, 411, 421, 431, 441]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [116, 211, 221, 311, 321, 331, 341, 411, 421, 431, 441]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 212, 221, 314, 325, 330, 346, 417, 428, 439]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 212, 221, 314, 325, 330, 346, 417, 428, 439]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 211, 221, 312, 323, 334, 345, 416, 427, 438, 449]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 211, 221, 312, 323, 334, 345, 416, 427, 438, 449]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 226, 332, 335, 341, 348, 437, 449]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 226, 332, 335, 341, 348, 437, 449]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 212, 229, 314, 325, 336, 347, 411, 422, 433, 444]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 212, 229, 314, 325, 336, 347, 411, 422, 433, 444]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 216, 222, 311, 318, 326, 329, 414, 423, 435, 437, 448]) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 216, 222, 311, 318, 326, 329, 414, 423, 435, 437, 448]) == 117: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 216, 227, 318, 329, 330, 341, 412, 423, 434, 445, 456, 467, 478, 489]) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 216, 227, 318, 329, 330, 341, 412, 423, 434, 445, 456, 467, 478, 489]) == 172: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 216, 224, 312, 323, 337, 348, 415, 429, 436, 441]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 216, 224, 312, 323, 337, 348, 415, 429, 436, 441]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 219, 228, 317, 326, 335, 344, 413, 422, 431, 440]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 219, 228, 317, 326, 335, 344, 413, 422, 431, 440]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474, 485]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474, 485]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [114, 212, 227, 315, 319, 328, 411, 416, 422, 425, 433, 434]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [114, 212, 227, 315, 319, 328, 411, 416, 422, 425, 433, 434]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 450, 461, 472, 483]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 450, 461, 472, 483]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 211, 223, 314, 325, 336, 417, 428, 439]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 211, 223, 314, 325, 336, 417, 428, 439]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 217, 228, 319, 326, 335, 412, 421, 437, 448]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 217, 228, 319, 326, 335, 412, 421, 437, 448]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 331, 342]) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 331, 342]) == 71: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 352, 363, 374, 385]) == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 352, 363, 374, 385]) == 69: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475, 484]) == 184
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475, 484]) == 184: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 216, 227, 312, 328, 339, 343, 411, 424, 435, 447]) == 117
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 216, 227, 312, 328, 339, 343, 411, 424, 435, 447]) == 117: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 218, 229, 311, 322, 333, 344, 415, 426, 437, 448, 359]) == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 218, 229, 311, 322, 333, 344, 415, 426, 437, 448, 359]) == 131: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 215, 228, 316, 322, 339, 347, 413, 424, 431, 445]) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 215, 228, 316, 322, 339, 347, 413, 424, 431, 445]) == 87: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449]) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449]) == 141: {e}')
    
    total += 1
    try:
        result = candidate(nums = [110, 211, 222, 313, 324, 335, 346, 417, 428, 439, 440]) == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [110, 211, 222, 313, 324, 335, 346, 417, 428, 439, 440]) == 57: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 218, 225, 317, 324, 333, 342, 411, 422, 433, 444]) == 133
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 218, 225, 317, 324, 333, 342, 411, 422, 433, 444]) == 133: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 214, 223, 312, 321, 336, 345, 417, 428, 439, 440, 451, 462]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 214, 223, 312, 321, 336, 345, 417, 428, 439, 440, 451, 462]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 219, 221, 315, 324, 338, 347, 413, 422, 431, 446]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 219, 221, 315, 324, 338, 347, 413, 422, 431, 446]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 225, 323, 334, 347, 421, 428, 432, 439]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 225, 323, 334, 347, 421, 428, 432, 439]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 215, 223, 317, 328, 336, 344, 412, 423, 431, 449]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 215, 223, 317, 328, 336, 344, 412, 423, 431, 449]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 216, 227, 318, 329, 331, 342, 413, 424, 435, 446]) == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 216, 227, 318, 329, 331, 342, 413, 424, 435, 446]) == 123: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 211, 229, 315, 322, 338, 344, 417, 425, 431, 446]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 211, 229, 315, 322, 338, 344, 417, 425, 431, 446]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 216, 227, 318, 329, 330, 411, 422, 433, 444]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 216, 227, 318, 329, 330, 411, 422, 433, 444]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442, 343]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442, 343]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442]) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442]) == 82: {e}')
    
    total += 1
    try:
        result = candidate(nums = [119, 215, 222, 311, 323, 334, 347, 418, 429, 436, 445]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [119, 215, 222, 311, 323, 334, 347, 418, 429, 436, 445]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(nums = [115, 213, 224, 312, 327, 331, 349, 418, 426, 435, 442]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [115, 213, 224, 312, 327, 331, 349, 418, 426, 435, 442]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 212, 223, 314, 325, 336, 417, 428, 439, 440]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 212, 223, 314, 325, 336, 417, 428, 439, 440]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474, 483]) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474, 483]) == 162: {e}')
    
    total += 1
    try:
        result = candidate(nums = [118, 215, 223, 312, 321, 337, 349, 414, 428, 436, 445]) == 119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [118, 215, 223, 312, 321, 337, 349, 414, 428, 436, 445]) == 119: {e}')
    
    total += 1
    try:
        result = candidate(nums = [113, 212, 221, 314, 325, 336, 417, 428, 439, 440]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [113, 212, 221, 314, 325, 336, 417, 428, 439, 440]) == 72: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [113, 221]) == 4
    assert candidate(nums = [116, 217, 228]) == 27
    assert candidate(nums = [118, 219, 220, 311, 322, 413, 424, 435]) == 75
    assert candidate(nums = [116, 217, 228, 315, 324, 333, 342]) == 68
    assert candidate(nums = [114, 219, 228, 311, 322, 336, 344, 418]) == 71
    assert candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439, 440]) == 72
    assert candidate(nums = [117]) == 7
    assert candidate(nums = [119, 218, 229, 311, 325, 337, 419, 425, 432, 446]) == 127
    assert candidate(nums = [115, 212, 221, 319, 328]) == 37
    assert candidate(nums = [116]) == 6
    assert candidate(nums = [119, 211, 223, 315, 320, 412]) == 39
    assert candidate(nums = [111, 212, 223]) == 7
    assert candidate(nums = [114, 215, 226, 317, 328, 419]) == 52
    assert candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449]) == 64
    assert candidate(nums = [115, 211, 228, 316, 323, 414, 421]) == 51
    assert candidate(nums = [119, 218, 227, 316, 325]) == 61
    assert candidate(nums = [114, 219, 229, 310, 320, 410, 420]) == 52
    assert candidate(nums = [117, 213, 222, 310, 320, 410]) == 29
    assert candidate(nums = [119]) == 9
    assert candidate(nums = [119, 211, 221, 310, 321, 332, 343, 411]) == 47
    assert candidate(nums = [113, 215, 312, 324, 416]) == 28
    assert candidate(nums = [110, 219, 228, 317, 326, 335, 344]) == 56
    assert candidate(nums = [118, 210, 220]) == 16
    assert candidate(nums = [112]) == 2
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 347]) == 36
    assert candidate(nums = [112, 213, 221, 314, 325, 336, 347, 418, 429, 431, 442]) == 77
    assert candidate(nums = [119, 218, 227, 316, 325, 334, 343]) == 84
    assert candidate(nums = [112, 215, 224, 310, 320, 410, 420, 430, 440]) == 34
    assert candidate(nums = [115, 210, 220, 312, 321, 410]) == 18
    assert candidate(nums = [111, 212, 223, 314, 325, 416, 427]) == 39
    assert candidate(nums = [115, 219, 221, 312, 328, 417, 422, 439, 446]) == 106
    assert candidate(nums = [110, 210, 220, 310, 320, 330, 340, 410, 420, 430, 440]) == 0
    assert candidate(nums = [113, 215, 312, 324]) == 22
    assert candidate(nums = [113, 215, 221]) == 12
    assert candidate(nums = [111, 219, 228, 314, 322, 333, 341, 415, 429, 436, 442]) == 96
    assert candidate(nums = [113, 214, 222, 316, 327, 331, 345, 419, 428, 434, 443]) == 94
    assert candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475]) == 164
    assert candidate(nums = [113, 214, 225, 316, 327, 338, 349, 410, 421, 432, 443, 454, 465, 476, 487]) == 148
    assert candidate(nums = [112, 211, 229, 313, 324, 335, 346, 417, 422, 438]) == 69
    assert candidate(nums = [117, 211, 229, 314, 326, 335, 342, 418, 427, 431, 449]) == 116
    assert candidate(nums = [118, 211, 229, 316, 324, 333, 342, 417, 428, 439, 441]) == 120
    assert candidate(nums = [112, 216, 227, 314, 323, 338, 415, 429, 436]) == 72
    assert candidate(nums = [115, 213, 227, 311, 329, 332, 346, 418, 424, 433, 441]) == 100
    assert candidate(nums = [116, 212, 228, 311, 323, 335, 347, 414, 426, 432, 448]) == 100
    assert candidate(nums = [112, 219, 225, 318, 324, 333, 347, 411, 422, 439, 446, 458, 464, 473, 485]) == 154
    assert candidate(nums = [112, 211, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 73
    assert candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442]) == 81
    assert candidate(nums = [118, 217, 224, 311, 322, 333, 344, 415, 426, 437, 448]) == 123
    assert candidate(nums = [118, 216, 225, 312, 323, 334, 349, 418, 421, 436, 447]) == 127
    assert candidate(nums = [115, 212, 226, 319, 327, 338, 345, 413, 424, 435, 446]) == 113
    assert candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464]) == 101
    assert candidate(nums = [118, 215, 222, 316, 324, 337, 341, 413, 428, 435, 449, 452, 464, 477]) == 155
    assert candidate(nums = [116, 217, 228, 319, 325, 336, 347, 411, 422, 433, 444, 455, 466, 477, 488]) == 198
    assert candidate(nums = [119, 210, 221, 312, 323, 334, 345, 416, 427, 438, 449, 350, 361, 372, 383]) == 105
    assert candidate(nums = [112, 211, 225, 316, 327, 338, 349, 413, 422, 431, 448]) == 83
    assert candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446]) == 105
    assert candidate(nums = [115, 214, 228, 312, 326, 339, 341, 417, 423, 435, 444, 459, 462, 478, 486]) == 168
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 431, 442]) == 71
    assert candidate(nums = [117, 218, 226, 319, 323, 331, 345, 412, 427, 434, 448, 456, 463, 479, 481]) == 188
    assert candidate(nums = [117, 214, 226, 318, 329, 333, 345, 412, 421, 437, 444]) == 126
    assert candidate(nums = [116, 215, 224, 313, 322, 331, 340, 419, 428, 437, 446, 455, 464, 473]) == 128
    assert candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449, 458, 467, 476]) == 182
    assert candidate(nums = [117, 218, 229, 310, 321, 332, 343, 414, 425, 436, 447]) == 121
    assert candidate(nums = [115, 211, 223, 312, 328, 336, 414, 429, 435, 441]) == 77
    assert candidate(nums = [119, 218, 225, 317, 324, 336, 343, 411, 422, 433, 444, 455, 466, 477, 488]) == 200
    assert candidate(nums = [118, 219, 220, 311, 322, 333, 344, 415, 426, 437, 448, 359, 360, 451, 462]) == 137
    assert candidate(nums = [111, 218, 224, 312, 325, 331, 347, 419, 423, 436, 448]) == 94
    assert candidate(nums = [119, 211, 222, 313, 316, 325, 328, 414, 427, 439, 443]) == 102
    assert candidate(nums = [115, 212, 228, 319, 323, 336, 341, 417, 425, 432, 448]) == 107
    assert candidate(nums = [117, 213, 229, 315, 326, 338, 344, 411, 422, 433, 447]) == 119
    assert candidate(nums = [112, 213, 225, 318, 329, 411, 422, 433, 444]) == 71
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474]) == 88
    assert candidate(nums = [116, 219, 223, 312, 317, 321, 328, 415, 426, 434, 438]) == 95
    assert candidate(nums = [114, 217, 225, 313, 329, 332, 346, 411, 422, 435, 444]) == 106
    assert candidate(nums = [115, 216, 227, 318, 329, 332, 341, 413, 424, 435, 446]) == 123
    assert candidate(nums = [112, 213, 224, 315, 326, 337, 348, 419, 420, 431, 442, 453, 464, 475, 486]) == 126
    assert candidate(nums = [114, 213, 222, 311, 325, 336, 347, 418, 429, 431, 442, 453, 464, 475, 486]) == 128
    assert candidate(nums = [111, 219, 228, 317, 324, 333, 342, 416, 425, 434, 443]) == 103
    assert candidate(nums = [115, 213, 224, 311, 322, 333, 344, 416, 427, 438, 449]) == 93
    assert candidate(nums = [117, 218, 224, 311, 323, 332, 346, 419, 428, 437, 445]) == 127
    assert candidate(nums = [113, 216, 224, 317, 321, 338, 342, 419, 425, 436, 444, 453, 467, 478, 489]) == 151
    assert candidate(nums = [116, 213, 227, 319, 322, 338, 341, 415, 424, 437, 446, 453, 469, 478, 482]) == 172
    assert candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474]) == 146
    assert candidate(nums = [112, 213, 224, 315, 326, 337, 418, 429, 430, 441]) == 73
    assert candidate(nums = [114, 215, 223, 318, 321, 337, 342, 416, 424, 439, 445, 453, 468, 472, 481]) == 138
    assert candidate(nums = [115, 214, 223, 312, 321, 336, 345, 414, 423, 432, 441]) == 79
    assert candidate(nums = [116, 211, 221, 311, 321, 331, 341, 411, 421, 431, 441]) == 52
    assert candidate(nums = [113, 212, 221, 314, 325, 330, 346, 417, 428, 439]) == 66
    assert candidate(nums = [119, 211, 221, 312, 323, 334, 345, 416, 427, 438, 449]) == 109
    assert candidate(nums = [113, 226, 332, 335, 341, 348, 437, 449]) == 31
    assert candidate(nums = [113, 212, 229, 314, 325, 336, 347, 411, 422, 433, 444]) == 85
    assert candidate(nums = [117, 216, 222, 311, 318, 326, 329, 414, 423, 435, 437, 448]) == 117
    assert candidate(nums = [115, 216, 227, 318, 329, 330, 341, 412, 423, 434, 445, 456, 467, 478, 489]) == 172
    assert candidate(nums = [118, 216, 224, 312, 323, 337, 348, 415, 429, 436, 441]) == 126
    assert candidate(nums = [118, 219, 228, 317, 326, 335, 344, 413, 422, 431, 440]) == 141
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 452, 463, 474, 485]) == 104
    assert candidate(nums = [114, 212, 227, 315, 319, 328, 411, 416, 422, 425, 433, 434]) == 70
    assert candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 450, 461, 472, 483]) == 64
    assert candidate(nums = [112, 211, 223, 314, 325, 336, 417, 428, 439]) == 57
    assert candidate(nums = [113, 217, 228, 319, 326, 335, 412, 421, 437, 448]) == 104
    assert candidate(nums = [111, 212, 223, 314, 325, 416, 427, 438, 449, 331, 342]) == 71
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 347, 418, 429, 430, 441, 352, 363, 374, 385]) == 69
    assert candidate(nums = [118, 217, 226, 315, 324, 333, 342, 411, 420, 439, 448, 457, 466, 475, 484]) == 184
    assert candidate(nums = [115, 216, 227, 312, 328, 339, 343, 411, 424, 435, 447]) == 117
    assert candidate(nums = [117, 218, 229, 311, 322, 333, 344, 415, 426, 437, 448, 359]) == 131
    assert candidate(nums = [111, 215, 228, 316, 322, 339, 347, 413, 424, 431, 445]) == 87
    assert candidate(nums = [119, 218, 227, 316, 325, 334, 343, 412, 421, 430, 449]) == 141
    assert candidate(nums = [110, 211, 222, 313, 324, 335, 346, 417, 428, 439, 440]) == 57
    assert candidate(nums = [119, 218, 225, 317, 324, 333, 342, 411, 422, 433, 444]) == 133
    assert candidate(nums = [115, 214, 223, 312, 321, 336, 345, 417, 428, 439, 440, 451, 462]) == 110
    assert candidate(nums = [112, 219, 221, 315, 324, 338, 347, 413, 422, 431, 446]) == 95
    assert candidate(nums = [111, 225, 323, 334, 347, 421, 428, 432, 439]) == 23
    assert candidate(nums = [119, 215, 223, 317, 328, 336, 344, 412, 423, 431, 449]) == 135
    assert candidate(nums = [115, 216, 227, 318, 329, 331, 342, 413, 424, 435, 446]) == 123
    assert candidate(nums = [113, 211, 229, 315, 322, 338, 344, 417, 425, 431, 446]) == 85
    assert candidate(nums = [115, 216, 227, 318, 329, 330, 411, 422, 433, 444]) == 100
    assert candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442, 343]) == 93
    assert candidate(nums = [112, 213, 224, 315, 326, 417, 428, 439]) == 61
    assert candidate(nums = [113, 214, 225, 316, 327, 338, 419, 420, 431, 442]) == 82
    assert candidate(nums = [119, 215, 222, 311, 323, 334, 347, 418, 429, 436, 445]) == 125
    assert candidate(nums = [115, 213, 224, 312, 327, 331, 349, 418, 426, 435, 442]) == 99
    assert candidate(nums = [111, 212, 223, 314, 325, 336, 417, 428, 439, 440]) == 64
    assert candidate(nums = [117, 216, 225, 314, 323, 332, 341, 410, 429, 438, 447, 456, 465, 474, 483]) == 162
    assert candidate(nums = [118, 215, 223, 312, 321, 337, 349, 414, 428, 436, 445]) == 119
    assert candidate(nums = [113, 212, 221, 314, 325, 336, 417, 428, 439, 440]) == 72


