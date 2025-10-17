def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30]) == "10/(20/30)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30]) == "10/(20/30)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == "3/(100/100/100/100/100/100/100/100/100)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == "3/(100/100/100/100/100/100/100/100/100)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11]) == "2/(3/5/7/11)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11]) == "2/(3/5/7/11)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2]) == "3/2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2]) == "3/2": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "10/(9/8/7/6/5/4/3/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "10/(9/8/7/6/5/4/3/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10]) == "10"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10]) == "10": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5]) == "9/(8/7/6/5)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5]) == "9/(8/7/6/5)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3]) == "2/3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3]) == "2/3": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7]) == "5/(6/7)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7]) == "5/(6/7)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5]) == "5/(5/5/5)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5]) == "5/(5/5/5)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8]) == "5/(6/7/8)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8]) == "5/(6/7/8)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2]) == "10/2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2]) == "10/2": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10]) == "3/(4/5/6/7/8/9/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10]) == "3/(4/5/6/7/8/9/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4]) == "2/(3/4)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4]) == "2/(3/4)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 10, 5, 2]) == "20/(10/5/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 10, 5, 2]) == "20/(10/5/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 10]) == "100/(50/25/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 10]) == "100/(50/25/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == "10/(9/8/7/6/5/4/3/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == "10/(9/8/7/6/5/4/3/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == "100/(50/25/12/6/3/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == "100/(50/25/12/6/3/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5]) == "10/5"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5]) == "10/5": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 100, 10, 2]) == "1000/(100/10/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 100, 10, 2]) == "1000/(100/10/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40]) == "10/(20/30/40)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40]) == "10/(20/30/40)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40]) == "100/(90/80/70/60/50/40)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40]) == "100/(90/80/70/60/50/40)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 202, 303, 404, 505]) == "101/(202/303/404/505)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 202, 303, 404, 505]) == "101/(202/303/404/505)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 3]) == "10/(5/2/6/3)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 3]) == "10/(5/2/6/3)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256]) == "8/(16/32/64/128/256)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256]) == "8/(16/32/64/128/256)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1000, 2, 5, 10]) == "3/(1000/2/5/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1000, 2, 5, 10]) == "3/(1000/2/5/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == "1024/(512/256/128/64/32/16/8/4/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == "1024/(512/256/128/64/32/16/8/4/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99/(98/97/96/95/94/93/92/91/90)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99/(98/97/96/95/94/93/92/91/90)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 50, 75, 100, 125]) == "25/(50/75/100/125)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 50, 75, 100, 125]) == "25/(50/75/100/125)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == "11/(22/33/44/55/66/77/88/99)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == "11/(22/33/44/55/66/77/88/99)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 18, 21, 24, 27, 30]) == "12/(15/18/21/24/27/30)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 18, 21, 24, 27, 30]) == "12/(15/18/21/24/27/30)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 12, 18, 24, 30, 36]) == "5/(9/12/18/24/30/36)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 12, 18, 24, 30, 36]) == "5/(9/12/18/24/30/36)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "1000/(2/3/4/5/6/7/8/9/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "1000/(2/3/4/5/6/7/8/9/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 200, 3000, 40000, 500000]) == "10/(200/3000/40000/500000)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 200, 3000, 40000, 500000]) == "10/(200/3000/40000/500000)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31]) == "1000/(500/250/125/62/31)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31]) == "1000/(500/250/125/62/31)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 10, 20, 50, 100]) == "2/(5/10/20/50/100)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 10, 20, 50, 100]) == "2/(5/10/20/50/100)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 250, 125, 62, 31, 15, 7]) == "500/(250/125/62/31/15/7)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 250, 125, 62, 31, 15, 7]) == "500/(250/125/62/31/15/7)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == "7/(11/13/17/19/23/29/31/37/41)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == "7/(11/13/17/19/23/29/31/37/41)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 13, 17, 19, 23, 29]) == "11/(13/17/19/23/29)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 13, 17, 19, 23, 29]) == "11/(13/17/19/23/29)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == "7/(14/21/28/35/42/49)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == "7/(14/21/28/35/42/49)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25]) == "5/(10/15/20/25)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25]) == "5/(10/15/20/25)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995]) == "999/(998/997/996/995)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995]) == "999/(998/997/996/995)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == "15/(25/35/45/55/65/75/85/95)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == "15/(25/35/45/55/65/75/85/95)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == "8/(16/32/64/128/256/512/1024/2048/4096)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == "8/(16/32/64/128/256/512/1024/2048/4096)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 8, 3, 7, 4, 6]) == "10/(5/2/8/3/7/4/6)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 8, 3, 7, 4, 6]) == "10/(5/2/8/3/7/4/6)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == "8/(16/24/32/40/48/56/64/72/80)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == "8/(16/24/32/40/48/56/64/72/80)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 5, 1]) == "30/(20/10/5/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 5, 1]) == "30/(20/10/5/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "12/(15/20/25/30/35/40/45/50/55)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "12/(15/20/25/30/35/40/45/50/55)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31]) == "7/(11/13/17/19/23/29/31)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31]) == "7/(11/13/17/19/23/29/31)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2]) == "8/(6/4/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2]) == "8/(6/4/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 10, 20, 30, 40, 50]) == "15/(10/20/30/40/50)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 10, 20, 30, 40, 50]) == "15/(10/20/30/40/50)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [150, 200, 250, 300, 350, 400, 450]) == "150/(200/250/300/350/400/450)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [150, 200, 250, 300, 350, 400, 450]) == "150/(200/250/300/350/400/450)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336]) == "42/(84/126/168/210/252/294/336)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336]) == "42/(84/126/168/210/252/294/336)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 12, 3, 12, 3, 12]) == "3/(12/3/12/3/12)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 12, 3, 12, 3, 12]) == "3/(12/3/12/3/12)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == "100/(200/300/400/500/600/700/800/900)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == "100/(200/300/400/500/600/700/800/900)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 20, 4, 2, 1]) == "100/(20/4/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 20, 4, 2, 1]) == "100/(20/4/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == "6/(12/18/24/30/36/42/48/54/60)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == "6/(12/18/24/30/36/42/48/54/60)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800]) == "100/(200/300/400/500/600/700/800)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800]) == "100/(200/300/400/500/600/700/800)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "100/(90/80/70/60/50/40/30/20/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "100/(90/80/70/60/50/40/30/20/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 6, 3, 1, 2, 4, 8]) == "12/(6/3/1/2/4/8)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 6, 3, 1, 2, 4, 8]) == "12/(6/3/1/2/4/8)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == "3/(6/9/12/15/18/21/24/27)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == "3/(6/9/12/15/18/21/24/27)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 8, 12, 15, 20]) == "5/(8/12/15/20)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 8, 12, 15, 20]) == "5/(8/12/15/20)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28]) == "12/(14/16/18/20/22/24/26/28)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28]) == "12/(14/16/18/20/22/24/26/28)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == "2/(2/4/8/16/32/64/128/256/512)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == "2/(2/4/8/16/32/64/128/256/512)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 8, 6, 3, 4, 7]) == "10/(5/2/8/6/3/4/7)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 8, 6, 3, 4, 7]) == "10/(5/2/8/6/3/4/7)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == "25/(30/35/40/45/50/55/60/65/70)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == "25/(30/35/40/45/50/55/60/65/70)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 3, 4, 6, 7, 8, 9, 10]) == "2/(5/3/4/6/7/8/9/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 3, 4, 6, 7, 8, 9, 10]) == "2/(5/3/4/6/7/8/9/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30]) == "5/(10/15/20/25/30)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30]) == "5/(10/15/20/25/30)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 8, 2, 6, 4]) == "3/(5/8/2/6/4)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 8, 2, 6, 4]) == "3/(5/8/2/6/4)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 12, 4, 7, 9, 2]) == "8/(12/4/7/9/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 12, 4, 7, 9, 2]) == "8/(12/4/7/9/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [33, 66, 99, 132, 165, 198]) == "33/(66/99/132/165/198)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [33, 66, 99, 132, 165, 198]) == "33/(66/99/132/165/198)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29]) == "3/(5/7/11/13/17/19/23/29)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29]) == "3/(5/7/11/13/17/19/23/29)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 9, 3, 9, 3, 9, 3]) == "3/(9/3/9/3/9/3)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 9, 3, 9, 3, 9, 3]) == "3/(9/3/9/3/9/3)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 250, 125, 62, 31]) == "500/(250/125/62/31)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 250, 125, 62, 31]) == "500/(250/125/62/31)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 10, 5, 2, 1]) == "50/(10/5/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 10, 5, 2, 1]) == "50/(10/5/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 8, 4, 1]) == "10/(5/2/8/4/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 8, 4, 1]) == "10/(5/2/8/4/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 20, 10, 5]) == "100/(50/20/10/5)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 20, 10, 5]) == "100/(50/20/10/5)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "10/(15/20/25/30/35/40/45/50/55)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "10/(15/20/25/30/35/40/45/50/55)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53]) == "97/(89/83/79/73/71/67/61/59/53)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53]) == "97/(89/83/79/73/71/67/61/59/53)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == "2/(3/5/7/11/13/17/19/23)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == "2/(3/5/7/11/13/17/19/23)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 14, 16, 18, 20, 22]) == "12/(14/16/18/20/22)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 14, 16, 18, 20, 22]) == "12/(14/16/18/20/22)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == "9/(18/27/36/45/54/63/72/81/90)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == "9/(18/27/36/45/54/63/72/81/90)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == "999/(998/997/996/995/994/993/992/991/990)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == "999/(998/997/996/995/994/993/992/991/990)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 7, 11, 13, 17, 19]) == "2/(5/7/11/13/17/19)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 7, 11, 13, 17, 19]) == "2/(5/7/11/13/17/19)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2]) == "9/(8/7/6/5/4/3/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2]) == "9/(8/7/6/5/4/3/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 100, 10, 2, 5, 4, 3, 2, 1]) == "500/(100/10/2/5/4/3/2/1)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 100, 10, 2, 5, 4, 3, 2, 1]) == "500/(100/10/2/5/4/3/2/1)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "2/(4/6/8/10/12/14/16/18/20)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "2/(4/6/8/10/12/14/16/18/20)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17]) == "3/(5/7/9/11/13/15/17)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17]) == "3/(5/7/9/11/13/15/17)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == "5/(10/15/20/25/30/35/40/45)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == "5/(10/15/20/25/30/35/40/45)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == "4/(3/2/1/5/6/7/8/9/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == "4/(3/2/1/5/6/7/8/9/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 1, 2, 5, 10]) == "10/(5/2/1/2/5/10)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 1, 2, 5, 10]) == "10/(5/2/1/2/5/10)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 13, 5, 4, 17, 6, 7, 8]) == "3/(13/5/4/17/6/7/8)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 13, 5, 4, 17, 6, 7, 8]) == "3/(13/5/4/17/6/7/8)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75]) == "3/(11/19/27/35/43/51/59/67/75)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75]) == "3/(11/19/27/35/43/51/59/67/75)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == "1000/(2/3/4/5/6/7/8/9/10/11)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == "1000/(2/3/4/5/6/7/8/9/10/11)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 3, 2, 4, 10, 8, 6, 7]) == "500/(3/2/4/10/8/6/7)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 3, 2, 4, 10, 8, 6, 7]) == "500/(3/2/4/10/8/6/7)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3/3/3/3)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3/3/3/3)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 9, 12, 15, 18]) == "3/(5/9/12/15/18)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 9, 12, 15, 18]) == "3/(5/9/12/15/18)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [18, 6, 3, 2]) == "18/(6/3/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [18, 6, 3, 2]) == "18/(6/3/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 3, 2]) == "7/(5/3/2)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 3, 2]) == "7/(5/3/2)": {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == "7/(14/21/28/35/42/49/56/63)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == "7/(14/21/28/35/42/49/56/63)": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30]) == "10/(20/30)"
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2)"
    assert candidate(nums = [3, 100, 100, 100, 100, 100, 100, 100, 100, 100]) == "3/(100/100/100/100/100/100/100/100/100)"
    assert candidate(nums = [2, 3, 5, 7, 11]) == "2/(3/5/7/11)"
    assert candidate(nums = [3, 2]) == "3/2"
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == "10/(9/8/7/6/5/4/3/2/1)"
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)"
    assert candidate(nums = [10]) == "10"
    assert candidate(nums = [9, 8, 7, 6, 5]) == "9/(8/7/6/5)"
    assert candidate(nums = [2, 3]) == "2/3"
    assert candidate(nums = [5, 6, 7]) == "5/(6/7)"
    assert candidate(nums = [5, 5, 5, 5]) == "5/(5/5/5)"
    assert candidate(nums = [5, 6, 7, 8]) == "5/(6/7/8)"
    assert candidate(nums = [10, 2]) == "10/2"
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10]) == "3/(4/5/6/7/8/9/10)"
    assert candidate(nums = [2, 3, 4]) == "2/(3/4)"
    assert candidate(nums = [20, 10, 5, 2]) == "20/(10/5/2)"
    assert candidate(nums = [100, 50, 25, 10]) == "100/(50/25/10)"
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2]) == "10/(9/8/7/6/5/4/3/2)"
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1]) == "100/(50/25/12/6/3/1)"
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)"
    assert candidate(nums = [10, 5]) == "10/5"
    assert candidate(nums = [1000, 100, 10, 2]) == "1000/(100/10/2)"
    assert candidate(nums = [10, 20, 30, 40]) == "10/(20/30/40)"
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40]) == "100/(90/80/70/60/50/40)"
    assert candidate(nums = [101, 202, 303, 404, 505]) == "101/(202/303/404/505)"
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == "100/(200/300/400/500/600/700/800/900/1000)"
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3)"
    assert candidate(nums = [10, 5, 2, 6, 3]) == "10/(5/2/6/3)"
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)"
    assert candidate(nums = [8, 16, 32, 64, 128, 256]) == "8/(16/32/64/128/256)"
    assert candidate(nums = [3, 1000, 2, 5, 10]) == "3/(1000/2/5/10)"
    assert candidate(nums = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == "1024/(512/256/128/64/32/16/8/4/2)"
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == "99/(98/97/96/95/94/93/92/91/90)"
    assert candidate(nums = [25, 50, 75, 100, 125]) == "25/(50/75/100/125)"
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == "9/(8/7/6/5/4/3/2/1)"
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]) == "11/(22/33/44/55/66/77/88/99)"
    assert candidate(nums = [12, 15, 18, 21, 24, 27, 30]) == "12/(15/18/21/24/27/30)"
    assert candidate(nums = [5, 9, 12, 18, 24, 30, 36]) == "5/(9/12/18/24/30/36)"
    assert candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == "1000/(2/3/4/5/6/7/8/9/10)"
    assert candidate(nums = [10, 200, 3000, 40000, 500000]) == "10/(200/3000/40000/500000)"
    assert candidate(nums = [1000, 500, 250, 125, 62, 31]) == "1000/(500/250/125/62/31)"
    assert candidate(nums = [2, 5, 10, 20, 50, 100]) == "2/(5/10/20/50/100)"
    assert candidate(nums = [500, 250, 125, 62, 31, 15, 7]) == "500/(250/125/62/31/15/7)"
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41]) == "7/(11/13/17/19/23/29/31/37/41)"
    assert candidate(nums = [11, 13, 17, 19, 23, 29]) == "11/(13/17/19/23/29)"
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2)"
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49]) == "7/(14/21/28/35/42/49)"
    assert candidate(nums = [5, 10, 15, 20, 25]) == "5/(10/15/20/25)"
    assert candidate(nums = [999, 998, 997, 996, 995]) == "999/(998/997/996/995)"
    assert candidate(nums = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == "15/(25/35/45/55/65/75/85/95)"
    assert candidate(nums = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]) == "8/(16/32/64/128/256/512/1024/2048/4096)"
    assert candidate(nums = [10, 5, 2, 8, 3, 7, 4, 6]) == "10/(5/2/8/3/7/4/6)"
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == "8/(16/24/32/40/48/56/64/72/80)"
    assert candidate(nums = [30, 20, 10, 5, 1]) == "30/(20/10/5/1)"
    assert candidate(nums = [12, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "12/(15/20/25/30/35/40/45/50/55)"
    assert candidate(nums = [7, 11, 13, 17, 19, 23, 29, 31]) == "7/(11/13/17/19/23/29/31)"
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "2/(2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2/2)"
    assert candidate(nums = [8, 6, 4, 2]) == "8/(6/4/2)"
    assert candidate(nums = [15, 10, 20, 30, 40, 50]) == "15/(10/20/30/40/50)"
    assert candidate(nums = [150, 200, 250, 300, 350, 400, 450]) == "150/(200/250/300/350/400/450)"
    assert candidate(nums = [42, 84, 126, 168, 210, 252, 294, 336]) == "42/(84/126/168/210/252/294/336)"
    assert candidate(nums = [3, 12, 3, 12, 3, 12]) == "3/(12/3/12/3/12)"
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == "100/(200/300/400/500/600/700/800/900)"
    assert candidate(nums = [100, 20, 4, 2, 1]) == "100/(20/4/2/1)"
    assert candidate(nums = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]) == "6/(12/18/24/30/36/42/48/54/60)"
    assert candidate(nums = [10, 20, 30, 40, 50, 60]) == "10/(20/30/40/50/60)"
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800]) == "100/(200/300/400/500/600/700/800)"
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == "100/(90/80/70/60/50/40/30/20/10)"
    assert candidate(nums = [12, 6, 3, 1, 2, 4, 8]) == "12/(6/3/1/2/4/8)"
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == "3/(6/9/12/15/18/21/24/27)"
    assert candidate(nums = [5, 8, 12, 15, 20]) == "5/(8/12/15/20)"
    assert candidate(nums = [12, 14, 16, 18, 20, 22, 24, 26, 28]) == "12/(14/16/18/20/22/24/26/28)"
    assert candidate(nums = [2, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == "2/(2/4/8/16/32/64/128/256/512)"
    assert candidate(nums = [10, 5, 2, 8, 6, 3, 4, 7]) == "10/(5/2/8/6/3/4/7)"
    assert candidate(nums = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]) == "25/(30/35/40/45/50/55/60/65/70)"
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)"
    assert candidate(nums = [2, 5, 3, 4, 6, 7, 8, 9, 10]) == "2/(5/3/4/6/7/8/9/10)"
    assert candidate(nums = [5, 10, 15, 20, 25, 30]) == "5/(10/15/20/25/30)"
    assert candidate(nums = [3, 5, 8, 2, 6, 4]) == "3/(5/8/2/6/4)"
    assert candidate(nums = [8, 12, 4, 7, 9, 2]) == "8/(12/4/7/9/2)"
    assert candidate(nums = [33, 66, 99, 132, 165, 198]) == "33/(66/99/132/165/198)"
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)"
    assert candidate(nums = [3, 5, 7, 11, 13, 17, 19, 23, 29]) == "3/(5/7/11/13/17/19/23/29)"
    assert candidate(nums = [3, 9, 3, 9, 3, 9, 3]) == "3/(9/3/9/3/9/3)"
    assert candidate(nums = [500, 250, 125, 62, 31]) == "500/(250/125/62/31)"
    assert candidate(nums = [50, 10, 5, 2, 1]) == "50/(10/5/2/1)"
    assert candidate(nums = [10, 5, 2, 8, 4, 1]) == "10/(5/2/8/4/1)"
    assert candidate(nums = [100, 50, 20, 10, 5]) == "100/(50/20/10/5)"
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == "10/(15/20/25/30/35/40/45/50/55)"
    assert candidate(nums = [97, 89, 83, 79, 73, 71, 67, 61, 59, 53]) == "97/(89/83/79/73/71/67/61/59/53)"
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]) == "2/(3/5/7/11/13/17/19/23)"
    assert candidate(nums = [12, 14, 16, 18, 20, 22]) == "12/(14/16/18/20/22)"
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]) == "9/(18/27/36/45/54/63/72/81/90)"
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == "999/(998/997/996/995/994/993/992/991/990)"
    assert candidate(nums = [2, 5, 7, 11, 13, 17, 19]) == "2/(5/7/11/13/17/19)"
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2]) == "9/(8/7/6/5/4/3/2)"
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == "10/(20/30/40/50/60/70/80/90/100)"
    assert candidate(nums = [500, 100, 10, 2, 5, 4, 3, 2, 1]) == "500/(100/10/2/5/4/3/2/1)"
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == "2/(4/6/8/10/12/14/16/18/20)"
    assert candidate(nums = [3, 5, 7, 9, 11, 13, 15, 17]) == "3/(5/7/9/11/13/15/17)"
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == "5/(10/15/20/25/30/35/40/45)"
    assert candidate(nums = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]) == "4/(3/2/1/5/6/7/8/9/10)"
    assert candidate(nums = [10, 5, 2, 1, 2, 5, 10]) == "10/(5/2/1/2/5/10)"
    assert candidate(nums = [3, 13, 5, 4, 17, 6, 7, 8]) == "3/(13/5/4/17/6/7/8)"
    assert candidate(nums = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75]) == "3/(11/19/27/35/43/51/59/67/75)"
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == "2/(3/5/7/11/13/17/19/23/29)"
    assert candidate(nums = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == "1000/(2/3/4/5/6/7/8/9/10/11)"
    assert candidate(nums = [500, 3, 2, 4, 10, 8, 6, 7]) == "500/(3/2/4/10/8/6/7)"
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "3/(3/3/3/3/3/3/3/3/3/3/3/3)"
    assert candidate(nums = [3, 5, 9, 12, 15, 18]) == "3/(5/9/12/15/18)"
    assert candidate(nums = [18, 6, 3, 2]) == "18/(6/3/2)"
    assert candidate(nums = [7, 5, 3, 2]) == "7/(5/3/2)"
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63]) == "7/(14/21/28/35/42/49/56/63)"


