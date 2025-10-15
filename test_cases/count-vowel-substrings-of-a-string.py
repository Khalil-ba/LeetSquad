def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(word = "aeiou") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiou") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiofvuaeiou") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiofvuaeiou") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoiea") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoiea") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxaeeiaouoieua") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxaeeiaouoieua") == 28: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 175: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaaioaaaaeiiiiouuuoo") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaaioaaaaeiiiiouuuoo") == 55: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiou") == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiou") == 66: {e}')
    
    total += 1
    try:
        result = candidate(word = "unicornarihan") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "unicornarihan") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aaaaaeeeeeeiiiiioooooouuuuu") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aaaaaeeeeeeiiiiioooooouuuuu") == 25: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouu") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouu") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "vowelsaeiou") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "vowelsaeiou") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "cuaieuouac") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "cuaieuouac") == 7: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiooauuieoiau") == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiooauuieoiau") == 41: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfeioau") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfeioau") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzaeiouzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzaeiouzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiou") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiou") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 496: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiouaeiou") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiouaeiou") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1326
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1326: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiou") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiou") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouuuueeiooiaaaeeoioioiaaaeeuuuiooiiuaeiouaeiouaeiouaeiouaeiou") == 1565
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouuuueeiooiaaaeeoioioiaaaeeuuuiooiiuaeiouaeiouaeiouaeiouaeiou") == 1565: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 231: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoieaueoiaueoiaueoiaueoi") == 208
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoieaueoiaueoiaueoiaueoi") == 208: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 666: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubcdfghjklmnpqrstvwxyzaeiou") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubcdfghjklmnpqrstvwxyzaeiou") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 15: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdaeioufghijklmnopqrstuvwxyz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdaeioufghijklmnopqrstuvwxyz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouwxyzaeiouwxyzaeiouwxyzaeiouwxyz") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouwxyzaeiouwxyzaeiouwxyzaeiouwxyz") == 4: {e}')
    
    total += 1
    try:
        result = candidate(word = "xayaioeoiuaueoieoiauiouio") == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xayaioeoiuaueoieoiauiouio") == 139: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiou") == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiou") == 90: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeiou") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeiou") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcaeiouaeiouaieouacb") == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcaeiouaeiouaieouacb") == 77: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "aieouaeiouaieouaeiouaieouaeiouaieou") == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aieouaeiouaieouaeiouaieouaeiouaieou") == 490: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouuueeiooiaaaeeoioioiaaaeeuuuiooiiu") == 348
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouuueeiooiaaaeeoioioiaaaeeuuuiooiiu") == 348: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeioucaeiou") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeioucaeiou") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouzzzzzzzzz") == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouzzzzzzzzz") == 231: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 8: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiou") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiou") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyaeiouaeiou") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyaeiouaeiou") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeeeeiiiioouuuaeiouaaaeioueee") == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeeeeiiiioouuuaeiouaaaeioueee") == 247: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioucaeioubaeiouaeiou") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioucaeioubaeiouaeiou") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiou") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiou") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyz") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyz") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcaeiouc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcaeiouc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 4656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 4656: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioueoiuaeiouaeioua") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioueoiuaeiouaeioua") == 125: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeeffgghhiijjkkllmmnnooouuupppqqrrsstttuuuvvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeeffgghhiijjkkllmmnnooouuupppqqrrsstttuuuvvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1081
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1081: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 105: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxxxaeiouaeiou") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxxxaeiouaeiou") == 42: {e}')
    
    total += 1
    try:
        result = candidate(word = "aebcioudfeiauoceioua") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aebcioudfeiauoceioua") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aouieaeioueaouieaeiou") == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aouieaeioueaouieaeiou") == 139: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouabcdeiouaeiouabcdeiouaeiou") == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouabcdeiouaeiouabcdeiouaeiou") == 64: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzvvvvvaeeeiioouuuaeiou") == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzvvvvvaeeeiioouuuaeiou") == 44: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoieaueoiaueoiaueoiaueoiaeiou") == 317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoieaueoiaueoiaueoiaueoiaeiou") == 317: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfeaioueaiouaeioueaioueaiou") == 229
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfeaioueaiouaeioueaioueaiou") == 229: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1596: {e}')
    
    total += 1
    try:
        result = candidate(word = "ueaiaoueoiuaeiouaeiouaeiou") == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "ueaiaoueoiuaeiouaeiouaeiou") == 245: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiaeiouoieiouaeiou") == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiaeiouoieiouaeiou") == 93: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufxyzaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeiouf") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufxyzaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeiouf") == 20: {e}')
    
    total += 1
    try:
        result = candidate(word = "uoieaueoiaueoiaueoiaueoiaeiouaeiouaeiouaeiouaeiou") == 1027
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "uoieaueoiaueoiaueoiaueoiaeiouaeiouaeiouaeiouaeiou") == 1027: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiooouiaeiouaeiou") == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiooouiaeiouaeiou") == 92: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiouxyzaeiouaeioubaeiou") == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiouxyzaeiouaeioubaeiou") == 112: {e}')
    
    total += 1
    try:
        result = candidate(word = "aabbccddeeffggahhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aabbccddeeffggahhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouaeiouxyz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouaeiouxyz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioueoiuaeiouaeioueoiuaeiouaeioueoiu") == 529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioueoiuaeiouaeioueoiuaeiouaeioueoiu") == 529: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzaeiouzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzaeiouzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "zbcdefghijklmnopqrstuvwxyaeiou") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zbcdefghijklmnopqrstuvwxyaeiou") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "bcdfgohueaioeuncdfeoiu") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "bcdfgohueaioeuncdfeoiu") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeioudaeioubaeioucaeioudaeioubaeioucaeiou") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeioudaeioubaeioucaeioudaeioubaeioucaeiou") == 9: {e}')
    
    total += 1
    try:
        result = candidate(word = "xaaaeeeiiiiooooouuuuuaaaeiiiou") == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xaaaeeeiiiiooooouuuuuaaaeiiiou") == 131: {e}')
    
    total += 1
    try:
        result = candidate(word = "eiaouoieaueioaeioaeiaoueioea") == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eiaouoieaueioaeioaeiaoueioea") == 253: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouxyzaeiouaeiouaeiouxyzaeiouaeiou") == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouxyzaeiouaeiouaeiouxyzaeiouaeiou") == 153: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzaeiouxyzaeiouxyz") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzaeiouxyzaeiouxyz") == 3: {e}')
    
    total += 1
    try:
        result = candidate(word = "mnopqrstuvwxyaeiouaeiouxyz") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "mnopqrstuvwxyaeiouaeiouxyz") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouaeiouaeiouaeiouaeiouaeiouxyz") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouaeiouaeiouaeiouaeiouaeiouxyz") == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "baeiouaeiouaeiouaeiouaeiou") == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "baeiouaeiouaeiouaeiouaeiou") == 231: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeioudeaeiouf") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeioudeaeiouf") == 5: {e}')
    
    total += 1
    try:
        result = candidate(word = "oiueaeiouaeiouaeiouaeiouaeiouaeiou") == 461
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "oiueaeiouaeiouaeiouaeiouaeiouaeiou") == 461: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeiouaeiouaeiou") == 137
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeiouaeiouaeiou") == 137: {e}')
    
    total += 1
    try:
        result = candidate(word = "zzzzzaeiouzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "zzzzzaeiouzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "baeioucaeiouaeioucb") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "baeioucaeiouaeioucb") == 22: {e}')
    
    total += 1
    try:
        result = candidate(word = "eiouaeioua") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eiouaeioua") == 21: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeioubaeiou") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeioubaeiou") == 23: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzabcdeioufghijklmnopqrstuvwaeiou") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzabcdeioufghijklmnopqrstuvwaeiou") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeeeeeiioouuuuuaeiou") == 146
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeeeeeiioouuuuuaeiou") == 146: {e}')
    
    total += 1
    try:
        result = candidate(word = "abcdeioua") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "abcdeioua") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 10: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioueaioueaioueaioueaioueaiou") == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioueaioueaioueaioueaioueaiou") == 350: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeioubaeiouaeioubaeiouaeiou") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeioubaeiouaeioubaeiouaeiou") == 43: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaebcdeaeiouaeiou") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaebcdeaeiouaeiou") == 63: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 351
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 351: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouaeiouaeiou") == 136
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouaeiouaeiou") == 136: {e}')
    
    total += 1
    try:
        result = candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 84
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 84: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouzyxwvutsrqponmlkjihgfedcbaeiou") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouzyxwvutsrqponmlkjihgfedcbaeiou") == 2: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouzzzzzzzzzzzzzzzzzzzz") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouzzzzzzzzzzzzzzzzzzzz") == 1: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 69: {e}')
    
    total += 1
    try:
        result = candidate(word = "eiouaeiouaeiouaeiouaeiouaeiou") == 325
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "eiouaeiouaeiouaeiouaeiouaeiou") == 325: {e}')
    
    total += 1
    try:
        result = candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 147: {e}')
    
    total += 1
    try:
        result = candidate(word = "xzaeiouaeiouaeiouaeiouaeioux") == 231
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(word = "xzaeiouaeiouaeiouaeiouaeioux") == 231: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(word = "aeiou") == 1
    assert candidate(word = "aeiofvuaeiou") == 3
    assert candidate(word = "uoiea") == 1
    assert candidate(word = "aeiouxaeeiaouoieua") == 28
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 175
    assert candidate(word = "aeiaaioaaaaeiiiiouuuoo") == 55
    assert candidate(word = "aeiouaeiouaeiou") == 66
    assert candidate(word = "unicornarihan") == 0
    assert candidate(word = "aaaaaeeeeeeiiiiioooooouuuuu") == 25
    assert candidate(word = "aeiouu") == 2
    assert candidate(word = "a") == 0
    assert candidate(word = "abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "vowelsaeiou") == 1
    assert candidate(word = "cuaieuouac") == 7
    assert candidate(word = "aeiooauuieoiau") == 41
    assert candidate(word = "bcdfeioau") == 1
    assert candidate(word = "zzzzzaeiouzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiou") == 43
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 496
    assert candidate(word = "aeiouxyzaeiouaeiou") == 22
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1326
    assert candidate(word = "aeiouxyzaeiou") == 2
    assert candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63
    assert candidate(word = "aeiouuuueeiooiaaaeeoioioiaaaeeuuuiooiiuaeiouaeiouaeiouaeiouaeiou") == 1565
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 231
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 63
    assert candidate(word = "uoieaueoiaueoiaueoiaueoi") == 208
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 666
    assert candidate(word = "aeioubcdfghjklmnpqrstvwxyzaeiou") == 2
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 63
    assert candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 15
    assert candidate(word = "bcdaeioufghijklmnopqrstuvwxyz") == 1
    assert candidate(word = "aeiouwxyzaeiouwxyzaeiouwxyzaeiouwxyz") == 4
    assert candidate(word = "xayaioeoiuaueoieoiauiouio") == 139
    assert candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiou") == 90
    assert candidate(word = "aeioubaeioucaeiou") == 3
    assert candidate(word = "bcaeiouaeiouaieouacb") == 77
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyz") == 42
    assert candidate(word = "aieouaeiouaieouaeiouaieouaeiouaieou") == 490
    assert candidate(word = "aeiouuueeiooiaaaeeoioioiaaaeeuuuiooiiu") == 348
    assert candidate(word = "aeioubaeiouaeioucaeiou") == 23
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouzzzzzzzzz") == 231
    assert candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 8
    assert candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiou") == 22
    assert candidate(word = "aeiouxyaeiouaeiou") == 22
    assert candidate(word = "aeeeeiiiioouuuaeiouaaaeioueee") == 247
    assert candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiouxyz") == 5
    assert candidate(word = "aeioucaeioubaeiouaeiou") == 23
    assert candidate(word = "aeiouxyzaeiouxyzaeiouxyzaeiouxyzaeiou") == 5
    assert candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyz") == 42
    assert candidate(word = "mnopqrstuvwxyaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 23
    assert candidate(word = "bcaeiouc") == 1
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 4656
    assert candidate(word = "aeioueoiuaeiouaeioua") == 125
    assert candidate(word = "aabbccddeeeffgghhiijjkkllmmnnooouuupppqqrrsstttuuuvvvwwxxyyzz") == 0
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1081
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 105
    assert candidate(word = "aeiouaeiouxxxaeiouaeiou") == 42
    assert candidate(word = "aebcioudfeiauoceioua") == 2
    assert candidate(word = "aouieaeioueaouieaeiou") == 139
    assert candidate(word = "aeiouaeiouabcdeiouaeiouabcdeiouaeiou") == 64
    assert candidate(word = "zzzzzvvvvvaeeeiioouuuaeiou") == 44
    assert candidate(word = "uoieaueoiaueoiaueoiaueoiaeiou") == 317
    assert candidate(word = "bcdfeaioueaiouaeioueaioueaiou") == 229
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou") == 1596
    assert candidate(word = "ueaiaoueoiuaeiouaeiouaeiou") == 245
    assert candidate(word = "aeiaeiouoieiouaeiou") == 93
    assert candidate(word = "aeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeioufxyzaeioubaeioucaeioudaeioufaeioubaeioucaeioudaeiouf") == 20
    assert candidate(word = "uoieaueoiaueoiaueoiaueoiaeiouaeiouaeiouaeiouaeiou") == 1027
    assert candidate(word = "aeiooouiaeiouaeiou") == 92
    assert candidate(word = "aeioubaeiouaeioubaeiouxyzaeiouaeiouaeioubaeiouxyzaeiouaeioubaeiou") == 112
    assert candidate(word = "aabbccddeeffggahhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == 0
    assert candidate(word = "xyzaeiouaeiouxyz") == 21
    assert candidate(word = "aeioueoiuaeiouaeioueoiuaeiouaeioueoiu") == 529
    assert candidate(word = "zzzzzaeiouzzzzzzzzzz") == 1
    assert candidate(word = "zbcdefghijklmnopqrstuvwxyaeiou") == 1
    assert candidate(word = "bcdfgohueaioeuncdfeoiu") == 5
    assert candidate(word = "aeioubaeioucaeioudaeioubaeioucaeioudaeioubaeioucaeiou") == 9
    assert candidate(word = "xaaaeeeiiiiooooouuuuuaaaeiiiou") == 131
    assert candidate(word = "eiaouoieaueioaeioaeiaoueioea") == 253
    assert candidate(word = "aeiouaeiouaeiouxyzaeiouaeiouaeiouxyzaeiouaeiou") == 153
    assert candidate(word = "aeiouxyzaeiouxyzaeiouxyz") == 3
    assert candidate(word = "mnopqrstuvwxyaeiouaeiouxyz") == 21
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 84
    assert candidate(word = "xyzaeiouaeiouaeiouaeiouaeiouaeiouxyz") == 351
    assert candidate(word = "baeiouaeiouaeiouaeiouaeiou") == 231
    assert candidate(word = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(word = "aeioubaeioucaeioudeaeiouf") == 5
    assert candidate(word = "oiueaeiouaeiouaeiouaeiouaeiouaeiou") == 461
    assert candidate(word = "aeioubaeiouaeiouaeiouaeiou") == 137
    assert candidate(word = "zzzzzaeiouzzzzz") == 1
    assert candidate(word = "baeioucaeiouaeioucb") == 22
    assert candidate(word = "eiouaeioua") == 21
    assert candidate(word = "aeioubaeiouaeioubaeiou") == 23
    assert candidate(word = "xyzabcdeioufghijklmnopqrstuvwaeiou") == 1
    assert candidate(word = "aeiouaeeeeeiioouuuuuaeiou") == 146
    assert candidate(word = "abcdeioua") == 1
    assert candidate(word = "aeioubaeioucaeioudeaeioufaeioubaeioucaeioudeaeiouf") == 10
    assert candidate(word = "aeioueaioueaioueaioueaioueaiou") == 350
    assert candidate(word = "aeioubaeiouaeioubaeiouaeiou") == 43
    assert candidate(word = "aeiouaeiouaebcdeaeiouaeiou") == 63
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiouaeiou") == 351
    assert candidate(word = "aeiouaeiouaeiouaeiou") == 136
    assert candidate(word = "xyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiou") == 84
    assert candidate(word = "aeiouzyxwvutsrqponmlkjihgfedcbaeiou") == 2
    assert candidate(word = "aeiouzzzzzzzzzzzzzzzzzzzz") == 1
    assert candidate(word = "aeiouxyzzyxwvutsrqponmlkjihgfedcbaeiouaeiouaeiouxyzaeiouxyzzyxwvutsrqponmlkjihgfedcbaeiou") == 69
    assert candidate(word = "eiouaeiouaeiouaeiouaeiouaeiou") == 325
    assert candidate(word = "aeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyzaeiouaeiouxyz") == 147
    assert candidate(word = "xzaeiouaeiouaeiouaeiouaeioux") == 231


