# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(buckets = [1, 1, 1, 1, 1, 1],loss = 50) == 0.9999923706054688
    assert candidate(buckets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],loss = 0) == 0.9999923706054688
    assert candidate(buckets = [5, 10, 15],loss = 20) == 9.61538314819336
    assert candidate(buckets = [100, 0, 0],loss = 99) == 0.49750804901123047
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 0) == 29.999995231628418
    assert candidate(buckets = [5, 5, 5, 5, 5],loss = 0) == 4.999990463256836
    assert candidate(buckets = [5, 5, 5, 5, 5],loss = 99) == 4.999990463256836
    assert candidate(buckets = [100000, 100000, 100000],loss = 0) == 99999.99999417923
    assert candidate(buckets = [2, 4, 6],loss = 50) == 3.499998092651367
    assert candidate(buckets = [10, 20, 30],loss = 50) == 17.49999761581421
    assert candidate(buckets = [100, 0, 0],loss = 50) == 19.999998807907104
    assert candidate(buckets = [10, 0, 10],loss = 10) == 6.428565979003906
    assert candidate(buckets = [0, 0, 0, 0],loss = 99) == 0
    assert candidate(buckets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],loss = 25) == 0.9999923706054688
    assert candidate(buckets = [1, 2, 7],loss = 80) == 1.9999990463256836
    assert candidate(buckets = [10, 20, 30, 40],loss = 10) == 24.473676681518555
    assert candidate(buckets = [3, 3, 3, 3],loss = 40) == 2.9999942779541016
    assert candidate(buckets = [0, 0, 0, 0],loss = 0) == 0
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 1) == 29.93963360786438
    assert candidate(buckets = [100000, 100000, 100000, 100000],loss = 50) == 99999.99999417923
    assert candidate(buckets = [0, 0, 0, 0],loss = 10) == 0
    assert candidate(buckets = [100000, 0, 0, 0],loss = 50) == 14285.71428405121
    assert candidate(buckets = [100000, 0, 0, 0, 0],loss = 99) == 249.37655543908477
    assert candidate(buckets = [5, 5, 5, 5, 5],loss = 20) == 4.999990463256836
    assert candidate(buckets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],loss = 20) == 0.9999923706054688
    assert candidate(buckets = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],loss = 60) == 218.75
    assert candidate(buckets = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],loss = 10) == 99.99999403953552
    assert candidate(buckets = [1000, 1500, 2000, 2500, 3000],loss = 70) == 1637.9310339689255
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],loss = 40) == 70.50847113132477
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],loss = 50) == 671.4285705238581
    assert candidate(buckets = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],loss = 60) == 58.81578826904297
    assert candidate(buckets = [99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999],loss = 90) == 99991.9285675098
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],loss = 15) == 100.94594359397888
    assert candidate(buckets = [100, 101, 99, 102, 98],loss = 5) == 99.96906673908234
    assert candidate(buckets = [99999, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 99) == 105.39360189205036
    assert candidate(buckets = [1, 10, 100, 1000, 10000, 100000],loss = 25) == 14975.826081354171
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 5) == 543.5897409915924
    assert candidate(buckets = [99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999, 99999],loss = 99) == 99998.99999417929
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 90) == 2.9285621643066406
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 50) == 464.285708963871
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 0) == 5.499992370605469
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 25) == 514.2857134342194
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 1) == 548.7437173724174
    assert candidate(buckets = [1, 10, 100, 1000, 10000, 100000],loss = 45) == 11911.891889758408
    assert candidate(buckets = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 45) == 418.67469251155853
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 75) == 3.8420963287353516
    assert candidate(buckets = [10, 10, 20, 20, 30, 30, 40, 40, 50, 50],loss = 25) == 28.235292434692383
    assert candidate(buckets = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],loss = 30) == 83096926.70212598
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],loss = 90) == 292.8571403026581
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],loss = 40) == 705.0847448408604
    assert candidate(buckets = [5, 15, 25, 35, 45, 55],loss = 75) == 19.999994039535522
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 10) == 5.368413925170898
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],loss = 99) == 14.128434658050537
    assert candidate(buckets = [50000, 50000, 50000, 50000, 50000],loss = 0) == 49999.999994179234
    assert candidate(buckets = [33333, 66666, 99999, 100000, 133333, 166666, 200000],loss = 55) == 97646.6117601376
    assert candidate(buckets = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],loss = 80) == 2.2727203369140625
    assert candidate(buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000000],loss = 99) == 1109.877906856127
    assert candidate(buckets = [100, 200, 300, 400, 500],loss = 90) == 171.42856866121292
    assert candidate(buckets = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],loss = 10) == 4.999990463256836
    assert candidate(buckets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100000],loss = 20) == 3847.1153820864856
    assert candidate(buckets = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300],loss = 60) == 128.84615063667297
    assert candidate(buckets = [99999, 100000, 100001, 100002, 100003, 100004],loss = 99) == 99999.14285372151
    assert candidate(buckets = [90, 80, 70, 60, 50, 40, 30, 20, 10],loss = 45) == 43.33332896232605
    assert candidate(buckets = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],loss = 85) == 1.9374942779541016
    assert candidate(buckets = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],loss = 95) == 1.4166641235351562
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],loss = 70) == 581.2499988824129
    assert candidate(buckets = [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],loss = 95) == 49999.999994179234
    assert candidate(buckets = [100, 50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.1953125],loss = 45) == 13.994759321212769
    assert candidate(buckets = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],loss = 15) == 5297.297295182943
    assert candidate(buckets = [0, 0, 0, 100, 100, 100, 100, 100, 100, 100],loss = 30) == 62.02531456947327
    assert candidate(buckets = [1, 1, 1, 1, 1, 1000, 1000, 1000, 1000, 1000],loss = 1) == 497.9899451136589
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],loss = 50) == 46.4285671710968
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 30) == 27.804875373840332
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 0) == 29.999995231628418
    assert candidate(buckets = [10000, 20000, 30000, 40000, 50000],loss = 30) == 27804.878045571968
    assert candidate(buckets = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],loss = 90) == 99991.9285675098
    assert candidate(buckets = [1, 1, 1, 1, 100000],loss = 5) == 19192.727271001786
    assert candidate(buckets = [500, 1000, 1500, 2000, 2500, 3000],loss = 10) == 1710.5263117700815
    assert candidate(buckets = [50000, 25000, 12500, 6250, 3125],loss = 30) == 16903.409088263288
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],loss = 60) == 631.2499959021807
    assert candidate(buckets = [0, 100, 200, 300, 400, 500],loss = 75) == 149.99999850988388
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 10) == 29.361701011657715
    assert candidate(buckets = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],loss = 25) == 9.285706043243408
    assert candidate(buckets = [100000, 50000, 25000, 12500, 6250],loss = 85) == 18367.346934974194
    assert candidate(buckets = [99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990],loss = 75) == 99992.84210432932
    assert candidate(buckets = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],loss = 25) == 9999.999990686774
    assert candidate(buckets = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],loss = 80) == 309.0909030288458
    assert candidate(buckets = [50, 100, 150, 200, 250],loss = 50) == 128.57142835855484
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],loss = 5) == 103.71794700622559
    assert candidate(buckets = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],loss = 55) == 45149.2537278682
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 30) == 5.0588226318359375
    assert candidate(buckets = [100000, 50000, 25000, 12500, 6250, 3125, 1562.5, 781.25, 390.625, 195.3125],loss = 80) == 7324.21875
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 25) == 28.235292434692383
    assert candidate(buckets = [10, 100, 1000, 10000, 100000],loss = 85) == 5336.3636310677975
    assert candidate(buckets = [10000, 20000, 30000, 40000, 50000],loss = 90) == 17142.8571396973
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 60) == 24.37499761581421
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 75) == 21.81817889213562
    assert candidate(buckets = [1, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],loss = 25) == 46.285709738731384
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],loss = 50) == 4.642848968505859
    assert candidate(buckets = [5, 15, 25, 35, 45, 55],loss = 30) == 27.35293745994568
    assert candidate(buckets = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000],loss = 65) == 6081.967209465802
    assert candidate(buckets = [1, 2, 3, 4, 5],loss = 99) == 1.0961532592773438
    assert candidate(buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],loss = 90) == 29.28571105003357
    assert candidate(buckets = [123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627, 282930],loss = 80) == 61408.49999413564
    assert candidate(buckets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],loss = 30) == 1188.9423057436943
    assert candidate(buckets = [10, 20, 30, 40, 50],loss = 1) == 29.93963360786438
    assert candidate(buckets = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],loss = 40) == 43.684205412864685
    assert candidate(buckets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],loss = 45) == 6.890408992767334
