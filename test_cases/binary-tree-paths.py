def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == ['1->2->4', '1->2->5', '1->3->6', '1->3->7']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == ['1->2->4', '1->2->5', '1->3->6', '1->3->7']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5])) == ['1->2->5', '1->3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5])) == ['1->2->5', '1->3']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == ['-10->9', '-10->20->15', '-10->20->7']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == ['-10->9', '-10->20->15', '-10->20->7']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60])) == ['-10->-20->-40', '-10->-30->-50', '-10->-30->-60']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60])) == ['-10->-20->-40', '-10->-30->-50', '-10->-30->-60']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == ['1->2->3->4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == ['1->2->3->4']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, 0, 5, 9])) == ['-10->-5->5', '-10->-5->9', '-10->0']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, 0, 5, 9])) == ['-10->-5->5', '-10->-5->9', '-10->0']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1])) == ['1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1])) == ['1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3])) == ['1->2->3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3])) == ['1->2->3']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == ['0->2->1->5', '0->2->1->1', '0->4->3->6', '0->4->-1->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == ['0->2->1->5', '0->2->1->1', '0->4->3->6', '0->4->-1->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, None, None, 2])) == ['3->1->2']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, None, None, 2])) == ['3->1->2']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, 21, 18, 22])) == ['3->9', '3->20->15->21', '3->20->7->18', '3->20->7->22']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, 21, 18, 22])) == ['3->9', '3->20->15->21', '3->20->7->18', '3->20->7->22']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -3, 5, 1, None, -4, 6, -7, None, None, None, None, -8, -9, 7])) == ['2->-3->1->-7->-9', '2->-3->1->-7->7', '2->5->-4', '2->5->6->-8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -3, 5, 1, None, -4, 6, -7, None, None, None, None, -8, -9, 7])) == ['2->-3->1->-7->-9', '2->-3->1->-7->7', '2->5->-4', '2->5->6->-8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 50, None, -100, None, 100, -50, None, 50, None, -100, None, 100])) == ['100->-50->-100->-50->-100', '100->50->100->50->100']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 50, None, -100, None, 100, -50, None, 50, None, -100, None, 100])) == ['100->-50->-100->-50->-100', '100->50->100->50->100']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == ['5->4->11->7', '5->4->11->2->9', '5->8->13', '5->8->4->5', '5->8->4->1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == ['5->4->11->7', '5->4->11->2->9', '5->8->13', '5->8->4->5', '5->8->4->1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, None, 10, 11, None, 13, None, None, 16])) == ['1->2->4->8', '1->3->6->10->16', '1->3->6->11', '1->3->7->13']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, None, 10, 11, None, 13, None, None, 16])) == ['1->2->4->8', '1->3->6->10->16', '1->3->6->11', '1->3->7->13']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == ['0->1->3->7', '0->1->3->8', '0->1->4->9', '0->1->4->10', '0->2->5->11', '0->2->5->12', '0->2->6->13', '0->2->6->14']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == ['0->1->3->7', '0->1->3->8', '0->1->4->9', '0->1->4->10', '0->2->5->11', '0->2->5->12', '0->2->6->13', '0->2->6->14']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100])) == ['10->-10->-20->-40->-80', '10->-10->-20->-40->90', '10->-10->-20->50->-90', '10->-10->-20->50->100', '10->-10->30->-50->-100', '10->-10->30->60', '10->20->-30->-60', '10->20->-30->70', '10->20->40->-70', '10->20->40->80']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100])) == ['10->-10->-20->-40->-80', '10->-10->-20->-40->90', '10->-10->-20->50->-90', '10->-10->-20->50->100', '10->-10->30->-50->-100', '10->-10->30->60', '10->20->-30->-60', '10->20->-30->70', '10->20->40->-70', '10->20->40->80']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80])) == ['10->20->30->40->50->60->70->80']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80])) == ['10->20->30->40->50->60->70->80']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -2, 1, None, None, -3, None, -4, None, None, 5])) == ['0->-2', '0->1->-3->-4->5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -2, 1, None, None, -3, None, -4, None, None, 5])) == ['0->-2', '0->1->-3->-4->5']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12])) == ['1->2->4->8->11', '1->2->5->9', '1->3->6', '1->3->7->10->12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12])) == ['1->2->4->8->11', '1->2->5->9', '1->3->6', '1->3->7->10->12']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10->16', '1->2->5->11->17', '1->2->5->11->18', '1->3->6->12->19', '1->3->6->12->20', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10->16', '1->2->5->11->17', '1->2->5->11->18', '1->3->6->12->19', '1->3->6->12->20', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8', '1->2->4->9->16->30', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->2->5->11->21', '1->3->6->12->22', '1->3->6->12->23', '1->3->6->13->24', '1->3->6->13->25', '1->3->7->14->26', '1->3->7->14->27', '1->3->7->15->28', '1->3->7->15->29']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8', '1->2->4->9->16->30', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->2->5->11->21', '1->3->6->12->22', '1->3->6->12->23', '1->3->6->13->24', '1->3->6->13->25', '1->3->7->14->26', '1->3->7->14->27', '1->3->7->15->28', '1->3->7->15->29']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, 10, 11, None, None, 16, 17, 18, 19])) == ['1->2->4->8', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11', '1->3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, 10, 11, None, None, 16, 17, 18, 19])) == ['1->2->4->8', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11', '1->3']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 1, 7, 6, 9, 12, None, None, 2, None, None, None, None, None, None, 3])) == ['8->5->7', '8->5->6->2->3', '8->1->9', '8->1->12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 1, 7, 6, 9, 12, None, None, 2, None, None, None, None, None, None, 3])) == ['8->5->7', '8->5->6->2->3', '8->1->9', '8->1->12']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 5, None, 6, None, None, None, 7, None, 8])) == ['1->2->5', '1->3->6->7->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 5, None, 6, None, None, None, 7, None, 8])) == ['1->2->5', '1->3->6->7->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == ['1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == ['1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, None, -8, -9, -10, -11, -12, None, -13, None, None, -14])) == ['0->-1->-3->-7->-13', '0->-1->-4->-8->-14', '0->-1->-4->-9', '0->-2->-5->-10', '0->-2->-5->-11', '0->-2->-6->-12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, None, -8, -9, -10, -11, -12, None, -13, None, None, -14])) == ['0->-1->-3->-7->-13', '0->-1->-4->-8->-14', '0->-1->-4->-9', '0->-2->-5->-10', '0->-2->-5->-11', '0->-2->-6->-12']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -3, 9, -10, None, 5])) == ['0->-3->-10', '0->9->5']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -3, 9, -10, None, 5])) == ['0->-3->-10', '0->9->5']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->4->8->12', '1->2->5->9->13', '1->3->6->10->14', '1->3->7->11->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->4->8->12', '1->2->5->9->13', '1->3->6->10->14', '1->3->7->11->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 1, -2, -3, 2, 3, -4, -5, -6, -7, 4, 5, 6, 7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31])) == ['0->-1->-2->-4->-8->-24', '0->-1->-2->-4->-8->-25', '0->-1->-2->-4->-9->-26', '0->-1->-2->-4->-9->-27', '0->-1->-2->-5->-10->-28', '0->-1->-2->-5->-10->-29', '0->-1->-2->-5->-11->-30', '0->-1->-2->-5->-11->-31', '0->-1->-3->-6->-12', '0->-1->-3->-6->-13', '0->-1->-3->-7->-14', '0->-1->-3->-7->-15', '0->1->2->4->-16', '0->1->2->4->-17', '0->1->2->5->-18', '0->1->2->5->-19', '0->1->3->6->-20', '0->1->3->6->-21', '0->1->3->7->-22', '0->1->3->7->-23']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 1, -2, -3, 2, 3, -4, -5, -6, -7, 4, 5, 6, 7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31])) == ['0->-1->-2->-4->-8->-24', '0->-1->-2->-4->-8->-25', '0->-1->-2->-4->-9->-26', '0->-1->-2->-4->-9->-27', '0->-1->-2->-5->-10->-28', '0->-1->-2->-5->-10->-29', '0->-1->-2->-5->-11->-30', '0->-1->-2->-5->-11->-31', '0->-1->-3->-6->-12', '0->-1->-3->-6->-13', '0->-1->-3->-7->-14', '0->-1->-3->-7->-15', '0->1->2->4->-16', '0->1->2->4->-17', '0->1->2->5->-18', '0->1->2->5->-19', '0->1->3->6->-20', '0->1->3->6->-21', '0->1->3->7->-22', '0->1->3->7->-23']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8])) == ['1->2->4->7', '1->3->5', '1->3->6->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8])) == ['1->2->4->7', '1->3->5', '1->3->6->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 15, 7, 6, 8, 1, 2, None, None, None, None, None, 4])) == ['3->9->15->1', '3->9->15->2', '3->9->7', '3->20->6', '3->20->8->4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 15, 7, 6, 8, 1, 2, None, None, None, None, None, 4])) == ['3->9->15->1', '3->9->15->2', '3->9->7', '3->20->6', '3->20->8->4']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == ['0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == ['0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18])) == ['3->9', '3->20->15->12', '3->20->7->18']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18])) == ['3->9', '3->20->15->12', '3->20->7->18']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -50, 50, -25, 25, -75, 75, None, None, -100, 100, -125, 125])) == ['100->-50->-25', '100->-50->25->-100', '100->-50->25->100', '100->50->-75->-125', '100->50->-75->125', '100->50->75']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -50, 50, -25, 25, -75, 75, None, None, -100, 100, -125, 125])) == ['100->-50->-25', '100->-50->25->-100', '100->-50->25->100', '100->50->-75->-125', '100->50->-75->125', '100->50->75']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == ['10->5->3', '10->5->7', '10->15->18->16', '10->15->18->20']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == ['10->5->3', '10->5->7', '10->15->18->16', '10->15->18->20']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == ['-1->-2->-4->-8', '-1->-2->-4->-9', '-1->-2->-5->-10', '-1->-3->-6', '-1->-3->-7']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == ['-1->-2->-4->-8', '-1->-2->-4->-9', '-1->-2->-5->-10', '-1->-3->-6', '-1->-3->-7']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, -4, 8, -11, None, 17, 4, 7, 2, None, None, None, 1])) == ['5->-4->-11->7', '5->-4->-11->2', '5->8->17', '5->8->4->1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, -4, 8, -11, None, 17, 4, 7, 2, None, None, None, 1])) == ['5->-4->-11->7', '5->-4->-11->2', '5->8->17', '5->8->4->1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == ['10->5->3->3', '10->5->3->-2', '10->5->2->1', '10->-3->11']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == ['10->5->3->3', '10->5->3->-2', '10->5->2->1', '10->-3->11']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, -100, 50, -50, 25, 0, 75, None, -75, -25, None, 20, None, None, None, 60])) == ['100->-100->-50->-75->60', '100->-100->25->-25', '100->50->0->20', '100->50->75']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, -100, 50, -50, 25, 0, 75, None, -75, -25, None, 20, None, None, None, 60])) == ['100->-100->-50->-75->60', '100->-100->25->-25', '100->50->0->20', '100->50->75']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 6, None, None, 13, 18])) == ['3->9->8->4', '3->9->8->6', '3->20->15', '3->20->7->13', '3->20->7->18']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 6, None, None, 13, 18])) == ['3->9->8->4', '3->9->8->6', '3->20->15', '3->20->7->13', '3->20->7->18']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->10->21', '1->2->5->11->22', '1->2->5->11->23', '1->3->6->12->24', '1->3->6->12->25', '1->3->6->13->26', '1->3->6->13->27', '1->3->7->14->28', '1->3->7->14->29', '1->3->7->15->30']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->10->21', '1->2->5->11->22', '1->2->5->11->23', '1->3->6->12->24', '1->3->6->12->25', '1->3->6->13->26', '1->3->6->13->27', '1->3->7->14->28', '1->3->7->14->29', '1->3->7->15->30']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9])) == ['1->2->4->7->9', '1->2->5->8', '1->3->6']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9])) == ['1->2->4->7->9', '1->2->5->8', '1->3->6']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -3, 3, -4, -5, -6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['2->-3->-4->8->16', '2->-3->-4->8->17', '2->-3->-4->9->18', '2->-3->-4->9->19', '2->-3->-5->10->20', '2->-3->-5->11', '2->3->-6->12', '2->3->-6->13', '2->3->-7->14', '2->3->-7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -3, 3, -4, -5, -6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['2->-3->-4->8->16', '2->-3->-4->8->17', '2->-3->-4->9->18', '2->-3->-4->9->19', '2->-3->-5->10->20', '2->-3->-5->11', '2->3->-6->12', '2->3->-6->13', '2->3->-7->14', '2->3->-7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, None, None, 10, 11, None, None, 12, None])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->4->8', '1->2->5->9->12', '1->3->6']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, None, None, 10, 11, None, None, 12, None])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->4->8', '1->2->5->9->12', '1->3->6']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == ['3->5->6', '3->5->2->7', '3->5->2->4', '3->1->0', '3->1->8']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == ['3->5->6', '3->5->2->7', '3->5->2->4', '3->1->0', '3->1->8']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, -1])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15->-1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, -1])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15->-1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, None, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->15', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->3->6->12', '1->3->6->13', '1->3->7->14']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, None, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->15', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->3->6->12', '1->3->6->13', '1->3->7->14']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, None, 3, None, 4, None, 4])) == ['1->2->3->4', '1->2->3->4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, None, 3, None, 4, None, 4])) == ['1->2->3->4', '1->2->3->4']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->7->13', '1->2->4->7->14', '1->2->4->8->15', '1->3->5->9', '1->3->5->10', '1->3->6->11', '1->3->6->12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->7->13', '1->2->4->7->14', '1->2->4->8->15', '1->3->5->9', '1->3->5->10', '1->3->6->11', '1->3->6->12']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, 9, None, 11, 12, None, 14, 15, None, None, 16, 17])) == ['1->2->4->8->14', '1->2->4->8->15', '1->2->4->9', '1->3->6->11->16', '1->3->6->11->17', '1->3->7->12']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, 9, None, 11, 12, None, 14, 15, None, None, 16, 17])) == ['1->2->4->8->14', '1->2->4->8->15', '1->2->4->9', '1->3->6->11->16', '1->3->6->11->17', '1->3->7->12']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, None, 10])) == ['1->2->4->6->9', '1->2->4->7->10', '1->2->5->8', '1->3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, None, 10])) == ['1->2->4->6->9', '1->2->4->7->10', '1->2->5->8', '1->3']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, None])) == ['1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, None])) == ['1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == ['1->2->3', '1->2->4', '1->2->4', '1->2->3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == ['1->2->3', '1->2->4', '1->2->4', '1->2->3']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -3, 9, -10, None, 5, -1, -6, None, -8, None, None, None, -11, None, -12, None, 13, -13, -14])) == ['0->-3->-10->-6->-11->13', '0->-3->-10->-6->-11->-13', '0->9->5->-8->-12->-14', '0->9->-1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -3, 9, -10, None, 5, -1, -6, None, -8, None, None, None, -11, None, -12, None, 13, -13, -14])) == ['0->-3->-10->-6->-11->13', '0->-3->-10->-6->-11->-13', '0->9->5->-8->-12->-14', '0->9->-1']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18->19->20']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18->19->20']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, -3, -3, -4, None, -5, -4, None, -6, None, -7])) == ['2->-3->-4->-6', '2->-3->-5->-7', '2->-3->-4']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, -3, -3, -4, None, -5, -4, None, -6, None, -7])) == ['2->-3->-4->-6', '2->-3->-5->-7', '2->-3->-4']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 13, 14, 18, 19])) == ['3->9', '3->20->15->13', '3->20->15->14', '3->20->7->18', '3->20->7->19']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 13, 14, 18, 19])) == ['3->9', '3->20->15->13', '3->20->15->14', '3->20->7->18', '3->20->7->19']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, None, 14, 16, 12, 17])) == ['3->9->8', '3->9->10', '3->20->15->14', '3->20->15->16', '3->20->7->12', '3->20->7->17']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, None, 14, 16, 12, 17])) == ['3->9->8', '3->9->10', '3->20->15->14', '3->20->15->16', '3->20->7->12', '3->20->7->17']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 10, 11])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->5->8', '1->2->5->9', '1->3->6']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 10, 11])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->5->8', '1->2->5->9', '1->3->6']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == ['0->-1->-3->-7->-15', '0->-1->-3->-8', '0->-1->-4->-9', '0->-1->-4->-10', '0->-2->-5->-11', '0->-2->-5->-12', '0->-2->-6->-13', '0->-2->-6->-14']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == ['0->-1->-3->-7->-15', '0->-1->-3->-8', '0->-1->-4->-9', '0->-1->-4->-10', '0->-2->-5->-11', '0->-2->-5->-12', '0->-2->-6->-13', '0->-2->-6->-14']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == ['10->5->3->1', '10->5->7->6', '10->15->18']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == ['10->5->3->1', '10->5->7->6', '10->15->18']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 6, 10, None, None, 13, 17, 16])) == ['3->9->8->6->16', '3->9->8->10', '3->20->15', '3->20->7->13', '3->20->7->17']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 6, 10, None, None, 13, 17, 16])) == ['3->9->8->6->16', '3->9->8->10', '3->20->15', '3->20->7->13', '3->20->7->17']: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->5', '5->8->4->1']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->5', '5->8->4->1']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7])) == ['1->2->4', '1->2->5', '1->3->6', '1->3->7']
    assert candidate(root = tree_node([1, 2, 3, None, 5])) == ['1->2->5', '1->3']
    assert candidate(root = tree_node([-10, 9, 20, None, None, 15, 7])) == ['-10->9', '-10->20->15', '-10->20->7']
    assert candidate(root = tree_node([-10, -20, -30, -40, None, -50, -60])) == ['-10->-20->-40', '-10->-30->-50', '-10->-30->-60']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4])) == ['1->2->3->4']
    assert candidate(root = tree_node([-10, -5, 0, 5, 9])) == ['-10->-5->5', '-10->-5->9', '-10->0']
    assert candidate(root = tree_node([1])) == ['1']
    assert candidate(root = tree_node([1, None, 2, None, 3])) == ['1->2->3']
    assert candidate(root = tree_node([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8])) == ['0->2->1->5', '0->2->1->1', '0->4->3->6', '0->4->-1->8']
    assert candidate(root = tree_node([3, 1, None, None, 2])) == ['3->1->2']
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, None, 21, 18, 22])) == ['3->9', '3->20->15->21', '3->20->7->18', '3->20->7->22']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']
    assert candidate(root = tree_node([2, -3, 5, 1, None, -4, 6, -7, None, None, None, None, -8, -9, 7])) == ['2->-3->1->-7->-9', '2->-3->1->-7->7', '2->5->-4', '2->5->6->-8']
    assert candidate(root = tree_node([100, -50, 50, None, -100, None, 100, -50, None, 50, None, -100, None, 100])) == ['100->-50->-100->-50->-100', '100->50->100->50->100']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, None, None, None, 9])) == ['5->4->11->7', '5->4->11->2->9', '5->8->13', '5->8->4->5', '5->8->4->1']
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, None, 10, 11, None, 13, None, None, 16])) == ['1->2->4->8', '1->3->6->10->16', '1->3->6->11', '1->3->7->13']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == ['0->1->3->7', '0->1->3->8', '0->1->4->9', '0->1->4->10', '0->2->5->11', '0->2->5->12', '0->2->6->13', '0->2->6->14']
    assert candidate(root = tree_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50, 60, -60, 70, -70, 80, -80, 90, -90, 100, -100])) == ['10->-10->-20->-40->-80', '10->-10->-20->-40->90', '10->-10->-20->50->-90', '10->-10->-20->50->100', '10->-10->30->-50->-100', '10->-10->30->60', '10->20->-30->-60', '10->20->-30->70', '10->20->40->-70', '10->20->40->80']
    assert candidate(root = tree_node([10, None, 20, None, 30, None, 40, None, 50, None, 60, None, 70, None, 80])) == ['10->20->30->40->50->60->70->80']
    assert candidate(root = tree_node([0, -2, 1, None, None, -3, None, -4, None, None, 5])) == ['0->-2', '0->1->-3->-4->5']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9, None, None, 10, None, None, 11, None, None, 12])) == ['1->2->4->8->11', '1->2->5->9', '1->3->6', '1->3->7->10->12']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10->16', '1->2->5->11->17', '1->2->5->11->18', '1->3->6->12->19', '1->3->6->12->20', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8', '1->2->4->9->16->30', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->2->5->11->21', '1->3->6->12->22', '1->3->6->12->23', '1->3->6->13->24', '1->3->6->13->25', '1->3->7->14->26', '1->3->7->14->27', '1->3->7->15->28', '1->3->7->15->29']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 8, 9, 10, 11, None, None, 16, 17, 18, 19])) == ['1->2->4->8', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11', '1->3']
    assert candidate(root = tree_node([8, 5, 1, 7, 6, 9, 12, None, None, 2, None, None, None, None, None, None, 3])) == ['8->5->7', '8->5->6->2->3', '8->1->9', '8->1->12']
    assert candidate(root = tree_node([1, 2, 3, None, 5, None, 6, None, None, None, 7, None, 8])) == ['1->2->5', '1->3->6->7->8']
    assert candidate(root = tree_node([1, 2, 2, 3, 3, None, None, 4, 4, 4, 4])) == ['1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2->3->4', '1->2']
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, None, -8, -9, -10, -11, -12, None, -13, None, None, -14])) == ['0->-1->-3->-7->-13', '0->-1->-4->-8->-14', '0->-1->-4->-9', '0->-2->-5->-10', '0->-2->-5->-11', '0->-2->-6->-12']
    assert candidate(root = tree_node([0, -3, 9, -10, None, 5])) == ['0->-3->-10', '0->9->5']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->4->8->12', '1->2->5->9->13', '1->3->6->10->14', '1->3->7->11->15']
    assert candidate(root = tree_node([0, -1, 1, -2, -3, 2, 3, -4, -5, -6, -7, 4, 5, 6, 7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31])) == ['0->-1->-2->-4->-8->-24', '0->-1->-2->-4->-8->-25', '0->-1->-2->-4->-9->-26', '0->-1->-2->-4->-9->-27', '0->-1->-2->-5->-10->-28', '0->-1->-2->-5->-10->-29', '0->-1->-2->-5->-11->-30', '0->-1->-2->-5->-11->-31', '0->-1->-3->-6->-12', '0->-1->-3->-6->-13', '0->-1->-3->-7->-14', '0->-1->-3->-7->-15', '0->1->2->4->-16', '0->1->2->4->-17', '0->1->2->5->-18', '0->1->2->5->-19', '0->1->3->6->-20', '0->1->3->6->-21', '0->1->3->7->-22', '0->1->3->7->-23']
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, None, None, None, 8])) == ['1->2->4->7', '1->3->5', '1->3->6->8']
    assert candidate(root = tree_node([3, 9, 20, 15, 7, 6, 8, 1, 2, None, None, None, None, None, 4])) == ['3->9->15->1', '3->9->15->2', '3->9->7', '3->20->6', '3->20->8->4']
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']
    assert candidate(root = tree_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == ['0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0', '0->0->0->0->0']
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 12, None, None, 18])) == ['3->9', '3->20->15->12', '3->20->7->18']
    assert candidate(root = tree_node([100, -50, 50, -25, 25, -75, 75, None, None, -100, 100, -125, 125])) == ['100->-50->-25', '100->-50->25->-100', '100->-50->25->100', '100->50->-75->-125', '100->50->-75->125', '100->50->75']
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, None, None, None, 16, 20])) == ['10->5->3', '10->5->7', '10->15->18->16', '10->15->18->20']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15']
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->1']
    assert candidate(root = tree_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == ['-1->-2->-4->-8', '-1->-2->-4->-9', '-1->-2->-5->-10', '-1->-3->-6', '-1->-3->-7']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])) == ['1->2->3->4->5->6->7->8->9']
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == ['1->2->3->4->5->6->7->8->9->10']
    assert candidate(root = tree_node([5, -4, 8, -11, None, 17, 4, 7, 2, None, None, None, 1])) == ['5->-4->-11->7', '5->-4->-11->2', '5->8->17', '5->8->4->1']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 16])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']
    assert candidate(root = tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])) == ['10->5->3->3', '10->5->3->-2', '10->5->2->1', '10->-3->11']
    assert candidate(root = tree_node([100, -100, 50, -50, 25, 0, 75, None, -75, -25, None, 20, None, None, None, 60])) == ['100->-100->-50->-75->60', '100->-100->25->-25', '100->50->0->20', '100->50->75']
    assert candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 4, 6, None, None, 13, 18])) == ['3->9->8->4', '3->9->8->6', '3->20->15', '3->20->7->13', '3->20->7->18']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->15']
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])) == ['1->2->3->4->5->6->7->8']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->10->21', '1->2->5->11->22', '1->2->5->11->23', '1->3->6->12->24', '1->3->6->12->25', '1->3->6->13->26', '1->3->6->13->27', '1->3->7->14->28', '1->3->7->14->29', '1->3->7->15->30']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, None, None, None, 9])) == ['1->2->4->7->9', '1->2->5->8', '1->3->6']
    assert candidate(root = tree_node([2, -3, 3, -4, -5, -6, -7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['2->-3->-4->8->16', '2->-3->-4->8->17', '2->-3->-4->9->18', '2->-3->-4->9->19', '2->-3->-5->10->20', '2->-3->-5->11', '2->3->-6->12', '2->3->-6->13', '2->3->-7->14', '2->3->-7->15']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, 8, None, 9, None, None, 10, 11, None, None, 12, None])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->4->8', '1->2->5->9->12', '1->3->6']
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])) == ['3->5->6', '3->5->2->7', '3->5->2->4', '3->1->0', '3->1->8']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, -1])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15->-1']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, None, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->15', '1->2->4->9->16', '1->2->4->9->17', '1->2->5->10->18', '1->2->5->10->19', '1->2->5->11->20', '1->3->6->12', '1->3->6->13', '1->3->7->14']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == ['1->2->4->8->16', '1->2->4->8->17', '1->2->4->9->18', '1->2->4->9->19', '1->2->5->10->20', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([1, 2, 2, 3, None, 3, None, 4, None, 4])) == ['1->2->3->4', '1->2->3->4']
    assert candidate(root = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->7->13', '1->2->4->7->14', '1->2->4->8->15', '1->3->5->9', '1->3->5->10', '1->3->6->11', '1->3->6->12']
    assert candidate(root = tree_node([1, 2, 3, 4, None, 6, 7, 8, 9, None, 11, 12, None, 14, 15, None, None, 16, 17])) == ['1->2->4->8->14', '1->2->4->8->15', '1->2->4->9', '1->3->6->11->16', '1->3->6->11->17', '1->3->7->12']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14', '1->3->7->15']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None])) == ['1->2->4->8', '1->2->4->9', '1->2->5->10', '1->2->5->11', '1->3->6->12', '1->3->6->13', '1->3->7->14']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, None, 10])) == ['1->2->4->6->9', '1->2->4->7->10', '1->2->5->8', '1->3']
    assert candidate(root = tree_node([1, None, None])) == ['1']
    assert candidate(root = tree_node([1, 2, 2, 3, 4, 4, 3])) == ['1->2->3', '1->2->4', '1->2->4', '1->2->3']
    assert candidate(root = tree_node([0, -3, 9, -10, None, 5, -1, -6, None, -8, None, None, None, -11, None, -12, None, 13, -13, -14])) == ['0->-3->-10->-6->-11->13', '0->-3->-10->-6->-11->-13', '0->9->5->-8->-12->-14', '0->9->-1']
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15, None, 16, None, 17, None, 18, None, 19, None, 20])) == ['1->2->3->4->5->6->7->8->9->10->11->12->13->14->15->16->17->18->19->20']
    assert candidate(root = tree_node([2, -3, -3, -4, None, -5, -4, None, -6, None, -7])) == ['2->-3->-4->-6', '2->-3->-5->-7', '2->-3->-4']
    assert candidate(root = tree_node([3, 9, 20, None, None, 15, 7, 13, 14, 18, 19])) == ['3->9', '3->20->15->13', '3->20->15->14', '3->20->7->18', '3->20->7->19']
    assert candidate(root = tree_node([3, 9, 20, 8, 10, 15, 7, None, None, None, None, 14, 16, 12, 17])) == ['3->9->8', '3->9->10', '3->20->15->14', '3->20->15->16', '3->20->7->12', '3->20->7->17']
    assert candidate(root = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, None, None, 10, 11])) == ['1->2->4->7->10', '1->2->4->7->11', '1->2->5->8', '1->2->5->9', '1->3->6']
    assert candidate(root = tree_node([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])) == ['0->-1->-3->-7->-15', '0->-1->-3->-8', '0->-1->-4->-9', '0->-1->-4->-10', '0->-2->-5->-11', '0->-2->-5->-12', '0->-2->-6->-13', '0->-2->-6->-14']
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6])) == ['10->5->3->1', '10->5->7->6', '10->15->18']
    assert candidate(root = tree_node([3, 9, 20, 8, None, 15, 7, 6, 10, None, None, 13, 17, 16])) == ['3->9->8->6->16', '3->9->8->10', '3->20->15', '3->20->7->13', '3->20->7->17']
    assert candidate(root = tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])) == ['5->4->11->7', '5->4->11->2', '5->8->13', '5->8->4->5', '5->8->4->1']


