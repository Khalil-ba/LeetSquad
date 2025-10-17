def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(expression = "!(!(t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(!(t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(t,t,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(t,t,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,f,f,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,f,f,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,t,t,t,t,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,t,t,t,t,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(&(t,f),|(t,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(&(t,f),|(t,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,t),&(t,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,t),&(t,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f),&(f,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f),&(f,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(f,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(f,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,t,f,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,t,f,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(f)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(f)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,t)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,t)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(!(t),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(!(t),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f),&(f,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f),&(f,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,|(f,f,f,t),!(&(f,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,|(f,f,f,t),!(&(f,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,t,t,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,t,t,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(t),|(f)),&(t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(t),|(f)),&(t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,f,f,f,f,f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,f,f,f,f,f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "t") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "t") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(t,f)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(t,f)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "f") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "f") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(t,f),&(f,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(t,f),&(f,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(t)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(t)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f),t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f),t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(!(!(t)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(!(!(t)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(f,t),|(t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(f,t),|(t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),&(f,t),|(t,t),&(f,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),&(f,t),|(t,t),&(f,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(t,f,t,f)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(t,f,t,f)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,t,t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,t,t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),|(f,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),|(f,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,&(t,f),|(f,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,&(t,f),|(f,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),&(f,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),&(f,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f),|(t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f),|(t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,!(t),&(|(f,f),|(t,t)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,!(t),&(|(f,f),|(t,t)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(|(|(t,f),f),t),!(f),&(t,!(f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(|(|(t,f),f),t),!(f),&(t,!(f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,|(f,f),t),&(f,!(t),t),|(t,f,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,|(f,f),t),&(f,!(t),t),|(t,f,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,t,f),&(t,f)),|(t,t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,t,f),&(t,f)),|(t,t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,&(f,f),t),&(f,|(t,f),t),|(&(f,t),f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,&(f,f),t),&(f,|(t,f),t),|(&(f,t),f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,|(f,f,f)),!(|(t,t,t)),&(f,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,|(f,f,f)),!(|(t,t,t)),&(f,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(&(t,f),&(f,f)),&(t,!(t)),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(&(t,f),&(f,f)),&(t,!(t)),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t,f,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t,f,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,|(f,!(t),&(t,f,t,t),|(f,f,f,f)),&(f,|(t,f,t,t,t)),!(f,|(t,f,f,f,f)),&(t,t,t),t)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,|(f,!(t),&(t,f,t,t),|(f,f,f,f)),&(f,|(t,f,t,t,t)),!(f,|(t,f,f,f,f)),&(t,t,t),t)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f),&(f,t),|(t,t),|(f,f),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f),&(f,t),|(t,t),|(f,f),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f,t)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f,t)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,!(f)),&(f,!(t)),&(t,t),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,!(f)),&(f,!(t)),&(t,t),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,!(t),&(t,f),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,!(t),&(t,f),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(f,t),|(t,f),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(f,t),|(t,f),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,t),&(f,f)),|(t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,t),&(f,f)),|(t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,t),!(t),|(f,f,f),&(|(t,f),f),|(t,t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,t),!(t),|(f,f,f),&(|(t,f),f),|(t,t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(t,f,f),f),|(t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(t,f,f),f),|(t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,!(t),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t),&(t,|(f,f,f),t),&(t,f,f,t),|(t,!(f),f),f,!(t),&(f,t,f),|(t,f,t),f,!(t),&(f,t,f),|(t,f,t),f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,!(t),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t),&(t,|(f,f,f),t),&(t,f,f,t),|(t,!(f),f),f,!(t),&(f,t,f),|(t,f,t),f,!(t),&(f,t,f),|(t,f,t),f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(f,t),f),f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(f,t),f),f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,!(f),&(t,f),|(t,t,f,f),&(t,t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,!(f),&(t,f),|(t,t,f,f),&(t,t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,t),!(t),|(f,t,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,t),!(t),|(f,t,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(t,f),&(f,f)),&(t,t),f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(t,f),&(f,f)),&(t,t),f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,!(t),|(f,f,t),&(t,t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,!(t),|(f,f,t),&(t,t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,|(f,!(t),&(t,f,t),|(f,f,f)),&(f,|(t,f,t,t)),!(f,|(t,f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,|(f,!(t),&(t,f,t),|(f,f,f)),&(f,|(t,f,t,t)),!(f,|(t,f)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(t,f),f),&(t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(t,f),f),&(t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,|(f,!(t),&(t,f)),&(f,|(t,f,t)),!(f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,|(f,!(t),&(t,f)),&(f,|(t,f,t)),!(f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(&(t,t),&(t,|(t,t)),&(t,|(t,|(t,t))),&(t,|(t,|(t,|(t,t)))))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(&(t,t),&(t,|(t,t)),&(t,|(t,|(t,t))),&(t,|(t,|(t,|(t,t)))))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,t),&(t,f)),|(f,f,f,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,t),&(t,f)),|(f,f,f,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,t),!(t),|(f,f,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,t),!(t),|(f,f,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,|(&(f,t),f),|(t,t),!(&(f,t)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,|(&(f,t),f),|(t,t),!(&(f,t)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(|(f,t),f),&(f,t,f,t)),|(f,f,f,f,f,t,t),&(t,t,t,t,t,t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(|(f,t),f),&(f,t,f,t)),|(f,f,f,f,f,t,t),&(t,t,t,t,t,t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t),&(t,t,t,t,t,t,t,t),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t),&(t,t,t,t,t,t,t,t),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(|(|(f),f),t),&(t,f,t),!(f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(|(|(f),f),t),&(t,f,t),!(f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(t,f),&(f,t)),|(t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(t,f),&(f,t)),|(t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,t,t),&(t,t,t),&(f,f,f),|(t,t,t),|(f,f,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,t,t),&(t,t,t),&(f,f,f),|(t,t,t),|(f,f,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(!(f),t),|(f,&(t,f),f),&(t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(!(f),t),|(f,&(t,f),f),&(t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,!(f),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,!(f),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,!(f),&(f,t)),|(t,!(t),&(f,f)),|(t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,!(f),&(f,t)),|(t,!(t),&(f,f)),|(t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,!(t)),f,!(f),t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,!(t)),f,!(f),t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(&(t,t),&(f,f)),|(&(t,f),&(t,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(&(t,t),&(f,f)),|(&(t,f),&(t,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,|(&(f,t),f),|(t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,|(&(f,t),f),|(t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,!(t)),f,!(f),t,!(|(&(f,t),f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,!(t)),f,!(f),t,!(|(&(f,t),f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(f,|(&(t,f),f),&(t,t,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(f,|(&(t,f),f),&(t,t,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,&(|(t,f),&(t,f)),|(t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,&(|(t,f),&(t,f)),|(t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(t,!(f),|(&(t,t),|(f,f)),&(|(t,f),f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(t,!(f),|(&(t,t),|(f,f)),&(|(t,f),f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f,t))),|(f,!(t),&(t,f,t)),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f,t))),|(f,!(t),&(t,f,t)),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),&(t,f),|(t,t),|(f,f),&(t,!(f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),&(t,f),|(t,t),|(f,f),&(t,!(f)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(f),f),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(f),f),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t),!(&(t,!(t))))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t),!(&(t,!(t))))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(|(|(t),f),t),f),&(t,!(f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(|(|(t),f),t),f),&(t,!(f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(|(|(|(|(|(f),f),f),f),f),f),f),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(|(|(|(|(|(f),f),f),f),f),f),f),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(|(|(|(t),f),t),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f)") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(|(|(|(t),f),t),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f)") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,&(|(f,f),t),&(f,|(t,f),f),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,&(|(f,f),t),&(f,|(t,f),f),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(|(t,f),f),&(t,!(f)),!(|(t,f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(|(t,f),f),&(t,!(f)),!(|(t,f)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,f),|(t,f,t),&(t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,f),|(t,f,t),&(t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,&(f,t)),|(t,|(f,f)),&(t,|(t,|(f,t))),|(t,&(f,|(f,t))))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,&(f,t)),|(t,|(f,f)),&(t,|(t,|(f,t))),|(t,&(f,|(f,t))))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(f,&(t,|(t,f)),!(t)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(f,&(t,|(t,f)),!(t)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(t,f),&(f,f)),!(|(t,t,t,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(t,f),&(f,f)),!(|(t,t,t,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,t),&(f,f,f),!(t),|(t,f,f,f,t),&(f,t,t,f))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,t),&(f,f,f),!(t),|(t,f,f,f,t),&(f,t,t,f))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(t,|(f,t)),t),&(f,!(t),t)),|(t,!(f),&(f,f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(t,|(f,t)),t),&(f,!(t),t)),|(t,!(f),&(f,f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(f,f,f,t),|(t,f,t,f),&(t,t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(f,f,f,t),|(t,f,t,f),&(t,t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(f,&(t,|(f,t),&(f,f)),!(f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(f,&(t,|(f,t),&(f,f)),!(f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),&(t,t,t,t,t,t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),&(t,t,t,t,t,t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),!(f),&(t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),!(f),&(t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(t,&(|(f,f),&(t,f)),&(t,|(t,f),&(f,f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(t,&(|(f,f),&(t,f)),&(t,|(t,f),&(f,f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(&(f,t),|(t,f),&(f,f),|(t,t),&(t,f),|(f,f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(&(f,t),|(t,f),&(f,f),|(t,t),&(t,f),|(f,f)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,t,t,t),|(|(f,f),f),&(t,f,f,t,t),!(t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,t,t,t),|(|(f,f),f),&(t,f,f,t,t),!(t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(f,t),&(t,f),|(t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(f,t),&(t,f),|(t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(f,f,f),&(t,t,t),!(|(f,f)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(f,f,f),&(t,t,t),!(|(f,f)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(f,f),t),f),|(f,|(t,f),&(f,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(f,f),t),f),|(f,|(t,f),&(f,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,t,t,t),|(f,f,f,f),&(t,f,t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,t,t,t),|(f,f,f,f),&(t,f,t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f,!(t)),&(t,f,t),&(f,!(t)),!(f),t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f,!(t)),&(t,f,t),&(f,!(t)),!(f),t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)),!(|(t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)),!(|(t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(t,!(f),&(t,t),|(t,f),&(t,!(t),&(f,f))))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(t,!(f),&(t,t),|(t,f),&(t,!(t),&(f,f))))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(f,f),&(t,t),&(t,f)),|(t,!(t),&(t,f)),&(t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(f,f),&(t,t),&(t,f)),|(t,!(t),&(t,f)),&(t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f),!(t))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f),!(t))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(t,f),&(t,t,t),!(f),&(f,!(t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(t,f),&(t,t,t),!(f),&(f,!(t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(!(!(!(!(t)))))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(!(!(!(!(t)))))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)),&(f,|(t,f)),|(f,|(t,f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)),&(f,|(t,f)),|(f,|(t,f)))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,|(t,|(f,!(t))))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,|(t,|(f,!(t))))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(|(|(f),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(|(|(f),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(&(t,t),|(f,f),&(f,t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(&(t,t),|(f,f),&(f,t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(t,f),f),&(t,|(t,f))),|(t,!(f),t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(t,f),f),&(t,|(t,f))),|(t,!(f),t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f))),|(f,!(t)))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f))),|(f,!(t)))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "&(f,&(|(f,f,t),!(t),|(f,f,f)),|(f,&(t,|(f,t),&(f,f)),!(f)),!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f))))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "&(f,&(|(f,f,t),!(t),|(f,f,f)),|(f,&(t,|(f,t),&(f,f)),!(f)),!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f))))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(&(f,t,f),|(t,f,t),&(t,t,t,t,t))") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(&(f,t,f),|(t,f,t),&(t,t,t,t,t))") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "|(|(|(t,f),f),&(|(t,t),&(f,t))),!(t)") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "|(|(|(t,f),f),&(|(t,t),&(f,t))),!(t)") == True: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(t,!(t),&(t,!(f))))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(t,!(t),&(t,!(f))))") == False: {e}')
    
    total += 1
    try:
        result = candidate(expression = "!(|(&(t,!(t)),&(f,!(f)),&(t,t),!(f)))") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(expression = "!(|(&(t,!(t)),&(f,!(f)),&(t,t),!(f)))") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(expression = "!(!(t))") == True
    assert candidate(expression = "|(t,t,t)") == True
    assert candidate(expression = "|(f,f,f,t)") == True
    assert candidate(expression = "&(t,t,t,t,t,t)") == True
    assert candidate(expression = "!(&(&(t,f),|(t,t)))") == True
    assert candidate(expression = "&(|(f,t),&(t,f))") == False
    assert candidate(expression = "!(|(t,t))") == False
    assert candidate(expression = "|(&(t,f),&(f,t))") == False
    assert candidate(expression = "!(&(f,t))") == True
    assert candidate(expression = "|(f,t,f,t)") == True
    assert candidate(expression = "!(f)") == True
    assert candidate(expression = "&(f,t)") == False
    assert candidate(expression = "&(!(t),f)") == False
    assert candidate(expression = "!(&(|(f),&(f,t)))") == True
    assert candidate(expression = "&(t,|(f,f,f,t),!(&(f,t)))") == True
    assert candidate(expression = "&(t,t,t,t)") == True
    assert candidate(expression = "&(|(f))") == False
    assert candidate(expression = "!(&(|(t),|(f)),&(t,f))") == True
    assert candidate(expression = "|(f,f,f,f,f,f)") == False
    assert candidate(expression = "t") == True
    assert candidate(expression = "|(t,f)") == True
    assert candidate(expression = "f") == False
    assert candidate(expression = "|(|(t,f),&(f,f))") == True
    assert candidate(expression = "!(t)") == False
    assert candidate(expression = "|(&(t,f),t)") == True
    assert candidate(expression = "!(!(!(t)))") == False
    assert candidate(expression = "|(&(f,t),|(t,f))") == True
    assert candidate(expression = "&(|(t,f),&(f,t),|(t,t),&(f,f))") == False
    assert candidate(expression = "|(t,f,t,f)") == True
    assert candidate(expression = "&(t,t,t)") == True
    assert candidate(expression = "&(|(t,f),|(f,t))") == True
    assert candidate(expression = "|(f,&(t,f),|(f,f))") == False
    assert candidate(expression = "&(|(t,f),&(f,t))") == False
    assert candidate(expression = "|(&(t,f),|(t,t))") == True
    assert candidate(expression = "|(f,!(t),&(|(f,f),|(t,t)))") == False
    assert candidate(expression = "&(|(|(|(t,f),f),t),!(f),&(t,!(f)))") == True
    assert candidate(expression = "|(&(t,|(f,f),t),&(f,!(t),t),|(t,f,f))") == True
    assert candidate(expression = "!(&(|(f,t,f),&(t,f)),|(t,t,f))") == True
    assert candidate(expression = "&(|(t,&(f,f),t),&(f,|(t,f),t),|(&(f,t),f))") == False
    assert candidate(expression = "|(&(t,|(f,f,f)),!(|(t,t,t)),&(f,f))") == False
    assert candidate(expression = "&(|(&(t,f),&(f,f)),&(t,!(t)),f)") == False
    assert candidate(expression = "&(|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f),|(f,t),&(t,f))") == False
    assert candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t,f,t))") == False
    assert candidate(expression = "&(t,|(f,!(t),&(t,f,t,t),|(f,f,f,f)),&(f,|(t,f,t,t,t)),!(f,|(t,f,f,f,f)),&(t,t,t),t)") == False
    assert candidate(expression = "|(&(t,f),&(f,t),|(t,t),|(f,f),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)))") == True
    assert candidate(expression = "|(&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f),&(f,t),&(t,f))") == False
    assert candidate(expression = "|(|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f,t)") == False
    assert candidate(expression = "|(&(t,!(f)),&(f,!(t)),&(t,t),!(f))") == True
    assert candidate(expression = "|(f,!(t),&(t,f),!(f))") == True
    assert candidate(expression = "|(&(f,t),|(t,f),!(f))") == True
    assert candidate(expression = "!(&(|(f,t),&(f,f)),|(t,t,t))") == True
    assert candidate(expression = "&(|(f,f,t),!(t),|(f,f,f),&(|(t,f),f),|(t,t,t))") == False
    assert candidate(expression = "!(&(|(t,f,f),f),|(t,t,t))") == True
    assert candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t))") == False
    assert candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t))") == False
    assert candidate(expression = "!(&(|(f,!(t),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t),&(t,|(f,f,f),t),&(t,f,f,t),|(t,!(f),f),f,!(t),&(f,t,f),|(t,f,t),f,!(t),&(f,t,f),|(t,f,t),f))") == True
    assert candidate(expression = "!(&(|(&(f,t),f),f))") == True
    assert candidate(expression = "|(f,!(f),&(t,f),|(t,t,f,f),&(t,t,t,t))") == True
    assert candidate(expression = "&(|(f,f,t),!(t),|(f,t,f))") == False
    assert candidate(expression = "!(&(|(&(t,f),&(f,f)),&(t,t),f))") == True
    assert candidate(expression = "&(f,!(t),|(f,f,t),&(t,t,t))") == False
    assert candidate(expression = "&(t,|(f,!(t),&(t,f,t),|(f,f,f)),&(f,|(t,f,t,t)),!(f,|(t,f)))") == False
    assert candidate(expression = "!(&(|(t,f),f),&(t,t,t))") == True
    assert candidate(expression = "&(t,|(f,!(t),&(t,f)),&(f,|(t,f,t)),!(f))") == False
    assert candidate(expression = "&(&(t,t),&(t,|(t,t)),&(t,|(t,|(t,t))),&(t,|(t,|(t,|(t,t)))))") == True
    assert candidate(expression = "!(&(|(f,t),&(t,f)),|(f,f,f,f))") == True
    assert candidate(expression = "&(|(f,f,t),!(t),|(f,f,f))") == False
    assert candidate(expression = "&(f,|(&(f,t),f),|(t,t),!(&(f,t)))") == False
    assert candidate(expression = "!(&(|(|(f,t),f),&(f,t,f,t)),|(f,f,f,f,f,t,t),&(t,t,t,t,t,t,t,t))") == True
    assert candidate(expression = "&(f,!(t),|(&(t,!(t)),|(t,f,f,t,f)),&(f,f,t,t,t,t),&(t,t,t,t,t,t,t,t),f)") == False
    assert candidate(expression = "&(|(|(|(f),f),t),&(t,f,t),!(f))") == False
    assert candidate(expression = "!(&(|(t,f),&(f,t)),|(t,t))") == True
    assert candidate(expression = "&(|(t,t,t),&(t,t,t),&(f,f,f),|(t,t,t),|(f,f,f))") == False
    assert candidate(expression = "!(&(!(f),t),|(f,&(t,f),f),&(t,f))") == True
    assert candidate(expression = "&(|(t,!(f),&(t,f)),!(|(f,f,t)),&(t,f),|(f,t,t,t))") == False
    assert candidate(expression = "&(|(t,!(f),&(f,t)),|(t,!(t),&(f,f)),|(t,t))") == True
    assert candidate(expression = "|(&(t,!(t)),f,!(f),t)") == True
    assert candidate(expression = "!(&(&(t,t),&(f,f)),|(&(t,f),&(t,t)))") == True
    assert candidate(expression = "&(f,|(&(f,t),f),|(t,t))") == False
    assert candidate(expression = "|(&(t,!(t)),f,!(f),t,!(|(&(f,t),f)))") == True
    assert candidate(expression = "!(&(f,|(&(t,f),f),&(t,t,t)))") == True
    assert candidate(expression = "|(f,&(|(t,f),&(t,f)),|(t,f))") == True
    assert candidate(expression = "&(t,!(f),|(&(t,t),|(f,f)),&(|(t,f),f))") == False
    assert candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f,t))),|(f,!(t),&(t,f,t)),!(f))") == True
    assert candidate(expression = "&(|(t,f),&(t,f),|(t,t),|(f,f),&(t,!(f)))") == False
    assert candidate(expression = "|(|(|(f),f),f)") == False
    assert candidate(expression = "&(f,!(t),&(t,!(f)),|(f,t),!(&(t,!(t))))") == False
    assert candidate(expression = "|(|(|(|(|(t),f),t),f),&(t,!(f)))") == True
    assert candidate(expression = "|(|(|(|(|(|(|(|(f),f),f),f),f),f),f),f)") == False
    assert candidate(expression = "!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f)))") == True
    assert candidate(expression = "&(|(|(|(|(t),f),t),f),&(t,t,t,t,t,t,t,t),|(t,f,f,t,f),&(f,f,t,t,t,t,f,t),f)") == False
    assert candidate(expression = "|(f,&(|(f,f),t),&(f,|(t,f),f),!(f))") == True
    assert candidate(expression = "&(|(|(t,f),f),&(t,!(f)),!(|(t,f)))") == False
    assert candidate(expression = "&(|(f,f,f),|(t,f,t),&(t,t))") == False
    assert candidate(expression = "&(|(t,&(f,t)),|(t,|(f,f)),&(t,|(t,|(f,t))),|(t,&(f,|(f,t))))") == True
    assert candidate(expression = "!(|(f,&(t,|(t,f)),!(t)))") == False
    assert candidate(expression = "!(&(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)))") == True
    assert candidate(expression = "!(&(|(t,f),&(f,f)),!(|(t,t,t,t)))") == True
    assert candidate(expression = "&(|(f,f,t),&(f,f,f),!(t),|(t,f,f,f,t),&(f,t,t,f))") == False
    assert candidate(expression = "!(&(|(&(t,|(f,t)),t),&(f,!(t),t)),|(t,!(f),&(f,f)))") == True
    assert candidate(expression = "&(|(f,f,f,t),|(t,f,t,f),&(t,t,t,t))") == True
    assert candidate(expression = "|(f,&(t,|(f,t),&(f,f)),!(f))") == True
    assert candidate(expression = "|(|(|(|(|(|(|(t),f),t),f),f),f),&(t,t,t,t,t,t,t,t),&(t,t,t,t,t,t,t,t))") == True
    assert candidate(expression = "&(|(t,f),!(f),&(t,t,t))") == True
    assert candidate(expression = "|(t,&(|(f,f),&(t,f)),&(t,|(t,f),&(f,f)))") == True
    assert candidate(expression = "!(|(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)))") == True
    assert candidate(expression = "!(|(&(f,t),|(t,f),&(f,f),|(t,t),&(t,f),|(f,f)))") == False
    assert candidate(expression = "|(&(t,t,t,t),|(|(f,f),f),&(t,f,f,t,t),!(t))") == True
    assert candidate(expression = "|(&(f,t),&(t,f),|(t,t))") == True
    assert candidate(expression = "|(|(f,f,f),&(t,t,t),!(|(f,f)))") == True
    assert candidate(expression = "!(&(|(&(f,f),t),f),|(f,|(t,f),&(f,t)))") == True
    assert candidate(expression = "|(&(t,t,t,t),|(f,f,f,f),&(t,f,t,f))") == True
    assert candidate(expression = "|(&(t,f,!(t)),&(t,f,t),&(f,!(t)),!(f),t)") == True
    assert candidate(expression = "&(|(|(f,t),t),f),&(f,|(t,!(t),f),&(t,t,t,t,t,t)),!(|(t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t))") == False
    assert candidate(expression = "!(&(t,!(f),&(t,t),|(t,f),&(t,!(t),&(f,f))))") == True
    assert candidate(expression = "!(&(|(f,f),&(t,t),&(t,f)),|(t,!(t),&(t,f)),&(t,t))") == True
    assert candidate(expression = "!(&(|(|(|(|(|(f),t),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f),!(t))") == False
    assert candidate(expression = "|(&(t,f),&(t,t,t),!(f),&(f,!(t)))") == True
    assert candidate(expression = "!(!(!(!(!(t)))))") == False
    assert candidate(expression = "&(|(t,f),|(f,t),&(t,t),|(t,t),&(t,f),|(f,t),!(t),!(f),&(t,|(t,t)),|(t,&(t,f)),&(f,|(t,f)),|(f,|(t,f)))") == False
    assert candidate(expression = "&(f,|(t,|(f,!(t))))") == False
    assert candidate(expression = "|(|(|(|(|(f),f),t),&(t,f,t),!(f),|(t,f)),&(f,t,t,f))") == True
    assert candidate(expression = "!(&(&(t,t),|(f,f),&(f,t)))") == True
    assert candidate(expression = "!(&(|(&(t,f),f),&(t,|(t,f))),|(t,!(f),t))") == True
    assert candidate(expression = "!(&(|(&(t,f),t),&(f,|(t,f))),|(f,!(t)))") == True
    assert candidate(expression = "&(f,&(|(f,f,t),!(t),|(f,f,f)),|(f,&(t,|(f,t),&(f,f)),!(f)),!(&(|(f,f,f,t),!(t),|(t,t,t)),|(f,&(t,|(f,t),&(f,f)),!(f))))") == False
    assert candidate(expression = "|(&(f,t,f),|(t,f,t),&(t,t,t,t,t))") == True
    assert candidate(expression = "|(|(|(t,f),f),&(|(t,t),&(f,t))),!(t)") == True
    assert candidate(expression = "!(|(t,!(t),&(t,!(f))))") == False
    assert candidate(expression = "!(|(&(t,!(t)),&(f,!(f)),&(t,t),!(f)))") == False


