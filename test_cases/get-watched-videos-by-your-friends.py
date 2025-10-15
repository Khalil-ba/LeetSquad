def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action', 'Comedy'], ['Action'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['Action', 'Comedy', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action', 'Comedy'], ['Action'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['Action', 'Comedy', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['Z', 'X'], ['X', 'Y', 'Z']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['Z', 'X', 'Y']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['Z', 'X'], ['X', 'Y', 'Z']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['Z', 'X', 'Y']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['X', 'Y'], ['Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['X', 'Y'], ['Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 1) == ['B', 'C']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 1) == ['B', 'C']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['M', 'N'], ['N'], ['M', 'N'], ['O']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 1) == ['M', 'N', 'O']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['M', 'N'], ['N'], ['M', 'N'], ['O']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 1) == ['M', 'N', 'O']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie3'], ['Movie2', 'Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie3'], ['Movie2', 'Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie3']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie2', 'Movie3'], ['Movie3', 'Movie4'], ['Movie4', 'Movie5']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2', 'Movie3']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie2', 'Movie3'], ['Movie3', 'Movie4'], ['Movie4', 'Movie5']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2', 'Movie3']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['P', 'Q'], ['R'], ['P', 'R'], ['S']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['P', 'R']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['P', 'Q'], ['R'], ['P', 'R'], ['S']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['P', 'R']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Movie1'], ['Movie2'], ['Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Movie1'], ['Movie2'], ['Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 2) == ['D']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 2) == ['D']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Fitness', 'Yoga'], ['Yoga', 'Pilates'], ['Pilates', 'Meditation'], ['Meditation', 'TaiChi'], ['TaiChi', 'Fitness'], ['Fitness', 'Yoga']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 0,level = 3) == ['Meditation', 'TaiChi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Fitness', 'Yoga'], ['Yoga', 'Pilates'], ['Pilates', 'Meditation'], ['Meditation', 'TaiChi'], ['TaiChi', 'Fitness'], ['Fitness', 'Yoga']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 0,level = 3) == ['Meditation', 'TaiChi']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]],id = 2,level = 2) == ['Reality', 'TalkShow']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]],id = 2,level = 2) == ['Reality', 'TalkShow']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Romance', 'Horror'], ['Romance', 'Drama'], ['Horror', 'Drama'], ['Romance'], ['Horror', 'Drama', 'Romance']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 2,level = 1) == ['Horror', 'Romance']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Romance', 'Horror'], ['Romance', 'Drama'], ['Horror', 'Drama'], ['Romance'], ['Horror', 'Drama', 'Romance']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 2,level = 1) == ['Horror', 'Romance']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Comedy', 'Horror'], ['Comedy', 'Drama'], ['Drama', 'Thriller']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 4, 5], [0, 4, 5], [1, 2, 3, 5], [2, 3, 4]],id = 3,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Comedy', 'Horror'], ['Comedy', 'Drama'], ['Drama', 'Thriller']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 4, 5], [0, 4, 5], [1, 2, 3, 5], [2, 3, 4]],id = 3,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Romance'], ['Romance', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Romance', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Romance'], ['Romance', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Romance', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action', 'Adventure'], ['Adventure', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Action'], ['Action', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Action']],friends = [[1, 3, 5, 7], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8]],id = 4,level = 2) == ['Action', 'Drama', 'Adventure', 'Horror', 'SciFi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action', 'Adventure'], ['Adventure', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Action'], ['Action', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Action']],friends = [[1, 3, 5, 7], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8]],id = 4,level = 2) == ['Action', 'Drama', 'Adventure', 'Horror', 'SciFi']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action'], ['Action', 'Adventure'], ['Action', 'Adventure', 'Comedy'], ['Action', 'Adventure', 'Comedy', 'Drama'], ['Action', 'Adventure', 'Comedy', 'Drama', 'Thriller']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 3,level = 2) == ['Action']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action'], ['Action', 'Adventure'], ['Action', 'Adventure', 'Comedy'], ['Action', 'Adventure', 'Comedy', 'Drama'], ['Action', 'Adventure', 'Comedy', 'Drama', 'Thriller']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 3,level = 2) == ['Action']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Horror', 'Thriller'], ['Horror'], ['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Thriller', 'Comedy']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2], [3]],id = 0,level = 2) == ['Thriller', 'Horror']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Horror', 'Thriller'], ['Horror'], ['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Thriller', 'Comedy']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2], [3]],id = 0,level = 2) == ['Thriller', 'Horror']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Sci-Fi', 'Animation'], ['Animation', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Sci-Fi'], ['Sci-Fi', 'Adventure']],friends = [[1, 4], [0, 2, 5], [1, 3], [2], [0], [1]],id = 1,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Sci-Fi', 'Animation'], ['Animation', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Sci-Fi'], ['Sci-Fi', 'Adventure']],friends = [[1, 4], [0, 2, 5], [1, 3], [2], [0], [1]],id = 1,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'SciFi']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Comedy', 'SciFi', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'SciFi']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Comedy', 'SciFi', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Romance', 'Drama'], ['Drama', 'Thriller'], ['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Romance'], ['Romance', 'Thriller']],friends = [[1, 2], [0, 3, 5], [0, 4], [1, 4], [2, 3], [1]],id = 3,level = 1) == ['Comedy', 'Drama', 'Romance', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Romance', 'Drama'], ['Drama', 'Thriller'], ['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Romance'], ['Romance', 'Thriller']],friends = [[1, 2], [0, 3, 5], [0, 4], [1, 4], [2, 3], [1]],id = 3,level = 1) == ['Comedy', 'Drama', 'Romance', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Anime', 'Cartoon'], ['Drama', 'Horror'], ['Cartoon'], ['Sci-Fi', 'Drama'], ['Horror', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Anime', 'Drama', 'Horror', 'Sci-Fi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Anime', 'Cartoon'], ['Drama', 'Horror'], ['Cartoon'], ['Sci-Fi', 'Drama'], ['Horror', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Anime', 'Drama', 'Horror', 'Sci-Fi']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Drama', 'Romance'], ['Romance', 'Adventure'], ['Adventure', 'Thriller'], ['Thriller', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 3) == ['Drama', 'Romance']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Drama', 'Romance'], ['Romance', 'Adventure'], ['Adventure', 'Thriller'], ['Thriller', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 3) == ['Drama', 'Romance']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Sci-Fi'], ['Drama'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 3, 4], [0, 3, 4], [0, 1, 2, 4], [1, 2, 3]],id = 0,level = 2) == ['Comedy', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Sci-Fi'], ['Drama'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 3, 4], [0, 3, 4], [0, 1, 2, 4], [1, 2, 3]],id = 0,level = 2) == ['Comedy', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Sci-Fi', 'Horror'], ['Romance'], ['Sci-Fi', 'Drama'], ['Romance', 'Sci-Fi'], ['Horror', 'Drama'], ['Comedy'], ['Drama'], ['Romance']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 6], [0, 2, 4, 7], [1, 3, 5, 7], [1, 4, 6], [2, 5], [3, 4, 7]],id = 1,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Sci-Fi', 'Horror'], ['Romance'], ['Sci-Fi', 'Drama'], ['Romance', 'Sci-Fi'], ['Horror', 'Drama'], ['Comedy'], ['Drama'], ['Romance']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 6], [0, 2, 4, 7], [1, 3, 5, 7], [1, 4, 6], [2, 5], [3, 4, 7]],id = 1,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['MusicVideo', 'Pop'], ['Pop', 'Rock'], ['Rock', 'HipHop'], ['HipHop', 'Jazz'], ['Jazz', 'Pop'], ['Pop', 'MusicVideo']],friends = [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3, 5], [4]],id = 2,level = 3) == ['MusicVideo', 'Pop']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['MusicVideo', 'Pop'], ['Pop', 'Rock'], ['Rock', 'HipHop'], ['HipHop', 'Jazz'], ['Jazz', 'Pop'], ['Pop', 'MusicVideo']],friends = [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3, 5], [4]],id = 2,level = 3) == ['MusicVideo', 'Pop']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama'], ['SciFi', 'Adventure', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [2, 5], [4]],id = 2,level = 2) == ['Action', 'Adventure']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama'], ['SciFi', 'Adventure', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [2, 5], [4]],id = 2,level = 2) == ['Action', 'Adventure']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror'], ['Horror', 'Thriller'], ['Action', 'Drama'], ['Action'], ['Drama', 'Thriller'], ['Drama'], ['Thriller', 'Horror'], ['Drama', 'Horror'], ['Drama', 'Action']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8], [1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 0, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9], [1, 2, 3, 4, 5, 0, 7, 8, 9], [1, 2, 3, 4, 5, 6, 0, 8, 9], [1, 2, 3, 4, 5, 6, 7, 0, 9], [1, 2, 3, 4, 5, 6, 7, 8, 0]],id = 4,level = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror'], ['Horror', 'Thriller'], ['Action', 'Drama'], ['Action'], ['Drama', 'Thriller'], ['Drama'], ['Thriller', 'Horror'], ['Drama', 'Horror'], ['Drama', 'Action']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8], [1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 0, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9], [1, 2, 3, 4, 5, 0, 7, 8, 9], [1, 2, 3, 4, 5, 6, 0, 8, 9], [1, 2, 3, 4, 5, 6, 7, 0, 9], [1, 2, 3, 4, 5, 6, 7, 8, 0]],id = 4,level = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation', 'Horror'], ['Horror', 'Sci-Fi'], ['Sci-Fi', 'Documentary'], ['Animation', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [1, 5], [3, 4]],id = 3,level = 2) == ['Sci-Fi', 'Documentary']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation', 'Horror'], ['Horror', 'Sci-Fi'], ['Sci-Fi', 'Documentary'], ['Animation', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [1, 5], [3, 4]],id = 3,level = 2) == ['Sci-Fi', 'Documentary']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Fantasy', 'Comedy'], ['Fantasy'], ['Fantasy', 'Comedy'], ['Drama'], ['Fantasy', 'Drama'], ['Comedy', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [2], [3]],id = 3,level = 2) == ['Comedy', 'Drama', 'Fantasy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Fantasy', 'Comedy'], ['Fantasy'], ['Fantasy', 'Comedy'], ['Drama'], ['Fantasy', 'Drama'], ['Comedy', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [2], [3]],id = 3,level = 2) == ['Comedy', 'Drama', 'Fantasy']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 1,level = 2) == ['Comedy', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 1,level = 2) == ['Comedy', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Drama'], ['Drama', 'Drama'], ['Thriller'], ['Thriller', 'Thriller', 'Drama'], ['Thriller', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 1,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Drama'], ['Drama', 'Drama'], ['Thriller'], ['Thriller', 'Thriller', 'Drama'], ['Thriller', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 1,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Anime', 'Cartoon'], ['Cartoon', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Comedy'], ['Comedy', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 1,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Anime', 'Cartoon'], ['Cartoon', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Comedy'], ['Comedy', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 1,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Sci-Fi', 'Adventure'], ['Action', 'Drama'], ['Drama', 'Sci-Fi'], ['Adventure', 'Comedy'], ['Comedy', 'Action']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 4]],id = 0,level = 2) == ['Action', 'Adventure', 'Comedy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Sci-Fi', 'Adventure'], ['Action', 'Drama'], ['Drama', 'Sci-Fi'], ['Adventure', 'Comedy'], ['Comedy', 'Action']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 4]],id = 0,level = 2) == ['Action', 'Adventure', 'Comedy']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['TalkShow', 'Documentary'], ['Documentary', 'RealityShow'], ['RealityShow', 'Drama'], ['Drama', 'TalkShow'], ['TalkShow', 'RealityShow']],friends = [[1, 2], [0, 3], [0, 3], [1, 4], [3, 5], [1, 5]],id = 0,level = 2) == ['Drama', 'RealityShow']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['TalkShow', 'Documentary'], ['Documentary', 'RealityShow'], ['RealityShow', 'Drama'], ['Drama', 'TalkShow'], ['TalkShow', 'RealityShow']],friends = [[1, 2], [0, 3], [0, 3], [1, 4], [3, 5], [1, 5]],id = 0,level = 2) == ['Drama', 'RealityShow']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action', 'Drama'], ['Comedy', 'Romance'], ['Action', 'Comedy'], ['Romance'], ['Action', 'Romance'], ['Drama', 'Comedy']],friends = [[1, 2, 3], [0, 4], [0, 5], [0, 5], [1, 5], [2, 3, 4]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Romance']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action', 'Drama'], ['Comedy', 'Romance'], ['Action', 'Comedy'], ['Romance'], ['Action', 'Romance'], ['Drama', 'Comedy']],friends = [[1, 2, 3], [0, 4], [0, 5], [0, 5], [1, 5], [2, 3, 4]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Romance']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Animation', 'Comedy'], ['Comedy', 'Adventure'], ['Adventure', 'Animation'], ['Animation', 'Comedy'], ['Adventure'], ['Adventure', 'Comedy'], ['Comedy'], ['Animation', 'Adventure'], ['Comedy', 'Animation'], ['Animation', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 0, 9], [0, 1, 2, 3, 4, 5, 6, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8]],id = 3,level = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Animation', 'Comedy'], ['Comedy', 'Adventure'], ['Adventure', 'Animation'], ['Animation', 'Comedy'], ['Adventure'], ['Adventure', 'Comedy'], ['Comedy'], ['Animation', 'Adventure'], ['Comedy', 'Animation'], ['Animation', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 0, 9], [0, 1, 2, 3, 4, 5, 6, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8]],id = 3,level = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary'], ['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 0,level = 3) == ['Documentary', 'War']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary'], ['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 0,level = 3) == ['Documentary', 'War']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Horror'], ['Comedy', 'Action'], ['Drama', 'Comedy'], ['Horror', 'Thriller'], ['Action', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 2]],id = 0,level = 2) == ['Action', 'Drama', 'Horror', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Horror'], ['Comedy', 'Action'], ['Drama', 'Comedy'], ['Horror', 'Thriller'], ['Action', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 2]],id = 0,level = 2) == ['Action', 'Drama', 'Horror', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Comedy', 'Drama', 'Thriller'], ['Drama', 'Thriller'], ['Drama', 'Thriller', 'Horror'], ['Horror', 'Drama', 'Comedy'], ['Horror', 'Drama', 'Comedy', 'Thriller']],friends = [[1, 3, 4], [0, 2, 5], [1, 4], [0, 5, 7], [0, 2, 6], [1, 3, 6], [4, 7], [3, 6]],id = 5,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Comedy', 'Drama', 'Thriller'], ['Drama', 'Thriller'], ['Drama', 'Thriller', 'Horror'], ['Horror', 'Drama', 'Comedy'], ['Horror', 'Drama', 'Comedy', 'Thriller']],friends = [[1, 3, 4], [0, 2, 5], [1, 4], [0, 5, 7], [0, 2, 6], [1, 3, 6], [4, 7], [3, 6]],id = 5,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 4,level = 2) == ['Adventure', 'Comedy', 'Action']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 4,level = 2) == ['Adventure', 'Comedy', 'Action']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Drama'], ['Adventure', 'Drama'], ['Drama', 'Action'], ['Adventure', 'Drama'], ['Action', 'Adventure'], ['Adventure', 'Action'], ['Drama', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Drama']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 7], [5, 8], [6, 9], [7, 8]],id = 4,level = 4) == ['Action', 'Adventure', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Drama'], ['Adventure', 'Drama'], ['Drama', 'Action'], ['Adventure', 'Drama'], ['Action', 'Adventure'], ['Adventure', 'Action'], ['Drama', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Drama']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 7], [5, 8], [6, 9], [7, 8]],id = 4,level = 4) == ['Action', 'Adventure', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller', 'Romance'], ['Action'], ['Romance', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller'], ['Action', 'Romance']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 4]],id = 1,level = 3) == ['Action', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller', 'Romance'], ['Action'], ['Romance', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller'], ['Action', 'Romance']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 4]],id = 1,level = 3) == ['Action', 'Thriller']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['RealityShow'], ['TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0], [0], [0], [0], [0], [0], [0], [0], [0]],id = 0,level = 1) == ['RealityShow', 'TalkShow']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['RealityShow'], ['TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0], [0], [0], [0], [0], [0], [0], [0], [0]],id = 0,level = 1) == ['RealityShow', 'TalkShow']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Animation', 'ShortFilm'], ['ShortFilm', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'LiveAction'], ['LiveAction', 'ShortFilm'], ['ShortFilm', 'Documentary']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 2) == ['Documentary', 'ShortFilm']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Animation', 'ShortFilm'], ['ShortFilm', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'LiveAction'], ['LiveAction', 'ShortFilm'], ['ShortFilm', 'Documentary']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 2) == ['Documentary', 'ShortFilm']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Animation', 'Comedy'], ['Animation'], ['Animation', 'Comedy'], ['Drama'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3, 4, 5], [1, 2, 5], [2], [2, 3]],id = 2,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Animation', 'Comedy'], ['Animation'], ['Animation', 'Comedy'], ['Drama'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3, 4, 5], [1, 2, 5], [2], [2, 3]],id = 2,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Music', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'Music'], ['Music', 'Animation'], ['Animation', 'Music']],friends = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]],id = 1,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Music', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'Music'], ['Music', 'Animation'], ['Animation', 'Music']],friends = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]],id = 1,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action'], ['Action', 'Comedy'], ['Comedy'], ['Drama', 'Action'], ['Drama'], ['Action', 'Drama'], ['Action', 'Comedy'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6]],id = 4,level = 2) == ['Action', 'Comedy', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action'], ['Action', 'Comedy'], ['Comedy'], ['Drama', 'Action'], ['Drama'], ['Action', 'Drama'], ['Action', 'Comedy'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6]],id = 4,level = 2) == ['Action', 'Comedy', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Documentary'], ['Comedy'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1, 10], [1], [2], [2], [3], [3], [4]],id = 4,level = 2) == ['Documentary', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Documentary'], ['Comedy'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1, 10], [1], [2], [2], [3], [3], [4]],id = 4,level = 2) == ['Documentary', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action', 'Horror'], ['Horror', 'Sci-Fi'], ['Action', 'Sci-Fi'], ['Sci-Fi', 'Adventure'], ['Adventure', 'Action'], ['Adventure', 'Horror']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 0,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action', 'Horror'], ['Horror', 'Sci-Fi'], ['Action', 'Sci-Fi'], ['Sci-Fi', 'Adventure'], ['Adventure', 'Action'], ['Adventure', 'Horror']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 0,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['SciFi', 'Adventure'], ['Adventure', 'Fantasy'], ['Fantasy', 'Mystery'], ['Mystery', 'Horror'], ['Horror', 'SciFi']],friends = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]],id = 2,level = 2) == ['Adventure', 'Horror', 'SciFi']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['SciFi', 'Adventure'], ['Adventure', 'Fantasy'], ['Fantasy', 'Mystery'], ['Mystery', 'Horror'], ['Horror', 'SciFi']],friends = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]],id = 2,level = 2) == ['Adventure', 'Horror', 'SciFi']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Animation'], ['Action', 'Adventure'], ['Animation', 'Comedy'], ['Action', 'Comedy'], ['Adventure', 'Comedy'], ['Animation', 'Action']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 5], [0, 2, 4], [1, 3, 5], [1, 2, 4]],id = 1,level = 2) == ['Action', 'Animation', 'Comedy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Animation'], ['Action', 'Adventure'], ['Animation', 'Comedy'], ['Action', 'Comedy'], ['Adventure', 'Comedy'], ['Animation', 'Action']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 5], [0, 2, 4], [1, 3, 5], [1, 2, 4]],id = 1,level = 2) == ['Action', 'Animation', 'Comedy']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2]],id = 0,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2]],id = 0,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Animation', 'Action'], ['Adventure', 'Comedy'], ['Action', 'Comedy'], ['Animation', 'Adventure'], ['Drama', 'Adventure']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1, 4]],id = 2,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Animation', 'Action'], ['Adventure', 'Comedy'], ['Action', 'Comedy'], ['Animation', 'Adventure'], ['Drama', 'Adventure']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1, 4]],id = 2,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5], [6, 7], [7, 8]],id = 3,level = 3) == ['Documentary', 'Reality', 'TalkShow']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5], [6, 7], [7, 8]],id = 3,level = 3) == ['Documentary', 'Reality', 'TalkShow']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Comedy'], ['Action'], ['Romance'], ['Action', 'Romance'], ['Comedy', 'Romance'], ['Comedy', 'Action']],friends = [[1, 2, 3, 4], [0, 4, 5], [0, 5, 3], [0, 2, 5], [0, 1, 3], [1, 2, 4]],id = 2,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Comedy'], ['Action'], ['Romance'], ['Action', 'Romance'], ['Comedy', 'Romance'], ['Comedy', 'Action']],friends = [[1, 2, 3, 4], [0, 4, 5], [0, 5, 3], [0, 2, 5], [0, 1, 3], [1, 2, 4]],id = 2,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Thriller'], ['Horror'], ['Sci-Fi'], ['Thriller', 'Horror'], ['Sci-Fi', 'Thriller'], ['Horror', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 5], [1, 5], [1, 5], [2, 3, 4]],id = 2,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Thriller'], ['Horror'], ['Sci-Fi'], ['Thriller', 'Horror'], ['Sci-Fi', 'Thriller'], ['Horror', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 5], [1, 5], [1, 5], [2, 3, 4]],id = 2,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Romantic', 'Comedy'], ['Action', 'Adventure'], ['Drama', 'Thriller'], ['Comedy', 'Romantic'], ['Adventure', 'Action'], ['Thriller', 'Drama'], ['Romantic', 'Drama'], ['Action', 'Comedy'], ['Adventure', 'Thriller']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 4,level = 2) == ['Action', 'Adventure', 'Romantic', 'Thriller', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Romantic', 'Comedy'], ['Action', 'Adventure'], ['Drama', 'Thriller'], ['Comedy', 'Romantic'], ['Adventure', 'Action'], ['Thriller', 'Drama'], ['Romantic', 'Drama'], ['Action', 'Comedy'], ['Adventure', 'Thriller']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 4,level = 2) == ['Action', 'Adventure', 'Romantic', 'Thriller', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation'], ['Documentary', 'Animation', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Comedy']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 3, 5], [0, 2, 4, 5, 6], [1, 3, 5], [2, 3, 4, 6], [3, 5]],id = 1,level = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation'], ['Documentary', 'Animation', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Comedy']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 3, 5], [0, 2, 4, 5, 6], [1, 3, 5], [2, 3, 4, 6], [3, 5]],id = 1,level = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Horror'], ['Horror', 'Thriller'], ['Thriller'], ['Horror', 'Thriller', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Action', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'Horror']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6], [3, 7]],id = 5,level = 3) == ['Action', 'Comedy']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Horror'], ['Horror', 'Thriller'], ['Thriller'], ['Horror', 'Thriller', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Action', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'Horror']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6], [3, 7]],id = 5,level = 3) == ['Action', 'Comedy']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Horror', 'SciFi'], ['Adventure', 'SciFi'], ['Horror', 'Comedy'], ['Comedy', 'SciFi'], ['Adventure', 'Comedy']],friends = [[1, 3, 4], [0, 2], [1, 3], [0, 2, 4], [0, 3]],id = 0,level = 2) == ['Comedy', 'Horror']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Horror', 'SciFi'], ['Adventure', 'SciFi'], ['Horror', 'Comedy'], ['Comedy', 'SciFi'], ['Adventure', 'Comedy']],friends = [[1, 3, 4], [0, 2], [1, 3], [0, 2, 4], [0, 3]],id = 0,level = 2) == ['Comedy', 'Horror']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Action'], ['Action'], ['Adventure', 'Action'], ['Adventure'], ['Action', 'Adventure'], ['Action'], ['Adventure', 'Action'], ['Action', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7], [0, 1, 3, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6]],id = 6,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Action'], ['Action'], ['Adventure', 'Action'], ['Adventure'], ['Action', 'Adventure'], ['Action'], ['Adventure', 'Action'], ['Action', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7], [0, 1, 3, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6]],id = 6,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 0,level = 2) == ['Action', 'Adventure', 'Drama']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 0,level = 2) == ['Action', 'Adventure', 'Drama']: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Romance'], ['Romance', 'Comedy'], ['Romance'], ['Comedy'], ['Romance', 'Action'], ['Action', 'Drama'], ['Drama', 'Action'], ['Drama'], ['Comedy', 'Romance'], ['Romance', 'Drama']],friends = [[1, 2, 3, 4], [0, 5, 6, 7, 8, 9], [0, 9, 8], [0, 5, 7], [0, 5, 8, 9], [1, 3, 4, 6, 9], [1, 5, 9], [1, 3, 9], [2, 4, 9], [2, 3, 4, 5, 6, 7]],id = 5,level = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Romance'], ['Romance', 'Comedy'], ['Romance'], ['Comedy'], ['Romance', 'Action'], ['Action', 'Drama'], ['Drama', 'Action'], ['Drama'], ['Comedy', 'Romance'], ['Romance', 'Drama']],friends = [[1, 2, 3, 4], [0, 5, 6, 7, 8, 9], [0, 9, 8], [0, 5, 7], [0, 5, 8, 9], [1, 3, 4, 6, 9], [1, 5, 9], [1, 3, 9], [2, 4, 9], [2, 3, 4, 5, 6, 7]],id = 5,level = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(watchedVideos = [['Action', 'Adventure'], ['Sci-Fi', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Thriller'], ['Action', 'Sci-Fi'], ['Adventure', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Action', 'Thriller'], ['Sci-Fi', 'Adventure']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1], [1, 2], [2], [2], [3], [3, 4]],id = 2,level = 2) == ['Action', 'Sci-Fi', 'Thriller']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(watchedVideos = [['Action', 'Adventure'], ['Sci-Fi', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Thriller'], ['Action', 'Sci-Fi'], ['Adventure', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Action', 'Thriller'], ['Sci-Fi', 'Adventure']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1], [1, 2], [2], [2], [3], [3, 4]],id = 2,level = 2) == ['Action', 'Sci-Fi', 'Thriller']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(watchedVideos = [['Action', 'Comedy'], ['Action'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['Action', 'Comedy', 'Drama']
    assert candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['Z', 'X'], ['X', 'Y', 'Z']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['Z', 'X', 'Y']
    assert candidate(watchedVideos = [['X', 'Y'], ['Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']
    assert candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 1) == ['B', 'C']
    assert candidate(watchedVideos = [['M', 'N'], ['N'], ['M', 'N'], ['O']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 1) == ['M', 'N', 'O']
    assert candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie3'], ['Movie2', 'Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie3']
    assert candidate(watchedVideos = [['Movie1', 'Movie2'], ['Movie2', 'Movie3'], ['Movie3', 'Movie4'], ['Movie4', 'Movie5']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2', 'Movie3']
    assert candidate(watchedVideos = [['P', 'Q'], ['R'], ['P', 'R'], ['S']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 3,level = 1) == ['P', 'R']
    assert candidate(watchedVideos = [['X', 'Y'], ['Y', 'Z'], ['X', 'Z'], ['W']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 1,level = 1) == ['W', 'X', 'Y']
    assert candidate(watchedVideos = [['Movie1'], ['Movie2'], ['Movie3'], ['Movie4']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 2,level = 2) == ['Movie2']
    assert candidate(watchedVideos = [['A', 'B'], ['C'], ['B', 'C'], ['D']],friends = [[1, 2], [0, 3], [0, 3], [1, 2]],id = 0,level = 2) == ['D']
    assert candidate(watchedVideos = [['Fitness', 'Yoga'], ['Yoga', 'Pilates'], ['Pilates', 'Meditation'], ['Meditation', 'TaiChi'], ['TaiChi', 'Fitness'], ['Fitness', 'Yoga']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 0,level = 3) == ['Meditation', 'TaiChi']
    assert candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Thriller']
    assert candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5]],id = 2,level = 2) == ['Reality', 'TalkShow']
    assert candidate(watchedVideos = [['Romance', 'Horror'], ['Romance', 'Drama'], ['Horror', 'Drama'], ['Romance'], ['Horror', 'Drama', 'Romance']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 2,level = 1) == ['Horror', 'Romance']
    assert candidate(watchedVideos = [['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Comedy', 'Horror'], ['Comedy', 'Drama'], ['Drama', 'Thriller']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 4, 5], [0, 4, 5], [1, 2, 3, 5], [2, 3, 4]],id = 3,level = 3) == []
    assert candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'Romance'], ['Romance', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Thriller']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1]],id = 0,level = 2) == ['Action', 'Comedy', 'Romance', 'Thriller']
    assert candidate(watchedVideos = [['Action', 'Adventure'], ['Adventure', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Action'], ['Action', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Action']],friends = [[1, 3, 5, 7], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [1, 3, 5, 7, 9], [2, 4, 6, 8]],id = 4,level = 2) == ['Action', 'Drama', 'Adventure', 'Horror', 'SciFi']
    assert candidate(watchedVideos = [['Action'], ['Action', 'Adventure'], ['Action', 'Adventure', 'Comedy'], ['Action', 'Adventure', 'Comedy', 'Drama'], ['Action', 'Adventure', 'Comedy', 'Drama', 'Thriller']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 3,level = 2) == ['Action']
    assert candidate(watchedVideos = [['Horror', 'Thriller'], ['Horror'], ['Thriller'], ['Horror', 'Thriller'], ['Horror'], ['Thriller', 'Comedy']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 5], [2], [3]],id = 0,level = 2) == ['Thriller', 'Horror']
    assert candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Sci-Fi', 'Animation'], ['Animation', 'Adventure'], ['Adventure', 'Drama'], ['Drama', 'Sci-Fi'], ['Sci-Fi', 'Adventure']],friends = [[1, 4], [0, 2, 5], [1, 3], [2], [0], [1]],id = 1,level = 3) == []
    assert candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror', 'SciFi'], ['SciFi', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'SciFi']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Comedy', 'SciFi', 'Thriller']
    assert candidate(watchedVideos = [['Romance', 'Drama'], ['Drama', 'Thriller'], ['Thriller', 'Horror'], ['Horror', 'Comedy'], ['Comedy', 'Romance'], ['Romance', 'Thriller']],friends = [[1, 2], [0, 3, 5], [0, 4], [1, 4], [2, 3], [1]],id = 3,level = 1) == ['Comedy', 'Drama', 'Romance', 'Thriller']
    assert candidate(watchedVideos = [['Anime', 'Cartoon'], ['Drama', 'Horror'], ['Cartoon'], ['Sci-Fi', 'Drama'], ['Horror', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 0,level = 2) == ['Anime', 'Drama', 'Horror', 'Sci-Fi']
    assert candidate(watchedVideos = [['Drama', 'Romance'], ['Romance', 'Adventure'], ['Adventure', 'Thriller'], ['Thriller', 'SciFi'], ['SciFi', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 3) == ['Drama', 'Romance']
    assert candidate(watchedVideos = [['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Sci-Fi'], ['Drama'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 3, 4], [0, 3, 4], [0, 1, 2, 4], [1, 2, 3]],id = 0,level = 2) == ['Comedy', 'Drama']
    assert candidate(watchedVideos = [['Sci-Fi', 'Horror'], ['Romance'], ['Sci-Fi', 'Drama'], ['Romance', 'Sci-Fi'], ['Horror', 'Drama'], ['Comedy'], ['Drama'], ['Romance']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 6], [0, 2, 4, 7], [1, 3, 5, 7], [1, 4, 6], [2, 5], [3, 4, 7]],id = 1,level = 3) == []
    assert candidate(watchedVideos = [['MusicVideo', 'Pop'], ['Pop', 'Rock'], ['Rock', 'HipHop'], ['HipHop', 'Jazz'], ['Jazz', 'Pop'], ['Pop', 'MusicVideo']],friends = [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3, 5], [4]],id = 2,level = 3) == ['MusicVideo', 'Pop']
    assert candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama'], ['SciFi', 'Adventure', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [2, 5], [4]],id = 2,level = 2) == ['Action', 'Adventure']
    assert candidate(watchedVideos = [['Thriller', 'Horror'], ['Horror'], ['Horror', 'Thriller'], ['Action', 'Drama'], ['Action'], ['Drama', 'Thriller'], ['Drama'], ['Thriller', 'Horror'], ['Drama', 'Horror'], ['Drama', 'Action']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8], [1, 0, 3, 4, 5, 6, 7, 8, 9], [1, 0, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9], [1, 2, 3, 4, 5, 0, 7, 8, 9], [1, 2, 3, 4, 5, 6, 0, 8, 9], [1, 2, 3, 4, 5, 6, 7, 0, 9], [1, 2, 3, 4, 5, 6, 7, 8, 0]],id = 4,level = 4) == []
    assert candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation', 'Horror'], ['Horror', 'Sci-Fi'], ['Sci-Fi', 'Documentary'], ['Animation', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [1, 5], [3, 4]],id = 3,level = 2) == ['Sci-Fi', 'Documentary']
    assert candidate(watchedVideos = [['Fantasy', 'Comedy'], ['Fantasy'], ['Fantasy', 'Comedy'], ['Drama'], ['Fantasy', 'Drama'], ['Comedy', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 5], [2], [3]],id = 3,level = 2) == ['Comedy', 'Drama', 'Fantasy']
    assert candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 1,level = 2) == ['Comedy', 'Drama']
    assert candidate(watchedVideos = [['Drama'], ['Drama', 'Drama'], ['Thriller'], ['Thriller', 'Thriller', 'Drama'], ['Thriller', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2, 4], [2, 3]],id = 1,level = 3) == []
    assert candidate(watchedVideos = [['Anime', 'Cartoon'], ['Cartoon', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Comedy'], ['Comedy', 'Anime']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 1,level = 3) == []
    assert candidate(watchedVideos = [['Sci-Fi', 'Adventure'], ['Action', 'Drama'], ['Drama', 'Sci-Fi'], ['Adventure', 'Comedy'], ['Comedy', 'Action']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 4]],id = 0,level = 2) == ['Action', 'Adventure', 'Comedy']
    assert candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['TalkShow', 'Documentary'], ['Documentary', 'RealityShow'], ['RealityShow', 'Drama'], ['Drama', 'TalkShow'], ['TalkShow', 'RealityShow']],friends = [[1, 2], [0, 3], [0, 3], [1, 4], [3, 5], [1, 5]],id = 0,level = 2) == ['Drama', 'RealityShow']
    assert candidate(watchedVideos = [['Action', 'Drama'], ['Comedy', 'Romance'], ['Action', 'Comedy'], ['Romance'], ['Action', 'Romance'], ['Drama', 'Comedy']],friends = [[1, 2, 3], [0, 4], [0, 5], [0, 5], [1, 5], [2, 3, 4]],id = 0,level = 2) == ['Action', 'Comedy', 'Drama', 'Romance']
    assert candidate(watchedVideos = [['Animation', 'Comedy'], ['Comedy', 'Adventure'], ['Adventure', 'Animation'], ['Animation', 'Comedy'], ['Adventure'], ['Adventure', 'Comedy'], ['Comedy'], ['Animation', 'Adventure'], ['Comedy', 'Animation'], ['Animation', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 0, 9], [0, 1, 2, 3, 4, 5, 6, 7, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8]],id = 3,level = 5) == []
    assert candidate(watchedVideos = [['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary'], ['Documentary', 'Biography'], ['Biography', 'Historical'], ['Historical', 'War'], ['War', 'Documentary']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 0,level = 3) == ['Documentary', 'War']
    assert candidate(watchedVideos = [['Thriller', 'Horror'], ['Comedy', 'Action'], ['Drama', 'Comedy'], ['Horror', 'Thriller'], ['Action', 'Drama']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1, 2]],id = 0,level = 2) == ['Action', 'Drama', 'Horror', 'Thriller']
    assert candidate(watchedVideos = [['Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Comedy', 'Drama', 'Thriller'], ['Drama', 'Thriller'], ['Drama', 'Thriller', 'Horror'], ['Horror', 'Drama', 'Comedy'], ['Horror', 'Drama', 'Comedy', 'Thriller']],friends = [[1, 3, 4], [0, 2, 5], [1, 4], [0, 5, 7], [0, 2, 6], [1, 3, 6], [4, 7], [3, 6]],id = 5,level = 3) == []
    assert candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Comedy'], ['Comedy', 'Horror'], ['Horror', 'Drama'], ['Drama', 'Adventure']],friends = [[1, 2], [0, 3], [0, 4], [1, 4], [2, 3]],id = 4,level = 2) == ['Adventure', 'Comedy', 'Action']
    assert candidate(watchedVideos = [['Adventure', 'Action'], ['Action', 'Drama'], ['Adventure', 'Drama'], ['Drama', 'Action'], ['Adventure', 'Drama'], ['Action', 'Adventure'], ['Adventure', 'Action'], ['Drama', 'Action'], ['Action', 'Adventure'], ['Adventure', 'Drama']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 7], [5, 8], [6, 9], [7, 8]],id = 4,level = 4) == ['Action', 'Adventure', 'Drama']
    assert candidate(watchedVideos = [['Thriller', 'Romance'], ['Action'], ['Romance', 'Drama'], ['Drama', 'Thriller'], ['Action', 'Thriller'], ['Action', 'Romance']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 4]],id = 1,level = 3) == ['Action', 'Thriller']
    assert candidate(watchedVideos = [['RealityShow', 'TalkShow'], ['RealityShow'], ['TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow'], ['RealityShow', 'TalkShow']],friends = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [0], [0], [0], [0], [0], [0], [0], [0], [0]],id = 0,level = 1) == ['RealityShow', 'TalkShow']
    assert candidate(watchedVideos = [['Animation', 'ShortFilm'], ['ShortFilm', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'LiveAction'], ['LiveAction', 'ShortFilm'], ['ShortFilm', 'Documentary']],friends = [[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [0, 4]],id = 3,level = 2) == ['Documentary', 'ShortFilm']
    assert candidate(watchedVideos = [['Animation', 'Comedy'], ['Animation'], ['Animation', 'Comedy'], ['Drama'], ['Comedy', 'Drama'], ['Drama']],friends = [[1, 2], [0, 3], [0, 3, 4, 5], [1, 2, 5], [2], [2, 3]],id = 2,level = 3) == []
    assert candidate(watchedVideos = [['Music', 'Documentary'], ['Documentary', 'Animation'], ['Animation', 'Music'], ['Music', 'Animation'], ['Animation', 'Music']],friends = [[1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3]],id = 1,level = 3) == []
    assert candidate(watchedVideos = [['Action'], ['Action', 'Comedy'], ['Comedy'], ['Drama', 'Action'], ['Drama'], ['Action', 'Drama'], ['Action', 'Comedy'], ['Comedy', 'Drama']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6]],id = 4,level = 2) == ['Action', 'Comedy', 'Drama']
    assert candidate(watchedVideos = [['Documentary'], ['Comedy'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary'], ['Drama'], ['Comedy'], ['Documentary']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1, 10], [1], [2], [2], [3], [3], [4]],id = 4,level = 2) == ['Documentary', 'Drama']
    assert candidate(watchedVideos = [['Action', 'Horror'], ['Horror', 'Sci-Fi'], ['Action', 'Sci-Fi'], ['Sci-Fi', 'Adventure'], ['Adventure', 'Action'], ['Adventure', 'Horror']],friends = [[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]],id = 0,level = 3) == []
    assert candidate(watchedVideos = [['SciFi', 'Adventure'], ['Adventure', 'Fantasy'], ['Fantasy', 'Mystery'], ['Mystery', 'Horror'], ['Horror', 'SciFi']],friends = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]],id = 2,level = 2) == ['Adventure', 'Horror', 'SciFi']
    assert candidate(watchedVideos = [['Adventure', 'Animation'], ['Action', 'Adventure'], ['Animation', 'Comedy'], ['Action', 'Comedy'], ['Adventure', 'Comedy'], ['Animation', 'Action']],friends = [[1, 2, 3], [0, 4, 5], [0, 3, 5], [0, 2, 4], [1, 3, 5], [1, 2, 4]],id = 1,level = 2) == ['Action', 'Animation', 'Comedy']
    assert candidate(watchedVideos = [['SciFi', 'Romance'], ['Action', 'Adventure'], ['Action', 'SciFi'], ['Romance', 'Adventure'], ['SciFi', 'Drama']],friends = [[1, 2], [0, 3], [0, 3, 4], [1, 2], [2]],id = 0,level = 3) == []
    assert candidate(watchedVideos = [['Animation', 'Action'], ['Adventure', 'Comedy'], ['Action', 'Comedy'], ['Animation', 'Adventure'], ['Drama', 'Adventure']],friends = [[1, 3], [0, 2, 4], [1, 3], [0, 2], [1, 4]],id = 2,level = 3) == []
    assert candidate(watchedVideos = [['Reality', 'TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary'], ['Documentary'], ['Reality', 'TalkShow'], ['Documentary', 'Reality'], ['TalkShow'], ['Reality', 'Documentary'], ['TalkShow', 'Documentary']],friends = [[1, 2], [0, 3], [0, 4], [1, 5], [2, 6], [3, 6], [4, 5], [6, 7], [7, 8]],id = 3,level = 3) == ['Documentary', 'Reality', 'TalkShow']
    assert candidate(watchedVideos = [['Comedy'], ['Action'], ['Romance'], ['Action', 'Romance'], ['Comedy', 'Romance'], ['Comedy', 'Action']],friends = [[1, 2, 3, 4], [0, 4, 5], [0, 5, 3], [0, 2, 5], [0, 1, 3], [1, 2, 4]],id = 2,level = 3) == []
    assert candidate(watchedVideos = [['Thriller'], ['Horror'], ['Sci-Fi'], ['Thriller', 'Horror'], ['Sci-Fi', 'Thriller'], ['Horror', 'Sci-Fi']],friends = [[1, 2], [0, 3, 4], [0, 5], [1, 5], [1, 5], [2, 3, 4]],id = 2,level = 3) == []
    assert candidate(watchedVideos = [['Romantic', 'Comedy'], ['Action', 'Adventure'], ['Drama', 'Thriller'], ['Comedy', 'Romantic'], ['Adventure', 'Action'], ['Thriller', 'Drama'], ['Romantic', 'Drama'], ['Action', 'Comedy'], ['Adventure', 'Thriller']],friends = [[1, 2, 4], [0, 3, 5], [0, 4, 6], [1, 5, 7], [0, 2, 8], [1, 3, 8], [2], [3], [4, 5]],id = 4,level = 2) == ['Action', 'Adventure', 'Romantic', 'Thriller', 'Drama']
    assert candidate(watchedVideos = [['Documentary'], ['Documentary', 'Animation'], ['Animation'], ['Documentary', 'Animation', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Comedy']],friends = [[1, 2, 3], [0, 2, 4], [0, 1, 3, 5], [0, 2, 4, 5, 6], [1, 3, 5], [2, 3, 4, 6], [3, 5]],id = 1,level = 4) == []
    assert candidate(watchedVideos = [['Horror'], ['Horror', 'Thriller'], ['Thriller'], ['Horror', 'Thriller', 'Comedy'], ['Comedy', 'Action'], ['Action', 'Comedy'], ['Action', 'Comedy'], ['Comedy', 'Thriller'], ['Thriller', 'Horror']],friends = [[1, 2, 3], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 6, 7], [1, 6], [2, 7], [2, 3, 4, 7], [3, 5, 6], [3, 7]],id = 5,level = 3) == ['Action', 'Comedy']
    assert candidate(watchedVideos = [['Horror', 'SciFi'], ['Adventure', 'SciFi'], ['Horror', 'Comedy'], ['Comedy', 'SciFi'], ['Adventure', 'Comedy']],friends = [[1, 3, 4], [0, 2], [1, 3], [0, 2, 4], [0, 3]],id = 0,level = 2) == ['Comedy', 'Horror']
    assert candidate(watchedVideos = [['Adventure', 'Action'], ['Action'], ['Adventure', 'Action'], ['Adventure'], ['Action', 'Adventure'], ['Action'], ['Adventure', 'Action'], ['Action', 'Adventure']],friends = [[1, 2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7], [0, 1, 3, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7], [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6]],id = 6,level = 3) == []
    assert candidate(watchedVideos = [['Adventure', 'Comedy'], ['Action', 'Adventure'], ['Comedy', 'Drama'], ['Drama'], ['Action', 'Adventure']],friends = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]],id = 0,level = 2) == ['Action', 'Adventure', 'Drama']
    assert candidate(watchedVideos = [['Romance'], ['Romance', 'Comedy'], ['Romance'], ['Comedy'], ['Romance', 'Action'], ['Action', 'Drama'], ['Drama', 'Action'], ['Drama'], ['Comedy', 'Romance'], ['Romance', 'Drama']],friends = [[1, 2, 3, 4], [0, 5, 6, 7, 8, 9], [0, 9, 8], [0, 5, 7], [0, 5, 8, 9], [1, 3, 4, 6, 9], [1, 5, 9], [1, 3, 9], [2, 4, 9], [2, 3, 4, 5, 6, 7]],id = 5,level = 3) == []
    assert candidate(watchedVideos = [['Action', 'Adventure'], ['Sci-Fi', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Thriller'], ['Action', 'Sci-Fi'], ['Adventure', 'Thriller'], ['Adventure', 'Sci-Fi'], ['Action', 'Adventure'], ['Action', 'Thriller'], ['Sci-Fi', 'Adventure']],friends = [[1, 2, 3], [0, 4, 5], [0, 6, 7], [0, 8, 9], [1], [1, 2], [2], [2], [3], [3, 4]],id = 2,level = 2) == ['Action', 'Sci-Fi', 'Thriller']


