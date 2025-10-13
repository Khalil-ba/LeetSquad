# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(year = 2023,month = 11) == 30
    assert candidate(year = 1583,month = 8) == 31
    assert candidate(year = 1583,month = 1) == 31
    assert candidate(year = 1583,month = 12) == 31
    assert candidate(year = 2020,month = 4) == 30
    assert candidate(year = 1992,month = 7) == 31
    assert candidate(year = 1600,month = 2) == 29
    assert candidate(year = 2100,month = 6) == 30
    assert candidate(year = 2024,month = 2) == 29
    assert candidate(year = 2023,month = 4) == 30
    assert candidate(year = 2020,month = 2) == 29
    assert candidate(year = 2100,month = 4) == 30
    assert candidate(year = 2100,month = 12) == 31
    assert candidate(year = 1900,month = 2) == 28
    assert candidate(year = 2019,month = 12) == 31
    assert candidate(year = 2000,month = 2) == 29
    assert candidate(year = 2024,month = 4) == 30
    assert candidate(year = 2040,month = 2) == 29
    assert candidate(year = 2021,month = 2) == 28
    assert candidate(year = 2004,month = 2) == 29
    assert candidate(year = 1900,month = 12) == 31
    assert candidate(year = 1920,month = 2) == 29
    assert candidate(year = 2060,month = 2) == 29
    assert candidate(year = 2012,month = 9) == 30
    assert candidate(year = 1800,month = 2) == 28
    assert candidate(year = 1996,month = 2) == 29
    assert candidate(year = 1848,month = 2) == 29
    assert candidate(year = 2032,month = 2) == 29
    assert candidate(year = 1583,month = 2) == 28
    assert candidate(year = 1924,month = 4) == 30
    assert candidate(year = 1980,month = 2) == 29
    assert candidate(year = 1700,month = 2) == 28
    assert candidate(year = 2025,month = 2) == 28
