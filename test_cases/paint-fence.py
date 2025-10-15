def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 15,k = 2) == 1974
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 2) == 1974: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 100000) == 9999999952000470103497974877463882973999752808161992015107745866422079306034625361145344447150025657641979544935635622518492524146014318959903717694542512167388769172663190491369774185925201548324161216740390990987623051800760407999592000170000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 100000) == 9999999952000470103497974877463882973999752808161992015107745866422079306034625361145344447150025657641979544935635622518492524146014318959903717694542512167388769172663190491369774185925201548324161216740390990987623051800760407999592000170000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 50) == 9469551703547193879850071929642500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 50) == 9469551703547193879850071929642500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 3) == 27408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 3) == 27408: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 10) == 64221618338674163619212551744715546727431459993700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 10) == 64221618338674163619212551744715546727431459993700: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 2) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 2) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 5) == 7348480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 5) == 7348480: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 10) == 97200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 10) == 97200: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 3) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 3) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 3) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 3) == 180: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 2) == 2692538
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 2) == 2692538: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5) == 16535782640425905735969222216908800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5) == 16535782640425905735969222216908800: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 10) == 84658667828908637700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 10) == 84658667828908637700: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 7) == 11501644896
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 7) == 11501644896: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3) == 4171776
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3) == 4171776: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 100000) == 99999999620003700629987749461117424190626611159774584147814002883721021868328199710909447292743660530491316462484508727846003471647637261403138201907875935811364921337322967499931100233999740000100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 100000) == 99999999620003700629987749461117424190626611159774584147814002883721021868328199710909447292743660530491316462484508727846003471647637261403138201907875935811364921337322967499931100233999740000100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 100) == 995750031911895429654448891601160344725076745761603290482390368082541128296281802429139900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 100) == 995750031911895429654448891601160344725076745761603290482390368082541128296281802429139900: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 2) == 40730022148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 2) == 40730022148: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 20) == 317568357189921946564531760025620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 20) == 317568357189921946564531760025620: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 20000) == 1073741748841698379484335880961020298720119191598534316480300885720078955495136225827805275893867614219082156707840152003599980000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 20000) == 1073741748841698379484335880961020298720119191598534316480300885720078955495136225827805275893867614219082156707840152003599980000: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 50000) == 28421708941560158655047401483051173293663261645904195679757424600797938823080588496854922795500225352930571890211938886724168770621231884683744546223156454423077124274179838552599581411624675775003625034999950000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 50000) == 28421708941560158655047401483051173293663261645904195679757424600797938823080588496854922795500225352930571890211938886724168770621231884683744546223156454423077124274179838552599581411624675775003625034999950000: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,k = 8) == 407992243047774765711266327672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,k = 8) == 407992243047774765711266327672: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 100000) == 99999999920000700014999750000600008999940000100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 100000) == 99999999920000700014999750000600008999940000100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 3) == 3672
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 3) == 3672: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 7) == 57269354438886912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 7) == 57269354438886912: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 5000) == 2910379204714972618368103558802135112437571033011875813247971671242931702436917711819398146923234934660857300160199975250300000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 5000) == 2910379204714972618368103558802135112437571033011875813247971671242931702436917711819398146923234934660857300160199975250300000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 99999) == 99951011288383259931564045605348096606512977878127426226546681184347240561505568829821619776420383510088073244412418800059411779061435493063874833271465070416037017811839663649158711625129854213855129138754961677805986553714966024705330364022784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 99999) == 99951011288383259931564045605348096606512977878127426226546681184347240561505568829821619776420383510088073244412418800059411779061435493063874833271465070416037017811839663649158711625129854213855129138754961677805986553714966024705330364022784: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 2) == 331160282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 2) == 331160282: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 7) == 3734184996864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 7) == 3734184996864: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 8) == 15388352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 8) == 15388352: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 100) == 99772405924850985256505622172378380436989683840100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 100) == 99772405924850985256505622172378380436989683840100: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 100000) == 999999998700012000549989999961002239983899936001489992400009000039999900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 100000) == 999999998700012000549989999961002239983899936001489992400009000039999900000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 4) == 864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 4) == 864: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 2) == 25172538050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 2) == 25172538050: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 7) == 13470235960809990817824768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 7) == 13470235960809990817824768: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 100) == 9967365568875105385884863244180601333550953690962746605728641802120000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 100) == 9967365568875105385884863244180601333550953690962746605728641802120000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,k = 100000) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 100000) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 2) == 242786
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 2) == 242786: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 50000) == 2980232211351919274326324314318672163302392871005965301639287160344502172185624995132866312281249350010499960000050000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 50000) == 2980232211351919274326324314318672163302392871005965301639287160344502172185624995132866312281249350010499960000050000: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 100000) == 99999999770002200209995999922102753997789185609597061737751014520104387770212159019999377003443992999989600083999840000100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 100000) == 99999999770002200209995999922102753997789185609597061737751014520104387770212159019999377003443992999989600083999840000100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 5) == 50612096204800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 5) == 50612096204800: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 9) == 784949351486331027456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 9) == 784949351486331027456: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 5) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 5) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 3) == 14711350935552
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 3) == 14711350935552: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 7) == 206586368447979697428149305344
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 7) == 206586368447979697428149305344: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 10) == 911315617290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 10) == 911315617290: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 10000) == 999999900009002799510001004999610007000299990000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 10000) == 999999900009002799510001004999610007000299990000: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 50) == 89602741156971186576848194582434056147913306182627726061058222935050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 50) == 89602741156971186576848194582434056147913306182627726061058222935050: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 3) == 2239218190909440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 3) == 2239218190909440: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 15) == 414567428748533760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 15) == 414567428748533760: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 2) == 21892
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 2) == 21892: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 3) == 2890275329929503571968
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 3) == 2890275329929503571968: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 50) == 174388418958707976132495599422315195551321101858063926373636941158868843553644920050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 50) == 174388418958707976132495599422315195551321101858063926373636941158868843553644920050: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 1000) == 999977022209599223753770865603151524530416714160993773443299896083984001000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 1000) == 999977022209599223753770865603151524530416714160993773443299896083984001000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 100000) == 9999999997000020000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 100000) == 9999999997000020000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5) == 348586958385808670720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5) == 348586958385808670720: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 3) == 634987008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 3) == 634987008: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 50000) == 90949468794887807307175503876924559151107081938691540856308664691503678460623124701186645661116529337768436183311345396195389785509588878816359255122460323239420859370693779249935000050000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 50000) == 90949468794887807307175503876924559151107081938691540856308664691503678460623124701186645661116529337768436183311345396195389785509588878816359255122460323239420859370693779249935000050000: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 5) == 132825888566804480
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 5) == 132825888566804480: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 30) == 4828302424321938917457579794849294424245181605164800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 30) == 4828302424321938917457579794849294424245181605164800: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 10000) == 9999997700220209959992212753977818569597617175114521043677032159199937703443929998960083998400010000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 10000) == 9999997700220209959992212753977818569597617175114521043677032159199937703443929998960083998400010000: {e}')
    
    total += 1
    try:
        result = candidate(n = 42,k = 2) == 866988874
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 42,k = 2) == 866988874: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 10) == 793731690733155352946777790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 10) == 793731690733155352946777790: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 1000) == 999957042818391667753785447550126192569330183844675051647047945638540344685568740578938651376947284860330629011252227197124029013999000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 1000) == 999957042818391667753785447550126192569330183844675051647047945638540344685568740578938651376947284860330629011252227197124029013999000: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 1000) == 999962037628769628442930171326501255813935595941273094779207838953024124084375279771057154213987250319749311233974001000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 1000) == 999962037628769628442930171326501255813935595941273094779207838953024124084375279771057154213987250319749311233974001000: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 15) == 70100013203862820252158826988883466045468054923509760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 15) == 70100013203862820252158826988883466045468054923509760: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 3) == 7896379049230303494144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 3) == 7896379049230303494144: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4) == 228
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4) == 228: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 100) == 998712539963223837482409039900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 100) == 998712539963223837482409039900: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 100000) == 99999999530004600989980638860536162659651628002247294995378143204787900203641454148891887100911812723235818458208757409403333574885730875773816094836838999139515428510124916987761235051042263801137257159944507702311937999857600359999680000100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 100000) == 99999999530004600989980638860536162659651628002247294995378143204787900203641454148891887100911812723235818458208757409403333574885730875773816094836838999139515428510124916987761235051042263801137257159944507702311937999857600359999680000100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 50000) == 291038300725705943302344470866242105832051767032898458360152646584626067576566806732257337227638186312510439361671894618603180659108591686265945749975250030000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 50000) == 291038300725705943302344470866242105832051767032898458360152646584626067576566806732257337227638186312510439361671894618603180659108591686265945749975250030000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 10) == 9282568410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 10) == 9282568410: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 100) == 9952571356412657726381564909919525409044075662747289070319607611923677876616169583970453167592170000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 100) == 9952571356412657726381564909919525409044075662747289070319607611923677876616169583970453167592170000: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 20) == 1004151076547626230786266566362256795580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 20) == 1004151076547626230786266566362256795580: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 20) == 10039746098689777957200971626557993327809319603621620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 20) == 10039746098689777957200971626557993327809319603621620: {e}')
    
    total += 1
    try:
        result = candidate(n = 47,k = 5000) == 710541457034313051290484603248594260678488454539345543230944707727101837527620429606035600637725264416314535686762408801653878584805972101916304818657952689599955000400000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 47,k = 5000) == 710541457034313051290484603248594260678488454539345543230944707727101837527620429606035600637725264416314535686762408801653878584805972101916304818657952689599955000400000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 100) == 999603009900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 100) == 999603009900: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 2) == 29860704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 2) == 29860704: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 50000) == 1953124994531343753124900000625004999950000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 50000) == 1953124994531343753124900000625004999950000: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 10) == 886481740149390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 10) == 886481740149390: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 5) == 914828192514254359756800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 5) == 914828192514254359756800: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 100000) == 999999997200027003249937498276058190174873841243964837285013265897406177303093752257083928348489350012178296040407392173031739942400019000089999900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 100000) == 999999997200027003249937498276058190174873841243964837285013265897406177303093752257083928348489350012178296040407392173031739942400019000089999900000: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 30) == 8265309825758255006277731320484013630
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 30) == 8265309825758255006277731320484013630: {e}')
    
    total += 1
    try:
        result = candidate(n = 48,k = 500) == 3552061312021803694641285550786487050792994883214147498910757830914643435165384888634893642773774043131571043068997827191378749500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 48,k = 500) == 3552061312021803694641285550786487050792994883214147498910757830914643435165384888634893642773774043131571043068997827191378749500: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 50) == 287291863842135288088949795966532967764016355355305412780000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 50) == 287291863842135288088949795966532967764016355355305412780000: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 12) == 8353663189476
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 12) == 8353663189476: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 50) == 2953434806047058459526357024483280610460050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 50) == 2953434806047058459526357024483280610460050: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 10) == 6481580482890944147517769612900651151794438116810
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 10) == 6481580482890944147517769612900651151794438116810: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 20) == 31745674986236020522693749791045360604849067349519696877580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 20) == 31745674986236020522693749791045360604849067349519696877580: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 100) == 997230185834338989682696063818771585742574439604682419089900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 100) == 997230185834338989682696063818771585742574439604682419089900: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 15,k = 2) == 1974
    assert candidate(n = 50,k = 100000) == 9999999952000470103497974877463882973999752808161992015107745866422079306034625361145344447150025657641979544935635622518492524146014318959903717694542512167388769172663190491369774185925201548324161216740390990987623051800760407999592000170000000000
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 3,k = 2) == 6
    assert candidate(n = 5,k = 1) == 0
    assert candidate(n = 20,k = 50) == 9469551703547193879850071929642500
    assert candidate(n = 10,k = 3) == 27408
    assert candidate(n = 50,k = 10) == 64221618338674163619212551744715546727431459993700
    assert candidate(n = 7,k = 2) == 42
    assert candidate(n = 4,k = 1) == 0
    assert candidate(n = 10,k = 5) == 7348480
    assert candidate(n = 5,k = 10) == 97200
    assert candidate(n = 2,k = 1) == 1
    assert candidate(n = 2,k = 3) == 9
    assert candidate(n = 4,k = 3) == 66
    assert candidate(n = 5,k = 3) == 180
    assert candidate(n = 30,k = 2) == 2692538
    assert candidate(n = 50,k = 5) == 16535782640425905735969222216908800
    assert candidate(n = 20,k = 10) == 84658667828908637700
    assert candidate(n = 12,k = 7) == 11501644896
    assert candidate(n = 15,k = 3) == 4171776
    assert candidate(n = 40,k = 100000) == 99999999620003700629987749461117424190626611159774584147814002883721021868328199710909447292743660530491316462484508727846003471647637261403138201907875935811364921337322967499931100233999740000100000
    assert candidate(n = 10,k = 1) == 0
    assert candidate(n = 45,k = 100) == 995750031911895429654448891601160344725076745761603290482390368082541128296281802429139900
    assert candidate(n = 50,k = 2) == 40730022148
    assert candidate(n = 2,k = 5) == 25
    assert candidate(n = 25,k = 20) == 317568357189921946564531760025620
    assert candidate(n = 30,k = 20000) == 1073741748841698379484335880961020298720119191598534316480300885720078955495136225827805275893867614219082156707840152003599980000
    assert candidate(n = 45,k = 50000) == 28421708941560158655047401483051173293663261645904195679757424600797938823080588496854922795500225352930571890211938886724168770621231884683744546223156454423077124274179838552599581411624675775003625034999950000
    assert candidate(n = 33,k = 8) == 407992243047774765711266327672
    assert candidate(n = 10,k = 100000) == 99999999920000700014999750000600008999940000100000
    assert candidate(n = 8,k = 3) == 3672
    assert candidate(n = 20,k = 7) == 57269354438886912
    assert candidate(n = 4,k = 2) == 10
    assert candidate(n = 35,k = 5000) == 2910379204714972618368103558802135112437571033011875813247971671242931702436917711819398146923234934660857300160199975250300000000
    assert candidate(n = 49,k = 99999) == 99951011288383259931564045605348096606512977878127426226546681184347240561505568829821619776420383510088073244412418800059411779061435493063874833271465070416037017811839663649158711625129854213855129138754961677805986553714966024705330364022784
    assert candidate(n = 40,k = 2) == 331160282
    assert candidate(n = 1,k = 5) == 5
    assert candidate(n = 15,k = 7) == 3734184996864
    assert candidate(n = 8,k = 8) == 15388352
    assert candidate(n = 25,k = 100) == 99772405924850985256505622172378380436989683840100
    assert candidate(n = 15,k = 100000) == 999999998700012000549989999961002239983899936001489992400009000039999900000
    assert candidate(n = 5,k = 4) == 864
    assert candidate(n = 49,k = 2) == 25172538050
    assert candidate(n = 30,k = 7) == 13470235960809990817824768
    assert candidate(n = 35,k = 100) == 9967365568875105385884863244180601333550953690962746605728641802120000
    assert candidate(n = 1,k = 100000) == 100000
    assert candidate(n = 25,k = 2) == 242786
    assert candidate(n = 25,k = 50000) == 2980232211351919274326324314318672163302392871005965301639287160344502172185624995132866312281249350010499960000050000
    assert candidate(n = 25,k = 100000) == 99999999770002200209995999922102753997789185609597061737751014520104387770212159019999377003443992999989600083999840000100000
    assert candidate(n = 20,k = 5) == 50612096204800
    assert candidate(n = 22,k = 9) == 784949351486331027456
    assert candidate(n = 5,k = 5) == 2800
    assert candidate(n = 30,k = 3) == 14711350935552
    assert candidate(n = 35,k = 7) == 206586368447979697428149305344
    assert candidate(n = 12,k = 10) == 911315617290
    assert candidate(n = 12,k = 10000) == 999999900009002799510001004999610007000299990000
    assert candidate(n = 40,k = 50) == 89602741156971186576848194582434056147913306182627726061058222935050
    assert candidate(n = 35,k = 3) == 2239218190909440
    assert candidate(n = 15,k = 15) == 414567428748533760
    assert candidate(n = 20,k = 2) == 21892
    assert candidate(n = 49,k = 3) == 2890275329929503571968
    assert candidate(n = 49,k = 50) == 174388418958707976132495599422315195551321101858063926373636941158868843553644920050
    assert candidate(n = 25,k = 1000) == 999977022209599223753770865603151524530416714160993773443299896083984001000
    assert candidate(n = 5,k = 100000) == 9999999997000020000000000
    assert candidate(n = 30,k = 5) == 348586958385808670720
    assert candidate(n = 20,k = 3) == 634987008
    assert candidate(n = 30,k = 1) == 0
    assert candidate(n = 40,k = 50000) == 90949468794887807307175503876924559151107081938691540856308664691503678460623124701186645661116529337768436183311345396195389785509588878816359255122460323239420859370693779249935000050000
    assert candidate(n = 25,k = 5) == 132825888566804480
    assert candidate(n = 35,k = 30) == 4828302424321938917457579794849294424245181605164800
    assert candidate(n = 25,k = 10000) == 9999997700220209959992212753977818569597617175114521043677032159199937703443929998960083998400010000
    assert candidate(n = 42,k = 2) == 866988874
    assert candidate(n = 27,k = 10) == 793731690733155352946777790
    assert candidate(n = 45,k = 1000) == 999957042818391667753785447550126192569330183844675051647047945638540344685568740578938651376947284860330629011252227197124029013999000
    assert candidate(n = 40,k = 1000) == 999962037628769628442930171326501255813935595941273094779207838953024124084375279771057154213987250319749311233974001000
    assert candidate(n = 45,k = 15) == 70100013203862820252158826988883466045468054923509760
    assert candidate(n = 50,k = 3) == 7896379049230303494144
    assert candidate(n = 4,k = 4) == 228
    assert candidate(n = 25,k = 1) == 0
    assert candidate(n = 15,k = 100) == 998712539963223837482409039900
    assert candidate(n = 49,k = 100000) == 99999999530004600989980638860536162659651628002247294995378143204787900203641454148891887100911812723235818458208757409403333574885730875773816094836838999139515428510124916987761235051042263801137257159944507702311937999857600359999680000100000
    assert candidate(n = 35,k = 50000) == 291038300725705943302344470866242105832051767032898458360152646584626067576566806732257337227638186312510439361671894618603180659108591686265945749975250030000000000
    assert candidate(n = 15,k = 1) == 0
    assert candidate(n = 10,k = 10) == 9282568410
    assert candidate(n = 50,k = 100) == 9952571356412657726381564909919525409044075662747289070319607611923677876616169583970453167592170000
    assert candidate(n = 30,k = 20) == 1004151076547626230786266566362256795580
    assert candidate(n = 40,k = 20) == 10039746098689777957200971626557993327809319603621620
    assert candidate(n = 47,k = 5000) == 710541457034313051290484603248594260678488454539345543230944707727101837527620429606035600637725264416314535686762408801653878584805972101916304818657952689599955000400000000
    assert candidate(n = 6,k = 100) == 999603009900
    assert candidate(n = 35,k = 2) == 29860704
    assert candidate(n = 9,k = 50000) == 1953124994531343753124900000625004999950000
    assert candidate(n = 15,k = 10) == 886481740149390
    assert candidate(n = 35,k = 5) == 914828192514254359756800
    assert candidate(n = 30,k = 100000) == 999999997200027003249937498276058190174873841243964837285013265897406177303093752257083928348489350012178296040407392173031739942400019000089999900000
    assert candidate(n = 25,k = 30) == 8265309825758255006277731320484013630
    assert candidate(n = 48,k = 500) == 3552061312021803694641285550786487050792994883214147498910757830914643435165384888634893642773774043131571043068997827191378749500
    assert candidate(n = 35,k = 50) == 287291863842135288088949795966532967764016355355305412780000
    assert candidate(n = 12,k = 12) == 8353663189476
    assert candidate(n = 25,k = 50) == 2953434806047058459526357024483280610460050
    assert candidate(n = 49,k = 10) == 6481580482890944147517769612900651151794438116810
    assert candidate(n = 45,k = 20) == 31745674986236020522693749791045360604849067349519696877580
    assert candidate(n = 30,k = 100) == 997230185834338989682696063818771585742574439604682419089900


