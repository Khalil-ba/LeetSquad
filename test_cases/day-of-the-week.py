# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(day = 31,month = 12,year = 2100) == "Friday"
    assert candidate(day = 15,month = 8,year = 1993) == "Sunday"
    assert candidate(day = 10,month = 9,year = 2023) == "Sunday"
    assert candidate(day = 18,month = 7,year = 1999) == "Sunday"
    assert candidate(day = 31,month = 8,year = 2019) == "Saturday"
    assert candidate(day = 4,month = 7,year = 2023) == "Tuesday"
    assert candidate(day = 25,month = 12,year = 2023) == "Monday"
    assert candidate(day = 29,month = 2,year = 2004) == "Sunday"
    assert candidate(day = 1,month = 1,year = 1971) == "Friday"
    assert candidate(day = 29,month = 2,year = 2000) == "Tuesday"
    assert candidate(day = 28,month = 2,year = 1900) == "Wednesday"
    assert candidate(day = 14,month = 2,year = 2000) == "Monday"
    assert candidate(day = 31,month = 10,year = 1984) == "Wednesday"
    assert candidate(day = 1,month = 3,year = 1999) == "Monday"
    assert candidate(day = 14,month = 3,year = 2047) == "Thursday"
    assert candidate(day = 15,month = 6,year = 2050) == "Wednesday"
    assert candidate(day = 30,month = 4,year = 2020) == "Thursday"
    assert candidate(day = 7,month = 11,year = 2025) == "Friday"
    assert candidate(day = 1,month = 9,year = 2001) == "Saturday"
