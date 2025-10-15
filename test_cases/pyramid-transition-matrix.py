def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(bottom = "FFFA",allowed = ['FFF', 'FFA', 'FAF', 'AFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FFFA",allowed = ['FFF', 'FFA', 'FAF', 'AFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABC",allowed = ['ABD', 'BDC', 'CDB', 'BDD', 'DEF', 'DEE']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABC",allowed = ['ABD', 'BDC', 'CDB', 'BDD', 'DEF', 'DEE']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF', 'GHI']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF', 'GHI']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "CDC",allowed = ['ABA', 'ACA', 'BCD', 'BDA', 'CDE', 'CBD', 'DEC', 'DEF', 'FFF']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "CDC",allowed = ['ABA', 'ACA', 'BCD', 'BDA', 'CDE', 'CBD', 'DEC', 'DEF', 'FFF']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XXY",allowed = ['XXY', 'XYX', 'YXX', 'XYY', 'YYX', 'YYY']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XXY",allowed = ['XXY', 'XYX', 'YXX', 'XYY', 'YYX', 'YYY']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "BCD",allowed = ['BCC', 'CDE', 'CEA', 'FFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "BCD",allowed = ['BCC', 'CDE', 'CEA', 'FFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XXY",allowed = ['XYX', 'XYD', 'YXZ', 'XYZ', 'XZX', 'XYX', 'YZX', 'XYZ', 'XYZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XXY",allowed = ['XYX', 'XYD', 'YXZ', 'XYZ', 'XZX', 'XYX', 'YZX', 'XYZ', 'XYZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "BDD",allowed = ['ABB', 'ACB', 'BDC', 'BDB', 'BCC', 'BDD', 'CCC', 'BCB', 'CBC', 'DEC', 'CDB', 'DEB', 'CDE']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "BDD",allowed = ['ABB', 'ACB', 'BDC', 'BDB', 'BCC', 'BDD', 'CCC', 'BCB', 'CBC', 'DEC', 'CDB', 'DEB', 'CDE']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AB",allowed = ['ABA', 'ABB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AB",allowed = ['ABA', 'ABB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AFA",allowed = ['AFF', 'FAA', 'FFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AFA",allowed = ['AFF', 'FAA', 'FFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XYZ",allowed = ['XYA', 'YZB', 'AXY', 'BYZ', 'XYZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XYZ",allowed = ['XYA', 'YZB', 'AXY', 'BYZ', 'XYZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABC",allowed = ['ABA', 'BCB', 'ACA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABC",allowed = ['ABA', 'BCB', 'ACA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AAAA",allowed = ['AAB', 'AAC', 'BCD', 'BBE', 'DEF']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AAAA",allowed = ['AAB', 'AAC', 'BCD', 'BBE', 'DEF']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "CCD",allowed = ['CCC', 'CDC', 'CDD', 'DDD']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "CCD",allowed = ['CCC', 'CDC', 'CDD', 'DDD']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XYZ",allowed = ['XYX', 'YZY', 'ZXZ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XYZ",allowed = ['XYX', 'YZY', 'ZXZ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "BCDE",allowed = ['BCF', 'CDE', 'DEF', 'EFG', 'FGH']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "BCDE",allowed = ['BCF', 'CDE', 'DEF', 'EFG', 'FGH']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCD",allowed = ['ABA', 'BAC', 'CAD', 'ADC', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCD",allowed = ['ABA', 'BAC', 'CAD', 'ADC', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEFA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEFA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGG', 'GGA', 'GGB', 'GBC', 'GCD', 'GDE', 'GEF', 'GFG', 'GHH', 'HHA', 'HHB', 'HHC', 'HHD', 'HEH', 'HHF', 'HGG', 'HHH']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGG', 'GGA', 'GGB', 'GBC', 'GCD', 'GDE', 'GEF', 'GFG', 'GHH', 'HHA', 'HHB', 'HHC', 'HHD', 'HEH', 'HHF', 'HGG', 'HHH']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AABBB",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBB', 'BBA', 'BAB', 'BAA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AABBB",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBB', 'BBA', 'BAB', 'BAA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABF', 'BCG', 'CDF', 'DEH', 'EFA', 'FGA', 'GHB', 'HHA', 'HIB', 'IBC', 'JCA', 'KBD', 'LCE', 'MDF', 'NEG', 'OFA', 'PGH', 'QHI', 'RIB', 'SJC', 'TKD', 'ULC', 'VMF', 'WNG', 'XOH', 'YPI', 'ZQJ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABF', 'BCG', 'CDF', 'DEH', 'EFA', 'FGA', 'GHB', 'HHA', 'HIB', 'IBC', 'JCA', 'KBD', 'LCE', 'MDF', 'NEG', 'OFA', 'PGH', 'QHI', 'RIB', 'SJC', 'TKD', 'ULC', 'VMF', 'WNG', 'XOH', 'YPI', 'ZQJ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "BCD",allowed = ['BCD', 'CDE', 'DEE', 'EEA', 'EAB', 'ABC', 'BCA', 'CAB', 'BAC', 'ACB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "BCD",allowed = ['BCD', 'CDE', 'DEE', 'EEA', 'EAB', 'ABC', 'BCA', 'CAB', 'BAC', 'ACB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'CAB', 'ABC', 'BCA', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA', 'ACF', 'CFA', 'FAC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'CAB', 'ABC', 'BCA', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA', 'ACF', 'CFA', 'FAC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA', 'BBB', 'AAC', 'ACA', 'ACC', 'BAC', 'BCA', 'BCB', 'BBC', 'BCC', 'CCC', 'CCA', 'CCC', 'BCC', 'CCC', 'CCC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA', 'BBB', 'AAC', 'ACA', 'ACC', 'BAC', 'BCA', 'BCB', 'BBC', 'BCC', 'CCC', 'CCA', 'CCC', 'BCC', 'CCC', 'CCC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HIG', 'IHA', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HIG', 'IHA', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEE', 'EEF', 'EFA', 'FAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEE', 'EEF', 'EFA', 'FAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCABC",allowed = ['ABA', 'BCB', 'CAC', 'CBC', 'BDB', 'CDC', 'ADA', 'AEA', 'CEC', 'DEC', 'BEB', 'FEC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCABC",allowed = ['ABA', 'BCB', 'CAC', 'CBC', 'BDB', 'CDC', 'ADA', 'AEA', 'CEC', 'DEC', 'BEB', 'FEC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDD', 'DCC', 'CCB', 'BBA', 'AAB', 'ABD', 'BCE', 'DEF', 'FFF', 'GHI', 'IJH', 'KIG', 'LIF', 'MEG', 'NHF', 'OGI', 'PHJ', 'QIK', 'RLH', 'SGM', 'THN', 'UIO', 'VJP', 'WKQ', 'XLR', 'YMV', 'ZNW', 'AOX', 'BQP', 'CRS', 'DUT', 'EVV', 'FWW', 'GXW', 'HYX', 'IZY', 'JZZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDD', 'DCC', 'CCB', 'BBA', 'AAB', 'ABD', 'BCE', 'DEF', 'FFF', 'GHI', 'IJH', 'KIG', 'LIF', 'MEG', 'NHF', 'OGI', 'PHJ', 'QIK', 'RLH', 'SGM', 'THN', 'UIO', 'VJP', 'WKQ', 'XLR', 'YMV', 'ZNW', 'AOX', 'BQP', 'CRS', 'DUT', 'EVV', 'FWW', 'GXW', 'HYX', 'IZY', 'JZZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XYZXYZ",allowed = ['XYA', 'YZB', 'ZXC', 'XYD', 'YZE', 'ZXF', 'XYG', 'YZH', 'ZXI', 'XYJ', 'YZK', 'ZXL', 'XYM', 'YZN', 'ZXM', 'XYP', 'YZQ', 'ZXZ', 'XYX', 'YZY', 'ZXZ', 'XZX', 'YZX', 'ZZX', 'XXY', 'YZZ', 'ZZY', 'XXZ', 'YXY', 'ZYZ', 'XYX', 'YZY', 'ZXZ', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XYZXYZ",allowed = ['XYA', 'YZB', 'ZXC', 'XYD', 'YZE', 'ZXF', 'XYG', 'YZH', 'ZXI', 'XYJ', 'YZK', 'ZXL', 'XYM', 'YZN', 'ZXM', 'XYP', 'YZQ', 'ZXZ', 'XYX', 'YZY', 'ZXZ', 'XZX', 'YZX', 'ZZX', 'XXY', 'YZZ', 'ZZY', 'XXZ', 'YXY', 'ZYZ', 'XYX', 'YZY', 'ZXZ', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABE', 'BCD', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BCF', 'CDA', 'DEB', 'EFC', 'FAB', 'GBC', 'HCD', 'IEA', 'JFB', 'KGA', 'LHB', 'MIA', 'NJB', 'OKC', 'PLD', 'QME', 'RNF', 'SGO', 'THP', 'UIQ', 'VRJ', 'WTK', 'XSL', 'YMV', 'ZNU']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABE', 'BCD', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BCF', 'CDA', 'DEB', 'EFC', 'FAB', 'GBC', 'HCD', 'IEA', 'JFB', 'KGA', 'LHB', 'MIA', 'NJB', 'OKC', 'PLD', 'QME', 'RNF', 'SGO', 'THP', 'UIQ', 'VRJ', 'WTK', 'XSL', 'YMV', 'ZNU']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEFG",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEFG",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCD",allowed = ['ABC', 'BCD', 'CDA', 'DAB', 'ABE', 'BCE', 'CEA', 'EAB', 'ACD', 'CDB', 'DBA', 'BAC', 'CAD', 'DCA', 'ACF', 'CFE', 'FEA', 'EAC', 'BDF', 'DFG', 'FGH', 'GHB', 'CDF', 'DFH', 'FHG', 'HGD', 'ACE', 'CEB', 'EBD', 'DBA', 'CFA', 'FAB', 'ABF', 'BFD', 'FDC', 'DCB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCD",allowed = ['ABC', 'BCD', 'CDA', 'DAB', 'ABE', 'BCE', 'CEA', 'EAB', 'ACD', 'CDB', 'DBA', 'BAC', 'CAD', 'DCA', 'ACF', 'CFE', 'FEA', 'EAC', 'BDF', 'DFG', 'FGH', 'GHB', 'CDF', 'DFH', 'FHG', 'HGD', 'ACE', 'CEB', 'EBD', 'DBA', 'CFA', 'FAB', 'ABF', 'BFD', 'FDC', 'DCB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCD",allowed = ['ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ABC']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCD",allowed = ['ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ABC']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ACF",allowed = ['ACF', 'CFA', 'FAC', 'BAC', 'BCA', 'CAB', 'ACB', 'BCC', 'CBA', 'ABC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ACF",allowed = ['ACF', 'CFA', 'FAC', 'BAC', 'BCA', 'CAB', 'ACB', 'BCC', 'CBA', 'ABC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDC', 'DBA', 'CBA', 'BAE', 'AEG']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDC', 'DBA', 'CBA', 'BAE', 'AEG']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB', 'BAE', 'AEC', 'ECF', 'CFD', 'DFG', 'FGH', 'GHG', 'HGH', 'GGH']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB', 'BAE', 'AEC', 'ECF', 'CFD', 'DFG', 'FGH', 'GHG', 'HGH', 'GGH']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'BCG', 'CGD', 'DGE', 'EGF', 'FGH', 'GHJ', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'BCG', 'CGD', 'DGE', 'EGF', 'FGH', 'GHJ', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FFFFF",allowed = ['FFF', 'FFG', 'FGF', 'GFF', 'GGG', 'FGG', 'GFG', 'GGF', 'FGH', 'GHF', 'GFG', 'HFG', 'FGF', 'GGG', 'FGF', 'GFG']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FFFFF",allowed = ['FFF', 'FFG', 'FGF', 'GFF', 'GGG', 'FGG', 'GFG', 'GGF', 'FGH', 'GHF', 'GFG', 'HFG', 'FGF', 'GGG', 'FGF', 'GFG']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABACD",allowed = ['ABA', 'BAC', 'ACD', 'CDE', 'DEA', 'EAB', 'ABC', 'BCD', 'CDA', 'DAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABACD",allowed = ['ABA', 'BAC', 'ACD', 'CDE', 'DEA', 'EAB', 'ABC', 'BCD', 'CDA', 'DAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCD",allowed = ['ABE', 'BCE', 'CDE', 'DEF', 'EFG', 'FGH']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCD",allowed = ['ABE', 'BCE', 'CDE', 'DEF', 'EFG', 'FGH']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "XYZXYZ",allowed = ['XYZ', 'YZX', 'ZXY', 'XZY', 'ZYX', 'YXZ', 'XYX', 'YYX', 'YXY', 'YXX', 'XXX', 'XXY', 'XYY', 'XZX', 'XZX', 'XZY', 'XYX', 'XYZ', 'YZX', 'ZXY', 'YZY', 'ZYY', 'ZZY', 'ZZZ', 'YZZ', 'XZZ', 'XXZ', 'XYX', 'XYZ', 'YYX', 'YXY', 'YZY', 'YZZ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "XYZXYZ",allowed = ['XYZ', 'YZX', 'ZXY', 'XZY', 'ZYX', 'YXZ', 'XYX', 'YYX', 'YXY', 'YXX', 'XXX', 'XXY', 'XYY', 'XZX', 'XZX', 'XZY', 'XYX', 'XYZ', 'YZX', 'ZXY', 'YZY', 'ZYY', 'ZZY', 'ZZZ', 'YZZ', 'XZZ', 'XXZ', 'XYX', 'XYZ', 'YYX', 'YXY', 'YZY', 'YZZ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AABB",allowed = ['AAB', 'ABA', 'BAA', 'AAA', 'BBB', 'ABB', 'BBA', 'BAB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AABB",allowed = ['AAB', 'ABA', 'BAA', 'AAA', 'BBB', 'ABB', 'BBA', 'BAB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "EABCD",allowed = ['EAB', 'ABF', 'BCG', 'CDF', 'DEH', 'FGI', 'GHI']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "EABCD",allowed = ['EAB', 'ABF', 'BCG', 'CDF', 'DEH', 'FGI', 'GHI']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDE",allowed = ['ABB', 'BCC', 'CDD', 'DEE', 'EFF', 'FGG', 'GHH', 'HHI']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDE",allowed = ['ABB', 'BCC', 'CDD', 'DEE', 'EFF', 'FGG', 'GHH', 'HHI']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ACDF",allowed = ['ACA', 'CDF', 'ACF', 'CDF', 'CAF', 'FAC', 'FCA', 'FCD', 'DFC', 'FDC', 'ADC', 'CAD', 'ACD', 'CDA', 'CAF', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ACDF",allowed = ['ACA', 'CDF', 'ACF', 'CDF', 'CAF', 'FAC', 'FCA', 'FCD', 'DFC', 'FDC', 'ADC', 'CAD', 'ACD', 'CDA', 'CAF', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FAEBC",allowed = ['FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FAEBC",allowed = ['FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCABC",allowed = ['ABA', 'BAC', 'ACB', 'BCA', 'CAB', 'CBA', 'AAB', 'BAA', 'ABB', 'BBA', 'AAC', 'CAA', 'ACC', 'CCA', 'BCC', 'CBB', 'BBB', 'AAA', 'CCC', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCABC",allowed = ['ABA', 'BAC', 'ACB', 'BCA', 'CAB', 'CBA', 'AAB', 'BAA', 'ABB', 'BBA', 'AAC', 'CAA', 'ACC', 'CCA', 'BCC', 'CBB', 'BBB', 'AAA', 'CCC', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCFE",allowed = ['ABC', 'BCF', 'CFE', 'FED', 'EDA', 'DAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB', 'BCE']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCFE",allowed = ['ABC', 'BCF', 'CFE', 'FED', 'EDA', 'DAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB', 'BCE']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABAC",allowed = ['ABA', 'BAC', 'ACA', 'BAA', 'CAA', 'ACB', 'CBA', 'BAB', 'ABA', 'BAA', 'AAB', 'BBA', 'ABA', 'ABB', 'BAC', 'BAA', 'BBA', 'BBA', 'BAC', 'BAC', 'BAC', 'BAC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABAC",allowed = ['ABA', 'BAC', 'ACA', 'BAA', 'CAA', 'ACB', 'CBA', 'BAB', 'ABA', 'BAA', 'AAB', 'BBA', 'ABA', 'ABB', 'BAC', 'BAA', 'BBA', 'BBA', 'BAC', 'BAC', 'BAC', 'BAC']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABG', 'BCG', 'CDG', 'DEG', 'EFG', 'FGA', 'GAB', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHG', 'CHD', 'DHE', 'EFH', 'FGH', 'GHG', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDC', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABG', 'BCG', 'CDG', 'DEG', 'EFG', 'FGA', 'GAB', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHG', 'CHD', 'DHE', 'EFH', 'FGH', 'GHG', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDC', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBA', 'BAB', 'BAA', 'BBB', 'ABA', 'AAA', 'BBA', 'BAA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBA', 'BAB', 'BAA', 'BBB', 'ABA', 'AAA', 'BBA', 'BAA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDC', 'DED', 'EFE', 'FGF', 'GAG', 'GBG', 'GGG', 'GHH', 'GHI', 'GJJ', 'GJG', 'HJH', 'HJI', 'HJG', 'IJJ', 'IJK', 'IJG', 'JKJ', 'JKK', 'JKG', 'KLL', 'KLK', 'KLG', 'LLL', 'LLM', 'LLG', 'MLM', 'MLN', 'MLG', 'NLO', 'NLP', 'NMG', 'OOO', 'OOP', 'ONP', 'PPP', 'PPQ', 'PMQ', 'QQQ', 'QQR', 'QSR', 'RRR', 'RSS', 'RST', 'SSS', 'SST', 'TTT', 'TTU', 'TTV', 'UUU', 'UUV', 'UVU', 'VVV', 'VVW', 'WWW']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDC', 'DED', 'EFE', 'FGF', 'GAG', 'GBG', 'GGG', 'GHH', 'GHI', 'GJJ', 'GJG', 'HJH', 'HJI', 'HJG', 'IJJ', 'IJK', 'IJG', 'JKJ', 'JKK', 'JKG', 'KLL', 'KLK', 'KLG', 'LLL', 'LLM', 'LLG', 'MLM', 'MLN', 'MLG', 'NLO', 'NLP', 'NMG', 'OOO', 'OOP', 'ONP', 'PPP', 'PPQ', 'PMQ', 'QQQ', 'QQR', 'QSR', 'RRR', 'RSS', 'RST', 'SSS', 'SST', 'TTT', 'TTU', 'TTV', 'UUU', 'UUV', 'UVU', 'VVV', 'VVW', 'WWW']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABACAB",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABACAB",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == True: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BDA', 'DBA', 'ADB', 'CDB', 'DCB', 'BEC', 'ECB', 'CEB', 'DCE', 'EDC', 'DEC', 'FED', 'EFD', 'FDE', 'DFE', 'EDE', 'DED', 'EEF', 'FEF', 'EFF', 'FFF', 'FGF', 'GFF', 'FGG', 'GGF', 'GFG', 'GGG']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BDA', 'DBA', 'ADB', 'CDB', 'DCB', 'BEC', 'ECB', 'CEB', 'DCE', 'EDC', 'DEC', 'FED', 'EFD', 'FDE', 'DFE', 'EDE', 'DED', 'EEF', 'FEF', 'EFF', 'FFF', 'FGF', 'GFF', 'FGG', 'GGF', 'GFG', 'GGG']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAF', 'AFB', 'FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAF', 'AFB', 'FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI']) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI']) == False: {e}')
    
    total += 1
    try:
        result = candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(bottom = "FFFA",allowed = ['FFF', 'FFA', 'FAF', 'AFF']) == True
    assert candidate(bottom = "ABC",allowed = ['ABD', 'BDC', 'CDB', 'BDD', 'DEF', 'DEE']) == False
    assert candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF']) == True
    assert candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF', 'GHI']) == True
    assert candidate(bottom = "CDC",allowed = ['ABA', 'ACA', 'BCD', 'BDA', 'CDE', 'CBD', 'DEC', 'DEF', 'FFF']) == False
    assert candidate(bottom = "XXY",allowed = ['XXY', 'XYX', 'YXX', 'XYY', 'YYX', 'YYY']) == True
    assert candidate(bottom = "BCD",allowed = ['BCC', 'CDE', 'CEA', 'FFF']) == True
    assert candidate(bottom = "XXY",allowed = ['XYX', 'XYD', 'YXZ', 'XYZ', 'XZX', 'XYX', 'YZX', 'XYZ', 'XYZ']) == False
    assert candidate(bottom = "BDD",allowed = ['ABB', 'ACB', 'BDC', 'BDB', 'BCC', 'BDD', 'CCC', 'BCB', 'CBC', 'DEC', 'CDB', 'DEB', 'CDE']) == False
    assert candidate(bottom = "AB",allowed = ['ABA', 'ABB']) == True
    assert candidate(bottom = "AFA",allowed = ['AFF', 'FAA', 'FFF']) == True
    assert candidate(bottom = "XYZ",allowed = ['XYA', 'YZB', 'AXY', 'BYZ', 'XYZ']) == False
    assert candidate(bottom = "ABC",allowed = ['ABD', 'BCE', 'DEF', 'FFF']) == True
    assert candidate(bottom = "ABC",allowed = ['ABA', 'BCB', 'ACA']) == True
    assert candidate(bottom = "AAAA",allowed = ['AAB', 'AAC', 'BCD', 'BBE', 'DEF']) == False
    assert candidate(bottom = "CCD",allowed = ['CCC', 'CDC', 'CDD', 'DDD']) == True
    assert candidate(bottom = "XYZ",allowed = ['XYX', 'YZY', 'ZXZ']) == True
    assert candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB']) == False
    assert candidate(bottom = "BCDE",allowed = ['BCF', 'CDE', 'DEF', 'EFG', 'FGH']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True
    assert candidate(bottom = "ABCD",allowed = ['ABA', 'BAC', 'CAD', 'ADC', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA']) == True
    assert candidate(bottom = "ABCDEFA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA']) == True
    assert candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGG', 'GGA', 'GGB', 'GBC', 'GCD', 'GDE', 'GEF', 'GFG', 'GHH', 'HHA', 'HHB', 'HHC', 'HHD', 'HEH', 'HHF', 'HGG', 'HHH']) == True
    assert candidate(bottom = "AABBB",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBB', 'BBA', 'BAB', 'BAA']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABF', 'BCG', 'CDF', 'DEH', 'EFA', 'FGA', 'GHB', 'HHA', 'HIB', 'IBC', 'JCA', 'KBD', 'LCE', 'MDF', 'NEG', 'OFA', 'PGH', 'QHI', 'RIB', 'SJC', 'TKD', 'ULC', 'VMF', 'WNG', 'XOH', 'YPI', 'ZQJ']) == False
    assert candidate(bottom = "BCD",allowed = ['BCD', 'CDE', 'DEE', 'EEA', 'EAB', 'ABC', 'BCA', 'CAB', 'BAC', 'ACB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
    assert candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI']) == True
    assert candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB']) == False
    assert candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'CAB', 'ABC', 'BCA', 'BCD', 'CDB', 'DBD', 'BCF', 'CFF', 'FFA', 'ACF', 'CFA', 'FAC']) == True
    assert candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA', 'BBB', 'AAC', 'ACA', 'ACC', 'BAC', 'BCA', 'BCB', 'BBC', 'BCC', 'CCC', 'CCA', 'CCC', 'BCC', 'CCC', 'CCC']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HIG', 'IHA', 'IDB', 'DEB', 'EFC', 'FDC', 'DGB', 'EHB', 'FHC', 'GHA', 'HIB', 'IDA', 'IDB', 'IDC', 'IDE', 'IDF', 'IDG', 'IDH', 'IDI']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH']) == False
    assert candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEE', 'EEF', 'EFA', 'FAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB']) == True
    assert candidate(bottom = "ABCABC",allowed = ['ABA', 'BCB', 'CAC', 'CBC', 'BDB', 'CDC', 'ADA', 'AEA', 'CEC', 'DEC', 'BEB', 'FEC']) == True
    assert candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDD', 'DCC', 'CCB', 'BBA', 'AAB', 'ABD', 'BCE', 'DEF', 'FFF', 'GHI', 'IJH', 'KIG', 'LIF', 'MEG', 'NHF', 'OGI', 'PHJ', 'QIK', 'RLH', 'SGM', 'THN', 'UIO', 'VJP', 'WKQ', 'XLR', 'YMV', 'ZNW', 'AOX', 'BQP', 'CRS', 'DUT', 'EVV', 'FWW', 'GXW', 'HYX', 'IZY', 'JZZ']) == False
    assert candidate(bottom = "XYZXYZ",allowed = ['XYA', 'YZB', 'ZXC', 'XYD', 'YZE', 'ZXF', 'XYG', 'YZH', 'ZXI', 'XYJ', 'YZK', 'ZXL', 'XYM', 'YZN', 'ZXM', 'XYP', 'YZQ', 'ZXZ', 'XYX', 'YZY', 'ZXZ', 'XZX', 'YZX', 'ZZX', 'XXY', 'YZZ', 'ZZY', 'XXZ', 'YXY', 'ZYZ', 'XYX', 'YZY', 'ZXZ', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX', 'XYZ', 'YZX', 'ZXY', 'XZY', 'YZZ', 'ZZX']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABE', 'BCD', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BCF', 'CDA', 'DEB', 'EFC', 'FAB', 'GBC', 'HCD', 'IEA', 'JFB', 'KGA', 'LHB', 'MIA', 'NJB', 'OKC', 'PLD', 'QME', 'RNF', 'SGO', 'THP', 'UIQ', 'VRJ', 'WTK', 'XSL', 'YMV', 'ZNU']) == False
    assert candidate(bottom = "ABCDEFG",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHA', 'BCG', 'CDG', 'DEG', 'EFG', 'FGH', 'GHA', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHB', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDA', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == False
    assert candidate(bottom = "ABCDEFG",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD', 'ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == False
    assert candidate(bottom = "ABCD",allowed = ['ABC', 'BCD', 'CDA', 'DAB', 'ABE', 'BCE', 'CEA', 'EAB', 'ACD', 'CDB', 'DBA', 'BAC', 'CAD', 'DCA', 'ACF', 'CFE', 'FEA', 'EAC', 'BDF', 'DFG', 'FGH', 'GHB', 'CDF', 'DFH', 'FHG', 'HGD', 'ACE', 'CEB', 'EBD', 'DBA', 'CFA', 'FAB', 'ABF', 'BFD', 'FDC', 'DCB']) == True
    assert candidate(bottom = "ABCD",allowed = ['ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ABC']) == False
    assert candidate(bottom = "ACF",allowed = ['ACF', 'CFA', 'FAC', 'BAC', 'BCA', 'CAB', 'ACB', 'BCC', 'CBA', 'ABC']) == True
    assert candidate(bottom = "FEDCBA",allowed = ['FEE', 'EDC', 'DBA', 'CBA', 'BAE', 'AEG']) == False
    assert candidate(bottom = "FEDCBA",allowed = ['FEG', 'EGD', 'GDC', 'DCA', 'CAB', 'ABF', 'BFB', 'BAE', 'AEC', 'ECF', 'CFD', 'DFG', 'FGH', 'GHG', 'HGH', 'GGH']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'BCG', 'CGD', 'DGE', 'EGF', 'FGH', 'GHJ', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
    assert candidate(bottom = "ABCDE",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'ABB', 'BBD', 'CCD', 'DDF', 'EFF', 'GFF', 'HFF', 'IFF', 'JFF', 'KFF', 'LFF', 'MFF', 'NFF', 'OFF', 'PFF', 'QFF', 'RFF', 'SFF', 'TFF', 'UFF', 'VFF', 'WFF', 'XFF', 'YFF', 'ZFF']) == True
    assert candidate(bottom = "FFFFF",allowed = ['FFF', 'FFG', 'FGF', 'GFF', 'GGG', 'FGG', 'GFG', 'GGF', 'FGH', 'GHF', 'GFG', 'HFG', 'FGF', 'GGG', 'FGF', 'GFG']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABB', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ']) == False
    assert candidate(bottom = "ABACD",allowed = ['ABA', 'BAC', 'ACD', 'CDE', 'DEA', 'EAB', 'ABC', 'BCD', 'CDA', 'DAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True
    assert candidate(bottom = "ABCD",allowed = ['ABE', 'BCE', 'CDE', 'DEF', 'EFG', 'FGH']) == False
    assert candidate(bottom = "XYZXYZ",allowed = ['XYZ', 'YZX', 'ZXY', 'XZY', 'ZYX', 'YXZ', 'XYX', 'YYX', 'YXY', 'YXX', 'XXX', 'XXY', 'XYY', 'XZX', 'XZX', 'XZY', 'XYX', 'XYZ', 'YZX', 'ZXY', 'YZY', 'ZYY', 'ZZY', 'ZZZ', 'YZZ', 'XZZ', 'XXZ', 'XYX', 'XYZ', 'YYX', 'YXY', 'YZY', 'YZZ']) == True
    assert candidate(bottom = "AABB",allowed = ['AAB', 'ABA', 'BAA', 'AAA', 'BBB', 'ABB', 'BBA', 'BAB']) == True
    assert candidate(bottom = "EABCD",allowed = ['EAB', 'ABF', 'BCG', 'CDF', 'DEH', 'FGI', 'GHI']) == False
    assert candidate(bottom = "ABCDE",allowed = ['ABB', 'BCC', 'CDD', 'DEE', 'EFF', 'FGG', 'GHH', 'HHI']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABE', 'BCE', 'CEF', 'DEF', 'EFD', 'FDA', 'ADB', 'BDC', 'CEB', 'DFC', 'EAD', 'FBE', 'ACB', 'BDC', 'CDB', 'DEA', 'EFD', 'FAD', 'BDA', 'CBD', 'DCB', 'EAF', 'FDB', 'AEB', 'BEC', 'CFA', 'DFB', 'EAD', 'FBA']) == True
    assert candidate(bottom = "ACDF",allowed = ['ACA', 'CDF', 'ACF', 'CDF', 'CAF', 'FAC', 'FCA', 'FCD', 'DFC', 'FDC', 'ADC', 'CAD', 'ACD', 'CDA', 'CAF', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC', 'CFA', 'CAF', 'FCA', 'FCD', 'FDC', 'CDA', 'DFC', 'FAC', 'CAD', 'ACD', 'FCA', 'FCD', 'CDA', 'FDC', 'DFC']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK']) == True
    assert candidate(bottom = "FAEBC",allowed = ['FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
    assert candidate(bottom = "ABCABC",allowed = ['ABA', 'BAC', 'ACB', 'BCA', 'CAB', 'CBA', 'AAB', 'BAA', 'ABB', 'BBA', 'AAC', 'CAA', 'ACC', 'CCA', 'BCC', 'CBB', 'BBB', 'AAA', 'CCC', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', 'MMM', 'NNN', 'OOO', 'PPP', 'QQQ', 'RRR', 'SSS', 'TTT', 'UUU', 'VVV', 'WWW', 'XXX', 'YYY', 'ZZZ']) == True
    assert candidate(bottom = "ABCFE",allowed = ['ABC', 'BCF', 'CFE', 'FED', 'EDA', 'DAB', 'ABE', 'BEC', 'ECA', 'CAD', 'CDA', 'DAB', 'ACF', 'CFB', 'BCE']) == True
    assert candidate(bottom = "FEDCBA",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFG', 'FGH', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB', 'FED', 'EDC', 'DCB', 'CBA', 'BAC', 'ACB', 'BCA', 'CAB', 'EAB', 'FCD', 'GHI', 'HJK', 'IKL', 'JKM', 'KLN', 'LMO', 'MNP', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXZ', 'XYZ', 'YZA', 'ZAB']) == True
    assert candidate(bottom = "ABAC",allowed = ['ABA', 'BAC', 'ACA', 'BAA', 'CAA', 'ACB', 'CBA', 'BAB', 'ABA', 'BAA', 'AAB', 'BBA', 'ABA', 'ABB', 'BAC', 'BAA', 'BBA', 'BBA', 'BAC', 'BAC', 'BAC', 'BAC']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABG', 'BCG', 'CDG', 'DEG', 'EFG', 'FGA', 'GAB', 'BCH', 'CDH', 'DEH', 'EFH', 'FGH', 'GHG', 'CHD', 'DHE', 'EFH', 'FGH', 'GHG', 'ACI', 'CDI', 'DEI', 'EFI', 'FGI', 'GHI', 'HIH', 'IDC', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII', 'IDE', 'DEC', 'EFD', 'FDG', 'DGE', 'EFG', 'FGH', 'GHI', 'HII']) == True
    assert candidate(bottom = "AAAAAA",allowed = ['AAA', 'AAB', 'ABA', 'ABB', 'BBA', 'BAB', 'BAA', 'BBB', 'ABA', 'AAA', 'BBA', 'BAA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA', 'BBA', 'ABB', 'AAB', 'BAB', 'BBA', 'ABB', 'BAB', 'BAA', 'BBB', 'AAA']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDC', 'DED', 'EFE', 'FGF', 'GAG', 'GBG', 'GGG', 'GHH', 'GHI', 'GJJ', 'GJG', 'HJH', 'HJI', 'HJG', 'IJJ', 'IJK', 'IJG', 'JKJ', 'JKK', 'JKG', 'KLL', 'KLK', 'KLG', 'LLL', 'LLM', 'LLG', 'MLM', 'MLN', 'MLG', 'NLO', 'NLP', 'NMG', 'OOO', 'OOP', 'ONP', 'PPP', 'PPQ', 'PMQ', 'QQQ', 'QQR', 'QSR', 'RRR', 'RSS', 'RST', 'SSS', 'SST', 'TTT', 'TTU', 'TTV', 'UUU', 'UUV', 'UVU', 'VVV', 'VVW', 'WWW']) == True
    assert candidate(bottom = "ABACAB",allowed = ['ABA', 'BAC', 'ACA', 'CAD', 'BDA', 'BAA', 'BBA', 'ABA', 'AAA', 'BBA', 'CAA', 'DAD', 'BBD']) == True
    assert candidate(bottom = "ABCDEF",allowed = ['ABA', 'BCB', 'CDE', 'DEF', 'EFG', 'FGA', 'GAB', 'BDA', 'DBA', 'ADB', 'CDB', 'DCB', 'BEC', 'ECB', 'CEB', 'DCE', 'EDC', 'DEC', 'FED', 'EFD', 'FDE', 'DFE', 'EDE', 'DED', 'EEF', 'FEF', 'EFF', 'FFF', 'FGF', 'GFF', 'FGG', 'GGF', 'GFG', 'GGG']) == False
    assert candidate(bottom = "FEDCBA",allowed = ['FED', 'EDC', 'DCB', 'CBA', 'BAF', 'AFB', 'FAB', 'ABD', 'BCE', 'CEB', 'EFA', 'FAB', 'ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FFF', 'GHI', 'HIJ', 'IJK', 'JKL', 'KLM', 'LMN', 'MNO', 'NOP', 'OPQ', 'PQR', 'QRS', 'RST', 'STU', 'TUV', 'UVW', 'VWX', 'WXY', 'XYZ']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABG', 'BCG', 'CDE', 'DEC', 'EFA', 'FGH', 'GHI']) == False
    assert candidate(bottom = "ABCDEF",allowed = ['ABC', 'BCD', 'CDE', 'DEF', 'EFA', 'FAB', 'ABD', 'BCE', 'CEF', 'DFE', 'EFD', 'FAC']) == True


