def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(color = "#999999") == "#999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#999999") == "#999999": {e}')
    
    total += 1
    try:
        result = candidate(color = "#abcdef") == "#aaccee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#abcdef") == "#aaccee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#000000") == "#000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#000000") == "#000000": {e}')
    
    total += 1
    try:
        result = candidate(color = "#4e3fe1") == "#5544dd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#4e3fe1") == "#5544dd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#aabbcc") == "#aabbcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#aabbcc") == "#aabbcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff0000") == "#ff0000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff0000") == "#ff0000": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffeedd") == "#ffeedd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffeedd") == "#ffeedd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ccbbdd") == "#ccbbdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ccbbdd") == "#ccbbdd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#112233") == "#112233"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#112233") == "#112233": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff00ff") == "#ff00ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff00ff") == "#ff00ff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#1a2b3c") == "#223344"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#1a2b3c") == "#223344": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00ffff") == "#00ffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00ffff") == "#00ffff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00ff00") == "#00ff00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00ff00") == "#00ff00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffffff") == "#ffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffffff") == "#ffffff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#123456") == "#113355"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#123456") == "#113355": {e}')
    
    total += 1
    try:
        result = candidate(color = "#33bbff") == "#33bbff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#33bbff") == "#33bbff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#09f166") == "#11ee66"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#09f166") == "#11ee66": {e}')
    
    total += 1
    try:
        result = candidate(color = "#fedcba") == "#ffddbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#fedcba") == "#ffddbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ccddeeff") == "#ccddee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ccddeeff") == "#ccddee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#c0ffee") == "#bbffee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#c0ffee") == "#bbffee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#dcdcdc") == "#dddddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#dcdcdc") == "#dddddd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#27ae60") == "#22aa66"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#27ae60") == "#22aa66": {e}')
    
    total += 1
    try:
        result = candidate(color = "#daa520") == "#ddaa22"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#daa520") == "#ddaa22": {e}')
    
    total += 1
    try:
        result = candidate(color = "#4a5b6c") == "#445566"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#4a5b6c") == "#445566": {e}')
    
    total += 1
    try:
        result = candidate(color = "#33ff57") == "#33ff55"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#33ff57") == "#33ff55": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffd700") == "#ffdd00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffd700") == "#ffdd00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#9c9c9c") == "#999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#9c9c9c") == "#999999": {e}')
    
    total += 1
    try:
        result = candidate(color = "#9b59b6") == "#9955bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#9b59b6") == "#9955bb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#778899") == "#778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#778899") == "#778899": {e}')
    
    total += 1
    try:
        result = candidate(color = "#1a2b3c4d5e6f") == "#223344"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#1a2b3c4d5e6f") == "#223344": {e}')
    
    total += 1
    try:
        result = candidate(color = "#deadbe") == "#ddaabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#deadbe") == "#ddaabb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#111213") == "#111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#111213") == "#111111": {e}')
    
    total += 1
    try:
        result = candidate(color = "#4b0082") == "#440088"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#4b0082") == "#440088": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff69b4") == "#ff66bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff69b4") == "#ff66bb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f9a2bc") == "#ffaabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f9a2bc") == "#ffaabb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#eeeeee") == "#eeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#eeeeee") == "#eeeeee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#a52a2a") == "#aa2222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#a52a2a") == "#aa2222": {e}')
    
    total += 1
    try:
        result = candidate(color = "#2980b9") == "#2288bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#2980b9") == "#2288bb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f0f0f0") == "#eeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f0f0f0") == "#eeeeee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#008080") == "#008888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#008080") == "#008888": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffdab9") == "#ffddbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffdab9") == "#ffddbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f39c12") == "#ee9911"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f39c12") == "#ee9911": {e}')
    
    total += 1
    try:
        result = candidate(color = "#c3b2a1") == "#bbaa99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#c3b2a1") == "#bbaa99": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffe4b5") == "#ffddbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffe4b5") == "#ffddbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00ccff") == "#00ccff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00ccff") == "#00ccff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffccff") == "#ffccff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffccff") == "#ffccff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00ffcc") == "#00ffcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00ffcc") == "#00ffcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#add8e6") == "#aaddee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#add8e6") == "#aaddee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#3c2b1a") == "#443322"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#3c2b1a") == "#443322": {e}')
    
    total += 1
    try:
        result = candidate(color = "#888888") == "#888888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#888888") == "#888888": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff9933") == "#ff9933"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff9933") == "#ff9933": {e}')
    
    total += 1
    try:
        result = candidate(color = "#34495e") == "#334466"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#34495e") == "#334466": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f5f5dc") == "#eeeedd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f5f5dc") == "#eeeedd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#a4b3c2") == "#aabbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#a4b3c2") == "#aabbbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#d2b48c") == "#ccbb88"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#d2b48c") == "#ccbb88": {e}')
    
    total += 1
    try:
        result = candidate(color = "#babe7ab") == "#bbbb77"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#babe7ab") == "#bbbb77": {e}')
    
    total += 1
    try:
        result = candidate(color = "#e74c3c") == "#ee4444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#e74c3c") == "#ee4444": {e}')
    
    total += 1
    try:
        result = candidate(color = "#cc00ff") == "#cc00ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#cc00ff") == "#cc00ff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#2e8b57") == "#338855"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#2e8b57") == "#338855": {e}')
    
    total += 1
    try:
        result = candidate(color = "#b22222") == "#aa2222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#b22222") == "#aa2222": {e}')
    
    total += 1
    try:
        result = candidate(color = "#333333") == "#333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#333333") == "#333333": {e}')
    
    total += 1
    try:
        result = candidate(color = "#7f8a9b") == "#778899"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#7f8a9b") == "#778899": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f9a8d7") == "#ffaadd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f9a8d7") == "#ffaadd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#afeeee") == "#aaeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#afeeee") == "#aaeeee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#a0a1a2") == "#9999aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#a0a1a2") == "#9999aa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f5deb3") == "#eeddbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f5deb3") == "#eeddbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#d9e8f7") == "#ddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#d9e8f7") == "#ddeeff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#16a085") == "#119988"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#16a085") == "#119988": {e}')
    
    total += 1
    try:
        result = candidate(color = "#beefca") == "#bbeecc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#beefca") == "#bbeecc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#e2f3d4") == "#ddeecc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#e2f3d4") == "#ddeecc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#b3d4f9") == "#bbccff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#b3d4f9") == "#bbccff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ddeeff") == "#ddeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ddeeff") == "#ddeeff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#789abc") == "#7799bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#789abc") == "#7799bb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#95a5a6") == "#99aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#95a5a6") == "#99aaaa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#5a5a5a") == "#555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#5a5a5a") == "#555555": {e}')
    
    total += 1
    try:
        result = candidate(color = "#7890ef") == "#7788ee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#7890ef") == "#7788ee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#88ff44") == "#88ff44"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#88ff44") == "#88ff44": {e}')
    
    total += 1
    try:
        result = candidate(color = "#33aacc") == "#33aacc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#33aacc") == "#33aacc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffffe0") == "#ffffdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffffe0") == "#ffffdd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#191970") == "#111177"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#191970") == "#111177": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f1e2d3") == "#eeddcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f1e2d3") == "#eeddcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#fafad2") == "#ffffcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#fafad2") == "#ffffcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff00cc") == "#ff00cc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff00cc") == "#ff00cc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#123123") == "#113322"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#123123") == "#113322": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff5733") == "#ff5533"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff5733") == "#ff5533": {e}')
    
    total += 1
    try:
        result = candidate(color = "#d2691e") == "#cc6622"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#d2691e") == "#cc6622": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f0e68c") == "#eeee88"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f0e68c") == "#eeee88": {e}')
    
    total += 1
    try:
        result = candidate(color = "#cccccc") == "#cccccc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#cccccc") == "#cccccc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#2c3e50") == "#334455"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#2c3e50") == "#334455": {e}')
    
    total += 1
    try:
        result = candidate(color = "#bbbbbb") == "#bbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#bbbbbb") == "#bbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#eeefff") == "#eeeeff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#eeefff") == "#eeeeff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#998877") == "#998877"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#998877") == "#998877": {e}')
    
    total += 1
    try:
        result = candidate(color = "#7f7f7f") == "#777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#7f7f7f") == "#777777": {e}')
    
    total += 1
    try:
        result = candidate(color = "#555555") == "#555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#555555") == "#555555": {e}')
    
    total += 1
    try:
        result = candidate(color = "#987654") == "#997755"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#987654") == "#997755": {e}')
    
    total += 1
    try:
        result = candidate(color = "#abacadaeaf") == "#aaaaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#abacadaeaf") == "#aaaaaa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#0000cd") == "#0000cc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#0000cd") == "#0000cc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#32cd32") == "#33cc33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#32cd32") == "#33cc33": {e}')
    
    total += 1
    try:
        result = candidate(color = "#0f0f0f") == "#111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#0f0f0f") == "#111111": {e}')
    
    total += 1
    try:
        result = candidate(color = "#9876543210") == "#997755"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#9876543210") == "#997755": {e}')
    
    total += 1
    try:
        result = candidate(color = "#c7d8e9") == "#ccddee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#c7d8e9") == "#ccddee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#face00") == "#ffcc00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#face00") == "#ffcc00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#6b7c8d") == "#667788"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#6b7c8d") == "#667788": {e}')
    
    total += 1
    try:
        result = candidate(color = "#bdbdbd") == "#bbbbbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#bdbdbd") == "#bbbbbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#456789") == "#446688"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#456789") == "#446688": {e}')
    
    total += 1
    try:
        result = candidate(color = "#abcabc") == "#aaccbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#abcabc") == "#aaccbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#2468ac") == "#2266aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#2468ac") == "#2266aa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#696969") == "#666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#696969") == "#666666": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff6347") == "#ff6644"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff6347") == "#ff6644": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffff00") == "#ffff00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffff00") == "#ffff00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00face") == "#00ffcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00face") == "#00ffcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#867530") == "#887733"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#867530") == "#887733": {e}')
    
    total += 1
    try:
        result = candidate(color = "#2ecc71") == "#33cc77"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#2ecc71") == "#33cc77": {e}')
    
    total += 1
    try:
        result = candidate(color = "#dedede") == "#dddddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#dedede") == "#dddddd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff1493") == "#ff1199"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff1493") == "#ff1199": {e}')
    
    total += 1
    try:
        result = candidate(color = "#20b2aa") == "#22aaaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#20b2aa") == "#22aaaa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#7890ab") == "#7788aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#7890ab") == "#7788aa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#9370db") == "#9977dd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#9370db") == "#9977dd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#808080") == "#888888"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#808080") == "#888888": {e}')
    
    total += 1
    try:
        result = candidate(color = "#4682b4") == "#4488bb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#4682b4") == "#4488bb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#8b008b") == "#880088"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#8b008b") == "#880088": {e}')
    
    total += 1
    try:
        result = candidate(color = "#777777") == "#777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#777777") == "#777777": {e}')
    
    total += 1
    try:
        result = candidate(color = "#e67e22") == "#ee7722"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#e67e22") == "#ee7722": {e}')
    
    total += 1
    try:
        result = candidate(color = "#0a0a0a") == "#111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#0a0a0a") == "#111111": {e}')
    
    total += 1
    try:
        result = candidate(color = "#8a2be2") == "#8833dd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#8a2be2") == "#8833dd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#050505") == "#000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#050505") == "#000000": {e}')
    
    total += 1
    try:
        result = candidate(color = "#a1b2c3") == "#99aabb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#a1b2c3") == "#99aabb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ef9078") == "#ee8877"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ef9078") == "#ee8877": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ff4500") == "#ff4400"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ff4500") == "#ff4400": {e}')
    
    total += 1
    try:
        result = candidate(color = "#cafebabe") == "#ccffbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#cafebabe") == "#ccffbb": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffdead") == "#ffddaa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffdead") == "#ffddaa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#102030") == "#112233"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#102030") == "#112233": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffebcd") == "#ffeecc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffebcd") == "#ffeecc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#3b4a5f") == "#334466"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#3b4a5f") == "#334466": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffcc33") == "#ffcc33"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffcc33") == "#ffcc33": {e}')
    
    total += 1
    try:
        result = candidate(color = "#00cc00") == "#00cc00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#00cc00") == "#00cc00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffe4e1") == "#ffdddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffe4e1") == "#ffdddd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#defdef") == "#ddffee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#defdef") == "#ddffee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#5733ff") == "#5533ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#5733ff") == "#5533ff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f1c40f") == "#eecc11"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f1c40f") == "#eecc11": {e}')
    
    total += 1
    try:
        result = candidate(color = "#808000") == "#888800"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#808000") == "#888800": {e}')
    
    total += 1
    try:
        result = candidate(color = "#666666") == "#666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#666666") == "#666666": {e}')
    
    total += 1
    try:
        result = candidate(color = "#000080") == "#000088"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#000080") == "#000088": {e}')
    
    total += 1
    try:
        result = candidate(color = "#5f5f5f") == "#666666"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#5f5f5f") == "#666666": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ccddff") == "#ccddff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ccddff") == "#ccddff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#8e44ad") == "#8844aa"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#8e44ad") == "#8844aa": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f8f8ff") == "#ffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f8f8ff") == "#ffffff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffcc00") == "#ffcc00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffcc00") == "#ffcc00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#008000") == "#008800"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#008000") == "#008800": {e}')
    
    total += 1
    try:
        result = candidate(color = "#800000") == "#880000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#800000") == "#880000": {e}')
    
    total += 1
    try:
        result = candidate(color = "#0000ff") == "#0000ff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#0000ff") == "#0000ff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#654321") == "#664422"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#654321") == "#664422": {e}')
    
    total += 1
    try:
        result = candidate(color = "#f0e1d2") == "#eeddcc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#f0e1d2") == "#eeddcc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#3498db") == "#3399dd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#3498db") == "#3399dd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#dddddd") == "#dddddd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#dddddd") == "#dddddd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#fff8dc") == "#ffffdd"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#fff8dc") == "#ffffdd": {e}')
    
    total += 1
    try:
        result = candidate(color = "#3f3f3f") == "#444444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#3f3f3f") == "#444444": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ccff00") == "#ccff00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ccff00") == "#ccff00": {e}')
    
    total += 1
    try:
        result = candidate(color = "#eaeaea") == "#eeeeee"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#eaeaea") == "#eeeeee": {e}')
    
    total += 1
    try:
        result = candidate(color = "#fefefe") == "#ffffff"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#fefefe") == "#ffffff": {e}')
    
    total += 1
    try:
        result = candidate(color = "#bbaacc") == "#bbaacc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#bbaacc") == "#bbaacc": {e}')
    
    total += 1
    try:
        result = candidate(color = "#010101") == "#000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#010101") == "#000000": {e}')
    
    total += 1
    try:
        result = candidate(color = "#7b7b7b") == "#777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#7b7b7b") == "#777777": {e}')
    
    total += 1
    try:
        result = candidate(color = "#800080") == "#880088"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#800080") == "#880088": {e}')
    
    total += 1
    try:
        result = candidate(color = "#1abc9c") == "#22bb99"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#1abc9c") == "#22bb99": {e}')
    
    total += 1
    try:
        result = candidate(color = "#0a0b0c") == "#111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#0a0b0c") == "#111111": {e}')
    
    total += 1
    try:
        result = candidate(color = "#ffa500") == "#ffaa00"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(color = "#ffa500") == "#ffaa00": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(color = "#999999") == "#999999"
    assert candidate(color = "#abcdef") == "#aaccee"
    assert candidate(color = "#000000") == "#000000"
    assert candidate(color = "#4e3fe1") == "#5544dd"
    assert candidate(color = "#aabbcc") == "#aabbcc"
    assert candidate(color = "#ff0000") == "#ff0000"
    assert candidate(color = "#ffeedd") == "#ffeedd"
    assert candidate(color = "#ccbbdd") == "#ccbbdd"
    assert candidate(color = "#112233") == "#112233"
    assert candidate(color = "#ff00ff") == "#ff00ff"
    assert candidate(color = "#1a2b3c") == "#223344"
    assert candidate(color = "#00ffff") == "#00ffff"
    assert candidate(color = "#00ff00") == "#00ff00"
    assert candidate(color = "#ffffff") == "#ffffff"
    assert candidate(color = "#123456") == "#113355"
    assert candidate(color = "#33bbff") == "#33bbff"
    assert candidate(color = "#09f166") == "#11ee66"
    assert candidate(color = "#fedcba") == "#ffddbb"
    assert candidate(color = "#ccddeeff") == "#ccddee"
    assert candidate(color = "#c0ffee") == "#bbffee"
    assert candidate(color = "#dcdcdc") == "#dddddd"
    assert candidate(color = "#27ae60") == "#22aa66"
    assert candidate(color = "#daa520") == "#ddaa22"
    assert candidate(color = "#4a5b6c") == "#445566"
    assert candidate(color = "#33ff57") == "#33ff55"
    assert candidate(color = "#ffd700") == "#ffdd00"
    assert candidate(color = "#9c9c9c") == "#999999"
    assert candidate(color = "#9b59b6") == "#9955bb"
    assert candidate(color = "#778899") == "#778899"
    assert candidate(color = "#1a2b3c4d5e6f") == "#223344"
    assert candidate(color = "#deadbe") == "#ddaabb"
    assert candidate(color = "#111213") == "#111111"
    assert candidate(color = "#4b0082") == "#440088"
    assert candidate(color = "#ff69b4") == "#ff66bb"
    assert candidate(color = "#f9a2bc") == "#ffaabb"
    assert candidate(color = "#eeeeee") == "#eeeeee"
    assert candidate(color = "#a52a2a") == "#aa2222"
    assert candidate(color = "#2980b9") == "#2288bb"
    assert candidate(color = "#f0f0f0") == "#eeeeee"
    assert candidate(color = "#008080") == "#008888"
    assert candidate(color = "#ffdab9") == "#ffddbb"
    assert candidate(color = "#f39c12") == "#ee9911"
    assert candidate(color = "#c3b2a1") == "#bbaa99"
    assert candidate(color = "#ffe4b5") == "#ffddbb"
    assert candidate(color = "#00ccff") == "#00ccff"
    assert candidate(color = "#ffccff") == "#ffccff"
    assert candidate(color = "#00ffcc") == "#00ffcc"
    assert candidate(color = "#add8e6") == "#aaddee"
    assert candidate(color = "#3c2b1a") == "#443322"
    assert candidate(color = "#888888") == "#888888"
    assert candidate(color = "#ff9933") == "#ff9933"
    assert candidate(color = "#34495e") == "#334466"
    assert candidate(color = "#f5f5dc") == "#eeeedd"
    assert candidate(color = "#a4b3c2") == "#aabbbb"
    assert candidate(color = "#d2b48c") == "#ccbb88"
    assert candidate(color = "#babe7ab") == "#bbbb77"
    assert candidate(color = "#e74c3c") == "#ee4444"
    assert candidate(color = "#cc00ff") == "#cc00ff"
    assert candidate(color = "#2e8b57") == "#338855"
    assert candidate(color = "#b22222") == "#aa2222"
    assert candidate(color = "#333333") == "#333333"
    assert candidate(color = "#7f8a9b") == "#778899"
    assert candidate(color = "#f9a8d7") == "#ffaadd"
    assert candidate(color = "#afeeee") == "#aaeeee"
    assert candidate(color = "#a0a1a2") == "#9999aa"
    assert candidate(color = "#f5deb3") == "#eeddbb"
    assert candidate(color = "#d9e8f7") == "#ddeeff"
    assert candidate(color = "#16a085") == "#119988"
    assert candidate(color = "#beefca") == "#bbeecc"
    assert candidate(color = "#e2f3d4") == "#ddeecc"
    assert candidate(color = "#b3d4f9") == "#bbccff"
    assert candidate(color = "#ddeeff") == "#ddeeff"
    assert candidate(color = "#789abc") == "#7799bb"
    assert candidate(color = "#95a5a6") == "#99aaaa"
    assert candidate(color = "#5a5a5a") == "#555555"
    assert candidate(color = "#7890ef") == "#7788ee"
    assert candidate(color = "#88ff44") == "#88ff44"
    assert candidate(color = "#33aacc") == "#33aacc"
    assert candidate(color = "#ffffe0") == "#ffffdd"
    assert candidate(color = "#191970") == "#111177"
    assert candidate(color = "#f1e2d3") == "#eeddcc"
    assert candidate(color = "#fafad2") == "#ffffcc"
    assert candidate(color = "#ff00cc") == "#ff00cc"
    assert candidate(color = "#123123") == "#113322"
    assert candidate(color = "#ff5733") == "#ff5533"
    assert candidate(color = "#d2691e") == "#cc6622"
    assert candidate(color = "#f0e68c") == "#eeee88"
    assert candidate(color = "#cccccc") == "#cccccc"
    assert candidate(color = "#2c3e50") == "#334455"
    assert candidate(color = "#bbbbbb") == "#bbbbbb"
    assert candidate(color = "#eeefff") == "#eeeeff"
    assert candidate(color = "#998877") == "#998877"
    assert candidate(color = "#7f7f7f") == "#777777"
    assert candidate(color = "#555555") == "#555555"
    assert candidate(color = "#987654") == "#997755"
    assert candidate(color = "#abacadaeaf") == "#aaaaaa"
    assert candidate(color = "#0000cd") == "#0000cc"
    assert candidate(color = "#32cd32") == "#33cc33"
    assert candidate(color = "#0f0f0f") == "#111111"
    assert candidate(color = "#9876543210") == "#997755"
    assert candidate(color = "#c7d8e9") == "#ccddee"
    assert candidate(color = "#face00") == "#ffcc00"
    assert candidate(color = "#6b7c8d") == "#667788"
    assert candidate(color = "#bdbdbd") == "#bbbbbb"
    assert candidate(color = "#456789") == "#446688"
    assert candidate(color = "#abcabc") == "#aaccbb"
    assert candidate(color = "#2468ac") == "#2266aa"
    assert candidate(color = "#696969") == "#666666"
    assert candidate(color = "#ff6347") == "#ff6644"
    assert candidate(color = "#ffff00") == "#ffff00"
    assert candidate(color = "#00face") == "#00ffcc"
    assert candidate(color = "#867530") == "#887733"
    assert candidate(color = "#2ecc71") == "#33cc77"
    assert candidate(color = "#dedede") == "#dddddd"
    assert candidate(color = "#ff1493") == "#ff1199"
    assert candidate(color = "#20b2aa") == "#22aaaa"
    assert candidate(color = "#7890ab") == "#7788aa"
    assert candidate(color = "#9370db") == "#9977dd"
    assert candidate(color = "#808080") == "#888888"
    assert candidate(color = "#4682b4") == "#4488bb"
    assert candidate(color = "#8b008b") == "#880088"
    assert candidate(color = "#777777") == "#777777"
    assert candidate(color = "#e67e22") == "#ee7722"
    assert candidate(color = "#0a0a0a") == "#111111"
    assert candidate(color = "#8a2be2") == "#8833dd"
    assert candidate(color = "#050505") == "#000000"
    assert candidate(color = "#a1b2c3") == "#99aabb"
    assert candidate(color = "#ef9078") == "#ee8877"
    assert candidate(color = "#ff4500") == "#ff4400"
    assert candidate(color = "#cafebabe") == "#ccffbb"
    assert candidate(color = "#ffdead") == "#ffddaa"
    assert candidate(color = "#102030") == "#112233"
    assert candidate(color = "#ffebcd") == "#ffeecc"
    assert candidate(color = "#3b4a5f") == "#334466"
    assert candidate(color = "#ffcc33") == "#ffcc33"
    assert candidate(color = "#00cc00") == "#00cc00"
    assert candidate(color = "#ffe4e1") == "#ffdddd"
    assert candidate(color = "#defdef") == "#ddffee"
    assert candidate(color = "#5733ff") == "#5533ff"
    assert candidate(color = "#f1c40f") == "#eecc11"
    assert candidate(color = "#808000") == "#888800"
    assert candidate(color = "#666666") == "#666666"
    assert candidate(color = "#000080") == "#000088"
    assert candidate(color = "#5f5f5f") == "#666666"
    assert candidate(color = "#ccddff") == "#ccddff"
    assert candidate(color = "#8e44ad") == "#8844aa"
    assert candidate(color = "#f8f8ff") == "#ffffff"
    assert candidate(color = "#ffcc00") == "#ffcc00"
    assert candidate(color = "#008000") == "#008800"
    assert candidate(color = "#800000") == "#880000"
    assert candidate(color = "#0000ff") == "#0000ff"
    assert candidate(color = "#654321") == "#664422"
    assert candidate(color = "#f0e1d2") == "#eeddcc"
    assert candidate(color = "#3498db") == "#3399dd"
    assert candidate(color = "#dddddd") == "#dddddd"
    assert candidate(color = "#fff8dc") == "#ffffdd"
    assert candidate(color = "#3f3f3f") == "#444444"
    assert candidate(color = "#ccff00") == "#ccff00"
    assert candidate(color = "#eaeaea") == "#eeeeee"
    assert candidate(color = "#fefefe") == "#ffffff"
    assert candidate(color = "#bbaacc") == "#bbaacc"
    assert candidate(color = "#010101") == "#000000"
    assert candidate(color = "#7b7b7b") == "#777777"
    assert candidate(color = "#800080") == "#880088"
    assert candidate(color = "#1abc9c") == "#22bb99"
    assert candidate(color = "#0a0b0c") == "#111111"
    assert candidate(color = "#ffa500") == "#ffaa00"


