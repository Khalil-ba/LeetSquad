def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'sql'],people = [['python'], ['sql'], ['python', 'sql']]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'sql'],people = [['python'], ['sql'], ['python', 'sql']]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['java', 'nodejs', 'reactjs'],people = [['java'], ['nodejs'], ['nodejs', 'reactjs']]) == [2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['java', 'nodejs', 'reactjs'],people = [['java'], ['nodejs'], ['nodejs', 'reactjs']]) == [2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['programming', 'testing', 'design'],people = [['programming'], ['testing'], ['design'], ['programming', 'testing'], ['testing', 'design'], ['design', 'programming']]) == [4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['programming', 'testing', 'design'],people = [['programming'], ['testing'], ['design'], ['programming', 'testing'], ['testing', 'design'], ['design', 'programming']]) == [4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['a', 'b', 'c'],people = [['a', 'b'], ['b', 'c'], ['c'], ['a']]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['a', 'b', 'c'],people = [['a', 'b'], ['b', 'c'], ['c'], ['a']]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['network', 'database'],people = [['network'], ['database'], ['network', 'database']]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['network', 'database'],people = [['network'], ['database'], ['network', 'database']]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2', 'skill3', 'skill4']]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2', 'skill3', 'skill4']]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'design', 'writing'],people = [['coding'], ['design'], ['writing'], ['coding', 'design', 'writing']]) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'design', 'writing'],people = [['coding'], ['design'], ['writing'], ['coding', 'design', 'writing']]) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'design'],people = [['coding'], ['design'], ['coding', 'design']]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'design'],people = [['coding'], ['design'], ['coding', 'design']]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2'], ['skill3', 'skill4']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2'], ['skill3', 'skill4']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'],people = [['algorithms', 'math', 'java'], ['algorithms', 'math', 'reactjs'], ['java', 'csharp', 'aws'], ['reactjs', 'csharp'], ['csharp', 'math'], ['aws', 'java']]) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'],people = [['algorithms', 'math', 'java'], ['algorithms', 'math', 'reactjs'], ['java', 'csharp', 'aws'], ['reactjs', 'csharp'], ['csharp', 'math'], ['aws', 'java']]) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'data', 'ai'],people = [['python'], ['data'], ['ai'], ['python', 'data'], ['data', 'ai'], ['python', 'ai']]) == [4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'data', 'ai'],people = [['python'], ['data'], ['ai'], ['python', 'data'], ['data', 'ai'], ['python', 'ai']]) == [4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['req1', 'req2'],people = [['req1'], ['req2'], ['req1', 'req2'], ['req1'], ['req2']]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['req1', 'req2'],people = [['req1'], ['req2'], ['req1', 'req2'], ['req1'], ['req2']]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'noSql'],people = [['sql'], ['noSql'], ['sql', 'noSql'], ['sql'], ['noSql']]) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'noSql'],people = [['sql'], ['noSql'], ['sql', 'noSql'], ['sql'], ['noSql']]) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['skill1', 'skill2', 'skill3'],people = [['skill1', 'skill2'], ['skill2', 'skill3'], ['skill3', 'skill1']]) == [1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['skill1', 'skill2', 'skill3'],people = [['skill1', 'skill2'], ['skill2', 'skill3'], ['skill3', 'skill1']]) == [1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['a', 'b', 'c', 'd'],people = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a'], ['a', 'b', 'c', 'd']]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['a', 'b', 'c', 'd'],people = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a'], ['a', 'b', 'c', 'd']]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['devops', 'data_analysis', 'cloud_services', 'ui_ux'],people = [['devops'], ['data_analysis'], ['cloud_services'], ['ui_ux'], ['devops', 'data_analysis'], ['cloud_services', 'ui_ux'], ['devops', 'cloud_services'], ['data_analysis', 'ui_ux']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['devops', 'data_analysis', 'cloud_services', 'ui_ux'],people = [['devops'], ['data_analysis'], ['cloud_services'], ['ui_ux'], ['devops', 'data_analysis'], ['cloud_services', 'ui_ux'], ['devops', 'cloud_services'], ['data_analysis', 'ui_ux']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['machinelearning', 'deeplearning', 'computer_vision', 'nlp'],people = [['machinelearning'], ['deeplearning'], ['computer_vision'], ['nlp'], ['machinelearning', 'deeplearning'], ['computer_vision', 'nlp'], ['machinelearning', 'nlp']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['machinelearning', 'deeplearning', 'computer_vision', 'nlp'],people = [['machinelearning'], ['deeplearning'], ['computer_vision'], ['nlp'], ['machinelearning', 'deeplearning'], ['computer_vision', 'nlp'], ['machinelearning', 'nlp']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['frontend', 'backend', 'fullstack', 'uiux', 'devops'],people = [['frontend'], ['backend'], ['fullstack'], ['uiux'], ['devops'], ['frontend', 'backend'], ['fullstack', 'uiux'], ['backend', 'devops'], ['fullstack', 'devops'], ['frontend', 'uiux'], ['frontend', 'backend', 'uiux']]) == [8, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['frontend', 'backend', 'fullstack', 'uiux', 'devops'],people = [['frontend'], ['backend'], ['fullstack'], ['uiux'], ['devops'], ['frontend', 'backend'], ['fullstack', 'uiux'], ['backend', 'devops'], ['fullstack', 'devops'], ['frontend', 'uiux'], ['frontend', 'backend', 'uiux']]) == [8, 10]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['ui', 'ux', 'backend', 'frontend'],people = [['ui'], ['ux'], ['backend'], ['frontend'], ['ui', 'ux'], ['backend', 'frontend'], ['ui', 'backend'], ['ux', 'frontend'], ['ui', 'ux', 'backend', 'frontend']]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['ui', 'ux', 'backend', 'frontend'],people = [['ui'], ['ux'], ['backend'], ['frontend'], ['ui', 'ux'], ['backend', 'frontend'], ['ui', 'backend'], ['ux', 'frontend'], ['ui', 'ux', 'backend', 'frontend']]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'c++', 'ruby'],people = [['python', 'javascript'], ['c++'], ['ruby'], ['python', 'c++'], ['javascript', 'ruby']]) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'c++', 'ruby'],people = [['python', 'javascript'], ['c++'], ['ruby'], ['python', 'c++'], ['javascript', 'ruby']]) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['backend', 'devops'], ['devops', 'qa'], ['frontend', 'qa'], ['frontend', 'backend', 'devops'], ['backend', 'devops', 'qa'], ['frontend', 'devops', 'qa'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['backend', 'devops'], ['devops', 'qa'], ['frontend', 'qa'], ['frontend', 'backend', 'devops'], ['backend', 'devops', 'qa'], ['frontend', 'devops', 'qa'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'nosql', 'big_data', 'data_warehouse'],people = [['sql'], ['nosql'], ['big_data'], ['data_warehouse'], ['sql', 'nosql'], ['nosql', 'big_data'], ['big_data', 'data_warehouse'], ['sql', 'data_warehouse'], ['sql', 'nosql', 'big_data'], ['nosql', 'big_data', 'data_warehouse'], ['sql', 'big_data', 'data_warehouse'], ['sql', 'nosql', 'data_warehouse'], ['sql', 'nosql', 'big_data', 'data_warehouse']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'nosql', 'big_data', 'data_warehouse'],people = [['sql'], ['nosql'], ['big_data'], ['data_warehouse'], ['sql', 'nosql'], ['nosql', 'big_data'], ['big_data', 'data_warehouse'], ['sql', 'data_warehouse'], ['sql', 'nosql', 'big_data'], ['nosql', 'big_data', 'data_warehouse'], ['sql', 'big_data', 'data_warehouse'], ['sql', 'nosql', 'data_warehouse'], ['sql', 'nosql', 'big_data', 'data_warehouse']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['mobiledev', 'webdev', 'devops', 'design', 'testing'],people = [['mobiledev'], ['webdev'], ['devops'], ['design'], ['testing'], ['mobiledev', 'webdev'], ['devops', 'design'], ['webdev', 'testing'], ['mobiledev', 'devops'], ['design', 'testing'], ['mobiledev', 'webdev', 'devops'], ['devops', 'design', 'testing']]) == [11, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['mobiledev', 'webdev', 'devops', 'design', 'testing'],people = [['mobiledev'], ['webdev'], ['devops'], ['design'], ['testing'], ['mobiledev', 'webdev'], ['devops', 'design'], ['webdev', 'testing'], ['mobiledev', 'devops'], ['design', 'testing'], ['mobiledev', 'webdev', 'devops'], ['devops', 'design', 'testing']]) == [11, 5]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['algorithm', 'datastructure', 'programming', 'problem-solving'],people = [['algorithm'], ['datastructure'], ['programming'], ['problem-solving'], ['algorithm', 'datastructure'], ['programming', 'problem-solving'], ['algorithm', 'problem-solving'], ['datastructure', 'programming'], ['algorithm', 'datastructure', 'programming', 'problem-solving']]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['algorithm', 'datastructure', 'programming', 'problem-solving'],people = [['algorithm'], ['datastructure'], ['programming'], ['problem-solving'], ['algorithm', 'datastructure'], ['programming', 'problem-solving'], ['algorithm', 'problem-solving'], ['datastructure', 'programming'], ['algorithm', 'datastructure', 'programming', 'problem-solving']]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['iot', 'ml', 'ai', 'automation', 'cloudcomputing'],people = [['iot'], ['ml'], ['ai'], ['automation'], ['cloudcomputing'], ['iot', 'ml'], ['ai', 'automation'], ['cloudcomputing', 'ml'], ['iot', 'automation'], ['ai', 'cloudcomputing'], ['iot', 'ml', 'ai'], ['automation', 'cloudcomputing', 'ml']]) == [11, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['iot', 'ml', 'ai', 'automation', 'cloudcomputing'],people = [['iot'], ['ml'], ['ai'], ['automation'], ['cloudcomputing'], ['iot', 'ml'], ['ai', 'automation'], ['cloudcomputing', 'ml'], ['iot', 'automation'], ['ai', 'cloudcomputing'], ['iot', 'ml', 'ai'], ['automation', 'cloudcomputing', 'ml']]) == [11, 10]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['project_management', 'communication', 'problem_solving', 'decision_making'],people = [['project_management'], ['communication'], ['problem_solving'], ['decision_making'], ['project_management', 'communication'], ['problem_solving', 'decision_making'], ['project_management', 'problem_solving'], ['communication', 'decision_making'], ['project_management', 'communication', 'problem_solving'], ['communication', 'problem_solving', 'decision_making']]) == [9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['project_management', 'communication', 'problem_solving', 'decision_making'],people = [['project_management'], ['communication'], ['problem_solving'], ['decision_making'], ['project_management', 'communication'], ['problem_solving', 'decision_making'], ['project_management', 'problem_solving'], ['communication', 'decision_making'], ['project_management', 'communication', 'problem_solving'], ['communication', 'problem_solving', 'decision_making']]) == [9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['database', 'frontend', 'backend', 'devops', 'cloud', 'security'],people = [['database'], ['frontend'], ['backend'], ['devops'], ['cloud'], ['security'], ['database', 'frontend'], ['backend', 'devops'], ['cloud', 'security'], ['database', 'backend'], ['frontend', 'devops'], ['cloud', 'frontend'], ['database', 'cloud'], ['devops', 'security'], ['database', 'frontend', 'backend'], ['devops', 'cloud', 'security']]) == [15, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['database', 'frontend', 'backend', 'devops', 'cloud', 'security'],people = [['database'], ['frontend'], ['backend'], ['devops'], ['cloud'], ['security'], ['database', 'frontend'], ['backend', 'devops'], ['cloud', 'security'], ['database', 'backend'], ['frontend', 'devops'], ['cloud', 'frontend'], ['database', 'cloud'], ['devops', 'security'], ['database', 'frontend', 'backend'], ['devops', 'cloud', 'security']]) == [15, 14]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'ruby', 'cpp'],people = [['python', 'cpp'], ['javascript'], ['ruby'], ['python', 'javascript'], ['cpp', 'ruby'], ['python', 'ruby']]) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'ruby', 'cpp'],people = [['python', 'cpp'], ['javascript'], ['ruby'], ['python', 'javascript'], ['cpp', 'ruby'], ['python', 'ruby']]) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'nosql', 'devops', 'cloud', 'agile'],people = [['sql'], ['nosql'], ['devops'], ['cloud'], ['agile'], ['sql', 'nosql'], ['devops', 'cloud'], ['cloud', 'agile'], ['sql', 'devops'], ['nosql', 'agile']]) == [7, 8, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'nosql', 'devops', 'cloud', 'agile'],people = [['sql'], ['nosql'], ['devops'], ['cloud'], ['agile'], ['sql', 'nosql'], ['devops', 'cloud'], ['cloud', 'agile'], ['sql', 'devops'], ['nosql', 'agile']]) == [7, 8, 1]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['leadership', 'communication', 'programming', 'project-management', 'design'],people = [['leadership'], ['communication'], ['programming'], ['project-management'], ['design'], ['leadership', 'communication'], ['programming', 'project-management'], ['design', 'communication'], ['leadership', 'programming'], ['project-management', 'design'], ['leadership', 'programming', 'design'], ['communication', 'project-management', 'design'], ['leadership', 'communication', 'design']]) == [11, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['leadership', 'communication', 'programming', 'project-management', 'design'],people = [['leadership'], ['communication'], ['programming'], ['project-management'], ['design'], ['leadership', 'communication'], ['programming', 'project-management'], ['design', 'communication'], ['leadership', 'programming'], ['project-management', 'design'], ['leadership', 'programming', 'design'], ['communication', 'project-management', 'design'], ['leadership', 'communication', 'design']]) == [11, 8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['javascript', 'typescript', 'angular', 'react'],people = [['javascript'], ['typescript'], ['angular'], ['react'], ['javascript', 'typescript'], ['angular', 'react'], ['javascript', 'angular'], ['typescript', 'react'], ['javascript', 'typescript', 'angular', 'react']]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['javascript', 'typescript', 'angular', 'react'],people = [['javascript'], ['typescript'], ['angular'], ['react'], ['javascript', 'typescript'], ['angular', 'react'], ['javascript', 'angular'], ['typescript', 'react'], ['javascript', 'typescript', 'angular', 'react']]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'c++', 'ruby', 'go'],people = [['python', 'javascript'], ['c++', 'ruby'], ['go'], ['python', 'c++'], ['javascript', 'ruby', 'go']]) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'c++', 'ruby', 'go'],people = [['python', 'javascript'], ['c++', 'ruby'], ['go'], ['python', 'c++'], ['javascript', 'ruby', 'go']]) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['linux', 'windows', 'macos', 'docker'],people = [['linux'], ['windows'], ['macos'], ['docker'], ['linux', 'windows'], ['macos', 'docker'], ['linux', 'macos'], ['windows', 'docker'], ['linux', 'macos', 'docker'], ['windows', 'macos', 'docker'], ['linux', 'windows', 'docker'], ['linux', 'windows', 'macos', 'docker']]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['linux', 'windows', 'macos', 'docker'],people = [['linux'], ['windows'], ['macos'], ['docker'], ['linux', 'windows'], ['macos', 'docker'], ['linux', 'macos'], ['windows', 'docker'], ['linux', 'macos', 'docker'], ['windows', 'macos', 'docker'], ['linux', 'windows', 'docker'], ['linux', 'windows', 'macos', 'docker']]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience'],people = [['sql', 'nosql'], ['bigdata', 'machinelearning'], ['datascience'], ['sql', 'bigdata'], ['nosql', 'machinelearning'], ['bigdata', 'datascience'], ['machinelearning', 'datascience'], ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience']]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience'],people = [['sql', 'nosql'], ['bigdata', 'machinelearning'], ['datascience'], ['sql', 'bigdata'], ['nosql', 'machinelearning'], ['bigdata', 'datascience'], ['machinelearning', 'datascience'], ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience']]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws'],people = [['git', 'docker'], ['jenkins', 'travis'], ['circleci', 'aws'], ['git', 'travis'], ['docker', 'circleci'], ['jenkins', 'aws'], ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws']]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws'],people = [['git', 'docker'], ['jenkins', 'travis'], ['circleci', 'aws'], ['git', 'travis'], ['docker', 'circleci'], ['jenkins', 'aws'], ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws']]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['mongodb', 'postgresql', 'mysql', 'oracle'],people = [['mongodb'], ['postgresql'], ['mysql'], ['oracle'], ['mongodb', 'postgresql'], ['mysql', 'oracle'], ['mongodb', 'mysql'], ['postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql'], ['postgresql', 'mysql', 'oracle'], ['mongodb', 'mysql', 'oracle'], ['mongodb', 'postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql', 'oracle']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['mongodb', 'postgresql', 'mysql', 'oracle'],people = [['mongodb'], ['postgresql'], ['mysql'], ['oracle'], ['mongodb', 'postgresql'], ['mysql', 'oracle'], ['mongodb', 'mysql'], ['postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql'], ['postgresql', 'mysql', 'oracle'], ['mongodb', 'mysql', 'oracle'], ['mongodb', 'postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql', 'oracle']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['communication', 'problem_solving', 'critical_thinking', 'leadership'],people = [['communication'], ['problem_solving'], ['critical_thinking'], ['leadership'], ['communication', 'problem_solving'], ['critical_thinking', 'leadership'], ['communication', 'critical_thinking'], ['problem_solving', 'leadership'], ['communication', 'problem_solving', 'critical_thinking'], ['communication', 'problem_solving', 'leadership'], ['communication', 'critical_thinking', 'leadership'], ['problem_solving', 'critical_thinking', 'leadership'], ['communication', 'problem_solving', 'critical_thinking', 'leadership']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['communication', 'problem_solving', 'critical_thinking', 'leadership'],people = [['communication'], ['problem_solving'], ['critical_thinking'], ['leadership'], ['communication', 'problem_solving'], ['critical_thinking', 'leadership'], ['communication', 'critical_thinking'], ['problem_solving', 'leadership'], ['communication', 'problem_solving', 'critical_thinking'], ['communication', 'problem_solving', 'leadership'], ['communication', 'critical_thinking', 'leadership'], ['problem_solving', 'critical_thinking', 'leadership'], ['communication', 'problem_solving', 'critical_thinking', 'leadership']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision'],people = [['image_processing'], ['natural_language_processing'], ['deep_learning'], ['computer_vision'], ['image_processing', 'natural_language_processing'], ['deep_learning', 'computer_vision'], ['image_processing', 'deep_learning'], ['natural_language_processing', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning'], ['natural_language_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision']]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision'],people = [['image_processing'], ['natural_language_processing'], ['deep_learning'], ['computer_vision'], ['image_processing', 'natural_language_processing'], ['deep_learning', 'computer_vision'], ['image_processing', 'deep_learning'], ['natural_language_processing', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning'], ['natural_language_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision']]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['java', 'spring', 'hibernate', 'react'],people = [['java'], ['spring'], ['hibernate'], ['react'], ['java', 'spring'], ['spring', 'hibernate'], ['hibernate', 'react'], ['java', 'react'], ['java', 'spring', 'hibernate'], ['java', 'spring', 'react'], ['spring', 'hibernate', 'react'], ['java', 'spring', 'hibernate', 'react']]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['java', 'spring', 'hibernate', 'react'],people = [['java'], ['spring'], ['hibernate'], ['react'], ['java', 'spring'], ['spring', 'hibernate'], ['hibernate', 'react'], ['java', 'react'], ['java', 'spring', 'hibernate'], ['java', 'spring', 'react'], ['spring', 'hibernate', 'react'], ['java', 'spring', 'hibernate', 'react']]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'python', 'frontend', 'backend'],people = [['sql'], ['python'], ['frontend'], ['backend'], ['sql', 'python'], ['frontend', 'backend']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'python', 'frontend', 'backend'],people = [['sql'], ['python'], ['frontend'], ['backend'], ['sql', 'python'], ['frontend', 'backend']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'java', 'c++', 'ruby'],people = [['python'], ['java'], ['c++'], ['ruby'], ['python', 'java'], ['c++', 'ruby'], ['python', 'c++'], ['java', 'ruby']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'java', 'c++', 'ruby'],people = [['python'], ['java'], ['c++'], ['ruby'], ['python', 'java'], ['c++', 'ruby'], ['python', 'c++'], ['java', 'ruby']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['aws', 'azure', 'gcp'],people = [['aws', 'azure'], ['gcp'], ['aws'], ['azure', 'gcp'], ['aws', 'gcp'], ['azure'], ['aws', 'azure', 'gcp']]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['aws', 'azure', 'gcp'],people = [['aws', 'azure'], ['gcp'], ['aws'], ['azure', 'gcp'], ['aws', 'gcp'], ['azure'], ['aws', 'azure', 'gcp']]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['data_science', 'data_engineering', 'ai', 'ml'],people = [['data_science'], ['data_engineering'], ['ai'], ['ml'], ['data_science', 'data_engineering'], ['ai', 'ml'], ['data_science', 'ai'], ['data_engineering', 'ml'], ['data_science', 'data_engineering', 'ai'], ['data_engineering', 'ai', 'ml'], ['data_science', 'ai', 'ml'], ['data_science', 'data_engineering', 'ai', 'ml']]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['data_science', 'data_engineering', 'ai', 'ml'],people = [['data_science'], ['data_engineering'], ['ai'], ['ml'], ['data_science', 'data_engineering'], ['ai', 'ml'], ['data_science', 'ai'], ['data_engineering', 'ml'], ['data_science', 'data_engineering', 'ai'], ['data_engineering', 'ai', 'ml'], ['data_science', 'ai', 'ml'], ['data_science', 'data_engineering', 'ai', 'ml']]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['security', 'testing', 'projectmanagement', 'communication', 'design'],people = [['security'], ['testing'], ['projectmanagement'], ['communication'], ['design'], ['security', 'testing'], ['projectmanagement', 'communication'], ['design', 'security'], ['testing', 'communication'], ['security', 'projectmanagement', 'design'], ['testing', 'communication', 'design']]) == [9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['security', 'testing', 'projectmanagement', 'communication', 'design'],people = [['security'], ['testing'], ['projectmanagement'], ['communication'], ['design'], ['security', 'testing'], ['projectmanagement', 'communication'], ['design', 'security'], ['testing', 'communication'], ['security', 'projectmanagement', 'design'], ['testing', 'communication', 'design']]) == [9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'debugging', 'testing', 'design'],people = [['coding', 'debugging'], ['testing'], ['design'], ['coding', 'testing'], ['debugging', 'design']]) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'debugging', 'testing', 'design'],people = [['coding', 'debugging'], ['testing'], ['design'], ['coding', 'testing'], ['debugging', 'design']]) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['photoshop', 'illustrator', 'indesign', 'lightroom'],people = [['photoshop', 'illustrator'], ['indesign'], ['lightroom'], ['photoshop', 'indesign'], ['illustrator', 'lightroom'], ['photoshop', 'lightroom'], ['indesign', 'lightroom'], ['photoshop', 'illustrator', 'indesign'], ['illustrator', 'indesign', 'lightroom'], ['photoshop', 'indesign', 'lightroom'], ['photoshop', 'illustrator', 'lightroom'], ['photoshop', 'illustrator', 'indesign', 'lightroom']]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['photoshop', 'illustrator', 'indesign', 'lightroom'],people = [['photoshop', 'illustrator'], ['indesign'], ['lightroom'], ['photoshop', 'indesign'], ['illustrator', 'lightroom'], ['photoshop', 'lightroom'], ['indesign', 'lightroom'], ['photoshop', 'illustrator', 'indesign'], ['illustrator', 'indesign', 'lightroom'], ['photoshop', 'indesign', 'lightroom'], ['photoshop', 'illustrator', 'lightroom'], ['photoshop', 'illustrator', 'indesign', 'lightroom']]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['algorithm', 'data-structures', 'database', 'networking', 'os'],people = [['algorithm', 'data-structures'], ['database'], ['networking'], ['os'], ['algorithm', 'os'], ['data-structures', 'networking'], ['database', 'os'], ['algorithm', 'data-structures', 'database'], ['networking', 'os'], ['algorithm', 'networking', 'os']]) == [8, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['algorithm', 'data-structures', 'database', 'networking', 'os'],people = [['algorithm', 'data-structures'], ['database'], ['networking'], ['os'], ['algorithm', 'os'], ['data-structures', 'networking'], ['database', 'os'], ['algorithm', 'data-structures', 'database'], ['networking', 'os'], ['algorithm', 'networking', 'os']]) == [8, 7]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['security', 'analytics', 'ml', 'devops'],people = [['security'], ['analytics'], ['ml'], ['devops'], ['security', 'analytics'], ['ml', 'devops'], ['security', 'ml'], ['analytics', 'devops'], ['security', 'analytics', 'ml'], ['security', 'analytics', 'devops'], ['security', 'ml', 'devops'], ['analytics', 'ml', 'devops'], ['security', 'analytics', 'ml', 'devops']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['security', 'analytics', 'ml', 'devops'],people = [['security'], ['analytics'], ['ml'], ['devops'], ['security', 'analytics'], ['ml', 'devops'], ['security', 'ml'], ['analytics', 'devops'], ['security', 'analytics', 'ml'], ['security', 'analytics', 'devops'], ['security', 'ml', 'devops'], ['analytics', 'ml', 'devops'], ['security', 'analytics', 'ml', 'devops']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'no_sql', 'big_data', 'cloud_computing'],people = [['sql'], ['no_sql'], ['big_data'], ['cloud_computing'], ['sql', 'no_sql'], ['big_data', 'cloud_computing'], ['sql', 'big_data'], ['no_sql', 'cloud_computing'], ['sql', 'no_sql', 'big_data'], ['no_sql', 'big_data', 'cloud_computing'], ['sql', 'big_data', 'cloud_computing'], ['sql', 'no_sql', 'cloud_computing']]) == [9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'no_sql', 'big_data', 'cloud_computing'],people = [['sql'], ['no_sql'], ['big_data'], ['cloud_computing'], ['sql', 'no_sql'], ['big_data', 'cloud_computing'], ['sql', 'big_data'], ['no_sql', 'cloud_computing'], ['sql', 'no_sql', 'big_data'], ['no_sql', 'big_data', 'cloud_computing'], ['sql', 'big_data', 'cloud_computing'], ['sql', 'no_sql', 'cloud_computing']]) == [9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'debugging', 'design', 'deployment'],people = [['coding', 'debugging'], ['design'], ['deployment'], ['coding', 'deployment'], ['design', 'debugging']]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'debugging', 'design', 'deployment'],people = [['coding', 'debugging'], ['design'], ['deployment'], ['coding', 'deployment'], ['design', 'debugging']]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['sql', 'nosql', 'bigdata', 'cloud', 'devops'],people = [['sql'], ['nosql'], ['bigdata'], ['cloud'], ['devops'], ['sql', 'nosql'], ['bigdata', 'cloud'], ['devops', 'sql'], ['nosql', 'cloud'], ['bigdata', 'devops'], ['sql', 'cloud'], ['nosql', 'devops'], ['bigdata', 'sql'], ['cloud', 'devops'], ['sql', 'nosql', 'cloud'], ['bigdata', 'sql', 'cloud'], ['nosql', 'cloud', 'devops']]) == [16, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['sql', 'nosql', 'bigdata', 'cloud', 'devops'],people = [['sql'], ['nosql'], ['bigdata'], ['cloud'], ['devops'], ['sql', 'nosql'], ['bigdata', 'cloud'], ['devops', 'sql'], ['nosql', 'cloud'], ['bigdata', 'devops'], ['sql', 'cloud'], ['nosql', 'devops'], ['bigdata', 'sql'], ['cloud', 'devops'], ['sql', 'nosql', 'cloud'], ['bigdata', 'sql', 'cloud'], ['nosql', 'cloud', 'devops']]) == [16, 12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'cpp', 'java', 'javascript'],people = [['python', 'cpp'], ['java'], ['javascript', 'java'], ['cpp', 'python'], ['cpp', 'java'], ['javascript']]) == [2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'cpp', 'java', 'javascript'],people = [['python', 'cpp'], ['java'], ['javascript', 'java'], ['cpp', 'python'], ['cpp', 'java'], ['javascript']]) == [2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'debugging', 'testing', 'deployment'],people = [['coding'], ['debugging'], ['testing'], ['deployment'], ['coding', 'debugging'], ['testing', 'deployment'], ['coding', 'testing'], ['debugging', 'deployment'], ['coding', 'debugging', 'testing'], ['debugging', 'testing', 'deployment'], ['coding', 'debugging', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'debugging', 'testing', 'deployment']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'debugging', 'testing', 'deployment'],people = [['coding'], ['debugging'], ['testing'], ['deployment'], ['coding', 'debugging'], ['testing', 'deployment'], ['coding', 'testing'], ['debugging', 'deployment'], ['coding', 'debugging', 'testing'], ['debugging', 'testing', 'deployment'], ['coding', 'debugging', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'debugging', 'testing', 'deployment']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['networking', 'security', 'project_management', 'budgeting'],people = [['networking'], ['security'], ['project_management'], ['budgeting'], ['networking', 'security'], ['project_management', 'budgeting'], ['networking', 'project_management'], ['security', 'budgeting'], ['networking', 'project_management', 'budgeting'], ['networking', 'security', 'project_management', 'budgeting']]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['networking', 'security', 'project_management', 'budgeting'],people = [['networking'], ['security'], ['project_management'], ['budgeting'], ['networking', 'security'], ['project_management', 'budgeting'], ['networking', 'project_management'], ['security', 'budgeting'], ['networking', 'project_management', 'budgeting'], ['networking', 'security', 'project_management', 'budgeting']]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['aws', 'azure', 'gcp', 'docker', 'kubernetes'],people = [['aws', 'azure'], ['gcp', 'docker'], ['kubernetes'], ['aws', 'docker'], ['azure', 'gcp'], ['aws', 'gcp', 'kubernetes']]) == [5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['aws', 'azure', 'gcp', 'docker', 'kubernetes'],people = [['aws', 'azure'], ['gcp', 'docker'], ['kubernetes'], ['aws', 'docker'], ['azure', 'gcp'], ['aws', 'gcp', 'kubernetes']]) == [5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['coding', 'testing', 'documentation', 'deployment'],people = [['coding', 'testing'], ['documentation', 'deployment'], ['coding', 'documentation'], ['testing', 'deployment'], ['coding', 'testing', 'documentation'], ['testing', 'documentation', 'deployment'], ['coding', 'documentation', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'testing', 'documentation', 'deployment']]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['coding', 'testing', 'documentation', 'deployment'],people = [['coding', 'testing'], ['documentation', 'deployment'], ['coding', 'documentation'], ['testing', 'deployment'], ['coding', 'testing', 'documentation'], ['testing', 'documentation', 'deployment'], ['coding', 'documentation', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'testing', 'documentation', 'deployment']]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['html', 'css', 'javascript', 'react', 'nodejs'],people = [['html', 'css'], ['javascript'], ['react', 'nodejs'], ['html', 'javascript'], ['css', 'nodejs'], ['react'], ['html', 'javascript', 'react']]) == [4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['html', 'css', 'javascript', 'react', 'nodejs'],people = [['html', 'css'], ['javascript'], ['react', 'nodejs'], ['html', 'javascript'], ['css', 'nodejs'], ['react'], ['html', 'javascript', 'react']]) == [4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['product', 'design', 'backend', 'frontend', 'testing'],people = [['product'], ['design'], ['backend'], ['frontend'], ['testing'], ['product', 'design'], ['backend', 'frontend'], ['testing', 'product'], ['design', 'backend'], ['frontend', 'testing'], ['product', 'backend', 'frontend', 'testing'], ['design', 'backend', 'frontend', 'testing']]) == [11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['product', 'design', 'backend', 'frontend', 'testing'],people = [['product'], ['design'], ['backend'], ['frontend'], ['testing'], ['product', 'design'], ['backend', 'frontend'], ['testing', 'product'], ['design', 'backend'], ['frontend', 'testing'], ['product', 'backend', 'frontend', 'testing'], ['design', 'backend', 'frontend', 'testing']]) == [11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['docker', 'kubernetes', 'aws', 'gcp'],people = [['docker'], ['kubernetes'], ['aws'], ['gcp'], ['docker', 'kubernetes'], ['aws', 'gcp'], ['docker', 'aws'], ['kubernetes', 'gcp']]) == [5, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['docker', 'kubernetes', 'aws', 'gcp'],people = [['docker'], ['kubernetes'], ['aws'], ['gcp'], ['docker', 'kubernetes'], ['aws', 'gcp'], ['docker', 'aws'], ['kubernetes', 'gcp']]) == [5, 4]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['linux', 'windows', 'macos', 'unix'],people = [['linux'], ['windows'], ['macos'], ['unix'], ['linux', 'windows'], ['macos', 'unix'], ['linux', 'macos'], ['windows', 'unix'], ['linux', 'unix'], ['windows', 'macos'], ['linux', 'macos', 'unix'], ['linux', 'windows', 'unix'], ['windows', 'macos', 'unix'], ['linux', 'windows', 'macos'], ['linux', 'windows', 'macos', 'unix']]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['linux', 'windows', 'macos', 'unix'],people = [['linux'], ['windows'], ['macos'], ['unix'], ['linux', 'windows'], ['macos', 'unix'], ['linux', 'macos'], ['windows', 'unix'], ['linux', 'unix'], ['windows', 'macos'], ['linux', 'macos', 'unix'], ['linux', 'windows', 'unix'], ['windows', 'macos', 'unix'], ['linux', 'windows', 'macos'], ['linux', 'windows', 'macos', 'unix']]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'typescript', 'react', 'angular', 'vue'],people = [['python'], ['javascript'], ['typescript'], ['react'], ['angular'], ['vue'], ['python', 'javascript'], ['typescript', 'react'], ['angular', 'vue'], ['python', 'react'], ['javascript', 'vue']]) == [8, 7, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'typescript', 'react', 'angular', 'vue'],people = [['python'], ['javascript'], ['typescript'], ['react'], ['angular'], ['vue'], ['python', 'javascript'], ['typescript', 'react'], ['angular', 'vue'], ['python', 'react'], ['javascript', 'vue']]) == [8, 7, 6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['html', 'css', 'javascript', 'react'],people = [['html', 'css'], ['javascript'], ['react'], ['css', 'javascript'], ['html', 'react'], ['html', 'css', 'javascript', 'react']]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['html', 'css', 'javascript', 'react'],people = [['html', 'css'], ['javascript'], ['react'], ['css', 'javascript'], ['html', 'react'], ['html', 'css', 'javascript', 'react']]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['algorithm', 'data_structure', 'design_patterns', 'software_architecture'],people = [['algorithm'], ['data_structure'], ['design_patterns'], ['software_architecture'], ['algorithm', 'data_structure'], ['design_patterns', 'software_architecture'], ['algorithm', 'design_patterns'], ['data_structure', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns'], ['algorithm', 'data_structure', 'software_architecture'], ['algorithm', 'design_patterns', 'software_architecture'], ['data_structure', 'design_patterns', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns', 'software_architecture']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['algorithm', 'data_structure', 'design_patterns', 'software_architecture'],people = [['algorithm'], ['data_structure'], ['design_patterns'], ['software_architecture'], ['algorithm', 'data_structure'], ['design_patterns', 'software_architecture'], ['algorithm', 'design_patterns'], ['data_structure', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns'], ['algorithm', 'data_structure', 'software_architecture'], ['algorithm', 'design_patterns', 'software_architecture'], ['data_structure', 'design_patterns', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns', 'software_architecture']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['devops', 'qa'], ['frontend', 'devops'], ['backend', 'qa'], ['frontend', 'devops', 'qa'], ['backend', 'devops', 'qa'], ['frontend', 'backend', 'devops'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['devops', 'qa'], ['frontend', 'devops'], ['backend', 'qa'], ['frontend', 'devops', 'qa'], ['backend', 'devops', 'qa'], ['frontend', 'backend', 'devops'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['machine-learning', 'deep-learning', 'neural-networks', 'cv', 'nlp'],people = [['machine-learning'], ['deep-learning'], ['neural-networks'], ['cv'], ['nlp'], ['machine-learning', 'deep-learning'], ['neural-networks', 'cv'], ['nlp', 'machine-learning'], ['deep-learning', 'cv'], ['neural-networks', 'nlp'], ['machine-learning', 'cv'], ['deep-learning', 'nlp'], ['machine-learning', 'neural-networks'], ['deep-learning', 'neural-networks'], ['cv', 'nlp'], ['machine-learning', 'deep-learning', 'cv'], ['neural-networks', 'cv', 'nlp'], ['machine-learning', 'deep-learning', 'nlp'], ['neural-networks', 'deep-learning', 'cv', 'nlp'], ['machine-learning', 'neural-networks', 'cv', 'nlp']]) == [18, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['machine-learning', 'deep-learning', 'neural-networks', 'cv', 'nlp'],people = [['machine-learning'], ['deep-learning'], ['neural-networks'], ['cv'], ['nlp'], ['machine-learning', 'deep-learning'], ['neural-networks', 'cv'], ['nlp', 'machine-learning'], ['deep-learning', 'cv'], ['neural-networks', 'nlp'], ['machine-learning', 'cv'], ['deep-learning', 'nlp'], ['machine-learning', 'neural-networks'], ['deep-learning', 'neural-networks'], ['cv', 'nlp'], ['machine-learning', 'deep-learning', 'cv'], ['neural-networks', 'cv', 'nlp'], ['machine-learning', 'deep-learning', 'nlp'], ['neural-networks', 'deep-learning', 'cv', 'nlp'], ['machine-learning', 'neural-networks', 'cv', 'nlp']]) == [18, 0]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment'],people = [['network_security'], ['cyber_security'], ['penetration_testing'], ['vulnerability_assessment'], ['network_security', 'cyber_security'], ['penetration_testing', 'vulnerability_assessment'], ['network_security', 'penetration_testing'], ['cyber_security', 'vulnerability_assessment'], ['network_security', 'vulnerability_assessment'], ['cyber_security', 'penetration_testing'], ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment']]) == [10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment'],people = [['network_security'], ['cyber_security'], ['penetration_testing'], ['vulnerability_assessment'], ['network_security', 'cyber_security'], ['penetration_testing', 'vulnerability_assessment'], ['network_security', 'penetration_testing'], ['cyber_security', 'vulnerability_assessment'], ['network_security', 'vulnerability_assessment'], ['cyber_security', 'penetration_testing'], ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment']]) == [10]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['front_end', 'back_end', 'database', 'cloud_services'],people = [['front_end'], ['back_end'], ['database'], ['cloud_services'], ['front_end', 'back_end'], ['database', 'cloud_services'], ['front_end', 'database'], ['back_end', 'cloud_services'], ['front_end', 'back_end', 'database'], ['front_end', 'back_end', 'cloud_services'], ['front_end', 'database', 'cloud_services'], ['back_end', 'database', 'cloud_services'], ['front_end', 'back_end', 'database', 'cloud_services']]) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['front_end', 'back_end', 'database', 'cloud_services'],people = [['front_end'], ['back_end'], ['database'], ['cloud_services'], ['front_end', 'back_end'], ['database', 'cloud_services'], ['front_end', 'database'], ['back_end', 'cloud_services'], ['front_end', 'back_end', 'database'], ['front_end', 'back_end', 'cloud_services'], ['front_end', 'database', 'cloud_services'], ['back_end', 'database', 'cloud_services'], ['front_end', 'back_end', 'database', 'cloud_services']]) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['data_science', 'machine_learning', 'deep_learning', 'computer_vision'],people = [['data_science'], ['machine_learning'], ['deep_learning'], ['computer_vision'], ['machine_learning', 'deep_learning'], ['data_science', 'computer_vision'], ['data_science', 'machine_learning'], ['data_science', 'deep_learning'], ['machine_learning', 'computer_vision'], ['deep_learning', 'computer_vision']]) == [9, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['data_science', 'machine_learning', 'deep_learning', 'computer_vision'],people = [['data_science'], ['machine_learning'], ['deep_learning'], ['computer_vision'], ['machine_learning', 'deep_learning'], ['data_science', 'computer_vision'], ['data_science', 'machine_learning'], ['data_science', 'deep_learning'], ['machine_learning', 'computer_vision'], ['deep_learning', 'computer_vision']]) == [9, 6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'html', 'css', 'react', 'nodejs'],people = [['python'], ['javascript'], ['html'], ['css'], ['react'], ['nodejs'], ['python', 'javascript'], ['html', 'css'], ['react', 'nodejs'], ['python', 'html', 'css'], ['javascript', 'react', 'nodejs']]) == [10, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'html', 'css', 'react', 'nodejs'],people = [['python'], ['javascript'], ['html'], ['css'], ['react'], ['nodejs'], ['python', 'javascript'], ['html', 'css'], ['react', 'nodejs'], ['python', 'html', 'css'], ['javascript', 'react', 'nodejs']]) == [10, 9]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['machine_learning', 'deep_learning', 'cv', 'nlp'],people = [['machine_learning', 'deep_learning'], ['cv'], ['nlp'], ['deep_learning', 'cv'], ['machine_learning', 'nlp'], ['deep_learning', 'nlp', 'cv'], ['machine_learning', 'deep_learning', 'cv', 'nlp']]) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['machine_learning', 'deep_learning', 'cv', 'nlp'],people = [['machine_learning', 'deep_learning'], ['cv'], ['nlp'], ['deep_learning', 'cv'], ['machine_learning', 'nlp'], ['deep_learning', 'nlp', 'cv'], ['machine_learning', 'deep_learning', 'cv', 'nlp']]) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['ux', 'ui', 'product', 'design', 'marketing'],people = [['ux'], ['ui'], ['product'], ['design'], ['marketing'], ['ux', 'ui'], ['product', 'design'], ['marketing', 'ux'], ['ui', 'product'], ['design', 'marketing'], ['ux', 'product'], ['ui', 'marketing'], ['product', 'design', 'marketing'], ['ux', 'ui', 'design'], ['ui', 'product', 'design'], ['ux', 'product', 'marketing'], ['ux', 'ui', 'product', 'design', 'marketing']]) == [16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['ux', 'ui', 'product', 'design', 'marketing'],people = [['ux'], ['ui'], ['product'], ['design'], ['marketing'], ['ux', 'ui'], ['product', 'design'], ['marketing', 'ux'], ['ui', 'product'], ['design', 'marketing'], ['ux', 'product'], ['ui', 'marketing'], ['product', 'design', 'marketing'], ['ux', 'ui', 'design'], ['ui', 'product', 'design'], ['ux', 'product', 'marketing'], ['ux', 'ui', 'product', 'design', 'marketing']]) == [16]: {e}')
    
    total += 1
    try:
        result = candidate(req_skills = ['python', 'javascript', 'cpp', 'go'],people = [['python', 'cpp'], ['javascript'], ['go'], ['python', 'javascript', 'go'], ['cpp', 'javascript']]) == [3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(req_skills = ['python', 'javascript', 'cpp', 'go'],people = [['python', 'cpp'], ['javascript'], ['go'], ['python', 'javascript', 'go'], ['cpp', 'javascript']]) == [3, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(req_skills = ['python', 'sql'],people = [['python'], ['sql'], ['python', 'sql']]) == [2]
    assert candidate(req_skills = ['java', 'nodejs', 'reactjs'],people = [['java'], ['nodejs'], ['nodejs', 'reactjs']]) == [2, 0]
    assert candidate(req_skills = ['programming', 'testing', 'design'],people = [['programming'], ['testing'], ['design'], ['programming', 'testing'], ['testing', 'design'], ['design', 'programming']]) == [4, 0]
    assert candidate(req_skills = ['a', 'b', 'c'],people = [['a', 'b'], ['b', 'c'], ['c'], ['a']]) == [1, 3]
    assert candidate(req_skills = ['network', 'database'],people = [['network'], ['database'], ['network', 'database']]) == [2]
    assert candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2', 'skill3', 'skill4']]) == [4]
    assert candidate(req_skills = ['coding', 'design', 'writing'],people = [['coding'], ['design'], ['writing'], ['coding', 'design', 'writing']]) == [3]
    assert candidate(req_skills = ['coding', 'design'],people = [['coding'], ['design'], ['coding', 'design']]) == [2]
    assert candidate(req_skills = ['skill1', 'skill2', 'skill3', 'skill4'],people = [['skill1'], ['skill2'], ['skill3'], ['skill4'], ['skill1', 'skill2'], ['skill3', 'skill4']]) == [5, 4]
    assert candidate(req_skills = ['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'],people = [['algorithms', 'math', 'java'], ['algorithms', 'math', 'reactjs'], ['java', 'csharp', 'aws'], ['reactjs', 'csharp'], ['csharp', 'math'], ['aws', 'java']]) == [2, 1]
    assert candidate(req_skills = ['python', 'data', 'ai'],people = [['python'], ['data'], ['ai'], ['python', 'data'], ['data', 'ai'], ['python', 'ai']]) == [4, 0]
    assert candidate(req_skills = ['req1', 'req2'],people = [['req1'], ['req2'], ['req1', 'req2'], ['req1'], ['req2']]) == [2]
    assert candidate(req_skills = ['sql', 'noSql'],people = [['sql'], ['noSql'], ['sql', 'noSql'], ['sql'], ['noSql']]) == [2]
    assert candidate(req_skills = ['skill1', 'skill2', 'skill3'],people = [['skill1', 'skill2'], ['skill2', 'skill3'], ['skill3', 'skill1']]) == [1, 0]
    assert candidate(req_skills = ['a', 'b', 'c', 'd'],people = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'a'], ['a', 'b', 'c', 'd']]) == [4]
    assert candidate(req_skills = ['devops', 'data_analysis', 'cloud_services', 'ui_ux'],people = [['devops'], ['data_analysis'], ['cloud_services'], ['ui_ux'], ['devops', 'data_analysis'], ['cloud_services', 'ui_ux'], ['devops', 'cloud_services'], ['data_analysis', 'ui_ux']]) == [5, 4]
    assert candidate(req_skills = ['machinelearning', 'deeplearning', 'computer_vision', 'nlp'],people = [['machinelearning'], ['deeplearning'], ['computer_vision'], ['nlp'], ['machinelearning', 'deeplearning'], ['computer_vision', 'nlp'], ['machinelearning', 'nlp']]) == [5, 4]
    assert candidate(req_skills = ['frontend', 'backend', 'fullstack', 'uiux', 'devops'],people = [['frontend'], ['backend'], ['fullstack'], ['uiux'], ['devops'], ['frontend', 'backend'], ['fullstack', 'uiux'], ['backend', 'devops'], ['fullstack', 'devops'], ['frontend', 'uiux'], ['frontend', 'backend', 'uiux']]) == [8, 10]
    assert candidate(req_skills = ['ui', 'ux', 'backend', 'frontend'],people = [['ui'], ['ux'], ['backend'], ['frontend'], ['ui', 'ux'], ['backend', 'frontend'], ['ui', 'backend'], ['ux', 'frontend'], ['ui', 'ux', 'backend', 'frontend']]) == [8]
    assert candidate(req_skills = ['python', 'javascript', 'c++', 'ruby'],people = [['python', 'javascript'], ['c++'], ['ruby'], ['python', 'c++'], ['javascript', 'ruby']]) == [4, 3]
    assert candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['backend', 'devops'], ['devops', 'qa'], ['frontend', 'qa'], ['frontend', 'backend', 'devops'], ['backend', 'devops', 'qa'], ['frontend', 'devops', 'qa'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]
    assert candidate(req_skills = ['sql', 'nosql', 'big_data', 'data_warehouse'],people = [['sql'], ['nosql'], ['big_data'], ['data_warehouse'], ['sql', 'nosql'], ['nosql', 'big_data'], ['big_data', 'data_warehouse'], ['sql', 'data_warehouse'], ['sql', 'nosql', 'big_data'], ['nosql', 'big_data', 'data_warehouse'], ['sql', 'big_data', 'data_warehouse'], ['sql', 'nosql', 'data_warehouse'], ['sql', 'nosql', 'big_data', 'data_warehouse']]) == [12]
    assert candidate(req_skills = ['mobiledev', 'webdev', 'devops', 'design', 'testing'],people = [['mobiledev'], ['webdev'], ['devops'], ['design'], ['testing'], ['mobiledev', 'webdev'], ['devops', 'design'], ['webdev', 'testing'], ['mobiledev', 'devops'], ['design', 'testing'], ['mobiledev', 'webdev', 'devops'], ['devops', 'design', 'testing']]) == [11, 5]
    assert candidate(req_skills = ['algorithm', 'datastructure', 'programming', 'problem-solving'],people = [['algorithm'], ['datastructure'], ['programming'], ['problem-solving'], ['algorithm', 'datastructure'], ['programming', 'problem-solving'], ['algorithm', 'problem-solving'], ['datastructure', 'programming'], ['algorithm', 'datastructure', 'programming', 'problem-solving']]) == [8]
    assert candidate(req_skills = ['iot', 'ml', 'ai', 'automation', 'cloudcomputing'],people = [['iot'], ['ml'], ['ai'], ['automation'], ['cloudcomputing'], ['iot', 'ml'], ['ai', 'automation'], ['cloudcomputing', 'ml'], ['iot', 'automation'], ['ai', 'cloudcomputing'], ['iot', 'ml', 'ai'], ['automation', 'cloudcomputing', 'ml']]) == [11, 10]
    assert candidate(req_skills = ['project_management', 'communication', 'problem_solving', 'decision_making'],people = [['project_management'], ['communication'], ['problem_solving'], ['decision_making'], ['project_management', 'communication'], ['problem_solving', 'decision_making'], ['project_management', 'problem_solving'], ['communication', 'decision_making'], ['project_management', 'communication', 'problem_solving'], ['communication', 'problem_solving', 'decision_making']]) == [9, 0]
    assert candidate(req_skills = ['database', 'frontend', 'backend', 'devops', 'cloud', 'security'],people = [['database'], ['frontend'], ['backend'], ['devops'], ['cloud'], ['security'], ['database', 'frontend'], ['backend', 'devops'], ['cloud', 'security'], ['database', 'backend'], ['frontend', 'devops'], ['cloud', 'frontend'], ['database', 'cloud'], ['devops', 'security'], ['database', 'frontend', 'backend'], ['devops', 'cloud', 'security']]) == [15, 14]
    assert candidate(req_skills = ['python', 'javascript', 'ruby', 'cpp'],people = [['python', 'cpp'], ['javascript'], ['ruby'], ['python', 'javascript'], ['cpp', 'ruby'], ['python', 'ruby']]) == [4, 3]
    assert candidate(req_skills = ['sql', 'nosql', 'devops', 'cloud', 'agile'],people = [['sql'], ['nosql'], ['devops'], ['cloud'], ['agile'], ['sql', 'nosql'], ['devops', 'cloud'], ['cloud', 'agile'], ['sql', 'devops'], ['nosql', 'agile']]) == [7, 8, 1]
    assert candidate(req_skills = ['leadership', 'communication', 'programming', 'project-management', 'design'],people = [['leadership'], ['communication'], ['programming'], ['project-management'], ['design'], ['leadership', 'communication'], ['programming', 'project-management'], ['design', 'communication'], ['leadership', 'programming'], ['project-management', 'design'], ['leadership', 'programming', 'design'], ['communication', 'project-management', 'design'], ['leadership', 'communication', 'design']]) == [11, 8]
    assert candidate(req_skills = ['javascript', 'typescript', 'angular', 'react'],people = [['javascript'], ['typescript'], ['angular'], ['react'], ['javascript', 'typescript'], ['angular', 'react'], ['javascript', 'angular'], ['typescript', 'react'], ['javascript', 'typescript', 'angular', 'react']]) == [8]
    assert candidate(req_skills = ['python', 'javascript', 'c++', 'ruby', 'go'],people = [['python', 'javascript'], ['c++', 'ruby'], ['go'], ['python', 'c++'], ['javascript', 'ruby', 'go']]) == [4, 3]
    assert candidate(req_skills = ['linux', 'windows', 'macos', 'docker'],people = [['linux'], ['windows'], ['macos'], ['docker'], ['linux', 'windows'], ['macos', 'docker'], ['linux', 'macos'], ['windows', 'docker'], ['linux', 'macos', 'docker'], ['windows', 'macos', 'docker'], ['linux', 'windows', 'docker'], ['linux', 'windows', 'macos', 'docker']]) == [11]
    assert candidate(req_skills = ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience'],people = [['sql', 'nosql'], ['bigdata', 'machinelearning'], ['datascience'], ['sql', 'bigdata'], ['nosql', 'machinelearning'], ['bigdata', 'datascience'], ['machinelearning', 'datascience'], ['sql', 'nosql', 'bigdata', 'machinelearning', 'datascience']]) == [7]
    assert candidate(req_skills = ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws'],people = [['git', 'docker'], ['jenkins', 'travis'], ['circleci', 'aws'], ['git', 'travis'], ['docker', 'circleci'], ['jenkins', 'aws'], ['git', 'docker', 'jenkins', 'travis', 'circleci', 'aws']]) == [6]
    assert candidate(req_skills = ['mongodb', 'postgresql', 'mysql', 'oracle'],people = [['mongodb'], ['postgresql'], ['mysql'], ['oracle'], ['mongodb', 'postgresql'], ['mysql', 'oracle'], ['mongodb', 'mysql'], ['postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql'], ['postgresql', 'mysql', 'oracle'], ['mongodb', 'mysql', 'oracle'], ['mongodb', 'postgresql', 'oracle'], ['mongodb', 'postgresql', 'mysql', 'oracle']]) == [12]
    assert candidate(req_skills = ['communication', 'problem_solving', 'critical_thinking', 'leadership'],people = [['communication'], ['problem_solving'], ['critical_thinking'], ['leadership'], ['communication', 'problem_solving'], ['critical_thinking', 'leadership'], ['communication', 'critical_thinking'], ['problem_solving', 'leadership'], ['communication', 'problem_solving', 'critical_thinking'], ['communication', 'problem_solving', 'leadership'], ['communication', 'critical_thinking', 'leadership'], ['problem_solving', 'critical_thinking', 'leadership'], ['communication', 'problem_solving', 'critical_thinking', 'leadership']]) == [12]
    assert candidate(req_skills = ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision'],people = [['image_processing'], ['natural_language_processing'], ['deep_learning'], ['computer_vision'], ['image_processing', 'natural_language_processing'], ['deep_learning', 'computer_vision'], ['image_processing', 'deep_learning'], ['natural_language_processing', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning'], ['natural_language_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'deep_learning', 'computer_vision'], ['image_processing', 'natural_language_processing', 'deep_learning', 'computer_vision']]) == [11]
    assert candidate(req_skills = ['java', 'spring', 'hibernate', 'react'],people = [['java'], ['spring'], ['hibernate'], ['react'], ['java', 'spring'], ['spring', 'hibernate'], ['hibernate', 'react'], ['java', 'react'], ['java', 'spring', 'hibernate'], ['java', 'spring', 'react'], ['spring', 'hibernate', 'react'], ['java', 'spring', 'hibernate', 'react']]) == [11]
    assert candidate(req_skills = ['sql', 'python', 'frontend', 'backend'],people = [['sql'], ['python'], ['frontend'], ['backend'], ['sql', 'python'], ['frontend', 'backend']]) == [5, 4]
    assert candidate(req_skills = ['python', 'java', 'c++', 'ruby'],people = [['python'], ['java'], ['c++'], ['ruby'], ['python', 'java'], ['c++', 'ruby'], ['python', 'c++'], ['java', 'ruby']]) == [5, 4]
    assert candidate(req_skills = ['aws', 'azure', 'gcp'],people = [['aws', 'azure'], ['gcp'], ['aws'], ['azure', 'gcp'], ['aws', 'gcp'], ['azure'], ['aws', 'azure', 'gcp']]) == [6]
    assert candidate(req_skills = ['data_science', 'data_engineering', 'ai', 'ml'],people = [['data_science'], ['data_engineering'], ['ai'], ['ml'], ['data_science', 'data_engineering'], ['ai', 'ml'], ['data_science', 'ai'], ['data_engineering', 'ml'], ['data_science', 'data_engineering', 'ai'], ['data_engineering', 'ai', 'ml'], ['data_science', 'ai', 'ml'], ['data_science', 'data_engineering', 'ai', 'ml']]) == [11]
    assert candidate(req_skills = ['security', 'testing', 'projectmanagement', 'communication', 'design'],people = [['security'], ['testing'], ['projectmanagement'], ['communication'], ['design'], ['security', 'testing'], ['projectmanagement', 'communication'], ['design', 'security'], ['testing', 'communication'], ['security', 'projectmanagement', 'design'], ['testing', 'communication', 'design']]) == [9, 8]
    assert candidate(req_skills = ['coding', 'debugging', 'testing', 'design'],people = [['coding', 'debugging'], ['testing'], ['design'], ['coding', 'testing'], ['debugging', 'design']]) == [4, 3]
    assert candidate(req_skills = ['photoshop', 'illustrator', 'indesign', 'lightroom'],people = [['photoshop', 'illustrator'], ['indesign'], ['lightroom'], ['photoshop', 'indesign'], ['illustrator', 'lightroom'], ['photoshop', 'lightroom'], ['indesign', 'lightroom'], ['photoshop', 'illustrator', 'indesign'], ['illustrator', 'indesign', 'lightroom'], ['photoshop', 'indesign', 'lightroom'], ['photoshop', 'illustrator', 'lightroom'], ['photoshop', 'illustrator', 'indesign', 'lightroom']]) == [11]
    assert candidate(req_skills = ['algorithm', 'data-structures', 'database', 'networking', 'os'],people = [['algorithm', 'data-structures'], ['database'], ['networking'], ['os'], ['algorithm', 'os'], ['data-structures', 'networking'], ['database', 'os'], ['algorithm', 'data-structures', 'database'], ['networking', 'os'], ['algorithm', 'networking', 'os']]) == [8, 7]
    assert candidate(req_skills = ['security', 'analytics', 'ml', 'devops'],people = [['security'], ['analytics'], ['ml'], ['devops'], ['security', 'analytics'], ['ml', 'devops'], ['security', 'ml'], ['analytics', 'devops'], ['security', 'analytics', 'ml'], ['security', 'analytics', 'devops'], ['security', 'ml', 'devops'], ['analytics', 'ml', 'devops'], ['security', 'analytics', 'ml', 'devops']]) == [12]
    assert candidate(req_skills = ['sql', 'no_sql', 'big_data', 'cloud_computing'],people = [['sql'], ['no_sql'], ['big_data'], ['cloud_computing'], ['sql', 'no_sql'], ['big_data', 'cloud_computing'], ['sql', 'big_data'], ['no_sql', 'cloud_computing'], ['sql', 'no_sql', 'big_data'], ['no_sql', 'big_data', 'cloud_computing'], ['sql', 'big_data', 'cloud_computing'], ['sql', 'no_sql', 'cloud_computing']]) == [9, 0]
    assert candidate(req_skills = ['coding', 'debugging', 'design', 'deployment'],people = [['coding', 'debugging'], ['design'], ['deployment'], ['coding', 'deployment'], ['design', 'debugging']]) == [3, 4]
    assert candidate(req_skills = ['sql', 'nosql', 'bigdata', 'cloud', 'devops'],people = [['sql'], ['nosql'], ['bigdata'], ['cloud'], ['devops'], ['sql', 'nosql'], ['bigdata', 'cloud'], ['devops', 'sql'], ['nosql', 'cloud'], ['bigdata', 'devops'], ['sql', 'cloud'], ['nosql', 'devops'], ['bigdata', 'sql'], ['cloud', 'devops'], ['sql', 'nosql', 'cloud'], ['bigdata', 'sql', 'cloud'], ['nosql', 'cloud', 'devops']]) == [16, 12]
    assert candidate(req_skills = ['python', 'cpp', 'java', 'javascript'],people = [['python', 'cpp'], ['java'], ['javascript', 'java'], ['cpp', 'python'], ['cpp', 'java'], ['javascript']]) == [2, 0]
    assert candidate(req_skills = ['coding', 'debugging', 'testing', 'deployment'],people = [['coding'], ['debugging'], ['testing'], ['deployment'], ['coding', 'debugging'], ['testing', 'deployment'], ['coding', 'testing'], ['debugging', 'deployment'], ['coding', 'debugging', 'testing'], ['debugging', 'testing', 'deployment'], ['coding', 'debugging', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'debugging', 'testing', 'deployment']]) == [12]
    assert candidate(req_skills = ['networking', 'security', 'project_management', 'budgeting'],people = [['networking'], ['security'], ['project_management'], ['budgeting'], ['networking', 'security'], ['project_management', 'budgeting'], ['networking', 'project_management'], ['security', 'budgeting'], ['networking', 'project_management', 'budgeting'], ['networking', 'security', 'project_management', 'budgeting']]) == [9]
    assert candidate(req_skills = ['aws', 'azure', 'gcp', 'docker', 'kubernetes'],people = [['aws', 'azure'], ['gcp', 'docker'], ['kubernetes'], ['aws', 'docker'], ['azure', 'gcp'], ['aws', 'gcp', 'kubernetes']]) == [5, 3, 0]
    assert candidate(req_skills = ['coding', 'testing', 'documentation', 'deployment'],people = [['coding', 'testing'], ['documentation', 'deployment'], ['coding', 'documentation'], ['testing', 'deployment'], ['coding', 'testing', 'documentation'], ['testing', 'documentation', 'deployment'], ['coding', 'documentation', 'deployment'], ['coding', 'testing', 'deployment'], ['coding', 'testing', 'documentation', 'deployment']]) == [8]
    assert candidate(req_skills = ['html', 'css', 'javascript', 'react', 'nodejs'],people = [['html', 'css'], ['javascript'], ['react', 'nodejs'], ['html', 'javascript'], ['css', 'nodejs'], ['react'], ['html', 'javascript', 'react']]) == [4, 6]
    assert candidate(req_skills = ['product', 'design', 'backend', 'frontend', 'testing'],people = [['product'], ['design'], ['backend'], ['frontend'], ['testing'], ['product', 'design'], ['backend', 'frontend'], ['testing', 'product'], ['design', 'backend'], ['frontend', 'testing'], ['product', 'backend', 'frontend', 'testing'], ['design', 'backend', 'frontend', 'testing']]) == [11, 0]
    assert candidate(req_skills = ['docker', 'kubernetes', 'aws', 'gcp'],people = [['docker'], ['kubernetes'], ['aws'], ['gcp'], ['docker', 'kubernetes'], ['aws', 'gcp'], ['docker', 'aws'], ['kubernetes', 'gcp']]) == [5, 4]
    assert candidate(req_skills = ['linux', 'windows', 'macos', 'unix'],people = [['linux'], ['windows'], ['macos'], ['unix'], ['linux', 'windows'], ['macos', 'unix'], ['linux', 'macos'], ['windows', 'unix'], ['linux', 'unix'], ['windows', 'macos'], ['linux', 'macos', 'unix'], ['linux', 'windows', 'unix'], ['windows', 'macos', 'unix'], ['linux', 'windows', 'macos'], ['linux', 'windows', 'macos', 'unix']]) == [14]
    assert candidate(req_skills = ['python', 'javascript', 'typescript', 'react', 'angular', 'vue'],people = [['python'], ['javascript'], ['typescript'], ['react'], ['angular'], ['vue'], ['python', 'javascript'], ['typescript', 'react'], ['angular', 'vue'], ['python', 'react'], ['javascript', 'vue']]) == [8, 7, 6]
    assert candidate(req_skills = ['html', 'css', 'javascript', 'react'],people = [['html', 'css'], ['javascript'], ['react'], ['css', 'javascript'], ['html', 'react'], ['html', 'css', 'javascript', 'react']]) == [5]
    assert candidate(req_skills = ['algorithm', 'data_structure', 'design_patterns', 'software_architecture'],people = [['algorithm'], ['data_structure'], ['design_patterns'], ['software_architecture'], ['algorithm', 'data_structure'], ['design_patterns', 'software_architecture'], ['algorithm', 'design_patterns'], ['data_structure', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns'], ['algorithm', 'data_structure', 'software_architecture'], ['algorithm', 'design_patterns', 'software_architecture'], ['data_structure', 'design_patterns', 'software_architecture'], ['algorithm', 'data_structure', 'design_patterns', 'software_architecture']]) == [12]
    assert candidate(req_skills = ['frontend', 'backend', 'devops', 'qa'],people = [['frontend'], ['backend'], ['devops'], ['qa'], ['frontend', 'backend'], ['devops', 'qa'], ['frontend', 'devops'], ['backend', 'qa'], ['frontend', 'devops', 'qa'], ['backend', 'devops', 'qa'], ['frontend', 'backend', 'devops'], ['frontend', 'backend', 'qa'], ['frontend', 'backend', 'devops', 'qa']]) == [12]
    assert candidate(req_skills = ['machine-learning', 'deep-learning', 'neural-networks', 'cv', 'nlp'],people = [['machine-learning'], ['deep-learning'], ['neural-networks'], ['cv'], ['nlp'], ['machine-learning', 'deep-learning'], ['neural-networks', 'cv'], ['nlp', 'machine-learning'], ['deep-learning', 'cv'], ['neural-networks', 'nlp'], ['machine-learning', 'cv'], ['deep-learning', 'nlp'], ['machine-learning', 'neural-networks'], ['deep-learning', 'neural-networks'], ['cv', 'nlp'], ['machine-learning', 'deep-learning', 'cv'], ['neural-networks', 'cv', 'nlp'], ['machine-learning', 'deep-learning', 'nlp'], ['neural-networks', 'deep-learning', 'cv', 'nlp'], ['machine-learning', 'neural-networks', 'cv', 'nlp']]) == [18, 0]
    assert candidate(req_skills = ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment'],people = [['network_security'], ['cyber_security'], ['penetration_testing'], ['vulnerability_assessment'], ['network_security', 'cyber_security'], ['penetration_testing', 'vulnerability_assessment'], ['network_security', 'penetration_testing'], ['cyber_security', 'vulnerability_assessment'], ['network_security', 'vulnerability_assessment'], ['cyber_security', 'penetration_testing'], ['network_security', 'cyber_security', 'penetration_testing', 'vulnerability_assessment']]) == [10]
    assert candidate(req_skills = ['front_end', 'back_end', 'database', 'cloud_services'],people = [['front_end'], ['back_end'], ['database'], ['cloud_services'], ['front_end', 'back_end'], ['database', 'cloud_services'], ['front_end', 'database'], ['back_end', 'cloud_services'], ['front_end', 'back_end', 'database'], ['front_end', 'back_end', 'cloud_services'], ['front_end', 'database', 'cloud_services'], ['back_end', 'database', 'cloud_services'], ['front_end', 'back_end', 'database', 'cloud_services']]) == [12]
    assert candidate(req_skills = ['data_science', 'machine_learning', 'deep_learning', 'computer_vision'],people = [['data_science'], ['machine_learning'], ['deep_learning'], ['computer_vision'], ['machine_learning', 'deep_learning'], ['data_science', 'computer_vision'], ['data_science', 'machine_learning'], ['data_science', 'deep_learning'], ['machine_learning', 'computer_vision'], ['deep_learning', 'computer_vision']]) == [9, 6]
    assert candidate(req_skills = ['python', 'javascript', 'html', 'css', 'react', 'nodejs'],people = [['python'], ['javascript'], ['html'], ['css'], ['react'], ['nodejs'], ['python', 'javascript'], ['html', 'css'], ['react', 'nodejs'], ['python', 'html', 'css'], ['javascript', 'react', 'nodejs']]) == [10, 9]
    assert candidate(req_skills = ['machine_learning', 'deep_learning', 'cv', 'nlp'],people = [['machine_learning', 'deep_learning'], ['cv'], ['nlp'], ['deep_learning', 'cv'], ['machine_learning', 'nlp'], ['deep_learning', 'nlp', 'cv'], ['machine_learning', 'deep_learning', 'cv', 'nlp']]) == [6]
    assert candidate(req_skills = ['ux', 'ui', 'product', 'design', 'marketing'],people = [['ux'], ['ui'], ['product'], ['design'], ['marketing'], ['ux', 'ui'], ['product', 'design'], ['marketing', 'ux'], ['ui', 'product'], ['design', 'marketing'], ['ux', 'product'], ['ui', 'marketing'], ['product', 'design', 'marketing'], ['ux', 'ui', 'design'], ['ui', 'product', 'design'], ['ux', 'product', 'marketing'], ['ux', 'ui', 'product', 'design', 'marketing']]) == [16]
    assert candidate(req_skills = ['python', 'javascript', 'cpp', 'go'],people = [['python', 'cpp'], ['javascript'], ['go'], ['python', 'javascript', 'go'], ['cpp', 'javascript']]) == [3, 0]


