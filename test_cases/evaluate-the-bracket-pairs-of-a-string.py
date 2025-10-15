def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)",knowledge = [['a', '1'], ['b', '2'], ['c', '3']]) == "123?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)",knowledge = [['a', '1'], ['b', '2'], ['c', '3']]) == "123?": {e}')
    
    total += 1
    try:
        result = candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa": {e}')
    
    total += 1
    try:
        result = candidate(s = "",knowledge = []) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "",knowledge = []) == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "noknowledgehere",knowledge = []) == "noknowledgehere"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "noknowledgehere",knowledge = []) == "noknowledgehere": {e}')
    
    total += 1
    try:
        result = candidate(s = "no(brackets)here",knowledge = []) == "no?here"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "no(brackets)here",knowledge = []) == "no?here": {e}')
    
    total += 1
    try:
        result = candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(nested)but(not)really",knowledge = [['nested', 'nested'], ['not', 'not']]) == "nestedbutnotreally"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(nested)but(not)really",knowledge = [['nested', 'nested'], ['not', 'not']]) == "nestedbutnotreally": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2?": {e}')
    
    total += 1
    try:
        result = candidate(s = "this(is)a(test)",knowledge = [['is', 'was'], ['test', 'trial']]) == "thiswasatrial"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "this(is)a(test)",knowledge = [['is', 'was'], ['test', 'trial']]) == "thiswasatrial": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)(key2)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)(key2)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2": {e}')
    
    total += 1
    try:
        result = candidate(s = "(single)",knowledge = [['single', 'one']]) == "one"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(single)",knowledge = [['single', 'one']]) == "one": {e}')
    
    total += 1
    try:
        result = candidate(s = "(last)one",knowledge = [['last', 'final']]) == "finalone"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(last)one",knowledge = [['last', 'final']]) == "finalone": {e}')
    
    total += 1
    try:
        result = candidate(s = "single",knowledge = [['single', 'word']]) == "single"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "single",knowledge = [['single', 'word']]) == "single": {e}')
    
    total += 1
    try:
        result = candidate(s = "hello",knowledge = []) == "hello"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "hello",knowledge = []) == "hello": {e}')
    
    total += 1
    try:
        result = candidate(s = "(unknown)key",knowledge = [['known', 'value']]) == "?key"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(unknown)key",knowledge = [['known', 'value']]) == "?key": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'val1'], ['key2', 'val2'], ['key3', 'val3']]) == "val1val2val3"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'val1'], ['key2', 'val2'], ['key3', 'val3']]) == "val1val2val3": {e}')
    
    total += 1
    try:
        result = candidate(s = "(book)written(by)(author)",knowledge = [['book', '1984'], ['author', 'George']]) == "1984written?George"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(book)written(by)(author)",knowledge = [['book', '1984'], ['author', 'George']]) == "1984written?George": {e}')
    
    total += 1
    try:
        result = candidate(s = "(city)(in)(country)",knowledge = [['city', 'Tokyo'], ['country', 'Japan']]) == "Tokyo?Japan"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(city)(in)(country)",knowledge = [['city', 'Tokyo'], ['country', 'Japan']]) == "Tokyo?Japan": {e}')
    
    total += 1
    try:
        result = candidate(s = "(nested)(key)(nested)",knowledge = [['key', 'value'], ['nested', 'deep']]) == "deepvaluedeep"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(nested)(key)(nested)",knowledge = [['key', 'value'], ['nested', 'deep']]) == "deepvaluedeep": {e}')
    
    total += 1
    try:
        result = candidate(s = "(ingredient)requiresto(cooktime)mins",knowledge = [['ingredient', 'Cookies'], ['cooktime', '15']]) == "Cookiesrequiresto15mins"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(ingredient)requiresto(cooktime)mins",knowledge = [['ingredient', 'Cookies'], ['cooktime', '15']]) == "Cookiesrequiresto15mins": {e}')
    
    total += 1
    try:
        result = candidate(s = "(one)(two)(three)(four)(five)",knowledge = [['one', '1'], ['two', '2'], ['three', '3'], ['four', '4']]) == "1234?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(one)(two)(three)(four)(five)",knowledge = [['one', '1'], ['two', '2'], ['three', '3'], ['four', '4']]) == "1234?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(customer)(order)at(store)",knowledge = [['customer', 'Alice'], ['order', 'Order123']]) == "AliceOrder123at?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(customer)(order)at(store)",knowledge = [['customer', 'Alice'], ['order', 'Order123']]) == "AliceOrder123at?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(keyA)and(keyB)and(keyC)and(keyD)",knowledge = [['keyA', 'valA'], ['keyB', 'valB']]) == "valAandvalBand?and?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(keyA)and(keyB)and(keyC)and(keyD)",knowledge = [['keyA', 'valA'], ['keyB', 'valB']]) == "valAandvalBand?and?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key)with(missing)knowledge",knowledge = [['key', 'value1'], ['missing', 'value2'], ['knowledge', 'value3']]) == "value1withvalue2knowledge"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key)with(missing)knowledge",knowledge = [['key', 'value1'], ['missing', 'value2'], ['knowledge', 'value3']]) == "value1withvalue2knowledge": {e}')
    
    total += 1
    try:
        result = candidate(s = "(greeting)(world)(planet)",knowledge = [['greeting', 'hello'], ['world', 'earth'], ['planet', 'mars']]) == "helloearthmars"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(greeting)(world)(planet)",knowledge = [['greeting', 'hello'], ['world', 'earth'], ['planet', 'mars']]) == "helloearthmars": {e}')
    
    total += 1
    try:
        result = candidate(s = "(this)(is)(a)(test)(string)(with)(multiple)(keys)",knowledge = [['this', 'it'], ['is', 'be'], ['a', 'an'], ['test', 'example'], ['string', 'sequence'], ['with', 'having'], ['multiple', 'several'], ['keys', 'identifiers']]) == "itbeanexamplesequencehavingseveralidentifiers"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(this)(is)(a)(test)(string)(with)(multiple)(keys)",knowledge = [['this', 'it'], ['is', 'be'], ['a', 'an'], ['test', 'example'], ['string', 'sequence'], ['with', 'having'], ['multiple', 'several'], ['keys', 'identifiers']]) == "itbeanexamplesequencehavingseveralidentifiers": {e}')
    
    total += 1
    try:
        result = candidate(s = "(language)programmingis(fun)",knowledge = [['language', 'python'], ['fun', 'awesome']]) == "pythonprogrammingisawesome"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(language)programmingis(fun)",knowledge = [['language', 'python'], ['fun', 'awesome']]) == "pythonprogrammingisawesome": {e}')
    
    total += 1
    try:
        result = candidate(s = "(fruit)(vegetable)",knowledge = [['fruit', 'apple'], ['vegetable', 'carrot']]) == "applecarrot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(fruit)(vegetable)",knowledge = [['fruit', 'apple'], ['vegetable', 'carrot']]) == "applecarrot": {e}')
    
    total += 1
    try:
        result = candidate(s = "(animal)lives(in)(habitat)",knowledge = [['animal', 'tiger'], ['habitat', 'jungle']]) == "tigerlives?jungle"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(animal)lives(in)(habitat)",knowledge = [['animal', 'tiger'], ['habitat', 'jungle']]) == "tigerlives?jungle": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)has(age)yearsand(occupation)",knowledge = [['name', 'Alice'], ['age', '30']]) == "Alicehas30yearsand?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)has(age)yearsand(occupation)",knowledge = [['name', 'Alice'], ['age', '30']]) == "Alicehas30yearsand?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(longkey)(anotherkey)(yetanotherkey)",knowledge = [['longkey', 'averylongvalue'], ['anotherkey', 'shortval'], ['yetanotherkey', 'value']]) == "averylongvalueshortvalvalue"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(longkey)(anotherkey)(yetanotherkey)",knowledge = [['longkey', 'averylongvalue'], ['anotherkey', 'shortval'], ['yetanotherkey', 'value']]) == "averylongvalueshortvalvalue": {e}')
    
    total += 1
    try:
        result = candidate(s = "(language)is(cool)",knowledge = [['language', 'Python'], ['cool', 'awesome']]) == "Pythonisawesome"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(language)is(cool)",knowledge = [['language', 'Python'], ['cool', 'awesome']]) == "Pythonisawesome": {e}')
    
    total += 1
    try:
        result = candidate(s = "(first)and(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnanddoename"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(first)and(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnanddoename": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)is(living)(in)(city)",knowledge = [['name', 'bob'], ['in', 'at'], ['city', 'london']]) == "bobis?atlondon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)is(living)(in)(city)",knowledge = [['name', 'bob'], ['in', 'at'], ['city', 'london']]) == "bobis?atlondon": {e}')
    
    total += 1
    try:
        result = candidate(s = "(animal)(eats)(food)",knowledge = [['animal', 'lion'], ['food', 'meat']]) == "lion?meat"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(animal)(eats)(food)",knowledge = [['animal', 'lion'], ['food', 'meat']]) == "lion?meat": {e}')
    
    total += 1
    try:
        result = candidate(s = "(user)likes(to)(eat)(food)",knowledge = [['user', 'alice'], ['eat', 'enjoy'], ['food', 'pizza']]) == "alicelikes?enjoypizza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(user)likes(to)(eat)(food)",knowledge = [['user', 'alice'], ['eat', 'enjoy'], ['food', 'pizza']]) == "alicelikes?enjoypizza": {e}')
    
    total += 1
    try:
        result = candidate(s = "(prefix)middle(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "startmiddleend"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(prefix)middle(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "startmiddleend": {e}')
    
    total += 1
    try:
        result = candidate(s = "(flower)grows(in)(soil)",knowledge = [['flower', 'rose'], ['soil', 'dirt']]) == "rosegrows?dirt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(flower)grows(in)(soil)",knowledge = [['flower', 'rose'], ['soil', 'dirt']]) == "rosegrows?dirt": {e}')
    
    total += 1
    try:
        result = candidate(s = "(first)nameis(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnnameisdoename"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(first)nameis(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnnameisdoename": {e}')
    
    total += 1
    try:
        result = candidate(s = "(longkey1)and(longkey2)and(longkey3)and(longkey4)",knowledge = [['longkey1', 'value1'], ['longkey2', 'value2'], ['longkey3', 'value3'], ['longkey4', 'value4']]) == "value1andvalue2andvalue3andvalue4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(longkey1)and(longkey2)and(longkey3)and(longkey4)",knowledge = [['longkey1', 'value1'], ['longkey2', 'value2'], ['longkey3', 'value3'], ['longkey4', 'value4']]) == "value1andvalue2andvalue3andvalue4": {e}')
    
    total += 1
    try:
        result = candidate(s = "(department)islocatedat(address)",knowledge = [['department', 'Sales'], ['address', '123BusinessSt']]) == "Salesislocatedat123BusinessSt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(department)islocatedat(address)",knowledge = [['department', 'Sales'], ['address', '123BusinessSt']]) == "Salesislocatedat123BusinessSt": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)has(a)(pet)",knowledge = [['name', 'Mary'], ['pet', 'dog']]) == "Maryhas?dog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)has(a)(pet)",knowledge = [['name', 'Mary'], ['pet', 'dog']]) == "Maryhas?dog": {e}')
    
    total += 1
    try:
        result = candidate(s = "(drink)is(served)in(glass)",knowledge = [['drink', 'water'], ['glass', 'big']]) == "wateris?inbig"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(drink)is(served)in(glass)",knowledge = [['drink', 'water'], ['glass', 'big']]) == "wateris?inbig": {e}')
    
    total += 1
    try:
        result = candidate(s = "prefix(key1)middle(key2)suffix",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "prefixvalue1middlevalue2suffix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "prefix(key1)middle(key2)suffix",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "prefixvalue1middlevalue2suffix": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)(key2)(key1)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2value1"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)(key2)(key1)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2value1": {e}')
    
    total += 1
    try:
        result = candidate(s = "(item1)(item2)(item3)(item4)",knowledge = [['item1', 'itemA'], ['item2', 'itemB'], ['item4', 'itemD']]) == "itemAitemB?itemD"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(item1)(item2)(item3)(item4)",knowledge = [['item1', 'itemA'], ['item2', 'itemB'], ['item4', 'itemD']]) == "itemAitemB?itemD": {e}')
    
    total += 1
    try:
        result = candidate(s = "(greeting)world",knowledge = [['greeting', 'hello'], ['farewell', 'bye']]) == "helloworld"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(greeting)world",knowledge = [['greeting', 'hello'], ['farewell', 'bye']]) == "helloworld": {e}')
    
    total += 1
    try:
        result = candidate(s = "(user)(name)livesin(city)with(zip)",knowledge = [['user', 'John'], ['city', 'San Francisco'], ['zip', '94111']]) == "John?livesinSan Franciscowith94111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(user)(name)livesin(city)with(zip)",knowledge = [['user', 'John'], ['city', 'San Francisco'], ['zip', '94111']]) == "John?livesinSan Franciscowith94111": {e}')
    
    total += 1
    try:
        result = candidate(s = "(person)(from)(place)isvisiting(placeofinterest)",knowledge = [['person', 'Bob'], ['from', 'LosAngeles'], ['place', 'SanFrancisco'], ['placeofinterest', 'Alcatraz']]) == "BobLosAngelesSanFranciscoisvisitingAlcatraz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(person)(from)(place)isvisiting(placeofinterest)",knowledge = [['person', 'Bob'], ['from', 'LosAngeles'], ['place', 'SanFrancisco'], ['placeofinterest', 'Alcatraz']]) == "BobLosAngelesSanFranciscoisvisitingAlcatraz": {e}')
    
    total += 1
    try:
        result = candidate(s = "(longkeyname)is(longervaluename)",knowledge = [['longkeyname', 'longervaluename']]) == "longervaluenameis?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(longkeyname)is(longervaluename)",knowledge = [['longkeyname', 'longervaluename']]) == "longervaluenameis?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)has(a)(pet)(dog)",knowledge = [['name', 'john'], ['pet', 'dog'], ['dog', 'buddy']]) == "johnhas?dogbuddy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)has(a)(pet)(dog)",knowledge = [['name', 'john'], ['pet', 'dog'], ['dog', 'buddy']]) == "johnhas?dogbuddy": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4']]) == "value1andvalue2andvalue3andvalue4and?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4']]) == "value1andvalue2andvalue3andvalue4and?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(prefix)_(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "start_end"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(prefix)_(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "start_end": {e}')
    
    total += 1
    try:
        result = candidate(s = "(number)plus(number)equals(twice_number)",knowledge = [['number', '10'], ['twice_number', '20']]) == "10plus10equals20"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(number)plus(number)equals(twice_number)",knowledge = [['number', '10'], ['twice_number', '20']]) == "10plus10equals20": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)livesat(address)andworksat(company)",knowledge = [['name', 'Alice'], ['address', 'Wonderland'], ['company', 'TechCorp']]) == "AlicelivesatWonderlandandworksatTechCorp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)livesat(address)andworksat(company)",knowledge = [['name', 'Alice'], ['address', 'Wonderland'], ['company', 'TechCorp']]) == "AlicelivesatWonderlandandworksatTechCorp": {e}')
    
    total += 1
    try:
        result = candidate(s = "(repeated)(key)(repeated)(key)",knowledge = [['key', 'value']]) == "?value?value"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(repeated)(key)(repeated)(key)",knowledge = [['key', 'value']]) == "?value?value": {e}')
    
    total += 1
    try:
        result = candidate(s = "(planet)(orbits)around(star)",knowledge = [['planet', 'Earth'], ['star', 'Sun']]) == "Earth?aroundSun"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(planet)(orbits)around(star)",knowledge = [['planet', 'Earth'], ['star', 'Sun']]) == "Earth?aroundSun": {e}')
    
    total += 1
    try:
        result = candidate(s = "(item)isavaliablefrom(date)",knowledge = [['item', 'Smartphone'], ['date', '2023-12-15']]) == "Smartphoneisavaliablefrom2023-12-15"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(item)isavaliablefrom(date)",knowledge = [['item', 'Smartphone'], ['date', '2023-12-15']]) == "Smartphoneisavaliablefrom2023-12-15": {e}')
    
    total += 1
    try:
        result = candidate(s = "(conference)heldon(date)",knowledge = [['conference', 'GDC'], ['date', '2024-03-19']]) == "GDCheldon2024-03-19"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(conference)heldon(date)",knowledge = [['conference', 'GDC'], ['date', '2024-03-19']]) == "GDCheldon2024-03-19": {e}')
    
    total += 1
    try:
        result = candidate(s = "(first)(second)(third)(fourth)",knowledge = [['first', 'one'], ['second', 'two'], ['third', 'three']]) == "onetwothree?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(first)(second)(third)(fourth)",knowledge = [['first', 'one'], ['second', 'two'], ['third', 'three']]) == "onetwothree?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(color)(animal)",knowledge = [['color', 'blue'], ['animal', 'dog'], ['bird', 'sparrow']]) == "bluedog"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(color)(animal)",knowledge = [['color', 'blue'], ['animal', 'dog'], ['bird', 'sparrow']]) == "bluedog": {e}')
    
    total += 1
    try:
        result = candidate(s = "(firstName)(lastName)isfrom(city)in(country)",knowledge = [['firstName', 'Alice'], ['lastName', 'Wonderland'], ['city', 'Wonderland'], ['country', 'Fantasia']]) == "AliceWonderlandisfromWonderlandinFantasia"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(firstName)(lastName)isfrom(city)in(country)",knowledge = [['firstName', 'Alice'], ['lastName', 'Wonderland'], ['city', 'Wonderland'], ['country', 'Fantasia']]) == "AliceWonderlandisfromWonderlandinFantasia": {e}')
    
    total += 1
    try:
        result = candidate(s = "(product)costs(dollars)and(euros)",knowledge = [['product', 'Laptop'], ['dollars', '1200'], ['euros', '1020']]) == "Laptopcosts1200and1020"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(product)costs(dollars)and(euros)",knowledge = [['product', 'Laptop'], ['dollars', '1200'], ['euros', '1020']]) == "Laptopcosts1200and1020": {e}')
    
    total += 1
    try:
        result = candidate(s = "(nested)but(notreally)nested",knowledge = [['nested', 'deep'], ['notreally', 'shallow']]) == "deepbutshallownested"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(nested)but(notreally)nested",knowledge = [['nested', 'deep'], ['notreally', 'shallow']]) == "deepbutshallownested": {e}')
    
    total += 1
    try:
        result = candidate(s = "(first)(last)(age)",knowledge = [['first', 'john'], ['last', 'doe'], ['age', 'thirty']]) == "johndoethirty"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(first)(last)(age)",knowledge = [['first', 'john'], ['last', 'doe'], ['age', 'thirty']]) == "johndoethirty": {e}')
    
    total += 1
    try:
        result = candidate(s = "(city)(has)(many)(buildings)",knowledge = [['city', 'newyork'], ['many', 'lots']]) == "newyork?lots?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(city)(has)(many)(buildings)",knowledge = [['city', 'newyork'], ['many', 'lots']]) == "newyork?lots?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(language)(framework)",knowledge = [['language', 'Python'], ['framework', 'Django'], ['version', '3.9']]) == "PythonDjango"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(language)(framework)",knowledge = [['language', 'Python'], ['framework', 'Django'], ['version', '3.9']]) == "PythonDjango": {e}')
    
    total += 1
    try:
        result = candidate(s = "(model)releasedon(year)",knowledge = [['model', 'iPhone15'], ['year', '2023']]) == "iPhone15releasedon2023"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(model)releasedon(year)",knowledge = [['model', 'iPhone15'], ['year', '2023']]) == "iPhone15releasedon2023": {e}')
    
    total += 1
    try:
        result = candidate(s = "(multiple)(keys)(here)",knowledge = [['multiple', 'many'], ['keys', 'some'], ['here', 'there']]) == "manysomethere"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(multiple)(keys)(here)",knowledge = [['multiple', 'many'], ['keys', 'some'], ['here', 'there']]) == "manysomethere": {e}')
    
    total += 1
    try:
        result = candidate(s = "(username)lastloggedin(on)",knowledge = [['username', 'Alice'], ['on', '2023-10-01']]) == "Alicelastloggedin2023-10-01"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(username)lastloggedin(on)",knowledge = [['username', 'Alice'], ['on', '2023-10-01']]) == "Alicelastloggedin2023-10-01": {e}')
    
    total += 1
    try:
        result = candidate(s = "(planet)is(almost)full",knowledge = [['planet', 'Earth'], ['almost', 'not'], ['full', 'occupied']]) == "Earthisnotfull"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(planet)is(almost)full",knowledge = [['planet', 'Earth'], ['almost', 'not'], ['full', 'occupied']]) == "Earthisnotfull": {e}')
    
    total += 1
    try:
        result = candidate(s = "(person)loves(to)(eat)",knowledge = [['person', 'John'], ['eat', 'pizza']]) == "Johnloves?pizza"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(person)loves(to)(eat)",knowledge = [['person', 'John'], ['eat', 'pizza']]) == "Johnloves?pizza": {e}')
    
    total += 1
    try:
        result = candidate(s = "(car)is(fast)and(economical)",knowledge = [['car', 'Ferrari'], ['fast', 'very'], ['economical', 'not']]) == "Ferrariisveryandnot"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(car)is(fast)and(economical)",knowledge = [['car', 'Ferrari'], ['fast', 'very'], ['economical', 'not']]) == "Ferrariisveryandnot": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)and(key2)and(key3)and(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key4', 'value4']]) == "value1andvalue2and?andvalue4"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)and(key2)and(key3)and(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key4', 'value4']]) == "value1andvalue2and?andvalue4": {e}')
    
    total += 1
    try:
        result = candidate(s = "(part1)(part2)(part3)",knowledge = [['part1', 'first'], ['part2', 'second'], ['part3', 'third']]) == "firstsecondthird"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(part1)(part2)(part3)",knowledge = [['part1', 'first'], ['part2', 'second'], ['part3', 'third']]) == "firstsecondthird": {e}')
    
    total += 1
    try:
        result = candidate(s = "(color)(is)(used)in(art)",knowledge = [['color', 'red'], ['used', 'frequently']]) == "red?frequentlyin?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(color)(is)(used)in(art)",knowledge = [['color', 'red'], ['used', 'frequently']]) == "red?frequentlyin?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)is(key2)and(key3)is(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']]) == "value1isvalue2andvalue3is?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)is(key2)and(key3)is(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']]) == "value1isvalue2andvalue3is?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)from(country)is(visitor)",knowledge = [['name', 'Bob'], ['country', 'USA']]) == "BobfromUSAis?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)from(country)is(visitor)",knowledge = [['name', 'Bob'], ['country', 'USA']]) == "BobfromUSAis?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(prefix)example(suffix)",knowledge = [['prefix', 'pre'], ['suffix', 'post']]) == "preexamplepost"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(prefix)example(suffix)",knowledge = [['prefix', 'pre'], ['suffix', 'post']]) == "preexamplepost": {e}')
    
    total += 1
    try:
        result = candidate(s = "(unknown)(key)(not)(present)",knowledge = [['present', 'available']]) == "???available"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(unknown)(key)(not)(present)",knowledge = [['present', 'available']]) == "???available": {e}')
    
    total += 1
    try:
        result = candidate(s = "(unknown)(key1)(unknown)(key2)(unknown)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "?value1?value2?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(unknown)(key1)(unknown)(key2)(unknown)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "?value1?value2?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(book)writtenby(author)publishedby(publisher)",knowledge = [['book', 'GreatExpectations'], ['author', 'CharlesDickens'], ['publisher', 'ChapmanandHall']]) == "GreatExpectationswrittenbyCharlesDickenspublishedbyChapmanandHall"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(book)writtenby(author)publishedby(publisher)",knowledge = [['book', 'GreatExpectations'], ['author', 'CharlesDickens'], ['publisher', 'ChapmanandHall']]) == "GreatExpectationswrittenbyCharlesDickenspublishedbyChapmanandHall": {e}')
    
    total += 1
    try:
        result = candidate(s = "(instrument)plays(music)",knowledge = [['instrument', 'guitar'], ['music', 'beautiful']]) == "guitarplaysbeautiful"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(instrument)plays(music)",knowledge = [['instrument', 'guitar'], ['music', 'beautiful']]) == "guitarplaysbeautiful": {e}')
    
    total += 1
    try:
        result = candidate(s = "(prefix)(middle)(suffix)",knowledge = [['prefix', 'pre'], ['middle', 'mid'], ['suffix', 'suf']]) == "premidsuf"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(prefix)(middle)(suffix)",knowledge = [['prefix', 'pre'], ['middle', 'mid'], ['suffix', 'suf']]) == "premidsuf": {e}')
    
    total += 1
    try:
        result = candidate(s = "(fruit)are(sweet)and(healthy)",knowledge = [['fruit', 'apples'], ['sweet', 'very'], ['healthy', 'indeed']]) == "applesareveryandindeed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(fruit)are(sweet)and(healthy)",knowledge = [['fruit', 'apples'], ['sweet', 'very'], ['healthy', 'indeed']]) == "applesareveryandindeed": {e}')
    
    total += 1
    try:
        result = candidate(s = "(repeated)repeated(repeated)",knowledge = [['repeated', 'again']]) == "againrepeatedagain"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(repeated)repeated(repeated)",knowledge = [['repeated', 'again']]) == "againrepeatedagain": {e}')
    
    total += 1
    try:
        result = candidate(s = "(planet)(moon)orbiting(planet)",knowledge = [['planet', 'Earth'], ['moon', 'Moon']]) == "EarthMoonorbitingEarth"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(planet)(moon)orbiting(planet)",knowledge = [['planet', 'Earth'], ['moon', 'Moon']]) == "EarthMoonorbitingEarth": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)(key1)(key1)(key1)(key1)",knowledge = [['key1', 'repeat']]) == "repeatrepeatrepeatrepeatrepeat"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)(key1)(key1)(key1)(key1)",knowledge = [['key1', 'repeat']]) == "repeatrepeatrepeatrepeatrepeat": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)is(key2)yearsold(key3)",knowledge = [['key1', 'bob'], ['key2', 'two']]) == "bobistwoyearsold?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)is(key2)yearsold(key3)",knowledge = [['key1', 'bob'], ['key2', 'two']]) == "bobistwoyearsold?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(greeting)everyone(my)name(is)(unknown)",knowledge = [['greeting', 'hi'], ['my', 'my']]) == "hieveryonemyname??"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(greeting)everyone(my)name(is)(unknown)",knowledge = [['greeting', 'hi'], ['my', 'my']]) == "hieveryonemyname??": {e}')
    
    total += 1
    try:
        result = candidate(s = "(bird)can(fly)high",knowledge = [['bird', 'eagle'], ['fly', 'soar']]) == "eaglecansoarhigh"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(bird)can(fly)high",knowledge = [['bird', 'eagle'], ['fly', 'soar']]) == "eaglecansoarhigh": {e}')
    
    total += 1
    try:
        result = candidate(s = "(country)has(a)(capital)",knowledge = [['country', 'India'], ['capital', 'Delhi']]) == "Indiahas?Delhi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(country)has(a)(capital)",knowledge = [['country', 'India'], ['capital', 'Delhi']]) == "Indiahas?Delhi": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six']]) == "onetwothreefourfivesix"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six']]) == "onetwothreefourfivesix": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['g', 'G'], ['h', 'H'], ['i', 'I'], ['j', 'J'], ['k', 'K'], ['l', 'L'], ['m', 'M'], ['n', 'N'], ['o', 'O'], ['p', 'P'], ['q', 'Q'], ['r', 'R'], ['s', 'S'], ['t', 'T'], ['u', 'U'], ['v', 'V'], ['w', 'W'], ['x', 'X'], ['y', 'Y'], ['z', 'Z']]) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['g', 'G'], ['h', 'H'], ['i', 'I'], ['j', 'J'], ['k', 'K'], ['l', 'L'], ['m', 'M'], ['n', 'N'], ['o', 'O'], ['p', 'P'], ['q', 'Q'], ['r', 'R'], ['s', 'S'], ['t', 'T'], ['u', 'U'], ['v', 'V'], ['w', 'W'], ['x', 'X'], ['y', 'Y'], ['z', 'Z']]) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ": {e}')
    
    total += 1
    try:
        result = candidate(s = "(color)(of)the(sky)",knowledge = [['color', 'blue'], ['sky', 'beautiful']]) == "blue?thebeautiful"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(color)(of)the(sky)",knowledge = [['color', 'blue'], ['sky', 'beautiful']]) == "blue?thebeautiful": {e}')
    
    total += 1
    try:
        result = candidate(s = "(name)is(unknown)but(age)yearsold",knowledge = [['name', 'alice'], ['age', '30']]) == "aliceis?but30yearsold"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(name)is(unknown)but(age)yearsold",knowledge = [['name', 'alice'], ['age', '30']]) == "aliceis?but30yearsold": {e}')
    
    total += 1
    try:
        result = candidate(s = "(product)priceis(price)and(quantity)itemsareavailable",knowledge = [['product', 'laptop'], ['price', '1000'], ['quantity', '5']]) == "laptoppriceis1000and5itemsareavailable"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(product)priceis(price)and(quantity)itemsareavailable",knowledge = [['product', 'laptop'], ['price', '1000'], ['quantity', '5']]) == "laptoppriceis1000and5itemsareavailable": {e}')
    
    total += 1
    try:
        result = candidate(s = "(item)costs(amount)currency",knowledge = [['item', 'book'], ['amount', '10'], ['currency', 'dollars']]) == "bookcosts10currency"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(item)costs(amount)currency",knowledge = [['item', 'book'], ['amount', '10'], ['currency', 'dollars']]) == "bookcosts10currency": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'], ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'], ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'], ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'y'], ['z', 'z']]) == "abcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'], ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'], ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'], ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'y'], ['z', 'z']]) == "abcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "(repeated)(repeated)(repeated)",knowledge = [['repeated', 'rep']]) == "repreprep"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(repeated)(repeated)(repeated)",knowledge = [['repeated', 'rep']]) == "repreprep": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)and(key6)and(key7)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4'], ['key5', 'value5'], ['key6', 'value6'], ['key7', 'value7']]) == "value1andvalue2andvalue3andvalue4andvalue5andvalue6andvalue7"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)and(key6)and(key7)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4'], ['key5', 'value5'], ['key6', 'value6'], ['key7', 'value7']]) == "value1andvalue2andvalue3andvalue4andvalue5andvalue6andvalue7": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six'], ['g', 'seven'], ['h', 'eight'], ['i', 'nine'], ['j', 'ten']]) == "onetwothreefourfivesixseveneightnineten"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six'], ['g', 'seven'], ['h', 'eight'], ['i', 'nine'], ['j', 'ten']]) == "onetwothreefourfivesixseveneightnineten": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'yes'], ['b', 'no'], ['c', 'maybe'], ['d', 'sure'], ['e', 'never'], ['f', 'always'], ['g', 'often'], ['h', 'rarely'], ['i', 'sometimes'], ['j', 'usually']]) == "yesnomaybesureneveralwaysoftenrarelysometimesusually"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'yes'], ['b', 'no'], ['c', 'maybe'], ['d', 'sure'], ['e', 'never'], ['f', 'always'], ['g', 'often'], ['h', 'rarely'], ['i', 'sometimes'], ['j', 'usually']]) == "yesnomaybesureneveralwaysoftenrarelysometimesusually": {e}')
    
    total += 1
    try:
        result = candidate(s = "(user)hasposted(numberofposts)times",knowledge = [['user', 'Charlie'], ['numberofposts', '250']]) == "Charliehasposted250times"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(user)hasposted(numberofposts)times",knowledge = [['user', 'Charlie'], ['numberofposts', '250']]) == "Charliehasposted250times": {e}')
    
    total += 1
    try:
        result = candidate(s = "(complex)(string)(with)(multiple)(keys)",knowledge = [['complex', 'com'], ['string', 'str'], ['with', 'wi'], ['multiple', 'mul'], ['keys', 'ke']]) == "comstrwimulke"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(complex)(string)(with)(multiple)(keys)",knowledge = [['complex', 'com'], ['string', 'str'], ['with', 'wi'], ['multiple', 'mul'], ['keys', 'ke']]) == "comstrwimulke": {e}')
    
    total += 1
    try:
        result = candidate(s = "(key1)is(key2)yearsold(key3)and(key4)livesin(key5)",knowledge = [['key1', 'bob'], ['key2', 'two'], ['key5', 'NYC']]) == "bobistwoyearsold?and?livesinNYC"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(key1)is(key2)yearsold(key3)and(key4)livesin(key5)",knowledge = [['key1', 'bob'], ['key2', 'two'], ['key5', 'NYC']]) == "bobistwoyearsold?and?livesinNYC": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon?": {e}')
    
    total += 1
    try:
        result = candidate(s = "(nested)brackets(are)not(allowed)",knowledge = [['nested', 'nested'], ['brackets', 'brackets'], ['not', 'not']]) == "nestedbrackets?not?"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(nested)brackets(are)not(allowed)",knowledge = [['nested', 'nested'], ['brackets', 'brackets'], ['not', 'not']]) == "nestedbrackets?not?": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa"
    assert candidate(s = "(a)(b)(c)(d)",knowledge = [['a', '1'], ['b', '2'], ['c', '3']]) == "123?"
    assert candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?"
    assert candidate(s = "(a)(a)(a)aaa",knowledge = [['a', 'yes']]) == "yesyesyesaaa"
    assert candidate(s = "",knowledge = []) == ""
    assert candidate(s = "noknowledgehere",knowledge = []) == "noknowledgehere"
    assert candidate(s = "no(brackets)here",knowledge = []) == "no?here"
    assert candidate(s = "hi(name)",knowledge = [['a', 'b']]) == "hi?"
    assert candidate(s = "(nested)but(not)really",knowledge = [['nested', 'nested'], ['not', 'not']]) == "nestedbutnotreally"
    assert candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2?"
    assert candidate(s = "this(is)a(test)",knowledge = [['is', 'was'], ['test', 'trial']]) == "thiswasatrial"
    assert candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold"
    assert candidate(s = "(key1)(key2)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2"
    assert candidate(s = "(single)",knowledge = [['single', 'one']]) == "one"
    assert candidate(s = "(last)one",knowledge = [['last', 'final']]) == "finalone"
    assert candidate(s = "single",knowledge = [['single', 'word']]) == "single"
    assert candidate(s = "hello",knowledge = []) == "hello"
    assert candidate(s = "(unknown)key",knowledge = [['known', 'value']]) == "?key"
    assert candidate(s = "(name)is(age)yearsold",knowledge = [['name', 'bob'], ['age', 'two']]) == "bobistwoyearsold"
    assert candidate(s = "(key1)(key2)(key3)",knowledge = [['key1', 'val1'], ['key2', 'val2'], ['key3', 'val3']]) == "val1val2val3"
    assert candidate(s = "(book)written(by)(author)",knowledge = [['book', '1984'], ['author', 'George']]) == "1984written?George"
    assert candidate(s = "(city)(in)(country)",knowledge = [['city', 'Tokyo'], ['country', 'Japan']]) == "Tokyo?Japan"
    assert candidate(s = "(nested)(key)(nested)",knowledge = [['key', 'value'], ['nested', 'deep']]) == "deepvaluedeep"
    assert candidate(s = "(ingredient)requiresto(cooktime)mins",knowledge = [['ingredient', 'Cookies'], ['cooktime', '15']]) == "Cookiesrequiresto15mins"
    assert candidate(s = "(one)(two)(three)(four)(five)",knowledge = [['one', '1'], ['two', '2'], ['three', '3'], ['four', '4']]) == "1234?"
    assert candidate(s = "(customer)(order)at(store)",knowledge = [['customer', 'Alice'], ['order', 'Order123']]) == "AliceOrder123at?"
    assert candidate(s = "(keyA)and(keyB)and(keyC)and(keyD)",knowledge = [['keyA', 'valA'], ['keyB', 'valB']]) == "valAandvalBand?and?"
    assert candidate(s = "(key)with(missing)knowledge",knowledge = [['key', 'value1'], ['missing', 'value2'], ['knowledge', 'value3']]) == "value1withvalue2knowledge"
    assert candidate(s = "(greeting)(world)(planet)",knowledge = [['greeting', 'hello'], ['world', 'earth'], ['planet', 'mars']]) == "helloearthmars"
    assert candidate(s = "(this)(is)(a)(test)(string)(with)(multiple)(keys)",knowledge = [['this', 'it'], ['is', 'be'], ['a', 'an'], ['test', 'example'], ['string', 'sequence'], ['with', 'having'], ['multiple', 'several'], ['keys', 'identifiers']]) == "itbeanexamplesequencehavingseveralidentifiers"
    assert candidate(s = "(language)programmingis(fun)",knowledge = [['language', 'python'], ['fun', 'awesome']]) == "pythonprogrammingisawesome"
    assert candidate(s = "(fruit)(vegetable)",knowledge = [['fruit', 'apple'], ['vegetable', 'carrot']]) == "applecarrot"
    assert candidate(s = "(animal)lives(in)(habitat)",knowledge = [['animal', 'tiger'], ['habitat', 'jungle']]) == "tigerlives?jungle"
    assert candidate(s = "(name)has(age)yearsand(occupation)",knowledge = [['name', 'Alice'], ['age', '30']]) == "Alicehas30yearsand?"
    assert candidate(s = "(longkey)(anotherkey)(yetanotherkey)",knowledge = [['longkey', 'averylongvalue'], ['anotherkey', 'shortval'], ['yetanotherkey', 'value']]) == "averylongvalueshortvalvalue"
    assert candidate(s = "(language)is(cool)",knowledge = [['language', 'Python'], ['cool', 'awesome']]) == "Pythonisawesome"
    assert candidate(s = "(first)and(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnanddoename"
    assert candidate(s = "(name)is(living)(in)(city)",knowledge = [['name', 'bob'], ['in', 'at'], ['city', 'london']]) == "bobis?atlondon"
    assert candidate(s = "(animal)(eats)(food)",knowledge = [['animal', 'lion'], ['food', 'meat']]) == "lion?meat"
    assert candidate(s = "(user)likes(to)(eat)(food)",knowledge = [['user', 'alice'], ['eat', 'enjoy'], ['food', 'pizza']]) == "alicelikes?enjoypizza"
    assert candidate(s = "(prefix)middle(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "startmiddleend"
    assert candidate(s = "(flower)grows(in)(soil)",knowledge = [['flower', 'rose'], ['soil', 'dirt']]) == "rosegrows?dirt"
    assert candidate(s = "(first)nameis(last)name",knowledge = [['first', 'john'], ['last', 'doe']]) == "johnnameisdoename"
    assert candidate(s = "(longkey1)and(longkey2)and(longkey3)and(longkey4)",knowledge = [['longkey1', 'value1'], ['longkey2', 'value2'], ['longkey3', 'value3'], ['longkey4', 'value4']]) == "value1andvalue2andvalue3andvalue4"
    assert candidate(s = "(department)islocatedat(address)",knowledge = [['department', 'Sales'], ['address', '123BusinessSt']]) == "Salesislocatedat123BusinessSt"
    assert candidate(s = "(name)has(a)(pet)",knowledge = [['name', 'Mary'], ['pet', 'dog']]) == "Maryhas?dog"
    assert candidate(s = "(drink)is(served)in(glass)",knowledge = [['drink', 'water'], ['glass', 'big']]) == "wateris?inbig"
    assert candidate(s = "prefix(key1)middle(key2)suffix",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "prefixvalue1middlevalue2suffix"
    assert candidate(s = "(key1)(key2)(key1)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "value1value2value1"
    assert candidate(s = "(item1)(item2)(item3)(item4)",knowledge = [['item1', 'itemA'], ['item2', 'itemB'], ['item4', 'itemD']]) == "itemAitemB?itemD"
    assert candidate(s = "(greeting)world",knowledge = [['greeting', 'hello'], ['farewell', 'bye']]) == "helloworld"
    assert candidate(s = "(user)(name)livesin(city)with(zip)",knowledge = [['user', 'John'], ['city', 'San Francisco'], ['zip', '94111']]) == "John?livesinSan Franciscowith94111"
    assert candidate(s = "(person)(from)(place)isvisiting(placeofinterest)",knowledge = [['person', 'Bob'], ['from', 'LosAngeles'], ['place', 'SanFrancisco'], ['placeofinterest', 'Alcatraz']]) == "BobLosAngelesSanFranciscoisvisitingAlcatraz"
    assert candidate(s = "(longkeyname)is(longervaluename)",knowledge = [['longkeyname', 'longervaluename']]) == "longervaluenameis?"
    assert candidate(s = "(name)has(a)(pet)(dog)",knowledge = [['name', 'john'], ['pet', 'dog'], ['dog', 'buddy']]) == "johnhas?dogbuddy"
    assert candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4']]) == "value1andvalue2andvalue3andvalue4and?"
    assert candidate(s = "(prefix)_(suffix)",knowledge = [['prefix', 'start'], ['suffix', 'end']]) == "start_end"
    assert candidate(s = "(number)plus(number)equals(twice_number)",knowledge = [['number', '10'], ['twice_number', '20']]) == "10plus10equals20"
    assert candidate(s = "(name)livesat(address)andworksat(company)",knowledge = [['name', 'Alice'], ['address', 'Wonderland'], ['company', 'TechCorp']]) == "AlicelivesatWonderlandandworksatTechCorp"
    assert candidate(s = "(repeated)(key)(repeated)(key)",knowledge = [['key', 'value']]) == "?value?value"
    assert candidate(s = "(planet)(orbits)around(star)",knowledge = [['planet', 'Earth'], ['star', 'Sun']]) == "Earth?aroundSun"
    assert candidate(s = "(item)isavaliablefrom(date)",knowledge = [['item', 'Smartphone'], ['date', '2023-12-15']]) == "Smartphoneisavaliablefrom2023-12-15"
    assert candidate(s = "(conference)heldon(date)",knowledge = [['conference', 'GDC'], ['date', '2024-03-19']]) == "GDCheldon2024-03-19"
    assert candidate(s = "(first)(second)(third)(fourth)",knowledge = [['first', 'one'], ['second', 'two'], ['third', 'three']]) == "onetwothree?"
    assert candidate(s = "(color)(animal)",knowledge = [['color', 'blue'], ['animal', 'dog'], ['bird', 'sparrow']]) == "bluedog"
    assert candidate(s = "(firstName)(lastName)isfrom(city)in(country)",knowledge = [['firstName', 'Alice'], ['lastName', 'Wonderland'], ['city', 'Wonderland'], ['country', 'Fantasia']]) == "AliceWonderlandisfromWonderlandinFantasia"
    assert candidate(s = "(product)costs(dollars)and(euros)",knowledge = [['product', 'Laptop'], ['dollars', '1200'], ['euros', '1020']]) == "Laptopcosts1200and1020"
    assert candidate(s = "(nested)but(notreally)nested",knowledge = [['nested', 'deep'], ['notreally', 'shallow']]) == "deepbutshallownested"
    assert candidate(s = "(first)(last)(age)",knowledge = [['first', 'john'], ['last', 'doe'], ['age', 'thirty']]) == "johndoethirty"
    assert candidate(s = "(city)(has)(many)(buildings)",knowledge = [['city', 'newyork'], ['many', 'lots']]) == "newyork?lots?"
    assert candidate(s = "(language)(framework)",knowledge = [['language', 'Python'], ['framework', 'Django'], ['version', '3.9']]) == "PythonDjango"
    assert candidate(s = "(model)releasedon(year)",knowledge = [['model', 'iPhone15'], ['year', '2023']]) == "iPhone15releasedon2023"
    assert candidate(s = "(multiple)(keys)(here)",knowledge = [['multiple', 'many'], ['keys', 'some'], ['here', 'there']]) == "manysomethere"
    assert candidate(s = "(username)lastloggedin(on)",knowledge = [['username', 'Alice'], ['on', '2023-10-01']]) == "Alicelastloggedin2023-10-01"
    assert candidate(s = "(planet)is(almost)full",knowledge = [['planet', 'Earth'], ['almost', 'not'], ['full', 'occupied']]) == "Earthisnotfull"
    assert candidate(s = "(person)loves(to)(eat)",knowledge = [['person', 'John'], ['eat', 'pizza']]) == "Johnloves?pizza"
    assert candidate(s = "(car)is(fast)and(economical)",knowledge = [['car', 'Ferrari'], ['fast', 'very'], ['economical', 'not']]) == "Ferrariisveryandnot"
    assert candidate(s = "(key1)and(key2)and(key3)and(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key4', 'value4']]) == "value1andvalue2and?andvalue4"
    assert candidate(s = "(part1)(part2)(part3)",knowledge = [['part1', 'first'], ['part2', 'second'], ['part3', 'third']]) == "firstsecondthird"
    assert candidate(s = "(color)(is)(used)in(art)",knowledge = [['color', 'red'], ['used', 'frequently']]) == "red?frequentlyin?"
    assert candidate(s = "(key1)is(key2)and(key3)is(key4)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']]) == "value1isvalue2andvalue3is?"
    assert candidate(s = "(name)from(country)is(visitor)",knowledge = [['name', 'Bob'], ['country', 'USA']]) == "BobfromUSAis?"
    assert candidate(s = "(prefix)example(suffix)",knowledge = [['prefix', 'pre'], ['suffix', 'post']]) == "preexamplepost"
    assert candidate(s = "(unknown)(key)(not)(present)",knowledge = [['present', 'available']]) == "???available"
    assert candidate(s = "(unknown)(key1)(unknown)(key2)(unknown)",knowledge = [['key1', 'value1'], ['key2', 'value2']]) == "?value1?value2?"
    assert candidate(s = "(book)writtenby(author)publishedby(publisher)",knowledge = [['book', 'GreatExpectations'], ['author', 'CharlesDickens'], ['publisher', 'ChapmanandHall']]) == "GreatExpectationswrittenbyCharlesDickenspublishedbyChapmanandHall"
    assert candidate(s = "(instrument)plays(music)",knowledge = [['instrument', 'guitar'], ['music', 'beautiful']]) == "guitarplaysbeautiful"
    assert candidate(s = "(prefix)(middle)(suffix)",knowledge = [['prefix', 'pre'], ['middle', 'mid'], ['suffix', 'suf']]) == "premidsuf"
    assert candidate(s = "(fruit)are(sweet)and(healthy)",knowledge = [['fruit', 'apples'], ['sweet', 'very'], ['healthy', 'indeed']]) == "applesareveryandindeed"
    assert candidate(s = "(repeated)repeated(repeated)",knowledge = [['repeated', 'again']]) == "againrepeatedagain"
    assert candidate(s = "(planet)(moon)orbiting(planet)",knowledge = [['planet', 'Earth'], ['moon', 'Moon']]) == "EarthMoonorbitingEarth"
    assert candidate(s = "(key1)(key1)(key1)(key1)(key1)",knowledge = [['key1', 'repeat']]) == "repeatrepeatrepeatrepeatrepeat"
    assert candidate(s = "(key1)is(key2)yearsold(key3)",knowledge = [['key1', 'bob'], ['key2', 'two']]) == "bobistwoyearsold?"
    assert candidate(s = "(greeting)everyone(my)name(is)(unknown)",knowledge = [['greeting', 'hi'], ['my', 'my']]) == "hieveryonemyname??"
    assert candidate(s = "(bird)can(fly)high",knowledge = [['bird', 'eagle'], ['fly', 'soar']]) == "eaglecansoarhigh"
    assert candidate(s = "(country)has(a)(capital)",knowledge = [['country', 'India'], ['capital', 'Delhi']]) == "Indiahas?Delhi"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six']]) == "onetwothreefourfivesix"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['g', 'G'], ['h', 'H'], ['i', 'I'], ['j', 'J'], ['k', 'K'], ['l', 'L'], ['m', 'M'], ['n', 'N'], ['o', 'O'], ['p', 'P'], ['q', 'Q'], ['r', 'R'], ['s', 'S'], ['t', 'T'], ['u', 'U'], ['v', 'V'], ['w', 'W'], ['x', 'X'], ['y', 'Y'], ['z', 'Z']]) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert candidate(s = "(color)(of)the(sky)",knowledge = [['color', 'blue'], ['sky', 'beautiful']]) == "blue?thebeautiful"
    assert candidate(s = "(name)is(unknown)but(age)yearsold",knowledge = [['name', 'alice'], ['age', '30']]) == "aliceis?but30yearsold"
    assert candidate(s = "(product)priceis(price)and(quantity)itemsareavailable",knowledge = [['product', 'laptop'], ['price', '1000'], ['quantity', '5']]) == "laptoppriceis1000and5itemsareavailable"
    assert candidate(s = "(item)costs(amount)currency",knowledge = [['item', 'book'], ['amount', '10'], ['currency', 'dollars']]) == "bookcosts10currency"
    assert candidate(s = "(a)(b)(c)(d)(e)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)",knowledge = [['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd'], ['e', 'e'], ['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'], ['j', 'j'], ['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'], ['o', 'o'], ['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'], ['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'y'], ['z', 'z']]) == "abcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "(repeated)(repeated)(repeated)",knowledge = [['repeated', 'rep']]) == "repreprep"
    assert candidate(s = "(key1)and(key2)and(key3)and(key4)and(key5)and(key6)and(key7)",knowledge = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3'], ['key4', 'value4'], ['key5', 'value5'], ['key6', 'value6'], ['key7', 'value7']]) == "value1andvalue2andvalue3andvalue4andvalue5andvalue6andvalue7"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'one'], ['b', 'two'], ['c', 'three'], ['d', 'four'], ['e', 'five'], ['f', 'six'], ['g', 'seven'], ['h', 'eight'], ['i', 'nine'], ['j', 'ten']]) == "onetwothreefourfivesixseveneightnineten"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)",knowledge = [['a', 'yes'], ['b', 'no'], ['c', 'maybe'], ['d', 'sure'], ['e', 'never'], ['f', 'always'], ['g', 'often'], ['h', 'rarely'], ['i', 'sometimes'], ['j', 'usually']]) == "yesnomaybesureneveralwaysoftenrarelysometimesusually"
    assert candidate(s = "(user)hasposted(numberofposts)times",knowledge = [['user', 'Charlie'], ['numberofposts', '250']]) == "Charliehasposted250times"
    assert candidate(s = "(complex)(string)(with)(multiple)(keys)",knowledge = [['complex', 'com'], ['string', 'str'], ['with', 'wi'], ['multiple', 'mul'], ['keys', 'ke']]) == "comstrwimulke"
    assert candidate(s = "(key1)is(key2)yearsold(key3)and(key4)livesin(key5)",knowledge = [['key1', 'bob'], ['key2', 'two'], ['key5', 'NYC']]) == "bobistwoyearsold?and?livesinNYC"
    assert candidate(s = "(a)(b)(c)(d)(e)(f)",knowledge = [['a', 'alpha'], ['b', 'beta'], ['c', 'gamma'], ['d', 'delta'], ['e', 'epsilon']]) == "alphabetagammadeltaepsilon?"
    assert candidate(s = "(nested)brackets(are)not(allowed)",knowledge = [['nested', 'nested'], ['brackets', 'brackets'], ['not', 'not']]) == "nestedbrackets?not?"


