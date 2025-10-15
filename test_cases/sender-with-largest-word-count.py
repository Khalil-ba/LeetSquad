def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi'],senders = ['Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi'],senders = ['Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message indeed'],senders = ['Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message indeed'],senders = ['Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['How is leetcode for everyone', 'Leetcode is useful for practice'],senders = ['Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['How is leetcode for everyone', 'Leetcode is useful for practice'],senders = ['Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi', 'Hello', 'Hey'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi', 'Hello', 'Hey'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree'],senders = ['Alice', 'userTwo', 'userThree', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree'],senders = ['Alice', 'userTwo', 'userThree', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message indeed'],senders = ['Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message indeed'],senders = ['Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message indeed'],senders = ['Charlie', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message indeed'],senders = ['Charlie', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message here', 'Even longer message here'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message here', 'Even longer message here'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a', 'b', 'c', 'd'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a', 'b', 'c', 'd'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello', 'Hi'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello', 'Hi'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello World', 'Foo Bar'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello World', 'Foo Bar'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi', 'Hello'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi', 'Hello'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal length messages here', 'Equal length messages here', 'Equal length messages here'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal length messages here', 'Equal length messages here', 'Equal length messages here'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a a a a a a a a a a', 'b b b b b b b b b', 'c c c c c c c c', 'd d d d d d d'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a a a a a a a a a a', 'b b b b b b b b b', 'c c c c c c c c', 'd d d d d d d'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello Alice', 'Hello Bob', 'Hello Charlie', 'Hello Dave', 'Hello Eve'],senders = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']) == "Eve"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello Alice', 'Hello Bob', 'Hello Charlie', 'Hello Dave', 'Hello Eve'],senders = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']) == "Eve": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message with multiple words', 'Another long message that is quite lengthy'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message with multiple words', 'Another long message that is quite lengthy'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'],senders = ['Alice', 'Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'],senders = ['Alice', 'Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word', 'Word Word Word Word Word'],senders = ['Yankee', 'yankee', 'YANKEE', 'Yankee', 'yankee']) == "yankee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word', 'Word Word Word Word Word'],senders = ['Yankee', 'yankee', 'YANKEE', 'Yankee', 'yankee']) == "yankee": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a', 'b c', 'd e f', 'g h i j'],senders = ['Z', 'Y', 'X', 'W']) == "W"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a', 'b c', 'd e f', 'g h i j'],senders = ['Z', 'Y', 'X', 'W']) == "W": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['First message', 'Second message', 'Third message', 'Fourth message'],senders = ['Dave', 'Dave', 'Eve', 'Dave']) == "Dave"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['First message', 'Second message', 'Third message', 'Fourth message'],senders = ['Dave', 'Dave', 'Eve', 'Dave']) == "Dave": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a longer message with multiple words', 'Short message', 'Another long message with several words in it'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a longer message with multiple words', 'Short message', 'Another long message with several words in it'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f'],senders = ['Z', 'Y', 'X', 'W', 'V', 'U']) == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f'],senders = ['Z', 'Y', 'X', 'W', 'V', 'U']) == "Z": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi', 'Hello', 'Hey', 'Goodbye', 'See you later'],senders = ['Alice', 'Bob', 'Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi', 'Hello', 'Hey', 'Goodbye', 'See you later'],senders = ['Alice', 'Bob', 'Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'How are you doing', 'I am fine thank you', 'And you'],senders = ['Bob', 'Charlie', 'Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'How are you doing', 'I am fine thank you', 'And you'],senders = ['Bob', 'Charlie', 'Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Many many words in this message to test the function', 'Few words'],senders = ['Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Many many words in this message to test the function', 'Few words'],senders = ['Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short message', 'Another short one'],senders = ['charlie', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short message', 'Another short one'],senders = ['charlie', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One two three four five', 'Six seven eight nine ten', 'Eleven twelve'],senders = ['George', 'Hannah', 'George']) == "George"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One two three four five', 'Six seven eight nine ten', 'Eleven twelve'],senders = ['George', 'Hannah', 'George']) == "George": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree', 'Great to see you Alice'],senders = ['Alice', 'userTwo', 'userThree', 'Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree', 'Great to see you Alice'],senders = ['Alice', 'userTwo', 'userThree', 'Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],senders = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']) == "A"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],senders = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']) == "A": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short msg', 'Medium length message indeed', 'A very long message with lots of words to count accurately'],senders = ['Carol', 'Carol', 'Carol']) == "Carol"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short msg', 'Medium length message indeed', 'A very long message with lots of words to count accurately'],senders = ['Carol', 'Carol', 'Carol']) == "Carol": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'Python programming is fun', 'Hello again', 'Data structures and algorithms'],senders = ['Alice', 'Bob', 'Alice', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'Python programming is fun', 'Hello again', 'Data structures and algorithms'],senders = ['Alice', 'Bob', 'Alice', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Long message to test', 'Another long message to test', 'Short'],senders = ['Charlie', 'Alice', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Long message to test', 'Another long message to test', 'Short'],senders = ['Charlie', 'Alice', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two', 'Three', 'Four', 'Five'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two', 'Three', 'Four', 'Five'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words here', 'Three words in this message', 'Four words make a sentence'],senders = ['Anna', 'Anna', 'Anna', 'Anna']) == "Anna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words here', 'Three words in this message', 'Four words make a sentence'],senders = ['Anna', 'Anna', 'Anna', 'Anna']) == "Anna": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Quick brown fox jumps over lazy dog', 'Hello', 'Goodbye'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Quick brown fox jumps over lazy dog', 'Hello', 'Goodbye'],senders = ['Alice', 'Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Quick brown fox', 'Lazy dog', 'Uppercase LOWERCASE', 'Mixed CASE Words'],senders = ['Alex', 'Bob', 'Charlie', 'David']) == "David"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Quick brown fox', 'Lazy dog', 'Uppercase LOWERCASE', 'Mixed CASE Words'],senders = ['Alex', 'Bob', 'Charlie', 'David']) == "David": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words here', 'Three words in this one', 'Four words make this message'],senders = ['Eve', 'eve', 'EVE', 'Eve']) == "Eve"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words here', 'Three words in this one', 'Four words make this message'],senders = ['Eve', 'eve', 'EVE', 'Eve']) == "Eve": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a longer message', 'Even longer message here', 'Short'],senders = ['Charlie', 'Charlie', 'Alice']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a longer message', 'Even longer message here', 'Short'],senders = ['Charlie', 'Charlie', 'Alice']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Longer message to test', 'Even longer message to check the word count', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Longer message to test', 'Even longer message to check the word count', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a test message', 'Another test', 'Yet another message here'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a test message', 'Another test', 'Yet another message here'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Foo bar baz'],senders = ['Dave', 'Eve']) == "Dave"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Foo bar baz'],senders = ['Dave', 'Eve']) == "Dave": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal words here', 'Equal words here'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal words here', 'Equal words here'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Many words in this message to test the word count functionality', 'Another message to ensure the solution works correctly'],senders = ['Anna', 'Anna']) == "Anna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Many words in this message to test the word count functionality', 'Another message to ensure the solution works correctly'],senders = ['Anna', 'Anna']) == "Anna": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Multiple words', 'Multiple words', 'Multiple words', 'Multiple words'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Multiple words', 'Multiple words', 'Multiple words', 'Multiple words'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal words', 'Equal words'],senders = ['Anna', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal words', 'Equal words'],senders = ['Anna', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal length message', 'Another equal length message'],senders = ['Dave', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal length message', 'Another equal length message'],senders = ['Dave', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Word', 'Word word', 'Word word word', 'Word word word word', 'Word word word word word'],senders = ['Alex', 'Alex', 'Alex', 'Brian', 'Brian']) == "Brian"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Word', 'Word word', 'Word word word', 'Word word word word', 'Word word word word word'],senders = ['Alex', 'Alex', 'Alex', 'Brian', 'Brian']) == "Brian": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in this message'],senders = ['Bob', 'Charlie', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in this message'],senders = ['Bob', 'Charlie', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Multiple words in this message', 'Single', 'Two words'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Multiple words in this message', 'Single', 'Two words'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal length', 'Equal length'],senders = ['Tom', 'Jerry']) == "Tom"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal length', 'Equal length'],senders = ['Tom', 'Jerry']) == "Tom": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal words in messages', 'Equal words in messages'],senders = ['Sender1', 'Sender2']) == "Sender2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal words in messages', 'Equal words in messages'],senders = ['Sender1', 'Sender2']) == "Sender2": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Unique message each time', 'Another unique one'],senders = ['Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Unique message each time', 'Another unique one'],senders = ['Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Same sender many times', 'Same sender many times', 'Same sender many times'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Same sender many times', 'Same sender many times', 'Same sender many times'],senders = ['Alice', 'Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message one', 'Another message', 'Yet another message to test', 'Final message'],senders = ['Zara', 'Alice', 'Bob', 'Charlie']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message one', 'Another message', 'Yet another message to test', 'Final message'],senders = ['Zara', 'Alice', 'Bob', 'Charlie']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A B C D E', 'F G H I J K L M N O P', 'Q R S T U V W X Y Z'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A B C D E', 'F G H I J K L M N O P', 'Q R S T U V W X Y Z'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'Foo bar baz', 'This is a test message'],senders = ['alice', 'Bob', 'alice']) == "alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'Foo bar baz', 'This is a test message'],senders = ['alice', 'Bob', 'alice']) == "alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message one', 'Message two', 'Message three'],senders = ['Zach', 'Yvonne', 'Xander']) == "Zach"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message one', 'Message two', 'Message three'],senders = ['Zach', 'Yvonne', 'Xander']) == "Zach": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Different sender', 'Different sender', 'Different sender', 'Different sender'],senders = ['Mike', 'Mike', 'Mike', 'Mike']) == "Mike"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Different sender', 'Different sender', 'Different sender', 'Different sender'],senders = ['Mike', 'Mike', 'Mike', 'Mike']) == "Mike": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short', 'Medium length message', 'A very very very long message that spans several words indeed'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short', 'Medium length message', 'A very very very long message that spans several words indeed'],senders = ['Alice', 'Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a longer message', 'Short', 'Another long message here'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a longer message', 'Short', 'Another long message here'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'],senders = ['Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'],senders = ['Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a', 'b', 'c', 'd', 'e'],senders = ['Eve', 'Eve', 'Eve', 'Eve', 'Eve']) == "Eve"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a', 'b', 'c', 'd', 'e'],senders = ['Eve', 'Eve', 'Eve', 'Eve', 'Eve']) == "Eve": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal words', 'Equal words'],senders = ['Frank', 'frank']) == "frank"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal words', 'Equal words'],senders = ['Frank', 'frank']) == "frank": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a test message', 'Another test', 'Short one'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a test message', 'Another test', 'Short one'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Sed do eiusmod tempor incididunt'],senders = ['Sam', 'Sam', 'Sam', 'Sam']) == "Sam"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Sed do eiusmod tempor incididunt'],senders = ['Sam', 'Sam', 'Sam', 'Sam']) == "Sam": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal', 'Equal Equal', 'Equal Equal Equal'],senders = ['Mickey', 'mickey', 'MICKEY']) == "MICKEY"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal', 'Equal Equal', 'Equal Equal Equal'],senders = ['Mickey', 'mickey', 'MICKEY']) == "MICKEY": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi Alice', 'Hello Bob', 'How are you Charlie'],senders = ['Bob', 'Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi Alice', 'Hello Bob', 'How are you Charlie'],senders = ['Bob', 'Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'Good morning', 'How are you doing'],senders = ['Charlie', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'Good morning', 'How are you doing'],senders = ['Charlie', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'How are you today', 'Hope you are well'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'How are you today', 'Hope you are well'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz', 'abc def', 'ghi jkl'],senders = ['Charlie', 'Bob', 'Alice', 'Charlie', 'Alice']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz', 'abc def', 'ghi jkl'],senders = ['Charlie', 'Bob', 'Alice', 'Charlie', 'Alice']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word'],senders = ['Zeta', 'Zeta', 'zeta', 'ZETA']) == "ZETA"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word'],senders = ['Zeta', 'Zeta', 'zeta', 'ZETA']) == "ZETA": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a very long message to test the word count functionality', 'Short msg'],senders = ['Delta', 'delta']) == "Delta"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a very long message to test the word count functionality', 'Short msg'],senders = ['Delta', 'delta']) == "Delta": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hi there', 'Hello there', 'Hi there', 'Hello there'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hi there', 'Hello there', 'Hi there', 'Hello there'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A', 'B', 'C', 'D'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A', 'B', 'C', 'D'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words', 'Three words here', 'Four words message test'],senders = ['David', 'David', 'Eve', 'Eve']) == "Eve"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words', 'Three words here', 'Four words message test'],senders = ['David', 'David', 'Eve', 'Eve']) == "Eve": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Same length', 'Same length', 'Same length', 'Same length'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Same length', 'Same length', 'Same length', 'Same length'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Quick brown fox jumps over the lazy dog', 'Lazy dog sleeps', 'Quick fox runs away'],senders = ['Dog', 'Dog', 'Fox']) == "Dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Quick brown fox jumps over the lazy dog', 'Lazy dog sleeps', 'Quick fox runs away'],senders = ['Dog', 'Dog', 'Fox']) == "Dog": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal words here', 'Equal words here', 'Equal words here'],senders = ['Anna', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal words here', 'Equal words here', 'Equal words here'],senders = ['Anna', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Multiple messages here', 'Even more messages', 'And yet another message'],senders = ['Kate', 'Kate', 'Laura']) == "Kate"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Multiple messages here', 'Even more messages', 'And yet another message'],senders = ['Kate', 'Kate', 'Laura']) == "Kate": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Multiple words in this message', 'Another message with several words', 'Just a few words'],senders = ['SenderX', 'SenderX', 'SenderY']) == "SenderX"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Multiple words in this message', 'Another message with several words', 'Just a few words'],senders = ['SenderX', 'SenderX', 'SenderY']) == "SenderX": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message from Alice', 'Another message from Alice', 'Yet another message from Alice', 'Final message from Alice'],senders = ['Alice', 'Alice', 'Alice', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message from Alice', 'Another message from Alice', 'Yet another message from Alice', 'Final message from Alice'],senders = ['Alice', 'Alice', 'Alice', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four', 'Message five'],senders = ['Neil', 'Neil', 'Neil', 'Neil', 'Neil']) == "Neil"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four', 'Message five'],senders = ['Neil', 'Neil', 'Neil', 'Neil', 'Neil']) == "Neil": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Multiple words in this message', 'Few words', 'One'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Multiple words in this message', 'Few words', 'One'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Equal length message', 'Equal length message'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Equal length message', 'Equal length message'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['word'],senders = ['Z']) == "Z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['word'],senders = ['Z']) == "Z": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Single', 'Double words', 'Triple words here'],senders = ['Eve', 'Eve', 'Frank']) == "Frank"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Single', 'Double words', 'Triple words here'],senders = ['Eve', 'Eve', 'Frank']) == "Frank": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Many words in this message to test the word count', 'Few words'],senders = ['Charlie', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Many words in this message to test the word count', 'Few words'],senders = ['Charlie', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Same sender multiple times', 'Same sender multiple times', 'Same sender multiple times'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Same sender multiple times', 'Same sender multiple times', 'Same sender multiple times'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A B C D E', 'F G H', 'I J K L M N O'],senders = ['Dave', 'Eve', 'Frank']) == "Frank"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A B C D E', 'F G H', 'I J K L M N O'],senders = ['Dave', 'Eve', 'Frank']) == "Frank": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Long message with multiple words indeed', 'Another long message with multiple words indeed'],senders = ['Anna', 'Anna']) == "Anna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Long message with multiple words indeed', 'Another long message with multiple words indeed'],senders = ['Anna', 'Anna']) == "Anna": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Zachary']) == "Zachary"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Zachary']) == "Zachary": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['This is a test message', 'Another message here', 'Short one'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['This is a test message', 'Another message here', 'Short one'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog'],senders = ['Grace', 'grace']) == "grace"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog'],senders = ['Grace', 'grace']) == "grace": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Single', 'Double double', 'Triple triple triple'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Single', 'Double double', 'Triple triple triple'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short message', 'Longer message here', 'Even longer message to check', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short message', 'Longer message here', 'Even longer message to check', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Short one', 'Another short one'],senders = ['Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Short one', 'Another short one'],senders = ['Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words', 'Three words here'],senders = ['Zara', 'Zara', 'Zara']) == "Zara"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words', 'Three words here'],senders = ['Zara', 'Zara', 'Zara']) == "Zara": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Unique words in each message', 'Unique words here too', 'More unique words'],senders = ['Zoe', 'Yasmin', 'Xander']) == "Zoe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Unique words in each message', 'Unique words here too', 'More unique words'],senders = ['Zoe', 'Yasmin', 'Xander']) == "Zoe": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in a sentence'],senders = ['Charlie', 'Alice', 'Bob', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in a sentence'],senders = ['Charlie', 'Alice', 'Bob', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'This is a longer message', 'Another message'],senders = ['Charlie', 'Bob', 'Charlie']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'This is a longer message', 'Another message'],senders = ['Charlie', 'Bob', 'Charlie']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Test message', 'Test message', 'Test message', 'Test message'],senders = ['Jack', 'Jack', 'Jack', 'Jack']) == "Jack"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Test message', 'Test message', 'Test message', 'Test message'],senders = ['Jack', 'Jack', 'Jack', 'Jack']) == "Jack": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['One more message', 'Yet another message', 'Final message'],senders = ['Charlie', 'Charlie', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['One more message', 'Yet another message', 'Final message'],senders = ['Charlie', 'Charlie', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'How are you doing today', 'Fine thank you'],senders = ['Charlie', 'Alice', 'Bob']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'How are you doing today', 'Fine thank you'],senders = ['Charlie', 'Alice', 'Bob']) == "Alice": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'This is a test', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'This is a test', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Single', 'Two words', 'Three word phrase', 'Four word sentence structure'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Single', 'Two words', 'Three word phrase', 'Four word sentence structure'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Hello world', 'Hello Alice', 'Hello Bob'],senders = ['Bob', 'Alice', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Hello world', 'Hello Alice', 'Hello Bob'],senders = ['Bob', 'Alice', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A B C D E F G', 'H I J K L M N', 'O P Q R S T U V W X Y Z'],senders = ['SenderA', 'SenderB', 'SenderC']) == "SenderC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A B C D E F G', 'H I J K L M N', 'O P Q R S T U V W X Y Z'],senders = ['SenderA', 'SenderB', 'SenderC']) == "SenderC": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Unique message', 'Unique message', 'Unique message'],senders = ['Ian', 'Ian', 'Ian']) == "Ian"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Unique message', 'Unique message', 'Unique message'],senders = ['Ian', 'Ian', 'Ian']) == "Ian": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Anna', 'Bob', 'Charlie', 'Bob']) == "Bob"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Anna', 'Bob', 'Charlie', 'Bob']) == "Bob": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['Long message to increase word count significantly', 'Short'],senders = ['Charlie', 'Charlie']) == "Charlie"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['Long message to increase word count significantly', 'Short'],senders = ['Charlie', 'Charlie']) == "Charlie": {e}')
    
    total += 1
    try:
        result = candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog', 'Lazy dog'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog', 'Lazy dog'],senders = ['Alice', 'Bob', 'Alice']) == "Alice": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Hi'],senders = ['Bob']) == "Bob"
    assert candidate(messages = ['Short', 'Longer message indeed'],senders = ['Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['How is leetcode for everyone', 'Leetcode is useful for practice'],senders = ['Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Hi', 'Hello', 'Hey'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree'],senders = ['Alice', 'userTwo', 'userThree', 'Alice']) == "Alice"
    assert candidate(messages = ['Short', 'Longer message indeed'],senders = ['Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['This is a test', 'Another test', 'Final test'],senders = ['Alice', 'Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Short', 'Longer message indeed'],senders = ['Charlie', 'Alice']) == "Alice"
    assert candidate(messages = ['Short', 'Longer message here', 'Even longer message here'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe"
    assert candidate(messages = ['a', 'b', 'c', 'd'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David"
    assert candidate(messages = ['Hello', 'Hi'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Hello World', 'Foo Bar'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Hi', 'Hello'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Equal length messages here', 'Equal length messages here', 'Equal length messages here'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['a a a a a a a a a a', 'b b b b b b b b b', 'c c c c c c c c', 'd d d d d d d'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Hello Alice', 'Hello Bob', 'Hello Charlie', 'Hello Dave', 'Hello Eve'],senders = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']) == "Eve"
    assert candidate(messages = ['Short', 'Longer message with multiple words', 'Another long message that is quite lengthy'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'],senders = ['Alice', 'Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word', 'Word Word Word Word Word'],senders = ['Yankee', 'yankee', 'YANKEE', 'Yankee', 'yankee']) == "yankee"
    assert candidate(messages = ['a', 'b c', 'd e f', 'g h i j'],senders = ['Z', 'Y', 'X', 'W']) == "W"
    assert candidate(messages = ['First message', 'Second message', 'Third message', 'Fourth message'],senders = ['Dave', 'Dave', 'Eve', 'Dave']) == "Dave"
    assert candidate(messages = ['This is a longer message with multiple words', 'Short message', 'Another long message with several words in it'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie"
    assert candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f'],senders = ['Z', 'Y', 'X', 'W', 'V', 'U']) == "Z"
    assert candidate(messages = ['Hi', 'Hello', 'Hey', 'Goodbye', 'See you later'],senders = ['Alice', 'Bob', 'Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Hello world', 'How are you doing', 'I am fine thank you', 'And you'],senders = ['Bob', 'Charlie', 'Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Many many words in this message to test the function', 'Few words'],senders = ['Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y', 'a b c d e f g h i j k l m n o p q r s t u v w x'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Short message', 'Another short one'],senders = ['charlie', 'Charlie']) == "Charlie"
    assert candidate(messages = ['One two three four five', 'Six seven eight nine ten', 'Eleven twelve'],senders = ['George', 'Hannah', 'George']) == "George"
    assert candidate(messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree', 'Great to see you Alice'],senders = ['Alice', 'userTwo', 'userThree', 'Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],senders = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']) == "A"
    assert candidate(messages = ['Short msg', 'Medium length message indeed', 'A very long message with lots of words to count accurately'],senders = ['Carol', 'Carol', 'Carol']) == "Carol"
    assert candidate(messages = ['Hello world', 'Python programming is fun', 'Hello again', 'Data structures and algorithms'],senders = ['Alice', 'Bob', 'Alice', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Long message to test', 'Another long message to test', 'Short'],senders = ['Charlie', 'Alice', 'Charlie']) == "Charlie"
    assert candidate(messages = ['One', 'Two', 'Three', 'Four', 'Five'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
    assert candidate(messages = ['One', 'Two words here', 'Three words in this message', 'Four words make a sentence'],senders = ['Anna', 'Anna', 'Anna', 'Anna']) == "Anna"
    assert candidate(messages = ['Quick brown fox jumps over lazy dog', 'Hello', 'Goodbye'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['Quick brown fox', 'Lazy dog', 'Uppercase LOWERCASE', 'Mixed CASE Words'],senders = ['Alex', 'Bob', 'Charlie', 'David']) == "David"
    assert candidate(messages = ['One', 'Two words here', 'Three words in this one', 'Four words make this message'],senders = ['Eve', 'eve', 'EVE', 'Eve']) == "Eve"
    assert candidate(messages = ['This is a longer message', 'Even longer message here', 'Short'],senders = ['Charlie', 'Charlie', 'Alice']) == "Charlie"
    assert candidate(messages = ['Short', 'Longer message to test', 'Even longer message to check the word count', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Alice"
    assert candidate(messages = ['This is a test message', 'Another test', 'Yet another message here'],senders = ['Charlie', 'Alice', 'Bob']) == "Charlie"
    assert candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Foo bar baz'],senders = ['Dave', 'Eve']) == "Dave"
    assert candidate(messages = ['Equal words here', 'Equal words here'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Many words in this message to test the word count functionality', 'Another message to ensure the solution works correctly'],senders = ['Anna', 'Anna']) == "Anna"
    assert candidate(messages = ['Multiple words', 'Multiple words', 'Multiple words', 'Multiple words'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David"
    assert candidate(messages = ['Equal words', 'Equal words'],senders = ['Anna', 'Bob']) == "Bob"
    assert candidate(messages = ['Equal length message', 'Another equal length message'],senders = ['Dave', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Word', 'Word word', 'Word word word', 'Word word word word', 'Word word word word word'],senders = ['Alex', 'Alex', 'Alex', 'Brian', 'Brian']) == "Brian"
    assert candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in this message'],senders = ['Bob', 'Charlie', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Multiple words in this message', 'Single', 'Two words'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Equal length', 'Equal length'],senders = ['Tom', 'Jerry']) == "Tom"
    assert candidate(messages = ['Equal words in messages', 'Equal words in messages'],senders = ['Sender1', 'Sender2']) == "Sender2"
    assert candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
    assert candidate(messages = ['Unique message each time', 'Another unique one'],senders = ['Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Same sender many times', 'Same sender many times', 'Same sender many times'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['Message one', 'Another message', 'Yet another message to test', 'Final message'],senders = ['Zara', 'Alice', 'Bob', 'Charlie']) == "Bob"
    assert candidate(messages = ['A B C D E', 'F G H I J K L M N O P', 'Q R S T U V W X Y Z'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob"
    assert candidate(messages = ['Hello world', 'Foo bar baz', 'This is a test message'],senders = ['alice', 'Bob', 'alice']) == "alice"
    assert candidate(messages = ['Message one', 'Message two', 'Message three'],senders = ['Zach', 'Yvonne', 'Xander']) == "Zach"
    assert candidate(messages = ['Different sender', 'Different sender', 'Different sender', 'Different sender'],senders = ['Mike', 'Mike', 'Mike', 'Mike']) == "Mike"
    assert candidate(messages = ['Short', 'Medium length message', 'A very very very long message that spans several words indeed'],senders = ['Alice', 'Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['This is a longer message', 'Short', 'Another long message here'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'],senders = ['Alice']) == "Alice"
    assert candidate(messages = ['a', 'b', 'c', 'd', 'e'],senders = ['Eve', 'Eve', 'Eve', 'Eve', 'Eve']) == "Eve"
    assert candidate(messages = ['Equal words', 'Equal words'],senders = ['Frank', 'frank']) == "frank"
    assert candidate(messages = ['This is a test message', 'Another test', 'Short one'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Sed do eiusmod tempor incididunt'],senders = ['Sam', 'Sam', 'Sam', 'Sam']) == "Sam"
    assert candidate(messages = ['Equal', 'Equal Equal', 'Equal Equal Equal'],senders = ['Mickey', 'mickey', 'MICKEY']) == "MICKEY"
    assert candidate(messages = ['Hi Alice', 'Hello Bob', 'How are you Charlie'],senders = ['Bob', 'Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Hello world', 'Good morning', 'How are you doing'],senders = ['Charlie', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Hello world', 'How are you today', 'Hope you are well'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz', 'abc def', 'ghi jkl'],senders = ['Charlie', 'Bob', 'Alice', 'Charlie', 'Alice']) == "Charlie"
    assert candidate(messages = ['Word', 'Word Word', 'Word Word Word', 'Word Word Word Word'],senders = ['Zeta', 'Zeta', 'zeta', 'ZETA']) == "ZETA"
    assert candidate(messages = ['This is a very long message to test the word count functionality', 'Short msg'],senders = ['Delta', 'delta']) == "Delta"
    assert candidate(messages = ['Hi there', 'Hello there', 'Hi there', 'Hello there'],senders = ['Alice', 'Bob', 'Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['A', 'B', 'C', 'D'],senders = ['Anna', 'Bob', 'Charlie', 'David']) == "David"
    assert candidate(messages = ['One', 'Two words', 'Three words here', 'Four words message test'],senders = ['David', 'David', 'Eve', 'Eve']) == "Eve"
    assert candidate(messages = ['Same length', 'Same length', 'Same length', 'Same length'],senders = ['Alice', 'Bob', 'Charlie', 'David']) == "David"
    assert candidate(messages = ['Quick brown fox jumps over the lazy dog', 'Lazy dog sleeps', 'Quick fox runs away'],senders = ['Dog', 'Dog', 'Fox']) == "Dog"
    assert candidate(messages = ['Equal words here', 'Equal words here', 'Equal words here'],senders = ['Anna', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Multiple messages here', 'Even more messages', 'And yet another message'],senders = ['Kate', 'Kate', 'Laura']) == "Kate"
    assert candidate(messages = ['Multiple words in this message', 'Another message with several words', 'Just a few words'],senders = ['SenderX', 'SenderX', 'SenderY']) == "SenderX"
    assert candidate(messages = ['Message from Alice', 'Another message from Alice', 'Yet another message from Alice', 'Final message from Alice'],senders = ['Alice', 'Alice', 'Alice', 'Alice']) == "Alice"
    assert candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four', 'Message five'],senders = ['Neil', 'Neil', 'Neil', 'Neil', 'Neil']) == "Neil"
    assert candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z', 'a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['Multiple words in this message', 'Few words', 'One'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"
    assert candidate(messages = ['Equal length message', 'Equal length message'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['word'],senders = ['Z']) == "Z"
    assert candidate(messages = ['Single', 'Double words', 'Triple words here'],senders = ['Eve', 'Eve', 'Frank']) == "Frank"
    assert candidate(messages = ['Many words in this message to test the word count', 'Few words'],senders = ['Charlie', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Same sender multiple times', 'Same sender multiple times', 'Same sender multiple times'],senders = ['Zoe', 'Zoe', 'Zoe']) == "Zoe"
    assert candidate(messages = ['A B C D E', 'F G H', 'I J K L M N O'],senders = ['Dave', 'Eve', 'Frank']) == "Frank"
    assert candidate(messages = ['Long message with multiple words indeed', 'Another long message with multiple words indeed'],senders = ['Anna', 'Anna']) == "Anna"
    assert candidate(messages = ['A quick brown fox jumps over the lazy dog', 'Lorem ipsum dolor sit amet', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice"
    assert candidate(messages = ['a b c d e f g h i j k l m n o p q r s t u v w x y z'],senders = ['Zachary']) == "Zachary"
    assert candidate(messages = ['This is a test message', 'Another message here', 'Short one'],senders = ['Alice', 'Bob', 'Charlie']) == "Alice"
    assert candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog'],senders = ['Grace', 'grace']) == "grace"
    assert candidate(messages = ['Single', 'Double double', 'Triple triple triple'],senders = ['Alice', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Short message', 'Longer message here', 'Even longer message to check', 'Short again'],senders = ['Bob', 'Charlie', 'Alice', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Short one', 'Another short one'],senders = ['Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['One', 'Two words', 'Three words here'],senders = ['Zara', 'Zara', 'Zara']) == "Zara"
    assert candidate(messages = ['Unique words in each message', 'Unique words here too', 'More unique words'],senders = ['Zoe', 'Yasmin', 'Xander']) == "Zoe"
    assert candidate(messages = ['One', 'Two words', 'Three words here', 'Four words in a sentence'],senders = ['Charlie', 'Alice', 'Bob', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Hello world', 'This is a longer message', 'Another message'],senders = ['Charlie', 'Bob', 'Charlie']) == "Bob"
    assert candidate(messages = ['Test message', 'Test message', 'Test message', 'Test message'],senders = ['Jack', 'Jack', 'Jack', 'Jack']) == "Jack"
    assert candidate(messages = ['One more message', 'Yet another message', 'Final message'],senders = ['Charlie', 'Charlie', 'Charlie']) == "Charlie"
    assert candidate(messages = ['Hello world', 'How are you doing today', 'Fine thank you'],senders = ['Charlie', 'Alice', 'Bob']) == "Alice"
    assert candidate(messages = ['Hello world', 'This is a test', 'Python programming'],senders = ['Alice', 'Bob', 'Charlie']) == "Bob"
    assert candidate(messages = ['Single', 'Two words', 'Three word phrase', 'Four word sentence structure'],senders = ['Zebra', 'Zebra', 'Zebra', 'Zebra']) == "Zebra"
    assert candidate(messages = ['Hello world', 'Hello Alice', 'Hello Bob'],senders = ['Bob', 'Alice', 'Bob']) == "Bob"
    assert candidate(messages = ['A B C D E F G', 'H I J K L M N', 'O P Q R S T U V W X Y Z'],senders = ['SenderA', 'SenderB', 'SenderC']) == "SenderC"
    assert candidate(messages = ['Unique message', 'Unique message', 'Unique message'],senders = ['Ian', 'Ian', 'Ian']) == "Ian"
    assert candidate(messages = ['Message one', 'Message two', 'Message three', 'Message four'],senders = ['Anna', 'Bob', 'Charlie', 'Bob']) == "Bob"
    assert candidate(messages = ['Long message to increase word count significantly', 'Short'],senders = ['Charlie', 'Charlie']) == "Charlie"
    assert candidate(messages = ['A quick brown fox jumps over the lazy dog', 'The quick brown fox jumps over the lazy dog', 'Lazy dog'],senders = ['Alice', 'Bob', 'Alice']) == "Alice"


