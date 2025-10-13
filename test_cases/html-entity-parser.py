# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(text = "&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not."
    assert candidate(text = "and I quote: &quot;...&quot;") == "and I quote: \"...\""
    assert candidate(text = "Stay home! Practice on Leetcode :)") == "Stay home! Practice on Leetcode :)"
    assert candidate(text = "x &gt; y &amp;&amp; x &lt; y is always False") == "x > y && x < y is always False"
    assert candidate(text = "leetcode.com&frasl;problemset&frasl;all") == "leetcode.com/problemset/all"
