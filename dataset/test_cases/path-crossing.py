def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(path = "NEESWNWWSNNWNSSSWEWEWEWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEESWNWWSNNWNSSSWEWEWEWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSSSSEEEEEEEWWWWWWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSSSSEEEEEEEWWWWWWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSNEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSNEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWEWEWEW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWEWEWEW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "N") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "N") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSSEEEWWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSSEEEWWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSWEWNNEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSWEWNNEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSNSNSNS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSNSNSNS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNESSEWSWNWNWSSSNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNESSEWSWNWNWSSSNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNESSWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNESSWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENESSWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENESSWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NES") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NES") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNSSSSWWWWEEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNSSSSWWWWEEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WEWEWEWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WEWEWEWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NWSWEWNWNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NWSWEWNWNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNEESSWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNEESSWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNEEESSWWNNNEEESSWWNNNESSWWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNEEESSWWNNNEEESSWWNNNESSWWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEEE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEEE") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "EESSEENN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EESSEENN") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "WEWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WEWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENW") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENW") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEEEEWWWWSSSSNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEEEEWWWWSSSSNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWSWNESWSWNESWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWSWNESWSWNESWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSEWSWESWESWESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSEWSWESWESWESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNEWSSEESSEENNNWNNNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNEWSSEESSEENNNWNNNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWNENWENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWNENWENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NWSNWSNWSNWSNWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NWSNWSNWSNWSNWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEEEEWWWWWSSSSSNNNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEEEEWWWWWSSSSSNNNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NWNWNWNWNWSWSWSWSW") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NWNWNWNWNWSWSWSWSW") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWWNESWWNESWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWWNESWWNESWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EESWWNNESWNESESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EESWWNNESWNESESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WENWENWENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WENWENWENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSEENWNNWSSSWEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSEENWNNWSSSWEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSSEEEWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSSEEEWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSNEWSNEWSNEWSNEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSNEWSNEWSNEWSNEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSNNEEWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSNNEEWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNWNWSSSWNEEEEEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNWNWSSSWNEEEEEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNESWSWNWNWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNESWSWNWNWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNSSSSWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNSSSSWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENWNWSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENWNWSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNEEESSEWWNNNNEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNEEESSEWWNNNNEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESEWNESEWNESEW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESEWNESEWNESEW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENNWWSSNNSSEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENNWWSSNNSSEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSSNNNNEEEEWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSSNNNNEEEEWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEEEEEEEEEEEEEEWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSNNNNNNNNNNNNNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEEEEEEEEEEEEEEWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSNNNNNNNNNNNNNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSNNNSSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSNNNSSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSNEWSNEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSNEWSNEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENSNWNWNWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENSNWNWNWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ESSNNWWSSEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ESSNNWWSSEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SWENSWENSWENSWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SWENSWENSWENSWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WESSNNESWWSE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WESSNNESWWSE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSWSENENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSWSENENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WSEWSEWSEWSEW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WSEWSEWSEWSEW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSSSSEEWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSSSSEEWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WENSNWSWES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WENSNWSWES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NWWWSSENNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NWWWSSENNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEESWNESWSWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEESWNESWSWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WEWNSWESWESWESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WEWNSWESWESWESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNWESWSWSEENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNWESWSWSEENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WNWSSNSSWEEENEEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WNWSSNSSWEEENEEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWEWEWEWEEWWEWEEWWSWWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWEWEWEWEEWWEWEEWWSWWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSSEEEEWWWNNSNWEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSSEEEEWWWNNSNWEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSENNWESSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSENNWESSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEEEEESWWWWNSSSSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEEEEESWWWWNSSSSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNNSSSSSAAAABBBB") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNNSSSSSAAAABBBB") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNEESWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNEESWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSEWSWENWSEWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSEWSWENWSEWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNNNNNSSSSSSSSWWWWWWWWEEEEEEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNNNNNSSSSSSSSWWWWWWWWEEEEEEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENENEWNWNWSWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENENEWNWNWSWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENENENESESESESESWSWSWSWSW") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENENENESESESESESWSWSWSWSW") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENEWWNNEWSWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENEWWNNEWSWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNNNNNNNN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNNNNNNNN") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWESWNESEENWSWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWESWNESEENWSWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESESWWSSWNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESESWWSSWNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENENENEWWWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENENENEWWWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNEEEESSSNNNWWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNEEEESSSNNNWWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENENENNENESESWSWWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENENENNENESESWSWWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENSWNESWNESEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENSWNESWNESEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWSESWNESWENSWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWSESWNESWENSWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENEENWNNWSSSSNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENEENWNNWSSSSNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEESSSNNNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEESSSNNNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSSSSEEEWWWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSSSSEEEWWWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EESNNWWSSEEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EESNNWWSSEEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNEEESSEESWWNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNEEESSEESWWNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENWNNWSSNNWEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENWNNWSSNNWEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWWNWSSWSEWSSN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWWNWSSWSEWSSN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESESWNESESWNESESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESESWNESESWNESESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSWNWNWSWNWNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSWNWNWSWNWNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSESWNESWNES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSESWNESWNES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENNENNE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENNENNE") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSNEWSNEWSNEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSNEWSNEWSNEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSEWSSEEEWWWNNEENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSEWSSEEEWWWNNEENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNWESSSWNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNWESSSWNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ESSSWWNNEEEWWNNSSEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ESSSWWNNEEEWWNNSSEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNESWNESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNESWNESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESESWWSWN") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESESWWSWN") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNESESWNESESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNESESWNESESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSEWSWNNWSEWSW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSEWSWNNWSEWSW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWNNWSSNWNWEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWNNWSSNWNWEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNWSENNWWSSSEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNWSENNWWSSSEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WNWSSNSSWEEENEENE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WNWSSNSSWEEENEENE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSEWNSSEWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSEWNSSEWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWSENWSENWSENWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWSENWSENWSENWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSSWWWWNNEE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSSWWWWNNEE") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSWWNEEENNEESSE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSWWNEEENNEESSE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWSWWSESNWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWSWWSESNWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSNWWNEEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSNWWNEEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSESSWWNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSESSWWNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWENSWEWNENSWSEWNESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWENSWEWNENSWSEWNESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WESSNNWESSNNWESSNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WESSNNWESSNNWESSNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSWWSSENNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSWWSSENNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ESWENSWENSWENSWENSWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ESWENSWENSWENSWENSWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNSWENSWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNSWENSWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWWSEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWWSEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWEWNEWEWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWEWNEWEWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENNWWNSSSNEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENNWWNSSSNEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EESWWNNEWSNEWSNEWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EESWWNNEWSNEWSNEWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WEWNENEWNWNWSWSNEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WEWNENEWNWNWSWSNEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNSWENWEWSWEWNSWEWENWSWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNSWENWEWSWEWNSWEWENWSWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSEWNENWSEWNENWSEW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSEWNENWSEWNENWSEW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WNESSWNESSWNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WNESSWNESSWNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WENWNNWENWSE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WENWNNWENWSE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSEWNNNSSSWEWEWEWWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSEWNNNSSSWEWEWEWWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWNWNWSENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWNWNWSENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WNEEESSNWWWEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WNEEESSNWWWEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEENNWWWWNEESSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEENNWWWWNEESSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSSNNNNWWEEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSSNNNNWWEEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEENNNEEWWSSSWWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEENNNEEWWSSSWWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEEEEEEWWWWWWSSSSSSNNNNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEEEEEEWWWWWWSSSSSSNNNNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EEEEEENNNNNNSSSSSWEWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EEEEEENNNNNNSSSSSWEWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSSWWWWEEEEEENNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSSWWWWEEEEEENNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSSEEEEWWWWNNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSSEEEEWWWWNNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSSSSSSSS") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSSSSSSSS") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSWWEENNSSSWWEEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSWWEENNSSSWWEEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EENNWWSSNWNWEEWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EENNWWSSNWNWEEWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENENE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENENE") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENESWNESE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENESWNESE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ENWSWEWNWSWEWNWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ENWSWEWNWSWEWNWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSEWSWNESWESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSEWSWNESWESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WWEENNWEES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WWEENNWEES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWEWNEWNWSWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWEWNEWNWSWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSSSSSWWWWWWWWWEEEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSSSSSWWWWWWWWWEEEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NWSWNWSWNW") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NWSWNWSWNW") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSSWWEENN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSSWWEENN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSEENWNNWSSSWEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSEENWNNWSSSWEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWSNWSNESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWSNWSNESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSWESWESWESWESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSWESWESWESWESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESNESNESNESNES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESNESNESNESNES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNNNWWWEES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNNNWWWEES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSNNSSNNSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSNNSSNNSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSWNNWSSNWNWEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSWNNWSSNWNWEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNWNWSSSWNEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNWNWSSSWNEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENWNSNS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENWNSNS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWSWNWESWE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWSWNWESWE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNEEWWSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNEEWWSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SEENENENEWSWSWNENE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SEENENENEWSWSWNENE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WNWSSNSSSENEEN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WNWSSNSSSENEEN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESESWSEWN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESESWSEWN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNEWSWSEWSSNENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNEWSWSEWSSNENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "EWEWEWEWEW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "EWEWEWEWEW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSEWEEWEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSEWEEWEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSSEEEEEWWWWNNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSSEEEEEWWWWNNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNWWWSSSE") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNWWWSSSE") == False: {e}')
    
    total += 1
    try:
        result = candidate(path = "NSSSNEEEWNWSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NSSSNEEEWNWSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NESWNESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NESWNESW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "ESESWNEWSWSWNENESE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "ESESWNEWSWSWNENESE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNWWSSSNE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNWWSSSNE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NEWSWNESWESWNES") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NEWSWNESWESWNES") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNESSEWW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNESSEWW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "WEEWEEWEEE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "WEEWEEWEEE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NENENWENWENWENWENW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NENENWENWENWENWENW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSSEEEWWWS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSSEEEWWWS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SWSWSWSWNENENENENE") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SWSWSWSWNENENENENE") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "SSSEEESSSWWNNN") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "SSSEEESSSWWNNN") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSSNNSS") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSSNNSS") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNSEESSWNW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNSEESSWNW") == True: {e}')
    
    total += 1
    try:
        result = candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENESESESESNESWENSWEWNENSWSEWNESW") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENESESESESNESWENSWEWNENSWSEWNESW") == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(path = "NEESWNWWSNNWNSSSWEWEWEWE") == True
    assert candidate(path = "NNNSSSSSSEEEEEEEWWWWWWWWW") == True
    assert candidate(path = "NEWSNEWS") == True
    assert candidate(path = "EWEWEWEW") == True
    assert candidate(path = "NESWW") == True
    assert candidate(path = "NSSS") == True
    assert candidate(path = "N") == False
    assert candidate(path = "NNSSEEEWWS") == True
    assert candidate(path = "NSSSWEWNNEE") == True
    assert candidate(path = "") == False
    assert candidate(path = "NSNSNSNS") == True
    assert candidate(path = "NNNSSSSS") == True
    assert candidate(path = "NESWNE") == True
    assert candidate(path = "NNESSEWSWNWNWSSSNW") == True
    assert candidate(path = "NS") == True
    assert candidate(path = "NNESSWW") == True
    assert candidate(path = "NENESSWW") == True
    assert candidate(path = "EWE") == True
    assert candidate(path = "NES") == False
    assert candidate(path = "NEWS") == True
    assert candidate(path = "NNNNSSSSWWWWEEEE") == True
    assert candidate(path = "WEWEWEWE") == True
    assert candidate(path = "NWSWEWNWNW") == True
    assert candidate(path = "NNEESSWW") == True
    assert candidate(path = "NNEEESSWWNNNEEESSWWNNNESSWWN") == True
    assert candidate(path = "EEEE") == False
    assert candidate(path = "EESSEENN") == False
    assert candidate(path = "WEWN") == True
    assert candidate(path = "EENW") == False
    assert candidate(path = "NEEEEWWWWSSSSNNN") == True
    assert candidate(path = "ENWSWNESWSWNESWS") == True
    assert candidate(path = "NENWSEWSWESWESWESW") == True
    assert candidate(path = "NNEWSSEESSEENNNWNNNW") == True
    assert candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENE") == True
    assert candidate(path = "ENWNENWENW") == True
    assert candidate(path = "NWSNWSNWSNWSNWS") == True
    assert candidate(path = "EEEEEWWWWWSSSSSNNNNN") == True
    assert candidate(path = "NWNWNWNWNWSWSWSWSW") == False
    assert candidate(path = "NESWWNESWWNESWW") == True
    assert candidate(path = "EESWWNNESWNESESW") == True
    assert candidate(path = "WENWENWENW") == True
    assert candidate(path = "NSEENWNNWSSSWEE") == True
    assert candidate(path = "NNSSEEEWWW") == True
    assert candidate(path = "NEWSNEWSNEWSNEWSNEWS") == True
    assert candidate(path = "SSNNEEWW") == True
    assert candidate(path = "NNWNWSSSWNEEEEEN") == True
    assert candidate(path = "NNESWSWNWNWS") == True
    assert candidate(path = "NNNNSSSSWWWW") == True
    assert candidate(path = "EENWNWSS") == True
    assert candidate(path = "NNNNEEESSEWWNNNNEE") == True
    assert candidate(path = "NESEWNESEWNESEW") == True
    assert candidate(path = "EENNWWSSNNSSEE") == True
    assert candidate(path = "SSSSNNNNEEEEWWWW") == True
    assert candidate(path = "EEEEEEEEEEEEEEEWWWWWWWWWWWWWWWSSSSSSSSSSSSSSSNNNNNNNNNNNNNNN") == True
    assert candidate(path = "NNNSSSNNNSSS") == True
    assert candidate(path = "NEWSNEWSNEWS") == True
    assert candidate(path = "ENSNWNWNWN") == True
    assert candidate(path = "ESSNNWWSSEN") == True
    assert candidate(path = "SWENSWENSWENSWEN") == True
    assert candidate(path = "WESSNNESWWSE") == True
    assert candidate(path = "NENWSWSENENW") == True
    assert candidate(path = "WSEWSEWSEWSEW") == True
    assert candidate(path = "NNNSSSSSSEEWWWW") == True
    assert candidate(path = "WENSNWSWES") == True
    assert candidate(path = "NWWWSSENNE") == True
    assert candidate(path = "NEESWNESWSWN") == True
    assert candidate(path = "WEWNSWESWESWESW") == True
    assert candidate(path = "NNWESWSWSEENW") == True
    assert candidate(path = "WNWSSNSSWEEENEEN") == True
    assert candidate(path = "EWEWEWEWEEWWEWEEWWSWWSW") == True
    assert candidate(path = "NSSSSEEEEWWWNNSNWEEE") == True
    assert candidate(path = "SSENNWESSW") == True
    assert candidate(path = "NEEEEESWWWWNSSSSS") == True
    assert candidate(path = "NNNNNSSSSSAAAABBBB") == True
    assert candidate(path = "NESWNEESWW") == True
    assert candidate(path = "NENWSEWSWENWSEWSW") == True
    assert candidate(path = "NNNNNNNNSSSSSSSSWWWWWWWWEEEEEEEE") == True
    assert candidate(path = "ENENEWNWNWSWSW") == True
    assert candidate(path = "NENENENENESESESESESWSWSWSWSW") == False
    assert candidate(path = "ENEWWNNEWSWE") == True
    assert candidate(path = "NNNNNNNNNN") == False
    assert candidate(path = "ENWESWNESEENWSWEN") == True
    assert candidate(path = "NESESWWSSWNE") == True
    assert candidate(path = "NENENENENEWWWWWW") == True
    assert candidate(path = "NNNEEEESSSNNNWWSW") == True
    assert candidate(path = "NENENENENNENESESWSWWSW") == True
    assert candidate(path = "ENSWNESWNESEWS") == True
    assert candidate(path = "ENWSESWNESWENSWE") == True
    assert candidate(path = "ENEENWNNWSSSSNE") == True
    assert candidate(path = "EEESSSNNNW") == True
    assert candidate(path = "NNNSSSSSSEEEWWWW") == True
    assert candidate(path = "EESNNWWSSEEN") == True
    assert candidate(path = "NNNEEESSEESWWNN") == True
    assert candidate(path = "EENWNNWSSNNWEE") == True
    assert candidate(path = "NEWWNWSSWSEWSSN") == True
    assert candidate(path = "NESESWNESESWNESESW") == True
    assert candidate(path = "NENWSWNWNWSWNWNW") == True
    assert candidate(path = "NENWSESWNESWNES") == True
    assert candidate(path = "NENENNENNE") == False
    assert candidate(path = "NEWSNEWSNEWSNEWS") == True
    assert candidate(path = "NSEWSSEEEWWWNNEENW") == True
    assert candidate(path = "NNWESSSWNE") == True
    assert candidate(path = "ESSSWWNNEEEWWNNSSEEE") == True
    assert candidate(path = "NESWNESWNESW") == True
    assert candidate(path = "NESESWWSWN") == False
    assert candidate(path = "NESWNESESWNESESW") == True
    assert candidate(path = "NENWSEWSWNNWSEWSW") == True
    assert candidate(path = "ENWNNWSSNWNWEE") == True
    assert candidate(path = "NNWSENNWWSSSEEE") == True
    assert candidate(path = "WNWSSNSSWEEENEENE") == True
    assert candidate(path = "NSEWNSSEWW") == True
    assert candidate(path = "ENWSENWSENWSENWS") == True
    assert candidate(path = "SSSSWWWWNNEE") == False
    assert candidate(path = "NSSSWWNEEENNEESSE") == True
    assert candidate(path = "ENWSWWSESNWEN") == True
    assert candidate(path = "NSSSNWWNEEEE") == True
    assert candidate(path = "NNSESSWWNE") == True
    assert candidate(path = "NESWENSWEWNENSWSEWNESW") == True
    assert candidate(path = "WESSNNWESSNNWESSNN") == True
    assert candidate(path = "SSWWSSENNE") == True
    assert candidate(path = "ESWENSWENSWENSWENSWEN") == True
    assert candidate(path = "NESWNSWENSWE") == True
    assert candidate(path = "NESWWSEN") == True
    assert candidate(path = "EWEWNEWEWN") == True
    assert candidate(path = "EENNWWNSSSNEEE") == True
    assert candidate(path = "EESWWNNEWSNEWSNEWS") == True
    assert candidate(path = "WEWNENEWNWNWSWSNEN") == True
    assert candidate(path = "NESWNSWENWEWSWEWNSWEWENWSWEN") == True
    assert candidate(path = "NENWSEWNENWSEWNENWSEW") == True
    assert candidate(path = "WNESSWNESSWNE") == True
    assert candidate(path = "WENWNNWENWSE") == True
    assert candidate(path = "NSEWNNNSSSWEWEWEWWE") == True
    assert candidate(path = "NENWNWNWSENW") == True
    assert candidate(path = "WNEEESSNWWWEN") == True
    assert candidate(path = "EEENNWWWWNEESSS") == True
    assert candidate(path = "SSSSNNNNWWEEEE") == True
    assert candidate(path = "EEENNNEEWWSSSWWN") == True
    assert candidate(path = "EEEEEEEWWWWWWSSSSSSNNNNNN") == True
    assert candidate(path = "EEEEEENNNNNNSSSSSWEWE") == True
    assert candidate(path = "NSSSSWWWWEEEEEENNN") == True
    assert candidate(path = "SSSSEEEEWWWWNNNN") == True
    assert candidate(path = "SSSSSSSSSS") == False
    assert candidate(path = "NSSSWWEENNSSSWWEEN") == True
    assert candidate(path = "EENNWWSSNWNWEEWN") == True
    assert candidate(path = "NENENENE") == False
    assert candidate(path = "NENESWNESE") == True
    assert candidate(path = "ENWSWEWNWSWEWNWS") == True
    assert candidate(path = "NENWSEWSWNESWESW") == True
    assert candidate(path = "WWEENNWEES") == True
    assert candidate(path = "EWEWNEWNWSWE") == True
    assert candidate(path = "NNNSSSSSSSWWWWWWWWWEEEEE") == True
    assert candidate(path = "NWSWNWSWNW") == False
    assert candidate(path = "NNSSWWEENN") == True
    assert candidate(path = "NSEENWNNWSSSWEEE") == True
    assert candidate(path = "NENWSNWSNESW") == True
    assert candidate(path = "NNSWESWESWESWESW") == True
    assert candidate(path = "NESNESNESNESNES") == True
    assert candidate(path = "NESWNNNWWWEES") == True
    assert candidate(path = "SSNNSSNNSS") == True
    assert candidate(path = "NEWSWNNWSSNWNWEE") == True
    assert candidate(path = "NNWNWSSSWNEEE") == True
    assert candidate(path = "NENWNSNS") == True
    assert candidate(path = "EWSWNWESWE") == True
    assert candidate(path = "NNEEWWSS") == True
    assert candidate(path = "SEENENENEWSWSWNENE") == True
    assert candidate(path = "WNWSSNSSSENEEN") == True
    assert candidate(path = "NESESWSEWN") == True
    assert candidate(path = "NNEWSWSEWSSNENW") == True
    assert candidate(path = "EWEWEWEWEW") == True
    assert candidate(path = "SSEWEEWEEE") == True
    assert candidate(path = "NSSSSEEEEEWWWWNNNN") == True
    assert candidate(path = "NNNWWWSSSE") == False
    assert candidate(path = "NSSSNEEEWNWSS") == True
    assert candidate(path = "NESWNESW") == True
    assert candidate(path = "ESESWNEWSWSWNENESE") == True
    assert candidate(path = "NNNWWSSSNE") == True
    assert candidate(path = "NEWSWNESWESWNES") == True
    assert candidate(path = "NNESSEWW") == True
    assert candidate(path = "WEEWEEWEEE") == True
    assert candidate(path = "NENENWENWENWENWENW") == True
    assert candidate(path = "NNSSEEEWWWS") == True
    assert candidate(path = "SWSWSWSWNENENENENE") == True
    assert candidate(path = "SSSEEESSSWWNNN") == True
    assert candidate(path = "NNSSNNSS") == True
    assert candidate(path = "NNSEESSWNW") == True
    assert candidate(path = "NNNSSSWEWEWESWNWNWNWWSWSWENENESESESESNESWENSWEWNENSWSEWNESW") == True


