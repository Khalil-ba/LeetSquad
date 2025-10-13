# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(pieces = ['bishop'],positions = [[4, 3]]) == 12
    assert candidate(pieces = ['queen', 'rook'],positions = [[1, 1], [2, 2]]) == 309
    assert candidate(pieces = ['rook', 'rook'],positions = [[1, 1], [8, 8]]) == 223
    assert candidate(pieces = ['queen', 'rook'],positions = [[2, 2], [5, 5]]) == 340
    assert candidate(pieces = ['rook', 'queen', 'bishop'],positions = [[1, 1], [5, 5], [8, 8]]) == 2907
    assert candidate(pieces = ['rook', 'queen', 'bishop'],positions = [[1, 1], [2, 2], [3, 3]]) == 3289
    assert candidate(pieces = ['rook', 'rook'],positions = [[1, 1], [1, 3]]) == 189
    assert candidate(pieces = ['rook'],positions = [[1, 1]]) == 15
    assert candidate(pieces = ['rook', 'bishop'],positions = [[1, 1], [4, 3]]) == 173
    assert candidate(pieces = ['bishop', 'bishop'],positions = [[2, 2], [7, 7]]) == 80
    assert candidate(pieces = ['bishop', 'bishop'],positions = [[2, 2], [6, 6]]) == 84
    assert candidate(pieces = ['queen', 'bishop'],positions = [[1, 1], [4, 4]]) == 280
    assert candidate(pieces = ['bishop', 'rook', 'bishop'],positions = [[3, 4], [5, 5], [7, 6]]) == 1265
    assert candidate(pieces = ['queen'],positions = [[1, 1]]) == 22
    assert candidate(pieces = ['rook', 'bishop'],positions = [[1, 1], [4, 4]]) == 205
    assert candidate(pieces = ['rook', 'queen', 'bishop'],positions = [[1, 1], [5, 5], [4, 3]]) == 4421
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[1, 1], [2, 2], [4, 3]]) == 3161
    assert candidate(pieces = ['rook', 'bishop', 'rook', 'bishop'],positions = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 16893
    assert candidate(pieces = ['queen', 'rook'],positions = [[1, 1], [8, 8]]) == 327
    assert candidate(pieces = ['queen', 'rook', 'rook'],positions = [[1, 1], [8, 8], [1, 8]]) == 4163
    assert candidate(pieces = ['rook', 'queen', 'bishop'],positions = [[3, 3], [5, 5], [7, 2]]) == 3589
    assert candidate(pieces = ['queen', 'bishop', 'bishop'],positions = [[1, 1], [8, 8], [1, 8]]) == 1232
    assert candidate(pieces = ['queen', 'rook', 'bishop', 'rook'],positions = [[1, 1], [1, 8], [8, 1], [8, 8]]) == 32176
    assert candidate(pieces = ['queen', 'rook', 'bishop', 'rook'],positions = [[1, 1], [8, 8], [3, 3], [6, 6]]) == 44166
    assert candidate(pieces = ['queen', 'queen'],positions = [[3, 3], [6, 6]]) == 638
    assert candidate(pieces = ['rook', 'rook', 'rook', 'rook'],positions = [[1, 1], [1, 8], [8, 1], [8, 8]]) == 33009
    assert candidate(pieces = ['bishop', 'bishop', 'rook', 'rook'],positions = [[1, 1], [8, 8], [4, 4], [5, 5]]) == 7561
    assert candidate(pieces = ['queen', 'bishop', 'rook', 'bishop'],positions = [[1, 1], [8, 8], [4, 4], [4, 1]]) == 15440
    assert candidate(pieces = ['rook', 'rook', 'rook'],positions = [[1, 1], [1, 8], [8, 1]]) == 2753
    assert candidate(pieces = ['rook', 'queen', 'bishop', 'rook'],positions = [[1, 1], [8, 8], [4, 4], [2, 2]]) == 51937
    assert candidate(pieces = ['rook', 'queen', 'bishop', 'rook'],positions = [[1, 1], [5, 5], [8, 8], [8, 1]]) == 38251
    assert candidate(pieces = ['queen', 'rook', 'rook', 'bishop'],positions = [[1, 1], [1, 8], [8, 1], [8, 8]]) == 29034
    assert candidate(pieces = ['queen', 'queen', 'rook'],positions = [[3, 3], [4, 4], [2, 2]]) == 8446
    assert candidate(pieces = ['queen', 'bishop', 'rook', 'rook'],positions = [[1, 1], [8, 8], [1, 8], [8, 1]]) == 29034
    assert candidate(pieces = ['queen', 'rook'],positions = [[4, 4], [7, 7]]) == 400
    assert candidate(pieces = ['rook', 'rook', 'bishop'],positions = [[1, 1], [8, 8], [4, 4]]) == 3034
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[2, 2], [7, 7], [3, 8]]) == 2590
    assert candidate(pieces = ['rook', 'rook'],positions = [[4, 4], [5, 5]]) == 193
    assert candidate(pieces = ['rook', 'queen', 'bishop'],positions = [[1, 4], [4, 4], [7, 4]]) == 3784
    assert candidate(pieces = ['rook', 'bishop', 'queen'],positions = [[1, 1], [8, 8], [4, 4]]) == 2681
    assert candidate(pieces = ['bishop', 'bishop', 'bishop', 'bishop'],positions = [[2, 2], [2, 7], [7, 2], [7, 7]]) == 6400
    assert candidate(pieces = ['queen', 'bishop', 'rook'],positions = [[8, 1], [1, 8], [4, 4]]) == 2110
    assert candidate(pieces = ['queen', 'bishop', 'rook'],positions = [[2, 2], [3, 3], [5, 5]]) == 3484
    assert candidate(pieces = ['bishop', 'rook', 'queen', 'rook'],positions = [[3, 3], [4, 4], [5, 5], [6, 6]]) == 44433
    assert candidate(pieces = ['queen', 'bishop', 'bishop'],positions = [[1, 1], [3, 3], [6, 6]]) == 2162
    assert candidate(pieces = ['rook', 'queen', 'rook', 'bishop'],positions = [[1, 1], [5, 5], [8, 1], [1, 8]]) == 41166
    assert candidate(pieces = ['rook', 'rook', 'queen'],positions = [[1, 1], [1, 8], [8, 8]]) == 4163
    assert candidate(pieces = ['bishop', 'rook', 'queen'],positions = [[3, 3], [4, 3], [3, 4]]) == 3142
    assert candidate(pieces = ['rook', 'rook', 'bishop', 'bishop'],positions = [[1, 2], [1, 7], [2, 1], [2, 8]]) == 10952
    assert candidate(pieces = ['bishop', 'rook', 'rook', 'bishop'],positions = [[1, 2], [3, 3], [6, 7], [8, 6]]) == 10473
    assert candidate(pieces = ['rook', 'bishop', 'bishop', 'queen'],positions = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 26725
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[1, 1], [8, 8], [4, 4]]) == 4145
    assert candidate(pieces = ['bishop', 'rook', 'queen', 'rook'],positions = [[1, 8], [2, 2], [5, 5], [8, 1]]) == 42649
    assert candidate(pieces = ['queen', 'rook', 'bishop', 'rook'],positions = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 35461
    assert candidate(pieces = ['rook', 'rook', 'rook'],positions = [[1, 1], [2, 2], [3, 3]]) == 2709
    assert candidate(pieces = ['rook', 'bishop'],positions = [[2, 2], [3, 6]]) == 172
    assert candidate(pieces = ['queen', 'queen'],positions = [[1, 1], [8, 8]]) == 462
    assert candidate(pieces = ['rook', 'bishop'],positions = [[1, 1], [8, 1]]) == 118
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[1, 1], [2, 2], [3, 3]]) == 2842
    assert candidate(pieces = ['bishop', 'bishop', 'rook', 'rook'],positions = [[2, 2], [7, 7], [1, 1], [8, 8]]) == 13998
    assert candidate(pieces = ['queen', 'bishop', 'bishop', 'rook'],positions = [[4, 4], [3, 3], [6, 6], [1, 1]]) == 39585
    assert candidate(pieces = ['rook', 'rook', 'rook'],positions = [[1, 1], [8, 8], [4, 4]]) == 3079
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[1, 1], [4, 5], [8, 2]]) == 2308
    assert candidate(pieces = ['bishop', 'bishop'],positions = [[3, 3], [6, 6]]) == 124
    assert candidate(pieces = ['bishop', 'rook', 'rook'],positions = [[1, 1], [8, 1], [8, 8]]) == 1600
    assert candidate(pieces = ['rook', 'rook', 'bishop', 'queen'],positions = [[1, 1], [8, 8], [3, 3], [6, 6]]) == 56730
    assert candidate(pieces = ['rook', 'bishop', 'rook'],positions = [[2, 2], [3, 3], [4, 4]]) == 2185
    assert candidate(pieces = ['queen', 'rook', 'rook'],positions = [[1, 1], [5, 5], [5, 6]]) == 4182
    assert candidate(pieces = ['rook', 'rook', 'bishop', 'bishop'],positions = [[1, 1], [1, 8], [8, 1], [8, 8]]) == 12485
    assert candidate(pieces = ['queen', 'rook', 'rook'],positions = [[4, 4], [1, 1], [8, 8]]) == 5890
    assert candidate(pieces = ['bishop', 'bishop', 'rook'],positions = [[2, 2], [7, 7], [1, 8]]) == 1112
    assert candidate(pieces = ['bishop', 'bishop', 'rook', 'rook'],positions = [[1, 1], [1, 8], [8, 1], [8, 8]]) == 12485
    assert candidate(pieces = ['bishop', 'rook', 'rook', 'queen'],positions = [[4, 4], [1, 1], [1, 8], [8, 8]]) == 49107
    assert candidate(pieces = ['queen', 'rook', 'bishop', 'rook'],positions = [[3, 3], [5, 5], [2, 2], [6, 6]]) == 37434
    assert candidate(pieces = ['queen', 'bishop'],positions = [[2, 2], [7, 7]]) == 220
    assert candidate(pieces = ['queen', 'queen', 'queen'],positions = [[2, 2], [3, 3], [4, 4]]) == 13103
    assert candidate(pieces = ['queen', 'bishop'],positions = [[1, 1], [8, 8]]) == 156
    assert candidate(pieces = ['queen', 'queen'],positions = [[2, 2], [7, 7]]) == 548
    assert candidate(pieces = ['bishop', 'bishop', 'rook', 'rook'],positions = [[2, 2], [3, 3], [6, 6], [7, 7]]) == 18260
    assert candidate(pieces = ['rook', 'bishop', 'queen'],positions = [[3, 3], [6, 6], [5, 5]]) == 4230
    assert candidate(pieces = ['rook', 'bishop', 'rook', 'bishop'],positions = [[1, 1], [8, 8], [2, 2], [7, 7]]) == 10336
    assert candidate(pieces = ['queen', 'rook', 'rook'],positions = [[1, 1], [1, 8], [8, 1]]) == 4286
    assert candidate(pieces = ['queen', 'rook'],positions = [[4, 4], [8, 1]]) == 412
    assert candidate(pieces = ['rook', 'rook', 'rook', 'rook', 'bishop'],positions = [[1, 1], [1, 8], [8, 1], [8, 8], [4, 4]]) == 437408
    assert candidate(pieces = ['rook', 'rook', 'queen', 'bishop'],positions = [[1, 1], [8, 8], [4, 4], [5, 5]]) == 74604
    assert candidate(pieces = ['queen', 'rook', 'rook'],positions = [[5, 5], [1, 1], [8, 8]]) == 5890
    assert candidate(pieces = ['bishop', 'bishop', 'rook'],positions = [[2, 2], [7, 7], [4, 4]]) == 1150
    assert candidate(pieces = ['queen', 'rook', 'bishop'],positions = [[4, 4], [1, 1], [8, 8]]) == 2681
    assert candidate(pieces = ['queen', 'bishop', 'rook'],positions = [[3, 3], [6, 6], [1, 1]]) == 4107
    assert candidate(pieces = ['queen', 'queen'],positions = [[1, 2], [8, 7]]) == 476
    assert candidate(pieces = ['queen', 'queen'],positions = [[2, 3], [3, 2]]) == 518
    assert candidate(pieces = ['bishop', 'bishop'],positions = [[1, 1], [8, 8]]) == 44
    assert candidate(pieces = ['bishop', 'bishop', 'bishop'],positions = [[2, 2], [5, 5], [8, 8]]) == 460
    assert candidate(pieces = ['rook', 'rook'],positions = [[1, 1], [1, 8]]) == 205
    assert candidate(pieces = ['rook', 'rook', 'bishop'],positions = [[1, 1], [8, 1], [4, 4]]) == 2764
    assert candidate(pieces = ['queen', 'queen', 'rook'],positions = [[1, 1], [8, 8], [4, 4]]) == 6380
    assert candidate(pieces = ['rook', 'queen', 'bishop', 'rook'],positions = [[1, 1], [2, 2], [3, 3], [4, 4]]) == 41894
    assert candidate(pieces = ['queen', 'rook'],positions = [[1, 1], [8, 1]]) == 309
    assert candidate(pieces = ['bishop', 'bishop', 'bishop'],positions = [[2, 3], [4, 5], [6, 7]]) == 728
    assert candidate(pieces = ['bishop', 'bishop', 'bishop'],positions = [[2, 2], [4, 4], [6, 6]]) == 792
