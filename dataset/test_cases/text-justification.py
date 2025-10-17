def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['Try', 'your', 'best', 'to', 'be', 'like', 'them', 'at', 'best', 'you', 'can', 'be', 'like', 'them.'],maxWidth = 20) == ['Try  your best to be', 'like  them  at  best', 'you   can   be  like', 'them.               ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Try', 'your', 'best', 'to', 'be', 'like', 'them', 'at', 'best', 'you', 'can', 'be', 'like', 'them.'],maxWidth = 20) == ['Try  your best to be', 'like  them  at  best', 'you   can   be  like', 'them.               ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'],maxWidth = 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'],maxWidth = 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'that', 'you', 'can', 'speak', 'to', 'none.'],maxWidth = 15) == ['Listen  to many', 'people  so that', 'you  can  speak', 'to none.       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'that', 'you', 'can', 'speak', 'to', 'none.'],maxWidth = 15) == ['Listen  to many', 'people  so that', 'you  can  speak', 'to none.       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'longwordhere', 'longwordhere', 'short'],maxWidth = 20) == ['short   longwordhere', 'longwordhere short  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'longwordhere', 'longwordhere', 'short'],maxWidth = 20) == ['short   longwordhere', 'longwordhere short  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a'],maxWidth = 2) == ['a ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a'],maxWidth = 2) == ['a ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'],maxWidth = 20) == ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'],maxWidth = 20) == ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'you', 'can', 'speak', 'to', 'all', 'people'],maxWidth = 7) == ['Listen ', 'to many', 'people ', 'so  you', 'can    ', 'speak  ', 'to  all', 'people ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'you', 'can', 'speak', 'to', 'all', 'people'],maxWidth = 7) == ['Listen ', 'to many', 'people ', 'so  you', 'can    ', 'speak  ', 'to  all', 'people ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'],maxWidth = 16) == ['This    is    an', 'example  of text', 'justification.  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'],maxWidth = 16) == ['This    is    an', 'example  of text', 'justification.  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Vestibulum', 'bibendum', 'porttitor', 'diam,'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing     elit.', 'Vestibulum  bibendum', 'porttitor diam,     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Vestibulum', 'bibendum', 'porttitor', 'diam,'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing     elit.', 'Vestibulum  bibendum', 'porttitor diam,     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Even', 'though', 'the', 'path', 'may', 'seem', 'long', 'and', 'difficult.'],maxWidth = 18) == ['Even   though  the', 'path may seem long', 'and difficult.    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Even', 'though', 'the', 'path', 'may', 'seem', 'long', 'and', 'difficult.'],maxWidth = 18) == ['Even   though  the', 'path may seem long', 'and difficult.    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly'],maxWidth = 50) == ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly'],maxWidth = 50) == ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Longer', 'words', 'and', 'evenlongerwords', 'are', 'here'],maxWidth = 25) == ['Longer      words     and', 'evenlongerwords are here ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Longer', 'words', 'and', 'evenlongerwords', 'are', 'here'],maxWidth = 25) == ['Longer      words     and', 'evenlongerwords are here ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs                ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs                ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['In', 'the', 'middle', 'of', 'the', 'night', 'the', 'old', 'owl', 'wisely', 'spread', 'his', 'wings'],maxWidth = 35) == ['In  the middle of the night the old', 'owl wisely spread his wings        ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['In', 'the', 'middle', 'of', 'the', 'night', 'the', 'old', 'owl', 'wisely', 'spread', 'his', 'wings'],maxWidth = 35) == ['In  the middle of the night the old', 'owl wisely spread his wings        ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Do', 'what', 'you', 'can', 'with', 'all', 'you', 'have,', 'wherever', 'you', 'are.'],maxWidth = 23) == ['Do  what  you  can with', 'all  you have, wherever', 'you are.               ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Do', 'what', 'you', 'can', 'with', 'all', 'you', 'have,', 'wherever', 'you', 'are.'],maxWidth = 23) == ['Do  what  you  can with', 'all  you have, wherever', 'you are.               ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Keep', 'your', 'face', 'always', 'toward', 'the', 'sunset.'],maxWidth = 21) == ['Keep your face always', 'toward the sunset.   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Keep', 'your', 'face', 'always', 'toward', 'the', 'sunset.'],maxWidth = 21) == ['Keep your face always', 'toward the sunset.   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o', 'p q r', 's t  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o', 'p q r', 's t  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Look', 'into', 'the', 'distance', 'where', 'you', 'can', 'see', 'the', 'futuristic', 'cityscape'],maxWidth = 35) == ['Look  into  the  distance where you', 'can see the futuristic cityscape   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Look', 'into', 'the', 'distance', 'where', 'you', 'can', 'see', 'the', 'futuristic', 'cityscape'],maxWidth = 35) == ['Look  into  the  distance where you', 'can see the futuristic cityscape   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Why', 'do', 'we', 'fall', 'ape', 'not', 'to', 'rise'],maxWidth = 8) == ['Why   do', 'we  fall', 'ape  not', 'to rise ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Why', 'do', 'we', 'fall', 'ape', 'not', 'to', 'rise'],maxWidth = 8) == ['Why   do', 'we  fall', 'ape  not', 'to rise ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 12) == ['To be or not', 'to  be  that', 'is       the', 'question    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 12) == ['To be or not', 'to  be  that', 'is       the', 'question    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 15) == ['Listen to many,', 'speak to a few.']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 15) == ['Listen to many,', 'speak to a few.']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Success', 'is', 'not', 'final,', 'failure', 'is', 'not', 'fatal:', 'It', 'is', 'the', 'courage', 'to', 'continue', 'that', 'counts.'],maxWidth = 25) == ['Success   is  not  final,', 'failure  is not fatal: It', 'is    the    courage   to', 'continue that counts.    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Success', 'is', 'not', 'final,', 'failure', 'is', 'not', 'fatal:', 'It', 'is', 'the', 'courage', 'to', 'continue', 'that', 'counts.'],maxWidth = 25) == ['Success   is  not  final,', 'failure  is not fatal: It', 'is    the    courage   to', 'continue that counts.    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not     to', 'be,that is', 'the       ', 'question: ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not     to', 'be,that is', 'the       ', 'question: ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Python', 'programming', 'is', 'fun,and', 'effective.'],maxWidth = 25) == ['Python   programming   is', 'fun,and effective.       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Python', 'programming', 'is', 'fun,and', 'effective.'],maxWidth = 25) == ['Python   programming   is', 'fun,and effective.       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Programming', 'is', 'not', 'about', 'what', 'you', 'know;', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.'],maxWidth = 25) == ['Programming  is not about', 'what   you  know;  it  is', 'about what you can figure', 'out.                     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Programming', 'is', 'not', 'about', 'what', 'you', 'know;', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.'],maxWidth = 25) == ['Programming  is not about', 'what   you  know;  it  is', 'about what you can figure', 'out.                     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'ring', 'to', 'rule', 'them', 'all,', 'One', 'ring', 'to', 'find', 'them.'],maxWidth = 18) == ['One  ring  to rule', 'them all, One ring', 'to find them.     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'ring', 'to', 'rule', 'them', 'all,', 'One', 'ring', 'to', 'find', 'them.'],maxWidth = 18) == ['One  ring  to rule', 'them all, One ring', 'to find them.     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 25) == ['To  be or not to be, that', 'is the question:         ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 25) == ['To  be or not to be, that', 'is the question:         ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Left', 'justified', 'line'],maxWidth = 30) == ['Left justified line           ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Left', 'justified', 'line'],maxWidth = 30) == ['Left justified line           ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['In', 'order', 'to', 'write', 'about', 'life,', 'one', 'must', 'live', 'it.'],maxWidth = 22) == ['In   order   to  write', 'about  life,  one must', 'live it.              ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['In', 'order', 'to', 'write', 'about', 'life,', 'one', 'must', 'live', 'it.'],maxWidth = 22) == ['In   order   to  write', 'about  life,  one must', 'live it.              ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Sometimes', 'the', 'wisest', 'course', 'requires', 'a', 'great', 'deal', 'of', 'courage'],maxWidth = 25) == ['Sometimes    the   wisest', 'course  requires  a great', 'deal of courage          ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Sometimes', 'the', 'wisest', 'course', 'requires', 'a', 'great', 'deal', 'of', 'courage'],maxWidth = 25) == ['Sometimes    the   wisest', 'course  requires  a great', 'deal of courage          ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'only', 'way', 'to', 'do', 'great', 'work', 'is', 'to', 'love', 'what', 'you', 'do.'],maxWidth = 25) == ['The  only way to do great', 'work  is to love what you', 'do.                      ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'only', 'way', 'to', 'do', 'great', 'work', 'is', 'to', 'love', 'what', 'you', 'do.'],maxWidth = 25) == ['The  only way to do great', 'work  is to love what you', 'do.                      ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood'],maxWidth = 20) == ['How  much wood would', 'a woodchuck chuck if', 'a   woodchuck  could', 'chuck wood          ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood'],maxWidth = 20) == ['How  much wood would', 'a woodchuck chuck if', 'a   woodchuck  could', 'chuck wood          ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Sometimes', 'you', 'have', 'to', 'run', 'before', 'you', 'can', 'walk'],maxWidth = 20) == ['Sometimes  you  have', 'to  run  before  you', 'can walk            ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Sometimes', 'you', 'have', 'to', 'run', 'before', 'you', 'can', 'walk'],maxWidth = 20) == ['Sometimes  you  have', 'to  run  before  you', 'can walk            ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['So', 'musing', 'on', 'the', 'marvel', 'of', 'this', 'theatre,'],maxWidth = 25) == ['So  musing  on the marvel', 'of this theatre,         ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['So', 'musing', 'on', 'the', 'marvel', 'of', 'this', 'theatre,'],maxWidth = 25) == ['So  musing  on the marvel', 'of this theatre,         ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Knowledge', 'is', 'a', 'treasure,', 'and', 'practice', 'is', 'the', 'key', 'to', 'mastering', 'it.'],maxWidth = 28) == ['Knowledge is a treasure, and', 'practice   is   the  key  to', 'mastering it.               ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Knowledge', 'is', 'a', 'treasure,', 'and', 'practice', 'is', 'the', 'key', 'to', 'mastering', 'it.'],maxWidth = 28) == ['Knowledge is a treasure, and', 'practice   is   the  key  to', 'mastering it.               ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Do', 'not', 'wait', 'to', 'strike', 'till', 'the', 'iron', 'is', 'hot;', 'but', 'make', 'it', 'hot', 'by', 'striking.'],maxWidth = 22) == ['Do  not wait to strike', 'till  the iron is hot;', 'but  make  it  hot  by', 'striking.             ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Do', 'not', 'wait', 'to', 'strike', 'till', 'the', 'iron', 'is', 'hot;', 'but', 'make', 'it', 'hot', 'by', 'striking.'],maxWidth = 22) == ['Do  not wait to strike', 'till  the iron is hot;', 'but  make  it  hot  by', 'striking.             ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Just', 'one', 'word'],maxWidth = 50) == ['Just one word                                     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Just', 'one', 'word'],maxWidth = 50) == ['Just one word                                     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog.  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog.  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'very', 'long', 'sentence', 'that', 'needs', 'to', 'be', 'formatted', 'correctly', 'with', 'various', 'spaces'],maxWidth = 10) == ['a     very', 'long      ', 'sentence  ', 'that needs', 'to      be', 'formatted ', 'correctly ', 'with      ', 'various   ', 'spaces    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'very', 'long', 'sentence', 'that', 'needs', 'to', 'be', 'formatted', 'correctly', 'with', 'various', 'spaces'],maxWidth = 10) == ['a     very', 'long      ', 'sentence  ', 'that needs', 'to      be', 'formatted ', 'correctly ', 'with      ', 'various   ', 'spaces    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 12) == ['Lorem  ipsum', 'dolor    sit', 'amet,       ', 'consectetur ', 'adipiscing  ', 'elit.       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 12) == ['Lorem  ipsum', 'dolor    sit', 'amet,       ', 'consectetur ', 'adipiscing  ', 'elit.       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['There', 'is', 'no', 'royal', 'road', 'to', 'learning.'],maxWidth = 20) == ['There  is  no  royal', 'road to learning.   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['There', 'is', 'no', 'royal', 'road', 'to', 'learning.'],maxWidth = 20) == ['There  is  no  royal', 'road to learning.   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['word'],maxWidth = 1) == ['word']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word'],maxWidth = 1) == ['word']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['A  quick  brown', 'fox  jumps over', 'the lazy dog.  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['A  quick  brown', 'fox  jumps over', 'the lazy dog.  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Short', 'words', 'only'],maxWidth = 5) == ['Short', 'words', 'only ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Short', 'words', 'only'],maxWidth = 5) == ['Short', 'words', 'only ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],maxWidth = 6) == ['a  b c', 'd  e f', 'g  h i', 'j  k l', 'm  n o', 'p  q r', 's  t u', 'v  w x', 'y z   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],maxWidth = 6) == ['a  b c', 'd  e f', 'g  h i', 'j  k l', 'm  n o', 'p  q r', 's  t u', 'v  w x', 'y z   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'best', 'way', 'to', 'predict', 'the', 'future', 'is', 'to', 'create', 'it.'],maxWidth = 20) == ['The   best   way  to', 'predict  the  future', 'is to create it.    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'best', 'way', 'to', 'predict', 'the', 'future', 'is', 'to', 'create', 'it.'],maxWidth = 20) == ['The   best   way  to', 'predict  the  future', 'is to create it.    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SingleWord'],maxWidth = 10) == ['SingleWord']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SingleWord'],maxWidth = 10) == ['SingleWord']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Failure', 'is', 'not', 'the', 'opposite', 'of', 'success;', 'it', 'is', 'part', 'of', 'success.'],maxWidth = 30) == ['Failure is not the opposite of', 'success;   it   is   part   of', 'success.                      ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Failure', 'is', 'not', 'the', 'opposite', 'of', 'success;', 'it', 'is', 'part', 'of', 'success.'],maxWidth = 30) == ['Failure is not the opposite of', 'success;   it   is   part   of', 'success.                      ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 6) == ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 6) == ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Equal', 'space', 'distribution'],maxWidth = 20) == ['Equal          space', 'distribution        ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Equal', 'space', 'distribution'],maxWidth = 20) == ['Equal          space', 'distribution        ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'brave', 'new', 'world,'],maxWidth = 30) == ['A brave new world,            ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'brave', 'new', 'world,'],maxWidth = 30) == ['A brave new world,            ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Listen', 'to', 'the', 'wind.', 'It', 'is', 'talking', 'to', 'you.'],maxWidth = 20) == ['Listen  to the wind.', 'It   is  talking  to', 'you.                ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Listen', 'to', 'the', 'wind.', 'It', 'is', 'talking', 'to', 'you.'],maxWidth = 20) == ['Listen  to the wind.', 'It   is  talking  to', 'you.                ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],maxWidth = 20) == ['A  B C D E F G H I J', 'K L M N O P Q R S T ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],maxWidth = 20) == ['A  B C D E F G H I J', 'K L M N O P Q R S T ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Let', 'us', 'hope', 'it', 'will', 'never', 'come', 'to', 'war'],maxWidth = 15) == ['Let  us hope it', 'will never come', 'to war         ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Let', 'us', 'hope', 'it', 'will', 'never', 'come', 'to', 'war'],maxWidth = 15) == ['Let  us hope it', 'will never come', 'to war         ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Equal', 'rights', 'for', 'all'],maxWidth = 10) == ['Equal     ', 'rights for', 'all       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Equal', 'rights', 'for', 'all'],maxWidth = 10) == ['Equal     ', 'rights for', 'all       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['all', 'the', 'world', 'is', 'a', 'stage', 'and', 'all', 'the', 'men', 'and', 'women', 'merely', 'players'],maxWidth = 25) == ['all  the world is a stage', 'and all the men and women', 'merely players           ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['all', 'the', 'world', 'is', 'a', 'stage', 'and', 'all', 'the', 'men', 'and', 'women', 'merely', 'players'],maxWidth = 25) == ['all  the world is a stage', 'and all the men and women', 'merely players           ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],maxWidth = 12) == ['One      two', 'three   four', 'five     six', 'seven  eight', 'nine ten    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],maxWidth = 12) == ['One      two', 'three   four', 'five     six', 'seven  eight', 'nine ten    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['It', 'is', 'during', 'our', 'darkest', 'hours', 'that', 'we', 'must', 'trust', 'in', 'the', 'light.'],maxWidth = 24) == ['It is during our darkest', 'hours that we must trust', 'in the light.           ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['It', 'is', 'during', 'our', 'darkest', 'hours', 'that', 'we', 'must', 'trust', 'in', 'the', 'light.'],maxWidth = 24) == ['It is during our darkest', 'hours that we must trust', 'in the light.           ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 25) == ['Once  upon  a  time  in a', 'land far far away        ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 25) == ['Once  upon  a  time  in a', 'land far far away        ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LongWord1234567890', 'Short', 'AnotherLongWord1234567', 'Tiny', 'Word'],maxWidth = 25) == ['LongWord1234567890  Short', 'AnotherLongWord1234567   ', 'Tiny Word                ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LongWord1234567890', 'Short', 'AnotherLongWord1234567', 'Tiny', 'Word'],maxWidth = 25) == ['LongWord1234567890  Short', 'AnotherLongWord1234567   ', 'Tiny Word                ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['We', 'are', 'now', 'a', 'great', 'nation', '', 'must', 'make', 'amends', 'that', 'we', 'have', 'wronged', 'visitors', 'from', 'other', 'lands'],maxWidth = 12) == ['We are now a', 'great nation', '  must  make', 'amends  that', 'we      have', 'wronged     ', 'visitors    ', 'from   other', 'lands       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['We', 'are', 'now', 'a', 'great', 'nation', '', 'must', 'make', 'amends', 'that', 'we', 'have', 'wronged', 'visitors', 'from', 'other', 'lands'],maxWidth = 12) == ['We are now a', 'great nation', '  must  make', 'amends  that', 'we      have', 'wronged     ', 'visitors    ', 'from   other', 'lands       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Sometimes', 'we', 'have', 'to', 'let', 'go', 'of', 'the', 'past,to', 'move', 'forward.'],maxWidth = 22) == ['Sometimes  we  have to', 'let  go of the past,to', 'move forward.         ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Sometimes', 'we', 'have', 'to', 'let', 'go', 'of', 'the', 'past,to', 'move', 'forward.'],maxWidth = 22) == ['Sometimes  we  have to', 'let  go of the past,to', 'move forward.         ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'journey', 'of', 'a', 'thousand', 'miles', 'begins', 'with', 'a', 'single', 'step'],maxWidth = 30) == ['A  journey of a thousand miles', 'begins with a single step     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'journey', 'of', 'a', 'thousand', 'miles', 'begins', 'with', 'a', 'single', 'step'],maxWidth = 30) == ['A  journey of a thousand miles', 'begins with a single step     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven'],maxWidth = 10) == ['One    two', 'three four', 'five   six', 'seven     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven'],maxWidth = 10) == ['One    two', 'three four', 'five   six', 'seven     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Short', 'words', 'only'],maxWidth = 10) == ['Short     ', 'words only']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Short', 'words', 'only'],maxWidth = 10) == ['Short     ', 'words only']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Life', 'is', 'either', 'a', 'great', 'adventure', 'or', 'nothing.'],maxWidth = 19) == ['Life  is  either  a', 'great  adventure or', 'nothing.           ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Life', 'is', 'either', 'a', 'great', 'adventure', 'or', 'nothing.'],maxWidth = 19) == ['Life  is  either  a', 'great  adventure or', 'nothing.           ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Justification', 'is', 'a', 'bit', 'tricky,', 'especially', 'when', 'the', 'words', 'are', 'short.', 'Here', 'we', 'go.'],maxWidth = 20) == ['Justification  is  a', 'bit          tricky,', 'especially  when the', 'words   are   short.', 'Here we go.         ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Justification', 'is', 'a', 'bit', 'tricky,', 'especially', 'when', 'the', 'words', 'are', 'short.', 'Here', 'we', 'go.'],maxWidth = 20) == ['Justification  is  a', 'bit          tricky,', 'especially  when the', 'words   are   short.', 'Here we go.         ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Here', 'is', 'a', 'longer', 'word', 'that', 'will', 'require', 'some', 'additional', 'spaces', 'to', 'justify'],maxWidth = 30) == ['Here  is  a  longer  word that', 'will  require  some additional', 'spaces to justify             ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Here', 'is', 'a', 'longer', 'word', 'that', 'will', 'require', 'some', 'additional', 'spaces', 'to', 'justify'],maxWidth = 30) == ['Here  is  a  longer  word that', 'will  require  some additional', 'spaces to justify             ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['It', 'is', 'a', 'truth', 'universally', 'acknowledged', 'that', 'a', 'single', 'man', 'in', 'possession', 'of', 'a', 'good', 'fortune'],maxWidth = 20) == ['It    is   a   truth', 'universally         ', 'acknowledged  that a', 'single     man    in', 'possession of a good', 'fortune             ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['It', 'is', 'a', 'truth', 'universally', 'acknowledged', 'that', 'a', 'single', 'man', 'in', 'possession', 'of', 'a', 'good', 'fortune'],maxWidth = 20) == ['It    is   a   truth', 'universally         ', 'acknowledged  that a', 'single     man    in', 'possession of a good', 'fortune             ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['If', 'you', 'set', 'your', 'goals', 'beyond', 'your', 'abilities,', 'you', 'will', 'never', 'achieve', 'them.'],maxWidth = 25) == ['If  you  set  your  goals', 'beyond   your  abilities,', 'you  will  never  achieve', 'them.                    ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['If', 'you', 'set', 'your', 'goals', 'beyond', 'your', 'abilities,', 'you', 'will', 'never', 'achieve', 'them.'],maxWidth = 25) == ['If  you  set  your  goals', 'beyond   your  abilities,', 'you  will  never  achieve', 'them.                    ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'world', 'is', 'a', 'book', 'and', 'those', 'who', 'do', 'not', 'travel', 'read', 'only', 'one', 'page.'],maxWidth = 25) == ['The  world  is a book and', 'those  who  do not travel', 'read only one page.      ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'world', 'is', 'a', 'book', 'and', 'those', 'who', 'do', 'not', 'travel', 'read', 'only', 'one', 'page.'],maxWidth = 25) == ['The  world  is a book and', 'those  who  do not travel', 'read only one page.      ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Every', 'great', 'developer', 'you', 'know', 'got', 'where', 'he', 'is', 'by', 'solving', 'problems', 'they', 'were', 'uncomfortable', 'solving', 'before.'],maxWidth = 40) == ['Every great developer you know got where', 'he  is  by  solving  problems  they were', 'uncomfortable solving before.           ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Every', 'great', 'developer', 'you', 'know', 'got', 'where', 'he', 'is', 'by', 'solving', 'problems', 'they', 'were', 'uncomfortable', 'solving', 'before.'],maxWidth = 40) == ['Every great developer you know got where', 'he  is  by  solving  problems  they were', 'uncomfortable solving before.           ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 25) == ['To  be  or not to be that', 'is the question          ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 25) == ['To  be  or not to be that', 'is the question          ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 22) == ['Once  upon a time in a', 'land far far away     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 22) == ['Once  upon a time in a', 'land far far away     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['I', 'have', 'a', 'dream'],maxWidth = 10) == ['I  have  a', 'dream     ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['I', 'have', 'a', 'dream'],maxWidth = 10) == ['I  have  a', 'dream     ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Programming', 'is', 'the', 'art', 'of', 'telling', 'another', 'person', 'what', 'to', 'do', 'in', 'a', 'language', 'that', 'the', 'other', 'person', 'can', 'understand'],maxWidth = 60) == ['Programming  is the art of telling another person what to do', 'in a language that the other person can understand          ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Programming', 'is', 'the', 'art', 'of', 'telling', 'another', 'person', 'what', 'to', 'do', 'in', 'a', 'language', 'that', 'the', 'other', 'person', 'can', 'understand'],maxWidth = 60) == ['Programming  is the art of telling another person what to do', 'in a language that the other person can understand          ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'small', 'step', 'for', 'man', 'one', 'giants', 'leap', 'for', 'mankind'],maxWidth = 30) == ['One  small  step  for  man one', 'giants leap for mankind       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'small', 'step', 'for', 'man', 'one', 'giants', 'leap', 'for', 'mankind'],maxWidth = 30) == ['One  small  step  for  man one', 'giants leap for mankind       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['This', 'is', 'a', 'test', 'for', 'justification', 'algorithm', 'to', 'see', 'how', 'it', 'works', 'with', 'longer', 'texts'],maxWidth = 25) == ['This   is   a   test  for', 'justification   algorithm', 'to  see how it works with', 'longer texts             ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['This', 'is', 'a', 'test', 'for', 'justification', 'algorithm', 'to', 'see', 'how', 'it', 'works', 'with', 'longer', 'texts'],maxWidth = 25) == ['This   is   a   test  for', 'justification   algorithm', 'to  see how it works with', 'longer texts             ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'word', 'in', 'each', 'line'],maxWidth = 1) == ['One', 'word', 'in', 'each', 'line']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'word', 'in', 'each', 'line'],maxWidth = 1) == ['One', 'word', 'in', 'each', 'line']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['All', 'the', 'world’s', 'a', 'stage,', 'And', 'all', 'the', 'men', 'and', 'women', 'merely', 'players.'],maxWidth = 20) == ['All  the  world’s  a', 'stage,  And  all the', 'men and women merely', 'players.            ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['All', 'the', 'world’s', 'a', 'stage,', 'And', 'all', 'the', 'men', 'and', 'women', 'merely', 'players.'],maxWidth = 20) == ['All  the  world’s  a', 'stage,  And  all the', 'men and women merely', 'players.            ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Continuous', 'learning', 'is', 'the', 'only', 'way', 'to', 'remain', 'relevant', 'in', 'the', 'fast-paced', 'world', 'of', 'technology.'],maxWidth = 40) == ['Continuous  learning  is the only way to', 'remain  relevant in the fast-paced world', 'of technology.                          ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Continuous', 'learning', 'is', 'the', 'only', 'way', 'to', 'remain', 'relevant', 'in', 'the', 'fast-paced', 'world', 'of', 'technology.'],maxWidth = 40) == ['Continuous  learning  is the only way to', 'remain  relevant in the fast-paced world', 'of technology.                          ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['The', 'best', 'time', 'of', 'our', 'lives', 'The', 'worst', 'time', 'of', 'our', 'lives'],maxWidth = 20) == ['The best time of our', 'lives The worst time', 'of our lives        ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['The', 'best', 'time', 'of', 'our', 'lives', 'The', 'worst', 'time', 'of', 'our', 'lives'],maxWidth = 20) == ['The best time of our', 'lives The worst time', 'of our lives        ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'simple', 'sentence.'],maxWidth = 20) == ['A simple sentence.  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'simple', 'sentence.'],maxWidth = 20) == ['A simple sentence.  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 20) == ['To  be  or not to be', 'that is the question']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 20) == ['To  be  or not to be', 'that is the question']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly'],maxWidth = 30) == ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly'],maxWidth = 30) == ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Pneumonoultramicroscopicsilicovolcanoconiosis'],maxWidth = 40) == ['Pneumonoultramicroscopicsilicovolcanoconiosis']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Pneumonoultramicroscopicsilicovolcanoconiosis'],maxWidth = 40) == ['Pneumonoultramicroscopicsilicovolcanoconiosis']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Believe', 'you', 'can', 'and', 'you', 're', 'halfway', 'there.'],maxWidth = 15) == ['Believe you can', 'and    you   re', 'halfway there. ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Believe', 'you', 'can', 'and', 'you', 're', 'halfway', 'there.'],maxWidth = 15) == ['Believe you can', 'and    you   re', 'halfway there. ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not to be,', 'that    is', 'the       ', 'question: ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not to be,', 'that    is', 'the       ', 'question: ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['This', 'is', 'an', 'example', 'of', 'a', 'longer', 'text', 'that', 'will', 'be', 'used', 'to', 'test', 'the', 'algorithm'],maxWidth = 15) == ['This    is   an', 'example   of  a', 'longer     text', 'that   will  be', 'used   to  test', 'the algorithm  ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['This', 'is', 'an', 'example', 'of', 'a', 'longer', 'text', 'that', 'will', 'be', 'used', 'to', 'test', 'the', 'algorithm'],maxWidth = 15) == ['This    is   an', 'example   of  a', 'longer     text', 'that   will  be', 'used   to  test', 'the algorithm  ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['One', 'Two', 'Three', 'Four', 'Five'],maxWidth = 10) == ['One    Two', 'Three Four', 'Five      ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['One', 'Two', 'Three', 'Four', 'Five'],maxWidth = 10) == ['One    Two', 'Three Four', 'Five      ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Many', 'spaces', 'should', 'go', 'here'],maxWidth = 23) == ['Many  spaces  should go', 'here                   ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Many', 'spaces', 'should', 'go', 'here'],maxWidth = 23) == ['Many  spaces  should go', 'here                   ']: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs.'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs.               ']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs.'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs.               ']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['Try', 'your', 'best', 'to', 'be', 'like', 'them', 'at', 'best', 'you', 'can', 'be', 'like', 'them.'],maxWidth = 20) == ['Try  your best to be', 'like  them  at  best', 'you   can   be  like', 'them.               ']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']
    assert candidate(words = ['What', 'must', 'be', 'acknowledgment', 'shall', 'be'],maxWidth = 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']
    assert candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'that', 'you', 'can', 'speak', 'to', 'none.'],maxWidth = 15) == ['Listen  to many', 'people  so that', 'you  can  speak', 'to none.       ']
    assert candidate(words = ['short', 'longwordhere', 'longwordhere', 'short'],maxWidth = 20) == ['short   longwordhere', 'longwordhere short  ']
    assert candidate(words = ['a'],maxWidth = 2) == ['a ']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],maxWidth = 3) == ['a b', 'c d', 'e  ']
    assert candidate(words = ['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'],maxWidth = 20) == ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
    assert candidate(words = ['Listen', 'to', 'many', 'people', 'so', 'you', 'can', 'speak', 'to', 'all', 'people'],maxWidth = 7) == ['Listen ', 'to many', 'people ', 'so  you', 'can    ', 'speak  ', 'to  all', 'people ']
    assert candidate(words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.'],maxWidth = 16) == ['This    is    an', 'example  of text', 'justification.  ']
    assert candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Vestibulum', 'bibendum', 'porttitor', 'diam,'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing     elit.', 'Vestibulum  bibendum', 'porttitor diam,     ']
    assert candidate(words = ['Even', 'though', 'the', 'path', 'may', 'seem', 'long', 'and', 'difficult.'],maxWidth = 18) == ['Even   though  the', 'path may seem long', 'and difficult.    ']
    assert candidate(words = ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly'],maxWidth = 50) == ['OneWordHereIsVeryLongIndeedAndItWillCauseSomeIssuesWithTheAlgorithmIfNotHandledProperly']
    assert candidate(words = ['Longer', 'words', 'and', 'evenlongerwords', 'are', 'here'],maxWidth = 25) == ['Longer      words     and', 'evenlongerwords are here ']
    assert candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs                ']
    assert candidate(words = ['In', 'the', 'middle', 'of', 'the', 'night', 'the', 'old', 'owl', 'wisely', 'spread', 'his', 'wings'],maxWidth = 35) == ['In  the middle of the night the old', 'owl wisely spread his wings        ']
    assert candidate(words = ['Do', 'what', 'you', 'can', 'with', 'all', 'you', 'have,', 'wherever', 'you', 'are.'],maxWidth = 23) == ['Do  what  you  can with', 'all  you have, wherever', 'you are.               ']
    assert candidate(words = ['Keep', 'your', 'face', 'always', 'toward', 'the', 'sunset.'],maxWidth = 21) == ['Keep your face always', 'toward the sunset.   ']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o', 'p q r', 's t  ']
    assert candidate(words = ['Look', 'into', 'the', 'distance', 'where', 'you', 'can', 'see', 'the', 'futuristic', 'cityscape'],maxWidth = 35) == ['Look  into  the  distance where you', 'can see the futuristic cityscape   ']
    assert candidate(words = ['Why', 'do', 'we', 'fall', 'ape', 'not', 'to', 'rise'],maxWidth = 8) == ['Why   do', 'we  fall', 'ape  not', 'to rise ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 12) == ['To be or not', 'to  be  that', 'is       the', 'question    ']
    assert candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 15) == ['Listen to many,', 'speak to a few.']
    assert candidate(words = ['Success', 'is', 'not', 'final,', 'failure', 'is', 'not', 'fatal:', 'It', 'is', 'the', 'courage', 'to', 'continue', 'that', 'counts.'],maxWidth = 25) == ['Success   is  not  final,', 'failure  is not fatal: It', 'is    the    courage   to', 'continue that counts.    ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not     to', 'be,that is', 'the       ', 'question: ']
    assert candidate(words = ['Python', 'programming', 'is', 'fun,and', 'effective.'],maxWidth = 25) == ['Python   programming   is', 'fun,and effective.       ']
    assert candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J    ']
    assert candidate(words = ['Programming', 'is', 'not', 'about', 'what', 'you', 'know;', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.'],maxWidth = 25) == ['Programming  is not about', 'what   you  know;  it  is', 'about what you can figure', 'out.                     ']
    assert candidate(words = ['One', 'ring', 'to', 'rule', 'them', 'all,', 'One', 'ring', 'to', 'find', 'them.'],maxWidth = 18) == ['One  ring  to rule', 'them all, One ring', 'to find them.     ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 25) == ['To  be or not to be, that', 'is the question:         ']
    assert candidate(words = ['Left', 'justified', 'line'],maxWidth = 30) == ['Left justified line           ']
    assert candidate(words = ['In', 'order', 'to', 'write', 'about', 'life,', 'one', 'must', 'live', 'it.'],maxWidth = 22) == ['In   order   to  write', 'about  life,  one must', 'live it.              ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']
    assert candidate(words = ['Sometimes', 'the', 'wisest', 'course', 'requires', 'a', 'great', 'deal', 'of', 'courage'],maxWidth = 25) == ['Sometimes    the   wisest', 'course  requires  a great', 'deal of courage          ']
    assert candidate(words = ['The', 'only', 'way', 'to', 'do', 'great', 'work', 'is', 'to', 'love', 'what', 'you', 'do.'],maxWidth = 25) == ['The  only way to do great', 'work  is to love what you', 'do.                      ']
    assert candidate(words = ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood'],maxWidth = 20) == ['How  much wood would', 'a woodchuck chuck if', 'a   woodchuck  could', 'chuck wood          ']
    assert candidate(words = ['Sometimes', 'you', 'have', 'to', 'run', 'before', 'you', 'can', 'walk'],maxWidth = 20) == ['Sometimes  you  have', 'to  run  before  you', 'can walk            ']
    assert candidate(words = ['So', 'musing', 'on', 'the', 'marvel', 'of', 'this', 'theatre,'],maxWidth = 25) == ['So  musing  on the marvel', 'of this theatre,         ']
    assert candidate(words = ['Knowledge', 'is', 'a', 'treasure,', 'and', 'practice', 'is', 'the', 'key', 'to', 'mastering', 'it.'],maxWidth = 28) == ['Knowledge is a treasure, and', 'practice   is   the  key  to', 'mastering it.               ']
    assert candidate(words = ['Do', 'not', 'wait', 'to', 'strike', 'till', 'the', 'iron', 'is', 'hot;', 'but', 'make', 'it', 'hot', 'by', 'striking.'],maxWidth = 22) == ['Do  not wait to strike', 'till  the iron is hot;', 'but  make  it  hot  by', 'striking.             ']
    assert candidate(words = ['Just', 'one', 'word'],maxWidth = 50) == ['Just one word                                     ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog.  ']
    assert candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit     ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 15) == ['The quick brown', 'fox  jumps over', 'the lazy dog   ']
    assert candidate(words = ['a', 'very', 'long', 'sentence', 'that', 'needs', 'to', 'be', 'formatted', 'correctly', 'with', 'various', 'spaces'],maxWidth = 10) == ['a     very', 'long      ', 'sentence  ', 'that needs', 'to      be', 'formatted ', 'correctly ', 'with      ', 'various   ', 'spaces    ']
    assert candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 12) == ['Lorem  ipsum', 'dolor    sit', 'amet,       ', 'consectetur ', 'adipiscing  ', 'elit.       ']
    assert candidate(words = ['There', 'is', 'no', 'royal', 'road', 'to', 'learning.'],maxWidth = 20) == ['There  is  no  royal', 'road to learning.   ']
    assert candidate(words = ['word'],maxWidth = 1) == ['word']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],maxWidth = 5) == ['a b c', 'd e f', 'g h i', 'j k l', 'm n o']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 15) == ['To be or not to', 'be  that is the', 'question       ']
    assert candidate(words = ['A', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'],maxWidth = 15) == ['A  quick  brown', 'fox  jumps over', 'the lazy dog.  ']
    assert candidate(words = ['Short', 'words', 'only'],maxWidth = 5) == ['Short', 'words', 'only ']
    assert candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']
    assert candidate(words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],maxWidth = 6) == ['a  b c', 'd  e f', 'g  h i', 'j  k l', 'm  n o', 'p  q r', 's  t u', 'v  w x', 'y z   ']
    assert candidate(words = ['The', 'best', 'way', 'to', 'predict', 'the', 'future', 'is', 'to', 'create', 'it.'],maxWidth = 20) == ['The   best   way  to', 'predict  the  future', 'is to create it.    ']
    assert candidate(words = ['SingleWord'],maxWidth = 10) == ['SingleWord']
    assert candidate(words = ['Failure', 'is', 'not', 'the', 'opposite', 'of', 'success;', 'it', 'is', 'part', 'of', 'success.'],maxWidth = 30) == ['Failure is not the opposite of', 'success;   it   is   part   of', 'success.                      ']
    assert candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']
    assert candidate(words = ['Listen', 'to', 'many,', 'speak', 'to', 'a', 'few.'],maxWidth = 6) == ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
    assert candidate(words = ['Equal', 'space', 'distribution'],maxWidth = 20) == ['Equal          space', 'distribution        ']
    assert candidate(words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.'],maxWidth = 20) == ['Lorem   ipsum  dolor', 'sit            amet,', 'consectetur         ', 'adipiscing elit.    ']
    assert candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],maxWidth = 5) == ['A B C', 'D E F', 'G H I', 'J K L', 'M N O', 'P Q R', 'S T U', 'V W X', 'Y Z  ']
    assert candidate(words = ['A', 'brave', 'new', 'world,'],maxWidth = 30) == ['A brave new world,            ']
    assert candidate(words = ['Listen', 'to', 'the', 'wind.', 'It', 'is', 'talking', 'to', 'you.'],maxWidth = 20) == ['Listen  to the wind.', 'It   is  talking  to', 'you.                ']
    assert candidate(words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],maxWidth = 20) == ['A  B C D E F G H I J', 'K L M N O P Q R S T ']
    assert candidate(words = ['Let', 'us', 'hope', 'it', 'will', 'never', 'come', 'to', 'war'],maxWidth = 15) == ['Let  us hope it', 'will never come', 'to war         ']
    assert candidate(words = ['Equal', 'rights', 'for', 'all'],maxWidth = 10) == ['Equal     ', 'rights for', 'all       ']
    assert candidate(words = ['all', 'the', 'world', 'is', 'a', 'stage', 'and', 'all', 'the', 'men', 'and', 'women', 'merely', 'players'],maxWidth = 25) == ['all  the world is a stage', 'and all the men and women', 'merely players           ']
    assert candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],maxWidth = 12) == ['One      two', 'three   four', 'five     six', 'seven  eight', 'nine ten    ']
    assert candidate(words = ['It', 'is', 'during', 'our', 'darkest', 'hours', 'that', 'we', 'must', 'trust', 'in', 'the', 'light.'],maxWidth = 24) == ['It is during our darkest', 'hours that we must trust', 'in the light.           ']
    assert candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 25) == ['Once  upon  a  time  in a', 'land far far away        ']
    assert candidate(words = ['LongWord1234567890', 'Short', 'AnotherLongWord1234567', 'Tiny', 'Word'],maxWidth = 25) == ['LongWord1234567890  Short', 'AnotherLongWord1234567   ', 'Tiny Word                ']
    assert candidate(words = ['We', 'are', 'now', 'a', 'great', 'nation', '', 'must', 'make', 'amends', 'that', 'we', 'have', 'wronged', 'visitors', 'from', 'other', 'lands'],maxWidth = 12) == ['We are now a', 'great nation', '  must  make', 'amends  that', 'we      have', 'wronged     ', 'visitors    ', 'from   other', 'lands       ']
    assert candidate(words = ['Sometimes', 'we', 'have', 'to', 'let', 'go', 'of', 'the', 'past,to', 'move', 'forward.'],maxWidth = 22) == ['Sometimes  we  have to', 'let  go of the past,to', 'move forward.         ']
    assert candidate(words = ['A', 'journey', 'of', 'a', 'thousand', 'miles', 'begins', 'with', 'a', 'single', 'step'],maxWidth = 30) == ['A  journey of a thousand miles', 'begins with a single step     ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']
    assert candidate(words = ['One', 'two', 'three', 'four', 'five', 'six', 'seven'],maxWidth = 10) == ['One    two', 'three four', 'five   six', 'seven     ']
    assert candidate(words = ['Short', 'words', 'only'],maxWidth = 10) == ['Short     ', 'words only']
    assert candidate(words = ['Life', 'is', 'either', 'a', 'great', 'adventure', 'or', 'nothing.'],maxWidth = 19) == ['Life  is  either  a', 'great  adventure or', 'nothing.           ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 20) == ['The  quick brown fox', 'jumps  over the lazy', 'dog                 ']
    assert candidate(words = ['Justification', 'is', 'a', 'bit', 'tricky,', 'especially', 'when', 'the', 'words', 'are', 'short.', 'Here', 'we', 'go.'],maxWidth = 20) == ['Justification  is  a', 'bit          tricky,', 'especially  when the', 'words   are   short.', 'Here we go.         ']
    assert candidate(words = ['Here', 'is', 'a', 'longer', 'word', 'that', 'will', 'require', 'some', 'additional', 'spaces', 'to', 'justify'],maxWidth = 30) == ['Here  is  a  longer  word that', 'will  require  some additional', 'spaces to justify             ']
    assert candidate(words = ['It', 'is', 'a', 'truth', 'universally', 'acknowledged', 'that', 'a', 'single', 'man', 'in', 'possession', 'of', 'a', 'good', 'fortune'],maxWidth = 20) == ['It    is   a   truth', 'universally         ', 'acknowledged  that a', 'single     man    in', 'possession of a good', 'fortune             ']
    assert candidate(words = ['If', 'you', 'set', 'your', 'goals', 'beyond', 'your', 'abilities,', 'you', 'will', 'never', 'achieve', 'them.'],maxWidth = 25) == ['If  you  set  your  goals', 'beyond   your  abilities,', 'you  will  never  achieve', 'them.                    ']
    assert candidate(words = ['The', 'world', 'is', 'a', 'book', 'and', 'those', 'who', 'do', 'not', 'travel', 'read', 'only', 'one', 'page.'],maxWidth = 25) == ['The  world  is a book and', 'those  who  do not travel', 'read only one page.      ']
    assert candidate(words = ['Every', 'great', 'developer', 'you', 'know', 'got', 'where', 'he', 'is', 'by', 'solving', 'problems', 'they', 'were', 'uncomfortable', 'solving', 'before.'],maxWidth = 40) == ['Every great developer you know got where', 'he  is  by  solving  problems  they were', 'uncomfortable solving before.           ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 25) == ['To  be  or not to be that', 'is the question          ']
    assert candidate(words = ['Once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],maxWidth = 22) == ['Once  upon a time in a', 'land far far away     ']
    assert candidate(words = ['I', 'have', 'a', 'dream'],maxWidth = 10) == ['I  have  a', 'dream     ']
    assert candidate(words = ['Programming', 'is', 'the', 'art', 'of', 'telling', 'another', 'person', 'what', 'to', 'do', 'in', 'a', 'language', 'that', 'the', 'other', 'person', 'can', 'understand'],maxWidth = 60) == ['Programming  is the art of telling another person what to do', 'in a language that the other person can understand          ']
    assert candidate(words = ['One', 'small', 'step', 'for', 'man', 'one', 'giants', 'leap', 'for', 'mankind'],maxWidth = 30) == ['One  small  step  for  man one', 'giants leap for mankind       ']
    assert candidate(words = ['This', 'is', 'a', 'test', 'for', 'justification', 'algorithm', 'to', 'see', 'how', 'it', 'works', 'with', 'longer', 'texts'],maxWidth = 25) == ['This   is   a   test  for', 'justification   algorithm', 'to  see how it works with', 'longer texts             ']
    assert candidate(words = ['One', 'word', 'in', 'each', 'line'],maxWidth = 1) == ['One', 'word', 'in', 'each', 'line']
    assert candidate(words = ['All', 'the', 'world’s', 'a', 'stage,', 'And', 'all', 'the', 'men', 'and', 'women', 'merely', 'players.'],maxWidth = 20) == ['All  the  world’s  a', 'stage,  And  all the', 'men and women merely', 'players.            ']
    assert candidate(words = ['Continuous', 'learning', 'is', 'the', 'only', 'way', 'to', 'remain', 'relevant', 'in', 'the', 'fast-paced', 'world', 'of', 'technology.'],maxWidth = 40) == ['Continuous  learning  is the only way to', 'remain  relevant in the fast-paced world', 'of technology.                          ']
    assert candidate(words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],maxWidth = 10) == ['The  quick', 'brown  fox', 'jumps over', 'the   lazy', 'dog       ']
    assert candidate(words = ['The', 'best', 'time', 'of', 'our', 'lives', 'The', 'worst', 'time', 'of', 'our', 'lives'],maxWidth = 20) == ['The best time of our', 'lives The worst time', 'of our lives        ']
    assert candidate(words = ['A', 'simple', 'sentence.'],maxWidth = 20) == ['A simple sentence.  ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be', 'that', 'is', 'the', 'question'],maxWidth = 20) == ['To  be  or not to be', 'that is the question']
    assert candidate(words = ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly'],maxWidth = 30) == ['SingleLongWordThatExceedsTheMaxWidthAndNeedsToBeHandledProperly']
    assert candidate(words = ['Pneumonoultramicroscopicsilicovolcanoconiosis'],maxWidth = 40) == ['Pneumonoultramicroscopicsilicovolcanoconiosis']
    assert candidate(words = ['Believe', 'you', 'can', 'and', 'you', 're', 'halfway', 'there.'],maxWidth = 15) == ['Believe you can', 'and    you   re', 'halfway there. ']
    assert candidate(words = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:'],maxWidth = 10) == ['To  be  or', 'not to be,', 'that    is', 'the       ', 'question: ']
    assert candidate(words = ['This', 'is', 'an', 'example', 'of', 'a', 'longer', 'text', 'that', 'will', 'be', 'used', 'to', 'test', 'the', 'algorithm'],maxWidth = 15) == ['This    is   an', 'example   of  a', 'longer     text', 'that   will  be', 'used   to  test', 'the algorithm  ']
    assert candidate(words = ['One', 'Two', 'Three', 'Four', 'Five'],maxWidth = 10) == ['One    Two', 'Three Four', 'Five      ']
    assert candidate(words = ['Many', 'spaces', 'should', 'go', 'here'],maxWidth = 23) == ['Many  spaces  should go', 'here                   ']
    assert candidate(words = ['Pack', 'my', 'box', 'with', 'five', 'dozen', 'liquor', 'jugs.'],maxWidth = 20) == ['Pack   my  box  with', 'five   dozen  liquor', 'jugs.               ']


