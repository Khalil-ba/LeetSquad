def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(pattern = "DDD") == "4321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDD") == "4321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDIDDD") == "123549876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDIDDD") == "123549876": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "ID") == "132"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "ID") == "132": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDD") == "126543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDD") == "126543": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIII") == "321456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIII") == "321456": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDID") == "13254"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDID") == "13254": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIII") == "12345"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIII") == "12345": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DI") == "213"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DI") == "213": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IID") == "1243"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IID") == "1243": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIDDIID") == "321654798"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIDDIID") == "321654798": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDID") == "132547698"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDID") == "132547698": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "I") == "12"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "I") == "12": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DID") == "2143"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DID") == "2143": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIII") == "123456"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIII") == "123456": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDD") == "654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDD") == "654321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "D") == "21"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "D") == "21": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDD") == "54321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDD") == "54321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDDIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDDIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDIDIII") == "432165789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDIDIII") == "432165789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDIIIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDIIIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDIIIII") == "432156789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDIIIII") == "432156789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDDDID") == "176543298"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDDDID") == "176543298": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDDDIDI") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDDDIDI") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIDIDIDIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIDIDIDIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDID") == "124365"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDID") == "124365": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIIIDDDI") == "213487659"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIIIDDDI") == "213487659": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDDDDII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDDDDII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDD") == "87654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDD") == "87654321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIDIDIDI") == "214365879"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIDIDIDI") == "214365879": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDDD") == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDDD") == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDIIDDI") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDIIDDI") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDIIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDIIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDIIII") == "543216789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDIIII") == "543216789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDIDIDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDIDIDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDIDID") == "123547698"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDIDID") == "123547698": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDIIDI") == "154326879"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDIIDI") == "154326879": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDIDDDI") == "124387659"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDIDDDI") == "124387659": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDIDDIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDIDDIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIDIDID") == "21436587"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIDIDID") == "21436587": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIIDDDIDI") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIIDDDIDI") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDIIIIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDIIIIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDIII") == "54321678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDIII") == "54321678": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDID") == "1325476"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDID") == "1325476": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDIDIDI") == "124365879"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDIDIDI") == "124365879": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDI") == "76543218"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDI") == "76543218": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIDDDID") == "321765498"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIDDDID") == "321765498": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIIIIIII") == "213456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIIIIIII") == "213456789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDDDDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDDDDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDIDII") == "154327689"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDIDII") == "154327689": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDIDDDI") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDIDDDI") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDIIIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDIIIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIDIDID") == "321547698"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIDIDID") == "321547698": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDDD") == "123987654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDDD") == "123987654": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDDIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDDIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIIDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIIDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIID") == "12345687"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIID") == "12345687": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIIIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIIIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDDDID") == "132765498"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDDDID") == "132765498": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDIDIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDIDIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIII") == "12345678"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIII") == "12345678": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDDDD") == "321498765"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDDDD") == "321498765": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIID") == "123456798"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIID") == "123456798": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIIDIDID") == "213547698"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIIDIDID") == "213547698": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDIDI") == "321465879"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDIDI") == "321465879": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDIIIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDIIIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDIIII") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDIIII") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDIID") == "126543798"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDIID") == "126543798": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDIII") == "126543789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDIII") == "126543789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDIDIDIDIDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDIDIDIDIDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DIDID") == "214365"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DIDID") == "214365": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDIII") == "654321789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDIII") == "654321789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDII") == "32145"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDII") == "32145": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDIDDDD") == "432198765"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDIDDDD") == "432198765": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDIDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDIDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIDDDDDDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIDDDDDDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDDDD") == "18765432"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDDDD") == "18765432": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDII") == "13245"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDII") == "13245": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDII") == "765432189"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDII") == "765432189": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDDI") == "123876549"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDDI") == "123876549": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDIDID") == "154327698"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDIDID") == "154327698": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIDDI") == "123458769"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIDDI") == "123458769": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDD") == "7654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDD") == "7654321": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDIDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDIDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIDDD") == "123459876"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIDDD") == "123459876": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDIDDDIDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDIDDDIDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIIID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIIID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDDDDDDDDID") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDDDDDDDDID") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDDDIID") == "54321687"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDDDIID") == "54321687": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IDDDIIDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IDDDIIDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDDDDDDDD") == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDDDDDDDD") == None: {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDDID") == "321476598"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDDID") == "321476598": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDDDD") == "129876543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDDDD") == "129876543": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDDII") == "12654378"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDDII") == "12654378": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIIDIDD") == "321465987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIIDIDD") == "321465987": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIDDIIDD") == "125436987"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIDDIIDD") == "125436987": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIIIIII") == "123456789"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIIIIII") == "123456789": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "IIIDDDD") == "12387654"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "IIIDDDD") == "12387654": {e}')
    
    total += 1
    try:
        result = candidate(pattern = "DDIID") == "321465"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(pattern = "DDIID") == "321465": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(pattern = "DDD") == "4321"
    assert candidate(pattern = "IIIDIDDD") == "123549876"
    assert candidate(pattern = "ID") == "132"
    assert candidate(pattern = "IIDDD") == "126543"
    assert candidate(pattern = "DDIII") == "321456"
    assert candidate(pattern = "IDID") == "13254"
    assert candidate(pattern = "IIII") == "12345"
    assert candidate(pattern = "DI") == "213"
    assert candidate(pattern = "IID") == "1243"
    assert candidate(pattern = "DDIDDIID") == "321654798"
    assert candidate(pattern = "IDIDIDID") == "132547698"
    assert candidate(pattern = "I") == "12"
    assert candidate(pattern = "DID") == "2143"
    assert candidate(pattern = "IIIII") == "123456"
    assert candidate(pattern = "DDDDD") == "654321"
    assert candidate(pattern = "D") == "21"
    assert candidate(pattern = "DDDD") == "54321"
    assert candidate(pattern = "DDIIDDIID") == None
    assert candidate(pattern = "IDIDIDIDID") == None
    assert candidate(pattern = "DDDIDIII") == "432165789"
    assert candidate(pattern = "DDDDDDIIIIIIII") == None
    assert candidate(pattern = "DDDIIIII") == "432156789"
    assert candidate(pattern = "IIIIIIIII") == None
    assert candidate(pattern = "IDDDDDID") == "176543298"
    assert candidate(pattern = "IDDDDDIDI") == None
    assert candidate(pattern = "DDIDIDIDIDIDID") == None
    assert candidate(pattern = "IIDID") == "124365"
    assert candidate(pattern = "DIIIDDDI") == "213487659"
    assert candidate(pattern = "DDDDDDDDDD") == None
    assert candidate(pattern = "IIIIIIIIII") == None
    assert candidate(pattern = "IIDDDDDDII") == None
    assert candidate(pattern = "DDIIDIDID") == None
    assert candidate(pattern = "IIIIIIDDD") == None
    assert candidate(pattern = "DDDDDDD") == "87654321"
    assert candidate(pattern = "DIDIDIDI") == "214365879"
    assert candidate(pattern = "IIDDDDDDD") == None
    assert candidate(pattern = "DDDDDDDD") == "987654321"
    assert candidate(pattern = "IIDDIIDDI") == None
    assert candidate(pattern = "IIDDDIIID") == None
    assert candidate(pattern = "DDDDIIII") == "543216789"
    assert candidate(pattern = "DDIIDDDDD") == None
    assert candidate(pattern = "IIDIDIDDD") == None
    assert candidate(pattern = "IIIIIDDDDDD") == None
    assert candidate(pattern = "IDIDIDDDDD") == None
    assert candidate(pattern = "IIIDIDID") == "123547698"
    assert candidate(pattern = "IDDDIIDI") == "154326879"
    assert candidate(pattern = "IIDIDDDI") == "124387659"
    assert candidate(pattern = "IIDDIDDIID") == None
    assert candidate(pattern = "DDDDDDDDDDDD") == None
    assert candidate(pattern = "DIDIDID") == "21436587"
    assert candidate(pattern = "IIIDDDIID") == None
    assert candidate(pattern = "DDIIIDDDIDI") == None
    assert candidate(pattern = "IIDDIIIIID") == None
    assert candidate(pattern = "DDDDIII") == "54321678"
    assert candidate(pattern = "IDIDID") == "1325476"
    assert candidate(pattern = "IIDIDIDI") == "124365879"
    assert candidate(pattern = "DDDDDDDDD") == None
    assert candidate(pattern = "DDDDDDI") == "76543218"
    assert candidate(pattern = "DDIDDDID") == "321765498"
    assert candidate(pattern = "DDIIIIIII") == None
    assert candidate(pattern = "DIIIIIII") == "213456789"
    assert candidate(pattern = "IIIDDDDDDID") == None
    assert candidate(pattern = "IDDDIDII") == "154327689"
    assert candidate(pattern = "DDIIDIDDDI") == None
    assert candidate(pattern = "DDDDIIIID") == None
    assert candidate(pattern = "DDIDIDID") == "321547698"
    assert candidate(pattern = "IIIDDDDD") == "123987654"
    assert candidate(pattern = "DDDDDIIIIII") == None
    assert candidate(pattern = "IIIDDDDIII") == None
    assert candidate(pattern = "IIIIIIIDDDDDD") == None
    assert candidate(pattern = "IIIIIID") == "12345687"
    assert candidate(pattern = "IIIIIIIIIII") == None
    assert candidate(pattern = "IDIDDDID") == "132765498"
    assert candidate(pattern = "IDIDIDIDIDIDID") == None
    assert candidate(pattern = "IDIDIIDID") == None
    assert candidate(pattern = "IIIIIII") == "12345678"
    assert candidate(pattern = "DDIIDDDD") == "321498765"
    assert candidate(pattern = "IIIIIIID") == "123456798"
    assert candidate(pattern = "IDIDIDIDIDID") == None
    assert candidate(pattern = "DIIDIDID") == "213547698"
    assert candidate(pattern = "DDIIDIDI") == "321465879"
    assert candidate(pattern = "DDDIIIDID") == None
    assert candidate(pattern = "IIDDDIIII") == None
    assert candidate(pattern = "IIDDDIID") == "126543798"
    assert candidate(pattern = "IIDDDIII") == "126543789"
    assert candidate(pattern = "IDIDIDIDIDIDIDID") == None
    assert candidate(pattern = "DIDID") == "214365"
    assert candidate(pattern = "DDDDDIII") == "654321789"
    assert candidate(pattern = "DDII") == "32145"
    assert candidate(pattern = "DDDIDDDD") == "432198765"
    assert candidate(pattern = "IIIDDDIDDD") == None
    assert candidate(pattern = "DDIDDDDDDID") == None
    assert candidate(pattern = "IDDDDDD") == "18765432"
    assert candidate(pattern = "IDII") == "13245"
    assert candidate(pattern = "DDDDDDII") == "765432189"
    assert candidate(pattern = "IIIDDDDI") == "123876549"
    assert candidate(pattern = "IDDDIDID") == "154327698"
    assert candidate(pattern = "IIIIIDDI") == "123458769"
    assert candidate(pattern = "DDDDDD") == "7654321"
    assert candidate(pattern = "IIDDDIDDDDD") == None
    assert candidate(pattern = "IIIIIDDD") == "123459876"
    assert candidate(pattern = "IDIDDDIDID") == None
    assert candidate(pattern = "IIIIIIIID") == None
    assert candidate(pattern = "DDDDDDDDDDDID") == None
    assert candidate(pattern = "IIIIIDDDD") == None
    assert candidate(pattern = "DDDDIID") == "54321687"
    assert candidate(pattern = "IDDDIIDDD") == None
    assert candidate(pattern = "IIIDDDDDDDDDD") == None
    assert candidate(pattern = "DDIIDDID") == "321476598"
    assert candidate(pattern = "IIDDDDDD") == "129876543"
    assert candidate(pattern = "IIDDDII") == "12654378"
    assert candidate(pattern = "DDIIDIDD") == "321465987"
    assert candidate(pattern = "IIDDIIDD") == "125436987"
    assert candidate(pattern = "IIIIIIII") == "123456789"
    assert candidate(pattern = "IIIDDDD") == "12387654"
    assert candidate(pattern = "DDIID") == "321465"


