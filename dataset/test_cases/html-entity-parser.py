def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(text = "&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not."
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not.": {e}')
    
    total += 1
    try:
        result = candidate(text = "and I quote: &quot;...&quot;") == "and I quote: \"...\""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "and I quote: &quot;...&quot;") == "and I quote: \"...\"": {e}')
    
    total += 1
    try:
        result = candidate(text = "Stay home! Practice on Leetcode :)") == "Stay home! Practice on Leetcode :)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "Stay home! Practice on Leetcode :)") == "Stay home! Practice on Leetcode :)": {e}')
    
    total += 1
    try:
        result = candidate(text = "x &gt; y &amp;&amp; x &lt; y is always False") == "x > y && x < y is always False"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "x &gt; y &amp;&amp; x &lt; y is always False") == "x > y && x < y is always False": {e}')
    
    total += 1
    try:
        result = candidate(text = "leetcode.com&frasl;problemset&frasl;all") == "leetcode.com/problemset/all"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(text = "leetcode.com&frasl;problemset&frasl;all") == "leetcode.com/problemset/all": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(text = "&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not."
    assert candidate(text = "and I quote: &quot;...&quot;") == "and I quote: \"...\""
    assert candidate(text = "Stay home! Practice on Leetcode :)") == "Stay home! Practice on Leetcode :)"
    assert candidate(text = "x &gt; y &amp;&amp; x &lt; y is always False") == "x > y && x < y is always False"
    assert candidate(text = "leetcode.com&frasl;problemset&frasl;all") == "leetcode.com/problemset/all"


