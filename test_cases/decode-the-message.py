def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "cba zyx") == "xyz abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "cba zyx") == "xyz abc": {e}')
    
    total += 1
    try:
        result = candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "yfcj myj pyjl ufcj myj pyjl ufcj myj pyjl") == "omer gor sorq cmer gor sorq cmer gor sorq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "yfcj myj pyjl ufcj myj pyjl ufcj myj pyjl") == "omer gor sorq cmer gor sorq cmer gor sorq": {e}')
    
    total += 1
    try:
        result = candidate(key = "the five boxing wizards jump quickly on this yellow pig",message = "jhxuh lqdj efxgh lpuaz fxdyjzjw") == "rbisb yvpr cdikb yusnm dipzrmrl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the five boxing wizards jump quickly on this yellow pig",message = "jhxuh lqdj efxgh lpuaz fxdyjzjw") == "rbisb yvpr cdikb yusnm dipzrmrl": {e}')
    
    total += 1
    try:
        result = candidate(key = "dvhfujngcpqxlwokzriebastmy",message = "mwtiaz azr") == "ynxsvq vqr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "dvhfujngcpqxlwokzriebastmy",message = "mwtiaz azr") == "ynxsvq vqr": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xyz abc") == "xyz abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xyz abc") == "xyz abc": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret": {e}')
    
    total += 1
    try:
        result = candidate(key = "byvzkgxfnqmpalwodjtrshceui",message = "xsm wv zmz") == "guk oc dkd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "byvzkgxfnqmpalwodjtrshceui",message = "xsm wv zmz") == "guk oc dkd": {e}')
    
    total += 1
    try:
        result = candidate(key = "wmtresuavhigdcbfykjqploxzn",message = "lfnlccyvmdg") == "vpzvnnqibml"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "wmtresuavhigdcbfykjqploxzn",message = "lfnlccyvmdg") == "vpzvnnqibml": {e}')
    
    total += 1
    try:
        result = candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "sl rfc zdf") == "tm sgd aeg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "sl rfc zdf") == "tm sgd aeg": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "mlkjhgfedcbazyxwvutsrqpon") == "nopqstuvwxyzabcdefghijklm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "mlkjhgfedcbazyxwvutsrqpon") == "nopqstuvwxyzabcdefghijklm": {e}')
    
    total += 1
    try:
        result = candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "z x c v") == "z x c v"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "z x c v") == "z x c v": {e}')
    
    total += 1
    try:
        result = candidate(key = "gysrnhxvaofcedwmltukipjbqz",message = "gigv symykgl igxvxjxg") == "auah cbpbtaq uaghgwga"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "gysrnhxvaofcedwmltukipjbqz",message = "gigv symykgl igxvxjxg") == "auah cbpbtaq uaghgwga": {e}')
    
    total += 1
    try:
        result = candidate(key = "phinxajsgkrzcwvltqbdemoufy",message = "xvo wv pmj") == "eow no avg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "phinxajsgkrzcwvltqbdemoufy",message = "xvo wv pmj") == "eow no avg": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zaoymnbxcqrljtheifkgdvspwu") == "zaoymnbxcqrljtheifkgdvspwu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zaoymnbxcqrljtheifkgdvspwu") == "zaoymnbxcqrljtheifkgdvspwu": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv jfrxp yildm ulc") == "olw qnduj fhsmz gsv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv jfrxp yildm ulc") == "olw qnduj fhsmz gsv": {e}')
    
    total += 1
    try:
        result = candidate(key = "the five boxing wizards jump quickly on this june day",message = "ymj lvfx sflhzymhs vxlw wjymjlvfx sflhzymhs") == "ztr yfdi qdybmztbq fiyl lrztryfdi qdybmztbq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the five boxing wizards jump quickly on this june day",message = "ymj lvfx sflhzymhs vxlw wjymjlvfx sflhzymhs") == "ztr yfdi qdybmztbq fiyl lrztryfdi qdybmztbq": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "thequ ickbr ownfo xjump sover thela zydog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "thequ ickbr ownfo xjump sover thela zydog": {e}')
    
    total += 1
    try:
        result = candidate(key = "dfghjklwcvxziomnpqrustyabe",message = "kckd ykky") == "fifa wffw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "dfghjklwcvxziomnpqrustyabe",message = "kckd ykky") == "fifa wffw": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnychdpbxofl wgviakjuzterqs",message = "irhvmvccsjb") == "pxeoaoddzsh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnychdpbxofl wgviakjuzterqs",message = "irhvmvccsjb") == "pxeoaoddzsh": {e}')
    
    total += 1
    try:
        result = candidate(key = "pack my box with five dozen liquor jugs",message = "xujf qv zgy jxpx qne nfgqj sraju") == "ivxn uo ryf xiai usp snyux zwbxv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "pack my box with five dozen liquor jugs",message = "xujf qv zgy jxpx qne nfgqj sraju") == "ivxn uo ryf xiai usp snyux zwbxv": {e}')
    
    total += 1
    try:
        result = candidate(key = "mwp dhxjzvcqrkbyanflstguoei",message = "di vccvmr wv czebwqha wv iv lvyrj") == "dz ijjial bi jhynbkep bi zi siolg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mwp dhxjzvcqrkbyanflstguoei",message = "di vccvmr wv czebwqha wv iv lvyrj") == "dz ijjial bi jhynbkep bi zi siolg": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "a b c d") == "z y x w"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "a b c d") == "z y x w": {e}')
    
    total += 1
    try:
        result = candidate(key = "the five boxing wizards jump quickly",message = "fmwp vifd ttp xosmead") == "dtlu fedp aau ihqtcnp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the five boxing wizards jump quickly",message = "fmwp vifd ttp xosmead") == "dtlu fedp aau ihqtcnp": {e}')
    
    total += 1
    try:
        result = candidate(key = "vuqangfkswjpryxtdmzobhcile",message = "wfn yv yfcv") == "jge na ngwa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "vuqangfkswjpryxtdmzobhcile",message = "wfn yv yfcv") == "jge na ngwa": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "eiqhw fjq hwdq") == "eiqhw fjq hwdq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "eiqhw fjq hwdq") == "eiqhw fjq hwdq": {e}')
    
    total += 1
    try:
        result = candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "zruog glhvg frp fvdw zl glcgv") == "vtchw wqniw mts miup vq wqewi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "zruog glhvg frp fvdw zl glcgv") == "vtchw wqniw mts miup vq wqewi": {e}')
    
    total += 1
    try:
        result = candidate(key = "thejumpsquickbrownfoxoverlazydog",message = "svhjyjsiqphsjudprvcbgijz") == "htbdxdhjigbhdeygntkmzjdw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "thejumpsquickbrownfoxoverlazydog",message = "svhjyjsiqphsjudprvcbgijz") == "htbdxdhjigbhdeygntkmzjdw": {e}')
    
    total += 1
    try:
        result = candidate(key = "ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az",message = "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz") == "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az",message = "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz") == "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz": {e}')
    
    total += 1
    try:
        result = candidate(key = "swzybfrxlnaoumdgtqivhjkpce",message = "flgxswdliefyirukyoaqmpjc") == "fiphaboiszfdsgmwdlkrnxvy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "swzybfrxlnaoumdgtqivhjkpce",message = "flgxswdliefyirukyoaqmpjc") == "fiphaboiszfdsgmwdlkrnxvy": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "qruqz efn nhr htyq") == "djedw cnm mbj baxd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "qruqz efn nhr htyq") == "djedw cnm mbj baxd": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "xibohu uvp xibohu") == "ofikbe etr ofikbe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "xibohu uvp xibohu") == "ofikbe etr ofikbe": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcd efgh ijkl mnop qrst uvwx yz",message = "vuwx yz abcd ef") == "vuwx yz abcd ef"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcd efgh ijkl mnop qrst uvwx yz",message = "vuwx yz abcd ef") == "vuwx yz abcd ef": {e}')
    
    total += 1
    try:
        result = candidate(key = "gymnopqrstuvwxzabcdefhiljk",message = "xqmgq zm zmjy") == "ngcag oc ocyb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "gymnopqrstuvwxzabcdefhiljk",message = "xqmgq zm zmjy") == "ngcag oc ocyb": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yxe xe xe") == "bcv cv cv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yxe xe xe") == "bcv cv cv": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",message = "abc def abc") == "abc def abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",message = "abc def abc") == "abc def abc": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "vxp qpy o") == "vxp qpy o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "vxp qpy o") == "vxp qpy o": {e}')
    
    total += 1
    try:
        result = candidate(key = "jumps over the lazy dog quick brown fox",message = "pvuzr cgviy ojizv bxz cfiwz nqzsx vgrb") == "dgbni tqgso fasng vzn tyswn xrnez gqiv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jumps over the lazy dog quick brown fox",message = "pvuzr cgviy ojizv bxz cfiwz nqzsx vgrb") == "dgbni tqgso fasng vzn tyswn xrnez gqiv": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "xqf") == "odn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "xqf") == "odn": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "gfn") == "znm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "gfn") == "znm": {e}')
    
    total += 1
    try:
        result = candidate(key = "pzucfelxwyabqomtjirdnsvhgk",message = "kwj kwi kwv wkv") == "ziq zir ziw izw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "pzucfelxwyabqomtjirdnsvhgk",message = "kwj kwi kwv wkv") == "ziq zir ziw izw": {e}')
    
    total += 1
    try:
        result = candidate(key = "fmwtkujhpnobxigcsqrzydalve",message = "fyh fyt fyv yfj") == "auh aud auy uag"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "fmwtkujhpnobxigcsqrzydalve",message = "fyh fyt fyv yfj") == "auh aud auy uag": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghij klmnopqrstuvwxyz",message = "qzcfj nx ud qzcfj") == "qzcfj nx ud qzcfj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghij klmnopqrstuvwxyz",message = "qzcfj nx ud qzcfj") == "qzcfj nx ud qzcfj": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx x") == "xpo o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx x") == "xpo o": {e}')
    
    total += 1
    try:
        result = candidate(key = "jumps over lazy dogs quick brown fox the this",message = "yjiwxtw vqzj spwq ovbxc yoz qjxv") == "maquxyu gpla edup fgtxr mfl paxg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jumps over lazy dogs quick brown fox the this",message = "yjiwxtw vqzj spwq ovbxc yoz qjxv") == "maquxyu gpla edup fgtxr mfl paxg": {e}')
    
    total += 1
    try:
        result = candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "frg fmh gfn") == "wix wdy xwe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "frg fmh gfn") == "wix wdy xwe": {e}')
    
    total += 1
    try:
        result = candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "qxy xyx yxq") == "ryz yzy zyr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "qxy xyx yxq") == "ryz yzy zyr": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret": {e}')
    
    total += 1
    try:
        result = candidate(key = "ekmflgdqvzntowyhxuspaibrcj",message = "jbs xut hig") == "zws qrl pvf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ekmflgdqvzntowyhxuspaibrcj",message = "jbs xut hig") == "zws qrl pvf": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "iyh uhy l") == "rbs fsb o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "iyh uhy l") == "rbs fsb o": {e}')
    
    total += 1
    try:
        result = candidate(key = "vwxymnbcdfghjklqropstuzaike",message = "vcp o cv vcp") == "ahs r ha ahs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "vwxymnbcdfghjklqropstuzaike",message = "vcp o cv vcp") == "ahs r ha ahs": {e}')
    
    total += 1
    try:
        result = candidate(key = "ajfzldkgotmhrvwsypnqicxebu",message = "oxt oxi oxd xot") == "iwj iwu iwf wij"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ajfzldkgotmhrvwsypnqicxebu",message = "oxt oxi oxd xot") == "iwj iwu iwf wij": {e}')
    
    total += 1
    try:
        result = candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "wfn yv yfcv") == "nwe pm pwtm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "wfn yv yfcv") == "nwe pm pwtm": {e}')
    
    total += 1
    try:
        result = candidate(key = "tevosjhbnyxrgqkfaumzilwpcd",message = "npu gpm gpy lgg") == "ixr mxs mxj vmm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "tevosjhbnyxrgqkfaumzilwpcd",message = "npu gpm gpy lgg") == "ixr mxs mxj vmm": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "hfu q jhu") == "kmt z jkt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "hfu q jhu") == "kmt z jkt": {e}')
    
    total += 1
    try:
        result = candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "yqz dpy o") == "ojt cso r"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "yqz dpy o") == "ojt cso r": {e}')
    
    total += 1
    try:
        result = candidate(key = "qbnvgjlftscxkouwamdphzreiy",message = "umr urv urm pyz") == "orw owd owr tzv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qbnvgjlftscxkouwamdphzreiy",message = "umr urv urm pyz") == "orw owd owr tzv": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "zqj dpy o") == "taq mjf i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "zqj dpy o") == "taq mjf i": {e}')
    
    total += 1
    try:
        result = candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "qzyc yvzctv yxqjvzq yjiwxtw on qjxv yoj") == "tkxu xckuyc xgtpckt xpbjgyj fh tpgc xfp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "qzyc yvzctv yxqjvzq yjiwxtw on qjxv yoj") == "tkxu xckuyc xgtpckt xpbjgyj fh tpgc xfp": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "c e") == "g c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "c e") == "g c": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "lii eil eil") == "mii eim eim"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "lii eil eil") == "mii eim eim": {e}')
    
    total += 1
    try:
        result = candidate(key = "vxznpqjwoefkytlimrdhaguscb",message = "tyf iy tf") == "nmk pm nk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "vxznpqjwoefkytlimrdhaguscb",message = "tyf iy tf") == "nmk pm nk": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw uqz") == "sl edw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw uqz") == "sl edw": {e}')
    
    total += 1
    try:
        result = candidate(key = "jxwtrklivnpmhudsfgcayzbeoq",message = "kcfizgv zr ocfv") == "fsqhvri ve ysqi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jxwtrklivnpmhudsfgcayzbeoq",message = "kcfizgv zr ocfv") == "fsqhvri ve ysqi": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs quick brown fox jumps over the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "wict hvpi fwnsl dtkpsyp wict itsw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs quick brown fox jumps over the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "wict hvpi fwnsl dtkpsyp wict itsw": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx z") == "xpo w"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx z") == "xpo w": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "mlml qmf lml gmgg") == "mlml qmf lml gmgg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "mlml qmf lml gmgg") == "mlml qmf lml gmgg": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "vz") == "tw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "vz") == "tw": {e}')
    
    total += 1
    try:
        result = candidate(key = "dbrujxfgzvcotwiympnslakqhe",message = "kmqs ks u kqsebs") == "wqxt wt d wxtzbt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "dbrujxfgzvcotwiympnslakqhe",message = "kmqs ks u kqsebs") == "wqxt wt d wxtzbt": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "wqiv xi sqin sqin") == "ldft of sdfm sdfm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "wqiv xi sqin sqin") == "ldft of sdfm sdfm": {e}')
    
    total += 1
    try:
        result = candidate(key = "dtjgsvyzxpkbfqwulcmohraeni",message = "obr obn oti atn") == "tlv tly tbz wby"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "dtjgsvyzxpkbfqwulcmohraeni",message = "obr obn oti atn") == "tlv tly tbz wby": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "svil km ybgu bg ujr krkhi yjr cvvux") == "svil km ybgu bg ujr krkhi yjr cvvux"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "svil km ybgu bg ujr krkhi yjr cvvux") == "svil km ybgu bg ujr krkhi yjr cvvux": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over lazy dogs",message = "mht zrs xqf ovkqvoq ngyu kgxqj bpxc") == "qba wjs odn kthdtkd mzxe hzodp irog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over lazy dogs",message = "mht zrs xqf ovkqvoq ngyu kgxqj bpxc") == "qba wjs odn kthdtkd mzxe hzodp irog": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq o") == "qfa ta i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq o") == "qfa ta i": {e}')
    
    total += 1
    try:
        result = candidate(key = "gibrfqotdhewakjyzlxmvncpus",message = "yxh lo loxhy") == "psj rg rgsjp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "gibrfqotdhewakjyzlxmvncpus",message = "yxh lo loxhy") == "psj rg rgsjp": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "aov eovm eovm") == "ocj scja scja"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "aov eovm eovm") == "ocj scja scja": {e}')
    
    total += 1
    try:
        result = candidate(key = "zxvtrqponmlkjihgfedcbazyw",message = "ajc eajc eajc") == "vmt rvmt rvmt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zxvtrqponmlkjihgfedcbazyw",message = "ajc eajc eajc") == "vmt rvmt rvmt": {e}')
    
    total += 1
    try:
        result = candidate(key = "gfedcbauioplkjhzyxwvtsrqmn",message = "ixv yxv oxv") == "irt qrt jrt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "gfedcbauioplkjhzyxwvtsrqmn",message = "ixv yxv oxv") == "irt qrt jrt": {e}')
    
    total += 1
    try:
        result = candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "wvf v fv") == "zyi y iy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "wvf v fv") == "zyi y iy": {e}')
    
    total += 1
    try:
        result = candidate(key = "abc def ghijk lmnop qrst uvwxyz",message = "nvmjy nbsytw") == "nvmjy nbsytw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abc def ghijk lmnop qrst uvwxyz",message = "nvmjy nbsytw") == "nvmjy nbsytw": {e}')
    
    total += 1
    try:
        result = candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "ihd hsih xihw gh hsi") == "rfl fsrf erfh mf fsr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "ihd hsih xihw gh hsi") == "rfl fsrf erfh mf fsr": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv q") == "mdi di d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv q") == "mdi di d": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "qytz nwt zwt") == "dxaw mla wla"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "qytz nwt zwt") == "dxaw mla wla": {e}')
    
    total += 1
    try:
        result = candidate(key = "quick brown fox jumps over the lazy dog and the quick brown fox jumps",message = "vxw aov g pufa ohq") == "qli vhq z obkv hta"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "quick brown fox jumps over the lazy dog and the quick brown fox jumps",message = "vxw aov g pufa ohq") == "qli vhq z obkv hta": {e}')
    
    total += 1
    try:
        result = candidate(key = "vbnmxczasdfghjklpoiuytrewq",message = "vkbs bs t suepuv") == "aobi bi v itxqta"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "vbnmxczasdfghjklpoiuytrewq",message = "vkbs bs t suepuv") == "aobi bi v itxqta": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yvc zc yz") == "bex ax ba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yvc zc yz") == "bex ax ba": {e}')
    
    total += 1
    try:
        result = candidate(key = "azbycxdwevfugthrskjqplomni",message = "tqppf ptd je") == "ntuuk ung si"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "azbycxdwevfugthrskjqplomni",message = "tqppf ptd je") == "ntuuk ung si": {e}')
    
    total += 1
    try:
        result = candidate(key = "xylophone qwertyuiop asdfghjklz cvbnm",message = "cvmu cvxqv") == "wxzm wxaix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "xylophone qwertyuiop asdfghjklz cvbnm",message = "cvmu cvxqv") == "wxzm wxaix": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "lqtfw xtg twkxq") == "saenb ueo ebrua"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "lqtfw xtg twkxq") == "saenb ueo ebrua": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx v") == "xpo t"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx v") == "xpo t": {e}')
    
    total += 1
    try:
        result = candidate(key = "nmqpviwedklxzfgrctuhyjasob",message = "ohc oha ohu voh") == "ytq ytw yts eyt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nmqpviwedklxzfgrctuhyjasob",message = "ohc oha ohu voh") == "ytq ytw yts eyt": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "izk zkh bva jnfrdq") == "vmx mxu oin waseqd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "izk zkh bva jnfrdq") == "vmx mxu oin waseqd": {e}')
    
    total += 1
    try:
        result = candidate(key = "quick brown fox jumps over the lazy dog",message = "rwjsi exmti gsrhri zv wimtix egzewy") == "gimpc rlnsc zpgtgc wq icnscl rzwrix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "quick brown fox jumps over the lazy dog",message = "rwjsi exmti gsrhri zv wimtix egzewy") == "gimpc rlnsc zpgtgc wq icnscl rzwrix": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs jumps over the quick brown fox the",message = "vqzj yjiwxtw spwq yoj spwq ovbxc yoz") == "mrci diswzpw hlwr dfi hlwr fmvzt dfc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs jumps over the quick brown fox the",message = "vqzj yjiwxtw spwq yoj spwq ovbxc yoz") == "mrci diswzpw hlwr dfi hlwr fmvzt dfc": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "mud gct gct") == "air uqh uqh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "mud gct gct") == "air uqh uqh": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs jumps quickly over the brown fox and",message = "vqzj yjiwxtw spwq yoj ovbxc yoz") == "qmci dinwztw hlwm dfi fqvzo dfc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs jumps quickly over the brown fox and",message = "vqzj yjiwxtw spwq yoj ovbxc yoz") == "qmci dinwztw hlwm dfi fqvzo dfc": {e}')
    
    total += 1
    try:
        result = candidate(key = "vzhofucmlnjqbdspartexwiykg",message = "dpy ld o yv") == "npx in d xa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "vzhofucmlnjqbdspartexwiykg",message = "dpy ld o yv") == "npx in d xa": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "cv lpcv") == "ed hqed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "cv lpcv") == "ed hqed": {e}')
    
    total += 1
    try:
        result = candidate(key = "the lazy dog jumps over the quick brown fox",message = "qjxv yoj vqzj spwq yjiwxtw ovbxc yvoqzgkxq") == "rkzp gik prfk onwr gkswzaw ipvzt gpirfjuzr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the lazy dog jumps over the quick brown fox",message = "qjxv yoj vqzj spwq yjiwxtw ovbxc yvoqzgkxq") == "rkzp gik prfk onwr gkswzaw ipvzt gpirfjuzr": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx yjx") == "xpo xpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx yjx") == "xpo xpo": {e}')
    
    total += 1
    try:
        result = candidate(key = "cvzkgbxquihmpnytjrsdawolef",message = "cfr cfd cfl mfl") == "azr azt azx lzx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "cvzkgbxquihmpnytjrsdawolef",message = "cfr cfd cfl mfl") == "azr azt azx lzx": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs jumps quickly over the brown fox the",message = "vqzj yjiwxtw spwq yoj ovbxc yoj") == "qmci dinwztw hlwm dfi fqvzo dfi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs jumps quickly over the brown fox the",message = "vqzj yjiwxtw spwq yoj ovbxc yoj") == "qmci dinwztw hlwm dfi fqvzo dfi": {e}')
    
    total += 1
    try:
        result = candidate(key = "thezyxwvutsrqponmlkjihgfedcba",message = "zqv eovm ztqkofv ztqkofv") == "dlh cnhp dalrnvh dalrnvh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "thezyxwvutsrqponmlkjihgfedcba",message = "zqv eovm ztqkofv ztqkofv") == "dlh cnhp dalrnvh dalrnvh": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "evh vhe yhe") == "ves esv bsv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "evh vhe yhe") == "ves esv bsv": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "zqf ykq fqu fqo ykt nqtk") == "wdn xhd nde ndk xha mdah"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "zqf ykq fqu fqo ykt nqtk") == "wdn xhd nde ndk xha mdah": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "hqv v yhqf") == "hqv v yhqf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "hqv v yhqf") == "hqv v yhqf": {e}')
    
    total += 1
    try:
        result = candidate(key = "ponmlkjihgfedcbazyxwvutsrq",message = "jxqy xtgy efn nhr") == "gszr swjr lkc ciy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ponmlkjihgfedcbazyxwvutsrq",message = "jxqy xtgy efn nhr") == "gszr swjr lkc ciy": {e}')
    
    total += 1
    try:
        result = candidate(key = "gymbztfkwjxehalnqosrudvpci",message = "nqzv nq p azdvmn") == "pqew pq x nevwcp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "gymbztfkwjxehalnqosrudvpci",message = "nqzv nq p azdvmn") == "pqew pq x nevwcp": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq": {e}')
    
    total += 1
    try:
        result = candidate(key = "brown fox the quick jumps over lazy dogs and",message = "ovbxc yoz spwq yvoqzgkxq vqzj qjxv ovgx") == "ctagn xcw srdk xtckwzogk tkwp kpgt ctzg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "brown fox the quick jumps over lazy dogs and",message = "ovbxc yoz spwq yvoqzgkxq vqzj qjxv ovgx") == "ctagn xcw srdk xtckwzogk tkwp kpgt ctzg": {e}')
    
    total += 1
    try:
        result = candidate(key = "qpwoeirutyalskdjfhgczxmvbn",message = "vcp o cv ocv") == "xtb d tx dtx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qpwoeirutyalskdjfhgczxmvbn",message = "vcp o cv ocv") == "xtb d tx dtx": {e}')
    
    total += 1
    try:
        result = candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv q") == "oin in i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv q") == "oin in i": {e}')
    
    total += 1
    try:
        result = candidate(key = "cijqxfyvolnmtzgdwsaehrkpbu",message = "fnw uvf uft nwg") == "fkq zhf zfm kqo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "cijqxfyvolnmtzgdwsaehrkpbu",message = "fnw uvf uft nwg") == "fkq zhf zfm kqo": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs jump quickly over the brown fox",message = "jxqy xtgy efn nhr") == "izmd ztgd ryx xus"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs jump quickly over the brown fox",message = "jxqy xtgy efn nhr") == "izmd ztgd ryx xus": {e}')
    
    total += 1
    try:
        result = candidate(key = "phinxqbcdgjkamlstvrewyzouf",message = "thx thg lv xkqhs") == "qbe qbj or elfbp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "phinxqbcdgjkamlstvrewyzouf",message = "thx thg lv xkqhs") == "qbe qbj or elfbp": {e}')
    
    total += 1
    try:
        result = candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "dru gct gct") == "uil xtk xtk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "dru gct gct") == "uil xtk xtk": {e}')
    
    total += 1
    try:
        result = candidate(key = "jxqtvknpsmuhbdrgzlcewfoaiy",message = "dgy gch dgy") == "npz psl npz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jxqtvknpsmuhbdrgzlcewfoaiy",message = "dgy gch dgy") == "npz psl npz": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "opq qpo qpo") == "opq qpo qpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "opq qpo qpo") == "opq qpo qpo": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv htk gdv jgd") == "olw per omw qom"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv htk gdv jgd") == "olw per omw qom": {e}')
    
    total += 1
    try:
        result = candidate(key = "jzkgwvqdhnmltisrfoxcabepy",message = "jwpwp yv owp") == "aexex yf rex"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jzkgwvqdhnmltisrfoxcabepy",message = "jwpwp yv owp") == "aexex yf rex": {e}')
    
    total += 1
    try:
        result = candidate(key = "wsgczxfltkbqpndohjuaevrmiy",message = "vmx gpm mvg maq") == "vxf cmx xvc xtl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "wsgczxfltkbqpndohjuaevrmiy",message = "vmx gpm mvg maq") == "vxf cmx xvc xtl": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xol mlu w yjx") == "xol mlu w yjx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xol mlu w yjx") == "xol mlu w yjx": {e}')
    
    total += 1
    try:
        result = candidate(key = "dogs quick brown fox jumps over lazy the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "sewp drle bsjoh xpgloyl sewp epos"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "dogs quick brown fox jumps over lazy the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "sewp drle bsjoh xpgloyl sewp epos": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefgijklmnopqrstuvwxyz",message = "qcp zc y") == "pco yc x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefgijklmnopqrstuvwxyz",message = "qcp zc y") == "pco yc x": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx y") == "xpo x"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx y") == "xpo x": {e}')
    
    total += 1
    try:
        result = candidate(key = "lmnopqrstuvwxyzabcdefghijk",message = "vqj qjv z") == "kfy fyk o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lmnopqrstuvwxyzabcdefghijk",message = "vqj qjv z") == "kfy fyk o": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qiy oiq z") == "qiy oiq z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qiy oiq z") == "qiy oiq z": {e}')
    
    total += 1
    try:
        result = candidate(key = "and the quick brown fox jumps over lazy dogs",message = "ovgx yoj spwq yvoqzgkxq ovbxc yjiwxtw vqzj") == "nvzq ynr utog yvngxzkqg nvlqj yrioqdo vgxr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "and the quick brown fox jumps over lazy dogs",message = "ovgx yoj spwq yvoqzgkxq ovbxc yjiwxtw vqzj") == "nvzq ynr utog yvngxzkqg nvlqj yrioqdo vgxr": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuioplkjhgfdsazxcvbnm",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "orwmp dujfh kqzgk vapyl nkcwh orwit sxbke"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuioplkjhgfdsazxcvbnm",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "orwmp dujfh kqzgk vapyl nkcwh orwit sxbke": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv z") == "mdi di m"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv z") == "mdi di m": {e}')
    
    total += 1
    try:
        result = candidate(key = "quick brown fox jumps over lazy dogs the this",message = "yvoqzgkxq ovbxc yjiwxtw vqzj qjxv spwq qjxv") == "vqhauxela hqfld vmcilyi qaum amlq poia amlq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "quick brown fox jumps over lazy dogs the this",message = "yvoqzgkxq ovbxc yjiwxtw vqzj qjxv spwq qjxv") == "vqhauxela hqfld vmcilyi qaum amlq poia amlq": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "oxj o j") == "iuq i q"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "oxj o j") == "iuq i q": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw yjx") == "sl xpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw yjx") == "sl xpo": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "v zifw ilxqfs") == "t wfnl fuodns"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "v zifw ilxqfs") == "t wfnl fuodns": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcf bfgs jgcd yqcf") == "qzcf bfgs jgcd yqcf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcf bfgs jgcd yqcf") == "qzcf bfgs jgcd yqcf": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "ulc cul cul") == "vmc cvm cvm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "ulc cul cul") == "vmc cvm cvm": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "tsr rst rst") == "ghi ihg ihg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "tsr rst rst") == "ghi ihg ihg": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qz cf") == "dw gn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qz cf") == "dw gn": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "mfir kkfr ifxk") == "znhd rrnd hnur"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "mfir kkfr ifxk") == "znhd rrnd hnur": {e}')
    
    total += 1
    try:
        result = candidate(key = "fnex wpviqkdmtlugybhcarzsoj",message = "hcv uxl") == "stg odn"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "fnex wpviqkdmtlugybhcarzsoj",message = "hcv uxl") == "stg odn": {e}')
    
    total += 1
    try:
        result = candidate(key = "zebra quick brown fox jumps over the lazy dog",message = "gqjty efn nhr htyq") == "zfpux bnm mvd vuxf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zebra quick brown fox jumps over the lazy dog",message = "gqjty efn nhr htyq") == "zfpux bnm mvd vuxf": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "vqz zqv z") == "idm mdi m"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "vqz zqv z") == "idm mdi m": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "vgj ov sa jhygjmt oh rjw") == "tzp kt sv pbxzpqa kb jpl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "vgj ov sa jhygjmt oh rjw") == "tzp kt sv pbxzpqa kb jpl": {e}')
    
    total += 1
    try:
        result = candidate(key = "bcadefghijklmnopqrstuvwxzy",message = "bdc bva jnfrdq") == "adb avc jnfrdq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "bcadefghijklmnopqrstuvwxzy",message = "bdc bva jnfrdq") == "adb avc jnfrdq": {e}')
    
    total += 1
    try:
        result = candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "wqv qv q") == "kjw jw j"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "wqv qv q") == "kjw jw j": {e}')
    
    total += 1
    try:
        result = candidate(key = "zebra tiger quick brown fox jumps over the lazy dog",message = "uybvf ojizv cfiwz nqzsx vgrb cgviy ojizv bxz") == "jycvp mrgav kpgna oiauq vhdc khvgy mrgav cqa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zebra tiger quick brown fox jumps over the lazy dog",message = "uybvf ojizv cfiwz nqzsx vgrb cgviy ojizv bxz") == "jycvp mrgav kpgna oiauq vhdc khvgy mrgav cqa": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v yvk") == "yht t xth"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v yvk") == "yht t xth": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv zc") == "mdi di mp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv zc") == "mdi di mp": {e}')
    
    total += 1
    try:
        result = candidate(key = "the brown fox jumps quickly over a lazy dog",message = "pjoj qvw xqt jqtqi yjiwxtw spwq jx gsvk yoj") == "nkfk pvg jpa kpapq ukqgjag ongp kj zovs ufk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the brown fox jumps quickly over a lazy dog",message = "pjoj qvw xqt jqtqi yjiwxtw spwq jx gsvk yoj") == "nkfk pvg jpa kpapq ukqgjag ongp kj zovs ufk": {e}')
    
    total += 1
    try:
        result = candidate(key = "this quick brown fox jumps over lazy dogs",message = "qjxv yvoqzgkxq ovbxc yjiwxtw spwq yoj vqzj") == "epos xskewzhoe ksiog xpcloal drle xkp sewp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "this quick brown fox jumps over lazy dogs",message = "qjxv yvoqzgkxq ovbxc yjiwxtw spwq yoj vqzj") == "epos xskewzhoe ksiog xpcloal drle xkp sewp": {e}')
    
    total += 1
    try:
        result = candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "sgtw xjxw xjxw") == "jxkn oaon oaon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "sgtw xjxw xjxw") == "jxkn oaon oaon": {e}')
    
    total += 1
    try:
        result = candidate(key = "a bc df egh ijkl mno pq rs tuvwxyz",message = "v lqyq w lwv yjx") == "v lqyq w lwv yjx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "a bc df egh ijkl mno pq rs tuvwxyz",message = "v lqyq w lwv yjx") == "v lqyq w lwv yjx": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcfb qmgox ypgmt gsv fiu") == "qzcfb qmgox ypgmt gsv fiu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcfb qmgox ypgmt gsv fiu") == "qzcfb qmgox ypgmt gsv fiu": {e}')
    
    total += 1
    try:
        result = candidate(key = "pqrkxlcdemosvahzwfygtnujib",message = "izv zfc yfcv") == "ypm prg srgm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "pqrkxlcdemosvahzwfygtnujib",message = "izv zfc yfcv") == "ypm prg srgm": {e}')
    
    total += 1
    try:
        result = candidate(key = "lazy dogs jump over quick brown fox the",message = "bxz bpxc wxqgc ebcjg fcivw zqzsx ojizv") == "txc tlxr uxpgr ntrig wrqmu cpchx fiqcm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "lazy dogs jump over quick brown fox the",message = "bxz bpxc wxqgc ebcjg fcivw zqzsx ojizv") == "txc tlxr uxpgr ntrig wrqmu cpchx fiqcm": {e}')
    
    total += 1
    try:
        result = candidate(key = "okyftdazhsxngijwumrcvqlpeb",message = "kqv mhg a lv vjx") == "bvu rim g wu uok"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "okyftdazhsxngijwumrcvqlpeb",message = "kqv mhg a lv vjx") == "bvu rim g wu uok": {e}')
    
    total += 1
    try:
        result = candidate(key = "the brown fox jumps quickly over a lazy dog",message = "mht zrs xqf ovkqvoq ngyu a qzfe nax") == "mba xeo jpi fvspvfp hzul w pxic hwj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the brown fox jumps quickly over a lazy dog",message = "mht zrs xqf ovkqvoq ngyu a qzfe nax") == "mba xeo jpi fvspvfp hzul w pxic hwj": {e}')
    
    total += 1
    try:
        result = candidate(key = "over lazy dogs quick brown fox jumps the this",message = "spwq vqzj spwq ovbxc yjiwxtw qjxv qjxv") == "kxrl blgv kxrl abquo hvnruyr lvub lvub"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "over lazy dogs quick brown fox jumps the this",message = "spwq vqzj spwq ovbxc yjiwxtw qjxv qjxv") == "kxrl blgv kxrl abquo hvnruyr lvub lvub": {e}')
    
    total += 1
    try:
        result = candidate(key = "the brown quick fox jumps over lazy dogs",message = "zqft gqf vxt xec ohq oizd") == "wina zin toa ocl fbi fkwy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the brown quick fox jumps over lazy dogs",message = "zqft gqf vxt xec ohq oizd") == "wina zin toa ocl fbi fkwy": {e}')
    
    total += 1
    try:
        result = candidate(key = "jumped over the lazy brown fox quick",message = "ujxqyc efn nhr htyq") == "batuow esr rki kjou"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "jumped over the lazy brown fox quick",message = "ujxqyc efn nhr htyq") == "batuow esr rki kjou": {e}')
    
    total += 1
    try:
        result = candidate(key = "fghijklmnopqrstuvwxyzabcde",message = "vrc vja vrc vja") == "qmx qev qmx qev"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "fghijklmnopqrstuvwxyzabcde",message = "vrc vja vrc vja") == "qmx qev qmx qev": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over lazy dogs and",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "srld xtkdwzhod ktiog xpfloal tdwp ktzo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over lazy dogs and",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "srld xtkdwzhod ktiog xpfloal tdwp ktzo": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qjvux xfgf q px") == "dpteo onzn d ro"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qjvux xfgf q px") == "dpteo onzn d ro": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v ydv") == "yht t xyt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v ydv") == "yht t xyt": {e}')
    
    total += 1
    try:
        result = candidate(key = "xlsnmveizhptfjugobcdkqrway",message = "wcr vcv wcv xwv") == "xsw fsf xsf axf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "xlsnmveizhptfjugobcdkqrway",message = "wcr vcv wcv xwv") == "xsw fsf xsf axf": {e}')
    
    total += 1
    try:
        result = candidate(key = "quick brown fox jumps over lazy dog the",message = "fxfsr jxqfk wtf pvuzr bcgy jxqfk dvo") == "klkpg mlake iyk oqbug fdxv mlake wqh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "quick brown fox jumps over lazy dog the",message = "fxfsr jxqfk wtf pvuzr bcgy jxqfk dvo") == "klkpg mlake iyk oqbug fdxv mlake wqh": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx w") == "xpo l"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx w") == "xpo l": {e}')
    
    total += 1
    try:
        result = candidate(key = "bdfhjlnprtvxzcgikmoqsuwyae",message = "hc vjg cji cgy") == "dn keo nep nox"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "bdfhjlnprtvxzcgikmoqsuwyae",message = "hc vjg cji cgy") == "dn keo nep nox": {e}')
    
    total += 1
    try:
        result = candidate(key = "onmlkjihgfedcbazyxwvutsrqp",message = "ixkz znxoz kx yq") == "grep pbrap er qy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "onmlkjihgfedcbazyxwvutsrqp",message = "ixkz znxoz kx yq") == "grep pbrap er qy": {e}')
    
    total += 1
    try:
        result = candidate(key = "phqgiumeaylnofdxjkrcvstzwb",message = "ixw ikg ikg ikg") == "epy erd erd erd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "phqgiumeaylnofdxjkrcvstzwb",message = "ixw ikg ikg ikg") == "epy erd erd erd": {e}')
    
    total += 1
    try:
        result = candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "wfkq xqfnk uveogvj pvuzr cfiwz rjgt jxqfk bxz") == "javt gtahv qcdficp scqkm uabjk mpiy pgtav egk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "wfkq xqfnk uveogvj pvuzr cfiwz rjgt jxqfk bxz") == "javt gtahv qcdficp scqkm uabjk mpiy pgtav egk": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "vqj qjv cv") == "waq aqw vw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "vqj qjv cv") == "waq aqw vw": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "ghw gct gct") == "ghv gcs gcs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "ghw gct gct") == "ghv gcs gcs": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "fnbv wvxm") == "nmit ltoq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "fnbv wvxm") == "nmit ltoq": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx") == "xpo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx") == "xpo": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "qnb wql fhw fql") == "zbc yzh mky mzh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "qnb wql fhw fql") == "zbc yzh mky mzh": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz",message = "anxanq azoz anu") == "anxanq azoz anu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz",message = "anxanq azoz anu") == "anxanq azoz anu": {e}')
    
    total += 1
    try:
        result = candidate(key = "thequickbrownfoxjumpsoverthelazydogs",message = "qjvux xfgf q px") == "dpteo onzn d ro"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "thequickbrownfoxjumpsoverthelazydogs",message = "qjvux xfgf q px") == "dpteo onzn d ro": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "jkq xjxw xjxw") == "ijp wiwv wiwv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "jkq xjxw xjxw") == "ijp wiwv wiwv": {e}')
    
    total += 1
    try:
        result = candidate(key = "bujgtfayrxohqzplmwdinckevs",message = "yzq d pyq o") == "hnm s ohm k"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "bujgtfayrxohqzplmwdinckevs",message = "yzq d pyq o") == "hnm s ohm k": {e}')
    
    total += 1
    try:
        result = candidate(key = "rjkylmfdqogavwunhixpctzesb",message = "tzm tmz tmh tmi") == "vwf vfw vfq vfr"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "rjkylmfdqogavwunhixpctzesb",message = "tzm tmz tmh tmi") == "vwf vfw vfq vfr": {e}')
    
    total += 1
    try:
        result = candidate(key = "the quick brown fox jumps over lazy dogs this",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj qjxv") == "srld xtkdwzhod ktiog xpfloal tdwp dpot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the quick brown fox jumps over lazy dogs this",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj qjxv") == "srld xtkdwzhod ktiog xpfloal tdwp dpot": {e}')
    
    total += 1
    try:
        result = candidate(key = "brown fox jumps over lazy dogs the quick this",message = "ovbxc yjiwxtw vqzj qjxv spwq yvoqzgkxq") == "cmagy rhxdgud mwqh whgm lkdw rmcwqtzgw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "brown fox jumps over lazy dogs the quick this",message = "ovbxc yjiwxtw vqzj qjxv spwq yvoqzgkxq") == "cmagy rhxdgud mwqh whgm lkdw rmcwqtzgw": {e}')
    
    total += 1
    try:
        result = candidate(key = "a b c d e f g h i j k l m n o p q r s t u v w x y z",message = "z k u o c g t w") == "z k u o c g t w"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "a b c d e f g h i j k l m n o p q r s t u v w x y z",message = "z k u o c g t w") == "z k u o c g t w": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gtgt nvo gtg mpgg") == "tgtg mel tgt nktt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gtgt nvo gtg mpgg") == "tgtg mel tgt nktt": {e}')
    
    total += 1
    try:
        result = candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv qv") == "oin in in"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv qv") == "oin in in": {e}')
    
    total += 1
    try:
        result = candidate(key = "mjw qzlnf hw uo kcf jehrv dpo osxgt cyqak",message = "jnjfdh frl df") == "bgbhqi hof qh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mjw qzlnf hw uo kcf jehrv dpo osxgt cyqak",message = "jnjfdh frl df") == "bgbhqi hof qh": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "vuvw xw yx za") == "wvwx yx zy ja"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "vuvw xw yx za") == "wvwx yx zy ja": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i": {e}')
    
    total += 1
    try:
        result = candidate(key = "wvutsrqponmlkjihgfedcba zyx",message = "zyxwvutsrqpnmolkjihgfedcba") == "xyzabcdefghjkilmnopqrstuvw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "wvutsrqponmlkjihgfedcba zyx",message = "zyxwvutsrqpnmolkjihgfedcba") == "xyzabcdefghjkilmnopqrstuvw": {e}')
    
    total += 1
    try:
        result = candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "vcp o cv v") == "deq r ed d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "vcp o cv v") == "deq r ed d": {e}')
    
    total += 1
    try:
        result = candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq j") == "qfa ta q"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq j") == "qfa ta q": {e}')
    
    total += 1
    try:
        result = candidate(key = "the brown fox jumps over the lazy dog quickly",message = "tqpp d dswcp gygij") == "awnn u uogyn vtvxk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "the brown fox jumps over the lazy dog quickly",message = "tqpp d dswcp gygij") == "awnn u uogyn vtvxk": {e}')
    
    total += 1
    try:
        result = candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "ixq kivk eiqb") == "rcj prep vrjy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "ixq kivk eiqb") == "rcj prep vrjy": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "wklv lv dq xvh hqw phvvdjh") == "wklv lv dq xvh hqw phvvdjh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "wklv lv dq xvh hqw phvvdjh") == "wklv lv dq xvh hqw phvvdjh": {e}')
    
    total += 1
    try:
        result = candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zcf jopcnboe wj jop") == "mps wbcpaobr jw wbc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zcf jopcnboe wj jop") == "mps wbcpaobr jw wbc": {e}')
    
    total += 1
    try:
        result = candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "xpu xh z") == "asx ak c"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "xpu xh z") == "asx ak c": {e}')
    
    total += 1
    try:
        result = candidate(key = "quick brown fox jumps over the lazy dog",message = "kxvzn hqomj jxq zpsvx wbvs hq tkgx") == "elqwj tahnm mla wopql ifqp ta sezl"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "quick brown fox jumps over the lazy dog",message = "kxvzn hqomj jxq zpsvx wbvs hq tkgx") == "elqwj tahnm mla wopql ifqp ta sezl": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv z") == "ehu zcv z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv z") == "ehu zcv z": {e}')
    
    total += 1
    try:
        result = candidate(key = "this quick brown fox jumps over lazy dogs and",message = "qjxv spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "epos drle xskewzhoe ksiog xpcloal sewp kszo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "this quick brown fox jumps over lazy dogs and",message = "qjxv spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "epos drle xskewzhoe ksiog xpcloal sewp kszo": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdef ghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdef ghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "qzdv lqaf qv yzxq") == "qzdv lqaf qv yzxq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "qzdv lqaf qv yzxq") == "qzdv lqaf qv yzxq": {e}')
    
    total += 1
    try:
        result = candidate(key = "abcdefghikjlmnopqrstuvwxyz",message = "hij iji iij") == "hik iki iik"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(key = "abcdefghikjlmnopqrstuvwxyz",message = "hij iji iij") == "hik iki iik": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "cba zyx") == "xyz abc"
    assert candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "yfcj myj pyjl ufcj myj pyjl ufcj myj pyjl") == "omer gor sorq cmer gor sorq cmer gor sorq"
    assert candidate(key = "the five boxing wizards jump quickly on this yellow pig",message = "jhxuh lqdj efxgh lpuaz fxdyjzjw") == "rbisb yvpr cdikb yusnm dipzrmrl"
    assert candidate(key = "dvhfujngcpqxlwokzriebastmy",message = "mwtiaz azr") == "ynxsvq vqr"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xyz abc") == "xyz abc"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret"
    assert candidate(key = "byvzkgxfnqmpalwodjtrshceui",message = "xsm wv zmz") == "guk oc dkd"
    assert candidate(key = "wmtresuavhigdcbfykjqploxzn",message = "lfnlccyvmdg") == "vpzvnnqibml"
    assert candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "sl rfc zdf") == "tm sgd aeg"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "mlkjhgfedcbazyxwvutsrqpon") == "nopqstuvwxyzabcdefghijklm"
    assert candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "z x c v") == "z x c v"
    assert candidate(key = "gysrnhxvaofcedwmltukipjbqz",message = "gigv symykgl igxvxjxg") == "auah cbpbtaq uaghgwga"
    assert candidate(key = "phinxajsgkrzcwvltqbdemoufy",message = "xvo wv pmj") == "eow no avg"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zaoymnbxcqrljtheifkgdvspwu") == "zaoymnbxcqrljtheifkgdvspwu"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv jfrxp yildm ulc") == "olw qnduj fhsmz gsv"
    assert candidate(key = "the five boxing wizards jump quickly on this june day",message = "ymj lvfx sflhzymhs vxlw wjymjlvfx sflhzymhs") == "ztr yfdi qdybmztbq fiyl lrztryfdi qdybmztbq"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "thequ ickbr ownfo xjump sover thela zydog"
    assert candidate(key = "dfghjklwcvxziomnpqrustyabe",message = "kckd ykky") == "fifa wffw"
    assert candidate(key = "mnychdpbxofl wgviakjuzterqs",message = "irhvmvccsjb") == "pxeoaoddzsh"
    assert candidate(key = "pack my box with five dozen liquor jugs",message = "xujf qv zgy jxpx qne nfgqj sraju") == "ivxn uo ryf xiai usp snyux zwbxv"
    assert candidate(key = "mwp dhxjzvcqrkbyanflstguoei",message = "di vccvmr wv czebwqha wv iv lvyrj") == "dz ijjial bi jhynbkep bi zi siolg"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "a b c d") == "z y x w"
    assert candidate(key = "the five boxing wizards jump quickly",message = "fmwp vifd ttp xosmead") == "dtlu fedp aau ihqtcnp"
    assert candidate(key = "vuqangfkswjpryxtdmzobhcile",message = "wfn yv yfcv") == "jge na ngwa"
    assert candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "eiqhw fjq hwdq") == "eiqhw fjq hwdq"
    assert candidate(key = "a quick movement of the enemy will jeopardize five gunboats",message = "zruog glhvg frp fvdw zl glcgv") == "vtchw wqniw mts miup vq wqewi"
    assert candidate(key = "thejumpsquickbrownfoxoverlazydog",message = "svhjyjsiqphsjudprvcbgijz") == "htbdxdhjigbhdeygntkmzjdw"
    assert candidate(key = "ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az",message = "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz") == "qz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz vz"
    assert candidate(key = "swzybfrxlnaoumdgtqivhjkpce",message = "flgxswdliefyirukyoaqmpjc") == "fiphaboiszfdsgmwdlkrnxvy"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "qruqz efn nhr htyq") == "djedw cnm mbj baxd"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "xibohu uvp xibohu") == "ofikbe etr ofikbe"
    assert candidate(key = "abcd efgh ijkl mnop qrst uvwx yz",message = "vuwx yz abcd ef") == "vuwx yz abcd ef"
    assert candidate(key = "gymnopqrstuvwxzabcdefhiljk",message = "xqmgq zm zmjy") == "ngcag oc ocyb"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yxe xe xe") == "bcv cv cv"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",message = "abc def abc") == "abc def abc"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "vxp qpy o") == "vxp qpy o"
    assert candidate(key = "jumps over the lazy dog quick brown fox",message = "pvuzr cgviy ojizv bxz cfiwz nqzsx vgrb") == "dgbni tqgso fasng vzn tyswn xrnez gqiv"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "xqf") == "odn"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "gfn") == "znm"
    assert candidate(key = "pzucfelxwyabqomtjirdnsvhgk",message = "kwj kwi kwv wkv") == "ziq zir ziw izw"
    assert candidate(key = "fmwtkujhpnobxigcsqrzydalve",message = "fyh fyt fyv yfj") == "auh aud auy uag"
    assert candidate(key = "abcdefghij klmnopqrstuvwxyz",message = "qzcfj nx ud qzcfj") == "qzcfj nx ud qzcfj"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx x") == "xpo o"
    assert candidate(key = "jumps over lazy dogs quick brown fox the this",message = "yjiwxtw vqzj spwq ovbxc yoz qjxv") == "maquxyu gpla edup fgtxr mfl paxg"
    assert candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "frg fmh gfn") == "wix wdy xwe"
    assert candidate(key = "zabcdefghijklmnopqrstuvwxy",message = "qxy xyx yxq") == "ryz yzy zyr"
    assert candidate(key = "the quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog",message = "vkbs bs t suepuv") == "this is a secret"
    assert candidate(key = "ekmflgdqvzntowyhxuspaibrcj",message = "jbs xut hig") == "zws qrl pvf"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "iyh uhy l") == "rbs fsb o"
    assert candidate(key = "vwxymnbcdfghjklqropstuzaike",message = "vcp o cv vcp") == "ahs r ha ahs"
    assert candidate(key = "ajfzldkgotmhrvwsypnqicxebu",message = "oxt oxi oxd xot") == "iwj iwu iwf wij"
    assert candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "wfn yv yfcv") == "nwe pm pwtm"
    assert candidate(key = "tevosjhbnyxrgqkfaumzilwpcd",message = "npu gpm gpy lgg") == "ixr mxs mxj vmm"
    assert candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "hfu q jhu") == "kmt z jkt"
    assert candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "yqz dpy o") == "ojt cso r"
    assert candidate(key = "qbnvgjlftscxkouwamdphzreiy",message = "umr urv urm pyz") == "orw owd owr tzv"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "zqj dpy o") == "taq mjf i"
    assert candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "qzyc yvzctv yxqjvzq yjiwxtw on qjxv yoj") == "tkxu xckuyc xgtpckt xpbjgyj fh tpgc xfp"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "c e") == "g c"
    assert candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "lii eil eil") == "mii eim eim"
    assert candidate(key = "vxznpqjwoefkytlimrdhaguscb",message = "tyf iy tf") == "nmk pm nk"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw uqz") == "sl edw"
    assert candidate(key = "jxwtrklivnpmhudsfgcayzbeoq",message = "kcfizgv zr ocfv") == "fsqhvri ve ysqi"
    assert candidate(key = "lazy dogs quick brown fox jumps over the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "wict hvpi fwnsl dtkpsyp wict itsw"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx z") == "xpo w"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "mlml qmf lml gmgg") == "mlml qmf lml gmgg"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "vz") == "tw"
    assert candidate(key = "dbrujxfgzvcotwiympnslakqhe",message = "kmqs ks u kqsebs") == "wqxt wt d wxtzbt"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "wqiv xi sqin sqin") == "ldft of sdfm sdfm"
    assert candidate(key = "dtjgsvyzxpkbfqwulcmohraeni",message = "obr obn oti atn") == "tlv tly tbz wby"
    assert candidate(key = "abcdefghijk lmnopqrstuvwxyz",message = "svil km ybgu bg ujr krkhi yjr cvvux") == "svil km ybgu bg ujr krkhi yjr cvvux"
    assert candidate(key = "the quick brown fox jumps over lazy dogs",message = "mht zrs xqf ovkqvoq ngyu kgxqj bpxc") == "qba wjs odn kthdtkd mzxe hzodp irog"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq o") == "qfa ta i"
    assert candidate(key = "gibrfqotdhewakjyzlxmvncpus",message = "yxh lo loxhy") == "psj rg rgsjp"
    assert candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "aov eovm eovm") == "ocj scja scja"
    assert candidate(key = "zxvtrqponmlkjihgfedcbazyw",message = "ajc eajc eajc") == "vmt rvmt rvmt"
    assert candidate(key = "gfedcbauioplkjhzyxwvtsrqmn",message = "ixv yxv oxv") == "irt qrt jrt"
    assert candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "wvf v fv") == "zyi y iy"
    assert candidate(key = "abc def ghijk lmnop qrst uvwxyz",message = "nvmjy nbsytw") == "nvmjy nbsytw"
    assert candidate(key = "eljuxhpwnyrdgtqkviszcfmabo",message = "ihd hsih xihw gh hsi") == "rfl fsrf erfh mf fsr"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv q") == "mdi di d"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "qytz nwt zwt") == "dxaw mla wla"
    assert candidate(key = "quick brown fox jumps over the lazy dog and the quick brown fox jumps",message = "vxw aov g pufa ohq") == "qli vhq z obkv hta"
    assert candidate(key = "vbnmxczasdfghjklpoiuytrewq",message = "vkbs bs t suepuv") == "aobi bi v itxqta"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "yvc zc yz") == "bex ax ba"
    assert candidate(key = "azbycxdwevfugthrskjqplomni",message = "tqppf ptd je") == "ntuuk ung si"
    assert candidate(key = "xylophone qwertyuiop asdfghjklz cvbnm",message = "cvmu cvxqv") == "wxzm wxaix"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "lqtfw xtg twkxq") == "saenb ueo ebrua"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx v") == "xpo t"
    assert candidate(key = "nmqpviwedklxzfgrctuhyjasob",message = "ohc oha ohu voh") == "ytq ytw yts eyt"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "izk zkh bva jnfrdq") == "vmx mxu oin waseqd"
    assert candidate(key = "quick brown fox jumps over the lazy dog",message = "rwjsi exmti gsrhri zv wimtix egzewy") == "gimpc rlnsc zpgtgc wq icnscl rzwrix"
    assert candidate(key = "lazy dogs jumps over the quick brown fox the",message = "vqzj yjiwxtw spwq yoj spwq ovbxc yoz") == "mrci diswzpw hlwr dfi hlwr fmvzt dfc"
    assert candidate(key = "mnopqrstuvwxyzabcdefghijkl",message = "mud gct gct") == "air uqh uqh"
    assert candidate(key = "lazy dogs jumps quickly over the brown fox and",message = "vqzj yjiwxtw spwq yoj ovbxc yoz") == "qmci dinwztw hlwm dfi fqvzo dfc"
    assert candidate(key = "vzhofucmlnjqbdspartexwiykg",message = "dpy ld o yv") == "npx in d xa"
    assert candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "cv lpcv") == "ed hqed"
    assert candidate(key = "the lazy dog jumps over the quick brown fox",message = "qjxv yoj vqzj spwq yjiwxtw ovbxc yvoqzgkxq") == "rkzp gik prfk onwr gkswzaw ipvzt gpirfjuzr"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx yjx") == "xpo xpo"
    assert candidate(key = "cvzkgbxquihmpnytjrsdawolef",message = "cfr cfd cfl mfl") == "azr azt azx lzx"
    assert candidate(key = "lazy dogs jumps quickly over the brown fox the",message = "vqzj yjiwxtw spwq yoj ovbxc yoj") == "qmci dinwztw hlwm dfi fqvzo dfi"
    assert candidate(key = "thezyxwvutsrqponmlkjihgfedcba",message = "zqv eovm ztqkofv ztqkofv") == "dlh cnhp dalrnvh dalrnvh"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "evh vhe yhe") == "ves esv bsv"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "zqf ykq fqu fqo ykt nqtk") == "wdn xhd nde ndk xha mdah"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "hqv v yhqf") == "hqv v yhqf"
    assert candidate(key = "ponmlkjihgfedcbazyxwvutsrq",message = "jxqy xtgy efn nhr") == "gszr swjr lkc ciy"
    assert candidate(key = "gymbztfkwjxehalnqosrudvpci",message = "nqzv nq p azdvmn") == "pqew pq x nevwcp"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq"
    assert candidate(key = "brown fox the quick jumps over lazy dogs and",message = "ovbxc yoz spwq yvoqzgkxq vqzj qjxv ovgx") == "ctagn xcw srdk xtckwzogk tkwp kpgt ctzg"
    assert candidate(key = "qpwoeirutyalskdjfhgczxmvbn",message = "vcp o cv ocv") == "xtb d tx dtx"
    assert candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv q") == "oin in i"
    assert candidate(key = "cijqxfyvolnmtzgdwsaehrkpbu",message = "fnw uvf uft nwg") == "fkq zhf zfm kqo"
    assert candidate(key = "lazy dogs jump quickly over the brown fox",message = "jxqy xtgy efn nhr") == "izmd ztgd ryx xus"
    assert candidate(key = "phinxqbcdgjkamlstvrewyzouf",message = "thx thg lv xkqhs") == "qbe qbj or elfbp"
    assert candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "dru gct gct") == "uil xtk xtk"
    assert candidate(key = "jxqtvknpsmuhbdrgzlcewfoaiy",message = "dgy gch dgy") == "npz psl npz"
    assert candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "opq qpo qpo") == "opq qpo qpo"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "gsv htk gdv jgd") == "olw per omw qom"
    assert candidate(key = "jzkgwvqdhnmltisrfoxcabepy",message = "jwpwp yv owp") == "aexex yf rex"
    assert candidate(key = "wsgczxfltkbqpndohjuaevrmiy",message = "vmx gpm mvg maq") == "vxf cmx xvc xtl"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "xol mlu w yjx") == "xol mlu w yjx"
    assert candidate(key = "dogs quick brown fox jumps over lazy the this",message = "vqzj spwq ovbxc yjiwxtw vqzj qjxv") == "sewp drle bsjoh xpgloyl sewp epos"
    assert candidate(key = "abcdefgijklmnopqrstuvwxyz",message = "qcp zc y") == "pco yc x"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx y") == "xpo x"
    assert candidate(key = "lmnopqrstuvwxyzabcdefghijk",message = "vqj qjv z") == "kfy fyk o"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qiy oiq z") == "qiy oiq z"
    assert candidate(key = "and the quick brown fox jumps over lazy dogs",message = "ovgx yoj spwq yvoqzgkxq ovbxc yjiwxtw vqzj") == "nvzq ynr utog yvngxzkqg nvlqj yrioqdo vgxr"
    assert candidate(key = "qwertyuioplkjhgfdsazxcvbnm",message = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt") == "orwmp dujfh kqzgk vapyl nkcwh orwit sxbke"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv z") == "mdi di m"
    assert candidate(key = "quick brown fox jumps over lazy dogs the this",message = "yvoqzgkxq ovbxc yjiwxtw vqzj qjxv spwq qjxv") == "vqhauxela hqfld vmcilyi qaum amlq poia amlq"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "oxj o j") == "iuq i q"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "sw yjx") == "sl xpo"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "v zifw ilxqfs") == "t wfnl fuodns"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcf bfgs jgcd yqcf") == "qzcf bfgs jgcd yqcf"
    assert candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "ulc cul cul") == "vmc cvm cvm"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "tsr rst rst") == "ghi ihg ihg"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qz cf") == "dw gn"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "mfir kkfr ifxk") == "znhd rrnd hnur"
    assert candidate(key = "fnex wpviqkdmtlugybhcarzsoj",message = "hcv uxl") == "stg odn"
    assert candidate(key = "zebra quick brown fox jumps over the lazy dog",message = "gqjty efn nhr htyq") == "zfpux bnm mvd vuxf"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "vqz zqv z") == "idm mdi m"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "vgj ov sa jhygjmt oh rjw") == "tzp kt sv pbxzpqa kb jpl"
    assert candidate(key = "bcadefghijklmnopqrstuvwxzy",message = "bdc bva jnfrdq") == "adb avc jnfrdq"
    assert candidate(key = "asdfghjklqwertyuiopzxcvbnm",message = "wqv qv q") == "kjw jw j"
    assert candidate(key = "zebra tiger quick brown fox jumps over the lazy dog",message = "uybvf ojizv cfiwz nqzsx vgrb cgviy ojizv bxz") == "jycvp mrgav kpgna oiauq vhdc khvgy mrgav cqa"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v yvk") == "yht t xth"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zqv qv zc") == "mdi di mp"
    assert candidate(key = "the brown fox jumps quickly over a lazy dog",message = "pjoj qvw xqt jqtqi yjiwxtw spwq jx gsvk yoj") == "nkfk pvg jpa kpapq ukqgjag ongp kj zovs ufk"
    assert candidate(key = "this quick brown fox jumps over lazy dogs",message = "qjxv yvoqzgkxq ovbxc yjiwxtw spwq yoj vqzj") == "epos xskewzhoe ksiog xpcloal drle xkp sewp"
    assert candidate(key = "jklmnopqrstuvwxyzabcdefghi",message = "sgtw xjxw xjxw") == "jxkn oaon oaon"
    assert candidate(key = "a bc df egh ijkl mno pq rs tuvwxyz",message = "v lqyq w lwv yjx") == "v lqyq w lwv yjx"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "qzcfb qmgox ypgmt gsv fiu") == "qzcfb qmgox ypgmt gsv fiu"
    assert candidate(key = "pqrkxlcdemosvahzwfygtnujib",message = "izv zfc yfcv") == "ypm prg srgm"
    assert candidate(key = "lazy dogs jump over quick brown fox the",message = "bxz bpxc wxqgc ebcjg fcivw zqzsx ojizv") == "txc tlxr uxpgr ntrig wrqmu cpchx fiqcm"
    assert candidate(key = "okyftdazhsxngijwumrcvqlpeb",message = "kqv mhg a lv vjx") == "bvu rim g wu uok"
    assert candidate(key = "the brown fox jumps quickly over a lazy dog",message = "mht zrs xqf ovkqvoq ngyu a qzfe nax") == "mba xeo jpi fvspvfp hzul w pxic hwj"
    assert candidate(key = "over lazy dogs quick brown fox jumps the this",message = "spwq vqzj spwq ovbxc yjiwxtw qjxv qjxv") == "kxrl blgv kxrl abquo hvnruyr lvub lvub"
    assert candidate(key = "the brown quick fox jumps over lazy dogs",message = "zqft gqf vxt xec ohq oizd") == "wina zin toa ocl fbi fkwy"
    assert candidate(key = "jumped over the lazy brown fox quick",message = "ujxqyc efn nhr htyq") == "batuow esr rki kjou"
    assert candidate(key = "fghijklmnopqrstuvwxyzabcde",message = "vrc vja vrc vja") == "qmx qev qmx qev"
    assert candidate(key = "the quick brown fox jumps over lazy dogs and",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "srld xtkdwzhod ktiog xpfloal tdwp ktzo"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "qjvux xfgf q px") == "dpteo onzn d ro"
    assert candidate(key = "the quick brown fox jumps over the lazy dog",message = "dkv v ydv") == "yht t xyt"
    assert candidate(key = "xlsnmveizhptfjugobcdkqrway",message = "wcr vcv wcv xwv") == "xsw fsf xsf axf"
    assert candidate(key = "quick brown fox jumps over lazy dog the",message = "fxfsr jxqfk wtf pvuzr bcgy jxqfk dvo") == "klkpg mlake iyk oqbug fdxv mlake wqh"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx w") == "xpo l"
    assert candidate(key = "bdfhjlnprtvxzcgikmoqsuwyae",message = "hc vjg cji cgy") == "dn keo nep nox"
    assert candidate(key = "onmlkjihgfedcbazyxwvutsrqp",message = "ixkz znxoz kx yq") == "grep pbrap er qy"
    assert candidate(key = "phqgiumeaylnofdxjkrcvstzwb",message = "ixw ikg ikg ikg") == "epy erd erd erd"
    assert candidate(key = "five boxing wizards jump quickly on this lazy dog",message = "wfkq xqfnk uveogvj pvuzr cfiwz rjgt jxqfk bxz") == "javt gtahv qcdficp scqkm uabjk mpiy pgtav egk"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "vqj qjv cv") == "waq aqw vw"
    assert candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "ghw gct gct") == "ghv gcs gcs"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "fnbv wvxm") == "nmit ltoq"
    assert candidate(key = "the quick brown fox jumps over the lazy dogs",message = "yjx") == "xpo"
    assert candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "qnb wql fhw fql") == "zbc yzh mky mzh"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz",message = "anxanq azoz anu") == "anxanq azoz anu"
    assert candidate(key = "thequickbrownfoxjumpsoverthelazydogs",message = "qjvux xfgf q px") == "dpteo onzn d ro"
    assert candidate(key = "abcdefghjklmnopqrstuvwxyzti",message = "jkq xjxw xjxw") == "ijp wiwv wiwv"
    assert candidate(key = "bujgtfayrxohqzplmwdinckevs",message = "yzq d pyq o") == "hnm s ohm k"
    assert candidate(key = "rjkylmfdqogavwunhixpctzesb",message = "tzm tmz tmh tmi") == "vwf vfw vfq vfr"
    assert candidate(key = "the quick brown fox jumps over lazy dogs this",message = "spwq yvoqzgkxq ovbxc yjiwxtw vqzj qjxv") == "srld xtkdwzhod ktiog xpfloal tdwp dpot"
    assert candidate(key = "brown fox jumps over lazy dogs the quick this",message = "ovbxc yjiwxtw vqzj qjxv spwq yvoqzgkxq") == "cmagy rhxdgud mwqh whgm lkdw rmcwqtzgw"
    assert candidate(key = "a b c d e f g h i j k l m n o p q r s t u v w x y z",message = "z k u o c g t w") == "z k u o c g t w"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "gtgt nvo gtg mpgg") == "tgtg mel tgt nktt"
    assert candidate(key = "ijklmnopqrstuvwxyzabcdefgh",message = "wqv qv qv") == "oin in in"
    assert candidate(key = "mjw qzlnf hw uo kcf jehrv dpo osxgt cyqak",message = "jnjfdh frl df") == "bgbhqi hof qh"
    assert candidate(key = "abcdefghizjklmnopqrstuvwxy",message = "vuvw xw yx za") == "wvwx yx zy ja"
    assert candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv i") == "ehu zcv i"
    assert candidate(key = "wvutsrqponmlkjihgfedcba zyx",message = "zyxwvutsrqpnmolkjihgfedcba") == "xyzabcdefghjkilmnopqrstuvw"
    assert candidate(key = "mnbvcxzlkjhgfdsapoiuytrewq",message = "vcp o cv v") == "deq r ed d"
    assert candidate(key = "qwertyuiopasdfghjklzxcvbnm",message = "jyq zq j") == "qfa ta q"
    assert candidate(key = "the brown fox jumps over the lazy dog quickly",message = "tqpp d dswcp gygij") == "awnn u uogyn vtvxk"
    assert candidate(key = "zyxwvutsrqponmlkjihgfedcba",message = "ixq kivk eiqb") == "rcj prep vrjy"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "wklv lv dq xvh hqw phvvdjh") == "wklv lv dq xvh hqw phvvdjh"
    assert candidate(key = "nopqrstuvwxyzabcdefghijklm",message = "zcf jopcnboe wj jop") == "mps wbcpaobr jw wbc"
    assert candidate(key = "xyzabcdefghijklmnopqrstuvw",message = "xpu xh z") == "asx ak c"
    assert candidate(key = "quick brown fox jumps over the lazy dog",message = "kxvzn hqomj jxq zpsvx wbvs hq tkgx") == "elqwj tahnm mla wopql ifqp ta sezl"
    assert candidate(key = "abcdefghijklmnopqrstuvwxyz",message = "ehu zcv z") == "ehu zcv z"
    assert candidate(key = "this quick brown fox jumps over lazy dogs and",message = "qjxv spwq yvoqzgkxq ovbxc yjiwxtw vqzj ovgx") == "epos drle xskewzhoe ksiog xpcloal sewp kszo"
    assert candidate(key = "abcdef ghijklmnopqrstuvwxyz",message = "zcf bvg jnfrdq") == "zcf bvg jnfrdq"
    assert candidate(key = "abcdefghijklnmopqrstuvwxyz",message = "qzdv lqaf qv yzxq") == "qzdv lqaf qv yzxq"
    assert candidate(key = "abcdefghikjlmnopqrstuvwxyz",message = "hij iji iij") == "hik iki iik"


