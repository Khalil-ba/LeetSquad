def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sentence = "no-digits123 or symbols#allowed") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-digits123 or symbols#allowed") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b.c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b.c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world, this-is-a-test") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world, this-is-a-test") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "singleletter a b c d e f g") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "singleletter a b c d e f g") == 8: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-words only") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-words only") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello world! this is a test.") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello world! this is a test.") == 6: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world, my.name-is Qwen") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world, my.name-is Qwen") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "ending-with-punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "ending-with-punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "invalid--double-dash") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "invalid--double-dash") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple   spaces   between   words") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple   spaces   between   words") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple--hyphens") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple--hyphens") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-hyphenated-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-hyphenated-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-invalid invalid- invalid-!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-invalid invalid- invalid-!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "well-well, well!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "well-well, well!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "singleletter") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "singleletter") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a! b. c?") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a! b. c?") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b-c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b-c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-world") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-world") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b-c d-e f-g") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b-c d-e f-g") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "no-digits-allowed 123 456-789") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-digits-allowed 123 456-789") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "alice and  bob are playing stone-game10") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "alice and  bob are playing stone-game10") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "no-dash-here") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-dash-here") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word here!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word here!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b- c d") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b- c d") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word here and another-valid one!") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word here and another-valid one!") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b-c-d.e.f!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b-c-d.e.f!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "singleletter a b c") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "singleletter a b c") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b. afad ba-c a! .") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b. afad ba-c a! .") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b-c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b-c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello!world") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello!world") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = ",") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = ",") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a!b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a!b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-ab cd- ef-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-ab cd- ef-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world, my name is john-doe.") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world, my name is john-doe.") == 5: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!this  1-s b8d!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!this  1-s b8d!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "trailingpunctuation. comma, exclamation!") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "trailingpunctuation. comma, exclamation!") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation,in,middle,a-b.c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation,in,middle,a-b.c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "invalid-end-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "invalid-end-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-invalid start") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-invalid start") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word here! and here.") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word here! and here.") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-here!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-here!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation,at,end.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation,at,end.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b.c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b.c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "cat and  dog") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "cat and  dog") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = ".") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = ".") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-invalid-start") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-invalid-start") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation! marks, are: allowed?") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation! marks, are: allowed?") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation.only,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation.only,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-word-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-word-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation-after-hyphen-! invalid") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation-after-hyphen-! invalid") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation-1,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation-1,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, valid-word!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, valid-word!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word?") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word?") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word@123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word@123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-hyphen-and-punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-hyphen-and-punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, invalid-word2") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, invalid-word2") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-1b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-1b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-1b-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-1b-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation,at,end.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation,at,end.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple---hyphens-in-a-row") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple---hyphens-in-a-row") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-in-middle-1word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-in-middle-1word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation-inside-word!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation-inside-word!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b-c d-e-f g-h") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b-c d-e-f g-h") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation-and-digit1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation-and-digit1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-word-with-leading-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-word-with-leading-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-b--1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-b--1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation! word-without") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation! word-without") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word. word- word!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word. word- word!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hyphenated-word- is valid") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hyphenated-word- is valid") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "no-spaces") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-spaces") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-1-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-1-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word! word- word. word?") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word! word- word. word?") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hyphen-at-end-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hyphen-at-end-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple---hyphens") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple---hyphens") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-exclamation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-exclamation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-word!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word word, word! word.") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word word, word! word.") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-b--") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-b--") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- word-with-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- word-with-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit1-and-punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit1-and-punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation-in-middle-of-word!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation-in-middle-of-word!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "singleletter singleletter! singleletter.") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "singleletter singleletter! singleletter.") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-at-end1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-at-end1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-1--b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-1--b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation-and-hyphen-word-123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation-and-hyphen-word-123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple--dashes are invalid") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple--dashes are invalid") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation.at.end,invalid") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation.at.end,invalid") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit1-and-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit1-and-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-punctuation-at-end,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-punctuation-at-end,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-hyphenated-word a-b") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-hyphenated-word a-b") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "123 word- word! word?") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "123 word- word! word?") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation, word-with-hyphen-and-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation, word-with-hyphen-and-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-word- valid-word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-word- valid-word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation-only! and !only-punctuation") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation-only! and !only-punctuation") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world- is not valid") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world- is not valid") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-valid-hyphen word-with--invalid-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-valid-hyphen word-with--invalid-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word valid-word- valid-word") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word valid-word- valid-word") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-1-word!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-1-word!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "invalid-1word and valid-word") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "invalid-1word and valid-word") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation,at,end!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation,at,end!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-ending-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-ending-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation,word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation,word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word..") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word..") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple-spaces   between   words") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple-spaces   between   words") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word-") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word-") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word- word- valid") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word- word- valid") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a--b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a--b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word word- word. word?") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word word- word. word?") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-b1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-b1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word- word! word@") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word- word! word@") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def,word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def,word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen- valid-word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen- valid-word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1-,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1-,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "validwordwithmultiplepunctuations,,,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "validwordwithmultiplepunctuations,,,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-hyphen-and-comma, valid.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-hyphen-and-comma, valid.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word,word,word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word,word,word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-punctuation-at-end!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-punctuation-at-end!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word,with,commas and.punctuations") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word,with,commas and.punctuations") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word@!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word@!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123?") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123?") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, valid-word. valid-word! valid-word") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, valid-word. valid-word! valid-word") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-space-in-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-space-in-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation word-with-hyphen-and-punctuation-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation word-with-hyphen-and-punctuation-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple---hyphens-in-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple---hyphens-in-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word,word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word,word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word?") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word?") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "123 456 789") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "123 456 789") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation!in!the!middle") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation!in!the!middle") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple-punctuation,,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple-punctuation,,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-digit-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-digit-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit123 and another-word!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit123 and another-word!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a!b.c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a!b.c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple-punctuation!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple-punctuation!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with123-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with123-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "only!only only.only only-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "only!only only.only only-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word1 word2- word3- word4") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word1 word2- word3- word4") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-1digit") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-1digit") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, and invalid-word1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, and invalid-word1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation-in-middle.a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation-in-middle.a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word@?") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word@?") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-period.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-period.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,and valid-word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,and valid-word!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations,word-with-punctuations.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations,word-with-punctuations.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word followed-by-number123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word followed-by-number123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-punctuation!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-punctuation!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word word- word! word-") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word word- word! word-") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-! word- word-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-! word- word-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-word-1.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-word-1.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen word-with-hyphen- word-with-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen word-with-hyphen- word-with-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word! another-valid-word?") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word! another-valid-word?") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation.at-end") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation.at-end") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, invalid-word123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, invalid-word123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!valid valid. valid-") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!valid valid. valid-") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1-.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1-.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a a-b a-b-c a-b-c-d") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a a-b a-b-c a-b-c-d") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-trailing-punctuation,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-trailing-punctuation,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple   spaces") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple   spaces") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word?") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word?") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple-punctuation..") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple-punctuation..") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word! word- word. word-") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word! word- word. word-") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word followed-by-digits123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word followed-by-digits123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen--b-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen--b-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hello-world- is-not-valid") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hello-world- is-not-valid") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations!word-with-punctuations!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations!word-with-punctuations!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-a") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-a") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "nohyphens here!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "nohyphens here!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation-at-start!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation-at-start!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "leading!and-trailing!punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "leading!and-trailing!punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "no-dashes-here but-here-are-too-many-dashes") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-dashes-here but-here-are-too-many-dashes") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphen- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphen- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-hyphen-and-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-hyphen-and-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, valid-word. valid-word!") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, valid-word. valid-word!") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation.at.end.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation.at.end.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word-") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word-") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a!b!c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a!b!c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-number1234 and valid-word") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-number1234 and valid-word") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word,word!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word,word!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word@") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word@") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word1 word2 word3 word4") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word1 word2 word3 word4") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation,at,end!invalid") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation,at,end!invalid") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "complex-word-with-punctuation,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "complex-word-with-punctuation,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-letter-word a") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-letter-word a") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-trailing-hyphen-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-trailing-hyphen-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation.multiple") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation.multiple") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multi-hyphen-word-123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multi-hyphen-word-123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen word-with-hyphen-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen word-with-hyphen-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word a valid-word- valid-word") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word a valid-word- valid-word") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation-1.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation-1.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-b-1--") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-b-1--") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word!word!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word!word!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!word .word ,word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!word .word ,word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "invalid-punctuation, invalid-punctuation! invalid-punctuation?") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "invalid-punctuation, invalid-punctuation! invalid-punctuation?") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b.c.d") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b.c.d") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multi-hyphenated-word-should-fail") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multi-hyphenated-word-should-fail") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation!in!middle") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation!in!middle") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "trailing-hyphen- invalid-hyphen-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "trailing-hyphen- invalid-hyphen-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-letter a") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-letter a") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen--b1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen--b1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-period-and-comma,./") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-period-and-comma,./") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations! word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations! word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-2-hyphens-a-b-c") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-2-hyphens-a-b-c") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with--double-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with--double-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b-c!d.e") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b-c!d.e") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "this-is-valid-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "this-is-valid-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word! valid-word!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word! valid-word!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-digit1-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-digit1-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a!b-c.d.e") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a!b-c.d.e") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b-c.d.e") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b-c.d.e") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1-!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1-!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "1word 12word word3") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "1word 12word word3") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation,word-with-punctuation, word-with-punctuation!word-with-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation,word-with-punctuation, word-with-punctuation!word-with-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a!b.c-d.e") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a!b.c-d.e") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-1 valid-word-2") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-1 valid-word-2") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word!word another-word,") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word!word another-word,") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b-c.d!e") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b-c.d!e") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b.c.d") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b.c.d") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "mid,dash") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "mid,dash") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid.word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid.word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word valid-word-") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word valid-word-") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations,word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations,word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-word-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-word-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-comma,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-comma,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-hyphen-at-start") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-hyphen-at-start") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-punctuation-mark.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-punctuation-mark.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!invalid-start-word invalid-end-word!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!invalid-start-word invalid-end-word!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a-b-c-d") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a-b-c-d") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-at-end1.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-at-end1.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple-hyphens-in--one-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple-hyphens-in--one-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a valid-word- valid-word valid-word-") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a valid-word- valid-word valid-word-") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "double--hyphen invalid") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "double--hyphen invalid") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "validwordwithmultiplepunctuations...") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "validwordwithmultiplepunctuations...") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "!a-b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "!a-b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word! word- word. word@") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word! word- word. word@") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-word valid-word") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-word valid-word") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "leading-hyphen invalid-hyphen") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "leading-hyphen invalid-hyphen") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "a.b.c!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "a.b.c!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "invalid-word- punctuation-here.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "invalid-word- punctuation-here.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-here, and-this.is!ok") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-here, and-this.is!ok") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word, valid-word.") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word, valid-word.") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word valid-word valid-word-") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word valid-word valid-word-") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-h word-hyphenated word-!") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-h word-hyphenated word-!") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "another!valid!word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "another!valid!word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with.punctuation") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with.punctuation") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-hyphenated-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-hyphenated-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word word-with-hyphen-") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word word-with-hyphen-") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation! word-with-hyphen-and-punctuation!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation! word-with-hyphen-and-punctuation!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "single-letter a valid-word") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "single-letter a valid-word") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-hyphen-and-punctuation,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-hyphen-and-punctuation,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen-and-punctuation.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen-and-punctuation.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word!") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "end! punctuation") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "end! punctuation") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-at-end1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-at-end1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "hyphenated-word-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "hyphenated-word-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word,") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word,") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-word-with-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-word-with-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "only-allowed-here") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "only-allowed-here") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-in-hyphen-1-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-in-hyphen-1-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "mixed-case Words Are Invalid") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "mixed-case Words Are Invalid") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "-leading-hyphen") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "-leading-hyphen") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation!at!the!end") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation!at!the!end") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "validwordwithmultiplepunctuations!!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "validwordwithmultiplepunctuations!!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word word-with-hyphen") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word word-with-hyphen") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit1-and-punctuation,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit1-and-punctuation,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-hyphen123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-hyphen123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation!at!end") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation!at!end") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated word- word. word?") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated word- word. word?") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-at-end1,") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-at-end1,") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word word- word! word?") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word word- word! word?") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word,another-valid-word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word,another-valid-word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "trailing-punctuations,, are! invalid") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "trailing-punctuations,, are! invalid") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuation!and-more") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuation!and-more") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "123abc and abc123 are invalid") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "123abc and abc123 are invalid") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen--b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen--b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-b-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-b-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word! valid-word, valid-word.") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word! valid-word, valid-word.") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "no-hyphens allowed") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "no-hyphens allowed") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation-1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation-1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple    spaces    between words") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple    spaces    between words") == 4: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "triple-hyphen---word") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "triple-hyphen---word") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "punctuation,,comma and space") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "punctuation,,comma and space") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-2!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-2!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit1-and-hyphen-b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit1-and-hyphen-b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-hyphen-word word- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-hyphen-word word- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word- word- word- word.") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word- word- word- word.") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "trailing-hyphen-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "trailing-hyphen-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word- word- word- word") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word- word- word- word") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-punctuation1!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-punctuation1!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-multiple-punctuations!!!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-multiple-punctuations!!!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations!.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations!.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word1- word2- word3- word4-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word1- word2- word3- word4-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multiple--hyphens-are!invalid") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multiple--hyphens-are!invalid") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc123") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc123") == 1: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word- valid-word- valid-word-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word- valid-word- valid-word-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-with-punctuation-at-end.") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-with-punctuation-at-end.") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen1-b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen1-b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "multi-hyphen-usage-is-not-allowed") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "multi-hyphen-usage-is-not-allowed") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with! punctuation") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with! punctuation") == 2: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word valid-word valid-word") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word valid-word valid-word") == 3: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid-word-1 valid-word-2 valid-word-3") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid-word-1 valid-word-2 valid-word-3") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-in-hyphen-word-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-in-hyphen-word-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "word-with-digit-and-hyphen-1-b") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "word-with-digit-and-hyphen-1-b") == 0: {e}')
    
    total += 1
    try:
        result = candidate(sentence = "valid,word valid.word valid-word!") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sentence = "valid,word valid.word valid-word!") == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sentence = "no-digits123 or symbols#allowed") == 2
    assert candidate(sentence = "a.b.c") == 0
    assert candidate(sentence = "hello-world, this-is-a-test") == 1
    assert candidate(sentence = "hello-") == 0
    assert candidate(sentence = "a-") == 0
    assert candidate(sentence = "singleletter a b c d e f g") == 8
    assert candidate(sentence = "valid-words only") == 2
    assert candidate(sentence = "a") == 1
    assert candidate(sentence = "hello world! this is a test.") == 6
    assert candidate(sentence = "hello-world, my.name-is Qwen") == 2
    assert candidate(sentence = "ending-with-punctuation!") == 0
    assert candidate(sentence = "invalid--double-dash") == 0
    assert candidate(sentence = "multiple   spaces   between   words") == 4
    assert candidate(sentence = "123") == 0
    assert candidate(sentence = "multiple--hyphens") == 0
    assert candidate(sentence = "valid-hyphenated-word") == 0
    assert candidate(sentence = "-invalid invalid- invalid-!") == 0
    assert candidate(sentence = "well-well, well!") == 2
    assert candidate(sentence = "singleletter") == 1
    assert candidate(sentence = "a! b. c?") == 3
    assert candidate(sentence = "hello-world") == 1
    assert candidate(sentence = "a-b-c") == 0
    assert candidate(sentence = "-world") == 0
    assert candidate(sentence = "a-b-c d-e f-g") == 2
    assert candidate(sentence = "-b") == 0
    assert candidate(sentence = "no-digits-allowed 123 456-789") == 0
    assert candidate(sentence = "alice and  bob are playing stone-game10") == 5
    assert candidate(sentence = "no-dash-here") == 0
    assert candidate(sentence = "a-b!") == 1
    assert candidate(sentence = "valid-word here!") == 2
    assert candidate(sentence = "a-b- c d") == 2
    assert candidate(sentence = "valid-word here and another-valid one!") == 5
    assert candidate(sentence = "a-b-c-d.e.f!") == 0
    assert candidate(sentence = "singleletter a b c") == 4
    assert candidate(sentence = "a-b. afad ba-c a! .") == 5
    assert candidate(sentence = "a.b-c") == 0
    assert candidate(sentence = "hello!world") == 0
    assert candidate(sentence = ",") == 1
    assert candidate(sentence = "a!b") == 0
    assert candidate(sentence = "-ab cd- ef-") == 0
    assert candidate(sentence = "hello-world, my name is john-doe.") == 5
    assert candidate(sentence = "!this  1-s b8d!") == 0
    assert candidate(sentence = "trailingpunctuation. comma, exclamation!") == 3
    assert candidate(sentence = "punctuation,in,middle,a-b.c") == 0
    assert candidate(sentence = "invalid-end-") == 0
    assert candidate(sentence = "-invalid start") == 1
    assert candidate(sentence = "valid-word here! and here.") == 4
    assert candidate(sentence = "!") == 1
    assert candidate(sentence = "valid-word-here!") == 0
    assert candidate(sentence = "punctuation,at,end.") == 0
    assert candidate(sentence = "a-b.c") == 0
    assert candidate(sentence = "cat and  dog") == 3
    assert candidate(sentence = ".") == 1
    assert candidate(sentence = "-invalid-start") == 0
    assert candidate(sentence = "a.b") == 0
    assert candidate(sentence = "hello-world!") == 1
    assert candidate(sentence = "punctuation! marks, are: allowed?") == 4
    assert candidate(sentence = "punctuation.only,") == 0
    assert candidate(sentence = "valid-word- valid-word-") == 0
    assert candidate(sentence = "word-with-digit1") == 0
    assert candidate(sentence = "punctuation-after-hyphen-! invalid") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation-1,") == 0
    assert candidate(sentence = "valid-word, valid-word!") == 2
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word?") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word@123") == 1
    assert candidate(sentence = "valid-word-with-hyphen-and-punctuation!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!") == 1
    assert candidate(sentence = "valid-word, invalid-word2") == 1
    assert candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-,") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@") == 1
    assert candidate(sentence = "word-with-digit-and-hyphen-1b") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-1b-") == 0
    assert candidate(sentence = "valid-word-123") == 0
    assert candidate(sentence = "word-with-punctuation,at,end.") == 0
    assert candidate(sentence = "multiple---hyphens-in-a-row") == 0
    assert candidate(sentence = "word-with-hyphen-") == 0
    assert candidate(sentence = "word-with-digit-in-middle-1word") == 0
    assert candidate(sentence = "punctuation-inside-word!word") == 0
    assert candidate(sentence = "a-b-c d-e-f g-h") == 1
    assert candidate(sentence = "word-with-punctuation-and-digit1!") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-!") == 0
    assert candidate(sentence = "-word-with-leading-hyphen") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-b--1") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc") == 1
    assert candidate(sentence = "word-with-punctuation! word-without") == 1
    assert candidate(sentence = "word. word- word!") == 2
    assert candidate(sentence = "hyphenated-word- is valid") == 2
    assert candidate(sentence = "no-spaces") == 1
    assert candidate(sentence = "word-with-digit-and-hyphen-1-word") == 0
    assert candidate(sentence = "word! word- word. word?") == 3
    assert candidate(sentence = "hyphen-at-end-") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word!") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@!") == 1
    assert candidate(sentence = "multiple---hyphens") == 0
    assert candidate(sentence = "word-with-hyphen-and-exclamation!") == 0
    assert candidate(sentence = "valid-word- valid-word!") == 1
    assert candidate(sentence = "word word, word! word.") == 4
    assert candidate(sentence = "word-with-digit-and-hyphen-b--") == 0
    assert candidate(sentence = "valid-word- word-with-hyphen") == 0
    assert candidate(sentence = "word-with-digit1-and-punctuation!") == 0
    assert candidate(sentence = "punctuation-in-middle-of-word!word") == 0
    assert candidate(sentence = "word!word") == 0
    assert candidate(sentence = "singleletter singleletter! singleletter.") == 3
    assert candidate(sentence = "word-with-digit-at-end1!") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-1--b") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#") == 1
    assert candidate(sentence = "word-with-punctuation-and-hyphen-word-123") == 0
    assert candidate(sentence = "multiple--dashes are invalid") == 2
    assert candidate(sentence = "word-with-punctuation.at.end,invalid") == 0
    assert candidate(sentence = "word-with-digit1-and-punctuation.") == 0
    assert candidate(sentence = "valid-word-with-punctuation-at-end,") == 0
    assert candidate(sentence = "single-hyphenated-word a-b") == 1
    assert candidate(sentence = "123 word- word! word?") == 2
    assert candidate(sentence = "a.b!") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation, word-with-hyphen-and-punctuation.") == 0
    assert candidate(sentence = "valid-word- valid-word- valid-word") == 1
    assert candidate(sentence = "punctuation-only! and !only-punctuation") == 2
    assert candidate(sentence = "hello-world- is not valid") == 3
    assert candidate(sentence = "word-with-valid-hyphen word-with--invalid-hyphen") == 0
    assert candidate(sentence = "valid-word valid-word- valid-word") == 2
    assert candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-1-word!") == 0
    assert candidate(sentence = "invalid-1word and valid-word") == 2
    assert candidate(sentence = "word-with-punctuation,at,end!") == 0
    assert candidate(sentence = "word- word") == 1
    assert candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
    assert candidate(sentence = "valid-ending-punctuation.") == 0
    assert candidate(sentence = "word-with-punctuation,word") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!") == 1
    assert candidate(sentence = "word..") == 0
    assert candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,") == 0
    assert candidate(sentence = "multiple-spaces   between   words") == 3
    assert candidate(sentence = "word-with-hyphen-123") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word-") == 1
    assert candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
    assert candidate(sentence = "valid!word") == 0
    assert candidate(sentence = "word- word- valid") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-123") == 1
    assert candidate(sentence = "a--b") == 0
    assert candidate(sentence = "word-hyphenated-word word- word. word?") == 2
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!") == 1
    assert candidate(sentence = "word-with-digit-and-hyphen-b1") == 0
    assert candidate(sentence = "word- word! word@") == 2
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def,word") == 1
    assert candidate(sentence = "word-with-hyphen- valid-word") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation1-,") == 0
    assert candidate(sentence = "validwordwithmultiplepunctuations,,,") == 0
    assert candidate(sentence = "valid-word-with-hyphen-and-comma, valid.") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#") == 1
    assert candidate(sentence = "word,word,word") == 0
    assert candidate(sentence = "valid-word-with-punctuation-at-end!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123!") == 1
    assert candidate(sentence = "word,with,commas and.punctuations") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word@!") == 2
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123?") == 1
    assert candidate(sentence = "valid-word, valid-word. valid-word! valid-word") == 4
    assert candidate(sentence = "word-with-hyphen-and-punctuation,") == 0
    assert candidate(sentence = "word-with-space-in-word") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation word-with-hyphen-and-punctuation-") == 0
    assert candidate(sentence = "multiple---hyphens-in-word") == 0
    assert candidate(sentence = "word,word") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word?") == 2
    assert candidate(sentence = "123 456 789") == 0
    assert candidate(sentence = "punctuation!in!the!middle") == 0
    assert candidate(sentence = "multiple-punctuation,,") == 0
    assert candidate(sentence = "word-with-hyphen-and-digit-1") == 0
    assert candidate(sentence = "word-with-digit123") == 0
    assert candidate(sentence = "word-with-digit123 and another-word!") == 2
    assert candidate(sentence = "a!b.c") == 0
    assert candidate(sentence = "multiple-punctuation!!") == 0
    assert candidate(sentence = "word-with123-hyphen") == 0
    assert candidate(sentence = "only!only only.only only-") == 0
    assert candidate(sentence = "word1 word2- word3- word4") == 0
    assert candidate(sentence = "word-with-hyphen- word") == 1
    assert candidate(sentence = "valid-word") == 1
    assert candidate(sentence = "-word") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word") == 1
    assert candidate(sentence = "word-with-1digit") == 0
    assert candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
    assert candidate(sentence = "valid-word, and invalid-word1") == 2
    assert candidate(sentence = "word-with-punctuation-in-middle.a") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word@?") == 2
    assert candidate(sentence = "word-with-hyphen-and-period.") == 0
    assert candidate(sentence = "word-with-multiple-hyphens-and-punctuation-,and valid-word!") == 1
    assert candidate(sentence = "word-with-punctuations,word-with-punctuations.") == 0
    assert candidate(sentence = "valid-word followed-by-number123") == 1
    assert candidate(sentence = "single-punctuation!") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@123") == 1
    assert candidate(sentence = "word word- word! word-") == 2
    assert candidate(sentence = "word-! word- word-") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc123") == 1
    assert candidate(sentence = "word-with-digit-and-hyphen-and-punctuation-word-1.") == 0
    assert candidate(sentence = "word-with-hyphen word-with-hyphen- word-with-hyphen") == 0
    assert candidate(sentence = "valid-word! another-valid-word?") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation1,") == 0
    assert candidate(sentence = "word-with-punctuation.at-end") == 0
    assert candidate(sentence = "valid-word, invalid-word123") == 1
    assert candidate(sentence = "!valid valid. valid-") == 1
    assert candidate(sentence = "valid-word.") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation1-.") == 0
    assert candidate(sentence = "a a-b a-b-c a-b-c-d") == 2
    assert candidate(sentence = "word-with-trailing-punctuation,") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation-after-hyphen-.") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@123") == 1
    assert candidate(sentence = "multiple   spaces") == 2
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word?") == 1
    assert candidate(sentence = "multiple-punctuation..") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-123") == 1
    assert candidate(sentence = "word! word- word. word-") == 2
    assert candidate(sentence = "valid-word followed-by-digits123") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc") == 1
    assert candidate(sentence = "word-with-digit-and-hyphen--b-1") == 0
    assert candidate(sentence = "hello-world- is-not-valid") == 0
    assert candidate(sentence = "word-with-punctuations!word-with-punctuations!") == 0
    assert candidate(sentence = "-a") == 0
    assert candidate(sentence = "nohyphens here!") == 2
    assert candidate(sentence = "word-with-punctuation-at-start!word") == 0
    assert candidate(sentence = "leading!and-trailing!punctuation!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def!") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc") == 1
    assert candidate(sentence = "no-dashes-here but-here-are-too-many-dashes") == 0
    assert candidate(sentence = "word-hyphen- word") == 1
    assert candidate(sentence = "valid-word-with-hyphen-and-punctuation.") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation!") == 0
    assert candidate(sentence = "valid-word, valid-word. valid-word!") == 3
    assert candidate(sentence = "word-with-punctuation.at.end.") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word-") == 1
    assert candidate(sentence = "a!b!c") == 0
    assert candidate(sentence = "word-with-number1234 and valid-word") == 2
    assert candidate(sentence = "word,word!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word@") == 2
    assert candidate(sentence = "word1 word2 word3 word4") == 0
    assert candidate(sentence = "word-with-punctuation,at,end!invalid") == 0
    assert candidate(sentence = "complex-word-with-punctuation,") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def!") == 1
    assert candidate(sentence = "word-with-punctuations!word-with-punctuations!word-with-punctuations!word-with-punctuations.") == 0
    assert candidate(sentence = "single-letter-word a") == 1
    assert candidate(sentence = "word-with-trailing-hyphen-") == 0
    assert candidate(sentence = "punctuation.multiple") == 0
    assert candidate(sentence = "multi-hyphen-word-123") == 0
    assert candidate(sentence = "word-with-hyphen word-with-hyphen-") == 0
    assert candidate(sentence = "valid-word a valid-word- valid-word") == 3
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc123") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation-1.") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-b-1--") == 0
    assert candidate(sentence = "word!word!") == 0
    assert candidate(sentence = "!word .word ,word") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation- word") == 1
    assert candidate(sentence = "invalid-punctuation, invalid-punctuation! invalid-punctuation?") == 3
    assert candidate(sentence = "a.b.c.d") == 0
    assert candidate(sentence = "multi-hyphenated-word-should-fail") == 0
    assert candidate(sentence = "valid-word!") == 1
    assert candidate(sentence = "punctuation!in!middle") == 0
    assert candidate(sentence = "trailing-hyphen- invalid-hyphen-") == 0
    assert candidate(sentence = "single-letter a") == 2
    assert candidate(sentence = "word-with-digit-and-hyphen--b1") == 0
    assert candidate(sentence = "word-with-hyphen-and-period-and-comma,./") == 0
    assert candidate(sentence = "word-with-punctuations! word") == 1
    assert candidate(sentence = "word-with-2-hyphens-a-b-c") == 0
    assert candidate(sentence = "word-with--double-hyphen") == 0
    assert candidate(sentence = "a.b-c!d.e") == 0
    assert candidate(sentence = "this-is-valid-1") == 0
    assert candidate(sentence = "valid-word! valid-word!") == 2
    assert candidate(sentence = "word-with-hyphen-and-digit1-") == 0
    assert candidate(sentence = "a!b-c.d.e") == 0
    assert candidate(sentence = "a.b-c.d.e") == 0
    assert candidate(sentence = "word-with-digit-and-punctuation1-!") == 0
    assert candidate(sentence = "1word 12word word3") == 0
    assert candidate(sentence = "word-with-punctuation,word-with-punctuation, word-with-punctuation!word-with-punctuation.") == 0
    assert candidate(sentence = "a!b.c-d.e") == 0
    assert candidate(sentence = "valid-word-1 valid-word-2") == 0
    assert candidate(sentence = "word!word another-word,") == 1
    assert candidate(sentence = "a.b-c.d!e") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def") == 1
    assert candidate(sentence = "a-b.c.d") == 0
    assert candidate(sentence = "mid,dash") == 0
    assert candidate(sentence = "valid.word") == 0
    assert candidate(sentence = "valid-word valid-word-") == 1
    assert candidate(sentence = "word-with-punctuations,word") == 0
    assert candidate(sentence = "word-with-digit-and-punctuation1.") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-word-1") == 0
    assert candidate(sentence = "word-!") == 0
    assert candidate(sentence = "word-with-hyphen-and-comma,") == 0
    assert candidate(sentence = "-hyphen-at-start") == 0
    assert candidate(sentence = "single-punctuation-mark.") == 0
    assert candidate(sentence = "!invalid-start-word invalid-end-word!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def!") == 1
    assert candidate(sentence = "a-b-c-d") == 0
    assert candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
    assert candidate(sentence = "word-with-digit-at-end1.") == 0
    assert candidate(sentence = "valid-word-!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc-def") == 1
    assert candidate(sentence = "multiple-hyphens-in--one-word") == 0
    assert candidate(sentence = "a valid-word- valid-word valid-word-") == 2
    assert candidate(sentence = "double--hyphen invalid") == 1
    assert candidate(sentence = "validwordwithmultiplepunctuations...") == 0
    assert candidate(sentence = "!a-b") == 0
    assert candidate(sentence = "word! word- word. word@") == 3
    assert candidate(sentence = "valid-word- valid-word valid-word") == 2
    assert candidate(sentence = "leading-hyphen invalid-hyphen") == 2
    assert candidate(sentence = "a.b.c!") == 0
    assert candidate(sentence = "invalid-word- punctuation-here.") == 1
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def") == 1
    assert candidate(sentence = "valid-word-here, and-this.is!ok") == 0
    assert candidate(sentence = "valid-word, valid-word.") == 2
    assert candidate(sentence = "valid-word valid-word valid-word-") == 2
    assert candidate(sentence = "word-h word-hyphenated word-!") == 2
    assert candidate(sentence = "another!valid!word") == 0
    assert candidate(sentence = "word-with.punctuation") == 0
    assert candidate(sentence = "valid-word- valid-hyphenated-word") == 0
    assert candidate(sentence = "valid-word word-with-hyphen-") == 1
    assert candidate(sentence = "word-with-hyphen-and-punctuation! word-with-hyphen-and-punctuation!") == 0
    assert candidate(sentence = "single-letter a valid-word") == 3
    assert candidate(sentence = "valid-word-with-hyphen-and-punctuation,") == 0
    assert candidate(sentence = "word-with-hyphen-and-punctuation.") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word!") == 1
    assert candidate(sentence = "end! punctuation") == 2
    assert candidate(sentence = "word-with-digit-at-end1") == 0
    assert candidate(sentence = "hyphenated-word-") == 0
    assert candidate(sentence = "valid-word,") == 1
    assert candidate(sentence = "-word-with-hyphen") == 0
    assert candidate(sentence = "only-allowed-here") == 0
    assert candidate(sentence = "word-with-digit-in-hyphen-1-word") == 0
    assert candidate(sentence = "mixed-case Words Are Invalid") == 4
    assert candidate(sentence = "-leading-hyphen") == 0
    assert candidate(sentence = "word-with-punctuation!at!the!end") == 0
    assert candidate(sentence = "validwordwithmultiplepunctuations!!!") == 0
    assert candidate(sentence = "valid-word word-with-hyphen") == 1
    assert candidate(sentence = "word-with-digit1-and-punctuation,") == 0
    assert candidate(sentence = "word-with-hyphen123") == 0
    assert candidate(sentence = "word-with-punctuation!at!end") == 0
    assert candidate(sentence = "word-hyphenated word- word. word?") == 3
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123") == 1
    assert candidate(sentence = "word-with-digit-at-end1,") == 0
    assert candidate(sentence = "word word- word! word?") == 3
    assert candidate(sentence = "valid-word,another-valid-word") == 0
    assert candidate(sentence = "trailing-punctuations,, are! invalid") == 2
    assert candidate(sentence = "word-with-punctuation!and-more") == 0
    assert candidate(sentence = "123abc and abc123 are invalid") == 3
    assert candidate(sentence = "word-with-digit-and-hyphen--b") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-b-1") == 0
    assert candidate(sentence = "valid-word! valid-word, valid-word.") == 3
    assert candidate(sentence = "no-hyphens allowed") == 2
    assert candidate(sentence = "word-with-digit-and-punctuation-1!") == 0
    assert candidate(sentence = "multiple    spaces    between words") == 4
    assert candidate(sentence = "triple-hyphen---word") == 0
    assert candidate(sentence = "punctuation,,comma and space") == 2
    assert candidate(sentence = "valid-word-2!") == 0
    assert candidate(sentence = "word-with-digit1-and-hyphen-b") == 0
    assert candidate(sentence = "valid-hyphen-word word- word") == 1
    assert candidate(sentence = "word- word- word- word.") == 1
    assert candidate(sentence = "word!!") == 0
    assert candidate(sentence = "trailing-hyphen-") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@") == 1
    assert candidate(sentence = "word- word- word- word") == 1
    assert candidate(sentence = "word-!!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-123") == 1
    assert candidate(sentence = "word-with-digit-and-punctuation1!") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#") == 1
    assert candidate(sentence = "word-with-multiple-punctuations!!!") == 0
    assert candidate(sentence = "word-with-punctuations!.") == 0
    assert candidate(sentence = "word1- word2- word3- word4-") == 0
    assert candidate(sentence = "multiple--hyphens-are!invalid") == 0
    assert candidate(sentence = "word-hyphenated-word- word- word. word-123@?!#abc-def,word@?!#abc-def,word@?!#abc123") == 1
    assert candidate(sentence = "valid-word- valid-word- valid-word-") == 0
    assert candidate(sentence = "valid-word-with-punctuation-at-end.") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen1-b") == 0
    assert candidate(sentence = "multi-hyphen-usage-is-not-allowed") == 0
    assert candidate(sentence = "word-with! punctuation") == 2
    assert candidate(sentence = "valid-word valid-word valid-word") == 3
    assert candidate(sentence = "valid-word-1 valid-word-2 valid-word-3") == 0
    assert candidate(sentence = "word-with-punctuations,word-with-punctuations,word-with-punctuations,word-with-punctuations!") == 0
    assert candidate(sentence = "word-with-digit-in-hyphen-word-1") == 0
    assert candidate(sentence = "word-") == 0
    assert candidate(sentence = "word-with-digit-and-hyphen-1-b") == 0
    assert candidate(sentence = "valid,word valid.word valid-word!") == 1


