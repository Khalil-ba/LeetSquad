# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(classes = [[5, 10], [6, 10], [7, 10]],extraStudents = 1) == 0.6151515151515151
    assert candidate(classes = [[2, 4], [3, 9], [4, 5], [2, 10]],extraStudents = 4) == 0.5348484848484849
    assert candidate(classes = [[1, 1], [1, 1], [1, 1]],extraStudents = 1) == 1.0
    assert candidate(classes = [[1, 2], [3, 5], [2, 2]],extraStudents = 2) == 0.7833333333333333
    assert candidate(classes = [[10, 20], [20, 30], [30, 40]],extraStudents = 5) == 0.6722222222222222
    assert candidate(classes = [[5, 5], [10, 10]],extraStudents = 10) == 1.0
    assert candidate(classes = [[1, 1], [1, 2], [1, 3]],extraStudents = 3) == 0.7555555555555555
    assert candidate(classes = [[99, 100], [999, 1000], [9999, 10000]],extraStudents = 1000) == 0.999331746031746
    assert candidate(classes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],extraStudents = 10) == 1.0
    assert candidate(classes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],extraStudents = 10) == 0.6842857142857143
    assert candidate(classes = [[100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000]],extraStudents = 45) == 0.7958742756361804
    assert candidate(classes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],extraStudents = 15) == 0.2273449131513648
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],extraStudents = 15) == 0.8571428571428571
    assert candidate(classes = [[1, 100], [10, 1000], [100, 10000], [1000, 100000]],extraStudents = 1000) == 0.3008176852167975
    assert candidate(classes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],extraStudents = 50) == 0.6412325174825175
    assert candidate(classes = [[99, 100], [999, 1000], [9999, 10000], [99999, 100000]],extraStudents = 10) == 0.9974497727272728
    assert candidate(classes = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50]],extraStudents = 25) == 0.5977592214345788
    assert candidate(classes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],extraStudents = 1000) == 1.0
    assert candidate(classes = [[1000, 2000], [1500, 3000], [2000, 4000], [2500, 5000], [3000, 6000]],extraStudents = 1000) == 0.5350170085037467
    assert candidate(classes = [[1, 3], [2, 6], [3, 9], [4, 12], [5, 15]],extraStudents = 10) == 0.4884670884670885
    assert candidate(classes = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],extraStudents = 10) == 0.4164285714285715
    assert candidate(classes = [[1, 100], [10, 100], [50, 100]],extraStudents = 50) == 0.3296191939890711
    assert candidate(classes = [[100, 200], [150, 250], [200, 300], [250, 350]],extraStudents = 50) == 0.6452380952380952
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]],extraStudents = 5) == 0.4371428571428571
    assert candidate(classes = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],extraStudents = 50) == 1.0
    assert candidate(classes = [[10000, 10001], [20000, 20001], [30000, 30001], [40000, 40001]],extraStudents = 1000) == 0.9999501925188506
    assert candidate(classes = [[50, 100], [75, 150], [125, 250], [200, 400], [300, 600], [450, 900]],extraStudents = 300) == 0.5992478200634347
    assert candidate(classes = [[5, 8], [5, 8], [5, 8], [5, 8], [5, 8]],extraStudents = 20) == 0.75
    assert candidate(classes = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],extraStudents = 100) == 0.8541887125220459
    assert candidate(classes = [[99, 100], [98, 100], [97, 100], [96, 100], [95, 100]],extraStudents = 5) == 0.9704761904761904
    assert candidate(classes = [[99999, 100000], [50000, 100000], [25000, 50000], [10000, 20000]],extraStudents = 5000) == 0.6499975
    assert candidate(classes = [[1, 100000], [2, 100000], [3, 100000]],extraStudents = 100000) == 0.2500150000093752
    assert candidate(classes = [[100, 200], [200, 500], [300, 800], [400, 1000]],extraStudents = 100) == 0.4604967738352485
    assert candidate(classes = [[1, 2], [3, 6], [5, 10], [7, 14], [9, 18]],extraStudents = 15) == 0.6531926406926407
    assert candidate(classes = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000]],extraStudents = 100000) == 0.16669166670370508
    assert candidate(classes = [[10000, 20000], [5000, 10000], [2500, 5000], [1000, 2000], [500, 1000], [250, 500], [100, 200], [50, 100], [25, 50], [10, 20]],extraStudents = 10000) == 0.7885364227868774
    assert candidate(classes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],extraStudents = 5) == 1.0
    assert candidate(classes = [[50, 100], [150, 300], [250, 500], [350, 700]],extraStudents = 150) == 0.5803610885401075
    assert candidate(classes = [[1, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],extraStudents = 20) == 0.9074074074074074
    assert candidate(classes = [[9, 10], [99, 100], [999, 1000], [9999, 10000], [99999, 100000]],extraStudents = 50000) == 0.9999456354114968
    assert candidate(classes = [[99, 100], [98, 100], [97, 100], [96, 100], [95, 100], [94, 100], [93, 100], [92, 100], [91, 100], [90, 100]],extraStudents = 10) == 0.945917211328976
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11]],extraStudents = 10) == 0.3255194805194805
    assert candidate(classes = [[50, 100], [100, 200], [150, 300], [200, 400]],extraStudents = 100) == 0.567861188343116
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],extraStudents = 9) == 0.341005291005291
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],extraStudents = 5) == 0.7966666666666666
    assert candidate(classes = [[10, 11], [20, 22], [30, 33], [40, 44]],extraStudents = 5) == 0.9161931818181818
    assert candidate(classes = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]],extraStudents = 15) == 0.7535606060606062
    assert candidate(classes = [[1, 3], [2, 5], [3, 7], [4, 9]],extraStudents = 5) == 0.528968253968254
    assert candidate(classes = [[1, 1000], [10, 1000], [100, 1000], [1000, 1000]],extraStudents = 100) == 0.30143093489681594
    assert candidate(classes = [[10, 15], [20, 25], [30, 35], [40, 45], [50, 55], [60, 65]],extraStudents = 100) == 0.9114219114219114
    assert candidate(classes = [[1, 100], [20, 50], [30, 40], [40, 60]],extraStudents = 10) == 0.4822964571623233
    assert candidate(classes = [[1, 100000], [100000, 100000], [100000, 100000], [100000, 100000], [1, 100000]],extraStudents = 100000) == 0.733336
    assert candidate(classes = [[5, 6], [10, 12], [15, 18], [20, 24], [25, 30]],extraStudents = 50) == 0.8996095210091154
    assert candidate(classes = [[1, 2], [2, 4], [3, 8], [4, 16], [5, 32], [6, 64], [7, 128], [8, 256], [9, 512]],extraStudents = 256) == 0.56112903154186
    assert candidate(classes = [[99999, 100000], [99998, 100000], [99997, 100000]],extraStudents = 3) == 0.999980000299991
    assert candidate(classes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],extraStudents = 100) == 0.29977994676131325
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],extraStudents = 45) == 0.5812816812816812
    assert candidate(classes = [[1, 3], [2, 5], [3, 7], [4, 9], [5, 11]],extraStudents = 5) == 0.5140836940836941
    assert candidate(classes = [[100, 200], [200, 300], [50, 150], [250, 500], [100, 250]],extraStudents = 50) == 0.5133333333333333
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5]],extraStudents = 5) == 0.5
    assert candidate(classes = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]],extraStudents = 5) == 0.5488095238095239
    assert candidate(classes = [[1000, 10000], [2000, 20000], [3000, 30000], [4000, 40000]],extraStudents = 2000) == 0.1375
    assert candidate(classes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],extraStudents = 200) == 0.638637428727642
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]],extraStudents = 50) == 0.9128787878787878
    assert candidate(classes = [[100, 101], [200, 201], [300, 301], [400, 401], [500, 501]],extraStudents = 500) == 0.9974701296361822
    assert candidate(classes = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000]],extraStudents = 500000) == 0.5000150000250008
    assert candidate(classes = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]],extraStudents = 5) == 0.5833333333333333
    assert candidate(classes = [[1, 100000], [100000, 200000], [1, 100000], [1, 100000]],extraStudents = 50000) == 0.23214928570379018
    assert candidate(classes = [[50, 100], [40, 80], [30, 60], [20, 40], [10, 20]],extraStudents = 20) == 0.554287556415216
    assert candidate(classes = [[1, 2], [2, 5], [3, 10], [4, 20], [5, 50], [6, 100], [7, 200], [8, 500], [9, 1000], [10, 10000]],extraStudents = 5000) == 0.7736090641036538
    assert candidate(classes = [[1, 1000], [1, 2000], [1, 3000], [1, 4000], [1, 5000]],extraStudents = 1500) == 0.14190236063451128
    assert candidate(classes = [[10, 20], [20, 40], [30, 60], [40, 80]],extraStudents = 20) == 0.56785944551902
    assert candidate(classes = [[99, 100], [199, 200], [299, 300], [399, 400], [499, 500]],extraStudents = 1000) == 0.998
    assert candidate(classes = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500], [6, 600], [7, 700], [8, 800], [9, 900], [10, 1000]],extraStudents = 4500) == 0.5002246672081883
    assert candidate(classes = [[10000, 100000], [20000, 100000], [30000, 100000], [40000, 100000]],extraStudents = 10000) == 0.27058853870831734
    assert candidate(classes = [[1, 100], [1, 100], [1, 100], [1, 100], [1, 100]],extraStudents = 500) == 0.505
    assert candidate(classes = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],extraStudents = 5) == 1.0
    assert candidate(classes = [[1, 10], [2, 15], [3, 20], [4, 25], [5, 30]],extraStudents = 15) == 0.2816248934356351
    assert candidate(classes = [[10, 20], [15, 25], [20, 30], [25, 35]],extraStudents = 10) == 0.6633597883597884
    assert candidate(classes = [[1, 100], [10, 100], [100, 100], [1000, 1000], [10000, 10000]],extraStudents = 10000) == 0.9925924392888745
    assert candidate(classes = [[1, 100000], [100000, 100000], [50000, 100000]],extraStudents = 50000) == 0.6114404678259185
    assert candidate(classes = [[10, 20], [15, 30], [5, 15], [25, 50]],extraStudents = 15) == 0.55
    assert candidate(classes = [[10000, 100000], [20000, 100000], [30000, 100000], [40000, 100000], [50000, 100000], [60000, 100000], [70000, 100000], [80000, 100000], [90000, 100000], [100000, 100000]],extraStudents = 10000) == 0.5582354154833269
    assert candidate(classes = [[50, 100], [40, 80], [30, 60], [20, 40], [10, 20]],extraStudents = 30) == 0.5707749766573296
    assert candidate(classes = [[1, 100000], [1, 100000], [1, 100000], [1, 100000], [1, 100000]],extraStudents = 100000) == 0.166675
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],extraStudents = 100) == 0.9415395787944808
    assert candidate(classes = [[10, 100], [20, 200], [30, 300], [40, 400], [50, 500]],extraStudents = 50) == 0.16025231286795627
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]],extraStudents = 15) == 0.5976190476190476
    assert candidate(classes = [[50, 100], [75, 150], [25, 75], [10, 50]],extraStudents = 20) == 0.44060351413292587
    assert candidate(classes = [[1, 100], [2, 100], [3, 100], [4, 100], [5, 100]],extraStudents = 250) == 0.3533647454875556
    assert candidate(classes = [[50000, 100000], [40000, 100000], [30000, 100000], [20000, 100000], [10000, 100000]],extraStudents = 50000) == 0.3696598823228846
    assert candidate(classes = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], [6, 12], [7, 14], [8, 16], [9, 18], [10, 20]],extraStudents = 100) == 0.7595597403486419
    assert candidate(classes = [[3, 4], [4, 5], [5, 6], [6, 7], [7, 8]],extraStudents = 3) == 0.8464285714285715
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],extraStudents = 9) == 0.8504850088183421
    assert candidate(classes = [[10, 12], [20, 25], [30, 35], [40, 45], [50, 55]],extraStudents = 30) == 0.8916472416472416
    assert candidate(classes = [[1, 2], [2, 4], [4, 8], [8, 16], [16, 32]],extraStudents = 64) == 0.7993434343434344
    assert candidate(classes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]],extraStudents = 100) == 0.49407730392552046
    assert candidate(classes = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],extraStudents = 21) == 0.5919612794612795
    assert candidate(classes = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],extraStudents = 500) == 0.5672899020682859
    assert candidate(classes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],extraStudents = 10) == 0.8541887125220459
    assert candidate(classes = [[999, 1000], [998, 1000], [997, 1000], [996, 1000], [995, 1000]],extraStudents = 10) == 0.997009900990099
