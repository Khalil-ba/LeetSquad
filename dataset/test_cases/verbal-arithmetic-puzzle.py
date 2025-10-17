def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(words = ['SEND', 'MORE'],result = "MONEY") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SEND', 'MORE'],result = "MONEY") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'A', 'A', 'A'],result = "AA") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'A', 'A', 'A'],result = "AA") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LEET', 'CODE'],result = "POINT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LEET', 'CODE'],result = "POINT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "HIALL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "HIALL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['AA', 'BB'],result = "CC") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['AA', 'BB'],result = "CC") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SIX', 'SEVEN', 'SEVEN'],result = "TWENTY") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SIX', 'SEVEN', 'SEVEN'],result = "TWENTY") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CAT', 'DOG'],result = "BIRD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CAT', 'DOG'],result = "BIRD") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ABA', 'B'],result = "ABC") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ABA', 'B'],result = "ABC") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'B'],result = "C") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'B'],result = "C") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ABC', 'BCD'],result = "DEE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ABC', 'BCD'],result = "DEE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "PEACE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "PEACE") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LONG', 'WORDS', 'HERE'],result = "ADDITION") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LONG', 'WORDS', 'HERE'],result = "ADDITION") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CASTLE', 'KNIGHT'],result = "BATTLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CASTLE', 'KNIGHT'],result = "BATTLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MAX', 'MIN'],result = "SUM") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MAX', 'MIN'],result = "SUM") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALGEBRA', 'GEOMETRY'],result = "MATHEMATICS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALGEBRA', 'GEOMETRY'],result = "MATHEMATICS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['BAT', 'BALL', 'BASE'],result = "TABLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['BAT', 'BALL', 'BASE'],result = "TABLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['EULER', 'GAUSS'],result = "ARITHMETIC") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['EULER', 'GAUSS'],result = "ARITHMETIC") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['COMPUTER', 'SCIENCE'],result = "DISCOVERY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['COMPUTER', 'SCIENCE'],result = "DISCOVERY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FAST', 'CAR'],result = "RACING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FAST', 'CAR'],result = "RACING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HEAL', 'HURT'],result = "BALANCE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HEAL', 'HURT'],result = "BALANCE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MATH', 'ENGLISH', 'SCIENCE'],result = "CURRICULUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MATH', 'ENGLISH', 'SCIENCE'],result = "CURRICULUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "PYTHON") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "PYTHON") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SAINT', 'SEER'],result = "VISION") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SAINT', 'SEER'],result = "VISION") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON', 'STAR'],result = "GALAXY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON', 'STAR'],result = "GALAXY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SNOW', 'ICE'],result = "COLD") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SNOW', 'ICE'],result = "COLD") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "HAPPY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "HAPPY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['A', 'BB', 'CCC', 'DDDD'],result = "E") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['A', 'BB', 'CCC', 'DDDD'],result = "E") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "DISPATCH") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "DISPATCH") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['KNIGHT', 'KNIGHT'],result = "WARLORD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['KNIGHT', 'KNIGHT'],result = "WARLORD") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SIX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SIX") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FIVE', 'NINE', 'ELEVEN'],result = "TWENTYFIVE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FIVE', 'NINE', 'ELEVEN'],result = "TWENTYFIVE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['TRUE', 'FALSE'],result = "PARADOX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['TRUE', 'FALSE'],result = "PARADOX") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['STAR', 'SHIP'],result = "GALAXY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['STAR', 'SHIP'],result = "GALAXY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['TEN', 'TEN', 'TEN'],result = "THIRTY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['TEN', 'TEN', 'TEN'],result = "THIRTY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HOUSE', 'DOG'],result = "FAMILY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HOUSE', 'DOG'],result = "FAMILY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MATH', 'ROCKS'],result = "LEARNING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MATH', 'ROCKS'],result = "LEARNING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SIX', 'EIGHT', 'TEN'],result = "TWENTYFOUR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SIX', 'EIGHT', 'TEN'],result = "TWENTYFOUR") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA'],result = "GRAPE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA'],result = "GRAPE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'],result = "SUMUP") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'],result = "SUMUP") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['UP', 'DOWN'],result = "ZERO") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['UP', 'DOWN'],result = "ZERO") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON'],result = "STAR") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON'],result = "STAR") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['BIG', 'DOG'],result = "ANIMAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['BIG', 'DOG'],result = "ANIMAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "PLANETS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "PLANETS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MOON', 'EARTH'],result = "UNIVERSE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MOON', 'EARTH'],result = "UNIVERSE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUITBOWL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUITBOWL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HAPPY', 'BIRTHDAY'],result = "CELEBRATE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HAPPY', 'BIRTHDAY'],result = "CELEBRATE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ABACAXI', 'MANGO', 'KIWI'],result = "FRUITS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ABACAXI', 'MANGO', 'KIWI'],result = "FRUITS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "PIG") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "PIG") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['UNIVERSAL', 'GALAXY', 'EARTH'],result = "COSMOS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['UNIVERSAL', 'GALAXY', 'EARTH'],result = "COSMOS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['BIRD', 'FLY', 'HIGH'],result = "FLIGHT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['BIRD', 'FLY', 'HIGH'],result = "FLIGHT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALICE', 'BOB'],result = "GAME") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALICE', 'BOB'],result = "GAME") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['RIGHT', 'WRONG'],result = "FALSE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['RIGHT', 'WRONG'],result = "FALSE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "CLAW") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "CLAW") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FRIENDSHIP") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FRIENDSHIP") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PHOENIX', 'DRAGON'],result = "MYTHICAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PHOENIX', 'DRAGON'],result = "MYTHICAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'ROCKS'],result = "PROGRAM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'ROCKS'],result = "PROGRAM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FLY', 'FLY', 'HIGH'],result = "SKYLINE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FLY', 'FLY', 'HIGH'],result = "SKYLINE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SEND', 'MORE', 'MONEY'],result = "TWICE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SEND', 'MORE', 'MONEY'],result = "TWICE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['UNO', 'DOS', 'TRES'],result = "SEIS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['UNO', 'DOS', 'TRES'],result = "SEIS") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['WIZARD', 'WAND'],result = "MAGIC") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['WIZARD', 'WAND'],result = "MAGIC") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LUCK', 'IN', 'THE', 'DRAW'],result = "SUCCESS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LUCK', 'IN', 'THE', 'DRAW'],result = "SUCCESS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['STAR', 'NIGHT'],result = "TWILIGHT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['STAR', 'NIGHT'],result = "TWILIGHT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON', 'STARS'],result = "SKYLINE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON', 'STARS'],result = "SKYLINE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['BLACK', 'WHITE', 'GRAY'],result = "COLORS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['BLACK', 'WHITE', 'GRAY'],result = "COLORS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['JAVA', 'PYTHON', 'CPLUSPLUS'],result = "PROGRAMMING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['JAVA', 'PYTHON', 'CPLUSPLUS'],result = "PROGRAMMING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['AARDVARK', 'ANTELOPE'],result = "MAMMALS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['AARDVARK', 'ANTELOPE'],result = "MAMMALS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['NINE', 'NINE'],result = "EIGHTEEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['NINE', 'NINE'],result = "EIGHTEEN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FICTION") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FICTION") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MAGIC', 'WAND'],result = "WIZARD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MAGIC', 'WAND'],result = "WIZARD") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['JAVA', 'PYTHON'],result = "SCRIPT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['JAVA', 'PYTHON'],result = "SCRIPT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['KNIGHT', 'BISHOP'],result = "CHECKMATE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['KNIGHT', 'BISHOP'],result = "CHECKMATE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['COMPUTER', 'SCIENCE', 'PROGRAMMING'],result = "DEVELOPMENT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['COMPUTER', 'SCIENCE', 'PROGRAMMING'],result = "DEVELOPMENT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['EARTH', 'MOON'],result = "UNIVERSE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['EARTH', 'MOON'],result = "UNIVERSE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SIXTY', 'SIXTY'],result = "ONETWENTY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SIXTY', 'SIXTY'],result = "ONETWENTY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SNOW', 'FALL'],result = "SNOWBALL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SNOW', 'FALL'],result = "SNOWBALL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FALCON', 'HAWK'],result = "BIRD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FALCON', 'HAWK'],result = "BIRD") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA'],result = "GRAPES") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA'],result = "GRAPES") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZEBRA', 'ELEPHANT'],result = "WILDLIFE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZEBRA', 'ELEPHANT'],result = "WILDLIFE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZERO', 'ONE'],result = "SUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZERO', 'ONE'],result = "SUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['EARTH', 'WATER'],result = "PLANET") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['EARTH', 'WATER'],result = "PLANET") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUIT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUIT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "TEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "TEN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "SUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "SUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MATH', 'IS', 'FUN'],result = "JOKES") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MATH', 'IS', 'FUN'],result = "JOKES") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['DOG', 'CAT'],result = "ANIMAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['DOG', 'CAT'],result = "ANIMAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['GREEN', 'BLUE', 'YELLOW'],result = "COLORS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['GREEN', 'BLUE', 'YELLOW'],result = "COLORS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "FIVE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "FIVE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MAT', 'ADD', 'SUB'],result = "SUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MAT', 'ADD', 'SUB'],result = "SUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['KANGAROO', 'KANGAROO', 'KANGAROO'],result = "JUMPOUTS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['KANGAROO', 'KANGAROO', 'KANGAROO'],result = "JUMPOUTS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['OCEAN', 'SEA', 'LAKE'],result = "WATERBODY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['OCEAN', 'SEA', 'LAKE'],result = "WATERBODY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['WITCH', 'WAND'],result = "MAGIC") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['WITCH', 'WAND'],result = "MAGIC") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HAPPY', 'JOY'],result = "BLISS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HAPPY', 'JOY'],result = "BLISS") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['STAR', 'PLANET', 'GALAXY'],result = "COSMOS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['STAR', 'PLANET', 'GALAXY'],result = "COSMOS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FAST', 'SLOW'],result = "BALANCE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FAST', 'SLOW'],result = "BALANCE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LEFT', 'RIGHT'],result = "EQUAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LEFT', 'RIGHT'],result = "EQUAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['COOL', 'DRINK'],result = "REFRESH") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['COOL', 'DRINK'],result = "REFRESH") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MAGICAL', 'REALM'],result = "MYSTERY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MAGICAL', 'REALM'],result = "MYSTERY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['LEARN', 'PYTHON'],result = "CODEING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['LEARN', 'PYTHON'],result = "CODEING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CAR', 'BIKE'],result = "VEHICLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CAR', 'BIKE'],result = "VEHICLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HEART', 'SOUL'],result = "LOVE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HEART', 'SOUL'],result = "LOVE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MATH', 'IS', 'FUN'],result = "GAMES") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MATH', 'IS', 'FUN'],result = "GAMES") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PARIS', 'BERLIN'],result = "ROME") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PARIS', 'BERLIN'],result = "ROME") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ABCDEFGHIJK', 'LMNOPQRS'],result = "TUVWXYZ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ABCDEFGHIJK', 'LMNOPQRS'],result = "TUVWXYZ") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON'],result = "AURA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON'],result = "AURA") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MATH', 'SCI', 'ENG'],result = "STUDY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MATH', 'SCI', 'ENG'],result = "STUDY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['UNICORN', 'PEGASUS'],result = "MYTHOLOGY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['UNICORN', 'PEGASUS'],result = "MYTHOLOGY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON', 'STAR'],result = "SKY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON', 'STAR'],result = "SKY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALPHA', 'BETA', 'GAMMA'],result = "DELTA") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALPHA', 'BETA', 'GAMMA'],result = "DELTA") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CLOCK', 'BELL'],result = "TICKTOCK") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CLOCK', 'BELL'],result = "TICKTOCK") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['DAY', 'NIGHT'],result = "TIMELESS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['DAY', 'NIGHT'],result = "TIMELESS") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['TEN', 'TWO'],result = "TWELVE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['TEN', 'TWO'],result = "TWELVE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FAST', 'RUN', 'JUMP'],result = "ATHLETE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FAST', 'RUN', 'JUMP'],result = "ATHLETE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA'],result = "CHERRY") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA'],result = "CHERRY") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALCHEMY', 'ENCHANT'],result = "MAGICAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALCHEMY', 'ENCHANT'],result = "MAGICAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "PEACEFUL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "PEACEFUL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'JAVA', 'CPLUS'],result = "PROGRAMMING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'JAVA', 'CPLUS'],result = "PROGRAMMING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON', 'STAR'],result = "UNIVERSAL") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON', 'STAR'],result = "UNIVERSAL") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MOUNTAIN', 'CLIMBER'],result = "ADVENTURE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MOUNTAIN', 'CLIMBER'],result = "ADVENTURE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'JAVA', 'CPLUSPLUS'],result = "PROGRAMMING") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'JAVA', 'CPLUSPLUS'],result = "PROGRAMMING") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "HALLO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "HALLO") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ONE', 'TWO', 'THREE'],result = "SIX") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ONE', 'TWO', 'THREE'],result = "SIX") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ABCDE', 'FGHIJ'],result = "KLMNO") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ABCDE', 'FGHIJ'],result = "KLMNO") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SKY', 'TREE'],result = "FOREST") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SKY', 'TREE'],result = "FOREST") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PI', 'E'],result = "CIRCLE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PI', 'E'],result = "CIRCLE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['RED', 'BLUE'],result = "COLOR") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['RED', 'BLUE'],result = "COLOR") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['JUMP', 'HIGH', 'LONG'],result = "JUMPROPE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['JUMP', 'HIGH', 'LONG'],result = "JUMPROPE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SUN', 'MOON', 'STAR'],result = "PLANET") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SUN', 'MOON', 'STAR'],result = "PLANET") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HIGH', 'LOW'],result = "AMPLITUDE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HIGH', 'LOW'],result = "AMPLITUDE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ALPACA', 'ANIMAL', 'ZOO'],result = "WILDLIFE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ALPACA', 'ANIMAL', 'ZOO'],result = "WILDLIFE") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HAPPY', 'JOY'],result = "HARMONY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HAPPY', 'JOY'],result = "HARMONY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['SPY', 'SPY'],result = "QUIZ") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['SPY', 'SPY'],result = "QUIZ") == True: {e}')
    
    total += 1
    try:
        result = candidate(words = ['APPLE', 'BANANA'],result = "FRUIT") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['APPLE', 'BANANA'],result = "FRUIT") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HAPPY', 'SAD'],result = "JOY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HAPPY', 'SAD'],result = "JOY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['CRYPT', 'GRAPH', 'DRY'],result = "DRYRUN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['CRYPT', 'GRAPH', 'DRY'],result = "DRYRUN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['GENIE', 'BOTTLE'],result = "WISHES") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['GENIE', 'BOTTLE'],result = "WISHES") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['RED', 'BLUE'],result = "GREEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['RED', 'BLUE'],result = "GREEN") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['HELLO', 'WORLD'],result = "HELLOWORLD") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['HELLO', 'WORLD'],result = "HELLOWORLD") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['BIRD', 'FLY'],result = "SKY") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['BIRD', 'FLY'],result = "SKY") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['MYTH', 'HERO'],result = "LEGEND") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['MYTH', 'HERO'],result = "LEGEND") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['Babbage', 'Difference', 'Engine'],result = "Calculator") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['Babbage', 'Difference', 'Engine'],result = "Calculator") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['PYTHON', 'JAVA', 'CPP'],result = "PROGRAM") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['PYTHON', 'JAVA', 'CPP'],result = "PROGRAM") == False: {e}')
    
    total += 1
    try:
        result = candidate(words = ['TREE', 'FOREST'],result = "GREEN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(words = ['TREE', 'FOREST'],result = "GREEN") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(words = ['SEND', 'MORE'],result = "MONEY") == True
    assert candidate(words = ['A', 'A', 'A', 'A'],result = "AA") == False
    assert candidate(words = ['LEET', 'CODE'],result = "POINT") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "HIALL") == False
    assert candidate(words = ['AA', 'BB'],result = "CC") == True
    assert candidate(words = ['SIX', 'SEVEN', 'SEVEN'],result = "TWENTY") == True
    assert candidate(words = ['CAT', 'DOG'],result = "BIRD") == True
    assert candidate(words = ['ABA', 'B'],result = "ABC") == True
    assert candidate(words = ['A', 'B'],result = "C") == True
    assert candidate(words = ['ABC', 'BCD'],result = "DEE") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "PEACE") == True
    assert candidate(words = ['LONG', 'WORDS', 'HERE'],result = "ADDITION") == False
    assert candidate(words = ['CASTLE', 'KNIGHT'],result = "BATTLE") == False
    assert candidate(words = ['MAX', 'MIN'],result = "SUM") == True
    assert candidate(words = ['ALGEBRA', 'GEOMETRY'],result = "MATHEMATICS") == False
    assert candidate(words = ['BAT', 'BALL', 'BASE'],result = "TABLE") == False
    assert candidate(words = ['EULER', 'GAUSS'],result = "ARITHMETIC") == False
    assert candidate(words = ['COMPUTER', 'SCIENCE'],result = "DISCOVERY") == False
    assert candidate(words = ['FAST', 'CAR'],result = "RACING") == False
    assert candidate(words = ['HEAL', 'HURT'],result = "BALANCE") == False
    assert candidate(words = ['MATH', 'ENGLISH', 'SCIENCE'],result = "CURRICULUM") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "PYTHON") == False
    assert candidate(words = ['SAINT', 'SEER'],result = "VISION") == False
    assert candidate(words = ['SUN', 'MOON', 'STAR'],result = "GALAXY") == False
    assert candidate(words = ['SNOW', 'ICE'],result = "COLD") == True
    assert candidate(words = ['HELLO', 'WORLD'],result = "HAPPY") == False
    assert candidate(words = ['A', 'BB', 'CCC', 'DDDD'],result = "E") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "DISPATCH") == False
    assert candidate(words = ['KNIGHT', 'KNIGHT'],result = "WARLORD") == False
    assert candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SIX") == False
    assert candidate(words = ['FIVE', 'NINE', 'ELEVEN'],result = "TWENTYFIVE") == False
    assert candidate(words = ['TRUE', 'FALSE'],result = "PARADOX") == False
    assert candidate(words = ['STAR', 'SHIP'],result = "GALAXY") == False
    assert candidate(words = ['TEN', 'TEN', 'TEN'],result = "THIRTY") == False
    assert candidate(words = ['HOUSE', 'DOG'],result = "FAMILY") == False
    assert candidate(words = ['MATH', 'ROCKS'],result = "LEARNING") == False
    assert candidate(words = ['SIX', 'EIGHT', 'TEN'],result = "TWENTYFOUR") == False
    assert candidate(words = ['APPLE', 'BANANA'],result = "GRAPE") == False
    assert candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE'],result = "SUMUP") == False
    assert candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False
    assert candidate(words = ['UP', 'DOWN'],result = "ZERO") == True
    assert candidate(words = ['SUN', 'MOON'],result = "STAR") == True
    assert candidate(words = ['BIG', 'DOG'],result = "ANIMAL") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "PLANETS") == False
    assert candidate(words = ['MOON', 'EARTH'],result = "UNIVERSE") == False
    assert candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUITBOWL") == False
    assert candidate(words = ['HAPPY', 'BIRTHDAY'],result = "CELEBRATE") == False
    assert candidate(words = ['ABACAXI', 'MANGO', 'KIWI'],result = "FRUITS") == False
    assert candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "PIG") == False
    assert candidate(words = ['UNIVERSAL', 'GALAXY', 'EARTH'],result = "COSMOS") == False
    assert candidate(words = ['BIRD', 'FLY', 'HIGH'],result = "FLIGHT") == False
    assert candidate(words = ['ALICE', 'BOB'],result = "GAME") == False
    assert candidate(words = ['RIGHT', 'WRONG'],result = "FALSE") == False
    assert candidate(words = ['CAT', 'DOG', 'MOUSE'],result = "CLAW") == False
    assert candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FRIENDSHIP") == False
    assert candidate(words = ['PHOENIX', 'DRAGON'],result = "MYTHICAL") == False
    assert candidate(words = ['PYTHON', 'ROCKS'],result = "PROGRAM") == False
    assert candidate(words = ['FLY', 'FLY', 'HIGH'],result = "SKYLINE") == False
    assert candidate(words = ['SEND', 'MORE', 'MONEY'],result = "TWICE") == False
    assert candidate(words = ['UNO', 'DOS', 'TRES'],result = "SEIS") == True
    assert candidate(words = ['WIZARD', 'WAND'],result = "MAGIC") == False
    assert candidate(words = ['LUCK', 'IN', 'THE', 'DRAW'],result = "SUCCESS") == False
    assert candidate(words = ['STAR', 'NIGHT'],result = "TWILIGHT") == False
    assert candidate(words = ['SUN', 'MOON', 'STARS'],result = "SKYLINE") == False
    assert candidate(words = ['BLACK', 'WHITE', 'GRAY'],result = "COLORS") == False
    assert candidate(words = ['JAVA', 'PYTHON', 'CPLUSPLUS'],result = "PROGRAMMING") == False
    assert candidate(words = ['AARDVARK', 'ANTELOPE'],result = "MAMMALS") == False
    assert candidate(words = ['NINE', 'NINE'],result = "EIGHTEEN") == False
    assert candidate(words = ['ALICE', 'BOB', 'CHARLIE'],result = "FICTION") == False
    assert candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False
    assert candidate(words = ['MAGIC', 'WAND'],result = "WIZARD") == False
    assert candidate(words = ['JAVA', 'PYTHON'],result = "SCRIPT") == False
    assert candidate(words = ['KNIGHT', 'BISHOP'],result = "CHECKMATE") == False
    assert candidate(words = ['COMPUTER', 'SCIENCE', 'PROGRAMMING'],result = "DEVELOPMENT") == False
    assert candidate(words = ['EARTH', 'MOON'],result = "UNIVERSE") == False
    assert candidate(words = ['SIXTY', 'SIXTY'],result = "ONETWENTY") == False
    assert candidate(words = ['SNOW', 'FALL'],result = "SNOWBALL") == False
    assert candidate(words = ['FALCON', 'HAWK'],result = "BIRD") == False
    assert candidate(words = ['APPLE', 'BANANA'],result = "GRAPES") == False
    assert candidate(words = ['ZEBRA', 'ELEPHANT'],result = "WILDLIFE") == False
    assert candidate(words = ['ZERO', 'ONE'],result = "SUM") == False
    assert candidate(words = ['EARTH', 'WATER'],result = "PLANET") == False
    assert candidate(words = ['APPLE', 'BANANA', 'CHERRY'],result = "FRUIT") == False
    assert candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "TEN") == False
    assert candidate(words = ['ONE', 'TWO', 'THREE', 'FOUR'],result = "SUM") == False
    assert candidate(words = ['MATH', 'IS', 'FUN'],result = "JOKES") == False
    assert candidate(words = ['DOG', 'CAT'],result = "ANIMAL") == False
    assert candidate(words = ['GREEN', 'BLUE', 'YELLOW'],result = "COLORS") == False
    assert candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "FIVE") == False
    assert candidate(words = ['MAT', 'ADD', 'SUB'],result = "SUM") == False
    assert candidate(words = ['KANGAROO', 'KANGAROO', 'KANGAROO'],result = "JUMPOUTS") == False
    assert candidate(words = ['OCEAN', 'SEA', 'LAKE'],result = "WATERBODY") == False
    assert candidate(words = ['WITCH', 'WAND'],result = "MAGIC") == True
    assert candidate(words = ['HAPPY', 'JOY'],result = "BLISS") == True
    assert candidate(words = ['STAR', 'PLANET', 'GALAXY'],result = "COSMOS") == False
    assert candidate(words = ['FAST', 'SLOW'],result = "BALANCE") == False
    assert candidate(words = ['LEFT', 'RIGHT'],result = "EQUAL") == False
    assert candidate(words = ['COOL', 'DRINK'],result = "REFRESH") == False
    assert candidate(words = ['MAGICAL', 'REALM'],result = "MYSTERY") == False
    assert candidate(words = ['LEARN', 'PYTHON'],result = "CODEING") == False
    assert candidate(words = ['CAR', 'BIKE'],result = "VEHICLE") == False
    assert candidate(words = ['HEART', 'SOUL'],result = "LOVE") == False
    assert candidate(words = ['MATH', 'IS', 'FUN'],result = "GAMES") == False
    assert candidate(words = ['PARIS', 'BERLIN'],result = "ROME") == False
    assert candidate(words = ['ABCDEFGHIJK', 'LMNOPQRS'],result = "TUVWXYZ") == False
    assert candidate(words = ['SUN', 'MOON'],result = "AURA") == True
    assert candidate(words = ['MATH', 'SCI', 'ENG'],result = "STUDY") == False
    assert candidate(words = ['UNICORN', 'PEGASUS'],result = "MYTHOLOGY") == False
    assert candidate(words = ['SUN', 'MOON', 'STAR'],result = "SKY") == False
    assert candidate(words = ['ALPHA', 'BETA', 'GAMMA'],result = "DELTA") == True
    assert candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False
    assert candidate(words = ['CLOCK', 'BELL'],result = "TICKTOCK") == False
    assert candidate(words = ['DAY', 'NIGHT'],result = "TIMELESS") == False
    assert candidate(words = ['TEN', 'TWO'],result = "TWELVE") == False
    assert candidate(words = ['FAST', 'RUN', 'JUMP'],result = "ATHLETE") == False
    assert candidate(words = ['APPLE', 'BANANA'],result = "CHERRY") == True
    assert candidate(words = ['ALCHEMY', 'ENCHANT'],result = "MAGICAL") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "PEACEFUL") == False
    assert candidate(words = ['PYTHON', 'JAVA', 'CPLUS'],result = "PROGRAMMING") == False
    assert candidate(words = ['PYTHON', 'JAVA'],result = "SCRIPT") == False
    assert candidate(words = ['SUN', 'MOON', 'STAR'],result = "UNIVERSAL") == False
    assert candidate(words = ['MOUNTAIN', 'CLIMBER'],result = "ADVENTURE") == False
    assert candidate(words = ['PYTHON', 'JAVA', 'CPLUSPLUS'],result = "PROGRAMMING") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "HALLO") == False
    assert candidate(words = ['ONE', 'TWO', 'THREE'],result = "SIX") == False
    assert candidate(words = ['ABCDE', 'FGHIJ'],result = "KLMNO") == False
    assert candidate(words = ['SKY', 'TREE'],result = "FOREST") == False
    assert candidate(words = ['PI', 'E'],result = "CIRCLE") == False
    assert candidate(words = ['FOUR', 'FIVE', 'SIX'],result = "FIFTEEN") == False
    assert candidate(words = ['RED', 'BLUE'],result = "COLOR") == False
    assert candidate(words = ['JUMP', 'HIGH', 'LONG'],result = "JUMPROPE") == False
    assert candidate(words = ['SUN', 'MOON', 'STAR'],result = "PLANET") == False
    assert candidate(words = ['HIGH', 'LOW'],result = "AMPLITUDE") == False
    assert candidate(words = ['ALPACA', 'ANIMAL', 'ZOO'],result = "WILDLIFE") == False
    assert candidate(words = ['HAPPY', 'JOY'],result = "HARMONY") == False
    assert candidate(words = ['SPY', 'SPY'],result = "QUIZ") == True
    assert candidate(words = ['APPLE', 'BANANA'],result = "FRUIT") == False
    assert candidate(words = ['HAPPY', 'SAD'],result = "JOY") == False
    assert candidate(words = ['CRYPT', 'GRAPH', 'DRY'],result = "DRYRUN") == False
    assert candidate(words = ['GENIE', 'BOTTLE'],result = "WISHES") == False
    assert candidate(words = ['RED', 'BLUE'],result = "GREEN") == False
    assert candidate(words = ['HELLO', 'WORLD'],result = "HELLOWORLD") == False
    assert candidate(words = ['BIRD', 'FLY'],result = "SKY") == False
    assert candidate(words = ['MYTH', 'HERO'],result = "LEGEND") == False
    assert candidate(words = ['Babbage', 'Difference', 'Engine'],result = "Calculator") == False
    assert candidate(words = ['ZERO', 'ONE', 'TWO', 'THREE'],result = "SUM") == False
    assert candidate(words = ['PYTHON', 'JAVA', 'CPP'],result = "PROGRAM") == False
    assert candidate(words = ['TREE', 'FOREST'],result = "GREEN") == False


