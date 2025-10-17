def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(username = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'a', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'a', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'x')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'x'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'b', 'c')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'b', 'c'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['joe', 'joe', 'joe', 'james', 'james', 'james', 'james', 'mary', 'mary', 'mary'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['joe', 'joe', 'joe', 'james', 'james', 'james', 'james', 'mary', 'mary', 'mary'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'z', 'y', 'x']) == ('x', 'z', 'y')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'z', 'y', 'x']) == ('x', 'z', 'y'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['mike', 'mike', 'mike'],timestamp = [3, 1, 2],website = ['a', 'b', 'c']) == ('b', 'c', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['mike', 'mike', 'mike'],timestamp = [3, 1, 2],website = ['a', 'b', 'c']) == ('b', 'c', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['u1', 'u2', 'u2', 'u2', 'u3', 'u3'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('y', 'z', 'x')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['u1', 'u2', 'u2', 'u2', 'u3', 'u3'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('y', 'z', 'x'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'y', 'z')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'y', 'z'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['ua', 'ua', 'ua', 'ub', 'ub', 'ub'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'a', 'a', 'b', 'c']) == ('a', 'b', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['ua', 'ua', 'ua', 'ub', 'ub', 'ub'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'a', 'a', 'b', 'c']) == ('a', 'b', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web1', 'web1', 'web1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web1', 'web1', 'web1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user2', 'user1', 'user3', 'user2', 'user1', 'user3', 'user2', 'user3', 'user1'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['site1', 'site1', 'site2', 'site1', 'site2', 'site3', 'site2', 'site3', 'site3', 'site1']) == ('site1', 'site2', 'site3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user2', 'user1', 'user3', 'user2', 'user1', 'user3', 'user2', 'user3', 'user1'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['site1', 'site1', 'site2', 'site1', 'site2', 'site3', 'site2', 'site3', 'site3', 'site1']) == ('site1', 'site2', 'site3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r']) == ('p', 'p', 'p')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r']) == ('p', 'p', 'p'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34],website = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == ('a', 'a', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34],website = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == ('a', 'a', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['xavier', 'xavier', 'xavier', 'xavier', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary'],timestamp = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['xavier', 'xavier', 'xavier', 'xavier', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary'],timestamp = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11, 13, 15],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web2', 'web3', 'web1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11, 13, 15],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web2', 'web3', 'web1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userA', 'userA', 'userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2']) == ('web1', 'web1', 'web2')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userA', 'userA', 'userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2']) == ('web1', 'web1', 'web2'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ']) == ('siteX', 'siteY', 'siteZ')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ']) == ('siteX', 'siteY', 'siteZ'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],timestamp = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10, 11, 12],website = ['site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4']) == ('site1', 'site1', 'site3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],timestamp = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10, 11, 12],website = ['site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4']) == ('site1', 'site1', 'site3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y']) == ('x', 'x', 'x')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y']) == ('x', 'x', 'x'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['game', 'movie', 'game', 'music', 'game', 'movie', 'music', 'game', 'movie', 'game', 'movie']) == ('game', 'game', 'game')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['game', 'movie', 'game', 'music', 'game', 'movie', 'music', 'game', 'movie', 'game', 'movie']) == ('game', 'game', 'game'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user5', 'user5', 'user5'],timestamp = [5, 2, 8, 6, 1, 4, 3, 7, 9, 11, 13, 10, 14, 12, 15],website = ['siteA', 'siteB', 'siteC', 'siteB', 'siteD', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteD', 'siteE', 'siteF', 'siteA', 'siteG']) == ('siteA', 'siteB', 'siteC')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user5', 'user5', 'user5'],timestamp = [5, 2, 8, 6, 1, 4, 3, 7, 9, 11, 13, 10, 14, 12, 15],website = ['siteA', 'siteB', 'siteC', 'siteB', 'siteD', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteD', 'siteE', 'siteF', 'siteA', 'siteG']) == ('siteA', 'siteB', 'siteC'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'about', 'career', 'career', 'home', 'home', 'about', 'about', 'career', 'career']) == ('about', 'about', 'career')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'about', 'career', 'career', 'home', 'home', 'about', 'about', 'career', 'career']) == ('about', 'about', 'career'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie', 'alice', 'bob', 'charlie', 'bob', 'alice'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['x', 'y', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'y')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie', 'alice', 'bob', 'charlie', 'bob', 'alice'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['x', 'y', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'y'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [10, 20, 30, 15, 25, 35, 5, 15, 25],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [10, 20, 30, 15, 25, 35, 5, 15, 25],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4']) == ('web1', 'web1', 'web1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4']) == ('web1', 'web1', 'web1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4', 'user4'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB']) == ('siteA', 'siteB', 'siteC')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4', 'user4'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB']) == ('siteA', 'siteB', 'siteC'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],timestamp = [1, 5, 10, 2, 3, 4, 6, 7, 8, 9, 11],website = ['news', 'shop', 'news', 'news', 'shop', 'news', 'shop', 'news', 'shop', 'news', 'news']) == ('news', 'shop', 'news')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],timestamp = [1, 5, 10, 2, 3, 4, 6, 7, 8, 9, 11],website = ['news', 'shop', 'news', 'news', 'shop', 'news', 'shop', 'news', 'shop', 'news', 'news']) == ('news', 'shop', 'news'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three']) == ('one', 'one', 'one')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three']) == ('one', 'one', 'one'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2'],timestamp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],website = ['x', 'x', 'y', 'y', 'z', 'z', 'x', 'x', 'y', 'y', 'z', 'z']) == ('x', 'x', 'y')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2'],timestamp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],website = ['x', 'x', 'y', 'y', 'z', 'z', 'x', 'x', 'y', 'y', 'z', 'z']) == ('x', 'x', 'y'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == ('a', 'b', 'c')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == ('a', 'b', 'c'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['person1', 'person1', 'person1', 'person2', 'person2', 'person2', 'person3', 'person3', 'person3', 'person4', 'person4', 'person4'],timestamp = [10, 20, 30, 15, 25, 35, 40, 50, 60, 45, 55, 65],website = ['store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout']) == ('store', 'cart', 'checkout')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['person1', 'person1', 'person1', 'person2', 'person2', 'person2', 'person3', 'person3', 'person3', 'person4', 'person4', 'person4'],timestamp = [10, 20, 30, 15, 25, 35, 40, 50, 60, 45, 55, 65],website = ['store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout']) == ('store', 'cart', 'checkout'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userX', 'userY', 'userZ', 'userX', 'userY', 'userZ', 'userX', 'userY', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma']) == ('alpha', 'alpha', 'alpha')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userX', 'userY', 'userZ', 'userX', 'userY', 'userZ', 'userX', 'userY', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma']) == ('alpha', 'alpha', 'alpha'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],website = ['home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore']) == ('explore', 'explore', 'explore')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],website = ['home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore']) == ('explore', 'explore', 'explore'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3],website = ['s', 't', 'u', 's', 't', 'u', 's', 't', 'u']) == ('s', 's', 's')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3],website = ['s', 't', 'u', 's', 't', 'u', 's', 't', 'u']) == ('s', 's', 's'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteA', 'siteA')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteA', 'siteA'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech']) == ('fun', 'fun', 'fun')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech']) == ('fun', 'fun', 'fun'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie', 'dave', 'dave', 'dave'],timestamp = [10, 15, 12, 20, 22, 21, 30, 25, 27, 35, 33, 34],website = ['site1', 'site2', 'site3', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site5', 'site6']) == ('site1', 'site3', 'site2')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie', 'dave', 'dave', 'dave'],timestamp = [10, 15, 12, 20, 22, 21, 30, 25, 27, 35, 33, 34],website = ['site1', 'site2', 'site3', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site5', 'site6']) == ('site1', 'site3', 'site2'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'career', 'home', 'home', 'about', 'career', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'career', 'home', 'home', 'about', 'career', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career', 'home', 'about', 'career', 'home', 'about']) == ('about', 'career', 'home')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career', 'home', 'about', 'career', 'home', 'about']) == ('about', 'career', 'home'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site1', 'site3', 'site1', 'site2', 'site1', 'site3']) == ('site1', 'site2', 'site3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site1', 'site3', 'site1', 'site2', 'site1', 'site3']) == ('site1', 'site2', 'site3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) == ('a', 'a', 'd')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) == ('a', 'a', 'd'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site2', 'site3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site2', 'site3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],website = ['w', 'x', 'y', 'z', 'w', 'x', 'y', 'w', 'x', 'y', 'z', 'w', 'x', 'y']) == ('w', 'w', 'x')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],website = ['w', 'x', 'y', 'z', 'w', 'x', 'y', 'w', 'x', 'y', 'z', 'w', 'x', 'y']) == ('w', 'w', 'x'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3'],timestamp = [10, 20, 30, 11, 21, 31, 12, 22, 32],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3'],timestamp = [10, 20, 30, 11, 21, 31, 12, 22, 32],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1']) == ('site1', 'site2', 'site1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1']) == ('site1', 'site2', 'site1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userA', 'userA', 'userB', 'userB', 'userC', 'userC', 'userA', 'userB', 'userC'],timestamp = [100, 200, 150, 250, 200, 300, 250, 350, 450],website = ['pageX', 'pageY', 'pageX', 'pageY', 'pageZ', 'pageX', 'pageZ', 'pageY', 'pageZ']) == ('pageX', 'pageY', 'pageY')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userA', 'userA', 'userB', 'userB', 'userC', 'userC', 'userA', 'userB', 'userC'],timestamp = [100, 200, 150, 250, 200, 300, 250, 350, 450],website = ['pageX', 'pageY', 'pageX', 'pageY', 'pageZ', 'pageX', 'pageZ', 'pageY', 'pageZ']) == ('pageX', 'pageY', 'pageY'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy'],timestamp = [1, 3, 5, 7, 9, 11],website = ['home', 'about', 'career', 'home', 'about', 'career']) == ('about', 'about', 'career')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy'],timestamp = [1, 3, 5, 7, 9, 11],website = ['home', 'about', 'career', 'home', 'about', 'career']) == ('about', 'about', 'career'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['frank', 'frank', 'frank', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['sports', 'travel', 'sports', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel']) == ('sports', 'travel', 'sports')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['frank', 'frank', 'frank', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['sports', 'travel', 'sports', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel']) == ('sports', 'travel', 'sports'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5'],timestamp = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],website = ['w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5']) == ('w1', 'w1', 'w1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5'],timestamp = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],website = ['w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5']) == ('w1', 'w1', 'w1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home']) == ('home', 'career', 'home')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home']) == ('home', 'career', 'home'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'home', 'about', 'about', 'about', 'career', 'career', 'career', 'home', 'about', 'career']) == ('about', 'career', 'career')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'home', 'about', 'about', 'about', 'career', 'career', 'career', 'home', 'about', 'career']) == ('about', 'career', 'career'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['alice', 'alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w2', 'w3')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['alice', 'alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w2', 'w3'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog']) == ('blog', 'blog', 'blog')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog']) == ('blog', 'blog', 'blog'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1'): {e}')
    
    total += 1
    try:
        result = candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],website = ['page1', 'page2', 'page3', 'page4', 'page1', 'page3', 'page2', 'page4', 'page1', 'page2', 'page3', 'page4', 'page1', 'page2', 'page3', 'page4']) == ('page1', 'page2', 'page4')
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],website = ['page1', 'page2', 'page3', 'page4', 'page1', 'page3', 'page2', 'page4', 'page1', 'page2', 'page3', 'page4', 'page1', 'page2', 'page3', 'page4']) == ('page1', 'page2', 'page4'): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(username = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'a', 'a')
    assert candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'x')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'c', 'a', 'b', 'c']) == ('a', 'b', 'c')
    assert candidate(username = ['joe', 'joe', 'joe', 'james', 'james', 'james', 'james', 'mary', 'mary', 'mary'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'z', 'y', 'x']) == ('x', 'z', 'y')
    assert candidate(username = ['mike', 'mike', 'mike'],timestamp = [3, 1, 2],website = ['a', 'b', 'c']) == ('b', 'c', 'a')
    assert candidate(username = ['u1', 'u2', 'u2', 'u2', 'u3', 'u3'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('y', 'z', 'x')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob'],timestamp = [1, 2, 3, 4, 5, 6],website = ['x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'y', 'z')
    assert candidate(username = ['ua', 'ua', 'ua', 'ub', 'ub', 'ub'],timestamp = [1, 2, 3, 4, 5, 6],website = ['a', 'b', 'a', 'a', 'b', 'c']) == ('a', 'b', 'a')
    assert candidate(username = ['peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter', 'peter'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a')
    assert candidate(username = ['person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5', 'person1', 'person2', 'person3', 'person4', 'person5'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web1', 'web1', 'web1')
    assert candidate(username = ['user1', 'user2', 'user1', 'user3', 'user2', 'user1', 'user3', 'user2', 'user3', 'user1'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],website = ['site1', 'site1', 'site2', 'site1', 'site2', 'site3', 'site2', 'site3', 'site3', 'site1']) == ('site1', 'site2', 'site3')
    assert candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r', 'p', 'q', 'r']) == ('p', 'p', 'p')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34],website = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']) == ('a', 'a', 'a')
    assert candidate(username = ['xavier', 'xavier', 'xavier', 'xavier', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'yvonne', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary', 'zachary'],timestamp = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3')
    assert candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1')
    assert candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 3, 5, 7, 2, 4, 6, 8, 9, 11, 13, 15],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web5']) == ('web2', 'web3', 'web1')
    assert candidate(username = ['userA', 'userA', 'userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],website = ['web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2', 'web3', 'web1', 'web2']) == ('web1', 'web1', 'web2')
    assert candidate(username = ['userX', 'userX', 'userX', 'userX', 'userY', 'userY', 'userY', 'userY', 'userZ', 'userZ', 'userZ', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ', 'siteX', 'siteY', 'siteZ']) == ('siteX', 'siteY', 'siteZ')
    assert candidate(username = ['alice', 'bob', 'alice', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice'],timestamp = [5, 1, 3, 2, 4, 6, 7, 8, 9, 10, 11, 12],website = ['site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4']) == ('site1', 'site1', 'site3')
    assert candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8],website = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y']) == ('x', 'x', 'x')
    assert candidate(username = ['anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna', 'anna'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['game', 'movie', 'game', 'music', 'game', 'movie', 'music', 'game', 'movie', 'game', 'movie']) == ('game', 'game', 'game')
    assert candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user5', 'user5', 'user5'],timestamp = [5, 2, 8, 6, 1, 4, 3, 7, 9, 11, 13, 10, 14, 12, 15],website = ['siteA', 'siteB', 'siteC', 'siteB', 'siteD', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteD', 'siteE', 'siteF', 'siteA', 'siteG']) == ('siteA', 'siteB', 'siteC')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'about', 'career', 'career', 'home', 'home', 'about', 'about', 'career', 'career']) == ('about', 'about', 'career')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'charlie', 'alice', 'bob', 'charlie', 'bob', 'alice'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['x', 'y', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']) == ('x', 'x', 'y')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [10, 20, 30, 15, 25, 35, 5, 15, 25],website = ['page1', 'page2', 'page3', 'page1', 'page2', 'page3', 'page1', 'page2', 'page3']) == ('page1', 'page2', 'page3')
    assert candidate(username = ['x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4', 'x1', 'x2', 'x3', 'x4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4', 'web1', 'web2', 'web3', 'web4']) == ('web1', 'web1', 'web1')
    assert candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4', 'user4'],timestamp = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB']) == ('siteA', 'siteB', 'siteC')
    assert candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC')
    assert candidate(username = ['dave', 'dave', 'dave', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve', 'eve'],timestamp = [1, 5, 10, 2, 3, 4, 6, 7, 8, 9, 11],website = ['news', 'shop', 'news', 'news', 'shop', 'news', 'shop', 'news', 'shop', 'news', 'news']) == ('news', 'shop', 'news')
    assert candidate(username = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1')
    assert candidate(username = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three']) == ('one', 'one', 'one')
    assert candidate(username = ['user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2', 'user1', 'user2'],timestamp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],website = ['x', 'x', 'y', 'y', 'z', 'z', 'x', 'x', 'y', 'y', 'z', 'z']) == ('x', 'x', 'y')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']) == ('a', 'b', 'c')
    assert candidate(username = ['person1', 'person1', 'person1', 'person2', 'person2', 'person2', 'person3', 'person3', 'person3', 'person4', 'person4', 'person4'],timestamp = [10, 20, 30, 15, 25, 35, 40, 50, 60, 45, 55, 65],website = ['store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout', 'store', 'cart', 'checkout']) == ('store', 'cart', 'checkout')
    assert candidate(username = ['userX', 'userY', 'userZ', 'userX', 'userY', 'userZ', 'userX', 'userY', 'userZ'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma', 'alpha', 'beta', 'gamma']) == ('alpha', 'alpha', 'alpha')
    assert candidate(username = ['visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor', 'visitor'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],website = ['home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore', 'home', 'explore']) == ('explore', 'explore', 'explore')
    assert candidate(username = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3],website = ['s', 't', 'u', 's', 't', 'u', 's', 't', 'u']) == ('s', 's', 's')
    assert candidate(username = ['user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3', 'user1', 'user2', 'user3'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteA', 'siteA')
    assert candidate(username = ['ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan', 'ivan'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech', 'fun', 'tech']) == ('fun', 'fun', 'fun')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie', 'dave', 'dave', 'dave'],timestamp = [10, 15, 12, 20, 22, 21, 30, 25, 27, 35, 33, 34],website = ['site1', 'site2', 'site3', 'site2', 'site3', 'site4', 'site1', 'site2', 'site3', 'site4', 'site5', 'site6']) == ('site1', 'site3', 'site2')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']) == ('a', 'a', 'a')
    assert candidate(username = ['userA', 'userA', 'userA', 'userA', 'userB', 'userB', 'userB', 'userB', 'userC', 'userC', 'userC', 'userC'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'about', 'career', 'home', 'home', 'about', 'career', 'home', 'home', 'about', 'career']) == ('home', 'about', 'career')
    assert candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben', 'ben'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career', 'home', 'about', 'career', 'home', 'about']) == ('about', 'career', 'home')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site1', 'site3', 'site1', 'site2', 'site1', 'site3']) == ('site1', 'site2', 'site3')
    assert candidate(username = ['alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie', 'alice', 'bob', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['a', 'b', 'c', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) == ('a', 'a', 'd')
    assert candidate(username = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'charlie', 'charlie', 'charlie'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site2', 'site3')
    assert candidate(username = ['u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u1', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2', 'u2'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],website = ['w', 'x', 'y', 'z', 'w', 'x', 'y', 'w', 'x', 'y', 'z', 'w', 'x', 'y']) == ('w', 'w', 'x')
    assert candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3'],timestamp = [10, 20, 30, 11, 21, 31, 12, 22, 32],website = ['siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC', 'siteA', 'siteB', 'siteC']) == ('siteA', 'siteB', 'siteC')
    assert candidate(username = ['u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4', 'u1', 'u2', 'u1', 'u3', 'u4'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1', 'site2', 'site1']) == ('site1', 'site2', 'site1')
    assert candidate(username = ['userA', 'userA', 'userB', 'userB', 'userC', 'userC', 'userA', 'userB', 'userC'],timestamp = [100, 200, 150, 250, 200, 300, 250, 350, 450],website = ['pageX', 'pageY', 'pageX', 'pageY', 'pageZ', 'pageX', 'pageZ', 'pageY', 'pageZ']) == ('pageX', 'pageY', 'pageY')
    assert candidate(username = ['amy', 'amy', 'amy', 'amy', 'amy', 'amy'],timestamp = [1, 3, 5, 7, 9, 11],website = ['home', 'about', 'career', 'home', 'about', 'career']) == ('about', 'about', 'career')
    assert candidate(username = ['frank', 'frank', 'frank', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace', 'grace'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],website = ['sports', 'travel', 'sports', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel', 'sports', 'travel']) == ('sports', 'travel', 'sports')
    assert candidate(username = ['userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC', 'userA', 'userB', 'userC'],timestamp = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w1', 'w1')
    assert candidate(username = ['u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5', 'u1', 'u2', 'u3', 'u4', 'u5'],timestamp = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],website = ['w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5', 'w1', 'w2', 'w3', 'w4', 'w5']) == ('w1', 'w1', 'w1')
    assert candidate(username = ['user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user3', 'user3'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home', 'career', 'home']) == ('home', 'career', 'home')
    assert candidate(username = ['alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob', 'alice', 'bob'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],website = ['home', 'home', 'home', 'about', 'about', 'about', 'career', 'career', 'career', 'home', 'about', 'career']) == ('about', 'career', 'career')
    assert candidate(username = ['alice', 'alice', 'alice', 'alice', 'bob', 'bob', 'bob', 'bob', 'bob', 'carol', 'carol', 'carol', 'carol', 'carol', 'carol'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],website = ['w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3', 'w1', 'w2', 'w3']) == ('w1', 'w2', 'w3')
    assert candidate(username = ['hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank', 'hank'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],website = ['blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog', 'store', 'blog']) == ('blog', 'blog', 'blog')
    assert candidate(username = ['user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user', 'user'],timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],website = ['site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3', 'site1', 'site2', 'site3']) == ('site1', 'site1', 'site1')
    assert candidate(username = ['user1', 'user1', 'user1', 'user1', 'user2', 'user2', 'user2', 'user2', 'user3', 'user3', 'user3', 'user3', 'user4', 'user4', 'user4', 'user4'],timestamp = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],website = ['page1', 'page2', 'page3', 'page4', 'page1', 'page3', 'page2', 'page4', 'page1', 'page2', 'page3', 'page4', 'page1', 'page2', 'page3', 'page4']) == ('page1', 'page2', 'page4')


