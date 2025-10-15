def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],bikes = [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]) == 4995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],bikes = [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]) == 4995: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 1], [1, 0]],bikes = [[2, 3], [3, 2], [4, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 1], [1, 0]],bikes = [[2, 3], [3, 2], [4, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 5], [20, 15], [30, 25], [40, 35]],bikes = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 5], [20, 15], [30, 25], [40, 35]],bikes = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [500, 500], [1000, 1000]],bikes = [[250, 250], [750, 750], [1250, 1250], [1750, 1750]]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [500, 500], [1000, 1000]],bikes = [[250, 250], [750, 750], [1250, 1250], [1750, 1750]]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [0, 0], [10, 10]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [0, 0], [10, 10]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [999, 0], [0, 999], [999, 999]],bikes = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]]) == 2996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [999, 0], [0, 999], [999, 999]],bikes = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]]) == 2996: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[150, 150], [250, 250], [350, 350], [400, 400], [450, 450]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[150, 150], [250, 250], [350, 350], [400, 400], [450, 450]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],bikes = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],bikes = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17]]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17]]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4]],bikes = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]]) == 9950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4]],bikes = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]]) == 9950: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]],bikes = [[50, 50], [125, 125], [175, 175], [225, 225], [275, 275], [350, 350], [400, 400], [450, 450], [500, 500]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]],bikes = [[50, 50], [125, 125], [175, 175], [225, 225], [275, 275], [350, 350], [400, 400], [450, 450], [500, 500]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[200, 0], [150, 50], [100, 100], [50, 150], [0, 200], [250, 250], [300, 300]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[200, 0], [150, 50], [100, 100], [50, 150], [0, 200], [250, 250], [300, 300]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 500], [500, 0], [500, 500]],bikes = [[250, 250], [250, 750], [750, 250], [750, 750], [0, 250], [0, 750], [500, 250], [500, 750]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 500], [500, 0], [500, 500]],bikes = [[250, 250], [250, 750], [750, 250], [750, 750], [0, 250], [0, 750], [500, 250], [500, 750]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 0], [998, 1], [997, 2]],bikes = [[500, 0], [501, 1], [502, 2], [503, 3], [504, 4]]) == 1491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 0], [998, 1], [997, 2]],bikes = [[500, 0], [501, 1], [502, 2], [503, 3], [504, 4]]) == 1491: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9900: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500]],bikes = [[100, 99], [200, 199], [300, 299], [400, 399], [500, 499], [600, 599], [700, 699], [800, 799], [900, 899]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500]],bikes = [[100, 99], [200, 199], [300, 299], [400, 399], [500, 499], [600, 599], [700, 699], [800, 799], [900, 899]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [150, 150], [250, 250], [350, 350]],bikes = [[55, 55], [155, 155], [255, 255], [355, 355], [455, 455], [555, 555]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [150, 150], [250, 250], [350, 350]],bikes = [[55, 55], [155, 155], [255, 255], [355, 355], [455, 455], [555, 555]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 10], [10, 0], [10, 10], [0, 0]],bikes = [[5, 5], [15, 15], [20, 20], [2, 2], [8, 8]]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 10], [10, 0], [10, 10], [0, 0]],bikes = [[5, 5], [15, 15], [20, 20], [2, 2], [8, 8]]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [9, 10], [11, 12], [13, 14], [15, 16]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [9, 10], [11, 12], [13, 14], [15, 16]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 0], [999, 1], [999, 2], [999, 3]],bikes = [[1000, 0], [1000, 1], [1000, 2], [1000, 3], [1001, 0], [1001, 1], [1001, 2], [1001, 3]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 0], [999, 1], [999, 2], [999, 3]],bikes = [[1000, 0], [1000, 1], [1000, 2], [1000, 3], [1001, 0], [1001, 1], [1001, 2], [1001, 3]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550], [650, 650], [750, 750]]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550], [650, 650], [750, 750]]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[500, 500], [600, 600], [700, 700]],bikes = [[550, 550], [650, 650], [750, 750], [850, 850]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[500, 500], [600, 600], [700, 700]],bikes = [[550, 550], [650, 650], [750, 750], [850, 850]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[50, 50], [40, 40], [30, 30], [20, 20], [10, 10], [0, 0], [15, 15], [25, 25], [35, 35], [45, 45]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[50, 50], [40, 40], [30, 30], [20, 20], [10, 10], [0, 0], [15, 15], [25, 25], [35, 35], [45, 45]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [5, 5]]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [5, 5]]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [9, 9], [10, 10], [11, 11], [12, 12]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [9, 9], [10, 10], [11, 11], [12, 12]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 0], [0, 1], [1, 2], [0, 3]],bikes = [[0, 0], [2, 0], [0, 2], [2, 2], [0, 4], [2, 4], [0, 6], [2, 6]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 0], [0, 1], [1, 2], [0, 3]],bikes = [[0, 0], [2, 0], [0, 2], [2, 2], [0, 4], [2, 4], [0, 6], [2, 6]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [70, 70], [75, 75], [80, 80]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [70, 70], [75, 75], [80, 80]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [3, 3], [5, 5], [7, 7]],bikes = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [3, 3], [5, 5], [7, 7]],bikes = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [16, 16], [17, 17]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [16, 16], [17, 17]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 0], [0, 1], [1, 2], [2, 1]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 0], [0, 1], [1, 2], [2, 1]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601], [701, 701], [801, 801], [901, 901]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601], [701, 701], [801, 801], [901, 901]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[994, 994], [993, 993], [992, 992], [991, 991], [990, 990], [989, 989], [988, 988], [987, 987], [986, 986]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[994, 994], [993, 993], [992, 992], [991, 991], [990, 990], [989, 989], [988, 988], [987, 987], [986, 986]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [6, 6], [11, 11], [16, 16], [2, 2], [7, 7], [12, 12], [17, 17]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [6, 6], [11, 11], [16, 16], [2, 2], [7, 7], [12, 12], [17, 17]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4], [994, 5]],bikes = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995], [994, 994], [993, 993]]) == 5964
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4], [994, 5]],bikes = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995], [994, 994], [993, 993]]) == 5964: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[40, 40], [55, 55], [65, 65], [75, 75], [85, 85], [90, 90]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[40, 40], [55, 55], [65, 65], [75, 75], [85, 85], [90, 90]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 2], [1, 3], [2, 1], [3, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 2], [1, 3], [2, 1], [3, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 20], [30, 40], [50, 60], [70, 80]],bikes = [[11, 21], [31, 41], [51, 61], [71, 81], [91, 91]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 20], [30, 40], [50, 60], [70, 80]],bikes = [[11, 21], [31, 41], [51, 61], [71, 81], [91, 91]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [50, 50], [100, 100]],bikes = [[25, 25], [75, 75], [125, 125], [150, 150]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [50, 50], [100, 100]],bikes = [[25, 25], [75, 75], [125, 125], [150, 150]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [1, 2], [1, 3], [1, 4]],bikes = [[1, 0], [1, 5], [2, 0], [2, 5], [3, 0], [3, 5], [4, 0], [4, 5]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [1, 2], [1, 3], [1, 4]],bikes = [[1, 0], [1, 5], [2, 0], [2, 5], [3, 0], [3, 5], [4, 0], [4, 5]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 100], [200, 100], [300, 200], [400, 300], [500, 400]],bikes = [[100, 0], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 100], [200, 100], [300, 200], [400, 300], [500, 400]],bikes = [[100, 0], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4975: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 999], [999, 1], [500, 500]],bikes = [[999, 999], [1, 1], [500, 1], [1, 500], [250, 250]]) == 1498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 999], [999, 1], [500, 500]],bikes = [[999, 999], [1, 1], [500, 1], [1, 500], [250, 250]]) == 1498: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[50, 40], [100, 90], [150, 140], [200, 190], [250, 240], [300, 290], [350, 340]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[50, 40], [100, 90], [150, 140], [200, 190], [250, 240], [300, 290], [350, 340]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],bikes = [[9, 0], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],bikes = [[9, 0], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 999], [1, 998], [2, 997]],bikes = [[0, 500], [1, 501], [2, 502], [3, 503], [4, 504]]) == 1491
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 999], [1, 998], [2, 997]],bikes = [[0, 500], [1, 501], [2, 502], [3, 503], [4, 504]]) == 1491: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 999], [999, 1], [500, 500], [250, 750]],bikes = [[500, 500], [250, 750], [750, 250], [999, 999], [1, 1]]) == 1496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 999], [999, 1], [500, 500], [250, 750]],bikes = [[500, 500], [250, 750], [750, 250], [999, 999], [1, 1]]) == 1496: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0], [6, 0], [7, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0], [6, 0], [7, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[110, 110], [210, 210], [310, 310], [410, 410], [510, 510]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[110, 110], [210, 210], [310, 310], [410, 410], [510, 510]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [50, 50], [55, 55], [60, 60]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [50, 50], [55, 55], [60, 60]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16]]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16]]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[500, 500], [501, 501], [502, 502]],bikes = [[499, 499], [500, 500], [501, 501], [502, 502]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[500, 500], [501, 501], [502, 502]],bikes = [[499, 499], [500, 500], [501, 501], [502, 502]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 4975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 4975: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[4, 6], [11, 12], [16, 14], [18, 18]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[4, 6], [11, 12], [16, 14], [18, 18]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(workers = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],bikes = [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]) == 4995
    assert candidate(workers = [[1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7]]) == 18
    assert candidate(workers = [[0, 0], [2, 1]],bikes = [[1, 2], [3, 3]]) == 6
    assert candidate(workers = [[0, 1], [1, 0]],bikes = [[2, 3], [3, 2], [4, 5]]) == 8
    assert candidate(workers = [[0, 0], [1, 1], [2, 0]],bikes = [[1, 0], [2, 2], [2, 1]]) == 4
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]) == 4
    assert candidate(workers = [[10, 5], [20, 15], [30, 25], [40, 35]],bikes = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50]]) == 40
    assert candidate(workers = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 60
    assert candidate(workers = [[0, 0], [500, 500], [1000, 1000]],bikes = [[250, 250], [750, 750], [1250, 1250], [1750, 1750]]) == 1500
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 40
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5], [0, 0], [10, 10]]) == 10
    assert candidate(workers = [[0, 0], [999, 0], [0, 999], [999, 999]],bikes = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]]) == 2996
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 80
    assert candidate(workers = [[100, 100], [200, 200], [300, 300]],bikes = [[150, 150], [250, 250], [350, 350], [400, 400], [450, 450]]) == 300
    assert candidate(workers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],bikes = [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]) == 10
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 0
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],bikes = [[0, 1], [1, 0], [2, 3], [3, 2], [4, 5], [5, 4], [6, 7], [7, 6], [8, 9], [9, 8]]) == 9
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]],bikes = [[8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16], [17, 17]]) == 98
    assert candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9]]) == 8
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]]) == 5
    assert candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4]],bikes = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]]) == 9950
    assert candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 15], [9, 17], [10, 19]]) == 12
    assert candidate(workers = [[100, 100], [150, 150], [200, 200], [250, 250], [300, 300]],bikes = [[50, 50], [125, 125], [175, 175], [225, 225], [275, 275], [350, 350], [400, 400], [450, 450], [500, 500]]) == 300
    assert candidate(workers = [[0, 0], [50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[200, 0], [150, 50], [100, 100], [50, 150], [0, 200], [250, 250], [300, 300]]) == 500
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],bikes = [[6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14]]) == 50
    assert candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 30
    assert candidate(workers = [[0, 0], [0, 500], [500, 0], [500, 500]],bikes = [[250, 250], [250, 750], [750, 250], [750, 750], [0, 250], [0, 750], [500, 250], [500, 750]]) == 1000
    assert candidate(workers = [[999, 0], [998, 1], [997, 2]],bikes = [[500, 0], [501, 1], [502, 2], [503, 3], [504, 4]]) == 1491
    assert candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 9900
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500]],bikes = [[100, 99], [200, 199], [300, 299], [400, 399], [500, 499], [600, 599], [700, 699], [800, 799], [900, 899]]) == 5
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
    assert candidate(workers = [[50, 50], [150, 150], [250, 250], [350, 350]],bikes = [[55, 55], [155, 155], [255, 255], [355, 355], [455, 455], [555, 555]]) == 40
    assert candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 1]]) == 12
    assert candidate(workers = [[0, 10], [10, 0], [10, 10], [0, 0]],bikes = [[5, 5], [15, 15], [20, 20], [2, 2], [8, 8]]) == 34
    assert candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450]]) == 500
    assert candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [9, 10], [11, 12], [13, 14], [15, 16]]) == 8
    assert candidate(workers = [[999, 0], [999, 1], [999, 2], [999, 3]],bikes = [[1000, 0], [1000, 1], [1000, 2], [1000, 3], [1001, 0], [1001, 1], [1001, 2], [1001, 3]]) == 4
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550], [650, 650], [750, 750]]) == 400
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85]]) == 50
    assert candidate(workers = [[500, 500], [600, 600], [700, 700]],bikes = [[550, 550], [650, 650], [750, 750], [850, 850]]) == 300
    assert candidate(workers = [[0, 0], [10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[50, 50], [40, 40], [30, 30], [20, 20], [10, 10], [0, 0], [15, 15], [25, 25], [35, 35], [45, 45]]) == 0
    assert candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [5, 5]]) == 16
    assert candidate(workers = [[1, 2], [3, 4], [5, 6], [7, 8]],bikes = [[8, 7], [6, 5], [4, 3], [2, 1], [0, 0], [9, 9], [10, 10], [11, 11], [12, 12]]) == 8
    assert candidate(workers = [[1, 0], [0, 1], [1, 2], [0, 3]],bikes = [[0, 0], [2, 0], [0, 2], [2, 2], [0, 4], [2, 4], [0, 6], [2, 6]]) == 4
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60]],bikes = [[5, 5], [15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [70, 70], [75, 75], [80, 80]]) == 60
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50]]) == 30
    assert candidate(workers = [[0, 0], [100, 100], [200, 200], [300, 300]],bikes = [[50, 50], [150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501]]) == 8
    assert candidate(workers = [[1, 1], [3, 3], [5, 5], [7, 7]],bikes = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]) == 8
    assert candidate(workers = [[10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [16, 16], [17, 17]]) == 40
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]) == 5
    assert candidate(workers = [[1, 0], [0, 1], [1, 2], [2, 1]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]) == 6
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600]],bikes = [[101, 101], [201, 201], [301, 301], [401, 401], [501, 501], [601, 601], [701, 701], [801, 801], [901, 901]]) == 12
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55]]) == 30
    assert candidate(workers = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995]],bikes = [[994, 994], [993, 993], [992, 992], [991, 991], [990, 990], [989, 989], [988, 988], [987, 987], [986, 986]]) == 50
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[150, 150], [250, 250], [350, 350], [450, 450], [550, 550]]) == 400
    assert candidate(workers = [[0, 0], [5, 5], [10, 10], [15, 15]],bikes = [[1, 1], [6, 6], [11, 11], [16, 16], [2, 2], [7, 7], [12, 12], [17, 17]]) == 8
    assert candidate(workers = [[999, 0], [998, 1], [997, 2], [996, 3], [995, 4], [994, 5]],bikes = [[999, 999], [998, 998], [997, 997], [996, 996], [995, 995], [994, 994], [993, 993]]) == 5964
    assert candidate(workers = [[50, 50], [60, 60], [70, 70]],bikes = [[40, 40], [55, 55], [65, 65], [75, 75], [85, 85], [90, 90]]) == 30
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3]]) == 8
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 32
    assert candidate(workers = [[0, 0], [0, 1], [1, 0], [1, 1]],bikes = [[2, 2], [2, 3], [3, 2], [3, 3], [1, 2], [1, 3], [2, 1], [3, 1]]) == 10
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]]) == 18
    assert candidate(workers = [[10, 20], [30, 40], [50, 60], [70, 80]],bikes = [[11, 21], [31, 41], [51, 61], [71, 81], [91, 91]]) == 8
    assert candidate(workers = [[0, 0], [50, 50], [100, 100]],bikes = [[25, 25], [75, 75], [125, 125], [150, 150]]) == 150
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95]]) == 50
    assert candidate(workers = [[1, 1], [1, 2], [1, 3], [1, 4]],bikes = [[1, 0], [1, 5], [2, 0], [2, 5], [3, 0], [3, 5], [4, 0], [4, 5]]) == 8
    assert candidate(workers = [[0, 100], [200, 100], [300, 200], [400, 300], [500, 400]],bikes = [[100, 0], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700]]) == 1000
    assert candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]) == 4975
    assert candidate(workers = [[1, 999], [999, 1], [500, 500]],bikes = [[999, 999], [1, 1], [500, 1], [1, 500], [250, 250]]) == 1498
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11]]) == 0
    assert candidate(workers = [[50, 50], [100, 100], [150, 150], [200, 200]],bikes = [[50, 40], [100, 90], [150, 140], [200, 190], [250, 240], [300, 290], [350, 340]]) == 40
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [55, 55], [65, 65], [75, 75], [85, 85], [95, 95], [105, 105]]) == 50
    assert candidate(workers = [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],bikes = [[9, 0], [8, 1], [7, 2], [6, 3], [5, 4], [4, 5], [3, 6], [2, 7], [1, 8], [0, 9]]) == 24
    assert candidate(workers = [[0, 999], [1, 998], [2, 997]],bikes = [[0, 500], [1, 501], [2, 502], [3, 503], [4, 504]]) == 1491
    assert candidate(workers = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 50
    assert candidate(workers = [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],bikes = [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17]]) == 27
    assert candidate(workers = [[10, 10], [20, 20], [30, 30]],bikes = [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]]) == 30
    assert candidate(workers = [[1, 999], [999, 1], [500, 500], [250, 750]],bikes = [[500, 500], [250, 750], [750, 250], [999, 999], [1, 1]]) == 1496
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4]],bikes = [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0], [6, 0], [7, 0]]) == 8
    assert candidate(workers = [[100, 100], [200, 200], [300, 300], [400, 400]],bikes = [[110, 110], [210, 210], [310, 310], [410, 410], [510, 510]]) == 80
    assert candidate(workers = [[10, 10], [20, 20], [30, 30], [40, 40]],bikes = [[15, 15], [25, 25], [35, 35], [45, 45], [50, 50], [55, 55], [60, 60]]) == 40
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],bikes = [[7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16]]) == 72
    assert candidate(workers = [[500, 500], [501, 501], [502, 502]],bikes = [[499, 499], [500, 500], [501, 501], [502, 502]]) == 0
    assert candidate(workers = [[0, 999], [1, 998], [2, 997], [3, 996], [4, 995]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 4975
    assert candidate(workers = [[5, 5], [10, 10], [15, 15]],bikes = [[4, 6], [11, 12], [16, 14], [18, 18]]) == 7
    assert candidate(workers = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]],bikes = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]) == 0
    assert candidate(workers = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],bikes = [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]]) == 25


