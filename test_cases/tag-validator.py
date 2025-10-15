def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(code = "<A>abc</A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>abc</A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[wahaha]]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[wahaha]]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "This is the first line <DIV></DIV>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "This is the first line <DIV></DIV>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[CDATA_CONTENT]]>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[CDATA_CONTENT]]>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></A></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></A></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A> <B> <C></C> </B> </A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A> <B> <C></C> </B> </A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "This is the first line <DIV> [CDATA[CDATA_CONTENT]] </DIV>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "This is the first line <DIV> [CDATA[CDATA_CONTENT]] </DIV>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = ">>  ![cdata[]] <div>]>]]>>]") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = ">>  ![cdata[]] <div>]>]]>>]") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[CDATA]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[CDATA]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "This is the first line <DIV><SPAN></SPAN></DIV>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "This is the first line <DIV><SPAN></SPAN></DIV>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A></A><B></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A></A><B></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><A><A></A></A></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><A><A></A></A></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><TAG></TAG></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><TAG></TAG></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><A>456</A>  <A> 123  <B> <C>  123 </C> <B></B> </A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><A>456</A>  <A> 123  <B> <C>  123 </C> <B></B> </A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[CDATA_CONTENT]]></DIV>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[CDATA_CONTENT]]></DIV>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "      ") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "      ") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>text <![CDATA[CDATA_CONTENT]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>text <![CDATA[CDATA_CONTENT]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[unmatched < > ]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[unmatched < > ]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>abc<![CDATA[CDATA]]>def</A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>abc<![CDATA[CDATA]]>def</A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><TAG>sometext</TAG></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><TAG>sometext</TAG></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<![CDATA[]]]]><TAG>sometext</TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<![CDATA[]]]]><TAG>sometext</TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[CDATA_CONTENT]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[CDATA_CONTENT]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A></A><A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A></A><A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><A>abc</A></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><A>abc</A></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[unmatched < > ]]><TAG></TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[unmatched < > ]]><TAG></TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[wahaha]]]><TAG>sometext</TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[wahaha]]]><TAG>sometext</TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></B></A><A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></B></A><A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[CDATA_CONTENT]]></CDATA>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[CDATA_CONTENT]]></CDATA>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<VALID><![CDATA[<INVALID></INVALID>]]></VALID>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<VALID><![CDATA[<INVALID></INVALID>]]></VALID>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C>content</C><![CDATA[content]]></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C>content</C><![CDATA[content]]></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><![CDATA[ignore <F> here]]></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><![CDATA[ignore <F> here]]></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<S><E><![CDATA[<INVALID></INVALID>]]></E></S>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<S><E><![CDATA[<INVALID></INVALID>]]></E></S>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NESTEDCDATA><CDATA><![CDATA[Nested CDATA]]></CDATA>]]></NESTEDCDATA>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NESTEDCDATA><CDATA><![CDATA[Nested CDATA]]></CDATA>]]></NESTEDCDATA>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[unmatched <]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[unmatched <]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<UNBALANCED></UNBALANCED></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<UNBALANCED></UNBALANCED></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<P><![CDATA[<P><P><P><P><P><P><P>many</P></P></P></P></P></P></P>]]></P>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<P><![CDATA[<P><P><P><P><P><P><P>many</P></P></P></P></P></P></P>]]></P>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><H><I><J><K></K></J></I></H></G></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><H><I><J><K></K></J></I></H></G></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[</I></H></G></F></E></D></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[</I></H></G></F></E></D></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B><D><![CDATA[TEXT]]></D></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B><D><![CDATA[TEXT]]></D></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<B>]]></A></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<B>]]></A></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[TEXT]]></B><![CDATA[TEXT]]></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[TEXT]]></B><![CDATA[TEXT]]></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]><B></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]><B></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<A>content</A>]]><A>content</A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<A>content</A>]]><A>content</A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[</]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[</]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NINECHARS><INNER><INNERMOST></INNERMOST></INNER></NINECHARS>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NINECHARS><INNER><INNERMOST></INNERMOST></INNER></NINECHARS>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></D>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></D>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[</A><B>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[</A><B>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG><![CDATA[<TAG>data</TAG>]]></TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG><![CDATA[<TAG>data</TAG>]]></TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<A>content</A>]]><B>content<![CDATA[<C>content</C>]]></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<A>content</A>]]><B>content<![CDATA[<C>content</C>]]></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A></A>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A></A>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A><B></B></A>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A><B></B></A>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<AA><BB><CC><DD><![CDATA[DDDD]]></DD></CC></BB></AA>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<AA><BB><CC><DD><![CDATA[DDDD]]></DD></CC></BB></AA>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<A>content</A>]]><B><![CDATA[<C>content</C>]]></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<A>content</A>]]><B><![CDATA[<C>content</C>]]></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[TEXT]]></B><B><![CDATA[TEXT]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[TEXT]]></B><B><![CDATA[TEXT]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D><E>deep</E></D>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D><E>deep</E></D>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG><INNER><CDATA><TAG>invalid</TAG></CDATA></INNER></TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG><INNER><CDATA><TAG>invalid</TAG></CDATA></INNER></TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[This is a <tag> inside CDATA]]></CDATA><TAG></TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[This is a <tag> inside CDATA]]></CDATA><TAG></TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A><B></B>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A><B></B>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG>Some text <![CDATA[<TAG>more text</TAG>]]> even more text</TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG>Some text <![CDATA[<TAG>more text</TAG>]]> even more text</TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></D>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></D>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[ignore <A><B><C> here]]></A></B></C>]]>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[ignore <A><B><C> here]]></A></B></C>]]>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[CDATA]]></I></H></G></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[CDATA]]></I></H></G></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[wahaha]]></B></C></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[wahaha]]></B></C></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[ignore <D></D> here]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[ignore <D></D> here]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[CDATA]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[CDATA]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<CODE><CODE><![CDATA[CODE]]></CODE></CODE>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<CODE><CODE><![CDATA[CODE]]></CODE></CODE>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<T><![CDATA[This is a ]]><![CDATA[CDATA section]]></T>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<T><![CDATA[This is a ]]><![CDATA[CDATA section]]></T>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>content<![CDATA[<>]]>content</A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>content<![CDATA[<>]]>content</A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<LONGTAG><SHORT><LONGER></LONGER></SHORT></LONGTAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<LONGTAG><SHORT><LONGER></LONGER></SHORT></LONGTAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X><Y><Z><![CDATA[X]]></Z></Y></X>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X><Y><Z><![CDATA[X]]></Z></Y></X>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D></D>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D></D>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>content<![CDATA[<B>content</B>]]>content</A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>content<![CDATA[<B>content</B>]]>content</A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B></B>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B></B>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<WRONG><TAG></WRONG></TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<WRONG><TAG></WRONG></TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG><![CDATA[<TAG>content</TAG>]]></TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG><![CDATA[<TAG>content</TAG>]]></TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D><E>INNER</E></D>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D><E>INNER</E></D>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><![CDATA[<E>]]></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><![CDATA[<E>]]></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><![CDATA[FGHIJKL]]></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><![CDATA[FGHIJKL]]></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<MULTIPLECDATA><![CDATA[First CDATA]]></MULTIPLECDATA><![CDATA[Second CDATA]]></MULTIPLECDATA>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<MULTIPLECDATA><![CDATA[First CDATA]]></MULTIPLECDATA><![CDATA[Second CDATA]]></MULTIPLECDATA>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[wahaha]]></B></A><C></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[wahaha]]></B></A><C></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NEST><INNER1><INNER2></INNER2></INNER1></NEST>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NEST><INNER1><INNER2></INNER2></INNER1></NEST>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<XYZ><XYZ><![CDATA[XYZ]]></XYZ></XYZ>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<XYZ><XYZ><![CDATA[XYZ]]></XYZ></XYZ>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<OUTER><INNER><![CDATA[<OUTER><INNER>]]></INNER></OUTER>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<OUTER><INNER><![CDATA[<OUTER><INNER>]]></INNER></OUTER>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[wahaha>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[wahaha>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<NOTATAG><INSIDECDATA>]]></NOTATAG>]<A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<NOTATAG><INSIDECDATA>]]></NOTATAG>]<A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></B></A><![CDATA[abc<def>ghi]]>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></B></A><![CDATA[abc<def>ghi]]>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X><![CDATA[<Y><Z></Z></Y>]]></X>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X><![CDATA[<Y><Z></Z></Y>]]></X>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G><H><![CDATA[CDATA]]></H><I><![CDATA[CDATA]]></I>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G><H><![CDATA[CDATA]]></H><I><![CDATA[CDATA]]></I>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X1><X2><X3></X3><X4><X5><X6></X6></X5></X4></X2></X1>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X1><X2><X3></X3><X4><X5><X6></X6></X5></X4></X2></X1>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D>></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D>></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<INVALID><INNER></INNER></OUTER>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<INVALID><INNER></INNER></OUTER>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[abc<def>ghi]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[abc<def>ghi]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<SINGLE><CDATA></CDATA></SINGLE><![CDATA[<![CDATA[<SINGLE>]]></SINGLE>]]>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<SINGLE><CDATA></CDATA></SINGLE><![CDATA[<![CDATA[<SINGLE>]]></SINGLE>]]>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B></B><C></C><D></D><E></E></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B></B><C></C><D></D><E></E></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NESTED><INSIDE><MOREINSIDE>content</MOREINSIDE></INSIDE></NESTED>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NESTED><INSIDE><MOREINSIDE>content</MOREINSIDE></INSIDE></NESTED>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<Z><Z></Z></Z><Z><Z></Z></Z>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<Z><Z></Z></Z><Z><Z></Z></Z>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<UNBALANCED>data</C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<UNBALANCED>data</C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[wahaha>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[wahaha>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X><Y><Z></Z></Y></X> <![CDATA[DATA]]></X>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X><Y><Z></Z></Y></X> <![CDATA[DATA]]></X>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B>![CDATA[wahaha]]]>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B>![CDATA[wahaha]]]>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG1><TAG2><![CDATA[valid CDATA]]></TAG2><TAG3>content</TAG3></TAG1>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG1><TAG2><![CDATA[valid CDATA]]></TAG2><TAG3>content</TAG3></TAG1>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><![CDATA[wahaha]]]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><![CDATA[wahaha]]]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F>></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F>></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E>CDATA</E></D></C></B>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E>CDATA</E></D></C></B>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A><B></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A><B></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<UNBALANCED></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<UNBALANCED></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[ignore <D> here]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[ignore <D> here]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<A><B><C></C></B></A>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<A><B><C></C></B></A>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG>some <TAG> nested <TAG></TAG> tags</TAG></TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG>some <TAG> nested <TAG></TAG> tags</TAG></TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B>content</B>]]></A><B>content</B><![CDATA[content]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B>content</B>]]></A><B>content</B><![CDATA[content]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<MAIN><SUB1><SUB2>data</SUB2></SUB1></MAIN>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<MAIN><SUB1><SUB2>data</SUB2></SUB1></MAIN>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><![CDATA[<C>content</C>]]></B>]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><![CDATA[<C>content</C>]]></B>]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C>></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C>></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<VALID><INNER> <![CDATA[<INNER>CDATA_CONTENT</INNER>]]> </INNER></VALID>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<VALID><INNER> <![CDATA[<INNER>CDATA_CONTENT</INNER>]]> </INNER></VALID>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NESTED><INNER>CONTENT</INNER></NESTED>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NESTED><INNER>CONTENT</INNER></NESTED>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<PARENT><CHILD><GRANDCHILD></GRANDCHILD></CHILD></PARENT><![CDATA[<PARENT><CHILD></CHILD></PARENT>]]></PARENT>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<PARENT><CHILD><GRANDCHILD></GRANDCHILD></CHILD></PARENT><![CDATA[<PARENT><CHILD></CHILD></PARENT>]]></PARENT>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<ROOT><CHILD><![CDATA[<DIV>unparsed</DIV>]]></CHILD></ROOT>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<ROOT><CHILD><![CDATA[<DIV>unparsed</DIV>]]></CHILD></ROOT>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D></E>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D></E>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A></B>]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A></B>]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X><Y><![CDATA[<Z>]]></X></Y></Z>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X><Y><![CDATA[<Z>]]></X></Y></Z>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C></B></A><![CDATA[<D>]]></D>]><A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C></B></A><![CDATA[<D>]]></D>]><A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C></B><![CDATA[TEXT]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C></B><![CDATA[TEXT]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<VALID><INNER>TEXT<![CDATA[CDATA_CONTENT]]></INNER></VALID>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<VALID><INNER>TEXT<![CDATA[CDATA_CONTENT]]></INNER></VALID>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><D><![CDATA[CDATA]]></D></C><E><F><![CDATA[CDATA]]></F></E><G><H><![CDATA[CDATA]]></H></G><I><J><![CDATA[CDATA]]></J></I>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><D><![CDATA[CDATA]]></D></C><E><F><![CDATA[CDATA]]></F></E><G><H><![CDATA[CDATA]]></H></G><I><J><![CDATA[CDATA]]></J></I>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></D></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></D></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<MAIN><SUB1><SUB2></SUB2></SUB1></MAIN>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<MAIN><SUB1><SUB2></SUB2></SUB1></MAIN>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[content]]></A><B>content</B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[content]]></A><B>content</B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[TEXT]]></A><![CDATA[TEXT]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[TEXT]]></A><![CDATA[TEXT]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<ROOT><CHILD1><GRANDCHILD></GRANDCHILD></CHILD1><CHILD2></CHILD2></ROOT>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<ROOT><CHILD1><GRANDCHILD></GRANDCHILD></CHILD1><CHILD2></CHILD2></ROOT>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<C></D>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<C></D>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<ROOT><![CDATA[<A></A>]]></ROOT>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<ROOT><![CDATA[<A></A>]]></ROOT>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<C><D></C>]]></D></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<C><D></C>]]></D></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[content]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[content]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[ignore <TAG> and </TAG> here]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[ignore <TAG> and </TAG> here]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<P><A><![CDATA[<BR>]]></A><SPAN>text</SPAN></P>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<P><A><![CDATA[<BR>]]></A><SPAN>text</SPAN></P>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<OUTER><MID><![CDATA[<INNER></INNER>]]></MID></OUTER>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<OUTER><MID><![CDATA[<INNER></INNER>]]></MID></OUTER>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG1><TAG2><TAG3>CONTENT</TAG3></TAG2></TAG1>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG1><TAG2><TAG3>CONTENT</TAG3></TAG2></TAG1>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D><E>CDATA</E></D>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D><E>CDATA</E></D>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[unmatched </]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[unmatched </]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha>]]></G></F></E></D></C></B>]]></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha>]]></G></F></E></D></C></B>]]></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<T><T><![CDATA[<T><T>INNER</T></T>]]></T></T>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<T><T><![CDATA[<T><T>INNER</T></T>]]></T></T>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG><![CDATA[<TAG><![CDATA[CDATA_CONTENT]]></TAG>]]></TAG>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG><![CDATA[<TAG><![CDATA[CDATA_CONTENT]]></TAG>]]></TAG>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<HELLO><WORLD><![CDATA[<HELLO>world</WORLD>]]></HELLO>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<HELLO><WORLD><![CDATA[<HELLO>world</WORLD>]]></HELLO>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[not <CLOSING]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[not <CLOSING]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E>></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E>></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[TEXT]]></C><D><![CDATA[TEXT]]></D></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[TEXT]]></C><D><![CDATA[TEXT]]></D></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[</]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[</]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CONTENT]]></E></D>]]></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CONTENT]]></E></D>]]></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G></G></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G></G></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[CDATA]]></A><B><![CDATA[CDATA]]></B><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[CDATA]]></A><B><![CDATA[CDATA]]></B><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A>]]><C></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A>]]><C></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><![CDATA[<E><F></F>]]></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><![CDATA[<E><F></F>]]></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C></B><D><![CDATA[TEXT]]></D></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C></B><D><![CDATA[TEXT]]></D></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NEST><INNER><![CDATA[<NEST><INNER><![CDATA[CDATA_CONTENT]]></INNER></NEST>]]></INNER></NEST>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NEST><INNER><![CDATA[<NEST><INNER><![CDATA[CDATA_CONTENT]]></INNER></NEST>]]></INNER></NEST>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<CORRECT><INSIDE></INSIDE></CORRECT>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<CORRECT><INSIDE></INSIDE></CORRECT>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><H><I><J><K><L><M><N><O><P><Q><R><S><T><U><V><W><X><Y><Z></Z></Y></X></W></V></U></T></S></R></Q></P></O></N></M></L></K></J></I></H></G></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><H><I><J><K><L><M><N><O><P><Q><R><S><T><U><V><W><X><Y><Z></Z></Y></X></W></V></U></T></S></R></Q></P></O></N></M></L></K></J></I></H></G></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CDATA_CONTENT]]></E></D>]]></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CDATA_CONTENT]]></E></D>]]></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></F></E></D></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></F></E></D></C></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<NOTATAG>data</NOTATAG>]]><VALID></VALID>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<NOTATAG>data</NOTATAG>]]><VALID></VALID>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<LAYER1><LAYER2><LAYER3></LAYER3></LAYER2></LAYER1>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<LAYER1><LAYER2><LAYER3></LAYER3></LAYER2></LAYER1>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<TAG><INNER><![CDATA[<INNER>CDATA_CONTENT</INNER>]]> <![CDATA[TEXT]]></INNER></TAG>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<TAG><INNER><![CDATA[<INNER>CDATA_CONTENT</INNER>]]> <![CDATA[TEXT]]></INNER></TAG>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C><![CDATA[TEXT]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C><![CDATA[TEXT]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[<Z><Z></Z></Z><Z><Z></Z></Z>]]></Z>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[<Z><Z></Z></Z><Z><Z></Z></Z>]]></Z>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C><D>content</D>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C><D>content</D>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<OUTER><MID><INNER>TEXT</INNER> <![CDATA[TEXT]]></MID></OUTER>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<OUTER><MID><INNER>TEXT</INNER> <![CDATA[TEXT]]></MID></OUTER>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><![CDATA[ABCDE]]></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><![CDATA[ABCDE]]></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[&]][CDATA[]]><B></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[&]][CDATA[]]><B></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[content]]></A><![CDATA[morecontent]]>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[content]]></A><![CDATA[morecontent]]>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<NEST><LVL1><LVL2><LVL3><![CDATA[<NEST><LVL1>deep</LVL1></NEST>]]></LVL3></LVL2></LVL1></NEST>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<NEST><LVL1><LVL2><LVL3><![CDATA[<NEST><LVL1>deep</LVL1></NEST>]]></LVL3></LVL2></LVL1></NEST>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B>content</B><![CDATA[content]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B>content</B><![CDATA[content]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><![CDATA[ignore <F></F> here]]></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><![CDATA[ignore <F></F> here]]></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[<A><B><C>]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[<A><B><C>]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<!CDATA[CDATA_CONTENT]]]]><B></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<!CDATA[CDATA_CONTENT]]]]><B></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[This is a <C></C> test]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[This is a <C></C> test]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<C></C>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<C></C>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<OUTER><INNER><![CDATA[<INNER>CDATA</INNER>]]></INNER></OUTER>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<OUTER><INNER><![CDATA[<INNER>CDATA</INNER>]]></INNER></OUTER>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[ignore <TAG> tags <INSIDE> </INSIDE> </TAG> ]]>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[ignore <TAG> tags <INSIDE> </INSIDE> </TAG> ]]>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C><D><![CDATA[TEXT]]></D></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C><D><![CDATA[TEXT]]></D></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C><D></D></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C><D></D></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]><A></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]><A></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<C><D></D></C>]]></B><C><D><![CDATA[<E><F></F></E>]]></D></C></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<C><D></D></C>]]></B><C><D><![CDATA[<E><F></F></E>]]></D></C></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<ALMOST><INNER><![CDATA[</INNER>]]></ALMOST>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<ALMOST><INNER><![CDATA[</INNER>]]></ALMOST>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[unmatched ]]></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[unmatched ]]></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><![CDATA[wahaha>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><![CDATA[wahaha>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<X><Y><![CDATA[Not a tag>]]></Y></X>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<X><Y><![CDATA[Not a tag>]]></Y></X>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[This is some text <B></B> with CDATA]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[This is some text <B></B> with CDATA]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C></C></B></A><D></D>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C></C></B></A><D></D>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<A></A>]]></B></A><C><D><![CDATA[<E></E>]]></D></C>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<A></A>]]></B></A><C><D><![CDATA[<E></E>]]></D></C>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B><![CDATA[content]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B><![CDATA[content]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></B>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></B>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><![CDATA[wahaha]]></C></D></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><![CDATA[wahaha]]></C></D></B></A>") == False: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><![CDATA[<B></C>]]></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><![CDATA[<B></C>]]></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G>></F></E></D></C></B></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G>></F></E></D></C></B></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A>content<![CDATA[<B>content</B>]]></A>") == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A>content<![CDATA[<B>content</B>]]></A>") == True: {e}')
    
    total += 1
    try:
        result = candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha>]]></F></E></D></C></B></A>") == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha>]]></F></E></D></C></B></A>") == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(code = "<A>abc</A>") == True
    assert candidate(code = "<A><![CDATA[wahaha]]]></A>") == True
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A>") == True
    assert candidate(code = "<A><B></C></B></A>") == False
    assert candidate(code = "This is the first line <DIV></DIV>") == False
    assert candidate(code = "<![CDATA[CDATA_CONTENT]]>") == True
    assert candidate(code = "<A><B></A></B>") == False
    assert candidate(code = "<A> <B> <C></C> </B> </A>") == True
    assert candidate(code = "This is the first line <DIV> [CDATA[CDATA_CONTENT]] </DIV>") == False
    assert candidate(code = ">>  ![cdata[]] <div>]>]]>>]") == False
    assert candidate(code = "<A><![CDATA[CDATA]]></A>") == True
    assert candidate(code = "This is the first line <DIV><SPAN></SPAN></DIV>") == False
    assert candidate(code = "<A></A><B></B>") == False
    assert candidate(code = "<A><A><A></A></A></A>") == True
    assert candidate(code = "<A><TAG></TAG></A>") == True
    assert candidate(code = "<A><A>456</A>  <A> 123  <B> <C>  123 </C> <B></B> </A></A>") == False
    assert candidate(code = "<![CDATA[CDATA_CONTENT]]></DIV>") == False
    assert candidate(code = "      ") == False
    assert candidate(code = "<A>text <![CDATA[CDATA_CONTENT]]></A>") == True
    assert candidate(code = "<A><![CDATA[unmatched < > ]]></A>") == True
    assert candidate(code = "<A>abc<![CDATA[CDATA]]>def</A>") == True
    assert candidate(code = "<A><TAG>sometext</TAG></A>") == True
    assert candidate(code = "<A></B>") == False
    assert candidate(code = "<![CDATA[<![CDATA[]]]]><TAG>sometext</TAG>") == False
    assert candidate(code = "<A><![CDATA[CDATA_CONTENT]]></A>") == True
    assert candidate(code = "<A><B><C></C></B></A>") == True
    assert candidate(code = "<A></A><A></A>") == False
    assert candidate(code = "<A><A>abc</A></A>") == True
    assert candidate(code = "<![CDATA[unmatched < > ]]><TAG></TAG>") == False
    assert candidate(code = "<![CDATA[wahaha]]]><TAG>sometext</TAG>") == False
    assert candidate(code = "<A><B></B></A><A></A>") == False
    assert candidate(code = "<A></A>") == True
    assert candidate(code = "<A><B></B></A>") == True
    assert candidate(code = "<![CDATA[CDATA_CONTENT]]></CDATA>") == False
    assert candidate(code = "<VALID><![CDATA[<INVALID></INVALID>]]></VALID>") == True
    assert candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C>content</C><![CDATA[content]]></C>") == False
    assert candidate(code = "<A><B><C><D><E><![CDATA[ignore <F> here]]></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><D></D></C></B></A>") == True
    assert candidate(code = "<S><E><![CDATA[<INVALID></INVALID>]]></E></S>") == True
    assert candidate(code = "<NESTEDCDATA><CDATA><![CDATA[Nested CDATA]]></CDATA>]]></NESTEDCDATA>") == False
    assert candidate(code = "<A><B><C><![CDATA[unmatched <]]></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<UNBALANCED></UNBALANCED></C></B></A>") == False
    assert candidate(code = "<P><![CDATA[<P><P><P><P><P><P><P>many</P></P></P></P></P></P></P>]]></P>") == True
    assert candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]]></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><H><I><J><K></K></J></I></H></G></F></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[</I></H></G></F></E></D></C></B></A>") == False
    assert candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B><D><![CDATA[TEXT]]></D></A>") == True
    assert candidate(code = "<A><B><![CDATA[<B>]]></A></B>") == False
    assert candidate(code = "<A><B><![CDATA[TEXT]]></B><![CDATA[TEXT]]></B></A>") == False
    assert candidate(code = "<A><B><C><![CDATA[<]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]><B></B></A>") == True
    assert candidate(code = "<![CDATA[<A>content</A>]]><A>content</A>") == False
    assert candidate(code = "<A><![CDATA[</]]></A>") == True
    assert candidate(code = "<NINECHARS><INNER><INNERMOST></INNERMOST></INNER></NINECHARS>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></D>") == False
    assert candidate(code = "<A><B><![CDATA[</A><B>]]></B></A>") == True
    assert candidate(code = "<TAG><![CDATA[<TAG>data</TAG>]]></TAG>") == True
    assert candidate(code = "<![CDATA[<A>content</A>]]><B>content<![CDATA[<C>content</C>]]></B>") == False
    assert candidate(code = "<A><B><![CDATA[<A></A>]]></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<A><B></B></A>]]></B></A>") == True
    assert candidate(code = "<AA><BB><CC><DD><![CDATA[DDDD]]></DD></CC></BB></AA>") == True
    assert candidate(code = "<![CDATA[<A>content</A>]]><B><![CDATA[<C>content</C>]]></B>") == False
    assert candidate(code = "<A><B><![CDATA[TEXT]]></B><B><![CDATA[TEXT]]></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D><E>deep</E></D>]]></C></B></A>") == True
    assert candidate(code = "<TAG><INNER><CDATA><TAG>invalid</TAG></CDATA></INNER></TAG>") == True
    assert candidate(code = "<![CDATA[This is a <tag> inside CDATA]]></CDATA><TAG></TAG>") == False
    assert candidate(code = "<A><B><![CDATA[<A><B></B>]]></B></A>") == True
    assert candidate(code = "<TAG>Some text <![CDATA[<TAG>more text</TAG>]]> even more text</TAG>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></C>") == False
    assert candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></D>") == False
    assert candidate(code = "<![CDATA[ignore <A><B><C> here]]></A></B></C>]]>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><H><I><![CDATA[CDATA]]></I></H></G></F></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[wahaha]]></B></C></A>") == False
    assert candidate(code = "<A><B><C><![CDATA[ignore <D></D> here]]></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[CDATA]]></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<A>]]></B></A>") == True
    assert candidate(code = "<CODE><CODE><![CDATA[CODE]]></CODE></CODE>") == True
    assert candidate(code = "<T><![CDATA[This is a ]]><![CDATA[CDATA section]]></T>") == True
    assert candidate(code = "<A>content<![CDATA[<>]]>content</A>") == True
    assert candidate(code = "<LONGTAG><SHORT><LONGER></LONGER></SHORT></LONGTAG>") == True
    assert candidate(code = "<X><Y><Z><![CDATA[X]]></Z></Y></X>") == True
    assert candidate(code = "<A><B><C><![CDATA[TEXT]]></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D></D>]]></C></B></A>") == True
    assert candidate(code = "<A>content<![CDATA[<B>content</B>]]>content</A>") == True
    assert candidate(code = "<A><![CDATA[<B></B>]]></A>") == True
    assert candidate(code = "<WRONG><TAG></WRONG></TAG>") == False
    assert candidate(code = "<TAG><![CDATA[<TAG>content</TAG>]]></TAG>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D><E>INNER</E></D>]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>]]></A>") == False
    assert candidate(code = "<A><B><C><D><![CDATA[<E>]]></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><![CDATA[FGHIJKL]]></F></E></D></C></B></A>") == True
    assert candidate(code = "<MULTIPLECDATA><![CDATA[First CDATA]]></MULTIPLECDATA><![CDATA[Second CDATA]]></MULTIPLECDATA>") == False
    assert candidate(code = "<A><B><![CDATA[wahaha]]></B></A><C></C>") == False
    assert candidate(code = "<NEST><INNER1><INNER2></INNER2></INNER1></NEST>") == False
    assert candidate(code = "<XYZ><XYZ><![CDATA[XYZ]]></XYZ></XYZ>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B]]></A>") == False
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B>]]></A>") == True
    assert candidate(code = "<OUTER><INNER><![CDATA[<OUTER><INNER>]]></INNER></OUTER>") == True
    assert candidate(code = "<A><B><![CDATA[wahaha>]]></B></A>") == True
    assert candidate(code = "<![CDATA[<NOTATAG><INSIDECDATA>]]></NOTATAG>]<A></A>") == False
    assert candidate(code = "<A><![CDATA[>]]></A>") == True
    assert candidate(code = "<A><B></B></A><![CDATA[abc<def>ghi]]>") == False
    assert candidate(code = "<X><![CDATA[<Y><Z></Z></Y>]]></X>") == True
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G><H><![CDATA[CDATA]]></H><I><![CDATA[CDATA]]></I>") == False
    assert candidate(code = "<A>content<![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False
    assert candidate(code = "<X1><X2><X3></X3><X4><X5><X6></X6></X5></X4></X2></X1>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D>></C></B></A>") == True
    assert candidate(code = "<INVALID><INNER></INNER></OUTER>") == False
    assert candidate(code = "<A><![CDATA[abc<def>ghi]]></A>") == True
    assert candidate(code = "<SINGLE><CDATA></CDATA></SINGLE><![CDATA[<![CDATA[<SINGLE>]]></SINGLE>]]>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></A>") == False
    assert candidate(code = "<A><B><![CDATA[abc]]></B><![CDATA[def]></A>") == False
    assert candidate(code = "<A><B></B><C></C><D></D><E></E></A>") == True
    assert candidate(code = "<NESTED><INSIDE><MOREINSIDE>content</MOREINSIDE></INSIDE></NESTED>") == False
    assert candidate(code = "<Z><Z></Z></Z><Z><Z></Z></Z>") == False
    assert candidate(code = "<A><B><C><![CDATA[<UNBALANCED>data</C></B></A>") == False
    assert candidate(code = "<A><B><C><![CDATA[wahaha>]]></C></B></A>") == True
    assert candidate(code = "<X><Y><Z></Z></Y></X> <![CDATA[DATA]]></X>") == False
    assert candidate(code = "<A><![CDATA[<B>![CDATA[wahaha]]]>]]></A>") == True
    assert candidate(code = "<TAG1><TAG2><![CDATA[valid CDATA]]></TAG2><TAG3>content</TAG3></TAG1>") == False
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F>") == False
    assert candidate(code = "<A><![CDATA[<B><![CDATA[wahaha]]]]></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F>></E></D></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E>CDATA</E></D></C></B>]]></A>") == True
    assert candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A><B></B>") == False
    assert candidate(code = "<A><B><C><![CDATA[<UNBALANCED></C></B></A>") == False
    assert candidate(code = "<A><B><C><![CDATA[ignore <D> here]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[ignore <B><C></C></B> here]]></A>") == True
    assert candidate(code = "<A><![CDATA[<A><B><C></C></B></A>]]></A>") == True
    assert candidate(code = "<TAG>some <TAG> nested <TAG></TAG> tags</TAG></TAG>") == True
    assert candidate(code = "<A><![CDATA[<B>content</B>]]></A><B>content</B><![CDATA[content]]></A>") == False
    assert candidate(code = "<MAIN><SUB1><SUB2>data</SUB2></SUB1></MAIN>") == False
    assert candidate(code = "<A><![CDATA[<B><![CDATA[<C>content</C>]]></B>]]></A>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C>></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B>></A>") == False
    assert candidate(code = "<VALID><INNER> <![CDATA[<INNER>CDATA_CONTENT</INNER>]]> </INNER></VALID>") == True
    assert candidate(code = "<NESTED><INNER>CONTENT</INNER></NESTED>") == True
    assert candidate(code = "<PARENT><CHILD><GRANDCHILD></GRANDCHILD></CHILD></PARENT><![CDATA[<PARENT><CHILD></CHILD></PARENT>]]></PARENT>") == False
    assert candidate(code = "<ROOT><CHILD><![CDATA[<DIV>unparsed</DIV>]]></CHILD></ROOT>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D></E>]]></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<A></B>]]></A>") == False
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></A>") == False
    assert candidate(code = "<X><Y><![CDATA[<Z>]]></X></Y></Z>") == False
    assert candidate(code = "<A><B><C></C></B></A><![CDATA[<D>]]></D>]><A>") == False
    assert candidate(code = "<A><B><C></C></B><![CDATA[TEXT]]></A>") == True
    assert candidate(code = "<VALID><INNER>TEXT<![CDATA[CDATA_CONTENT]]></INNER></VALID>") == True
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><D><![CDATA[CDATA]]></D></C><E><F><![CDATA[CDATA]]></F></E><G><H><![CDATA[CDATA]]></H></G><I><J><![CDATA[CDATA]]></J></I>") == False
    assert candidate(code = "<A><B><C></D></C></B></A>") == False
    assert candidate(code = "<A><![CDATA[<]]></A>") == True
    assert candidate(code = "<MAIN><SUB1><SUB2></SUB2></SUB1></MAIN>") == False
    assert candidate(code = "<A><![CDATA[content]]></A><B>content</B>") == False
    assert candidate(code = "<A><![CDATA[TEXT]]></A><![CDATA[TEXT]]></A>") == False
    assert candidate(code = "<ROOT><CHILD1><GRANDCHILD></GRANDCHILD></CHILD1><CHILD2></CHILD2></ROOT>") == False
    assert candidate(code = "<A><B><![CDATA[<C></D>]]></B></A>") == True
    assert candidate(code = "<ROOT><![CDATA[<A></A>]]></ROOT>") == True
    assert candidate(code = "<A><B><C><![CDATA[wahaha]]></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<C><D></C>]]></D></B></A>") == False
    assert candidate(code = "<A><![CDATA[content]]></A>") == True
    assert candidate(code = "<A><B><![CDATA[ignore <TAG> and </TAG> here]]></B></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A></B>") == False
    assert candidate(code = "<P><A><![CDATA[<BR>]]></A><SPAN>text</SPAN></P>") == True
    assert candidate(code = "<A><B><C><D><E></E></D></C></B></A>") == True
    assert candidate(code = "<OUTER><MID><![CDATA[<INNER></INNER>]]></MID></OUTER>") == True
    assert candidate(code = "<TAG1><TAG2><TAG3>CONTENT</TAG3></TAG2></TAG1>") == False
    assert candidate(code = "<A><B><C><![CDATA[<D><E>CDATA</E></D>]]></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D>") == False
    assert candidate(code = "<A><B><C><![CDATA[unmatched </]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha>]]></G></F></E></D></C></B>]]></A>") == False
    assert candidate(code = "<A><B><![CDATA[CDATA]]></B></A><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E>") == False
    assert candidate(code = "<T><T><![CDATA[<T><T>INNER</T></T>]]></T></T>") == True
    assert candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]>") == True
    assert candidate(code = "<TAG><![CDATA[<TAG><![CDATA[CDATA_CONTENT]]></TAG>]]></TAG>") == False
    assert candidate(code = "<HELLO><WORLD><![CDATA[<HELLO>world</WORLD>]]></HELLO>") == False
    assert candidate(code = "<A><B><![CDATA[not <CLOSING]]></B></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E>></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[TEXT]]></C><D><![CDATA[TEXT]]></D></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[</]]></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CONTENT]]></E></D>]]></C></B></A>") == False
    assert candidate(code = "<A><B><C><D><E><F><G></G></F></E></D></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[CDATA]]></A><B><![CDATA[CDATA]]></B><C><![CDATA[CDATA]]></C><D><![CDATA[CDATA]]></D><E><![CDATA[CDATA]]></E><F><![CDATA[CDATA]]></F><G><![CDATA[CDATA]]></G>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><H><I></I></H></G></F></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<A>]]><C></C></B></A>") == True
    assert candidate(code = "<A><B><C><D><![CDATA[<E><F></F>]]></D></C></B></A>") == True
    assert candidate(code = "<A><B><C></C></B><D><![CDATA[TEXT]]></D></A>") == True
    assert candidate(code = "<NEST><INNER><![CDATA[<NEST><INNER><![CDATA[CDATA_CONTENT]]></INNER></NEST>]]></INNER></NEST>") == False
    assert candidate(code = "<A><B><C><![CDATA[>]]></C></B></A>") == True
    assert candidate(code = "<CORRECT><INSIDE></INSIDE></CORRECT>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><H><I><J><K><L><M><N><O><P><Q><R><S><T><U><V><W><X><Y><Z></Z></Y></X></W></V></U></T></S></R></Q></P></O></N></M></L></K></J></I></H></G></F></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<D><E><![CDATA[CDATA_CONTENT]]></E></D>]]></C></B></A>") == False
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></F></E></D></C></B></A>") == False
    assert candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B></A>") == True
    assert candidate(code = "<![CDATA[<NOTATAG>data</NOTATAG>]]><VALID></VALID>") == False
    assert candidate(code = "<LAYER1><LAYER2><LAYER3></LAYER3></LAYER2></LAYER1>") == False
    assert candidate(code = "<TAG><INNER><![CDATA[<INNER>CDATA_CONTENT</INNER>]]> <![CDATA[TEXT]]></INNER></TAG>") == True
    assert candidate(code = "<A><B><C></C><![CDATA[TEXT]]></B></A>") == True
    assert candidate(code = "<![CDATA[<Z><Z></Z></Z><Z><Z></Z></Z>]]></Z>") == False
    assert candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C><D>content</D>") == False
    assert candidate(code = "<OUTER><MID><INNER>TEXT</INNER> <![CDATA[TEXT]]></MID></OUTER>") == True
    assert candidate(code = "<A><B><C><D><E><![CDATA[ABCDE]]></E></D></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[&]][CDATA[]]><B></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B>content</B>]]></A><C><![CDATA[content]]></C>") == False
    assert candidate(code = "<A><![CDATA[content]]></A><![CDATA[morecontent]]>") == False
    assert candidate(code = "<NEST><LVL1><LVL2><LVL3><![CDATA[<NEST><LVL1>deep</LVL1></NEST>]]></LVL3></LVL2></LVL1></NEST>") == False
    assert candidate(code = "<A><B>content</B><![CDATA[content]]></A>") == True
    assert candidate(code = "<A><B><C><D><E><![CDATA[ignore <F></F> here]]></E></D></C></B></A>") == True
    assert candidate(code = "<A><B><C><![CDATA[<A><B><C>]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[<!CDATA[CDATA_CONTENT]]]]><B></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[This is a <C></C> test]]></B></A>") == True
    assert candidate(code = "<A><B><![CDATA[<C></C>]]></B></A>") == True
    assert candidate(code = "<OUTER><INNER><![CDATA[<INNER>CDATA</INNER>]]></INNER></OUTER>") == True
    assert candidate(code = "<![CDATA[ignore <TAG> tags <INSIDE> </INSIDE> </TAG> ]]>") == True
    assert candidate(code = "<A><B><C></C><D><![CDATA[TEXT]]></D></B></A>") == True
    assert candidate(code = "<A><B><C></C><D></D></B></A>") == True
    assert candidate(code = "<![CDATA[ignore <A><B><C></C></B></A> here]]><A></A>") == False
    assert candidate(code = "<A><B><![CDATA[<C><D></D></C>]]></B><C><D><![CDATA[<E><F></F></E>]]></D></C></A>") == True
    assert candidate(code = "<ALMOST><INNER><![CDATA[</INNER>]]></ALMOST>") == False
    assert candidate(code = "<A><B><C><![CDATA[unmatched ]]></C></B></A>") == True
    assert candidate(code = "<A><![CDATA[<B><![CDATA[wahaha>]]></A>") == True
    assert candidate(code = "<X><Y><![CDATA[Not a tag>]]></Y></X>") == True
    assert candidate(code = "<A><![CDATA[This is some text <B></B> with CDATA]]></A>") == True
    assert candidate(code = "<A><B><C></C></B></A><D></D>") == False
    assert candidate(code = "<A><B><![CDATA[<A></A>]]></B></A><C><D><![CDATA[<E></E>]]></D></C>") == False
    assert candidate(code = "<A><B>content<![CDATA[<C>content</C>]]></B><![CDATA[content]]></A>") == True
    assert candidate(code = "<A><![CDATA[<B>]]></A>") == True
    assert candidate(code = "<A><![CDATA[<B><C><D><E><F><G><![CDATA[wahaha]]></G></F></E></D></C></B></A>></B>") == False
    assert candidate(code = "<A><B><C><![CDATA[wahaha]]></C></D></B></A>") == False
    assert candidate(code = "<A><B><![CDATA[<B></C>]]></B></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha]]></G>></F></E></D></C></B></A>") == True
    assert candidate(code = "<A>content<![CDATA[<B>content</B>]]></A>") == True
    assert candidate(code = "<A><B><C><D><E><F><G><![CDATA[wahaha>]]></F></E></D></C></B></A>") == False


