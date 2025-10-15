def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 8,delay = 3,forget = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,delay = 3,forget = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 100,forget = 400) == 5820125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 100,forget = 400) == 5820125: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,delay = 1,forget = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,delay = 1,forget = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 5,forget = 10) == 743819361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 5,forget = 10) == 743819361: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 1,forget = 999) == 344211603
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 1,forget = 999) == 344211603: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,delay = 2,forget = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,delay = 2,forget = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,delay = 3,forget = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,delay = 3,forget = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,delay = 4,forget = 7) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,delay = 4,forget = 7) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,delay = 2,forget = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,delay = 2,forget = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,delay = 1,forget = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,delay = 1,forget = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,delay = 2,forget = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,delay = 2,forget = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,delay = 10,forget = 50) == 22517820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,delay = 10,forget = 50) == 22517820: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,delay = 50,forget = 150) == 27250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,delay = 50,forget = 150) == 27250: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 300,forget = 650) == 45500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 300,forget = 650) == 45500: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 150,forget = 450) == 203375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 150,forget = 450) == 203375: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 400,forget = 700) == 11625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 400,forget = 700) == 11625: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 150,forget = 600) == 79177860
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 150,forget = 600) == 79177860: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 150,forget = 300) == 935294905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 150,forget = 300) == 935294905: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 1,forget = 10) == 694661098
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 1,forget = 10) == 694661098: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 110,forget = 550) == 887595495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 110,forget = 550) == 887595495: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 250,forget = 550) == 5350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 250,forget = 550) == 5350: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 100,forget = 200) == 5264525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 100,forget = 200) == 5264525: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,delay = 2,forget = 199) == 349361643
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,delay = 2,forget = 199) == 349361643: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 1,forget = 500) == 28219034
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 1,forget = 500) == 28219034: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 1,forget = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 1,forget = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 250,forget = 500) == 31625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 250,forget = 500) == 31625: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,delay = 50,forget = 400) == 112339611
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,delay = 50,forget = 400) == 112339611: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 300,forget = 600) == 81225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 300,forget = 600) == 81225: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 200,forget = 600) == 635625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 200,forget = 600) == 635625: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 200,forget = 500) == 9051525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 200,forget = 500) == 9051525: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 125,forget = 500) == 6406900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 125,forget = 500) == 6406900: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 200,forget = 300) == 843250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 200,forget = 300) == 843250: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 110,forget = 440) == 8292625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 110,forget = 440) == 8292625: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 150,forget = 450) == 7127075
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 150,forget = 450) == 7127075: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 5,forget = 100) == 121345145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 5,forget = 100) == 121345145: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 120,forget = 450) == 913950185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 120,forget = 450) == 913950185: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,delay = 60,forget = 280) == 907415
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,delay = 60,forget = 280) == 907415: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 150,forget = 400) == 42450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 150,forget = 400) == 42450: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 50,forget = 550) == 979826832
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 50,forget = 550) == 979826832: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 125,forget = 550) == 450909175
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 125,forget = 550) == 450909175: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 70,forget = 400) == 326052608
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 70,forget = 400) == 326052608: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 400,forget = 750) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 400,forget = 750) == 350: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,delay = 20,forget = 100) == 207054
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,delay = 20,forget = 100) == 207054: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,delay = 30,forget = 150) == 689207212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,delay = 30,forget = 150) == 689207212: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 100,forget = 600) == 153808266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 100,forget = 600) == 153808266: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 200,forget = 300) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 200,forget = 300) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 300,forget = 600) == 45450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 300,forget = 600) == 45450: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 150,forget = 850) == 488545869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 150,forget = 850) == 488545869: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 250,forget = 400) == 5200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 250,forget = 400) == 5200: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,delay = 130,forget = 520) == 15497300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,delay = 130,forget = 520) == 15497300: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 350,forget = 560) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 350,forget = 560) == 210: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 140,forget = 650) == 285835661
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 140,forget = 650) == 285835661: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,delay = 300,forget = 500) == 28975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,delay = 300,forget = 500) == 28975: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,delay = 90,forget = 500) == 926898505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,delay = 90,forget = 500) == 926898505: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 250,forget = 450) == 1475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 250,forget = 450) == 1475: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 200,forget = 500) == 1423700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 200,forget = 500) == 1423700: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 250,forget = 550) == 31675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 250,forget = 550) == 31675: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 80,forget = 450) == 2109288
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 80,forget = 450) == 2109288: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 200,forget = 400) == 5250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 200,forget = 400) == 5250: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 50,forget = 900) == 770071855
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 50,forget = 900) == 770071855: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 120,forget = 500) == 914080410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 120,forget = 500) == 914080410: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 150,forget = 450) == 619250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 150,forget = 450) == 619250: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,delay = 300,forget = 750) == 246900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,delay = 300,forget = 750) == 246900: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 50,forget = 950) == 770074505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 50,forget = 950) == 770074505: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 190,forget = 760) == 65412725
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 190,forget = 760) == 65412725: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 10,forget = 500) == 104566774
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 10,forget = 500) == 104566774: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 120,forget = 480) == 11476850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 120,forget = 480) == 11476850: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 400,forget = 700) == 20400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 400,forget = 700) == 20400: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 100,forget = 800) == 892948851
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 100,forget = 800) == 892948851: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,delay = 50,forget = 450) == 344465040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,delay = 50,forget = 450) == 344465040: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,delay = 40,forget = 150) == 219220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,delay = 40,forget = 150) == 219220: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,delay = 50,forget = 250) == 8177885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,delay = 50,forget = 250) == 8177885: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 500,forget = 900) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 500,forget = 900) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 100,forget = 500) == 165273270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 100,forget = 500) == 165273270: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 200,forget = 500) == 632925
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 200,forget = 500) == 632925: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,delay = 130,forget = 550) == 523316449
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,delay = 130,forget = 550) == 523316449: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,delay = 90,forget = 360) == 3944850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,delay = 90,forget = 360) == 3944850: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 150,forget = 700) == 188312873
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 150,forget = 700) == 188312873: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 999,forget = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 999,forget = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,delay = 10,forget = 350) == 610381426
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,delay = 10,forget = 350) == 610381426: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 150,forget = 350) == 77362035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 150,forget = 350) == 77362035: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 190,forget = 560) == 426390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 190,forget = 560) == 426390: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,delay = 220,forget = 330) == 6215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,delay = 220,forget = 330) == 6215: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 250,forget = 600) == 651750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 250,forget = 600) == 651750: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 70,forget = 630) == 66046770
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 70,forget = 630) == 66046770: {e}')
    
    total += 1
    try:
        result = candidate(n = 950,delay = 400,forget = 850) == 11775
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 950,delay = 400,forget = 850) == 11775: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,delay = 150,forget = 600) == 26594875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,delay = 150,forget = 600) == 26594875: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,delay = 100,forget = 350) == 192050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,delay = 100,forget = 350) == 192050: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,delay = 10,forget = 299) == 236977941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,delay = 10,forget = 299) == 236977941: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,delay = 200,forget = 600) == 1434000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,delay = 200,forget = 600) == 1434000: {e}')
    
    total += 1
    try:
        result = candidate(n = 900,delay = 200,forget = 700) == 9092125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 900,delay = 200,forget = 700) == 9092125: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,delay = 100,forget = 500) == 766847687
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,delay = 100,forget = 500) == 766847687: {e}')
    
    total += 1
    try:
        result = candidate(n = 650,delay = 175,forget = 525) == 378875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 650,delay = 175,forget = 525) == 378875: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,delay = 80,forget = 400) == 816019201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,delay = 80,forget = 400) == 816019201: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,delay = 500,forget = 999) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,delay = 500,forget = 999) == 499: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,delay = 100,forget = 200) == 5150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,delay = 100,forget = 200) == 5150: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 8,delay = 3,forget = 6) == 6
    assert candidate(n = 500,delay = 100,forget = 400) == 5820125
    assert candidate(n = 4,delay = 1,forget = 3) == 6
    assert candidate(n = 1000,delay = 5,forget = 10) == 743819361
    assert candidate(n = 1000,delay = 1,forget = 999) == 344211603
    assert candidate(n = 10,delay = 2,forget = 5) == 30
    assert candidate(n = 10,delay = 3,forget = 5) == 5
    assert candidate(n = 15,delay = 4,forget = 7) == 19
    assert candidate(n = 6,delay = 2,forget = 4) == 5
    assert candidate(n = 5,delay = 1,forget = 4) == 14
    assert candidate(n = 7,delay = 2,forget = 3) == 2
    assert candidate(n = 100,delay = 10,forget = 50) == 22517820
    assert candidate(n = 200,delay = 50,forget = 150) == 27250
    assert candidate(n = 900,delay = 300,forget = 650) == 45500
    assert candidate(n = 550,delay = 150,forget = 450) == 203375
    assert candidate(n = 950,delay = 400,forget = 700) == 11625
    assert candidate(n = 800,delay = 150,forget = 600) == 79177860
    assert candidate(n = 900,delay = 150,forget = 300) == 935294905
    assert candidate(n = 1000,delay = 1,forget = 10) == 694661098
    assert candidate(n = 700,delay = 110,forget = 550) == 887595495
    assert candidate(n = 600,delay = 250,forget = 550) == 5350
    assert candidate(n = 500,delay = 100,forget = 200) == 5264525
    assert candidate(n = 200,delay = 2,forget = 199) == 349361643
    assert candidate(n = 1000,delay = 1,forget = 500) == 28219034
    assert candidate(n = 1000,delay = 1,forget = 2) == 2
    assert candidate(n = 750,delay = 250,forget = 500) == 31625
    assert candidate(n = 999,delay = 50,forget = 400) == 112339611
    assert candidate(n = 950,delay = 300,forget = 600) == 81225
    assert candidate(n = 750,delay = 200,forget = 600) == 635625
    assert candidate(n = 900,delay = 200,forget = 500) == 9051525
    assert candidate(n = 600,delay = 125,forget = 500) == 6406900
    assert candidate(n = 800,delay = 200,forget = 300) == 843250
    assert candidate(n = 550,delay = 110,forget = 440) == 8292625
    assert candidate(n = 700,delay = 150,forget = 450) == 7127075
    assert candidate(n = 500,delay = 5,forget = 100) == 121345145
    assert candidate(n = 750,delay = 120,forget = 450) == 913950185
    assert candidate(n = 300,delay = 60,forget = 280) == 907415
    assert candidate(n = 500,delay = 150,forget = 400) == 42450
    assert candidate(n = 600,delay = 50,forget = 550) == 979826832
    assert candidate(n = 750,delay = 125,forget = 550) == 450909175
    assert candidate(n = 550,delay = 70,forget = 400) == 326052608
    assert candidate(n = 800,delay = 400,forget = 750) == 350
    assert candidate(n = 120,delay = 20,forget = 100) == 207054
    assert candidate(n = 400,delay = 30,forget = 150) == 689207212
    assert candidate(n = 800,delay = 100,forget = 600) == 153808266
    assert candidate(n = 600,delay = 200,forget = 300) == 10000
    assert candidate(n = 900,delay = 300,forget = 600) == 45450
    assert candidate(n = 950,delay = 150,forget = 850) == 488545869
    assert candidate(n = 600,delay = 250,forget = 400) == 5200
    assert candidate(n = 650,delay = 130,forget = 520) == 15497300
    assert candidate(n = 700,delay = 350,forget = 560) == 210
    assert candidate(n = 950,delay = 140,forget = 650) == 285835661
    assert candidate(n = 850,delay = 300,forget = 500) == 28975
    assert candidate(n = 650,delay = 90,forget = 500) == 926898505
    assert candidate(n = 550,delay = 250,forget = 450) == 1475
    assert candidate(n = 800,delay = 200,forget = 500) == 1423700
    assert candidate(n = 750,delay = 250,forget = 550) == 31675
    assert candidate(n = 550,delay = 80,forget = 450) == 2109288
    assert candidate(n = 500,delay = 200,forget = 400) == 5250
    assert candidate(n = 1000,delay = 50,forget = 900) == 770071855
    assert candidate(n = 750,delay = 120,forget = 500) == 914080410
    assert candidate(n = 600,delay = 150,forget = 450) == 619250
    assert candidate(n = 999,delay = 300,forget = 750) == 246900
    assert candidate(n = 1000,delay = 50,forget = 950) == 770074505
    assert candidate(n = 950,delay = 190,forget = 760) == 65412725
    assert candidate(n = 1000,delay = 10,forget = 500) == 104566774
    assert candidate(n = 600,delay = 120,forget = 480) == 11476850
    assert candidate(n = 1000,delay = 400,forget = 700) == 20400
    assert candidate(n = 900,delay = 100,forget = 800) == 892948851
    assert candidate(n = 500,delay = 50,forget = 450) == 344465040
    assert candidate(n = 200,delay = 40,forget = 150) == 219220
    assert candidate(n = 300,delay = 50,forget = 250) == 8177885
    assert candidate(n = 1000,delay = 500,forget = 900) == 400
    assert candidate(n = 600,delay = 100,forget = 500) == 165273270
    assert candidate(n = 750,delay = 200,forget = 500) == 632925
    assert candidate(n = 850,delay = 130,forget = 550) == 523316449
    assert candidate(n = 450,delay = 90,forget = 360) == 3944850
    assert candidate(n = 1000,delay = 150,forget = 700) == 188312873
    assert candidate(n = 1000,delay = 999,forget = 1000) == 2
    assert candidate(n = 400,delay = 10,forget = 350) == 610381426
    assert candidate(n = 800,delay = 150,forget = 350) == 77362035
    assert candidate(n = 700,delay = 190,forget = 560) == 426390
    assert candidate(n = 550,delay = 220,forget = 330) == 6215
    assert candidate(n = 900,delay = 250,forget = 600) == 651750
    assert candidate(n = 700,delay = 70,forget = 630) == 66046770
    assert candidate(n = 950,delay = 400,forget = 850) == 11775
    assert candidate(n = 750,delay = 150,forget = 600) == 26594875
    assert candidate(n = 400,delay = 100,forget = 350) == 192050
    assert candidate(n = 300,delay = 10,forget = 299) == 236977941
    assert candidate(n = 800,delay = 200,forget = 600) == 1434000
    assert candidate(n = 900,delay = 200,forget = 700) == 9092125
    assert candidate(n = 700,delay = 100,forget = 500) == 766847687
    assert candidate(n = 650,delay = 175,forget = 525) == 378875
    assert candidate(n = 600,delay = 80,forget = 400) == 816019201
    assert candidate(n = 1000,delay = 500,forget = 999) == 499
    assert candidate(n = 300,delay = 100,forget = 200) == 5150


