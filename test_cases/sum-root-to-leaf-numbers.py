# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == 522
    assert candidate(root = tree_node([9, 3, 20, None, None, 15, 7])) == 2315
    assert candidate(root = tree_node([1, 2, 3])) == 25
    assert candidate(root = tree_node([1, 0, 0])) == 20
    assert candidate(root = tree_node([1, 0])) == 10
    assert candidate(root = tree_node([5, 2, 8, 3, 5, 4, 9, 0, None, None, 6])) == 11659
    assert candidate(root = tree_node([1, 0, 1])) == 21
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1])) == 422
    assert candidate(root = tree_node([4, 9, 0, 5, 1])) == 1026
    assert candidate(root = tree_node([1, None, 2])) == 12
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])) == 17231
    assert candidate(root = tree_node([0])) == 0
    assert candidate(root = tree_node([5, 3, 7, 2, 4, 6, 8])) == 2220
    assert candidate(root = tree_node([4, 3, None, 1, 2])) == 863
    assert candidate(root = tree_node([2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6])) == 19350
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 22655
    assert candidate(root = tree_node([3, 1, 5, None, 2, 4, 6, 7, 8, 9])) == 10160
    assert candidate(root = tree_node([8, None, 5, None, 3, None, 1])) == 8531
    assert candidate(root = tree_node([2, 3, 5, 6, 4, None, 9, 8, 7, 1, 0, None, None, None, None, None, None, 5])) == 30749
    assert candidate(root = tree_node([9, 4, 0, 9, 8, 6, 0, 1, 3, 8, 9, 0, 6, 7, 9])) == 74103
    assert candidate(root = tree_node([5, 5, 5, 5, 5, None, 5, 5, None, 5, 5, 5, 5, None, None, 5])) == 77775
    assert candidate(root = tree_node([1, 3, None, None, 5, 2, None, None, 8, 6, 9])) == 270575
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None])) == 123456789
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 157777
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 123456789
    assert candidate(root = tree_node([5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 43076
    assert candidate(root = tree_node([1, 9, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 123485
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == 541795
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 0, 1])) == 27594
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])) == 10472
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, None, None, None])) == 31520
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5])) == 78398
    assert candidate(root = tree_node([6, 0, 8, None, 7, 1, 3, None, None, 2, 5, None, None, None, 4])) == 76229
    assert candidate(root = tree_node([1, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, 0, 9, 8, 7, 6, 5, 4, 3])) == 104082
    assert candidate(root = tree_node([2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 23456789
    assert candidate(root = tree_node([5, 9, 6, 7, 4, 0, 2, None, None, 8, 1, None, None, 3, 9])) == 24298
    assert candidate(root = tree_node([1, 9, 8, 2, 8, 7, 9, 4, 4, 6, 8, 3, 0, 7, 9, None, None, None, None, None, 4, None, None, None, None, 0, None, 3, None, None, 2, None, 1, None, 9])) == 431324
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 1499985
    assert candidate(root = tree_node([1, None, 3, None, 5, None, 7, None, 9, None, 11, None, 13, None, 15, None, 17, None, 19])) == 1358024689
    assert candidate(root = tree_node([8, 15, 7, 1, None, 10, 2, 8, None, None, 5, None, 10, None, 9])) == 112724
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])) == 27790
    assert candidate(root = tree_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 8444
    assert candidate(root = tree_node([7, 0, 8, None, 2, 3, None, 9])) == 7812
    assert candidate(root = tree_node([5, 9, 1, None, 3, None, None, None, 2])) == 5983
    assert candidate(root = tree_node([7, 5, 6, 0, 1, 2, 8, 4, None, 3, None, None, None, None, None, 9])) == 84092
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, None, None, None, None, None, 9])) == 120287
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 69405
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 0])) == 1234567890
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == 31520
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, None, 1, 2, None, 3, 4, None, 5, 6, None, 7, 8, None, 9, 0, None, 1])) == 104580
    assert candidate(root = tree_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == 150745
    assert candidate(root = tree_node([7, 6, 7, 4, 3, 6, 7, 8, 7, 4, 7, 8, 7, 3, 7])) == 61651
    assert candidate(root = tree_node([7, 3, 6, 1, 5, 8, 2, 0, 9, None, None, None, None, None, None])) == 16894
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 69195
    assert candidate(root = tree_node([3, 9, 8, 4, 0, 1, 2, None, None, None, 5, None, None, 6, 7])) == 12333
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])) == 131357
    assert candidate(root = tree_node([7, 1, 4, 6, 9, None, 3, None, None, None, 5])) == 8654
    assert candidate(root = tree_node([2, 3, 5, 4, 1, 6, 8, 7, None, 9, None, None, None, 0, None])) == 7502
    assert candidate(root = tree_node([5, 3, 6, 2, 4, 8, 9, 1, 7, None, None, 0, None, None, 0, 0, None, None, 0, 0])) == 169504
    assert candidate(root = tree_node([5, 3, 2, 8, 9, 7, 1, 4, 6, None, None, None, None, None, None])) == 12357
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 1, None, 2, None, 3, None, 4, None, 5])) == 565898
    assert candidate(root = tree_node([9, 4, 5, 1, 6, 7, 2, None, None, None, None, 8, 3, 0, None])) == 30558
    assert candidate(root = tree_node([5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5])) == 43996
    assert candidate(root = tree_node([6, 7, 8, 0, 1, 2, 3, 4, 5, None, None, None, None, None, None, 9])) == 75790
    assert candidate(root = tree_node([4, 9, 0, 5, 1, 0, 0, None, None, 3, 2, 0, 0])) == 18720
    assert candidate(root = tree_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) == 12176
    assert candidate(root = tree_node([2, 3, 5, 1, 9, 4, 6, 7, 8, 0, 2, 5, 8, 9, 3])) == 19642
    assert candidate(root = tree_node([1, 0, 2, 3, 4, 5, 6, 7, 8, 9])) == 3375
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 25, 26, 30, 31, 32, 33, 34, 35])) == 217394
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 2, 5, 10, 11, 12, 13, 14, 15])) == 216394
    assert candidate(root = tree_node([7, 3, 4, 1, 5, 8, 2, 9, 6, None, None, 0, None, None, 0, None, None, 0, None, None, 0])) == 163434
    assert candidate(root = tree_node([8, 5, 9, 7, 3, None, 1, None, 6, 2, 4])) == 26533
    assert candidate(root = tree_node([6, 7, 8, 9, 0, 1, 2, 3, 4, 5, None, None, None, None, None, None, None, None, None])) == 21655
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, None, None])) == 475
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 195765
    assert candidate(root = tree_node([3, 1, 8, None, 4, 2, 7, None, None, None, 5])) == 4526
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5])) == 19397
    assert candidate(root = tree_node([0, 1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == 123456789
    assert candidate(root = tree_node([6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 54282
    assert candidate(root = tree_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, None, 9, 8, 7, 6])) == 68543
    assert candidate(root = tree_node([7, 3, 8, None, None, 1, 4, 6, 2, None, None, 5, 9])) == 165003
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 79992
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4])) == 1594
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 93345
    assert candidate(root = tree_node([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) == 1599984
    assert candidate(root = tree_node([1, 9, None, 2, 8, None, 7, None, 3, 6, None, 4, 5, None, None, None, None])) == 58945
    assert candidate(root = tree_node([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, 5, None, None, None, None, None, 5])) == 88716
    assert candidate(root = tree_node([1, None, 9, 2, None, 8, 4, None, None, None, 5, None, None, 6, 3])) == 21173
    assert candidate(root = tree_node([1, 0, 1, None, 1, 0, 1, None, None, None, 1])) == 1313
    assert candidate(root = tree_node([3, 0, 1, None, None, 0, 2, 1, 4, None, None, 6, 9, None, None, 8, None, None, None, None, None])) == 344633
    assert candidate(root = tree_node([1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9])) == 105550
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == 475
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == 23308
