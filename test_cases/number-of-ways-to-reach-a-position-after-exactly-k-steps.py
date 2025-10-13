# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(startPos = 1,endPos = 2,k = 3) == 3
    assert candidate(startPos = 5,endPos = 5,k = 0) == 1
    assert candidate(startPos = 0,endPos = 0,k = 2) == 2
    assert candidate(startPos = 10,endPos = 1,k = 15) == 455
    assert candidate(startPos = 5,endPos = 5,k = 10) == 252
    assert candidate(startPos = 10,endPos = 1,k = 9) == 1
    assert candidate(startPos = 0,endPos = 0,k = 0) == 1
    assert candidate(startPos = 2,endPos = 5,k = 10) == 0
    assert candidate(startPos = 1,endPos = 2,k = 100) == 0
    assert candidate(startPos = 100,endPos = 50,k = 150) == 713790273
    assert candidate(startPos = 500,endPos = 450,k = 100) == 244856590
    assert candidate(startPos = -5,endPos = -10,k = 7) == 7
    assert candidate(startPos = 2,endPos = 1,k = 4) == 0
    assert candidate(startPos = 10,endPos = -10,k = 20) == 1
    assert candidate(startPos = 500,endPos = 400,k = 100) == 1
    assert candidate(startPos = -50,endPos = 50,k = 100) == 1
    assert candidate(startPos = 5,endPos = 5,k = 1) == 0
    assert candidate(startPos = 1000,endPos = 990,k = 20) == 15504
    assert candidate(startPos = -1,endPos = 1,k = 2) == 1
    assert candidate(startPos = 100,endPos = 50,k = 200) == 489348363
    assert candidate(startPos = -10,endPos = 10,k = 20) == 1
    assert candidate(startPos = 0,endPos = 1,k = 3) == 3
    assert candidate(startPos = 1,endPos = -1,k = 2) == 1
    assert candidate(startPos = 5,endPos = 15,k = 12) == 12
    assert candidate(startPos = -100,endPos = -200,k = 300) == 236868103
    assert candidate(startPos = 1,endPos = 2,k = 5) == 10
    assert candidate(startPos = 100,endPos = 100,k = 200) == 407336795
    assert candidate(startPos = -100,endPos = 100,k = 200) == 1
    assert candidate(startPos = 500,endPos = 400,k = 199) == 0
    assert candidate(startPos = 3,endPos = 3,k = 6) == 20
    assert candidate(startPos = 100,endPos = -100,k = 200) == 1
    assert candidate(startPos = 100,endPos = 100,k = 1) == 0
    assert candidate(startPos = -5,endPos = 5,k = 10) == 1
    assert candidate(startPos = 0,endPos = -10,k = 20) == 15504
    assert candidate(startPos = 50,endPos = 50,k = 50) == 605552882
    assert candidate(startPos = 1,endPos = 0,k = 3) == 3
    assert candidate(startPos = 100,endPos = 200,k = 150) == 297103639
    assert candidate(startPos = 1,endPos = -1,k = 4) == 4
    assert candidate(startPos = 3,endPos = -2,k = 10) == 0
