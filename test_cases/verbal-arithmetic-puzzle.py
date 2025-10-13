# Import the utils module for prompts
from utils import *

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
