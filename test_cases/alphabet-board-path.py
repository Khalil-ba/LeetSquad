def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = "azaz") == "!DDDDD!UUUUU!DDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "azaz") == "!DDDDD!UUUUU!DDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zm") == "DDDDD!UUURR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zm") == "DDDDD!UUURR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcde") == "!R!R!R!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcde") == "!R!R!R!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "leet") == "RDD!UURRR!!DDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "leet") == "RDD!UURRR!!DDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zuz") == "DDDDD!U!D!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zuz") == "DDDDD!U!D!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abc") == "!R!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abc") == "!R!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zb") == "DDDDD!UUUUUR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zb") == "DDDDD!UUUUUR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyzzzzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyzzzzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zz") == "DDDDD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zz") == "DDDDD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxy") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxy") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "xyz") == "RRRDDDD!R!LLLLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "xyz") == "RRRDDDD!R!LLLLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zyxwvutsrqponmlkjihgfedcba") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zyxwvutsrqponmlkjihgfedcba") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zbcd") == "DDDDD!UUUUUR!R!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zbcd") == "DDDDD!UUUUUR!R!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zdz") == "DDDDD!UUUUURRR!LLLDDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zdz") == "DDDDD!UUUUURRR!LLLDDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "a") == "!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "a") == "!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnopqrstuvwxyzz") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnopqrstuvwxyzz") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzz") == "DDDDD!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzz") == "DDDDD!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "code") == "RR!RRDD!LUU!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "code") == "RR!RRDD!LUU!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzzz") == "DDDDD!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzzz") == "DDDDD!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "az") == "!DDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "az") == "!DDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "algorithms") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!RD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "algorithms") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!RD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "inputs") == "RRRD!D!LLLD!D!URRRR!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "inputs") == "RRRD!D!LLLD!D!URRRR!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "hello") == "RRD!URR!LLLDD!!RRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "hello") == "RRD!URR!LLLDD!!RRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "elephant") == "RRRR!LLLDD!UURRR!LLLLDDD!UURR!LLU!RRRDD!RD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "elephant") == "RRRR!LLLDD!UURRR!LLLLDDD!UURR!LLU!RRRDD!RD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "alphabet") == "!RDD!LD!UURR!LLU!R!RRR!DDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "alphabet") == "!RDD!LD!UURR!LLU!R!RRR!DDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccccddddddddddddeeeeeeeeeeeefffffffffffgggggggggggghhhhhhhhhhhhiiiiiiiiiiiijjjjjjjjjjjjkkkkkkkkkkklllllllllllmmmmmmmmmmmnnnnnnnnnnnoooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwxxxyyyyyyyyzzzzzzzz") == "!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!R!!!R!!!!!!!!LLLLD!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccccddddddddddddeeeeeeeeeeeefffffffffffgggggggggggghhhhhhhhhhhhiiiiiiiiiiiijjjjjjjjjjjjkkkkkkkkkkklllllllllllmmmmmmmmmmmnnnnnnnnnnnoooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwxxxyyyyyyyyzzzzzzzz") == "!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!R!!!R!!!!!!!!LLLLD!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "qrstuvwxyza") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "qrstuvwxyza") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "minimum") == "RRDD!UR!D!U!LD!LLDD!UURR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "minimum") == "RRDD!UR!D!U!LD!LLDD!UURR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zxywvutsrqponmlkjihgfedcba") == "DDDDD!URRR!R!LL!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zxywvutsrqponmlkjihgfedcba") == "DDDDD!URRR!R!LL!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "fish") == "D!RRR!DD!LUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "fish") == "D!RRR!DD!LUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "snake") == "RRRDDD!U!LLLUU!DD!UURRRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "snake") == "RRRDDD!U!LLLUU!DD!UURRRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "uvwxyz") == "DDDD!R!R!R!R!LLLLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "uvwxyz") == "DDDD!R!R!R!R!LLLLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab") == "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab") == "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "whale") == "RRDDDD!UUU!LLU!RDD!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "whale") == "RRDDDD!UUU!LLU!RDD!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnopqrstuvwxyzabcde") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!R!R!R!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnopqrstuvwxyzabcde") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!R!R!R!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "rhythm") == "RRDDD!UU!RRDDD!U!LLUU!D!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "rhythm") == "RRDDD!UU!RRDDD!U!LLUU!D!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "testcase") == "RRRRDDD!UUU!LDDD!R!LLUUU!LL!RRRDDD!UUUR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "testcase") == "RRRRDDD!UUU!LDDD!R!LLUUU!LL!RRRDDD!UUUR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "hellofromtheotherside") == "RRD!URR!LLLDD!!RRR!LLLLU!RRDD!URR!LL!RRD!LLUU!URR!DD!D!LLUU!URR!LLDDD!R!UU!U!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "hellofromtheotherside") == "RRD!URR!LLLDD!!RRR!LLLLU!RRDD!URR!LL!RRD!LLUU!URR!DD!D!LLUU!URR!LLDDD!R!UU!U!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "pythonprogramming") == "DDD!RRRRD!U!LLUU!RRD!L!LLLD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "pythonprogramming") == "DDD!RRRRD!U!LLUU!RRD!L!LLLD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "qpwoeiuytrmnbvcxzlkjhgfdsaz") == "RDDD!L!RRD!UURR!UU!LD!LLLDDD!RRRR!U!LL!U!R!LLUU!DDDD!UUUUR!RDDDD!LLLD!UUUR!L!URRRR!LL!L!L!URRR!DDD!LLLUUU!DDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "qpwoeiuytrmnbvcxzlkjhgfdsaz") == "RDDD!L!RRD!UURR!UU!LD!LLLDDD!RRRR!U!LL!U!R!LLUU!DDDD!UUUUR!RDDDD!LLLD!UUUR!L!URRRR!LL!L!L!URRR!DDD!LLLUUU!DDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "quicksand") == "RDDD!LD!UUURRR!LU!LLDD!RRRD!LLLUUU!RRRDD!UU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "quicksand") == "RDDD!LD!UUURRR!LU!LLDD!RRRD!LLLUUU!RRRDD!UU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abacaxabacax") == "!R!L!RR!LL!RRRDDDD!LLLUUUU!R!L!RR!LL!RRRDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abacaxabacax") == "!R!L!RR!LL!RRRDDDD!LLLUUUU!R!L!RR!LL!RRRDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "movesteps") == "RRDD!RR!LLLDD!UUUURRR!LDDD!R!UUU!LLLLDDD!RRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "movesteps") == "RRDD!RR!LLLDD!UUUURRR!LDDD!R!UUU!LLLLDDD!RRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzazzazzazz") == "DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzazzazzazz") == "DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "ddddddddeeeeeeeeedddddddd") == "RRR!!!!!!!!R!!!!!!!!!L!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "ddddddddeeeeeeeeedddddddd") == "RRR!!!!!!!!R!!!!!!!!!L!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "crocodile") == "RR!DDD!URR!LLUU!RRDD!LUU!D!LLD!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "crocodile") == "RR!DDD!URR!LLUU!RRDD!LUU!D!LLD!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "aaabbbcccddd") == "!!!R!!!R!!!R!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "aaabbbcccddd") == "!!!R!!!R!!!R!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "microsoft") == "RRDD!UR!LU!DDD!URR!LD!UR!LLLLU!RRRRDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "microsoft") == "RRDD!UR!LU!DDD!URR!LD!UR!LLLLU!RRRRDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnopqrstuvwxyza") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnopqrstuvwxyza") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "uvwxyzz") == "DDDD!R!R!R!R!LLLLD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "uvwxyzz") == "DDDD!R!R!R!R!LLLLD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "board") == "R!RRRDD!LLLLUU!RRDDD!UUUR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "board") == "R!RRRDD!LLLLUU!RRDDD!UUUR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "solution") == "RRRDDD!UR!LLL!LDD!URRRR!LUU!RD!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "solution") == "RRRDDD!UR!LLL!LDD!URRRR!LUU!RD!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyzaa") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyzaa") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "qpwoeirutyalskdjfhgzxcvbnm") == "RDDD!L!RRD!UURR!UU!LD!LDD!LLD!URRRR!D!LLLLUUUU!RDD!RRD!LLLU!UURRR!RD!LLLL!RR!L!LDDDD!URRR!LUUUU!LDDDD!UUUU!RRDD!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "qpwoeirutyalskdjfhgzxcvbnm") == "RDDD!L!RRD!UURR!UU!LD!LDD!LLD!URRRR!D!LLLLUUUU!RDD!RRD!LLLU!UURRR!RD!LLLL!RR!L!LDDDD!URRR!LUUUU!LDDDD!UUUU!RRDD!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "xyzzzyxyzzz") == "RRRDDDD!R!LLLLD!!!URRRR!L!R!LLLLD!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "xyzzzyxyzzz") == "RRRDDDD!R!LLLLD!!!URRRR!L!R!LLLLD!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "challenge") == "RR!D!LLU!RDD!!UURRR!LDD!LLU!URRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "challenge") == "RR!D!LLU!RDD!!UURRR!LDD!LLU!URRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnopqrstu") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnopqrstu") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "giraffe") == "RD!RR!LDD!LLUUU!D!!URRRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "giraffe") == "RD!RR!LDD!LLUUU!D!!URRRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zyxwvutsrqponmlkjihgfedcbaaabbbcccddd") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!!!R!!!R!!!R!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zyxwvutsrqponmlkjihgfedcbaaabbbcccddd") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!!!R!!!R!!!R!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "dolphin") == "RRR!RDD!LLL!LD!UURR!R!D!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "dolphin") == "RRR!RDD!LLL!LD!UURR!R!D!": {e}')
    
    total += 1
    try:
        result = candidate(target = "efficient") == "RRRR!LLLLD!!RRR!LU!RD!UR!LDD!RD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "efficient") == "RRRR!LLLLD!!RRR!LU!RD!UR!LDD!RD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "hellothere") == "RRD!URR!LLLDD!!RRR!D!LLUU!URR!LLDDD!UUURR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "hellothere") == "RRD!URR!LLLDD!!RRR!D!LLUU!URR!LLDDD!UUURR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "thequickbrownfoxjumpsoverthelazydog") == "RRRRDDD!LLUU!URR!LLLDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!UUUR!LLLLDDD!UURR!LLD!RRR!UR!LLLDD!UUUURRR!LLDDD!RR!LLUU!URR!LLLDD!LUU!DDDDD!URRRR!LUUUU!RDD!LLLU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "thequickbrownfoxjumpsoverthelazydog") == "RRRRDDD!LLUU!URR!LLLDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!UUUR!LLLLDDD!UURR!LLD!RRR!UR!LLLDD!UUUURRR!LLDDD!RR!LLUU!URR!LLLDD!LUU!DDDDD!URRRR!LUUUU!RDD!LLLU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mississippi") == "RRDD!UR!DD!!UU!DD!!UU!LLLDD!!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mississippi") == "RRDD!UR!DD!!UU!DD!!UU!LLLDD!!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "dynamic") == "RRR!RDDDD!LUU!LLLUU!RRDD!UR!LU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "dynamic") == "RRR!RDDDD!LUU!LLLUU!RRDD!UR!LU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "programming") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "programming") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "world") == "RRDDDD!UURR!LLD!LU!UURR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "world") == "RRDDDD!UURR!LLD!LU!UURR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "alphabetboardpath") == "!RDD!LD!UURR!LLU!R!RRR!DDD!LLLUUU!RRRDD!LLLLUU!RRDDD!UUUR!LLLDDD!UUU!RRRRDDD!LLUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "alphabetboardpath") == "!RDD!LD!UURR!LLU!R!RRR!DDD!LLLUUU!RRRDD!LLLLUU!RRDDD!UUUR!LLLDDD!UUU!RRRRDDD!LLUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzz") == "DDDDD!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzz") == "DDDDD!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "jump") == "RRRRD!LLLLDDD!UURR!LLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "jump") == "RRRRD!LLLLDDD!UURR!LLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "interview") == "RRRD!D!RD!UUU!LLDDD!LD!UUURR!UR!LLDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "interview") == "RRRD!D!RD!UUU!LLDDD!LD!UUURR!UR!LLDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "python") == "DDD!RRRRD!U!LLUU!RRD!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "python") == "DDD!RRRRD!U!LLUU!RRD!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "qrstuvwxyzaa") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "qrstuvwxyzaa") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "xylophone") == "RRRDDDD!R!LLLUU!RRR!LLLLD!UURR!RRD!L!UUR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "xylophone") == "RRRDDDD!R!LLLUU!RRR!LLLLD!UURR!RRD!L!UUR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "supercalifragilisticexpialidocious") == "RRRDDD!LLLD!U!UUURRRR!LLDDD!UUU!LL!RDD!URR!LLL!RRDD!LLUUU!RD!RR!LLD!URR!DD!R!LUU!LU!RR!LDDDD!LLLU!UURRR!LLLU!RDD!URR!U!RDD!LLUU!RD!RD!LLLLDD!URRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "supercalifragilisticexpialidocious") == "RRRDDD!LLLD!U!UUURRRR!LLDDD!UUU!LL!RDD!URR!LLL!RRDD!LLUUU!RD!RR!LLD!URR!DD!R!LUU!LU!RR!LDDDD!LLLU!UURRR!LLLU!RDD!URR!U!RDD!LLUU!RD!RD!LLLLDD!URRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "quickbrownfox") == "RDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "quickbrownfox") == "RDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "complex") == "RR!RRDD!LL!LLD!UR!UURRR!LDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "complex") == "RR!RRDD!LL!LLD!UR!UURRR!LDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "hellozworld") == "RRD!URR!LLLDD!!RRR!LLLLDDD!URR!UURR!LLD!LU!UURR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "hellozworld") == "RRD!URR!LLLDD!!RRR!LLLLDDD!URR!UURR!LLD!LU!UURR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "tiger") == "RRRRDDD!LUU!LL!URRR!LLDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "tiger") == "RRRRDDD!LUU!LL!URRR!LLDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "lxyzzzz") == "RDD!RRDD!R!LLLLD!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "lxyzzzz") == "RDD!RRDD!R!LLLLD!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghiz") == "!R!R!R!R!LLLLD!R!R!R!LLLDDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghiz") == "!R!R!R!R!LLLLD!R!R!R!LLLDDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "leetcode") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "leetcode") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!": {e}')
    
    total += 1
    try:
        result = candidate(target = "xyzzyx") == "RRRDDDD!R!LLLLD!!URRRR!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "xyzzyx") == "RRRDDDD!R!LLLLD!!URRRR!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "bza") == "R!LDDDDD!UUUUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "bza") == "R!LDDDDD!UUUUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnonmlkjihgfedcba") == "RRDD!R!R!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnonmlkjihgfedcba") == "RRDD!R!R!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!": {e}')
    
    total += 1
    try:
        result = candidate(target = "algorithm") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "algorithm") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!": {e}')
    
    total += 1
    try:
        result = candidate(target = "sequence") == "RRRDDD!UUUR!LLLDDD!LD!UUUURRRR!LDD!LUU!RR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "sequence") == "RRRDDD!UUUR!LLLDDD!LD!UUUURRRR!LDD!LUU!RR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "leetcodeisfun") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!LD!DD!LLLUU!DDD!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "leetcodeisfun") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!LD!DD!LLLUU!DDD!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefgHIJKLmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!LUUUUUU!R!R!R!R!LLDDDDDDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefgHIJKLmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!LUUUUUU!R!R!R!R!LLDDDDDDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "programmingisfun") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!RR!DD!LLLUU!DDD!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "programmingisfun") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!RR!DD!LLLUU!DDD!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "datastructures") == "RRR!LLL!RRRRDDD!LLLLUUU!RRRDDD!R!LL!LLD!UUUURR!RRDDD!LLLLD!URR!UUURR!LDDD!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "datastructures") == "RRR!LLL!RRRRDDD!LLLLUUU!RRRDDD!R!LL!LLD!UUUURR!RRDDD!LLLLD!URR!UUURR!LDDD!": {e}')
    
    total += 1
    try:
        result = candidate(target = "zzzzzzzzzz") == "DDDDD!!!!!!!!!!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "zzzzzzzzzz") == "DDDDD!!!!!!!!!!": {e}')
    
    total += 1
    try:
        result = candidate(target = "example") == "RRRR!LDDDD!LLLUUUU!RRDD!LLD!UR!UURRR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "example") == "RRRR!LDDDD!LLLUUUU!RRDD!LLD!UR!UURRR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "mnonmonmnonmo") == "RRDD!R!R!L!L!RR!L!L!R!R!L!L!RR!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "mnonmonmnonmo") == "RRDD!R!R!L!L!RR!L!L!R!R!L!L!RR!": {e}')
    
    total += 1
    try:
        result = candidate(target = "abcdefghijklmnopqrstuvwxyza") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "abcdefghijklmnopqrstuvwxyza") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!": {e}')
    
    total += 1
    try:
        result = candidate(target = "question") == "RDDD!LD!UUUURRRR!LDDD!R!LUU!RD!L!"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = "question") == "RDDD!LD!UUUURRRR!LDDD!R!LUU!RD!L!": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = "azaz") == "!DDDDD!UUUUU!DDDDD!"
    assert candidate(target = "zm") == "DDDDD!UUURR!"
    assert candidate(target = "abcde") == "!R!R!R!R!"
    assert candidate(target = "leet") == "RDD!UURRR!!DDD!"
    assert candidate(target = "zuz") == "DDDDD!U!D!"
    assert candidate(target = "abc") == "!R!R!"
    assert candidate(target = "zb") == "DDDDD!UUUUUR!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyzzzzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!!!!"
    assert candidate(target = "zz") == "DDDDD!!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxy") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!"
    assert candidate(target = "xyz") == "RRRDDDD!R!LLLLD!"
    assert candidate(target = "zyxwvutsrqponmlkjihgfedcba") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
    assert candidate(target = "zbcd") == "DDDDD!UUUUUR!R!R!"
    assert candidate(target = "zdz") == "DDDDD!UUUUURRR!LLLDDDDD!"
    assert candidate(target = "a") == "!"
    assert candidate(target = "mnopqrstuvwxyzz") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!"
    assert candidate(target = "zzz") == "DDDDD!!!"
    assert candidate(target = "code") == "RR!RRDD!LUU!R!"
    assert candidate(target = "zzzzz") == "DDDDD!!!!!"
    assert candidate(target = "az") == "!DDDDD!"
    assert candidate(target = "algorithms") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!RD!"
    assert candidate(target = "inputs") == "RRRD!D!LLLD!D!URRRR!L!"
    assert candidate(target = "hello") == "RRD!URR!LLLDD!!RRR!"
    assert candidate(target = "elephant") == "RRRR!LLLDD!UURRR!LLLLDDD!UURR!LLU!RRRDD!RD!"
    assert candidate(target = "alphabet") == "!RDD!LD!UURR!LLU!R!RRR!DDD!"
    assert candidate(target = "aaaaaaaaaaaabbbbbbbbbbbbccccccccccccddddddddddddeeeeeeeeeeeefffffffffffgggggggggggghhhhhhhhhhhhiiiiiiiiiiiijjjjjjjjjjjjkkkkkkkkkkklllllllllllmmmmmmmmmmmnnnnnnnnnnnoooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwxxxyyyyyyyyzzzzzzzz") == "!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!R!!!!!!!!!!!!LLLLD!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!!!R!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!!LLLLD!!!!!!!!!!R!!!!!!!!!!R!!!!!!!!!R!!!R!!!!!!!!LLLLD!!!!!!!!"
    assert candidate(target = "qrstuvwxyza") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
    assert candidate(target = "minimum") == "RRDD!UR!D!U!LD!LLDD!UURR!"
    assert candidate(target = "zxywvutsrqponmlkjihgfedcba") == "DDDDD!URRR!R!LL!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
    assert candidate(target = "fish") == "D!RRR!DD!LUU!"
    assert candidate(target = "snake") == "RRRDDD!U!LLLUU!DD!UURRRR!"
    assert candidate(target = "uvwxyz") == "DDDD!R!R!R!R!LLLLD!"
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    assert candidate(target = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab") == "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!R!"
    assert candidate(target = "whale") == "RRDDDD!UUU!LLU!RDD!UURRR!"
    assert candidate(target = "mnopqrstuvwxyzabcde") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!R!R!R!R!"
    assert candidate(target = "rhythm") == "RRDDD!UU!RRDDD!U!LLUU!D!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!"
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    assert candidate(target = "testcase") == "RRRRDDD!UUU!LDDD!R!LLUUU!LL!RRRDDD!UUUR!"
    assert candidate(target = "hellofromtheotherside") == "RRD!URR!LLLDD!!RRR!LLLLU!RRDD!URR!LL!RRD!LLUU!URR!DD!D!LLUU!URR!LLDDD!R!UU!U!R!"
    assert candidate(target = "pythonprogramming") == "DDD!RRRRD!U!LLUU!RRD!L!LLLD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!"
    assert candidate(target = "qpwoeiuytrmnbvcxzlkjhgfdsaz") == "RDDD!L!RRD!UURR!UU!LD!LLLDDD!RRRR!U!LL!U!R!LLUU!DDDD!UUUUR!RDDDD!LLLD!UUUR!L!URRRR!LL!L!L!URRR!DDD!LLLUUU!DDDDD!"
    assert candidate(target = "quicksand") == "RDDD!LD!UUURRR!LU!LLDD!RRRD!LLLUUU!RRRDD!UU!"
    assert candidate(target = "abacaxabacax") == "!R!L!RR!LL!RRRDDDD!LLLUUUU!R!L!RR!LL!RRRDDDD!"
    assert candidate(target = "movesteps") == "RRDD!RR!LLLDD!UUUURRR!LDDD!R!UUU!LLLLDDD!RRR!"
    assert candidate(target = "zzazzazzazz") == "DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!UUUUU!DDDDD!!"
    assert candidate(target = "ddddddddeeeeeeeeedddddddd") == "RRR!!!!!!!!R!!!!!!!!!L!!!!!!!!"
    assert candidate(target = "crocodile") == "RR!DDD!URR!LLUU!RRDD!LUU!D!LLD!UURRR!"
    assert candidate(target = "aaabbbcccddd") == "!!!R!!!R!!!R!!!"
    assert candidate(target = "microsoft") == "RRDD!UR!LU!DDD!URR!LD!UR!LLLLU!RRRRDD!"
    assert candidate(target = "mnopqrstuvwxyza") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
    assert candidate(target = "uvwxyzz") == "DDDD!R!R!R!R!LLLLD!!"
    assert candidate(target = "board") == "R!RRRDD!LLLLUU!RRDDD!UUUR!"
    assert candidate(target = "solution") == "RRRDDD!UR!LLL!LDD!URRRR!LUU!RD!L!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyzaa") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!"
    assert candidate(target = "qpwoeirutyalskdjfhgzxcvbnm") == "RDDD!L!RRD!UURR!UU!LD!LDD!LLD!URRRR!D!LLLLUUUU!RDD!RRD!LLLU!UURRR!RD!LLLL!RR!L!LDDDD!URRR!LUUUU!LDDDD!UUUU!RRDD!L!"
    assert candidate(target = "xyzzzyxyzzz") == "RRRDDDD!R!LLLLD!!!URRRR!L!R!LLLLD!!!"
    assert candidate(target = "mnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
    assert candidate(target = "challenge") == "RR!D!LLU!RDD!!UURRR!LDD!LLU!URRR!"
    assert candidate(target = "mnopqrstu") == "RRDD!R!R!LLLLD!R!R!R!R!LLLLD!"
    assert candidate(target = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz") == "DDDDD!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    assert candidate(target = "giraffe") == "RD!RR!LDD!LLUUU!D!!URRRR!"
    assert candidate(target = "zyxwvutsrqponmlkjihgfedcbaaabbbcccddd") == "DDDDD!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!!!R!!!R!!!R!!!"
    assert candidate(target = "dolphin") == "RRR!RDD!LLL!LD!UURR!R!D!"
    assert candidate(target = "efficient") == "RRRR!LLLLD!!RRR!LU!RD!UR!LDD!RD!"
    assert candidate(target = "hellothere") == "RRD!URR!LLLDD!!RRR!D!LLUU!URR!LLDDD!UUURR!"
    assert candidate(target = "thequickbrownfoxjumpsoverthelazydog") == "RRRRDDD!LLUU!URR!LLLDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!UUUR!LLLLDDD!UURR!LLD!RRR!UR!LLLDD!UUUURRR!LLDDD!RR!LLUU!URR!LLLDD!LUU!DDDDD!URRRR!LUUUU!RDD!LLLU!"
    assert candidate(target = "mississippi") == "RRDD!UR!DD!!UU!DD!!UU!LLLDD!!UURRR!"
    assert candidate(target = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz") == "!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!R!!R!!R!!R!!LLLLD!!"
    assert candidate(target = "dynamic") == "RRR!RDDDD!LUU!LLLUU!RRDD!UR!LU!"
    assert candidate(target = "programming") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!"
    assert candidate(target = "world") == "RRDDDD!UURR!LLD!LU!UURR!"
    assert candidate(target = "alphabetboardpath") == "!RDD!LD!UURR!LLU!R!RRR!DDD!LLLUUU!RRRDD!LLLLUU!RRDDD!UUUR!LLLDDD!UUU!RRRRDDD!LLUU!"
    assert candidate(target = "zzzz") == "DDDDD!!!!"
    assert candidate(target = "jump") == "RRRRD!LLLLDDD!UURR!LLD!"
    assert candidate(target = "interview") == "RRRD!D!RD!UUU!LLDDD!LD!UUURR!UR!LLDDDD!"
    assert candidate(target = "python") == "DDD!RRRRD!U!LLUU!RRD!L!"
    assert candidate(target = "qrstuvwxyzaa") == "RDDD!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!!"
    assert candidate(target = "xylophone") == "RRRDDDD!R!LLLUU!RRR!LLLLD!UURR!RRD!L!UUR!"
    assert candidate(target = "supercalifragilisticexpialidocious") == "RRRDDD!LLLD!U!UUURRRR!LLDDD!UUU!LL!RDD!URR!LLL!RRDD!LLUUU!RD!RR!LLD!URR!DD!R!LUU!LU!RR!LDDDD!LLLU!UURRR!LLLU!RDD!URR!U!RDD!LLUU!RD!RD!LLLLDD!URRR!"
    assert candidate(target = "quickbrownfox") == "RDDD!LD!UUURRR!LU!LLDD!UUR!RDDD!URR!LLDD!UUR!LLLU!RRRRD!LDD!"
    assert candidate(target = "complex") == "RR!RRDD!LL!LLD!UR!UURRR!LDDDD!"
    assert candidate(target = "hellozworld") == "RRD!URR!LLLDD!!RRR!LLLLDDD!URR!UURR!LLD!LU!UURR!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyzz") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!!"
    assert candidate(target = "tiger") == "RRRRDDD!LUU!LL!URRR!LLDDD!"
    assert candidate(target = "lxyzzzz") == "RDD!RRDD!R!LLLLD!!!!"
    assert candidate(target = "abcdefghiz") == "!R!R!R!R!LLLLD!R!R!R!LLLDDDD!"
    assert candidate(target = "leetcode") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!"
    assert candidate(target = "xyzzyx") == "RRRDDDD!R!LLLLD!!URRRR!L!"
    assert candidate(target = "bza") == "R!LDDDDD!UUUUU!"
    assert candidate(target = "mnonmlkjihgfedcba") == "RRDD!R!R!L!L!L!L!URRRR!L!L!L!L!URRRR!L!L!L!L!"
    assert candidate(target = "algorithm") == "!RDD!U!RRRD!LLD!UUR!RDD!LLUU!D!"
    assert candidate(target = "sequence") == "RRRDDD!UUUR!LLLDDD!LD!UUUURRRR!LDD!LUU!RR!"
    assert candidate(target = "leetcodeisfun") == "RDD!UURRR!!DDD!LLUUU!RRDD!LUU!R!LD!DD!LLLUU!DDD!UURRR!"
    assert candidate(target = "abcdefgHIJKLmnopqrstuvwxyz") == "!R!R!R!R!LLLLD!R!LUUUUUU!R!R!R!R!LLDDDDDDD!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!"
    assert candidate(target = "programmingisfun") == "DDD!RR!URR!LLLU!RDD!LLUUU!RRDD!!UR!D!LLU!RR!DD!LLLUU!DDD!UURRR!"
    assert candidate(target = "datastructures") == "RRR!LLL!RRRRDDD!LLLLUUU!RRRDDD!R!LL!LLD!UUUURR!RRDDD!LLLLD!URR!UUURR!LDDD!"
    assert candidate(target = "zzzzzzzzzz") == "DDDDD!!!!!!!!!!"
    assert candidate(target = "example") == "RRRR!LDDDD!LLLUUUU!RRDD!LLD!UR!UURRR!"
    assert candidate(target = "mnonmonmnonmo") == "RRDD!R!R!L!L!RR!L!L!R!R!L!L!RR!"
    assert candidate(target = "abcdefghijklmnopqrstuvwxyza") == "!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!R!R!R!R!LLLLD!UUUUU!"
    assert candidate(target = "question") == "RDDD!LD!UUUURRRR!LDDD!R!LUU!RD!L!"


