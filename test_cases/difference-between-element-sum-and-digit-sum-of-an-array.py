# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [1111, 2222, 3333, 4444]) == 11070
    assert candidate(nums = [2000, 1999, 1, 0]) == 3969
    assert candidate(nums = [1, 1, 1, 1]) == 0
    assert candidate(nums = [10, 11, 12, 13]) == 36
    assert candidate(nums = [1, 15, 6, 3]) == 9
    assert candidate(nums = [1]) == 0
    assert candidate(nums = [10, 100, 1000]) == 1107
    assert candidate(nums = [1, 2, 3, 4]) == 0
    assert candidate(nums = [5, 12, 43, 78]) == 108
    assert candidate(nums = [123, 456, 789, 101, 111]) == 1530
    assert candidate(nums = [2000, 1999, 1000, 999]) == 5940
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 504
    assert candidate(nums = [999, 1000, 1001]) == 2970
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(nums = [123, 456, 789]) == 1323
    assert candidate(nums = [9, 99, 999, 9999]) == 11016
    assert candidate(nums = [5, 55, 555, 5555]) == 6120
    assert candidate(nums = [2000, 1000, 500, 250]) == 3735
    assert candidate(nums = [1111, 2222, 3333, 4444]) == 11070
    assert candidate(nums = [10, 20, 30, 40, 50]) == 135
    assert candidate(nums = [18, 46, 89, 37]) == 144
    assert candidate(nums = [2000, 1999, 1998, 1997]) == 7911
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(nums = [2000, 1111, 999, 888]) == 4941
    assert candidate(nums = [111, 222, 333]) == 648
    assert candidate(nums = [10, 20, 30, 40]) == 90
    assert candidate(nums = [101, 1234, 56789, 234567]) == 292617
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]) == 111110778
    assert candidate(nums = [555, 666, 777, 888, 999, 1000]) == 4779
    assert candidate(nums = [123, 456, 789, 101, 112, 123, 134, 145, 156, 167, 178, 189]) == 2538
    assert candidate(nums = [1, 10, 100, 1000, 10000]) == 11106
    assert candidate(nums = [1999, 2998, 3997, 4996, 5995]) == 19845
    assert candidate(nums = [999, 888, 777, 666, 555, 444, 333, 222, 111]) == 4860
    assert candidate(nums = [10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009]) == 99990
    assert candidate(nums = [10, 100, 1000, 10000, 11111, 22222, 33333, 44444, 55555, 66666]) == 244332
    assert candidate(nums = [5, 50, 500, 5000, 1500, 2500, 3500, 4500, 6500, 7500, 8500, 9500]) == 49455
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005]) == 14985
    assert candidate(nums = [1, 22, 333, 4444, 55555]) == 60300
    assert candidate(nums = [1999, 1888, 1777, 1666, 1555, 1444, 1333, 1222, 1111]) == 13851
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 19350
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1010, 1111]) == 6975
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5454
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324]) == 809838
    assert candidate(nums = [1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]) == 19710
    assert candidate(nums = [1999, 1998, 1997, 1996, 1995, 1994]) == 11826
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993]) == 15795
    assert candidate(nums = [2000, 2000, 2000, 2000, 2000]) == 9990
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 11111110605
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981]) == 39366
    assert candidate(nums = [987, 654, 321, 111, 222]) == 2241
    assert candidate(nums = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930]) == 1345347
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991]) == 19737
    assert candidate(nums = [2000, 1500, 1000, 500, 250]) == 5229
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 10000]) == 59814
    assert candidate(nums = [1634, 2356, 7890, 1122, 3344, 5566, 7788, 9900]) == 39456
    assert candidate(nums = [1, 234, 567, 890, 432, 765, 109, 876, 543, 210]) == 4509
    assert candidate(nums = [987, 654, 321, 999, 888]) == 3753
    assert candidate(nums = [102030, 405060, 708090, 101112, 131415]) == 1447641
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]) == 111111102
    assert candidate(nums = [1000, 1001, 1002, 1003, 1004, 1005]) == 5994
    assert candidate(nums = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]) == 27450
    assert candidate(nums = [19, 28, 37, 46, 55, 64, 73, 82, 91]) == 405
    assert candidate(nums = [98765, 43210, 11111, 22222, 33333, 44444, 55555, 66666, 77777]) == 452898
    assert candidate(nums = [1999, 2998, 3997, 4996, 5995, 6994, 7993, 8992, 9991, 10990]) == 64674
    assert candidate(nums = [1234, 5678, 91011, 121314]) == 219177
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == 5859
    assert candidate(nums = [987, 654, 321, 876, 543, 210, 765, 432, 109]) == 4779
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 111105
    assert candidate(nums = [2000, 1000, 500, 250, 125]) == 3852
    assert candidate(nums = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 99999999]) == 197393409
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999]) == 4860
    assert candidate(nums = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]) == 9999
    assert candidate(nums = [500, 400, 300, 200, 100, 99, 98, 97, 96, 95]) == 1890
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555]) == 16605
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995]) == 11853
    assert candidate(nums = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]) == 49815
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 1971
    assert candidate(nums = [11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 100000]) == 599769
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 44955
    assert candidate(nums = [2000, 1500, 1000, 500, 100]) == 5085
    assert candidate(nums = [999, 111, 222, 333, 444, 555, 666, 777, 888]) == 4860
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == 99630
    assert candidate(nums = [9876, 6543, 3210, 1111, 2222]) == 22896
    assert candidate(nums = [123456789, 987654321, 111111111, 222222222, 333333333, 444444444, 555555555]) == 2777777550
    assert candidate(nums = [9876, 5432, 1357, 2468, 1111, 2222, 3333, 4444, 5555, 6666]) == 42300
    assert candidate(nums = [1999, 1998, 1997, 1996, 1995, 1994, 1993]) == 13797
    assert candidate(nums = [101, 202, 303, 404, 505, 606, 707, 808, 909]) == 4455
    assert candidate(nums = [1999, 1888, 1777, 1666, 1555, 1444, 1333, 1222, 1111, 1000]) == 14850
    assert candidate(nums = [1234, 4321, 5678, 8765, 9876, 6789]) == 36531
    assert candidate(nums = [9876, 6543, 3210, 2468]) == 22023
    assert candidate(nums = [123, 456, 789, 321, 654, 987, 159, 753, 951, 842]) == 5886
    assert candidate(nums = [10, 200, 3000, 40000, 500000]) == 543195
    assert candidate(nums = [1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509]) == 14940
    assert candidate(nums = [2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992]) == 17766
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 108
    assert candidate(nums = [2000, 1500, 1000, 500, 100, 50, 10, 5, 1]) == 5139
    assert candidate(nums = [123, 456, 789, 1011, 1213]) == 3537
    assert candidate(nums = [123, 456, 789, 101112, 131415]) == 233829
    assert candidate(nums = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 5904
