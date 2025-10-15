def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(equations = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3']],values = [1.1, 2.2, 3.3],queries = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3'], ['b1', 'a1']]) == [1.1, 2.2, 3.3, 0.9090909090909091]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3']],values = [1.1, 2.2, 3.3],queries = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3'], ['b1', 'a1']]) == [1.1, 2.2, 3.3, 0.9090909090909091]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c']],values = [2.0, 3.0],queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]) == [6.0, 0.5, -1, 1.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c']],values = [2.0, 3.0],queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]) == [6.0, 0.5, -1, 1.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b']],values = [0.5],queries = [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]) == [0.5, 2.0, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b']],values = [0.5],queries = [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]) == [0.5, 2.0, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'x2'], ['x3', 'x4']],values = [2.0, 3.0],queries = [['x1', 'x2'], ['x3', 'x4'], ['x1', 'x3']]) == [2.0, 3.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'x2'], ['x3', 'x4']],values = [2.0, 3.0],queries = [['x1', 'x2'], ['x3', 'x4'], ['x1', 'x3']]) == [2.0, 3.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['bc', 'cd']],values = [1.5, 2.5, 5.0],queries = [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]) == [3.75, 0.4, 5.0, 0.2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['bc', 'cd']],values = [1.5, 2.5, 5.0],queries = [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]) == [3.75, 0.4, 5.0, 0.2]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4']],values = [2.0, 3.0, 4.0],queries = [['x1', 'x4'], ['x4', 'x1'], ['x1', 'x5']]) == [24.0, 0.041666666666666664, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4']],values = [2.0, 3.0, 4.0],queries = [['x1', 'x4'], ['x4', 'x1'], ['x1', 'x5']]) == [24.0, 0.041666666666666664, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm1'], ['m1', 'm5']],values = [1.2, 2.3, 3.4, 4.5, 5.6],queries = [['m1', 'm3'], ['m3', 'm1'], ['m2', 'm4'], ['m4', 'm2'], ['m1', 'm6']]) == [2.76, 0.3623188405797102, 7.8199999999999985, 0.1278772378516624, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm1'], ['m1', 'm5']],values = [1.2, 2.3, 3.4, 4.5, 5.6],queries = [['m1', 'm3'], ['m3', 'm1'], ['m2', 'm4'], ['m4', 'm2'], ['m1', 'm6']]) == [2.76, 0.3623188405797102, 7.8199999999999985, 0.1278772378516624, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a']],values = [2.0, 3.0, 0.5, 0.333],queries = [['a', 'c'], ['c', 'a'], ['b', 'd'], ['d', 'b'], ['a', 'a'], ['e', 'e']]) == [6.0, 0.16666666666666666, 1.5, 0.6666666666666666, 1.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a']],values = [2.0, 3.0, 0.5, 0.333],queries = [['a', 'c'], ['c', 'a'], ['b', 'd'], ['d', 'b'], ['a', 'a'], ['e', 'e']]) == [6.0, 0.16666666666666666, 1.5, 0.6666666666666666, 1.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota'], ['iota', 'kappa'], ['kappa', 'lambda']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0],queries = [['alpha', 'lambda'], ['lambda', 'alpha'], ['beta', 'kappa'], ['kappa', 'beta'], ['gamma', 'iota'], ['iota', 'gamma'], ['delta', 'theta'], ['theta', 'delta'], ['epsilon', 'eta'], ['eta', 'epsilon'], ['alpha', 'mu']]) == [39916800.0, 2.505210838544172e-08, 1814400.0, 5.511463844797178e-07, 60480.0, 1.6534391534391536e-05, 1680.0, 0.0005952380952380953, 42.0, 0.023809523809523808, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota'], ['iota', 'kappa'], ['kappa', 'lambda']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0],queries = [['alpha', 'lambda'], ['lambda', 'alpha'], ['beta', 'kappa'], ['kappa', 'beta'], ['gamma', 'iota'], ['iota', 'gamma'], ['delta', 'theta'], ['theta', 'delta'], ['epsilon', 'eta'], ['eta', 'epsilon'], ['alpha', 'mu']]) == [39916800.0, 2.505210838544172e-08, 1814400.0, 5.511463844797178e-07, 60480.0, 1.6534391534391536e-05, 1680.0, 0.0005952380952380953, 42.0, 0.023809523809523808, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['nodeA', 'nodeB'], ['nodeB', 'nodeC'], ['nodeC', 'nodeD'], ['nodeD', 'nodeE'], ['nodeE', 'nodeF'], ['nodeF', 'nodeG'], ['nodeG', 'nodeH'], ['nodeH', 'nodeI'], ['nodeI', 'nodeJ'], ['nodeJ', 'nodeA']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1],queries = [['nodeA', 'nodeJ'], ['nodeJ', 'nodeA'], ['nodeB', 'nodeD'], ['nodeD', 'nodeB'], ['nodeE', 'nodeH'], ['nodeH', 'nodeE'], ['nodeF', 'nodeG'], ['nodeG', 'nodeF'], ['nodeA', 'nodeK']]) == [60.9493248, 0.016407072650622703, 1.8199999999999998, 0.5494505494505495, 4.896000000000001, 0.20424836601307186, 1.7, 0.5882352941176471, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['nodeA', 'nodeB'], ['nodeB', 'nodeC'], ['nodeC', 'nodeD'], ['nodeD', 'nodeE'], ['nodeE', 'nodeF'], ['nodeF', 'nodeG'], ['nodeG', 'nodeH'], ['nodeH', 'nodeI'], ['nodeI', 'nodeJ'], ['nodeJ', 'nodeA']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1],queries = [['nodeA', 'nodeJ'], ['nodeJ', 'nodeA'], ['nodeB', 'nodeD'], ['nodeD', 'nodeB'], ['nodeE', 'nodeH'], ['nodeH', 'nodeE'], ['nodeF', 'nodeG'], ['nodeG', 'nodeF'], ['nodeA', 'nodeK']]) == [60.9493248, 0.016407072650622703, 1.8199999999999998, 0.5494505494505495, 4.896000000000001, 0.20424836601307186, 1.7, 0.5882352941176471, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['a', 'g'], ['g', 'a'], ['b', 'f'], ['f', 'b'], ['c', 'e'], ['e', 'c'], ['a', 'h'], ['h', 'a']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['a', 'g'], ['g', 'a'], ['b', 'f'], ['f', 'b'], ['c', 'e'], ['e', 'c'], ['a', 'h'], ['h', 'a']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon']],values = [1.2, 1.3, 1.4, 1.5],queries = [['alpha', 'epsilon'], ['epsilon', 'alpha'], ['beta', 'delta'], ['gamma', 'beta'], ['alpha', 'zeta']]) == [3.2759999999999994, 0.30525030525030533, 1.8199999999999996, 0.7692307692307693, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon']],values = [1.2, 1.3, 1.4, 1.5],queries = [['alpha', 'epsilon'], ['epsilon', 'alpha'], ['beta', 'delta'], ['gamma', 'beta'], ['alpha', 'zeta']]) == [3.2759999999999994, 0.30525030525030533, 1.8199999999999996, 0.7692307692307693, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [120.0, 0.008333333333333333, 10.0, 0.6666666666666666, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [120.0, 0.008333333333333333, 10.0, 0.6666666666666666, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7']],values = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0],queries = [['var1', 'var7'], ['var7', 'var1'], ['var2', 'var6'], ['var3', 'var5'], ['x', 'y']]) == [64.0, 0.015625, 16.0, 4.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7']],values = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0],queries = [['var1', 'var7'], ['var7', 'var1'], ['var2', 'var6'], ['var3', 'var5'], ['x', 'y']]) == [64.0, 0.015625, 16.0, 4.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta']],values = [1.2, 1.3, 1.4, 1.5, 1.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['alpha', 'epsilon'], ['epsilon', 'alpha'], ['alpha', 'delta'], ['delta', 'alpha'], ['alpha', 'gamma'], ['gamma', 'alpha'], ['alpha', 'beta'], ['beta', 'alpha'], ['zeta', 'beta'], ['beta', 'zeta'], ['zeta', 'gamma'], ['gamma', 'zeta'], ['zeta', 'delta'], ['delta', 'zeta'], ['zeta', 'epsilon'], ['epsilon', 'zeta'], ['a', 'a'], ['b', 'b']]) == [5.2416, 0.19078144078144077, 3.276, 0.3052503052503053, 2.1839999999999997, 0.4578754578754579, 1.5599999999999998, 0.6410256410256411, 1.2, 0.8333333333333334, 0.22893772893772893, 4.368, 0.2976190476190476, 3.3600000000000003, 0.41666666666666663, 2.4000000000000004, 0.625, 1.6, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta']],values = [1.2, 1.3, 1.4, 1.5, 1.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['alpha', 'epsilon'], ['epsilon', 'alpha'], ['alpha', 'delta'], ['delta', 'alpha'], ['alpha', 'gamma'], ['gamma', 'alpha'], ['alpha', 'beta'], ['beta', 'alpha'], ['zeta', 'beta'], ['beta', 'zeta'], ['zeta', 'gamma'], ['gamma', 'zeta'], ['zeta', 'delta'], ['delta', 'zeta'], ['zeta', 'epsilon'], ['epsilon', 'zeta'], ['a', 'a'], ['b', 'b']]) == [5.2416, 0.19078144078144077, 3.276, 0.3052503052503053, 2.1839999999999997, 0.4578754578754579, 1.5599999999999998, 0.6410256410256411, 1.2, 0.8333333333333334, 0.22893772893772893, 4.368, 0.2976190476190476, 3.3600000000000003, 0.41666666666666663, 2.4000000000000004, 0.625, 1.6, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node1'], ['node1', 'node5']],values = [3.0, 4.0, 5.0, 6.0, 7.0],queries = [['node1', 'node5'], ['node5', 'node1'], ['node2', 'node4'], ['node3', 'node2'], ['node4', 'node3'], ['node1', 'node6']]) == [7.0, 0.14285714285714285, 20.0, 0.25, 0.19999999999999998, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node1'], ['node1', 'node5']],values = [3.0, 4.0, 5.0, 6.0, 7.0],queries = [['node1', 'node5'], ['node5', 'node1'], ['node2', 'node4'], ['node3', 'node2'], ['node4', 'node3'], ['node1', 'node6']]) == [7.0, 0.14285714285714285, 20.0, 0.25, 0.19999999999999998, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v1']],values = [3.0, 4.0, 5.0, 6.0],queries = [['v1', 'v4'], ['v4', 'v1'], ['v2', 'v3'], ['v3', 'v2'], ['v5', 'v5']]) == [60.0, 0.016666666666666666, 4.0, 0.25, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v1']],values = [3.0, 4.0, 5.0, 6.0],queries = [['v1', 'v4'], ['v4', 'v1'], ['v2', 'v3'], ['v3', 'v2'], ['v5', 'v5']]) == [60.0, 0.016666666666666666, 4.0, 0.25, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9'], ['var9', 'var10']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['var1', 'var10'], ['var10', 'var1'], ['var2', 'var9'], ['var9', 'var2'], ['var3', 'var8'], ['var8', 'var3'], ['var4', 'var7'], ['var7', 'var4'], ['var5', 'var6'], ['var6', 'var5']]) == [3628800.0, 2.755731922398589e-07, 181440.0, 5.5114638447971785e-06, 6720.0, 0.00014880952380952382, 210.0, 0.004761904761904762, 6.0, 0.16666666666666666]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9'], ['var9', 'var10']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['var1', 'var10'], ['var10', 'var1'], ['var2', 'var9'], ['var9', 'var2'], ['var3', 'var8'], ['var8', 'var3'], ['var4', 'var7'], ['var7', 'var4'], ['var5', 'var6'], ['var6', 'var5']]) == [3628800.0, 2.755731922398589e-07, 181440.0, 5.5114638447971785e-06, 6720.0, 0.00014880952380952382, 210.0, 0.004761904761904762, 6.0, 0.16666666666666666]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f']],values = [1.0, 2.0, 3.0, 4.0, 5.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'd'], ['d', 'b'], ['c', 'e'], ['e', 'c']]) == [120.0, 0.008333333333333333, 6.0, 0.16666666666666666, 12.0, 0.08333333333333333]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f']],values = [1.0, 2.0, 3.0, 4.0, 5.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'd'], ['d', 'b'], ['c', 'e'], ['e', 'c']]) == [120.0, 0.008333333333333333, 6.0, 0.16666666666666666, 12.0, 0.08333333333333333]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['u1', 'u2'], ['u2', 'u3'], ['u3', 'u4'], ['u4', 'u5'], ['u5', 'u6'], ['u6', 'u1'], ['u1', 'u7'], ['u7', 'u8']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8],queries = [['u1', 'u8'], ['u8', 'u1'], ['u2', 'u7'], ['u7', 'u2'], ['u3', 'u6'], ['u6', 'u3']]) == [67.76, 0.014757969303423848, 7.0, 0.14285714285714288, 79.86, 0.01252191334835963]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['u1', 'u2'], ['u2', 'u3'], ['u3', 'u4'], ['u4', 'u5'], ['u5', 'u6'], ['u6', 'u1'], ['u1', 'u7'], ['u7', 'u8']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8],queries = [['u1', 'u8'], ['u8', 'u1'], ['u2', 'u7'], ['u7', 'u2'], ['u3', 'u6'], ['u6', 'u3']]) == [67.76, 0.014757969303423848, 7.0, 0.14285714285714288, 79.86, 0.01252191334835963]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['var1', 'var5'], ['var5', 'var1'], ['var2', 'var4'], ['var3', 'var2'], ['var1', 'var6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['var1', 'var5'], ['var5', 'var1'], ['var2', 'var4'], ['var3', 'var2'], ['var1', 'var6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['q1', 'q2'], ['q2', 'q3'], ['q3', 'q4'], ['q4', 'q5'], ['q5', 'q6'], ['q6', 'q1'], ['q1', 'q7'], ['q7', 'q8'], ['q8', 'q9']],values = [0.5, 1.2, 1.8, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],queries = [['q1', 'q9'], ['q9', 'q1'], ['q2', 'q8'], ['q8', 'q2'], ['q3', 'q7'], ['q7', 'q3']]) == [90.00000000000001, 0.01111111111111111, 36.00000000000001, 0.027777777777777773, 6.666666666666668, 0.14999999999999997]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['q1', 'q2'], ['q2', 'q3'], ['q3', 'q4'], ['q4', 'q5'], ['q5', 'q6'], ['q6', 'q1'], ['q1', 'q7'], ['q7', 'q8'], ['q8', 'q9']],values = [0.5, 1.2, 1.8, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],queries = [['q1', 'q9'], ['q9', 'q1'], ['q2', 'q8'], ['q8', 'q2'], ['q3', 'q7'], ['q7', 'q3']]) == [90.00000000000001, 0.01111111111111111, 36.00000000000001, 0.027777777777777773, 6.666666666666668, 0.14999999999999997]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta']],values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['beta', 'epsilon'], ['epsilon', 'beta'], ['gamma', 'eta'], ['eta', 'gamma']]) == [0.0012000000000000001, 833.3333333333333, 0.024, 41.666666666666664, 0.036, 27.77777777777778]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta']],values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['beta', 'epsilon'], ['epsilon', 'beta'], ['gamma', 'eta'], ['eta', 'gamma']]) == [0.0012000000000000001, 833.3333333333333, 0.024, 41.666666666666664, 0.036, 27.77777777777778]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 0.5, 3.0, 0.25],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['b', 'c'], ['c', 'b'], ['a', 'x']]) == [0.75, 1.3333333333333333, 3.0, 0.3333333333333333, 0.5, 2.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 0.5, 3.0, 0.25],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['b', 'c'], ['c', 'b'], ['a', 'x']]) == [0.75, 1.3333333333333333, 3.0, 0.3333333333333333, 0.5, 2.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],queries = [['alpha', 'iota'], ['iota', 'alpha'], ['beta', 'theta'], ['gamma', 'delta'], ['z', 'z']]) == [30.4746624, 0.032814145301245407, 13.366080000000002, 1.4, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],queries = [['alpha', 'iota'], ['iota', 'alpha'], ['beta', 'theta'], ['gamma', 'delta'], ['z', 'z']]) == [30.4746624, 0.032814145301245407, 13.366080000000002, 1.4, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6'], ['v6', 'v7'], ['v7', 'v8'], ['v8', 'v9'], ['v9', 'v10'], ['v10', 'v11'], ['v11', 'v12'], ['v12', 'v13'], ['v13', 'v14'], ['v14', 'v15']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0],queries = [['v1', 'v15'], ['v15', 'v14'], ['v14', 'v13'], ['v13', 'v12'], ['v12', 'v11'], ['v11', 'v10'], ['v10', 'v9'], ['v9', 'v8'], ['v8', 'v7'], ['v7', 'v6'], ['v6', 'v5'], ['v5', 'v4'], ['v4', 'v3'], ['v3', 'v2'], ['v2', 'v1'], ['v1', 'v16']]) == [87178291200.0, 0.07142857142857142, 0.07692307692307693, 0.08333333333333333, 0.09090909090909091, 0.1, 0.1111111111111111, 0.125, 0.14285714285714285, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5, 1.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6'], ['v6', 'v7'], ['v7', 'v8'], ['v8', 'v9'], ['v9', 'v10'], ['v10', 'v11'], ['v11', 'v12'], ['v12', 'v13'], ['v13', 'v14'], ['v14', 'v15']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0],queries = [['v1', 'v15'], ['v15', 'v14'], ['v14', 'v13'], ['v13', 'v12'], ['v12', 'v11'], ['v11', 'v10'], ['v10', 'v9'], ['v9', 'v8'], ['v8', 'v7'], ['v7', 'v6'], ['v6', 'v5'], ['v5', 'v4'], ['v4', 'v3'], ['v3', 'v2'], ['v2', 'v1'], ['v1', 'v16']]) == [87178291200.0, 0.07142857142857142, 0.07692307692307693, 0.08333333333333333, 0.09090909090909091, 0.1, 0.1111111111111111, 0.125, 0.14285714285714285, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5, 1.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm5'], ['m5', 'm6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['m1', 'm6'], ['m6', 'm1'], ['m2', 'm4'], ['m3', 'm5'], ['m1', 'm7']]) == [3.6035999999999997, 0.2775002775002775, 1.56, 1.8199999999999996, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm5'], ['m5', 'm6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['m1', 'm6'], ['m6', 'm1'], ['m2', 'm4'], ['m3', 'm5'], ['m1', 'm7']]) == [3.6035999999999997, 0.2775002775002775, 1.56, 1.8199999999999996, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['x2', 'y2'], ['y2', 'z2'], ['x3', 'y3'], ['y3', 'z3'], ['x4', 'y4'], ['y4', 'z4']],values = [0.5, 2.0, 1.5, 3.0, 2.5, 4.0, 3.5, 5.0],queries = [['x1', 'z4'], ['z4', 'x1'], ['y2', 'z2'], ['x3', 'y3'], ['a', 'b']]) == [-1, -1, 3.0, 2.5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['x2', 'y2'], ['y2', 'z2'], ['x3', 'y3'], ['y3', 'z3'], ['x4', 'y4'], ['y4', 'z4']],values = [0.5, 2.0, 1.5, 3.0, 2.5, 4.0, 3.5, 5.0],queries = [['x1', 'z4'], ['z4', 'x1'], ['y2', 'z2'], ['x3', 'y3'], ['a', 'b']]) == [-1, -1, 3.0, 2.5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a1', 'b1'], ['b1', 'c1'], ['c1', 'd1'], ['d1', 'e1'], ['e1', 'f1'], ['f1', 'g1'], ['g1', 'h1']],values = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8],queries = [['a1', 'h1'], ['h1', 'a1'], ['b1', 'g1'], ['g1', 'b1'], ['c1', 'f1'], ['f1', 'c1']]) == [12358.277567999996, 8.09174251425909e-05, 1320.3287999999995, 0.0007573870993346508, 85.67999999999999, 0.011671335200746967]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a1', 'b1'], ['b1', 'c1'], ['c1', 'd1'], ['d1', 'e1'], ['e1', 'f1'], ['f1', 'g1'], ['g1', 'h1']],values = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8],queries = [['a1', 'h1'], ['h1', 'a1'], ['b1', 'g1'], ['g1', 'b1'], ['c1', 'f1'], ['f1', 'c1']]) == [12358.277567999996, 8.09174251425909e-05, 1320.3287999999995, 0.0007573870993346508, 85.67999999999999, 0.011671335200746967]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [2.5, 3.5, 4.5, 5.5],queries = [['m1', 'q1'], ['q1', 'm1'], ['n1', 'p1'], ['p1', 'n1'], ['m1', 'x1'], ['x1', 'm1']]) == [216.5625, 0.004617604617604618, 15.75, 0.06349206349206349, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [2.5, 3.5, 4.5, 5.5],queries = [['m1', 'q1'], ['q1', 'm1'], ['n1', 'p1'], ['p1', 'n1'], ['m1', 'x1'], ['x1', 'm1']]) == [216.5625, 0.004617604617604618, 15.75, 0.06349206349206349, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'c'], ['c', 'a'], ['a', 'e'], ['e', 'a'], ['x', 'x']]) == [6.000000000000001, 0.16666666666666666, 20.0, 0.05, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'c'], ['c', 'a'], ['a', 'e'], ['e', 'a'], ['x', 'x']]) == [6.000000000000001, 0.16666666666666666, 20.0, 0.05, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['x1', 'x6'], ['x6', 'x1'], ['x1', 'x5'], ['x5', 'x1'], ['x1', 'x4'], ['x4', 'x1'], ['x1', 'x3'], ['x3', 'x1'], ['x1', 'x2'], ['x2', 'x1'], ['x6', 'x2'], ['x2', 'x6'], ['x6', 'x3'], ['x3', 'x6'], ['x6', 'x4'], ['x4', 'x6'], ['x6', 'x5'], ['x5', 'x6']]) == [3.6035999999999997, 0.2775002775002775, 2.4023999999999996, 0.4162504162504163, 1.7160000000000002, 0.5827505827505827, 1.32, 0.7575757575757575, 1.1, 0.909090909090909, 0.30525030525030533, 3.2759999999999994, 0.3663003663003664, 2.7299999999999995, 0.4761904761904763, 2.0999999999999996, 0.6666666666666666, 1.5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['x1', 'x6'], ['x6', 'x1'], ['x1', 'x5'], ['x5', 'x1'], ['x1', 'x4'], ['x4', 'x1'], ['x1', 'x3'], ['x3', 'x1'], ['x1', 'x2'], ['x2', 'x1'], ['x6', 'x2'], ['x2', 'x6'], ['x6', 'x3'], ['x3', 'x6'], ['x6', 'x4'], ['x4', 'x6'], ['x6', 'x5'], ['x5', 'x6']]) == [3.6035999999999997, 0.2775002775002775, 2.4023999999999996, 0.4162504162504163, 1.7160000000000002, 0.5827505827505827, 1.32, 0.7575757575757575, 1.1, 0.909090909090909, 0.30525030525030533, 3.2759999999999994, 0.3663003663003664, 2.7299999999999995, 0.4761904761904763, 2.0999999999999996, 0.6666666666666666, 1.5]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['p1', 'q1'], ['p2', 'q2'], ['q1', 'q2'], ['q2', 'p1'], ['p1', 'p2']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['p1', 'p2'], ['p2', 'p1'], ['q1', 'q2'], ['q2', 'q1'], ['p1', 'q3']]) == [1.65, 0.6060606060606061, 3.3, 0.30303030303030304, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['p1', 'q1'], ['p2', 'q2'], ['q1', 'q2'], ['q2', 'p1'], ['p1', 'p2']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['p1', 'p2'], ['p2', 'p1'], ['q1', 'q2'], ['q2', 'q1'], ['p1', 'q3']]) == [1.65, 0.6060606060606061, 3.3, 0.30303030303030304, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5']],values = [0.5, 1.5, 2.5, 3.5],queries = [['p1', 'p5'], ['p5', 'p1'], ['p2', 'p4'], ['p4', 'p2'], ['p1', 'p6']]) == [6.5625, 0.1523809523809524, 3.75, 0.26666666666666666, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5']],values = [0.5, 1.5, 2.5, 3.5],queries = [['p1', 'p5'], ['p5', 'p1'], ['p2', 'p4'], ['p4', 'p2'], ['p1', 'p6']]) == [6.5625, 0.1523809523809524, 3.75, 0.26666666666666666, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['n1', 'n2'], ['n2', 'n3'], ['n3', 'n4'], ['n4', 'n1'], ['n1', 'n5'], ['n5', 'n6']],values = [0.7, 1.1, 1.3, 1.7, 2.1, 2.3],queries = [['n1', 'n4'], ['n4', 'n1'], ['n2', 'n5'], ['n5', 'n2'], ['n3', 'n6'], ['n6', 'n3']]) == [1.0010000000000001, 0.9990009990009989, 3.0000000000000004, 0.3333333333333333, 6.2727272727272725, 0.15942028985507248]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['n1', 'n2'], ['n2', 'n3'], ['n3', 'n4'], ['n4', 'n1'], ['n1', 'n5'], ['n5', 'n6']],values = [0.7, 1.1, 1.3, 1.7, 2.1, 2.3],queries = [['n1', 'n4'], ['n4', 'n1'], ['n2', 'n5'], ['n5', 'n2'], ['n3', 'n6'], ['n6', 'n3']]) == [1.0010000000000001, 0.9990009990009989, 3.0000000000000004, 0.3333333333333333, 6.2727272727272725, 0.15942028985507248]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't'], ['t', 'u']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['p', 'u'], ['u', 'p'], ['q', 't'], ['r', 's'], ['z', 'z']]) == [3.6035999999999997, 0.2775002775002775, 2.1839999999999997, 1.3, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't'], ['t', 'u']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['p', 'u'], ['u', 'p'], ['q', 't'], ['r', 's'], ['z', 'z']]) == [3.6035999999999997, 0.2775002775002775, 2.1839999999999997, 1.3, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [1.5, 2.5, 3.5, 4.5],queries = [['m1', 'o1'], ['o1', 'm1'], ['n1', 'q1'], ['q1', 'n1'], ['p1', 'p1']]) == [3.75, 0.26666666666666666, 39.375, 0.025396825396825397, 1.0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [1.5, 2.5, 3.5, 4.5],queries = [['m1', 'o1'], ['o1', 'm1'], ['n1', 'q1'], ['q1', 'n1'], ['p1', 'p1']]) == [3.75, 0.26666666666666666, 39.375, 0.025396825396825397, 1.0]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't']],values = [0.5, 2.0, 3.0, 4.0],queries = [['p', 't'], ['t', 'p'], ['q', 's'], ['s', 'q'], ['r', 'p'], ['x', 'y']]) == [12.0, 0.08333333333333333, 6.0, 0.16666666666666666, 1.0, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't']],values = [0.5, 2.0, 3.0, 4.0],queries = [['p', 't'], ['t', 'p'], ['q', 's'], ['s', 'q'], ['r', 'p'], ['x', 'y']]) == [12.0, 0.08333333333333333, 6.0, 0.16666666666666666, 1.0, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['u1', 'v1'], ['v1', 'w1'], ['u2', 'v2'], ['v2', 'w2'], ['u3', 'v3'], ['v3', 'w3'], ['u4', 'v4'], ['v4', 'w4']],values = [2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2],queries = [['u1', 'w4'], ['w4', 'u1'], ['v2', 'w2'], ['u3', 'v3'], ['a', 'b']]) == [-1, -1, 3.2, 4.1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['u1', 'v1'], ['v1', 'w1'], ['u2', 'v2'], ['v2', 'w2'], ['u3', 'v3'], ['v3', 'w3'], ['u4', 'v4'], ['v4', 'w4']],values = [2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2],queries = [['u1', 'w4'], ['w4', 'u1'], ['v2', 'w2'], ['u3', 'v3'], ['a', 'b']]) == [-1, -1, 3.2, 4.1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x0', 'y0'], ['y0', 'z0'], ['z0', 'x1'], ['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['w1', 'x2']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7],queries = [['x0', 'x2'], ['x2', 'x0'], ['y0', 'w1'], ['w1', 'y0'], ['z0', 'z1'], ['z1', 'z0'], ['x1', 'y1']]) == [9821.534184000002, 0.00010181708695053704, 1159.5672000000002, 0.0008623907264710488, 79.86, 0.012521913348359628, 4.4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x0', 'y0'], ['y0', 'z0'], ['z0', 'x1'], ['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['w1', 'x2']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7],queries = [['x0', 'x2'], ['x2', 'x0'], ['y0', 'w1'], ['w1', 'y0'], ['z0', 'z1'], ['z1', 'z0'], ['x1', 'y1']]) == [9821.534184000002, 0.00010181708695053704, 1159.5672000000002, 0.0008623907264710488, 79.86, 0.012521913348359628, 4.4]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h'], ['h', 'i'], ['i', 'j']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['a', 'j'], ['j', 'a'], ['b', 'd'], ['d', 'b'], ['e', 'h'], ['h', 'e'], ['f', 'g'], ['g', 'f'], ['a', 'k']]) == [3628800.0, 2.755731922398589e-07, 12.0, 0.08333333333333333, 336.0, 0.002976190476190476, 7.0, 0.14285714285714285, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h'], ['h', 'i'], ['i', 'j']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['a', 'j'], ['j', 'a'], ['b', 'd'], ['d', 'b'], ['e', 'h'], ['h', 'e'], ['f', 'g'], ['g', 'f'], ['a', 'k']]) == [3628800.0, 2.755731922398589e-07, 12.0, 0.08333333333333333, 336.0, 0.002976190476190476, 7.0, 0.14285714285714285, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'a'], ['d', 'e'], ['e', 'f'], ['f', 'd']],values = [2.0, 3.0, 0.5, 4.0, 5.0, 0.25],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [-1, -1, -1, -1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'a'], ['d', 'e'], ['e', 'f'], ['f', 'd']],values = [2.0, 3.0, 0.5, 4.0, 5.0, 0.25],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [-1, -1, -1, -1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['m2', 'n2'], ['n2', 'o2'], ['m3', 'n3'], ['n3', 'o3']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m1', 'o3'], ['o3', 'm1'], ['n2', 'o2'], ['m3', 'n3'], ['a', 'b']]) == [-1, -1, 4.5, 5.5, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['m2', 'n2'], ['n2', 'o2'], ['m3', 'n3'], ['n3', 'o3']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m1', 'o3'], ['o3', 'm1'], ['n2', 'o2'], ['m3', 'n3'], ['a', 'b']]) == [-1, -1, 4.5, 5.5, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['x1', 'w1'], ['w1', 'x1'], ['y1', 'w1']],values = [2.0, 3.0, 4.0, 24.0, 0.0416667, 12.0],queries = [['x1', 'z1'], ['z1', 'x1'], ['y1', 'w1'], ['w1', 'y1'], ['x1', 'y1'], ['y1', 'x1']]) == [6.0, 0.16666666666666666, 12.0, 0.08333333333333333, 2.0, 0.5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['x1', 'w1'], ['w1', 'x1'], ['y1', 'w1']],values = [2.0, 3.0, 4.0, 24.0, 0.0416667, 12.0],queries = [['x1', 'z1'], ['z1', 'x1'], ['y1', 'w1'], ['w1', 'y1'], ['x1', 'y1'], ['y1', 'x1']]) == [6.0, 0.16666666666666666, 12.0, 0.08333333333333333, 2.0, 0.5]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['x1', 'x5'], ['x5', 'x1'], ['x2', 'x4'], ['x3', 'x2'], ['x1', 'x6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['x1', 'x5'], ['x5', 'x1'], ['x2', 'x4'], ['x3', 'x2'], ['x1', 'x6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3'], ['y1', 'y2'], ['y2', 'y3'], ['y3', 'x1']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],queries = [['x1', 'y3'], ['y3', 'x1'], ['x2', 'y1'], ['y1', 'x2'], ['x3', 'y2'], ['y2', 'x3'], ['x1', 'x4']]) == [26.620000000000005, 0.03756574004507888, 0.5, 2.0, 0.6, 1.6666666666666667, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3'], ['y1', 'y2'], ['y2', 'y3'], ['y3', 'x1']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],queries = [['x1', 'y3'], ['y3', 'x1'], ['x2', 'y1'], ['y1', 'x2'], ['x3', 'y2'], ['y2', 'x3'], ['x1', 'x4']]) == [26.620000000000005, 0.03756574004507888, 0.5, 2.0, 0.6, 1.6666666666666667, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9']],values = [1.11, 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88],queries = [['var1', 'var9'], ['var9', 'var1'], ['var2', 'var8'], ['var8', 'var2'], ['var3', 'var7'], ['var7', 'var3']]) == [92918.9628750124, 1.0762065880407262e-05, 9426.889342891443, 0.00010607953096999833, 546.5053476000002, 0.0018298082615138891]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9']],values = [1.11, 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88],queries = [['var1', 'var9'], ['var9', 'var1'], ['var2', 'var8'], ['var8', 'var2'], ['var3', 'var7'], ['var7', 'var3']]) == [92918.9628750124, 1.0762065880407262e-05, 9426.889342891443, 0.00010607953096999833, 546.5053476000002, 0.0018298082615138891]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var1']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['var1', 'var3'], ['var3', 'var1'], ['var2', 'var4'], ['var4', 'var2'], ['var1', 'var5'], ['var5', 'var1'], ['var1', 'var6']]) == [2.4200000000000004, 0.4132231404958677, 7.26, 0.13774104683195593, 35.138400000000004, 0.02845889397354461, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var1']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['var1', 'var3'], ['var3', 'var1'], ['var2', 'var4'], ['var4', 'var2'], ['var1', 'var5'], ['var5', 'var1'], ['var1', 'var6']]) == [2.4200000000000004, 0.4132231404958677, 7.26, 0.13774104683195593, 35.138400000000004, 0.02845889397354461, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6']],values = [1.2, 1.5, 1.7, 1.9, 2.1],queries = [['v1', 'v6'], ['v6', 'v1'], ['v2', 'v5'], ['v5', 'v2'], ['v3', 'v4']]) == [12.209399999999997, 0.08190410667190855, 4.844999999999999, 0.20639834881320954, 1.7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6']],values = [1.2, 1.5, 1.7, 1.9, 2.1],queries = [['v1', 'v6'], ['v6', 'v1'], ['v2', 'v5'], ['v5', 'v2'], ['v3', 'v4']]) == [12.209399999999997, 0.08190410667190855, 4.844999999999999, 0.20639834881320954, 1.7]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5'], ['p5', 'p1']],values = [2.0, 3.0, 0.5, 0.25, 4.0],queries = [['p1', 'p3'], ['p3', 'p1'], ['p2', 'p5'], ['p4', 'p2'], ['p1', 'p6']]) == [6.0, 0.16666666666666666, 0.375, 0.6666666666666666, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5'], ['p5', 'p1']],values = [2.0, 3.0, 0.5, 0.25, 4.0],queries = [['p1', 'p3'], ['p3', 'p1'], ['p2', 'p5'], ['p4', 'p2'], ['p1', 'p6']]) == [6.0, 0.16666666666666666, 0.375, 0.6666666666666666, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['m', 'r'], ['r', 'q'], ['q', 'p'], ['p', 'o'], ['o', 'n'], ['n', 'm']]) == [720.0, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['m', 'r'], ['r', 'q'], ['q', 'p'], ['p', 'o'], ['o', 'n'], ['n', 'm']]) == [720.0, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x', 'y'], ['y', 'z'], ['z', 'w'], ['w', 'v'], ['v', 'u'], ['u', 't']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x', 't'], ['t', 'x'], ['y', 'u'], ['u', 'y'], ['z', 'v'], ['v', 'z']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x', 'y'], ['y', 'z'], ['z', 'w'], ['w', 'v'], ['v', 'u'], ['u', 't']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x', 't'], ['t', 'x'], ['y', 'u'], ['u', 'y'], ['z', 'v'], ['v', 'z']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r'], ['r', 's']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m', 's'], ['s', 'm'], ['m', 'r'], ['r', 'm'], ['m', 'q'], ['q', 'm'], ['m', 'p'], ['p', 'm'], ['m', 'o'], ['o', 'm'], ['m', 'n'], ['n', 'm'], ['t', 't']]) == [2111.484375, 0.0004736004736004736, 324.84375, 0.0030784030784030783, 59.0625, 0.016931216931216932, 13.125, 0.0761904761904762, 3.75, 0.26666666666666666, 1.5, 0.6666666666666666, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r'], ['r', 's']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m', 's'], ['s', 'm'], ['m', 'r'], ['r', 'm'], ['m', 'q'], ['q', 'm'], ['m', 'p'], ['p', 'm'], ['m', 'o'], ['o', 'm'], ['m', 'n'], ['n', 'm'], ['t', 't']]) == [2111.484375, 0.0004736004736004736, 324.84375, 0.0030784030784030783, 59.0625, 0.016931216931216932, 13.125, 0.0761904761904762, 3.75, 0.26666666666666666, 1.5, 0.6666666666666666, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['s1', 's2'], ['s2', 's3'], ['s3', 's4'], ['s4', 's5'], ['s5', 's1'], ['s1', 's6'], ['s6', 's2']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 2.0, 0.5],queries = [['s1', 's5'], ['s5', 's1'], ['s2', 's4'], ['s3', 's2'], ['s1', 's7']]) == [2.4024, 0.41625041625041626, 1.56, 0.8333333333333335, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['s1', 's2'], ['s2', 's3'], ['s3', 's4'], ['s4', 's5'], ['s5', 's1'], ['s1', 's6'], ['s6', 's2']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 2.0, 0.5],queries = [['s1', 's5'], ['s5', 's1'], ['s2', 's4'], ['s3', 's2'], ['s1', 's7']]) == [2.4024, 0.41625041625041626, 1.56, 0.8333333333333335, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x7'], ['x7', 'x1']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x1', 'x7'], ['x7', 'x1'], ['x2', 'x5'], ['x5', 'x2'], ['x3', 'x6'], ['x6', 'x3']]) == [720.0, 0.001388888888888889, 24.0, 0.041666666666666664, 60.0, 0.016666666666666666]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x7'], ['x7', 'x1']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x1', 'x7'], ['x7', 'x1'], ['x2', 'x5'], ['x5', 'x2'], ['x3', 'x6'], ['x6', 'x3']]) == [720.0, 0.001388888888888889, 24.0, 0.041666666666666664, 60.0, 0.016666666666666666]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['x', 'y']]) == [120.0, 0.008333333333333333, 24.0, 0.041666666666666664, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['x', 'y']]) == [120.0, 0.008333333333333333, 24.0, 0.041666666666666664, -1]: {e}')
    
    total += 1
    try:
        result = candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node5'], ['node5', 'node6'], ['node6', 'node7'], ['node7', 'node8'], ['node8', 'node9']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],queries = [['node1', 'node9'], ['node9', 'node1'], ['node2', 'node8'], ['node8', 'node2'], ['node3', 'node7'], ['node7', 'node3'], ['node4', 'node6'], ['node6', 'node4'], ['node1', 'node10']]) == [17.6432256, 0.0566789782476057, 8.91072, 0.11222437693025929, 4.368, 0.2289377289377289, 2.0999999999999996, 0.4761904761904762, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node5'], ['node5', 'node6'], ['node6', 'node7'], ['node7', 'node8'], ['node8', 'node9']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],queries = [['node1', 'node9'], ['node9', 'node1'], ['node2', 'node8'], ['node8', 'node2'], ['node3', 'node7'], ['node7', 'node3'], ['node4', 'node6'], ['node6', 'node4'], ['node1', 'node10']]) == [17.6432256, 0.0566789782476057, 8.91072, 0.11222437693025929, 4.368, 0.2289377289377289, 2.0999999999999996, 0.4761904761904762, -1]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(equations = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3']],values = [1.1, 2.2, 3.3],queries = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3'], ['b1', 'a1']]) == [1.1, 2.2, 3.3, 0.9090909090909091]
    assert candidate(equations = [['a', 'b'], ['b', 'c']],values = [2.0, 3.0],queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]) == [6.0, 0.5, -1, 1.0, -1]
    assert candidate(equations = [['a', 'b']],values = [0.5],queries = [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]) == [0.5, 2.0, -1, -1]
    assert candidate(equations = [['x1', 'x2'], ['x3', 'x4']],values = [2.0, 3.0],queries = [['x1', 'x2'], ['x3', 'x4'], ['x1', 'x3']]) == [2.0, 3.0, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['bc', 'cd']],values = [1.5, 2.5, 5.0],queries = [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]) == [3.75, 0.4, 5.0, 0.2]
    assert candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4']],values = [2.0, 3.0, 4.0],queries = [['x1', 'x4'], ['x4', 'x1'], ['x1', 'x5']]) == [24.0, 0.041666666666666664, -1]
    assert candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm1'], ['m1', 'm5']],values = [1.2, 2.3, 3.4, 4.5, 5.6],queries = [['m1', 'm3'], ['m3', 'm1'], ['m2', 'm4'], ['m4', 'm2'], ['m1', 'm6']]) == [2.76, 0.3623188405797102, 7.8199999999999985, 0.1278772378516624, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a']],values = [2.0, 3.0, 0.5, 0.333],queries = [['a', 'c'], ['c', 'a'], ['b', 'd'], ['d', 'b'], ['a', 'a'], ['e', 'e']]) == [6.0, 0.16666666666666666, 1.5, 0.6666666666666666, 1.0, -1]
    assert candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota'], ['iota', 'kappa'], ['kappa', 'lambda']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0],queries = [['alpha', 'lambda'], ['lambda', 'alpha'], ['beta', 'kappa'], ['kappa', 'beta'], ['gamma', 'iota'], ['iota', 'gamma'], ['delta', 'theta'], ['theta', 'delta'], ['epsilon', 'eta'], ['eta', 'epsilon'], ['alpha', 'mu']]) == [39916800.0, 2.505210838544172e-08, 1814400.0, 5.511463844797178e-07, 60480.0, 1.6534391534391536e-05, 1680.0, 0.0005952380952380953, 42.0, 0.023809523809523808, -1]
    assert candidate(equations = [['nodeA', 'nodeB'], ['nodeB', 'nodeC'], ['nodeC', 'nodeD'], ['nodeD', 'nodeE'], ['nodeE', 'nodeF'], ['nodeF', 'nodeG'], ['nodeG', 'nodeH'], ['nodeH', 'nodeI'], ['nodeI', 'nodeJ'], ['nodeJ', 'nodeA']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1],queries = [['nodeA', 'nodeJ'], ['nodeJ', 'nodeA'], ['nodeB', 'nodeD'], ['nodeD', 'nodeB'], ['nodeE', 'nodeH'], ['nodeH', 'nodeE'], ['nodeF', 'nodeG'], ['nodeG', 'nodeF'], ['nodeA', 'nodeK']]) == [60.9493248, 0.016407072650622703, 1.8199999999999998, 0.5494505494505495, 4.896000000000001, 0.20424836601307186, 1.7, 0.5882352941176471, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['a', 'g'], ['g', 'a'], ['b', 'f'], ['f', 'b'], ['c', 'e'], ['e', 'c'], ['a', 'h'], ['h', 'a']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05, -1, -1]
    assert candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon']],values = [1.2, 1.3, 1.4, 1.5],queries = [['alpha', 'epsilon'], ['epsilon', 'alpha'], ['beta', 'delta'], ['gamma', 'beta'], ['alpha', 'zeta']]) == [3.2759999999999994, 0.30525030525030533, 1.8199999999999996, 0.7692307692307693, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [120.0, 0.008333333333333333, 10.0, 0.6666666666666666, -1]
    assert candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7']],values = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0],queries = [['var1', 'var7'], ['var7', 'var1'], ['var2', 'var6'], ['var3', 'var5'], ['x', 'y']]) == [64.0, 0.015625, 16.0, 4.0, -1]
    assert candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta']],values = [1.2, 1.3, 1.4, 1.5, 1.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['alpha', 'epsilon'], ['epsilon', 'alpha'], ['alpha', 'delta'], ['delta', 'alpha'], ['alpha', 'gamma'], ['gamma', 'alpha'], ['alpha', 'beta'], ['beta', 'alpha'], ['zeta', 'beta'], ['beta', 'zeta'], ['zeta', 'gamma'], ['gamma', 'zeta'], ['zeta', 'delta'], ['delta', 'zeta'], ['zeta', 'epsilon'], ['epsilon', 'zeta'], ['a', 'a'], ['b', 'b']]) == [5.2416, 0.19078144078144077, 3.276, 0.3052503052503053, 2.1839999999999997, 0.4578754578754579, 1.5599999999999998, 0.6410256410256411, 1.2, 0.8333333333333334, 0.22893772893772893, 4.368, 0.2976190476190476, 3.3600000000000003, 0.41666666666666663, 2.4000000000000004, 0.625, 1.6, -1, -1]
    assert candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node1'], ['node1', 'node5']],values = [3.0, 4.0, 5.0, 6.0, 7.0],queries = [['node1', 'node5'], ['node5', 'node1'], ['node2', 'node4'], ['node3', 'node2'], ['node4', 'node3'], ['node1', 'node6']]) == [7.0, 0.14285714285714285, 20.0, 0.25, 0.19999999999999998, -1]
    assert candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v1']],values = [3.0, 4.0, 5.0, 6.0],queries = [['v1', 'v4'], ['v4', 'v1'], ['v2', 'v3'], ['v3', 'v2'], ['v5', 'v5']]) == [60.0, 0.016666666666666666, 4.0, 0.25, -1]
    assert candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9'], ['var9', 'var10']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['var1', 'var10'], ['var10', 'var1'], ['var2', 'var9'], ['var9', 'var2'], ['var3', 'var8'], ['var8', 'var3'], ['var4', 'var7'], ['var7', 'var4'], ['var5', 'var6'], ['var6', 'var5']]) == [3628800.0, 2.755731922398589e-07, 181440.0, 5.5114638447971785e-06, 6720.0, 0.00014880952380952382, 210.0, 0.004761904761904762, 6.0, 0.16666666666666666]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f']],values = [1.0, 2.0, 3.0, 4.0, 5.0],queries = [['a', 'f'], ['f', 'a'], ['b', 'd'], ['d', 'b'], ['c', 'e'], ['e', 'c']]) == [120.0, 0.008333333333333333, 6.0, 0.16666666666666666, 12.0, 0.08333333333333333]
    assert candidate(equations = [['u1', 'u2'], ['u2', 'u3'], ['u3', 'u4'], ['u4', 'u5'], ['u5', 'u6'], ['u6', 'u1'], ['u1', 'u7'], ['u7', 'u8']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8],queries = [['u1', 'u8'], ['u8', 'u1'], ['u2', 'u7'], ['u7', 'u2'], ['u3', 'u6'], ['u6', 'u3']]) == [67.76, 0.014757969303423848, 7.0, 0.14285714285714288, 79.86, 0.01252191334835963]
    assert candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['var1', 'var5'], ['var5', 'var1'], ['var2', 'var4'], ['var3', 'var2'], ['var1', 'var6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]
    assert candidate(equations = [['q1', 'q2'], ['q2', 'q3'], ['q3', 'q4'], ['q4', 'q5'], ['q5', 'q6'], ['q6', 'q1'], ['q1', 'q7'], ['q7', 'q8'], ['q8', 'q9']],values = [0.5, 1.2, 1.8, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],queries = [['q1', 'q9'], ['q9', 'q1'], ['q2', 'q8'], ['q8', 'q2'], ['q3', 'q7'], ['q7', 'q3']]) == [90.00000000000001, 0.01111111111111111, 36.00000000000001, 0.027777777777777773, 6.666666666666668, 0.14999999999999997]
    assert candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta']],values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],queries = [['alpha', 'zeta'], ['zeta', 'alpha'], ['beta', 'epsilon'], ['epsilon', 'beta'], ['gamma', 'eta'], ['eta', 'gamma']]) == [0.0012000000000000001, 833.3333333333333, 0.024, 41.666666666666664, 0.036, 27.77777777777778]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 0.5, 3.0, 0.25],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['b', 'c'], ['c', 'b'], ['a', 'x']]) == [0.75, 1.3333333333333333, 3.0, 0.3333333333333333, 0.5, 2.0, -1]
    assert candidate(equations = [['alpha', 'beta'], ['beta', 'gamma'], ['gamma', 'delta'], ['delta', 'epsilon'], ['epsilon', 'zeta'], ['zeta', 'eta'], ['eta', 'theta'], ['theta', 'iota']],values = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9],queries = [['alpha', 'iota'], ['iota', 'alpha'], ['beta', 'theta'], ['gamma', 'delta'], ['z', 'z']]) == [30.4746624, 0.032814145301245407, 13.366080000000002, 1.4, -1]
    assert candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6'], ['v6', 'v7'], ['v7', 'v8'], ['v8', 'v9'], ['v9', 'v10'], ['v10', 'v11'], ['v11', 'v12'], ['v12', 'v13'], ['v13', 'v14'], ['v14', 'v15']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0],queries = [['v1', 'v15'], ['v15', 'v14'], ['v14', 'v13'], ['v13', 'v12'], ['v12', 'v11'], ['v11', 'v10'], ['v10', 'v9'], ['v9', 'v8'], ['v8', 'v7'], ['v7', 'v6'], ['v6', 'v5'], ['v5', 'v4'], ['v4', 'v3'], ['v3', 'v2'], ['v2', 'v1'], ['v1', 'v16']]) == [87178291200.0, 0.07142857142857142, 0.07692307692307693, 0.08333333333333333, 0.09090909090909091, 0.1, 0.1111111111111111, 0.125, 0.14285714285714285, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5, 1.0, -1]
    assert candidate(equations = [['m1', 'm2'], ['m2', 'm3'], ['m3', 'm4'], ['m4', 'm5'], ['m5', 'm6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['m1', 'm6'], ['m6', 'm1'], ['m2', 'm4'], ['m3', 'm5'], ['m1', 'm7']]) == [3.6035999999999997, 0.2775002775002775, 1.56, 1.8199999999999996, -1]
    assert candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['x2', 'y2'], ['y2', 'z2'], ['x3', 'y3'], ['y3', 'z3'], ['x4', 'y4'], ['y4', 'z4']],values = [0.5, 2.0, 1.5, 3.0, 2.5, 4.0, 3.5, 5.0],queries = [['x1', 'z4'], ['z4', 'x1'], ['y2', 'z2'], ['x3', 'y3'], ['a', 'b']]) == [-1, -1, 3.0, 2.5, -1]
    assert candidate(equations = [['a1', 'b1'], ['b1', 'c1'], ['c1', 'd1'], ['d1', 'e1'], ['e1', 'f1'], ['f1', 'g1'], ['g1', 'h1']],values = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8],queries = [['a1', 'h1'], ['h1', 'a1'], ['b1', 'g1'], ['g1', 'b1'], ['c1', 'f1'], ['f1', 'c1']]) == [12358.277567999996, 8.09174251425909e-05, 1320.3287999999995, 0.0007573870993346508, 85.67999999999999, 0.011671335200746967]
    assert candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [2.5, 3.5, 4.5, 5.5],queries = [['m1', 'q1'], ['q1', 'm1'], ['n1', 'p1'], ['p1', 'n1'], ['m1', 'x1'], ['x1', 'm1']]) == [216.5625, 0.004617604617604618, 15.75, 0.06349206349206349, -1, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['a', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'c'], ['c', 'a'], ['a', 'e'], ['e', 'a'], ['x', 'x']]) == [6.000000000000001, 0.16666666666666666, 20.0, 0.05, -1]
    assert candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['x1', 'x6'], ['x6', 'x1'], ['x1', 'x5'], ['x5', 'x1'], ['x1', 'x4'], ['x4', 'x1'], ['x1', 'x3'], ['x3', 'x1'], ['x1', 'x2'], ['x2', 'x1'], ['x6', 'x2'], ['x2', 'x6'], ['x6', 'x3'], ['x3', 'x6'], ['x6', 'x4'], ['x4', 'x6'], ['x6', 'x5'], ['x5', 'x6']]) == [3.6035999999999997, 0.2775002775002775, 2.4023999999999996, 0.4162504162504163, 1.7160000000000002, 0.5827505827505827, 1.32, 0.7575757575757575, 1.1, 0.909090909090909, 0.30525030525030533, 3.2759999999999994, 0.3663003663003664, 2.7299999999999995, 0.4761904761904763, 2.0999999999999996, 0.6666666666666666, 1.5]
    assert candidate(equations = [['p1', 'q1'], ['p2', 'q2'], ['q1', 'q2'], ['q2', 'p1'], ['p1', 'p2']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['p1', 'p2'], ['p2', 'p1'], ['q1', 'q2'], ['q2', 'q1'], ['p1', 'q3']]) == [1.65, 0.6060606060606061, 3.3, 0.30303030303030304, -1]
    assert candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5']],values = [0.5, 1.5, 2.5, 3.5],queries = [['p1', 'p5'], ['p5', 'p1'], ['p2', 'p4'], ['p4', 'p2'], ['p1', 'p6']]) == [6.5625, 0.1523809523809524, 3.75, 0.26666666666666666, -1]
    assert candidate(equations = [['n1', 'n2'], ['n2', 'n3'], ['n3', 'n4'], ['n4', 'n1'], ['n1', 'n5'], ['n5', 'n6']],values = [0.7, 1.1, 1.3, 1.7, 2.1, 2.3],queries = [['n1', 'n4'], ['n4', 'n1'], ['n2', 'n5'], ['n5', 'n2'], ['n3', 'n6'], ['n6', 'n3']]) == [1.0010000000000001, 0.9990009990009989, 3.0000000000000004, 0.3333333333333333, 6.2727272727272725, 0.15942028985507248]
    assert candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't'], ['t', 'u']],values = [1.1, 1.2, 1.3, 1.4, 1.5],queries = [['p', 'u'], ['u', 'p'], ['q', 't'], ['r', 's'], ['z', 'z']]) == [3.6035999999999997, 0.2775002775002775, 2.1839999999999997, 1.3, -1]
    assert candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['o1', 'p1'], ['p1', 'q1']],values = [1.5, 2.5, 3.5, 4.5],queries = [['m1', 'o1'], ['o1', 'm1'], ['n1', 'q1'], ['q1', 'n1'], ['p1', 'p1']]) == [3.75, 0.26666666666666666, 39.375, 0.025396825396825397, 1.0]
    assert candidate(equations = [['p', 'q'], ['q', 'r'], ['r', 's'], ['s', 't']],values = [0.5, 2.0, 3.0, 4.0],queries = [['p', 't'], ['t', 'p'], ['q', 's'], ['s', 'q'], ['r', 'p'], ['x', 'y']]) == [12.0, 0.08333333333333333, 6.0, 0.16666666666666666, 1.0, -1]
    assert candidate(equations = [['u1', 'v1'], ['v1', 'w1'], ['u2', 'v2'], ['v2', 'w2'], ['u3', 'v3'], ['v3', 'w3'], ['u4', 'v4'], ['v4', 'w4']],values = [2.1, 2.2, 3.1, 3.2, 4.1, 4.2, 5.1, 5.2],queries = [['u1', 'w4'], ['w4', 'u1'], ['v2', 'w2'], ['u3', 'v3'], ['a', 'b']]) == [-1, -1, 3.2, 4.1, -1]
    assert candidate(equations = [['x0', 'y0'], ['y0', 'z0'], ['z0', 'x1'], ['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['w1', 'x2']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7],queries = [['x0', 'x2'], ['x2', 'x0'], ['y0', 'w1'], ['w1', 'y0'], ['z0', 'z1'], ['z1', 'z0'], ['x1', 'y1']]) == [9821.534184000002, 0.00010181708695053704, 1159.5672000000002, 0.0008623907264710488, 79.86, 0.012521913348359628, 4.4]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h'], ['h', 'i'], ['i', 'j']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],queries = [['a', 'j'], ['j', 'a'], ['b', 'd'], ['d', 'b'], ['e', 'h'], ['h', 'e'], ['f', 'g'], ['g', 'f'], ['a', 'k']]) == [3628800.0, 2.755731922398589e-07, 12.0, 0.08333333333333333, 336.0, 0.002976190476190476, 7.0, 0.14285714285714285, -1]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'a'], ['d', 'e'], ['e', 'f'], ['f', 'd']],values = [2.0, 3.0, 0.5, 4.0, 5.0, 0.25],queries = [['a', 'f'], ['f', 'a'], ['b', 'e'], ['c', 'd'], ['x', 'y']]) == [-1, -1, -1, -1, -1]
    assert candidate(equations = [['m1', 'n1'], ['n1', 'o1'], ['m2', 'n2'], ['n2', 'o2'], ['m3', 'n3'], ['n3', 'o3']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m1', 'o3'], ['o3', 'm1'], ['n2', 'o2'], ['m3', 'n3'], ['a', 'b']]) == [-1, -1, 4.5, 5.5, -1]
    assert candidate(equations = [['x1', 'y1'], ['y1', 'z1'], ['z1', 'w1'], ['x1', 'w1'], ['w1', 'x1'], ['y1', 'w1']],values = [2.0, 3.0, 4.0, 24.0, 0.0416667, 12.0],queries = [['x1', 'z1'], ['z1', 'x1'], ['y1', 'w1'], ['w1', 'y1'], ['x1', 'y1'], ['y1', 'x1']]) == [6.0, 0.16666666666666666, 12.0, 0.08333333333333333, 2.0, 0.5]
    assert candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5']],values = [2.0, 3.0, 4.0, 5.0],queries = [['x1', 'x5'], ['x5', 'x1'], ['x2', 'x4'], ['x3', 'x2'], ['x1', 'x6']]) == [120.0, 0.008333333333333333, 12.0, 0.3333333333333333, -1]
    assert candidate(equations = [['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3'], ['y1', 'y2'], ['y2', 'y3'], ['y3', 'x1']],values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],queries = [['x1', 'y3'], ['y3', 'x1'], ['x2', 'y1'], ['y1', 'x2'], ['x3', 'y2'], ['y2', 'x3'], ['x1', 'x4']]) == [26.620000000000005, 0.03756574004507888, 0.5, 2.0, 0.6, 1.6666666666666667, -1]
    assert candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var6'], ['var6', 'var7'], ['var7', 'var8'], ['var8', 'var9']],values = [1.11, 2.22, 3.33, 4.44, 5.55, 6.66, 7.77, 8.88],queries = [['var1', 'var9'], ['var9', 'var1'], ['var2', 'var8'], ['var8', 'var2'], ['var3', 'var7'], ['var7', 'var3']]) == [92918.9628750124, 1.0762065880407262e-05, 9426.889342891443, 0.00010607953096999833, 546.5053476000002, 0.0018298082615138891]
    assert candidate(equations = [['var1', 'var2'], ['var2', 'var3'], ['var3', 'var4'], ['var4', 'var5'], ['var5', 'var1']],values = [1.1, 2.2, 3.3, 4.4, 5.5],queries = [['var1', 'var3'], ['var3', 'var1'], ['var2', 'var4'], ['var4', 'var2'], ['var1', 'var5'], ['var5', 'var1'], ['var1', 'var6']]) == [2.4200000000000004, 0.4132231404958677, 7.26, 0.13774104683195593, 35.138400000000004, 0.02845889397354461, -1]
    assert candidate(equations = [['v1', 'v2'], ['v2', 'v3'], ['v3', 'v4'], ['v4', 'v5'], ['v5', 'v6']],values = [1.2, 1.5, 1.7, 1.9, 2.1],queries = [['v1', 'v6'], ['v6', 'v1'], ['v2', 'v5'], ['v5', 'v2'], ['v3', 'v4']]) == [12.209399999999997, 0.08190410667190855, 4.844999999999999, 0.20639834881320954, 1.7]
    assert candidate(equations = [['p1', 'p2'], ['p2', 'p3'], ['p3', 'p4'], ['p4', 'p5'], ['p5', 'p1']],values = [2.0, 3.0, 0.5, 0.25, 4.0],queries = [['p1', 'p3'], ['p3', 'p1'], ['p2', 'p5'], ['p4', 'p2'], ['p1', 'p6']]) == [6.0, 0.16666666666666666, 0.375, 0.6666666666666666, -1]
    assert candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r']],values = [2.0, 3.0, 4.0, 5.0, 6.0],queries = [['m', 'r'], ['r', 'q'], ['q', 'p'], ['p', 'o'], ['o', 'n'], ['n', 'm']]) == [720.0, 0.16666666666666666, 0.2, 0.25, 0.3333333333333333, 0.5]
    assert candidate(equations = [['x', 'y'], ['y', 'z'], ['z', 'w'], ['w', 'v'], ['v', 'u'], ['u', 't']],values = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x', 't'], ['t', 'x'], ['y', 'u'], ['u', 'y'], ['z', 'v'], ['v', 'z']]) == [5040.0, 0.0001984126984126984, 360.0, 0.002777777777777778, 20.0, 0.05]
    assert candidate(equations = [['m', 'n'], ['n', 'o'], ['o', 'p'], ['p', 'q'], ['q', 'r'], ['r', 's']],values = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],queries = [['m', 's'], ['s', 'm'], ['m', 'r'], ['r', 'm'], ['m', 'q'], ['q', 'm'], ['m', 'p'], ['p', 'm'], ['m', 'o'], ['o', 'm'], ['m', 'n'], ['n', 'm'], ['t', 't']]) == [2111.484375, 0.0004736004736004736, 324.84375, 0.0030784030784030783, 59.0625, 0.016931216931216932, 13.125, 0.0761904761904762, 3.75, 0.26666666666666666, 1.5, 0.6666666666666666, -1]
    assert candidate(equations = [['s1', 's2'], ['s2', 's3'], ['s3', 's4'], ['s4', 's5'], ['s5', 's1'], ['s1', 's6'], ['s6', 's2']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 2.0, 0.5],queries = [['s1', 's5'], ['s5', 's1'], ['s2', 's4'], ['s3', 's2'], ['s1', 's7']]) == [2.4024, 0.41625041625041626, 1.56, 0.8333333333333335, -1]
    assert candidate(equations = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x4'], ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x7'], ['x7', 'x1']],values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],queries = [['x1', 'x7'], ['x7', 'x1'], ['x2', 'x5'], ['x5', 'x2'], ['x3', 'x6'], ['x6', 'x3']]) == [720.0, 0.001388888888888889, 24.0, 0.041666666666666664, 60.0, 0.016666666666666666]
    assert candidate(equations = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e']],values = [2.0, 3.0, 4.0, 5.0],queries = [['a', 'e'], ['e', 'a'], ['a', 'd'], ['d', 'a'], ['x', 'y']]) == [120.0, 0.008333333333333333, 24.0, 0.041666666666666664, -1]
    assert candidate(equations = [['node1', 'node2'], ['node2', 'node3'], ['node3', 'node4'], ['node4', 'node5'], ['node5', 'node6'], ['node6', 'node7'], ['node7', 'node8'], ['node8', 'node9']],values = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8],queries = [['node1', 'node9'], ['node9', 'node1'], ['node2', 'node8'], ['node8', 'node2'], ['node3', 'node7'], ['node7', 'node3'], ['node4', 'node6'], ['node6', 'node4'], ['node1', 'node10']]) == [17.6432256, 0.0566789782476057, 8.91072, 0.11222437693025929, 4.368, 0.2289377289377289, 2.0999999999999996, 0.4761904761904762, -1]


