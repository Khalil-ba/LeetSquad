def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "I love to code",k = 3) == "I love to"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I love to code",k = 3) == "I love to": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python is great",k = 2) == "Python is"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python is great",k = 2) == "Python is": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python programming is fun",k = 2) == "Python programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python programming is fun",k = 2) == "Python programming": {e}')
    
    total += 1
    try:
        result = candidate(s = "A quick brown fox jumps over the lazy dog",k = 3) == "A quick brown"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A quick brown fox jumps over the lazy dog",k = 3) == "A quick brown": {e}')
    
    total += 1
    try:
        result = candidate(s = "I love programming in Python",k = 3) == "I love programming"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I love programming in Python",k = 3) == "I love programming": {e}')
    
    total += 1
    try:
        result = candidate(s = "Hello how are you Contestant",k = 4) == "Hello how are you"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello how are you Contestant",k = 4) == "Hello how are you": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python is a great programming language",k = 2) == "Python is"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python is a great programming language",k = 2) == "Python is": {e}')
    
    total += 1
    try:
        result = candidate(s = "chopper is not a tanuki",k = 5) == "chopper is not a tanuki"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "chopper is not a tanuki",k = 5) == "chopper is not a tanuki": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python is fun",k = 2) == "Python is"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python is fun",k = 2) == "Python is": {e}')
    
    total += 1
    try:
        result = candidate(s = "I love programming",k = 1) == "I"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I love programming",k = 1) == "I": {e}')
    
    total += 1
    try:
        result = candidate(s = "What is the solution to this problem",k = 4) == "What is the solution"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "What is the solution to this problem",k = 4) == "What is the solution": {e}')
    
    total += 1
    try:
        result = candidate(s = "I love solving problems",k = 3) == "I love solving"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "I love solving problems",k = 3) == "I love solving": {e}')
    
    total += 1
    try:
        result = candidate(s = "It does not matter how slowly you go as long as you do not stop",k = 9) == "It does not matter how slowly you go as"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "It does not matter how slowly you go as long as you do not stop",k = 9) == "It does not matter how slowly you go as": {e}')
    
    total += 1
    try:
        result = candidate(s = "The road to success is always under construction",k = 7) == "The road to success is always under"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The road to success is always under construction",k = 7) == "The road to success is always under": {e}')
    
    total += 1
    try:
        result = candidate(s = "The best way to predict your future is to create it",k = 8) == "The best way to predict your future is"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The best way to predict your future is to create it",k = 8) == "The best way to predict your future is": {e}')
    
    total += 1
    try:
        result = candidate(s = "This is a test sentence to check the functionality of the code",k = 9) == "This is a test sentence to check the functionality"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "This is a test sentence to check the functionality of the code",k = 9) == "This is a test sentence to check the functionality": {e}')
    
    total += 1
    try:
        result = candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 5) == "a b c d e"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 5) == "a b c d e": {e}')
    
    total += 1
    try:
        result = candidate(s = "In computer science, the art of programming is the science of abstraction",k = 8) == "In computer science, the art of programming is"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "In computer science, the art of programming is the science of abstraction",k = 8) == "In computer science, the art of programming is": {e}')
    
    total += 1
    try:
        result = candidate(s = "A journey of a thousand miles begins with a single step",k = 8) == "A journey of a thousand miles begins with"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A journey of a thousand miles begins with a single step",k = 8) == "A journey of a thousand miles begins with": {e}')
    
    total += 1
    try:
        result = candidate(s = "Believe you can and you're halfway there",k = 5) == "Believe you can and you're"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Believe you can and you're halfway there",k = 5) == "Believe you can and you're": {e}')
    
    total += 1
    try:
        result = candidate(s = "Keep it simple stupid",k = 5) == "Keep it simple stupid"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Keep it simple stupid",k = 5) == "Keep it simple stupid": {e}')
    
    total += 1
    try:
        result = candidate(s = "To be or not to be that is the question",k = 10) == "To be or not to be that is the question"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "To be or not to be that is the question",k = 10) == "To be or not to be that is the question": {e}')
    
    total += 1
    try:
        result = candidate(s = "May the Force be with you young Jedi",k = 6) == "May the Force be with you"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "May the Force be with you young Jedi",k = 6) == "May the Force be with you": {e}')
    
    total += 1
    try:
        result = candidate(s = "Short sentence",k = 2) == "Short sentence"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Short sentence",k = 2) == "Short sentence": {e}')
    
    total += 1
    try:
        result = candidate(s = "The only way to do great work is to love what you do",k = 7) == "The only way to do great work"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The only way to do great work is to love what you do",k = 7) == "The only way to do great work": {e}')
    
    total += 1
    try:
        result = candidate(s = "Honesty is the best policy",k = 4) == "Honesty is the best"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Honesty is the best policy",k = 4) == "Honesty is the best": {e}')
    
    total += 1
    try:
        result = candidate(s = "In the middle of difficulty lies opportunity",k = 4) == "In the middle of"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "In the middle of difficulty lies opportunity",k = 4) == "In the middle of": {e}')
    
    total += 1
    try:
        result = candidate(s = "Natural language processing has become a cornerstone of modern technology",k = 9) == "Natural language processing has become a cornerstone of modern"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Natural language processing has become a cornerstone of modern technology",k = 9) == "Natural language processing has become a cornerstone of modern": {e}')
    
    total += 1
    try:
        result = candidate(s = "One two three four five six seven eight nine ten",k = 10) == "One two three four five six seven eight nine ten"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "One two three four five six seven eight nine ten",k = 10) == "One two three four five six seven eight nine ten": {e}')
    
    total += 1
    try:
        result = candidate(s = "You miss 100 percent of the shots you don t take Wayne Gretzky",k = 11) == "You miss 100 percent of the shots you don t take"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "You miss 100 percent of the shots you don t take Wayne Gretzky",k = 11) == "You miss 100 percent of the shots you don t take": {e}')
    
    total += 1
    try:
        result = candidate(s = "OpenAI GPT-4 can generate human-like text based on the input it receives",k = 7) == "OpenAI GPT-4 can generate human-like text based"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OpenAI GPT-4 can generate human-like text based on the input it receives",k = 7) == "OpenAI GPT-4 can generate human-like text based": {e}')
    
    total += 1
    try:
        result = candidate(s = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen",k = 10) == "One two three four five six seven eight nine ten"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen",k = 10) == "One two three four five six seven eight nine ten": {e}')
    
    total += 1
    try:
        result = candidate(s = "What you get by achieving your goals is not as important as what you become by achieving your goals",k = 12) == "What you get by achieving your goals is not as important as"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "What you get by achieving your goals is not as important as what you become by achieving your goals",k = 12) == "What you get by achieving your goals is not as important as": {e}')
    
    total += 1
    try:
        result = candidate(s = "Debugging is twice as hard as writing the code in the first place",k = 7) == "Debugging is twice as hard as writing"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Debugging is twice as hard as writing the code in the first place",k = 7) == "Debugging is twice as hard as writing": {e}')
    
    total += 1
    try:
        result = candidate(s = "Python programming is fun and challenging",k = 10) == "Python programming is fun and challenging"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Python programming is fun and challenging",k = 10) == "Python programming is fun and challenging": {e}')
    
    total += 1
    try:
        result = candidate(s = "A journey of a thousand miles begins with a single step",k = 7) == "A journey of a thousand miles begins"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A journey of a thousand miles begins with a single step",k = 7) == "A journey of a thousand miles begins": {e}')
    
    total += 1
    try:
        result = candidate(s = "Success is not final success is to be able to continue to try",k = 8) == "Success is not final success is to be"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Success is not final success is to be able to continue to try",k = 8) == "Success is not final success is to be": {e}')
    
    total += 1
    try:
        result = candidate(s = "OneWordOnly",k = 1) == "OneWordOnly"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "OneWordOnly",k = 1) == "OneWordOnly": {e}')
    
    total += 1
    try:
        result = candidate(s = "Data Science and Machine Learning",k = 3) == "Data Science and"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Data Science and Machine Learning",k = 3) == "Data Science and": {e}')
    
    total += 1
    try:
        result = candidate(s = "Life is what happens when you are busy making other plans",k = 7) == "Life is what happens when you are"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Life is what happens when you are busy making other plans",k = 7) == "Life is what happens when you are": {e}')
    
    total += 1
    try:
        result = candidate(s = "The early morning sun is warm and welcoming",k = 7) == "The early morning sun is warm and"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The early morning sun is warm and welcoming",k = 7) == "The early morning sun is warm and": {e}')
    
    total += 1
    try:
        result = candidate(s = "To be or not to be that is the question",k = 7) == "To be or not to be that"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "To be or not to be that is the question",k = 7) == "To be or not to be that": {e}')
    
    total += 1
    try:
        result = candidate(s = "Short but tricky",k = 2) == "Short but"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Short but tricky",k = 2) == "Short but": {e}')
    
    total += 1
    try:
        result = candidate(s = "The early bird catches the worm",k = 5) == "The early bird catches the"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The early bird catches the worm",k = 5) == "The early bird catches the": {e}')
    
    total += 1
    try:
        result = candidate(s = "Final complex sentence with multiple words indeed",k = 7) == "Final complex sentence with multiple words indeed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Final complex sentence with multiple words indeed",k = 7) == "Final complex sentence with multiple words indeed": {e}')
    
    total += 1
    try:
        result = candidate(s = "The best way to predict the future is to invent it",k = 9) == "The best way to predict the future is to"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The best way to predict the future is to invent it",k = 9) == "The best way to predict the future is to": {e}')
    
    total += 1
    try:
        result = candidate(s = "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences",k = 1) == "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences",k = 1) == "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences": {e}')
    
    total += 1
    try:
        result = candidate(s = "Do not judge a book by its cover",k = 7) == "Do not judge a book by its"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Do not judge a book by its cover",k = 7) == "Do not judge a book by its": {e}')
    
    total += 1
    try:
        result = candidate(s = "All that glitters is not gold only the good do well by gold",k = 9) == "All that glitters is not gold only the good"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "All that glitters is not gold only the good do well by gold",k = 9) == "All that glitters is not gold only the good": {e}')
    
    total += 1
    try:
        result = candidate(s = "All that glitters is not gold",k = 5) == "All that glitters is not"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "All that glitters is not gold",k = 5) == "All that glitters is not": {e}')
    
    total += 1
    try:
        result = candidate(s = "To be or not to be that is the question",k = 5) == "To be or not to"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "To be or not to be that is the question",k = 5) == "To be or not to": {e}')
    
    total += 1
    try:
        result = candidate(s = "Edge case with k equal to the number of words here",k = 9) == "Edge case with k equal to the number of"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Edge case with k equal to the number of words here",k = 9) == "Edge case with k equal to the number of": {e}')
    
    total += 1
    try:
        result = candidate(s = "Multiple words with mixed CASE Words",k = 4) == "Multiple words with mixed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Multiple words with mixed CASE Words",k = 4) == "Multiple words with mixed": {e}')
    
    total += 1
    try:
        result = candidate(s = "Programming in Python is both fun and educational",k = 6) == "Programming in Python is both fun"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Programming in Python is both fun and educational",k = 6) == "Programming in Python is both fun": {e}')
    
    total += 1
    try:
        result = candidate(s = "A journey of a thousand miles begins with a single step",k = 6) == "A journey of a thousand miles"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A journey of a thousand miles begins with a single step",k = 6) == "A journey of a thousand miles": {e}')
    
    total += 1
    try:
        result = candidate(s = "Success is not final success is courage to continue",k = 7) == "Success is not final success is courage"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Success is not final success is courage to continue",k = 7) == "Success is not final success is courage": {e}')
    
    total += 1
    try:
        result = candidate(s = "In the beginning God created the heavens and the earth",k = 6) == "In the beginning God created the"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "In the beginning God created the heavens and the earth",k = 6) == "In the beginning God created the": {e}')
    
    total += 1
    try:
        result = candidate(s = "Programming in Python is very rewarding",k = 5) == "Programming in Python is very"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Programming in Python is very rewarding",k = 5) == "Programming in Python is very": {e}')
    
    total += 1
    try:
        result = candidate(s = "You can lead a horse to water but you cannot make it drink",k = 11) == "You can lead a horse to water but you cannot make"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "You can lead a horse to water but you cannot make it drink",k = 11) == "You can lead a horse to water but you cannot make": {e}')
    
    total += 1
    try:
        result = candidate(s = "Another example with different words",k = 3) == "Another example with"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Another example with different words",k = 3) == "Another example with": {e}')
    
    total += 1
    try:
        result = candidate(s = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",k = 10) == "A B C D E F G H I J"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",k = 10) == "A B C D E F G H I J": {e}')
    
    total += 1
    try:
        result = candidate(s = "The quick brown fox jumps over the lazy dog",k = 9) == "The quick brown fox jumps over the lazy dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The quick brown fox jumps over the lazy dog",k = 9) == "The quick brown fox jumps over the lazy dog": {e}')
    
    total += 1
    try:
        result = candidate(s = "MixedCASE Words In Sentences Should Be Handled",k = 5) == "MixedCASE Words In Sentences Should"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "MixedCASE Words In Sentences Should Be Handled",k = 5) == "MixedCASE Words In Sentences Should": {e}')
    
    total += 1
    try:
        result = candidate(s = "Well done is better than well said",k = 5) == "Well done is better than"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Well done is better than well said",k = 5) == "Well done is better than": {e}')
    
    total += 1
    try:
        result = candidate(s = "The quick brown fox jumps over the lazy dog",k = 7) == "The quick brown fox jumps over the"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "The quick brown fox jumps over the lazy dog",k = 7) == "The quick brown fox jumps over the": {e}')
    
    total += 1
    try:
        result = candidate(s = "Yet another test to ensure correctness",k = 5) == "Yet another test to ensure"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Yet another test to ensure correctness",k = 5) == "Yet another test to ensure": {e}')
    
    total += 1
    try:
        result = candidate(s = "Edge case test with exact words count",k = 6) == "Edge case test with exact words"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Edge case test with exact words count",k = 6) == "Edge case test with exact words": {e}')
    
    total += 1
    try:
        result = candidate(s = "SingleWord",k = 1) == "SingleWord"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "SingleWord",k = 1) == "SingleWord": {e}')
    
    total += 1
    try:
        result = candidate(s = "Hello World from the other side of the universe",k = 8) == "Hello World from the other side of the"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Hello World from the other side of the universe",k = 8) == "Hello World from the other side of the": {e}')
    
    total += 1
    try:
        result = candidate(s = "In the middle of every difficulty lies opportunity",k = 8) == "In the middle of every difficulty lies opportunity"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "In the middle of every difficulty lies opportunity",k = 8) == "In the middle of every difficulty lies opportunity": {e}')
    
    total += 1
    try:
        result = candidate(s = "One two three four five six seven eight nine ten",k = 5) == "One two three four five"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "One two three four five six seven eight nine ten",k = 5) == "One two three four five": {e}')
    
    total += 1
    try:
        result = candidate(s = "With great power comes great responsibility",k = 5) == "With great power comes great"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "With great power comes great responsibility",k = 5) == "With great power comes great": {e}')
    
    total += 1
    try:
        result = candidate(s = "Multiple    Spaces    Between    Words    Are    Not    Allowed",k = 5) == "Multiple Spaces Between Words Are"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Multiple    Spaces    Between    Words    Are    Not    Allowed",k = 5) == "Multiple Spaces Between Words Are": {e}')
    
    total += 1
    try:
        result = candidate(s = "Multiple     spaces    should    not    be    here    but    for    testing    purposes    we    will    add    them",k = 10) == "Multiple spaces should not be here but for testing purposes"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Multiple     spaces    should    not    be    here    but    for    testing    purposes    we    will    add    them",k = 10) == "Multiple spaces should not be here but for testing purposes": {e}')
    
    total += 1
    try:
        result = candidate(s = "An apple a day keeps the doctor away",k = 8) == "An apple a day keeps the doctor away"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "An apple a day keeps the doctor away",k = 8) == "An apple a day keeps the doctor away": {e}')
    
    total += 1
    try:
        result = candidate(s = "Sometimes the journey is more important than the destination",k = 9) == "Sometimes the journey is more important than the destination"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Sometimes the journey is more important than the destination",k = 9) == "Sometimes the journey is more important than the destination": {e}')
    
    total += 1
    try:
        result = candidate(s = "Sometimes you just want to have a long sentence to test the truncation functionality of the code",k = 15) == "Sometimes you just want to have a long sentence to test the truncation functionality of"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Sometimes you just want to have a long sentence to test the truncation functionality of the code",k = 15) == "Sometimes you just want to have a long sentence to test the truncation functionality of": {e}')
    
    total += 1
    try:
        result = candidate(s = "A quick brown fox jumps over the lazy dog",k = 9) == "A quick brown fox jumps over the lazy dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "A quick brown fox jumps over the lazy dog",k = 9) == "A quick brown fox jumps over the lazy dog": {e}')
    
    total += 1
    try:
        result = candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 26) == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 26) == "a b c d e f g h i j k l m n o p q r s t u v w x y z": {e}')
    
    total += 1
    try:
        result = candidate(s = "This is a very long sentence that we need to truncate to the first few words",k = 7) == "This is a very long sentence that"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "This is a very long sentence that we need to truncate to the first few words",k = 7) == "This is a very long sentence that": {e}')
    
    total += 1
    try:
        result = candidate(s = "May the force be with you",k = 5) == "May the force be with"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "May the force be with you",k = 5) == "May the force be with": {e}')
    
    total += 1
    try:
        result = candidate(s = "In the heart of the night the fireflies dance",k = 8) == "In the heart of the night the fireflies"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "In the heart of the night the fireflies dance",k = 8) == "In the heart of the night the fireflies": {e}')
    
    total += 1
    try:
        result = candidate(s = "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords",k = 5) == "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords",k = 5) == "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords": {e}')
    
    total += 1
    try:
        result = candidate(s = "To be or not to be that is the question",k = 6) == "To be or not to be"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "To be or not to be that is the question",k = 6) == "To be or not to be": {e}')
    
    total += 1
    try:
        result = candidate(s = "Better late than never",k = 4) == "Better late than never"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Better late than never",k = 4) == "Better late than never": {e}')
    
    total += 1
    try:
        result = candidate(s = "Actions speak louder than words",k = 4) == "Actions speak louder than"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Actions speak louder than words",k = 4) == "Actions speak louder than": {e}')
    
    total += 1
    try:
        result = candidate(s = "Keep calm and carry on",k = 3) == "Keep calm and"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Keep calm and carry on",k = 3) == "Keep calm and": {e}')
    
    total += 1
    try:
        result = candidate(s = "Lorem ipsum dolor sit amet consectetur adipiscing elit",k = 7) == "Lorem ipsum dolor sit amet consectetur adipiscing"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Lorem ipsum dolor sit amet consectetur adipiscing elit",k = 7) == "Lorem ipsum dolor sit amet consectetur adipiscing": {e}')
    
    total += 1
    try:
        result = candidate(s = "This is a longer sentence to test the functionality",k = 7) == "This is a longer sentence to test"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "This is a longer sentence to test the functionality",k = 7) == "This is a longer sentence to test": {e}')
    
    total += 1
    try:
        result = candidate(s = "Software design is all about managing complexity",k = 7) == "Software design is all about managing complexity"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Software design is all about managing complexity",k = 7) == "Software design is all about managing complexity": {e}')
    
    total += 1
    try:
        result = candidate(s = "May the Force be with you",k = 3) == "May the Force"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "May the Force be with you",k = 3) == "May the Force": {e}')
    
    total += 1
    try:
        result = candidate(s = "Data structures and algorithms are the building blocks of software development",k = 8) == "Data structures and algorithms are the building blocks"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "Data structures and algorithms are the building blocks of software development",k = 8) == "Data structures and algorithms are the building blocks": {e}')
    
    total += 1
    try:
        result = candidate(s = "An algorithm must be seen to be believed",k = 5) == "An algorithm must be seen"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "An algorithm must be seen to be believed",k = 5) == "An algorithm must be seen": {e}')
    
    total += 1
    try:
        result = candidate(s = "This is a test for truncating the sentence at exactly the word limit",k = 10) == "This is a test for truncating the sentence at exactly"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "This is a test for truncating the sentence at exactly the word limit",k = 10) == "This is a test for truncating the sentence at exactly": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "I love to code",k = 3) == "I love to"
    assert candidate(s = "Python is great",k = 2) == "Python is"
    assert candidate(s = "Python programming is fun",k = 2) == "Python programming"
    assert candidate(s = "A quick brown fox jumps over the lazy dog",k = 3) == "A quick brown"
    assert candidate(s = "I love programming in Python",k = 3) == "I love programming"
    assert candidate(s = "Hello how are you Contestant",k = 4) == "Hello how are you"
    assert candidate(s = "Python is a great programming language",k = 2) == "Python is"
    assert candidate(s = "chopper is not a tanuki",k = 5) == "chopper is not a tanuki"
    assert candidate(s = "Python is fun",k = 2) == "Python is"
    assert candidate(s = "I love programming",k = 1) == "I"
    assert candidate(s = "What is the solution to this problem",k = 4) == "What is the solution"
    assert candidate(s = "I love solving problems",k = 3) == "I love solving"
    assert candidate(s = "It does not matter how slowly you go as long as you do not stop",k = 9) == "It does not matter how slowly you go as"
    assert candidate(s = "The road to success is always under construction",k = 7) == "The road to success is always under"
    assert candidate(s = "The best way to predict your future is to create it",k = 8) == "The best way to predict your future is"
    assert candidate(s = "This is a test sentence to check the functionality of the code",k = 9) == "This is a test sentence to check the functionality"
    assert candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 5) == "a b c d e"
    assert candidate(s = "In computer science, the art of programming is the science of abstraction",k = 8) == "In computer science, the art of programming is"
    assert candidate(s = "A journey of a thousand miles begins with a single step",k = 8) == "A journey of a thousand miles begins with"
    assert candidate(s = "Believe you can and you're halfway there",k = 5) == "Believe you can and you're"
    assert candidate(s = "Keep it simple stupid",k = 5) == "Keep it simple stupid"
    assert candidate(s = "To be or not to be that is the question",k = 10) == "To be or not to be that is the question"
    assert candidate(s = "May the Force be with you young Jedi",k = 6) == "May the Force be with you"
    assert candidate(s = "Short sentence",k = 2) == "Short sentence"
    assert candidate(s = "The only way to do great work is to love what you do",k = 7) == "The only way to do great work"
    assert candidate(s = "Honesty is the best policy",k = 4) == "Honesty is the best"
    assert candidate(s = "In the middle of difficulty lies opportunity",k = 4) == "In the middle of"
    assert candidate(s = "Natural language processing has become a cornerstone of modern technology",k = 9) == "Natural language processing has become a cornerstone of modern"
    assert candidate(s = "One two three four five six seven eight nine ten",k = 10) == "One two three four five six seven eight nine ten"
    assert candidate(s = "You miss 100 percent of the shots you don t take Wayne Gretzky",k = 11) == "You miss 100 percent of the shots you don t take"
    assert candidate(s = "OpenAI GPT-4 can generate human-like text based on the input it receives",k = 7) == "OpenAI GPT-4 can generate human-like text based"
    assert candidate(s = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen",k = 10) == "One two three four five six seven eight nine ten"
    assert candidate(s = "What you get by achieving your goals is not as important as what you become by achieving your goals",k = 12) == "What you get by achieving your goals is not as important as"
    assert candidate(s = "Debugging is twice as hard as writing the code in the first place",k = 7) == "Debugging is twice as hard as writing"
    assert candidate(s = "Python programming is fun and challenging",k = 10) == "Python programming is fun and challenging"
    assert candidate(s = "A journey of a thousand miles begins with a single step",k = 7) == "A journey of a thousand miles begins"
    assert candidate(s = "Success is not final success is to be able to continue to try",k = 8) == "Success is not final success is to be"
    assert candidate(s = "OneWordOnly",k = 1) == "OneWordOnly"
    assert candidate(s = "Data Science and Machine Learning",k = 3) == "Data Science and"
    assert candidate(s = "Life is what happens when you are busy making other plans",k = 7) == "Life is what happens when you are"
    assert candidate(s = "The early morning sun is warm and welcoming",k = 7) == "The early morning sun is warm and"
    assert candidate(s = "To be or not to be that is the question",k = 7) == "To be or not to be that"
    assert candidate(s = "Short but tricky",k = 2) == "Short but"
    assert candidate(s = "The early bird catches the worm",k = 5) == "The early bird catches the"
    assert candidate(s = "Final complex sentence with multiple words indeed",k = 7) == "Final complex sentence with multiple words indeed"
    assert candidate(s = "The best way to predict the future is to invent it",k = 9) == "The best way to predict the future is to"
    assert candidate(s = "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences",k = 1) == "VeryLongWordWithoutSpacesIsAlsoAcceptedButNotTypicalInSentences"
    assert candidate(s = "Do not judge a book by its cover",k = 7) == "Do not judge a book by its"
    assert candidate(s = "All that glitters is not gold only the good do well by gold",k = 9) == "All that glitters is not gold only the good"
    assert candidate(s = "All that glitters is not gold",k = 5) == "All that glitters is not"
    assert candidate(s = "To be or not to be that is the question",k = 5) == "To be or not to"
    assert candidate(s = "Edge case with k equal to the number of words here",k = 9) == "Edge case with k equal to the number of"
    assert candidate(s = "Multiple words with mixed CASE Words",k = 4) == "Multiple words with mixed"
    assert candidate(s = "Programming in Python is both fun and educational",k = 6) == "Programming in Python is both fun"
    assert candidate(s = "A journey of a thousand miles begins with a single step",k = 6) == "A journey of a thousand miles"
    assert candidate(s = "Success is not final success is courage to continue",k = 7) == "Success is not final success is courage"
    assert candidate(s = "In the beginning God created the heavens and the earth",k = 6) == "In the beginning God created the"
    assert candidate(s = "Programming in Python is very rewarding",k = 5) == "Programming in Python is very"
    assert candidate(s = "You can lead a horse to water but you cannot make it drink",k = 11) == "You can lead a horse to water but you cannot make"
    assert candidate(s = "Another example with different words",k = 3) == "Another example with"
    assert candidate(s = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",k = 10) == "A B C D E F G H I J"
    assert candidate(s = "The quick brown fox jumps over the lazy dog",k = 9) == "The quick brown fox jumps over the lazy dog"
    assert candidate(s = "MixedCASE Words In Sentences Should Be Handled",k = 5) == "MixedCASE Words In Sentences Should"
    assert candidate(s = "Well done is better than well said",k = 5) == "Well done is better than"
    assert candidate(s = "The quick brown fox jumps over the lazy dog",k = 7) == "The quick brown fox jumps over the"
    assert candidate(s = "Yet another test to ensure correctness",k = 5) == "Yet another test to ensure"
    assert candidate(s = "Edge case test with exact words count",k = 6) == "Edge case test with exact words"
    assert candidate(s = "SingleWord",k = 1) == "SingleWord"
    assert candidate(s = "Hello World from the other side of the universe",k = 8) == "Hello World from the other side of the"
    assert candidate(s = "In the middle of every difficulty lies opportunity",k = 8) == "In the middle of every difficulty lies opportunity"
    assert candidate(s = "One two three four five six seven eight nine ten",k = 5) == "One two three four five"
    assert candidate(s = "With great power comes great responsibility",k = 5) == "With great power comes great"
    assert candidate(s = "Multiple    Spaces    Between    Words    Are    Not    Allowed",k = 5) == "Multiple Spaces Between Words Are"
    assert candidate(s = "Multiple     spaces    should    not    be    here    but    for    testing    purposes    we    will    add    them",k = 10) == "Multiple spaces should not be here but for testing purposes"
    assert candidate(s = "An apple a day keeps the doctor away",k = 8) == "An apple a day keeps the doctor away"
    assert candidate(s = "Sometimes the journey is more important than the destination",k = 9) == "Sometimes the journey is more important than the destination"
    assert candidate(s = "Sometimes you just want to have a long sentence to test the truncation functionality of the code",k = 15) == "Sometimes you just want to have a long sentence to test the truncation functionality of"
    assert candidate(s = "A quick brown fox jumps over the lazy dog",k = 9) == "A quick brown fox jumps over the lazy dog"
    assert candidate(s = "a b c d e f g h i j k l m n o p q r s t u v w x y z",k = 26) == "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    assert candidate(s = "This is a very long sentence that we need to truncate to the first few words",k = 7) == "This is a very long sentence that"
    assert candidate(s = "May the force be with you",k = 5) == "May the force be with"
    assert candidate(s = "In the heart of the night the fireflies dance",k = 8) == "In the heart of the night the fireflies"
    assert candidate(s = "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords",k = 5) == "ManyManyWordsInOneSentenceWithoutSpacesButAllowedByConstraintsIfWeRemoveSpacesThenThisWillBeAVeryLongListofWords"
    assert candidate(s = "To be or not to be that is the question",k = 6) == "To be or not to be"
    assert candidate(s = "Better late than never",k = 4) == "Better late than never"
    assert candidate(s = "Actions speak louder than words",k = 4) == "Actions speak louder than"
    assert candidate(s = "Keep calm and carry on",k = 3) == "Keep calm and"
    assert candidate(s = "Lorem ipsum dolor sit amet consectetur adipiscing elit",k = 7) == "Lorem ipsum dolor sit amet consectetur adipiscing"
    assert candidate(s = "This is a longer sentence to test the functionality",k = 7) == "This is a longer sentence to test"
    assert candidate(s = "Software design is all about managing complexity",k = 7) == "Software design is all about managing complexity"
    assert candidate(s = "May the Force be with you",k = 3) == "May the Force"
    assert candidate(s = "Data structures and algorithms are the building blocks of software development",k = 8) == "Data structures and algorithms are the building blocks"
    assert candidate(s = "An algorithm must be seen to be believed",k = 5) == "An algorithm must be seen"
    assert candidate(s = "This is a test for truncating the sentence at exactly the word limit",k = 10) == "This is a test for truncating the sentence at exactly"


