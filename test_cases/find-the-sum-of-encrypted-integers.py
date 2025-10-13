# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [523, 213, 111]) == 999
    assert candidate(nums = [523, 213, 111]) == 999
    assert candidate(nums = [1, 10, 100, 1000]) == 1234
    assert candidate(nums = [999, 100, 101]) == 1221
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
    assert candidate(nums = [456, 789, 321]) == 1998
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555]) == 16665
    assert candidate(nums = [987, 654, 321]) == 1998
    assert candidate(nums = [5, 15, 25, 35]) == 170
    assert candidate(nums = [100, 200, 300]) == 666
    assert candidate(nums = [12, 21, 34, 43, 56, 65]) == 264
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == 495
    assert candidate(nums = [123, 456, 789]) == 1998
    assert candidate(nums = [9, 99, 999, 9999]) == 11106
    assert candidate(nums = [999, 888, 777]) == 2664
    assert candidate(nums = [123, 456, 789]) == 1998
    assert candidate(nums = [999, 123, 456]) == 1998
    assert candidate(nums = [1000, 100, 10, 1]) == 1234
    assert candidate(nums = [12, 23, 34, 45, 56, 67, 78, 89]) == 484
    assert candidate(nums = [999, 888, 777, 666]) == 3330
    assert candidate(nums = [5, 15, 25]) == 115
    assert candidate(nums = [111, 222, 333]) == 666
    assert candidate(nums = [11, 22, 33, 44, 55]) == 165
    assert candidate(nums = [999, 100, 200]) == 1332
    assert candidate(nums = [1, 2, 3]) == 6
    assert candidate(nums = [10, 21, 31]) == 66
    assert candidate(nums = [99, 999, 9999, 99999]) == 111096
    assert candidate(nums = [1, 11, 111, 1111, 11111]) == 12345
    assert candidate(nums = [567, 890, 1234, 54321, 98765]) == 161774
    assert candidate(nums = [1234, 4321, 1199, 2288, 3377]) == 35552
    assert candidate(nums = [987654, 321, 4321, 111, 222, 333]) == 1005442
    assert candidate(nums = [199, 299, 399, 499, 599, 699, 799, 899, 991]) == 8991
    assert candidate(nums = [987, 654, 321, 123, 456, 789, 101112]) == 226218
    assert candidate(nums = [865, 743, 219, 987, 567, 432, 321]) == 5217
    assert candidate(nums = [12345, 67890, 11122, 33344, 55566]) == 288886
    assert candidate(nums = [123456, 789012, 345678, 901234]) == 3555552
    assert candidate(nums = [901, 892, 783, 674, 567]) == 4440
    assert candidate(nums = [199, 288, 377, 466, 555, 644, 733, 822, 911]) == 7215
    assert candidate(nums = [345, 6789, 101112]) == 232776
    assert candidate(nums = [12345, 98765, 54321, 654321, 112233]) == 1211108
    assert candidate(nums = [987, 654, 321, 123, 456, 789, 876, 543, 210]) == 5661
    assert candidate(nums = [4321, 1111, 9999, 8765, 5432]) == 29997
    assert candidate(nums = [987, 654, 321, 987]) == 2997
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321]) == 43329
    assert candidate(nums = [123, 122, 121, 120, 119]) == 1998
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 12345
    assert candidate(nums = [100, 200, 300, 400, 500]) == 1665
    assert candidate(nums = [12345, 67890, 111111, 222222]) == 488887
    assert candidate(nums = [1000, 999, 888, 777, 666]) == 4441
    assert candidate(nums = [123, 321, 456, 654, 789, 987, 111, 222, 333]) == 4662
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 4995
    assert candidate(nums = [50, 51, 52, 53, 54]) == 275
    assert candidate(nums = [1234, 5678, 91011, 121314]) == 557775
    assert candidate(nums = [987, 654, 321, 123, 456]) == 2997
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 4995
    assert candidate(nums = [9, 99, 999, 9999, 99999]) == 111105
    assert candidate(nums = [123, 234, 345, 456, 567, 678, 789, 890, 901]) == 6660
    assert candidate(nums = [1001, 2002, 3003, 4004]) == 11110
    assert candidate(nums = [123, 456, 789, 101112, 321, 654, 987]) == 226218
    assert candidate(nums = [56, 78, 90, 123, 456, 789]) == 2251
    assert candidate(nums = [12, 23, 34, 45, 56, 67, 78, 89, 90]) == 583
    assert candidate(nums = [9876, 5432, 1111, 2222, 3333]) == 22220
    assert candidate(nums = [19, 92, 299, 9992, 123456]) == 677862
    assert candidate(nums = [1234, 5678, 9012]) == 23331
    assert candidate(nums = [12, 345, 6789, 9876]) == 20575
    assert candidate(nums = [10203, 40506, 70809]) == 199998
    assert candidate(nums = [1234, 4321, 2341, 3412, 1243]) == 22220
    assert candidate(nums = [12, 123, 1234, 12345, 123456]) == 727020
    assert candidate(nums = [1234, 5678, 91011]) == 113331
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432]) == 38885
    assert candidate(nums = [12, 21, 345, 543, 654]) == 1820
    assert candidate(nums = [100, 2000, 30000, 400000, 5000000]) == 6035665
    assert candidate(nums = [990, 881, 772, 663, 554, 445, 336, 227, 118]) == 6771
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050, 606060, 707070, 808080, 909090]) == 4999995
    assert candidate(nums = [1000, 200, 30, 4, 56, 7890, 12345]) == 66990
    assert candidate(nums = [12, 345, 6789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == 15571
    assert candidate(nums = [59, 68, 77, 86, 95, 104, 213, 322, 431]) == 2005
    assert candidate(nums = [9876, 8765, 7654, 6543, 5432, 4321, 3210, 2109, 1098]) == 66660
    assert candidate(nums = [888, 887, 886, 885, 884]) == 4440
    assert candidate(nums = [12, 345, 6789, 101112]) == 232798
    assert candidate(nums = [98765, 43210, 11223, 44556, 77889]) == 344441
    assert candidate(nums = [101, 102, 103, 104, 105]) == 1665
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 49995
    assert candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090]) == 49995
    assert candidate(nums = [1234, 4321, 2341, 3412, 1243, 2134, 4123, 3214]) == 35552
    assert candidate(nums = [12, 234, 3456, 45678, 567890]) == 1096019
    assert candidate(nums = [112233, 223344, 334455, 445566, 556677, 667788, 778899]) == 4666662
    assert candidate(nums = [199, 299, 399, 499, 599]) == 4995
    assert candidate(nums = [1234, 5678, 9012, 3456, 7890]) == 39996
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000]) == 16665
    assert candidate(nums = [56, 65, 78, 87, 90, 900]) == 1406
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 606
    assert candidate(nums = [101, 202, 303, 404, 505]) == 1665
    assert candidate(nums = [199, 299, 399, 499, 599, 699, 799, 899, 999]) == 8991
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 4995
    assert candidate(nums = [987, 654, 321, 111, 222, 333]) == 2664
    assert candidate(nums = [98765, 87654, 76543, 65432, 54321]) == 388885
    assert candidate(nums = [123456789, 987654321, 112233445566778899, 1000000000]) == 1000000003111111108
    assert candidate(nums = [12, 345, 6789, 101]) == 10687
    assert candidate(nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]) == 1097393685
    assert candidate(nums = [111111, 222222, 333333, 444444, 555555]) == 1666665
    assert candidate(nums = [12345, 67890, 54321]) == 211109
