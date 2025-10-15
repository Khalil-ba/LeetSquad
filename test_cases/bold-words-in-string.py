def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = [],s = "nothingtoboldhere") == "nothingtoboldhere"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = [],s = "nothingtoboldhere") == "nothingtoboldhere": {e}')
    
    total += 1
    try:
        result = candidate(words = [],s = "abcdefg") == "abcdefg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = [],s = "abcdefg") == "abcdefg": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa'],s = "aaaaa") == "<b>aaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa'],s = "aaaaa") == "<b>aaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc'],s = "aabcd") == "a<b>abc</b>d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc'],s = "aabcd") == "a<b>abc</b>d": {e}')
    
    total += 1
    try:
        result = candidate(words = ['is', 'in'],s = "this is an interesting string") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g str<b>in</b>g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['is', 'in'],s = "this is an interesting string") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g str<b>in</b>g": {e}')
    
    total += 1
    try:
        result = candidate(words = ['foo', 'bar'],s = "foobarbaz") == "<b>foobar</b>baz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['foo', 'bar'],s = "foobarbaz") == "<b>foobar</b>baz": {e}')
    
    total += 1
    try:
        result = candidate(words = ['z'],s = "zzz") == "<b>zzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['z'],s = "zzz") == "<b>zzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "abcabc") == "<b>abcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "abcabc") == "<b>abcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['z', 'zz'],s = "zzz") == "<b>zzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['z', 'zz'],s = "zzz") == "<b>zzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['x', 'y', 'z'],s = "xyzxyz") == "<b>xyzxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['x', 'y', 'z'],s = "xyzxyz") == "<b>xyzxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'cb'],s = "aabcd") == "a<b>ab</b>cd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'cb'],s = "aabcd") == "a<b>ab</b>cd": {e}')
    
    total += 1
    try:
        result = candidate(words = ['test'],s = "this is a test string") == "this is a <b>test</b> string"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test'],s = "this is a test string") == "this is a <b>test</b> string": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog'],s = "cat and dog are friends, but catdog is a special creature") == "<b>cat</b> and <b>dog</b> are friends, but <b>catdog</b> is a special creature"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog'],s = "cat and dog are friends, but catdog is a special creature") == "<b>cat</b> and <b>dog</b> are friends, but <b>catdog</b> is a special creature": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyyxxyyx") == "<b>xyyxxyyx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyyxxyyx") == "<b>xyyxxyyx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothreeonethree") == "<b>onetwothreeonethree</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothreeonethree") == "<b>onetwothreeonethree</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['x', 'xx', 'xxx', 'xxxx'],s = "xxxxxxx") == "<b>xxxxxxx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['x', 'xx', 'xxx', 'xxxx'],s = "xxxxxxx") == "<b>xxxxxxx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothreefouronetwothree") == "<b>onetwothree</b>four<b>onetwothree</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothreefouronetwothree") == "<b>onetwothree</b>four<b>onetwothree</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def'],s = "abcdefgabcdef") == "<b>abcdef</b>g<b>abcdef</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def'],s = "abcdefgabcdef") == "<b>abcdef</b>g<b>abcdef</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing'],s = "this is a test testing string") == "this is a <b>test</b> <b>testing</b> string"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing'],s = "this is a test testing string") == "this is a <b>test</b> <b>testing</b> string": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['is', 'island', 'sand'],s = "this is an island surrounded by sand") == "th<b>is</b> <b>is</b> an <b>island</b> surrounded by <b>sand</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['is', 'island', 'sand'],s = "this is an island surrounded by sand") == "th<b>is</b> <b>is</b> an <b>island</b> surrounded by <b>sand</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['start', 'middle', 'end'],s = "startmiddleend") == "<b>startmiddleend</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['start', 'middle', 'end'],s = "startmiddleend") == "<b>startmiddleend</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['zz', 'z'],s = "zzzzzzzzz") == "<b>zzzzzzzzz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['zz', 'z'],s = "zzzzzzzzz") == "<b>zzzzzzzzz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lap'],s = "overlaplap") == "<b>overlaplap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lap'],s = "overlaplap") == "<b>overlaplap</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lap', 'ap'],s = "overlaplap") == "<b>overlaplap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lap', 'ap'],s = "overlaplap") == "<b>overlaplap</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lapping'],s = "overlappinglapping") == "<b>overlappinglapping</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lapping'],s = "overlappinglapping") == "<b>overlappinglapping</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same'],s = "samesamesame") == "<b>samesamesame</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same'],s = "samesamesame") == "<b>samesamesame</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['is', 'in'],s = "this is an interesting situation") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g situation"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['is', 'in'],s = "this is an interesting situation") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g situation": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == "<b>abcdefghi</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == "<b>abcdefghi</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique', 'words'],s = "uniquewordswordsunique") == "<b>uniquewordswordsunique</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique', 'words'],s = "uniquewordswordsunique") == "<b>uniquewordswordsunique</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['in', 'inception', 'ception'],s = "inceptionception") == "<b>inceptionception</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['in', 'inception', 'ception'],s = "inceptionception") == "<b>inceptionception</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyxxyxyyx") == "<b>xyxxyxyyx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyxxyxyyx") == "<b>xyxxyxyyx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd'],s = "abcbcd") == "<b>abcbcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd'],s = "abcbcd") == "<b>abcbcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "hello world, hello universe") == "<b>hello</b> <b>world</b>, <b>hello</b> universe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "hello world, hello universe") == "<b>hello</b> <b>world</b>, <b>hello</b> universe": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat', 'rat'],s = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat', 'rat'],s = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lap', 'lapel'],s = "overlaplapel") == "<b>overlaplapel</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lap', 'lapel'],s = "overlaplapel") == "<b>overlaplapel</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "hello world! hello universe") == "<b>hello</b> <b>world</b>! <b>hello</b> universe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "hello world! hello universe") == "<b>hello</b> <b>world</b>! <b>hello</b> universe": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc', 'cd'],s = "abcbcd") == "<b>abcbcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc', 'cd'],s = "abcbcd") == "<b>abcbcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['bold', 'word', 'words'],s = "boldwords") == "<b>boldwords</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['bold', 'word', 'words'],s = "boldwords") == "<b>boldwords</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['banana', 'anana'],s = "bananabanana") == "<b>bananabanana</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['banana', 'anana'],s = "bananabanana") == "<b>bananabanana</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "hello world hello") == "<b>hello</b> <b>world</b> <b>hello</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "hello world hello") == "<b>hello</b> <b>world</b> <b>hello</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'abcd', 'abcde'],s = "abcde") == "<b>abcde</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'abcd', 'abcde'],s = "abcde") == "<b>abcde</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bbb', 'ccc'],s = "aaabbbccc") == "<b>aaabbbccc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bbb', 'ccc'],s = "aaabbbccc") == "<b>aaabbbccc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "edcbaedcba") == "<b>edcbaedcba</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "edcbaedcba") == "<b>edcbaedcba</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['nested', 'nest', 'set'],s = "nestedset") == "<b>nestedset</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['nested', 'nest', 'set'],s = "nestedset") == "<b>nestedset</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abcde', 'bcdef', 'cdefg'],s = "abcdefghij") == "<b>abcdefg</b>hij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abcde', 'bcdef', 'cdefg'],s = "abcdefghij") == "<b>abcdefg</b>hij": {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeated', 'repeat', 'rep'],s = "repeated repeated repeat reprepeated") == "<b>repeated</b> <b>repeated</b> <b>repeat</b> <b>reprepeated</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeated', 'repeat', 'rep'],s = "repeated repeated repeat reprepeated") == "<b>repeated</b> <b>repeated</b> <b>repeat</b> <b>reprepeated</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lapping', 'overlappping'],s = "overlappingslappinglappingpings") == "<b>overlapping</b>s<b>lappinglapping</b>pings"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lapping', 'overlappping'],s = "overlappingslappinglappingpings") == "<b>overlapping</b>s<b>lappinglapping</b>pings": {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'longword', 'tiny'],s = "shortlongwordtinyshort") == "<b>shortlongwordtinyshort</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'longword', 'tiny'],s = "shortlongwordtinyshort") == "<b>shortlongwordtinyshort</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothreeone") == "<b>onetwothreeone</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothreeone") == "<b>onetwothreeone</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'rat'],s = "thecatandthedogandtherat") == "the<b>cat</b>andthe<b>dog</b>andthe<b>rat</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'rat'],s = "thecatandthedogandtherat") == "the<b>cat</b>andthe<b>dog</b>andthe<b>rat</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['quick', 'brown', 'fox'],s = "the quick brown fox jumps over the lazy dog") == "the <b>quick</b> <b>brown</b> <b>fox</b> jumps over the lazy dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quick', 'brown', 'fox'],s = "the quick brown fox jumps over the lazy dog") == "the <b>quick</b> <b>brown</b> <b>fox</b> jumps over the lazy dog": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyyxxy") == "<b>xyyxxy</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyyxxy") == "<b>xyyxxy</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'bird'],s = "thecatandthedogandthebird") == "the<b>cat</b>andthe<b>dog</b>andthe<b>bird</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'bird'],s = "thecatandthedogandthebird") == "the<b>cat</b>andthe<b>dog</b>andthe<b>bird</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'app', 'ple'],s = "appleapples") == "<b>appleapple</b>s"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'app', 'ple'],s = "appleapples") == "<b>appleapple</b>s": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aab', 'abc'],s = "aaaabacababc") == "<b>aaaab</b>acab<b>abc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aab', 'abc'],s = "aaaabacababc") == "<b>aaaab</b>acab<b>abc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['in', 'inside', 'side'],s = "insideinsideinside") == "<b>insideinsideinside</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['in', 'inside', 'side'],s = "insideinsideinside") == "<b>insideinsideinside</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['foo', 'bar', 'baz'],s = "foobarbazfoobarbaz") == "<b>foobarbazfoobarbaz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['foo', 'bar', 'baz'],s = "foobarbazfoobarbaz") == "<b>foobarbazfoobarbaz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['mississippi', 'issi', 'issipp'],s = "mississippiississippi") == "<b>mississippiississipp</b>i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['mississippi', 'issi', 'issipp'],s = "mississippiississippi") == "<b>mississippiississipp</b>i": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeat', 'peat', 'eat'],s = "repeatpeatpeatpeat") == "<b>repeatpeatpeatpeat</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeat', 'peat', 'eat'],s = "repeatpeatpeatpeat") == "<b>repeatpeatpeatpeat</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'longerword'],s = "shortlongerwordshort") == "<b>shortlongerwordshort</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'longerword'],s = "shortlongerwordshort") == "<b>shortlongerwordshort</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'bat'],s = "the cattle were battling the bat") == "the <b>cat</b>tle were <b>bat</b>tling the <b>bat</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'bat'],s = "the cattle were battling the bat") == "the <b>cat</b>tle were <b>bat</b>tling the <b>bat</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['shorter', 'short', 'sho', 'sh'],s = "shortershortershosh") == "<b>shortershortershosh</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['shorter', 'short', 'sho', 'sh'],s = "shortershortershosh") == "<b>shortershortershosh</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'hell', 'he', 'h'],s = "hellohelhekhhh") == "<b>hellohe</b>l<b>he</b>k<b>hhh</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'hell', 'he', 'h'],s = "hellohelhekhhh") == "<b>hellohe</b>l<b>he</b>k<b>hhh</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothree") == "<b>onetwothree</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothree") == "<b>onetwothree</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'longerword', 'tiny'],s = "thisisalongerword") == "thisisa<b>longerword</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'longerword', 'tiny'],s = "thisisalongerword") == "thisisa<b>longerword</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lapping'],s = "overlapping") == "<b>overlapping</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lapping'],s = "overlapping") == "<b>overlapping</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['substring', 'string'],s = "this is a substring string") == "this is a <b>substring</b> <b>string</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['substring', 'string'],s = "this is a substring string") == "this is a <b>substring</b> <b>string</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['jump', 'jumps'],s = "hejumpsjumpproperly") == "he<b>jumpsjump</b>properly"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['jump', 'jumps'],s = "hejumpsjumpproperly") == "he<b>jumpsjump</b>properly": {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'world', 'wor'],s = "worldwide world of words") == "<b>world</b>wide <b>world</b> of <b>word</b>s"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'world', 'wor'],s = "worldwide world of words") == "<b>world</b>wide <b>world</b> of <b>word</b>s": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry'],s = "applebananaapplecherry") == "<b>applebananaapplecherry</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry'],s = "applebananaapplecherry") == "<b>applebananaapplecherry</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['python', 'java', 'c'],s = "pythonjavaandcsareprogramminglanguages") == "<b>pythonjava</b>and<b>c</b>sareprogramminglanguages"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['python', 'java', 'c'],s = "pythonjavaandcsareprogramminglanguages") == "<b>pythonjava</b>and<b>c</b>sareprogramminglanguages": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyxxyyxxyx") == "<b>xyxxyyxxyx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyxxyyxxyx") == "<b>xyxxyyxxyx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaaa") == "<b>aaaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaaa") == "<b>aaaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'banana', 'cherry'],s = "applebananacherry") == "<b>applebananacherry</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'banana', 'cherry'],s = "applebananacherry") == "<b>applebananacherry</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "hello world! welcome to the hello world") == "<b>hello</b> <b>world</b>! welcome to the <b>hello</b> <b>world</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "hello world! welcome to the hello world") == "<b>hello</b> <b>world</b>! welcome to the <b>hello</b> <b>world</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['one', 'two', 'three'],s = "onetwothreeonetwothree") == "<b>onetwothreeonetwothree</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['one', 'two', 'three'],s = "onetwothreeonetwothree") == "<b>onetwothreeonetwothree</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested'],s = "testtestingtested") == "<b>testtestingtested</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested'],s = "testtestingtested") == "<b>testtestingtested</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'pineapple'],s = "pineappleapple") == "<b>pineappleapple</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'pineapple'],s = "pineappleapple") == "<b>pineappleapple</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'bird'],s = "dogcatbirdbirdcat") == "<b>dogcatbirdbirdcat</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'bird'],s = "dogcatbirdbirdcat") == "<b>dogcatbirdbirdcat</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['example', 'sample', 'text'],s = "example sample text") == "<b>example</b> <b>sample</b> <b>text</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['example', 'sample', 'text'],s = "example sample text") == "<b>example</b> <b>sample</b> <b>text</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde'],s = "abcdexyzcde") == "<b>abcde</b>xyz<b>cde</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde'],s = "abcdexyzcde") == "<b>abcde</b>xyz<b>cde</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'abc', 'abcd'],s = "abcdabcab") == "<b>abcdabcab</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'abc', 'abcd'],s = "abcdabcab") == "<b>abcdabcab</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyxxyxyxyxxyyx") == "<b>xyxxyxyxyxxyyx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyxxyxyxyxxyyx") == "<b>xyxxyxyxyxxyyx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyxyxyyxxyxxy") == "<b>xyxyxyyxxyxxy</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyxyxyyxxyxxy") == "<b>xyxyxyyxxyxxy</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaa") == "<b>aaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaa") == "<b>aaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd'],s = "abcdabcdabcd") == "<b>abcdabcdabcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd'],s = "abcdabcdabcd") == "<b>abcdabcdabcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeat', 'eat', 'peat'],s = "repeatpeatpeat") == "<b>repeatpeatpeat</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeat', 'eat', 'peat'],s = "repeatpeatpeat") == "<b>repeatpeatpeat</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['jump', 'jumps', 'jumping'],s = "he was jumping over the jumps while he jump") == "he was <b>jumping</b> over the <b>jumps</b> while he <b>jump</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['jump', 'jumps', 'jumping'],s = "he was jumping over the jumps while he jump") == "he was <b>jumping</b> over the <b>jumps</b> while he <b>jump</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bbbb', 'cc'],s = "aaabbbbbc") == "<b>aaabbbbb</b>c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bbbb', 'cc'],s = "aaabbbbbc") == "<b>aaabbbbb</b>c": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'lapping'],s = "overlapping strings can be tricky") == "<b>overlapping</b> strings can be tricky"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'lapping'],s = "overlapping strings can be tricky") == "<b>overlapping</b> strings can be tricky": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xx', 'xxx', 'xxxx'],s = "xxxxxxxxxxxxxx") == "<b>xxxxxxxxxxxxxx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xx', 'xxx', 'xxxx'],s = "xxxxxxxxxxxxxx") == "<b>xxxxxxxxxxxxxx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c'],s = "abacabadabacaba") == "<b>abacaba</b>d<b>abacaba</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c'],s = "abacabadabacaba") == "<b>abacaba</b>d<b>abacaba</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aba', 'bab', 'abc'],s = "abababc") == "<b>abababc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aba', 'bab', 'abc'],s = "abababc") == "<b>abababc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['ab', 'bc', 'cd'],s = "abcd") == "<b>abcd</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ab', 'bc', 'cd'],s = "abcd") == "<b>abcd</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['nested', 'nest', 'nesting'],s = "nestednestingneste") == "<b>nestednestingnest</b>e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['nested', 'nest', 'nesting'],s = "nestednestingneste") == "<b>nestednestingnest</b>e": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'zyx', 'yzx'],s = "xyzzyxzyxzyxzyx") == "<b>xyzzyxzyxzyxzyx</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'zyx', 'yzx'],s = "xyzzyxzyxzyxzyx") == "<b>xyzzyxzyxzyxzyx</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['quick', 'brown', 'fox'],s = "thequickbrownfoxjumpsoverthelazydog") == "the<b>quickbrownfox</b>jumpsoverthelazydog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['quick', 'brown', 'fox'],s = "thequickbrownfoxjumpsoverthelazydog") == "the<b>quickbrownfox</b>jumpsoverthelazydog": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog'],s = "the cat and the dog went to the market") == "the <b>cat</b> and the <b>dog</b> went to the market"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog'],s = "the cat and the dog went to the market") == "the <b>cat</b> and the <b>dog</b> went to the market": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd'],s = "abcdabc") == "<b>abcdabc</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd'],s = "abcdabc") == "<b>abcdabc</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['unique'],s = "uniqueuniqueunique") == "<b>uniqueuniqueunique</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['unique'],s = "uniqueuniqueunique") == "<b>uniqueuniqueunique</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['overlap', 'laphover'],s = "laphoverlap") == "<b>laphoverlap</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['overlap', 'laphover'],s = "laphoverlap") == "<b>laphoverlap</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['apple', 'apples', 'app'],s = "applesarefruitapples") == "<b>apples</b>arefruit<b>apples</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['apple', 'apples', 'app'],s = "applesarefruitapples") == "<b>apples</b>arefruit<b>apples</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['cat', 'dog', 'fish'],s = "thecatandthedogandthefish") == "the<b>cat</b>andthe<b>dog</b>andthe<b>fish</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['cat', 'dog', 'fish'],s = "thecatandthedogandthefish") == "the<b>cat</b>andthe<b>dog</b>andthe<b>fish</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aba', 'aaa'],s = "aaabaabaa") == "<b>aaabaaba</b>a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aba', 'aaa'],s = "aaabaabaa") == "<b>aaabaaba</b>a": {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'shorter', 'shortest'],s = "shortshortershortest") == "<b>shortshortershortest</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'shorter', 'shortest'],s = "shortshortershortest") == "<b>shortshortershortest</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xyz', 'zyx'],s = "xyzzyxzyxzyxxyz") == "<b>xyzzyxzyxzyxxyz</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xyz', 'zyx'],s = "xyzzyxzyxzyxxyz") == "<b>xyzzyxzyxzyxxyz</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xy', 'yx'],s = "xyyxxyyxxy") == "<b>xyyxxyyxxy</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xy', 'yx'],s = "xyyxxyyxxy") == "<b>xyyxxyyxxy</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing', 'tested'],s = "testtestedtesting") == "<b>testtestedtesting</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing', 'tested'],s = "testtestedtesting") == "<b>testtestedtesting</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['same', 'same', 'same'],s = "samesamesamesame") == "<b>samesamesamesame</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['same', 'same', 'same'],s = "samesamesamesame") == "<b>samesamesamesame</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['test', 'testing'],s = "testtestingtest") == "<b>testtestingtest</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['test', 'testing'],s = "testtestingtest") == "<b>testtestingtest</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wording', 'wordings'],s = "wordwordingwordingsword") == "<b>wordwordingwordingsword</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wording', 'wordings'],s = "wordwordingwordingsword") == "<b>wordwordingwordingsword</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "helloworldhello") == "<b>helloworldhello</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "helloworldhello") == "<b>helloworldhello</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['programming', 'is', 'fun'],s = "programmingisfunandfunisprogramming") == "<b>programmingisfun</b>and<b>funisprogramming</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['programming', 'is', 'fun'],s = "programmingisfunandfunisprogramming") == "<b>programmingisfun</b>and<b>funisprogramming</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['word', 'wording'],s = "wordingword") == "<b>wordingword</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['word', 'wording'],s = "wordingword") == "<b>wordingword</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['dog', 'ogg', 'log'],s = "dog log ogg") == "<b>dog</b> <b>log</b> <b>ogg</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['dog', 'ogg', 'log'],s = "dog log ogg") == "<b>dog</b> <b>log</b> <b>ogg</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['repeated', 'repeat', 'repe'],s = "repeatedrepeatrepeatere") == "<b>repeatedrepeatrepeat</b>ere"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['repeated', 'repeat', 'repe'],s = "repeatedrepeatrepeatere") == "<b>repeatedrepeatrepeat</b>ere": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['abc', 'bcd', 'cde'],s = "abcde") == "<b>abcde</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['abc', 'bcd', 'cde'],s = "abcde") == "<b>abcde</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcdeedcba") == "<b>abcdeedcba</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcdeedcba") == "<b>abcdeedcba</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aaa', 'bbb'],s = "aaabbbccc") == "<b>aaabbb</b>ccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aaa', 'bbb'],s = "aaabbbccc") == "<b>aaabbb</b>ccc": {e}')
    
    total += 1
    try:
        result = candidate(words = ['this', 'that'],s = "this is a test, that should be bold, but this is not that") == "<b>this</b> is a test, <b>that</b> should be bold, but <b>this</b> is not <b>that</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['this', 'that'],s = "this is a test, that should be bold, but this is not that") == "<b>this</b> is a test, <b>that</b> should be bold, but <b>this</b> is not <b>that</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aa', 'aaa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aa', 'aaa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['short', 'longerword', 'longestword'],s = "shortlongerwordlongestword") == "<b>shortlongerwordlongestword</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['short', 'longerword', 'longestword'],s = "shortlongerwordlongestword") == "<b>shortlongerwordlongestword</b>": {e}')
    
    total += 1
    try:
        result = candidate(words = ['xx', 'yy', 'zz'],s = "xyxzyzyxzyzyzyzx") == "xyxzyzyxzyzyzyzx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['xx', 'yy', 'zz'],s = "xyxzyzyxzyzyzyzx") == "xyxzyzyxzyzyzyzx": {e}')
    
    total += 1
    try:
        result = candidate(words = ['aabb', 'bbaa', 'abba'],s = "aabbabbaabba") == "<b>aabbabbaabba</b>"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['aabb', 'bbaa', 'abba'],s = "aabbabbaabba") == "<b>aabbabbaabba</b>": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = [],s = "nothingtoboldhere") == "nothingtoboldhere"
    assert candidate(words = [],s = "abcdefg") == "abcdefg"
    assert candidate(words = ['aaa'],s = "aaaaa") == "<b>aaaaa</b>"
    assert candidate(words = ['ab', 'bc'],s = "aabcd") == "a<b>abc</b>d"
    assert candidate(words = ['is', 'in'],s = "this is an interesting string") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g str<b>in</b>g"
    assert candidate(words = ['foo', 'bar'],s = "foobarbaz") == "<b>foobar</b>baz"
    assert candidate(words = ['z'],s = "zzz") == "<b>zzz</b>"
    assert candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e"
    assert candidate(words = ['a', 'b', 'c'],s = "abcabc") == "<b>abcabc</b>"
    assert candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>"
    assert candidate(words = ['z', 'zz'],s = "zzz") == "<b>zzz</b>"
    assert candidate(words = ['x', 'y', 'z'],s = "xyzxyz") == "<b>xyzxyz</b>"
    assert candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>"
    assert candidate(words = ['ab', 'cb'],s = "aabcd") == "a<b>ab</b>cd"
    assert candidate(words = ['test'],s = "this is a test string") == "this is a <b>test</b> string"
    assert candidate(words = ['cat', 'dog'],s = "cat and dog are friends, but catdog is a special creature") == "<b>cat</b> and <b>dog</b> are friends, but <b>catdog</b> is a special creature"
    assert candidate(words = ['xy', 'yx'],s = "xyyxxyyx") == "<b>xyyxxyyx</b>"
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothreeonethree") == "<b>onetwothreeonethree</b>"
    assert candidate(words = ['x', 'xx', 'xxx', 'xxxx'],s = "xxxxxxx") == "<b>xxxxxxx</b>"
    assert candidate(words = ['aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothreefouronetwothree") == "<b>onetwothree</b>four<b>onetwothree</b>"
    assert candidate(words = ['abc', 'def'],s = "abcdefgabcdef") == "<b>abcdef</b>g<b>abcdef</b>"
    assert candidate(words = ['test', 'testing'],s = "this is a test testing string") == "this is a <b>test</b> <b>testing</b> string"
    assert candidate(words = ['aaa', 'aa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>"
    assert candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>"
    assert candidate(words = ['is', 'island', 'sand'],s = "this is an island surrounded by sand") == "th<b>is</b> <b>is</b> an <b>island</b> surrounded by <b>sand</b>"
    assert candidate(words = ['start', 'middle', 'end'],s = "startmiddleend") == "<b>startmiddleend</b>"
    assert candidate(words = ['zz', 'z'],s = "zzzzzzzzz") == "<b>zzzzzzzzz</b>"
    assert candidate(words = ['overlap', 'lap'],s = "overlaplap") == "<b>overlaplap</b>"
    assert candidate(words = ['overlap', 'lap', 'ap'],s = "overlaplap") == "<b>overlaplap</b>"
    assert candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
    assert candidate(words = ['overlap', 'lapping'],s = "overlappinglapping") == "<b>overlappinglapping</b>"
    assert candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
    assert candidate(words = ['same', 'same', 'same'],s = "samesamesame") == "<b>samesamesame</b>"
    assert candidate(words = ['is', 'in'],s = "this is an interesting situation") == "th<b>is</b> <b>is</b> an <b>in</b>terest<b>in</b>g situation"
    assert candidate(words = ['a', 'b', 'c'],s = "abcabcabc") == "<b>abcabcabc</b>"
    assert candidate(words = ['abc', 'def', 'ghi'],s = "abcdefghi") == "<b>abcdefghi</b>"
    assert candidate(words = ['unique', 'words'],s = "uniquewordswordsunique") == "<b>uniquewordswordsunique</b>"
    assert candidate(words = ['in', 'inception', 'ception'],s = "inceptionception") == "<b>inceptionception</b>"
    assert candidate(words = ['xy', 'yx'],s = "xyxxyxyyx") == "<b>xyxxyxyyx</b>"
    assert candidate(words = ['abc', 'bcd'],s = "abcbcd") == "<b>abcbcd</b>"
    assert candidate(words = ['hello', 'world'],s = "hello world, hello universe") == "<b>hello</b> <b>world</b>, <b>hello</b> universe"
    assert candidate(words = ['cat', 'bat', 'rat'],s = "thequickbrownfoxjumpsoverthelazydog") == "thequickbrownfoxjumpsoverthelazydog"
    assert candidate(words = ['overlap', 'lap', 'lapel'],s = "overlaplapel") == "<b>overlaplapel</b>"
    assert candidate(words = ['hello', 'world'],s = "hello world! hello universe") == "<b>hello</b> <b>world</b>! <b>hello</b> universe"
    assert candidate(words = ['ab', 'bc', 'cd'],s = "abcbcd") == "<b>abcbcd</b>"
    assert candidate(words = ['bold', 'word', 'words'],s = "boldwords") == "<b>boldwords</b>"
    assert candidate(words = ['banana', 'anana'],s = "bananabanana") == "<b>bananabanana</b>"
    assert candidate(words = ['hello', 'world'],s = "hello world hello") == "<b>hello</b> <b>world</b> <b>hello</b>"
    assert candidate(words = ['abc', 'abcd', 'abcde'],s = "abcde") == "<b>abcde</b>"
    assert candidate(words = ['aaa', 'bbb', 'ccc'],s = "aaabbbccc") == "<b>aaabbbccc</b>"
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "edcbaedcba") == "<b>edcbaedcba</b>"
    assert candidate(words = ['nested', 'nest', 'set'],s = "nestedset") == "<b>nestedset</b>"
    assert candidate(words = ['abcde', 'bcdef', 'cdefg'],s = "abcdefghij") == "<b>abcdefg</b>hij"
    assert candidate(words = ['repeated', 'repeat', 'rep'],s = "repeated repeated repeat reprepeated") == "<b>repeated</b> <b>repeated</b> <b>repeat</b> <b>reprepeated</b>"
    assert candidate(words = ['overlap', 'lapping', 'overlappping'],s = "overlappingslappinglappingpings") == "<b>overlapping</b>s<b>lappinglapping</b>pings"
    assert candidate(words = ['short', 'longword', 'tiny'],s = "shortlongwordtinyshort") == "<b>shortlongwordtinyshort</b>"
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothreeone") == "<b>onetwothreeone</b>"
    assert candidate(words = ['cat', 'dog', 'rat'],s = "thecatandthedogandtherat") == "the<b>cat</b>andthe<b>dog</b>andthe<b>rat</b>"
    assert candidate(words = ['quick', 'brown', 'fox'],s = "the quick brown fox jumps over the lazy dog") == "the <b>quick</b> <b>brown</b> <b>fox</b> jumps over the lazy dog"
    assert candidate(words = ['xy', 'yx'],s = "xyyxxy") == "<b>xyyxxy</b>"
    assert candidate(words = ['cat', 'dog', 'bird'],s = "thecatandthedogandthebird") == "the<b>cat</b>andthe<b>dog</b>andthe<b>bird</b>"
    assert candidate(words = ['apple', 'app', 'ple'],s = "appleapples") == "<b>appleapple</b>s"
    assert candidate(words = ['aaa', 'aab', 'abc'],s = "aaaabacababc") == "<b>aaaab</b>acab<b>abc</b>"
    assert candidate(words = ['in', 'inside', 'side'],s = "insideinsideinside") == "<b>insideinsideinside</b>"
    assert candidate(words = ['foo', 'bar', 'baz'],s = "foobarbazfoobarbaz") == "<b>foobarbazfoobarbaz</b>"
    assert candidate(words = ['mississippi', 'issi', 'issipp'],s = "mississippiississippi") == "<b>mississippiississipp</b>i"
    assert candidate(words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],s = "aaaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaaa</b>"
    assert candidate(words = ['repeat', 'peat', 'eat'],s = "repeatpeatpeatpeat") == "<b>repeatpeatpeatpeat</b>"
    assert candidate(words = ['short', 'longerword'],s = "shortlongerwordshort") == "<b>shortlongerwordshort</b>"
    assert candidate(words = ['cat', 'bat'],s = "the cattle were battling the bat") == "the <b>cat</b>tle were <b>bat</b>tling the <b>bat</b>"
    assert candidate(words = ['shorter', 'short', 'sho', 'sh'],s = "shortershortershosh") == "<b>shortershortershosh</b>"
    assert candidate(words = ['hello', 'hell', 'he', 'h'],s = "hellohelhekhhh") == "<b>hellohe</b>l<b>he</b>k<b>hhh</b>"
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothree") == "<b>onetwothree</b>"
    assert candidate(words = ['short', 'longerword', 'tiny'],s = "thisisalongerword") == "thisisa<b>longerword</b>"
    assert candidate(words = ['overlap', 'lapping'],s = "overlapping") == "<b>overlapping</b>"
    assert candidate(words = ['substring', 'string'],s = "this is a substring string") == "this is a <b>substring</b> <b>string</b>"
    assert candidate(words = ['jump', 'jumps'],s = "hejumpsjumpproperly") == "he<b>jumpsjump</b>properly"
    assert candidate(words = ['word', 'world', 'wor'],s = "worldwide world of words") == "<b>world</b>wide <b>world</b> of <b>word</b>s"
    assert candidate(words = ['apple', 'banana', 'cherry'],s = "applebananaapplecherry") == "<b>applebananaapplecherry</b>"
    assert candidate(words = ['python', 'java', 'c'],s = "pythonjavaandcsareprogramminglanguages") == "<b>pythonjava</b>and<b>c</b>sareprogramminglanguages"
    assert candidate(words = ['xy', 'yx'],s = "xyxxyyxxyx") == "<b>xyxxyyxxyx</b>"
    assert candidate(words = ['a', 'aa', 'aaa'],s = "aaaaaaaaaa") == "<b>aaaaaaaaaa</b>"
    assert candidate(words = ['apple', 'banana', 'cherry'],s = "applebananacherry") == "<b>applebananacherry</b>"
    assert candidate(words = ['hello', 'world'],s = "hello world! welcome to the hello world") == "<b>hello</b> <b>world</b>! welcome to the <b>hello</b> <b>world</b>"
    assert candidate(words = ['one', 'two', 'three'],s = "onetwothreeonetwothree") == "<b>onetwothreeonetwothree</b>"
    assert candidate(words = ['test', 'testing', 'tested'],s = "testtestingtested") == "<b>testtestingtested</b>"
    assert candidate(words = ['apple', 'pineapple'],s = "pineappleapple") == "<b>pineappleapple</b>"
    assert candidate(words = ['cat', 'dog', 'bird'],s = "dogcatbirdbirdcat") == "<b>dogcatbirdbirdcat</b>"
    assert candidate(words = ['example', 'sample', 'text'],s = "example sample text") == "<b>example</b> <b>sample</b> <b>text</b>"
    assert candidate(words = ['abc', 'bcd', 'cde'],s = "abcdexyzcde") == "<b>abcde</b>xyz<b>cde</b>"
    assert candidate(words = ['aaa', 'aaaa'],s = "aaaaaaaaa") == "<b>aaaaaaaaa</b>"
    assert candidate(words = ['ab', 'abc', 'abcd'],s = "abcdabcab") == "<b>abcdabcab</b>"
    assert candidate(words = ['xy', 'yx'],s = "xyxxyxyxyxxyyx") == "<b>xyxxyxyxyxxyyx</b>"
    assert candidate(words = ['xy', 'yx'],s = "xyxyxyyxxyxxy") == "<b>xyxyxyyxxyxxy</b>"
    assert candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaa") == "<b>aaaaaa</b>"
    assert candidate(words = ['abc', 'bcd'],s = "abcde") == "<b>abcd</b>e"
    assert candidate(words = ['a', 'b', 'c', 'd'],s = "abcdabcdabcd") == "<b>abcdabcdabcd</b>"
    assert candidate(words = ['repeat', 'eat', 'peat'],s = "repeatpeatpeat") == "<b>repeatpeatpeat</b>"
    assert candidate(words = ['jump', 'jumps', 'jumping'],s = "he was jumping over the jumps while he jump") == "he was <b>jumping</b> over the <b>jumps</b> while he <b>jump</b>"
    assert candidate(words = ['aaa', 'bbbb', 'cc'],s = "aaabbbbbc") == "<b>aaabbbbb</b>c"
    assert candidate(words = ['overlap', 'lapping'],s = "overlapping strings can be tricky") == "<b>overlapping</b> strings can be tricky"
    assert candidate(words = ['xx', 'xxx', 'xxxx'],s = "xxxxxxxxxxxxxx") == "<b>xxxxxxxxxxxxxx</b>"
    assert candidate(words = ['a', 'b', 'c'],s = "abacabadabacaba") == "<b>abacaba</b>d<b>abacaba</b>"
    assert candidate(words = ['aba', 'bab', 'abc'],s = "abababc") == "<b>abababc</b>"
    assert candidate(words = ['ab', 'bc', 'cd'],s = "abcd") == "<b>abcd</b>"
    assert candidate(words = ['nested', 'nest', 'nesting'],s = "nestednestingneste") == "<b>nestednestingnest</b>e"
    assert candidate(words = ['xyz', 'zyx', 'yzx'],s = "xyzzyxzyxzyxzyx") == "<b>xyzzyxzyxzyxzyx</b>"
    assert candidate(words = ['quick', 'brown', 'fox'],s = "thequickbrownfoxjumpsoverthelazydog") == "the<b>quickbrownfox</b>jumpsoverthelazydog"
    assert candidate(words = ['cat', 'dog'],s = "the cat and the dog went to the market") == "the <b>cat</b> and the <b>dog</b> went to the market"
    assert candidate(words = ['abc', 'bcd'],s = "abcdabc") == "<b>abcdabc</b>"
    assert candidate(words = ['unique'],s = "uniqueuniqueunique") == "<b>uniqueuniqueunique</b>"
    assert candidate(words = ['overlap', 'laphover'],s = "laphoverlap") == "<b>laphoverlap</b>"
    assert candidate(words = ['apple', 'apples', 'app'],s = "applesarefruitapples") == "<b>apples</b>arefruit<b>apples</b>"
    assert candidate(words = ['cat', 'dog', 'fish'],s = "thecatandthedogandthefish") == "the<b>cat</b>andthe<b>dog</b>andthe<b>fish</b>"
    assert candidate(words = ['aba', 'aaa'],s = "aaabaabaa") == "<b>aaabaaba</b>a"
    assert candidate(words = ['short', 'shorter', 'shortest'],s = "shortshortershortest") == "<b>shortshortershortest</b>"
    assert candidate(words = ['xyz', 'zyx'],s = "xyzzyxzyxzyxxyz") == "<b>xyzzyxzyxzyxxyz</b>"
    assert candidate(words = ['xy', 'yx'],s = "xyyxxyyxxy") == "<b>xyyxxyyxxy</b>"
    assert candidate(words = ['test', 'testing', 'tested'],s = "testtestedtesting") == "<b>testtestedtesting</b>"
    assert candidate(words = ['same', 'same', 'same'],s = "samesamesamesame") == "<b>samesamesamesame</b>"
    assert candidate(words = ['test', 'testing'],s = "testtestingtest") == "<b>testtestingtest</b>"
    assert candidate(words = ['word', 'wording', 'wordings'],s = "wordwordingwordingsword") == "<b>wordwordingwordingsword</b>"
    assert candidate(words = ['hello', 'world'],s = "helloworldhello") == "<b>helloworldhello</b>"
    assert candidate(words = ['programming', 'is', 'fun'],s = "programmingisfunandfunisprogramming") == "<b>programmingisfun</b>and<b>funisprogramming</b>"
    assert candidate(words = ['word', 'wording'],s = "wordingword") == "<b>wordingword</b>"
    assert candidate(words = ['dog', 'ogg', 'log'],s = "dog log ogg") == "<b>dog</b> <b>log</b> <b>ogg</b>"
    assert candidate(words = ['repeated', 'repeat', 'repe'],s = "repeatedrepeatrepeatere") == "<b>repeatedrepeatrepeat</b>ere"
    assert candidate(words = ['aaa', 'aa', 'a'],s = "aaaaaaaa") == "<b>aaaaaaaa</b>"
    assert candidate(words = ['abc', 'bcd', 'cde'],s = "abcde") == "<b>abcde</b>"
    assert candidate(words = ['a', 'b', 'c', 'd', 'e'],s = "abcdeedcba") == "<b>abcdeedcba</b>"
    assert candidate(words = ['hello', 'world'],s = "helloworld") == "<b>helloworld</b>"
    assert candidate(words = ['aaa', 'bbb'],s = "aaabbbccc") == "<b>aaabbb</b>ccc"
    assert candidate(words = ['this', 'that'],s = "this is a test, that should be bold, but this is not that") == "<b>this</b> is a test, <b>that</b> should be bold, but <b>this</b> is not <b>that</b>"
    assert candidate(words = ['aa', 'aaa'],s = "aaaaaaaaaaaaaaaa") == "<b>aaaaaaaaaaaaaaaa</b>"
    assert candidate(words = ['short', 'longerword', 'longestword'],s = "shortlongerwordlongestword") == "<b>shortlongerwordlongestword</b>"
    assert candidate(words = ['xx', 'yy', 'zz'],s = "xyxzyzyxzyzyzyzx") == "xyxzyzyxzyzyzyzx"
    assert candidate(words = ['aabb', 'bbaa', 'abba'],s = "aabbabbaabba") == "<b>aabbabbaabba</b>"


