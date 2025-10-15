def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(title = "ai and ml") == "ai And ml"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "ai and ml") == "ai And ml": {e}')
    
    total += 1
    try:
        result = candidate(title = "First leTTeR of EACH Word") == "First Letter of Each Word"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "First leTTeR of EACH Word") == "First Letter of Each Word": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHis iS a tEsT") == "This is a Test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHis iS a tEsT") == "This is a Test": {e}')
    
    total += 1
    try:
        result = candidate(title = "a b c") == "a b c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a b c") == "a b c": {e}')
    
    total += 1
    try:
        result = candidate(title = "HELLO WORLD") == "Hello World"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "HELLO WORLD") == "Hello World": {e}')
    
    total += 1
    try:
        result = candidate(title = "a b c d e f g") == "a b c d e f g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a b c d e f g") == "a b c d e f g": {e}')
    
    total += 1
    try:
        result = candidate(title = "sMaLl wOrDs") == "Small Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "sMaLl wOrDs") == "Small Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "mY nAmE is Qwen") == "my Name is Qwen"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "mY nAmE is Qwen") == "my Name is Qwen": {e}')
    
    total += 1
    try:
        result = candidate(title = "abc") == "Abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "abc") == "Abc": {e}')
    
    total += 1
    try:
        result = candidate(title = "mY sOLution IS Awesome") == "my Solution is Awesome"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "mY sOLution IS Awesome") == "my Solution is Awesome": {e}')
    
    total += 1
    try:
        result = candidate(title = "ab") == "ab"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "ab") == "ab": {e}')
    
    total += 1
    try:
        result = candidate(title = "Python Programming") == "Python Programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Python Programming") == "Python Programming": {e}')
    
    total += 1
    try:
        result = candidate(title = "this is a test") == "This is a Test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "this is a test") == "This is a Test": {e}')
    
    total += 1
    try:
        result = candidate(title = "i lOve leetcode") == "i Love Leetcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "i lOve leetcode") == "i Love Leetcode": {e}')
    
    total += 1
    try:
        result = candidate(title = "mY NaMe Is Qwen") == "my Name is Qwen"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "mY NaMe Is Qwen") == "my Name is Qwen": {e}')
    
    total += 1
    try:
        result = candidate(title = "capiTalIze tHe titLe") == "Capitalize The Title"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "capiTalIze tHe titLe") == "Capitalize The Title": {e}')
    
    total += 1
    try:
        result = candidate(title = "Alibaba Cloud") == "Alibaba Cloud"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Alibaba Cloud") == "Alibaba Cloud": {e}')
    
    total += 1
    try:
        result = candidate(title = "machine learning") == "Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "machine learning") == "Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHis is a TeSt") == "This is a Test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHis is a TeSt") == "This is a Test": {e}')
    
    total += 1
    try:
        result = candidate(title = "a") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a") == "a": {e}')
    
    total += 1
    try:
        result = candidate(title = "hello world") == "Hello World"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "hello world") == "Hello World": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHis is A tEsT cASE") == "This is a Test Case"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHis is A tEsT cASE") == "This is a Test Case": {e}')
    
    total += 1
    try:
        result = candidate(title = "data science") == "Data Science"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data science") == "Data Science": {e}')
    
    total += 1
    try:
        result = candidate(title = "data science and machine learning") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data science and machine learning") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "the quick") == "The Quick"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "the quick") == "The Quick": {e}')
    
    total += 1
    try:
        result = candidate(title = "tiny a big BIGGEST") == "Tiny a Big Biggest"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tiny a big BIGGEST") == "Tiny a Big Biggest": {e}')
    
    total += 1
    try:
        result = candidate(title = "advanced DATABASE MANAGEMENT SYSTEM") == "Advanced Database Management System"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "advanced DATABASE MANAGEMENT SYSTEM") == "Advanced Database Management System": {e}')
    
    total += 1
    try:
        result = candidate(title = "FLASK and DJANGO web FRAMEWORKS") == "Flask And Django Web Frameworks"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "FLASK and DJANGO web FRAMEWORKS") == "Flask And Django Web Frameworks": {e}')
    
    total += 1
    try:
        result = candidate(title = "sINGLEcHaRaCters AND twOCHaRaCters") == "Singlecharacters And Twocharacters"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "sINGLEcHaRaCters AND twOCHaRaCters") == "Singlecharacters And Twocharacters": {e}')
    
    total += 1
    try:
        result = candidate(title = "PYTHON pROGRAMMING") == "Python Programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "PYTHON pROGRAMMING") == "Python Programming": {e}')
    
    total += 1
    try:
        result = candidate(title = "pyThOn cOdInG chAlLenge") == "Python Coding Challenge"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "pyThOn cOdInG chAlLenge") == "Python Coding Challenge": {e}')
    
    total += 1
    try:
        result = candidate(title = "data sCience and MaChine LeArning") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data sCience and MaChine LeArning") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "PYTHON programming LANGUAGE") == "Python Programming Language"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "PYTHON programming LANGUAGE") == "Python Programming Language": {e}')
    
    total += 1
    try:
        result = candidate(title = "DESIGN PATTERNS in software ENGINEERING") == "Design Patterns in Software Engineering"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "DESIGN PATTERNS in software ENGINEERING") == "Design Patterns in Software Engineering": {e}')
    
    total += 1
    try:
        result = candidate(title = "lowercase with small words like a and the") == "Lowercase With Small Words Like a And The"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "lowercase with small words like a and the") == "Lowercase With Small Words Like a And The": {e}')
    
    total += 1
    try:
        result = candidate(title = "wHy cApItAlIzE sOmE wOrDs") == "Why Capitalize Some Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wHy cApItAlIzE sOmE wOrDs") == "Why Capitalize Some Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "data sCience and MaChInE lEaRnInG") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data sCience and MaChInE lEaRnInG") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "WEB DEVELOPMENT essentials") == "Web Development Essentials"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "WEB DEVELOPMENT essentials") == "Web Development Essentials": {e}')
    
    total += 1
    try:
        result = candidate(title = "an") == "an"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "an") == "an": {e}')
    
    total += 1
    try:
        result = candidate(title = "Data Science and Machine Learning") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Data Science and Machine Learning") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "INformation TECHNOLOGY") == "Information Technology"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "INformation TECHNOLOGY") == "Information Technology": {e}')
    
    total += 1
    try:
        result = candidate(title = "cryptography and SECURITY") == "Cryptography And Security"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "cryptography and SECURITY") == "Cryptography And Security": {e}')
    
    total += 1
    try:
        result = candidate(title = "UPPER lower CASE") == "Upper Lower Case"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "UPPER lower CASE") == "Upper Lower Case": {e}')
    
    total += 1
    try:
        result = candidate(title = "SOFTWARE ENGINEERING principles") == "Software Engineering Principles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "SOFTWARE ENGINEERING principles") == "Software Engineering Principles": {e}')
    
    total += 1
    try:
        result = candidate(title = "LONGEST wORD") == "Longest Word"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "LONGEST wORD") == "Longest Word": {e}')
    
    total += 1
    try:
        result = candidate(title = "pYtHoN pRoGrAmMiNg") == "Python Programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "pYtHoN pRoGrAmMiNg") == "Python Programming": {e}')
    
    total += 1
    try:
        result = candidate(title = "multiple     spaces   here") == "Multiple Spaces Here"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "multiple     spaces   here") == "Multiple Spaces Here": {e}')
    
    total += 1
    try:
        result = candidate(title = "sInGlE") == "Single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "sInGlE") == "Single": {e}')
    
    total += 1
    try:
        result = candidate(title = "openai gpt four") == "Openai Gpt Four"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "openai gpt four") == "Openai Gpt Four": {e}')
    
    total += 1
    try:
        result = candidate(title = "user INTERFACE and user EXPERIENCE") == "User Interface And User Experience"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "user INTERFACE and user EXPERIENCE") == "User Interface And User Experience": {e}')
    
    total += 1
    try:
        result = candidate(title = "VIRTUALIZATION technology") == "Virtualization Technology"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "VIRTUALIZATION technology") == "Virtualization Technology": {e}')
    
    total += 1
    try:
        result = candidate(title = "in the land OF wonder AND magic") == "in The Land of Wonder And Magic"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "in the land OF wonder AND magic") == "in The Land of Wonder And Magic": {e}')
    
    total += 1
    try:
        result = candidate(title = "CoMpLeX wOrDs LiKe SuPeRcAlIfR aNd qUiXoTtIc") == "Complex Words Like Supercalifr And Quixottic"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "CoMpLeX wOrDs LiKe SuPeRcAlIfR aNd qUiXoTtIc") == "Complex Words Like Supercalifr And Quixottic": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHis is A tEsT String") == "This is a Test String"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHis is A tEsT String") == "This is a Test String": {e}')
    
    total += 1
    try:
        result = candidate(title = "INTERNET of THINGS iot") == "Internet of Things Iot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "INTERNET of THINGS iot") == "Internet of Things Iot": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHiS is a sHoRt TeSt") == "This is a Short Test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHiS is a sHoRt TeSt") == "This is a Short Test": {e}')
    
    total += 1
    try:
        result = candidate(title = "python programming LANGUAGE") == "Python Programming Language"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "python programming LANGUAGE") == "Python Programming Language": {e}')
    
    total += 1
    try:
        result = candidate(title = "a quick brown fox jumps over the lazy dog") == "a Quick Brown Fox Jumps Over The Lazy Dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a quick brown fox jumps over the lazy dog") == "a Quick Brown Fox Jumps Over The Lazy Dog": {e}')
    
    total += 1
    try:
        result = candidate(title = "UPPERCASE lowercase MIXEDcase") == "Uppercase Lowercase Mixedcase"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "UPPERCASE lowercase MIXEDcase") == "Uppercase Lowercase Mixedcase": {e}')
    
    total += 1
    try:
        result = candidate(title = "a SHORT story IN a SMALL town") == "a Short Story in a Small Town"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a SHORT story IN a SMALL town") == "a Short Story in a Small Town": {e}')
    
    total += 1
    try:
        result = candidate(title = "single") == "Single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "single") == "Single": {e}')
    
    total += 1
    try:
        result = candidate(title = "data STRUCTURE and ALGORITHMS") == "Data Structure And Algorithms"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data STRUCTURE and ALGORITHMS") == "Data Structure And Algorithms": {e}')
    
    total += 1
    try:
        result = candidate(title = "this is a test STRING with MIXED CASE") == "This is a Test String With Mixed Case"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "this is a test STRING with MIXED CASE") == "This is a Test String With Mixed Case": {e}')
    
    total += 1
    try:
        result = candidate(title = "to be or not to be") == "to be or Not to be"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "to be or not to be") == "to be or Not to be": {e}')
    
    total += 1
    try:
        result = candidate(title = "wordlengthsofthreetwoone") == "Wordlengthsofthreetwoone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wordlengthsofthreetwoone") == "Wordlengthsofthreetwoone": {e}')
    
    total += 1
    try:
        result = candidate(title = "wiTh lOnG wOrDs liKe suPercalifragilisticexpialidocious") == "With Long Words Like Supercalifragilisticexpialidocious"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wiTh lOnG wOrDs liKe suPercalifragilisticexpialidocious") == "With Long Words Like Supercalifragilisticexpialidocious": {e}')
    
    total += 1
    try:
        result = candidate(title = "this is a longer sentence with more words to test the function") == "This is a Longer Sentence With More Words to Test The Function"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "this is a longer sentence with more words to test the function") == "This is a Longer Sentence With More Words to Test The Function": {e}')
    
    total += 1
    try:
        result = candidate(title = "very Very LONG title with MANY Words indeed") == "Very Very Long Title With Many Words Indeed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "very Very LONG title with MANY Words indeed") == "Very Very Long Title With Many Words Indeed": {e}')
    
    total += 1
    try:
        result = candidate(title = "Algorithms and DATA structures") == "Algorithms And Data Structures"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Algorithms and DATA structures") == "Algorithms And Data Structures": {e}')
    
    total += 1
    try:
        result = candidate(title = "tEsTiNg WoRdS wItH vArIoUs lEnGtHs") == "Testing Words With Various Lengths"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tEsTiNg WoRdS wItH vArIoUs lEnGtHs") == "Testing Words With Various Lengths": {e}')
    
    total += 1
    try:
        result = candidate(title = "a quick brown fox") == "a Quick Brown Fox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a quick brown fox") == "a Quick Brown Fox": {e}')
    
    total += 1
    try:
        result = candidate(title = "tExT pRoCeSsInG") == "Text Processing"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tExT pRoCeSsInG") == "Text Processing": {e}')
    
    total += 1
    try:
        result = candidate(title = "the quick BROWN fox JUMPS OVER the LAZY DOG") == "The Quick Brown Fox Jumps Over The Lazy Dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "the quick BROWN fox JUMPS OVER the LAZY DOG") == "The Quick Brown Fox Jumps Over The Lazy Dog": {e}')
    
    total += 1
    try:
        result = candidate(title = "algorithms and data structures") == "Algorithms And Data Structures"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "algorithms and data structures") == "Algorithms And Data Structures": {e}')
    
    total += 1
    try:
        result = candidate(title = "a short AND a LONG word") == "a Short And a Long Word"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a short AND a LONG word") == "a Short And a Long Word": {e}')
    
    total += 1
    try:
        result = candidate(title = "AlGoRiThM aNd dAtA sTrUcTuRe") == "Algorithm And Data Structure"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "AlGoRiThM aNd dAtA sTrUcTuRe") == "Algorithm And Data Structure": {e}')
    
    total += 1
    try:
        result = candidate(title = "data sCIENCE and maCHine LEARNING") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data sCIENCE and maCHine LEARNING") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "cOnsIdEr tHiS eXaMpLe") == "Consider This Example"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "cOnsIdEr tHiS eXaMpLe") == "Consider This Example": {e}')
    
    total += 1
    try:
        result = candidate(title = "cloud COMPUTING") == "Cloud Computing"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "cloud COMPUTING") == "Cloud Computing": {e}')
    
    total += 1
    try:
        result = candidate(title = "fLASK aNd dJANGO") == "Flask And Django"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "fLASK aNd dJANGO") == "Flask And Django": {e}')
    
    total += 1
    try:
        result = candidate(title = "To be OR not TO be") == "to be or Not to be"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "To be OR not TO be") == "to be or Not to be": {e}')
    
    total += 1
    try:
        result = candidate(title = "multiple words of varying length and CASE") == "Multiple Words of Varying Length And Case"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "multiple words of varying length and CASE") == "Multiple Words of Varying Length And Case": {e}')
    
    total += 1
    try:
        result = candidate(title = "network SECURITY") == "Network Security"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "network SECURITY") == "Network Security": {e}')
    
    total += 1
    try:
        result = candidate(title = "programming IN python") == "Programming in Python"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "programming IN python") == "Programming in Python": {e}')
    
    total += 1
    try:
        result = candidate(title = "the QUICK brown FOX jumps OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "the QUICK brown FOX jumps OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog": {e}')
    
    total += 1
    try:
        result = candidate(title = "MiXcAsE wOrDlEnGtH") == "Mixcase Wordlength"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "MiXcAsE wOrDlEnGtH") == "Mixcase Wordlength": {e}')
    
    total += 1
    try:
        result = candidate(title = "in") == "in"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "in") == "in": {e}')
    
    total += 1
    try:
        result = candidate(title = "wiTh grEat pOwEr cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wiTh grEat pOwEr cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility": {e}')
    
    total += 1
    try:
        result = candidate(title = "algorithms AND dataSTRUCTURES") == "Algorithms And Datastructures"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "algorithms AND dataSTRUCTURES") == "Algorithms And Datastructures": {e}')
    
    total += 1
    try:
        result = candidate(title = "wiTh gReAt pOWeR cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wiTh gReAt pOWeR cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility": {e}')
    
    total += 1
    try:
        result = candidate(title = "A B c D E F G") == "a b c d e f g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "A B c D E F G") == "a b c d e f g": {e}')
    
    total += 1
    try:
        result = candidate(title = "AI and MACHINE LEARNING") == "ai And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "AI and MACHINE LEARNING") == "ai And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "big DATA ANALYSIS") == "Big Data Analysis"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "big DATA ANALYSIS") == "Big Data Analysis": {e}')
    
    total += 1
    try:
        result = candidate(title = "mUlTiPlE sMaLl wOrDs") == "Multiple Small Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "mUlTiPlE sMaLl wOrDs") == "Multiple Small Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "LEETcode IS coOL") == "Leetcode is Cool"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "LEETcode IS coOL") == "Leetcode is Cool": {e}')
    
    total += 1
    try:
        result = candidate(title = "two Words") == "Two Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "two Words") == "Two Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "introduction to ARTIFICIAL INTELLIGENCE") == "Introduction to Artificial Intelligence"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "introduction to ARTIFICIAL INTELLIGENCE") == "Introduction to Artificial Intelligence": {e}')
    
    total += 1
    try:
        result = candidate(title = "sOlVe tHe rObOt wOrLd cHAlLeNgEs") == "Solve The Robot World Challenges"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "sOlVe tHe rObOt wOrLd cHAlLeNgEs") == "Solve The Robot World Challenges": {e}')
    
    total += 1
    try:
        result = candidate(title = "mIxEd cAsE iNpUt") == "Mixed Case Input"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "mIxEd cAsE iNpUt") == "Mixed Case Input": {e}')
    
    total += 1
    try:
        result = candidate(title = "EACH WORD IN THE TITLE") == "Each Word in The Title"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "EACH WORD IN THE TITLE") == "Each Word in The Title": {e}')
    
    total += 1
    try:
        result = candidate(title = "programming in PYTHON") == "Programming in Python"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "programming in PYTHON") == "Programming in Python": {e}')
    
    total += 1
    try:
        result = candidate(title = "one two three four five six seven eight nine ten") == "One Two Three Four Five Six Seven Eight Nine Ten"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "one two three four five six seven eight nine ten") == "One Two Three Four Five Six Seven Eight Nine Ten": {e}')
    
    total += 1
    try:
        result = candidate(title = "very very LONG words in THIS sentence") == "Very Very Long Words in This Sentence"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "very very LONG words in THIS sentence") == "Very Very Long Words in This Sentence": {e}')
    
    total += 1
    try:
        result = candidate(title = "leet code CHALLENGE") == "Leet Code Challenge"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "leet code CHALLENGE") == "Leet Code Challenge": {e}')
    
    total += 1
    try:
        result = candidate(title = "the") == "The"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "the") == "The": {e}')
    
    total += 1
    try:
        result = candidate(title = "double two") == "Double Two"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "double two") == "Double Two": {e}')
    
    total += 1
    try:
        result = candidate(title = "a B c D E F G") == "a b c d e f g"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a B c D E F G") == "a b c d e f g": {e}')
    
    total += 1
    try:
        result = candidate(title = "a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z": {e}')
    
    total += 1
    try:
        result = candidate(title = "in The HoLlyWoOd") == "in The Hollywood"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "in The HoLlyWoOd") == "in The Hollywood": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHis is a tEsT string") == "This is a Test String"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHis is a tEsT string") == "This is a Test String": {e}')
    
    total += 1
    try:
        result = candidate(title = "MiXeD CaSe wOrDs") == "Mixed Case Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "MiXeD CaSe wOrDs") == "Mixed Case Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "multiple small words in here") == "Multiple Small Words in Here"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "multiple small words in here") == "Multiple Small Words in Here": {e}')
    
    total += 1
    try:
        result = candidate(title = "in the HEART of the CITY") == "in The Heart of The City"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "in the HEART of the CITY") == "in The Heart of The City": {e}')
    
    total += 1
    try:
        result = candidate(title = "randomly CaPiTaLiZed WoRds") == "Randomly Capitalized Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "randomly CaPiTaLiZed WoRds") == "Randomly Capitalized Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "To BE OR NOT to BE") == "to be or Not to be"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "To BE OR NOT to BE") == "to be or Not to be": {e}')
    
    total += 1
    try:
        result = candidate(title = "MiNiMaL MaXiMaL") == "Minimal Maximal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "MiNiMaL MaXiMaL") == "Minimal Maximal": {e}')
    
    total += 1
    try:
        result = candidate(title = "HELLO wORLD") == "Hello World"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "HELLO wORLD") == "Hello World": {e}')
    
    total += 1
    try:
        result = candidate(title = "THE quick BROWN fox JUMPS OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "THE quick BROWN fox JUMPS OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog": {e}')
    
    total += 1
    try:
        result = candidate(title = "data SCIENCE and MACHINE LEARNING") == "Data Science And Machine Learning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "data SCIENCE and MACHINE LEARNING") == "Data Science And Machine Learning": {e}')
    
    total += 1
    try:
        result = candidate(title = "pYthon programming lanGuage") == "Python Programming Language"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "pYthon programming lanGuage") == "Python Programming Language": {e}')
    
    total += 1
    try:
        result = candidate(title = "OpenAI GPT-4") == "Openai Gpt-4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "OpenAI GPT-4") == "Openai Gpt-4": {e}')
    
    total += 1
    try:
        result = candidate(title = "triple three words") == "Triple Three Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "triple three words") == "Triple Three Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "eNcYcLopEdIa oF pHySiCs aNd mAtHeMaTiCs") == "Encyclopedia of Physics And Mathematics"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "eNcYcLopEdIa oF pHySiCs aNd mAtHeMaTiCs") == "Encyclopedia of Physics And Mathematics": {e}')
    
    total += 1
    try:
        result = candidate(title = "a a a a a a a") == "a a a a a a a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "a a a a a a a") == "a a a a a a a": {e}')
    
    total += 1
    try:
        result = candidate(title = "openAI GPT AND machineLEARNING") == "Openai Gpt And Machinelearning"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "openAI GPT AND machineLEARNING") == "Openai Gpt And Machinelearning": {e}')
    
    total += 1
    try:
        result = candidate(title = "PYTHON programming") == "Python Programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "PYTHON programming") == "Python Programming": {e}')
    
    total += 1
    try:
        result = candidate(title = "sOFTWARE dEVELOPMENT") == "Software Development"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "sOFTWARE dEVELOPMENT") == "Software Development": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHiS iS a TeSt CaSe") == "This is a Test Case"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHiS iS a TeSt CaSe") == "This is a Test Case": {e}')
    
    total += 1
    try:
        result = candidate(title = "wEb dEveLopMeNt fOr bEgInNeRs") == "Web Development For Beginners"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "wEb dEveLopMeNt fOr bEgInNeRs") == "Web Development For Beginners": {e}')
    
    total += 1
    try:
        result = candidate(title = "one") == "One"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "one") == "One": {e}')
    
    total += 1
    try:
        result = candidate(title = "Data STRUCTURES and ALGORITHMs") == "Data Structures And Algorithms"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Data STRUCTURES and ALGORITHMs") == "Data Structures And Algorithms": {e}')
    
    total += 1
    try:
        result = candidate(title = "aBcDeFgHiJ kLmNoPqRsT") == "Abcdefghij Klmnopqrst"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "aBcDeFgHiJ kLmNoPqRsT") == "Abcdefghij Klmnopqrst": {e}')
    
    total += 1
    try:
        result = candidate(title = "Python Programming Language") == "Python Programming Language"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Python Programming Language") == "Python Programming Language": {e}')
    
    total += 1
    try:
        result = candidate(title = "blockCHAIN technology") == "Blockchain Technology"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "blockCHAIN technology") == "Blockchain Technology": {e}')
    
    total += 1
    try:
        result = candidate(title = "Python Programming Is Fun") == "Python Programming is Fun"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "Python Programming Is Fun") == "Python Programming is Fun": {e}')
    
    total += 1
    try:
        result = candidate(title = "LoNg WoRdS aNd sHoRt wOrDs") == "Long Words And Short Words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "LoNg WoRdS aNd sHoRt wOrDs") == "Long Words And Short Words": {e}')
    
    total += 1
    try:
        result = candidate(title = "tHe qUiCk bRoWn fOx") == "The Quick Brown Fox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(title = "tHe qUiCk bRoWn fOx") == "The Quick Brown Fox": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(title = "ai and ml") == "ai And ml"
    assert candidate(title = "First leTTeR of EACH Word") == "First Letter of Each Word"
    assert candidate(title = "tHis iS a tEsT") == "This is a Test"
    assert candidate(title = "a b c") == "a b c"
    assert candidate(title = "HELLO WORLD") == "Hello World"
    assert candidate(title = "a b c d e f g") == "a b c d e f g"
    assert candidate(title = "sMaLl wOrDs") == "Small Words"
    assert candidate(title = "mY nAmE is Qwen") == "my Name is Qwen"
    assert candidate(title = "abc") == "Abc"
    assert candidate(title = "mY sOLution IS Awesome") == "my Solution is Awesome"
    assert candidate(title = "ab") == "ab"
    assert candidate(title = "Python Programming") == "Python Programming"
    assert candidate(title = "this is a test") == "This is a Test"
    assert candidate(title = "i lOve leetcode") == "i Love Leetcode"
    assert candidate(title = "mY NaMe Is Qwen") == "my Name is Qwen"
    assert candidate(title = "capiTalIze tHe titLe") == "Capitalize The Title"
    assert candidate(title = "Alibaba Cloud") == "Alibaba Cloud"
    assert candidate(title = "machine learning") == "Machine Learning"
    assert candidate(title = "tHis is a TeSt") == "This is a Test"
    assert candidate(title = "a") == "a"
    assert candidate(title = "hello world") == "Hello World"
    assert candidate(title = "tHis is A tEsT cASE") == "This is a Test Case"
    assert candidate(title = "data science") == "Data Science"
    assert candidate(title = "data science and machine learning") == "Data Science And Machine Learning"
    assert candidate(title = "the quick") == "The Quick"
    assert candidate(title = "tiny a big BIGGEST") == "Tiny a Big Biggest"
    assert candidate(title = "advanced DATABASE MANAGEMENT SYSTEM") == "Advanced Database Management System"
    assert candidate(title = "FLASK and DJANGO web FRAMEWORKS") == "Flask And Django Web Frameworks"
    assert candidate(title = "sINGLEcHaRaCters AND twOCHaRaCters") == "Singlecharacters And Twocharacters"
    assert candidate(title = "PYTHON pROGRAMMING") == "Python Programming"
    assert candidate(title = "pyThOn cOdInG chAlLenge") == "Python Coding Challenge"
    assert candidate(title = "data sCience and MaChine LeArning") == "Data Science And Machine Learning"
    assert candidate(title = "PYTHON programming LANGUAGE") == "Python Programming Language"
    assert candidate(title = "DESIGN PATTERNS in software ENGINEERING") == "Design Patterns in Software Engineering"
    assert candidate(title = "lowercase with small words like a and the") == "Lowercase With Small Words Like a And The"
    assert candidate(title = "wHy cApItAlIzE sOmE wOrDs") == "Why Capitalize Some Words"
    assert candidate(title = "data sCience and MaChInE lEaRnInG") == "Data Science And Machine Learning"
    assert candidate(title = "WEB DEVELOPMENT essentials") == "Web Development Essentials"
    assert candidate(title = "an") == "an"
    assert candidate(title = "Data Science and Machine Learning") == "Data Science And Machine Learning"
    assert candidate(title = "INformation TECHNOLOGY") == "Information Technology"
    assert candidate(title = "cryptography and SECURITY") == "Cryptography And Security"
    assert candidate(title = "UPPER lower CASE") == "Upper Lower Case"
    assert candidate(title = "SOFTWARE ENGINEERING principles") == "Software Engineering Principles"
    assert candidate(title = "LONGEST wORD") == "Longest Word"
    assert candidate(title = "pYtHoN pRoGrAmMiNg") == "Python Programming"
    assert candidate(title = "multiple     spaces   here") == "Multiple Spaces Here"
    assert candidate(title = "sInGlE") == "Single"
    assert candidate(title = "openai gpt four") == "Openai Gpt Four"
    assert candidate(title = "user INTERFACE and user EXPERIENCE") == "User Interface And User Experience"
    assert candidate(title = "VIRTUALIZATION technology") == "Virtualization Technology"
    assert candidate(title = "in the land OF wonder AND magic") == "in The Land of Wonder And Magic"
    assert candidate(title = "CoMpLeX wOrDs LiKe SuPeRcAlIfR aNd qUiXoTtIc") == "Complex Words Like Supercalifr And Quixottic"
    assert candidate(title = "tHis is A tEsT String") == "This is a Test String"
    assert candidate(title = "INTERNET of THINGS iot") == "Internet of Things Iot"
    assert candidate(title = "tHiS is a sHoRt TeSt") == "This is a Short Test"
    assert candidate(title = "python programming LANGUAGE") == "Python Programming Language"
    assert candidate(title = "a quick brown fox jumps over the lazy dog") == "a Quick Brown Fox Jumps Over The Lazy Dog"
    assert candidate(title = "UPPERCASE lowercase MIXEDcase") == "Uppercase Lowercase Mixedcase"
    assert candidate(title = "a SHORT story IN a SMALL town") == "a Short Story in a Small Town"
    assert candidate(title = "single") == "Single"
    assert candidate(title = "data STRUCTURE and ALGORITHMS") == "Data Structure And Algorithms"
    assert candidate(title = "this is a test STRING with MIXED CASE") == "This is a Test String With Mixed Case"
    assert candidate(title = "to be or not to be") == "to be or Not to be"
    assert candidate(title = "wordlengthsofthreetwoone") == "Wordlengthsofthreetwoone"
    assert candidate(title = "wiTh lOnG wOrDs liKe suPercalifragilisticexpialidocious") == "With Long Words Like Supercalifragilisticexpialidocious"
    assert candidate(title = "this is a longer sentence with more words to test the function") == "This is a Longer Sentence With More Words to Test The Function"
    assert candidate(title = "very Very LONG title with MANY Words indeed") == "Very Very Long Title With Many Words Indeed"
    assert candidate(title = "Algorithms and DATA structures") == "Algorithms And Data Structures"
    assert candidate(title = "tEsTiNg WoRdS wItH vArIoUs lEnGtHs") == "Testing Words With Various Lengths"
    assert candidate(title = "a quick brown fox") == "a Quick Brown Fox"
    assert candidate(title = "tExT pRoCeSsInG") == "Text Processing"
    assert candidate(title = "the quick BROWN fox JUMPS OVER the LAZY DOG") == "The Quick Brown Fox Jumps Over The Lazy Dog"
    assert candidate(title = "algorithms and data structures") == "Algorithms And Data Structures"
    assert candidate(title = "a short AND a LONG word") == "a Short And a Long Word"
    assert candidate(title = "AlGoRiThM aNd dAtA sTrUcTuRe") == "Algorithm And Data Structure"
    assert candidate(title = "data sCIENCE and maCHine LEARNING") == "Data Science And Machine Learning"
    assert candidate(title = "cOnsIdEr tHiS eXaMpLe") == "Consider This Example"
    assert candidate(title = "cloud COMPUTING") == "Cloud Computing"
    assert candidate(title = "fLASK aNd dJANGO") == "Flask And Django"
    assert candidate(title = "To be OR not TO be") == "to be or Not to be"
    assert candidate(title = "multiple words of varying length and CASE") == "Multiple Words of Varying Length And Case"
    assert candidate(title = "network SECURITY") == "Network Security"
    assert candidate(title = "programming IN python") == "Programming in Python"
    assert candidate(title = "the QUICK brown FOX jumps OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog"
    assert candidate(title = "MiXcAsE wOrDlEnGtH") == "Mixcase Wordlength"
    assert candidate(title = "in") == "in"
    assert candidate(title = "wiTh grEat pOwEr cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility"
    assert candidate(title = "algorithms AND dataSTRUCTURES") == "Algorithms And Datastructures"
    assert candidate(title = "wiTh gReAt pOWeR cOmEs gReAt rEsPoNsIbIlItY") == "With Great Power Comes Great Responsibility"
    assert candidate(title = "A B c D E F G") == "a b c d e f g"
    assert candidate(title = "AI and MACHINE LEARNING") == "ai And Machine Learning"
    assert candidate(title = "big DATA ANALYSIS") == "Big Data Analysis"
    assert candidate(title = "mUlTiPlE sMaLl wOrDs") == "Multiple Small Words"
    assert candidate(title = "LEETcode IS coOL") == "Leetcode is Cool"
    assert candidate(title = "two Words") == "Two Words"
    assert candidate(title = "introduction to ARTIFICIAL INTELLIGENCE") == "Introduction to Artificial Intelligence"
    assert candidate(title = "sOlVe tHe rObOt wOrLd cHAlLeNgEs") == "Solve The Robot World Challenges"
    assert candidate(title = "mIxEd cAsE iNpUt") == "Mixed Case Input"
    assert candidate(title = "EACH WORD IN THE TITLE") == "Each Word in The Title"
    assert candidate(title = "programming in PYTHON") == "Programming in Python"
    assert candidate(title = "one two three four five six seven eight nine ten") == "One Two Three Four Five Six Seven Eight Nine Ten"
    assert candidate(title = "very very LONG words in THIS sentence") == "Very Very Long Words in This Sentence"
    assert candidate(title = "leet code CHALLENGE") == "Leet Code Challenge"
    assert candidate(title = "the") == "The"
    assert candidate(title = "double two") == "Double Two"
    assert candidate(title = "a B c D E F G") == "a b c d e f g"
    assert candidate(title = "a b c d e f g h i j k l m n o p q r s t u v w x y z") == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert candidate(title = "in The HoLlyWoOd") == "in The Hollywood"
    assert candidate(title = "tHis is a tEsT string") == "This is a Test String"
    assert candidate(title = "MiXeD CaSe wOrDs") == "Mixed Case Words"
    assert candidate(title = "multiple small words in here") == "Multiple Small Words in Here"
    assert candidate(title = "in the HEART of the CITY") == "in The Heart of The City"
    assert candidate(title = "randomly CaPiTaLiZed WoRds") == "Randomly Capitalized Words"
    assert candidate(title = "To BE OR NOT to BE") == "to be or Not to be"
    assert candidate(title = "MiNiMaL MaXiMaL") == "Minimal Maximal"
    assert candidate(title = "HELLO wORLD") == "Hello World"
    assert candidate(title = "THE quick BROWN fox JUMPS OVER the LAZY dog") == "The Quick Brown Fox Jumps Over The Lazy Dog"
    assert candidate(title = "data SCIENCE and MACHINE LEARNING") == "Data Science And Machine Learning"
    assert candidate(title = "pYthon programming lanGuage") == "Python Programming Language"
    assert candidate(title = "OpenAI GPT-4") == "Openai Gpt-4"
    assert candidate(title = "triple three words") == "Triple Three Words"
    assert candidate(title = "eNcYcLopEdIa oF pHySiCs aNd mAtHeMaTiCs") == "Encyclopedia of Physics And Mathematics"
    assert candidate(title = "a a a a a a a") == "a a a a a a a"
    assert candidate(title = "openAI GPT AND machineLEARNING") == "Openai Gpt And Machinelearning"
    assert candidate(title = "PYTHON programming") == "Python Programming"
    assert candidate(title = "sOFTWARE dEVELOPMENT") == "Software Development"
    assert candidate(title = "tHiS iS a TeSt CaSe") == "This is a Test Case"
    assert candidate(title = "wEb dEveLopMeNt fOr bEgInNeRs") == "Web Development For Beginners"
    assert candidate(title = "one") == "One"
    assert candidate(title = "Data STRUCTURES and ALGORITHMs") == "Data Structures And Algorithms"
    assert candidate(title = "aBcDeFgHiJ kLmNoPqRsT") == "Abcdefghij Klmnopqrst"
    assert candidate(title = "Python Programming Language") == "Python Programming Language"
    assert candidate(title = "blockCHAIN technology") == "Blockchain Technology"
    assert candidate(title = "Python Programming Is Fun") == "Python Programming is Fun"
    assert candidate(title = "LoNg WoRdS aNd sHoRt wOrDs") == "Long Words And Short Words"
    assert candidate(title = "tHe qUiCk bRoWn fOx") == "The Quick Brown Fox"


