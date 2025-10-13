# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(sentence1 = "Similar sentences",sentence2 = "Similar similar sentences") == True
    assert candidate(sentence1 = "Start end",sentence2 = "Start middle end") == True
    assert candidate(sentence1 = "Eating right now",sentence2 = "Eating") == True
    assert candidate(sentence1 = "A quick brown fox",sentence2 = "A quick brown fox jumps over the lazy dog") == True
    assert candidate(sentence1 = "Quick brown fox",sentence2 = "Quick brown fox jumps over the lazy dog") == True
    assert candidate(sentence1 = "of",sentence2 = "A lot of words") == False
    assert candidate(sentence1 = "Similarity check",sentence2 = "check Similarity") == False
    assert candidate(sentence1 = "Similar sentences",sentence2 = "Sentences Similar") == False
    assert candidate(sentence1 = "Similar sentences",sentence2 = "Similar very very similar sentences") == True
    assert candidate(sentence1 = "Python is great",sentence2 = "Python is very very great") == True
    assert candidate(sentence1 = "One two three",sentence2 = "One three") == True
    assert candidate(sentence1 = "Python is great",sentence2 = "is great") == True
    assert candidate(sentence1 = "Similar sentences",sentence2 = "Sentences that are Similar") == False
    assert candidate(sentence1 = "One",sentence2 = "One two three") == True
    assert candidate(sentence1 = "One",sentence2 = "One") == True
    assert candidate(sentence1 = "Test",sentence2 = "Test test") == True
    assert candidate(sentence1 = "Single",sentence2 = "Single word") == True
    assert candidate(sentence1 = "Test test test",sentence2 = "Test test test test") == True
    assert candidate(sentence1 = "Python programming",sentence2 = "programming") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is") == True
    assert candidate(sentence1 = "A B C",sentence2 = "A B X C") == True
    assert candidate(sentence1 = "One two three",sentence2 = "One two three four") == True
    assert candidate(sentence1 = "Similar sentences",sentence2 = "Similar very similar sentences") == True
    assert candidate(sentence1 = "My name is Haley",sentence2 = "My Haley") == True
    assert candidate(sentence1 = "Same Same Same",sentence2 = "Same") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is a dummy test") == True
    assert candidate(sentence1 = "Same same",sentence2 = "Same same same") == True
    assert candidate(sentence1 = "Overlap here",sentence2 = "Overlap word here") == True
    assert candidate(sentence1 = "Hello World",sentence2 = "World") == True
    assert candidate(sentence1 = "Hello World",sentence2 = "Hello") == True
    assert candidate(sentence1 = "Same same",sentence2 = "Same same") == True
    assert candidate(sentence1 = "Hello World",sentence2 = "Hello amazing World") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is a simple test") == True
    assert candidate(sentence1 = "First Second Third",sentence2 = "First Third") == True
    assert candidate(sentence1 = "Match here",sentence2 = "Match something here") == True
    assert candidate(sentence1 = "Hello World",sentence2 = "Hello from the World") == True
    assert candidate(sentence1 = "Alice in Wonderland",sentence2 = "Alice is in Wonderland") == True
    assert candidate(sentence1 = "Left Right",sentence2 = "Left Middle Right") == True
    assert candidate(sentence1 = "The quick brown fox",sentence2 = "The quick brown fox jumps over") == True
    assert candidate(sentence1 = "To be or not to be that is the question",sentence2 = "To be that is the question") == True
    assert candidate(sentence1 = "The world is a stage",sentence2 = "The world is a stage and all the men and women merely players") == True
    assert candidate(sentence1 = "One two three",sentence2 = "One two insert three") == True
    assert candidate(sentence1 = "The quick brown fox",sentence2 = "The quick brown fox jumps") == True
    assert candidate(sentence1 = "No pain no gain",sentence2 = "No pain no gain but sometimes the pain is not worth the gain") == True
    assert candidate(sentence1 = "Let us play",sentence2 = "Let us play a game") == True
    assert candidate(sentence1 = "Mary had a little lamb",sentence2 = "Mary lamb") == True
    assert candidate(sentence1 = "All roads lead to Rome",sentence2 = "All roads lead to Rome but not all roads are the same") == True
    assert candidate(sentence1 = "Unique words only",sentence2 = "Unique unique words only") == True
    assert candidate(sentence1 = "Quick brown fox jumps over the lazy dog",sentence2 = "Quick brown fox jumps over the lazy quick brown dog") == True
    assert candidate(sentence1 = "a b c d e f g h i j",sentence2 = "a b c X Y Z d e f g h i j") == True
    assert candidate(sentence1 = "OnlyOneWordHere",sentence2 = "Only One Word Here") == False
    assert candidate(sentence1 = "Actions speak louder than words",sentence2 = "Actions speak") == True
    assert candidate(sentence1 = "One two three four five",sentence2 = "One two four five") == True
    assert candidate(sentence1 = "Python programming is fun",sentence2 = "Python programming is very fun") == True
    assert candidate(sentence1 = "Actions speak louder than words",sentence2 = "Actions speak louder than words but intentions matter") == True
    assert candidate(sentence1 = "Python is fun",sentence2 = "Python programming is really fun") == False
    assert candidate(sentence1 = "OpenAI is great",sentence2 = "OpenAI is indeed indeed great") == True
    assert candidate(sentence1 = "Do or do not there is no try",sentence2 = "Do or do not there is no no try") == True
    assert candidate(sentence1 = "Quick brown fox jumps over the lazy dog",sentence2 = "Quick fox jumps over the lazy dog") == True
    assert candidate(sentence1 = "Time flies when you are having fun",sentence2 = "Time flies") == True
    assert candidate(sentence1 = "The world is a book and those who do not travel read only one page",sentence2 = "The world is a book and those who do not travel read only one chapter") == False
    assert candidate(sentence1 = "Python programming is fun and effective",sentence2 = "Python programming effective") == True
    assert candidate(sentence1 = "Complex complex case",sentence2 = "Complex even more complex case") == True
    assert candidate(sentence1 = "Time heals all wounds",sentence2 = "Time heals all wounds but time is also a thief") == True
    assert candidate(sentence1 = "SingleWord",sentence2 = "SingleWord") == True
    assert candidate(sentence1 = "The cat sat on the mat",sentence2 = "The cat sat on the blue mat") == True
    assert candidate(sentence1 = "First and last",sentence2 = "First something in the middle last") == False
    assert candidate(sentence1 = "Once upon a time",sentence2 = "Once upon a time in a land far far away") == True
    assert candidate(sentence1 = "I think therefore I am",sentence2 = "I think therefore I am six") == True
    assert candidate(sentence1 = "Single word match",sentence2 = "Single word match") == True
    assert candidate(sentence1 = "Silence is golden",sentence2 = "Silence is golden in the morning") == True
    assert candidate(sentence1 = "A quick brown fox jumps",sentence2 = "A quick brown fox quick brown fox jumps") == True
    assert candidate(sentence1 = "Complex problem solving",sentence2 = "Complex problem problem solving") == True
    assert candidate(sentence1 = "Short",sentence2 = "Short and sweet") == True
    assert candidate(sentence1 = "a",sentence2 = "a b c d e f g h i j k l m n o p q r s t u v w x y z") == True
    assert candidate(sentence1 = "Overlap at end",sentence2 = "Continue overlap at end") == False
    assert candidate(sentence1 = "Happy birthday",sentence2 = "Happy birthday dear") == True
    assert candidate(sentence1 = "First word last word",sentence2 = "First first word last word") == True
    assert candidate(sentence1 = "To be or not to be",sentence2 = "To be or not to be that is the question") == True
    assert candidate(sentence1 = "May the force be with you",sentence2 = "May the force") == True
    assert candidate(sentence1 = "Python programming is fun",sentence2 = "Python programming is really really fun") == True
    assert candidate(sentence1 = "Alibaba Cloud offers various cloud services",sentence2 = "Alibaba Cloud offers cloud computing and storage services") == False
    assert candidate(sentence1 = "The early morning sun was a beautiful sight",sentence2 = "The early morning sun was a beautiful golden sight") == True
    assert candidate(sentence1 = "This is a long sentence with multiple words in it",sentence2 = "This long sentence with multiple words in it") == True
    assert candidate(sentence1 = "Lorem ipsum dolor sit amet",sentence2 = "Lorem ipsum dolor sit amet consectetur adipiscing elit") == True
    assert candidate(sentence1 = "Hello from the other side",sentence2 = "Hello from this side") == False
    assert candidate(sentence1 = "One two three",sentence2 = "One two X Y Z three") == True
    assert candidate(sentence1 = "Beginning middle end",sentence2 = "Beginning middle middle middle end") == True
    assert candidate(sentence1 = "Unique sentence",sentence2 = "Unique special sentence") == True
    assert candidate(sentence1 = "The quick brown fox jumps over the lazy dog",sentence2 = "The quick brown fox jumps over the lazy") == True
    assert candidate(sentence1 = "Start with a sentence",sentence2 = "Start with a really long sentence") == True
    assert candidate(sentence1 = "Python is fun",sentence2 = "Python is an amazing and fun language") == False
    assert candidate(sentence1 = "All your base are belong to us",sentence2 = "All base are belong to us") == True
    assert candidate(sentence1 = "Longer sentence with multiple words",sentence2 = "Longer sentence with even more multiple words") == True
    assert candidate(sentence1 = "She sells sea shells by the sea shore",sentence2 = "She sells green sea shells by the sea shore") == True
    assert candidate(sentence1 = "Complex algorithm design and analysis",sentence2 = "Complex algorithm") == True
    assert candidate(sentence1 = "In the middle",sentence2 = "In the middle of nowhere") == True
    assert candidate(sentence1 = "First Last",sentence2 = "First in between Last") == True
    assert candidate(sentence1 = "I love to code",sentence2 = "I love to code code code") == True
    assert candidate(sentence1 = "Unique words only",sentence2 = "Unique words in between only") == True
    assert candidate(sentence1 = "The quick brown fox",sentence2 = "The quick brown fox jumps over the lazy dog") == True
    assert candidate(sentence1 = "Single",sentence2 = "Single single single") == True
    assert candidate(sentence1 = "Life is a journey",sentence2 = "Life is a journey not a destination") == True
    assert candidate(sentence1 = "A B C D E",sentence2 = "A B X Y Z C D E") == True
    assert candidate(sentence1 = "The rain in Spain stays mainly in the plain",sentence2 = "The rain in Spain falls mainly in the plain") == False
    assert candidate(sentence1 = "A quick movement of the enemy will jeopardize six gunboats",sentence2 = "A quick movement of the enemy will jeopardize") == True
    assert candidate(sentence1 = "Short",sentence2 = "Very very short") == False
    assert candidate(sentence1 = "Do or do not there is no try",sentence2 = "Do or do not there is no other way") == False
    assert candidate(sentence1 = "Python programming is fun",sentence2 = "Python programming is very very fun") == True
    assert candidate(sentence1 = "Start coding",sentence2 = "Start coding today") == True
    assert candidate(sentence1 = "Happy new year",sentence2 = "Happy new new new year") == True
    assert candidate(sentence1 = "I love programming in Python",sentence2 = "I love programming in Java Python") == True
    assert candidate(sentence1 = "Actions speak louder than words",sentence2 = "Actions speak louder than words but words can inspire actions") == True
    assert candidate(sentence1 = "Python is great",sentence2 = "Programming in Python is great") == True
    assert candidate(sentence1 = "Data engineering and data science",sentence2 = "Data engineering") == True
    assert candidate(sentence1 = "One two three four",sentence2 = "One two five six seven eight three four") == True
    assert candidate(sentence1 = "I love coding",sentence2 = "I love coding in Python") == True
    assert candidate(sentence1 = "Prefix and suffix",sentence2 = "Prefix and more words suffix") == True
    assert candidate(sentence1 = "One two three four",sentence2 = "One two three four five six") == True
    assert candidate(sentence1 = "The quick brown fox jumps over the lazy dog",sentence2 = "The quick brown fox jumps over lazy dog") == True
    assert candidate(sentence1 = "Catch me if you can",sentence2 = "Catch me") == True
    assert candidate(sentence1 = "This is a complex example",sentence2 = "This is an extremely complex example") == False
    assert candidate(sentence1 = "Match start",sentence2 = "Match start middle") == True
    assert candidate(sentence1 = "x y z",sentence2 = "a b c x y z") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is only a test") == True
    assert candidate(sentence1 = "The quick brown fox jumps over the lazy dog",sentence2 = "The quick brown fox jumps high over the lazy dog") == True
    assert candidate(sentence1 = "Python is great",sentence2 = "Python is the best language great") == True
    assert candidate(sentence1 = "The cat in the hat sat on the mat",sentence2 = "The cat sat on the mat") == True
    assert candidate(sentence1 = "The pen is mightier than the sword",sentence2 = "The pen is mightier than the sword but silence is golden") == True
    assert candidate(sentence1 = "Machine learning is transforming industries",sentence2 = "Machine learning transforming industries") == True
    assert candidate(sentence1 = "The quick brown fox",sentence2 = "The quick brown lazy dog") == False
    assert candidate(sentence1 = "One two three",sentence2 = "One two two three") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is a longer test sentence") == False
    assert candidate(sentence1 = "Insert this sentence",sentence2 = "Insert some words this sentence") == True
    assert candidate(sentence1 = "An apple a day keeps the doctor away",sentence2 = "An apple a day") == True
    assert candidate(sentence1 = "Learning new things every day",sentence2 = "Learning new things every single day") == True
    assert candidate(sentence1 = "Match end",sentence2 = "Middle match end") == False
    assert candidate(sentence1 = "Silence is golden",sentence2 = "Silence is golden but sometimes it's better to speak your mind") == True
    assert candidate(sentence1 = "Test",sentence2 = "Test test test") == True
    assert candidate(sentence1 = "A B C D E",sentence2 = "A B C X Y Z D E") == True
    assert candidate(sentence1 = "Start with this",sentence2 = "Start with something in the middle this") == True
    assert candidate(sentence1 = "Qwen is a large language model",sentence2 = "Qwen is a language model") == True
    assert candidate(sentence1 = "The cat sat on the mat",sentence2 = "The cat sat on the brown mat") == True
    assert candidate(sentence1 = "Last word",sentence2 = "Last last last word") == True
    assert candidate(sentence1 = "Python is great for data science",sentence2 = "Python is great") == True
    assert candidate(sentence1 = "Quick brown fox jumps over the lazy dog",sentence2 = "Quick brown fox quickly jumps over the lazy dog") == True
    assert candidate(sentence1 = "It is a truth universally acknowledged",sentence2 = "It is a universally acknowledged") == True
    assert candidate(sentence1 = "Start and finish",sentence2 = "Start middle and finish") == True
    assert candidate(sentence1 = "SingleWord",sentence2 = "SingleWordInserted") == False
    assert candidate(sentence1 = "End with a sentence",sentence2 = "End with a sentence and more words") == True
    assert candidate(sentence1 = "Overlap at start",sentence2 = "Overlap at start and continue") == True
    assert candidate(sentence1 = "We hold these truths to be self evident",sentence2 = "We hold these self evident") == True
    assert candidate(sentence1 = "Once upon a time in a land far far away",sentence2 = "Once upon a time") == True
    assert candidate(sentence1 = "Java is a high level programming language",sentence2 = "Java is a high level programming language that is platform independent") == True
    assert candidate(sentence1 = "Similar beginning and end",sentence2 = "Similar beginning with extra words and end") == True
    assert candidate(sentence1 = "Hello from the other side",sentence2 = "Hello from the very very other side") == True
    assert candidate(sentence1 = "Quick brown fox jumps over lazy dog",sentence2 = "Quick brown fox jumps over the lazy dog") == True
    assert candidate(sentence1 = "Silence is golden",sentence2 = "Silence") == True
    assert candidate(sentence1 = "Middle insertion is key",sentence2 = "Middle insertion of some text is key") == True
    assert candidate(sentence1 = "To be or not to be that is the question",sentence2 = "To be or not to be") == True
    assert candidate(sentence1 = "This is a simple test",sentence2 = "This is an extremely simple and detailed test") == False
    assert candidate(sentence1 = "It was the best of times it was the worst of times",sentence2 = "It was the best of times") == True
    assert candidate(sentence1 = "Quick brown fox jumps over the lazy dog",sentence2 = "Quick brown fox jumps over the lazy brown dog") == True
    assert candidate(sentence1 = "Learning new things is fun",sentence2 = "Learning fun") == True
    assert candidate(sentence1 = "Life is a journey not a destination",sentence2 = "Life is a journey of ups and downs not a destination") == True
    assert candidate(sentence1 = "She sells sea shells by the sea shore",sentence2 = "She sells sea") == True
    assert candidate(sentence1 = "In the beginning God created the heaven and the earth",sentence2 = "In the beginning God created the earth") == True
    assert candidate(sentence1 = "Insert sentence here",sentence2 = "Insert sentence in the middle sentence here") == True
    assert candidate(sentence1 = "End with this",sentence2 = "End with this and something more") == True
    assert candidate(sentence1 = "Python is fun",sentence2 = "Python is very very fun") == True
    assert candidate(sentence1 = "Advanced machine learning techniques",sentence2 = "Advanced machine learning deep learning techniques") == True
    assert candidate(sentence1 = "Hello from the other side",sentence2 = "Hello from the other side my old friend") == True
    assert candidate(sentence1 = "Single word",sentence2 = "Single single word") == True
    assert candidate(sentence1 = "Time heals all wounds",sentence2 = "Time heals all wounds but sometimes it's better to face them head on") == True
    assert candidate(sentence1 = "One two three four five",sentence2 = "One two six seven eight nine five") == False
    assert candidate(sentence1 = "Same at the start",sentence2 = "Same at the start but different end") == True
    assert candidate(sentence1 = "All animals are equal",sentence2 = "All animals are equal but some animals are more equal than others") == True
    assert candidate(sentence1 = "The rain in Spain stays mainly in the plain",sentence2 = "The rain in Spain stays") == True
    assert candidate(sentence1 = "Multiple words in between",sentence2 = "Multiple multiple words in between") == True
    assert candidate(sentence1 = "Natural language processing is fascinating",sentence2 = "Natural language processing") == True
    assert candidate(sentence1 = "Hello my friend",sentence2 = "Hello my dear friend") == True
    assert candidate(sentence1 = "This is a test",sentence2 = "This is an amazing test") == False
    assert candidate(sentence1 = "Front and back",sentence2 = "Front middle back") == False
    assert candidate(sentence1 = "Complex sentences are fun",sentence2 = "Complex sentences with more words in between are fun") == True
    assert candidate(sentence1 = "Alice went to the market",sentence2 = "Alice went to the market to buy apples") == True
    assert candidate(sentence1 = "The early morning light",sentence2 = "The early morning light is so peaceful") == True
    assert candidate(sentence1 = "Same same same",sentence2 = "Same Same") == False
    assert candidate(sentence1 = "Same at the end",sentence2 = "Different start same at the end") == False
    assert candidate(sentence1 = "Beautiful day in the neighborhood",sentence2 = "Beautiful day in the beautiful neighborhood") == True
    assert candidate(sentence1 = "First second third",sentence2 = "First first first second third") == True
    assert candidate(sentence1 = "Hello from the other side",sentence2 = "Hello") == True
    assert candidate(sentence1 = "I have a dream",sentence2 = "I have a dream that one day this nation will rise up and live out the true meaning of its creed") == True
    assert candidate(sentence1 = "May the force be with you",sentence2 = "May the be with you") == True
    assert candidate(sentence1 = "OpenAI develops AI models",sentence2 = "OpenAI develops cutting edge AI models") == True
    assert candidate(sentence1 = "May the Force be with you",sentence2 = "May the Force be with you always") == True
    assert candidate(sentence1 = "Keep it simple",sentence2 = "Keep it simple stupid") == True
    assert candidate(sentence1 = "A short sentence",sentence2 = "A very very very short sentence") == True
