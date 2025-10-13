# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(wordsDict = ['hello', 'world', 'this', 'is', 'a', 'test', 'hello'],word1 = "hello",word2 = "test") == 1
    assert candidate(wordsDict = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],word1 = "quick",word2 = "lazy") == 6
    assert candidate(wordsDict = ['hello', 'world', 'this', 'is', 'a', 'test', 'hello', 'world'],word1 = "hello",word2 = "world") == 1
    assert candidate(wordsDict = ['practice', 'makes', 'perfect', 'coding', 'makes'],word1 = "coding",word2 = "practice") == 3
    assert candidate(wordsDict = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],word1 = "the",word2 = "fox") == 3
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'a', 'b'],word1 = "a",word2 = "b") == 1
    assert candidate(wordsDict = ['hello', 'world', 'hello', 'world', 'hello'],word1 = "hello",word2 = "world") == 1
    assert candidate(wordsDict = ['practice', 'makes', 'perfect', 'coding', 'makes'],word1 = "makes",word2 = "coding") == 1
    assert candidate(wordsDict = ['hello', 'world', 'this', 'is', 'a', 'test', 'hello'],word1 = "hello",word2 = "world") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],word1 = "three",word2 = "seven") == 4
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],word1 = "a",word2 = "z") == 25
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a'],word1 = "a",word2 = "j") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'x', 'y', 'z', 'x'],word1 = "x",word2 = "z") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],word1 = "two",word2 = "nine") == 7
    assert candidate(wordsDict = ['hello', 'world', 'foo', 'bar', 'hello'],word1 = "hello",word2 = "world") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],word1 = "x",word2 = "z") == 1
    assert candidate(wordsDict = ['sun', 'moon', 'star', 'planet', 'moon', 'sun', 'star', 'planet', 'moon', 'sun', 'star', 'planet', 'moon', 'sun'],word1 = "sun",word2 = "planet") == 2
    assert candidate(wordsDict = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'alpha'],word1 = "alpha",word2 = "epsilon") == 4
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'banana', 'cherry', 'apple', 'banana', 'cherry'],word1 = "apple",word2 = "cherry") == 1
    assert candidate(wordsDict = ['short', 'distance', 'between', 'two', 'words', 'short', 'distance', 'between', 'two', 'words'],word1 = "short",word2 = "words") == 1
    assert candidate(wordsDict = ['find', 'the', 'shortest', 'distance', 'between', 'two', 'words', 'in', 'this', 'example', 'find', 'the', 'shortest'],word1 = "find",word2 = "shortest") == 2
    assert candidate(wordsDict = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],word1 = "a",word2 = "b") == 1
    assert candidate(wordsDict = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],word1 = "a",word2 = "b") == 1
    assert candidate(wordsDict = ['red', 'blue', 'green', 'red', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue'],word1 = "red",word2 = "blue") == 1
    assert candidate(wordsDict = ['sun', 'moon', 'star', 'planet', 'moon', 'sun', 'planet', 'star', 'moon', 'sun'],word1 = "sun",word2 = "star") == 2
    assert candidate(wordsDict = ['aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'ccc'],word1 = "aaa",word2 = "ccc") == 1
    assert candidate(wordsDict = ['example', 'of', 'a', 'longer', 'list', 'with', 'repeated', 'words', 'that', 'appear', 'multiple', 'times', 'example', 'of', 'a'],word1 = "example",word2 = "a") == 2
    assert candidate(wordsDict = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'red', 'blue', 'green', 'yellow', 'red'],word1 = "red",word2 = "yellow") == 1
    assert candidate(wordsDict = ['sun', 'moon', 'stars', 'comet', 'planet', 'moon', 'sun', 'planet', 'comet', 'stars', 'moon', 'sun', 'planet', 'comet', 'stars', 'moon', 'sun', 'planet', 'comet', 'stars'],word1 = "sun",word2 = "comet") == 2
    assert candidate(wordsDict = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red'],word1 = "red",word2 = "yellow") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'one', 'two'],word1 = "one",word2 = "twenty") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],word1 = "x",word2 = "y") == 1
    assert candidate(wordsDict = ['sun', 'moon', 'star', 'planet', 'galaxy', 'universe', 'sun', 'moon', 'star', 'planet', 'galaxy', 'universe'],word1 = "sun",word2 = "universe") == 1
    assert candidate(wordsDict = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply', 'waldo', 'fred', 'plugh', 'xyzzy', 'thud', 'foo', 'bar'],word1 = "foo",word2 = "thud") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'],word1 = "three",word2 = "eleven") == 8
    assert candidate(wordsDict = ['complexity', 'of', 'the', 'algorithm', 'is', 'important', 'complexity', 'of', 'the', 'algorithm', 'is', 'important'],word1 = "complexity",word2 = "important") == 1
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e'],word1 = "a",word2 = "z") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],word1 = "x",word2 = "z") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'apple', 'banana', 'cherry'],word1 = "apple",word2 = "grape") == 1
    assert candidate(wordsDict = ['word', 'distance', 'calculation', 'word', 'distance', 'calculation', 'word', 'distance', 'calculation'],word1 = "word",word2 = "distance") == 1
    assert candidate(wordsDict = ['cat', 'dog', 'cat', 'fish', 'dog', 'cat', 'bird', 'dog', 'cat', 'fish', 'cat'],word1 = "cat",word2 = "dog") == 1
    assert candidate(wordsDict = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega'],word1 = "alpha",word2 = "omega") == 23
    assert candidate(wordsDict = ['fast', 'faster', 'fastest', 'slow', 'slower', 'slowest', 'fast', 'faster', 'fastest', 'slow', 'slower', 'slowest'],word1 = "fast",word2 = "slow") == 3
    assert candidate(wordsDict = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit'],word1 = "lorem",word2 = "adipiscing") == 2
    assert candidate(wordsDict = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow'],word1 = "blue",word2 = "yellow") == 2
    assert candidate(wordsDict = ['cat', 'dog', 'fish', 'bird', 'cat', 'dog', 'fish', 'bird', 'cat', 'dog', 'fish', 'bird', 'cat', 'dog', 'fish', 'bird', 'cat', 'dog', 'fish', 'bird'],word1 = "cat",word2 = "bird") == 1
    assert candidate(wordsDict = ['python', 'java', 'c', 'c++', 'javascript', 'python', 'go', 'c#', 'python', 'java'],word1 = "python",word2 = "java") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two', 'three', 'four', 'five'],word1 = "one",word2 = "ten") == 1
    assert candidate(wordsDict = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],word1 = "a",word2 = "b") == 1
    assert candidate(wordsDict = ['sun', 'moon', 'star', 'planet', 'galaxy', 'sun', 'moon', 'star', 'planet', 'galaxy', 'sun'],word1 = "sun",word2 = "galaxy") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two'],word1 = "one",word2 = "ten") == 1
    assert candidate(wordsDict = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],word1 = "abc",word2 = "yz") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],word1 = "one",word2 = "ten") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],word1 = "x",word2 = "a") == 25
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],word1 = "one",word2 = "ten") == 9
    assert candidate(wordsDict = ['repeat', 'this', 'sentence', 'repeat', 'this', 'sentence', 'repeat', 'this', 'sentence', 'repeat', 'this', 'sentence'],word1 = "repeat",word2 = "sentence") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen'],word1 = "one",word2 = "twelve") == 11
    assert candidate(wordsDict = ['data', 'science', 'machine', 'learning', 'data', 'science', 'artificial', 'intelligence'],word1 = "data",word2 = "intelligence") == 3
    assert candidate(wordsDict = ['zebra', 'giraffe', 'elephant', 'hippo', 'giraffe', 'zebra', 'hippo', 'elephant', 'giraffe', 'zebra'],word1 = "giraffe",word2 = "elephant") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'],word1 = "one",word2 = "fifteen") == 14
    assert candidate(wordsDict = ['repeat', 'this', 'repeat', 'this', 'repeat', 'this', 'repeat', 'this', 'repeat', 'this'],word1 = "repeat",word2 = "this") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'apple', 'banana'],word1 = "apple",word2 = "grape") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'apple', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'apple'],word1 = "apple",word2 = "grape") == 1
    assert candidate(wordsDict = ['python', 'java', 'c', 'c++', 'python', 'javascript', 'java', 'python', 'c', 'java'],word1 = "python",word2 = "java") == 1
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'one', 'three', 'five'],word1 = "one",word2 = "five") == 2
    assert candidate(wordsDict = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'one'],word1 = "one",word2 = "twenty") == 1
    assert candidate(wordsDict = ['car', 'bike', 'bus', 'train', 'car', 'bike', 'bus', 'train', 'car', 'bike', 'bus', 'train'],word1 = "car",word2 = "train") == 1
    assert candidate(wordsDict = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'alpha'],word1 = "alpha",word2 = "epsilon") == 4
    assert candidate(wordsDict = ['hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world'],word1 = "hello",word2 = "world") == 1
    assert candidate(wordsDict = ['python', 'java', 'c++', 'python', 'java', 'c#', 'python', 'ruby'],word1 = "python",word2 = "c++") == 1
    assert candidate(wordsDict = ['repeated', 'word', 'repeated', 'word', 'repeated', 'word', 'repeated', 'word'],word1 = "repeated",word2 = "word") == 1
    assert candidate(wordsDict = ['zebra', 'yak', 'xenon', 'wolf', 'vulture', 'toucan', 'snake', 'rabbit', 'quail', 'panda', 'orangutan', 'novel'],word1 = "zebra",word2 = "novel") == 11
    assert candidate(wordsDict = ['random', 'words', 'here', 'to', 'make', 'it', 'longer', 'and', 'more', 'complex', 'random', 'words'],word1 = "random",word2 = "complex") == 1
    assert candidate(wordsDict = ['loop', 'around', 'the', 'world', 'loop', 'around', 'the', 'world', 'loop', 'around', 'the', 'world'],word1 = "loop",word2 = "world") == 1
    assert candidate(wordsDict = ['far', 'apart', 'words', 'in', 'the', 'list', 'far', 'apart', 'words', 'in', 'the', 'list'],word1 = "far",word2 = "words") == 2
    assert candidate(wordsDict = ['red', 'blue', 'green', 'yellow', 'red', 'green', 'blue', 'red', 'green', 'yellow', 'red', 'blue'],word1 = "green",word2 = "red") == 1
    assert candidate(wordsDict = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],word1 = "x",word2 = "z") == 2
    assert candidate(wordsDict = ['left', 'right', 'up', 'down', 'left', 'right', 'up', 'down', 'left', 'right', 'up', 'down'],word1 = "left",word2 = "down") == 1
    assert candidate(wordsDict = ['repeat', 'me', 'please', 'repeat', 'me', 'please', 'repeat', 'me', 'please'],word1 = "repeat",word2 = "please") == 1
    assert candidate(wordsDict = ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow'],word1 = "red",word2 = "yellow") == 1
    assert candidate(wordsDict = ['once', 'upon', 'a', 'time', 'in', 'a', 'land', 'far', 'far', 'away'],word1 = "a",word2 = "away") == 4
    assert candidate(wordsDict = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11', 'word12', 'word1', 'word2'],word1 = "word1",word2 = "word2") == 1
    assert candidate(wordsDict = ['this', 'is', 'a', 'longer', 'test', 'case', 'with', 'multiple', 'words', 'this', 'is', 'another', 'test'],word1 = "this",word2 = "test") == 3
    assert candidate(wordsDict = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu'],word1 = "alpha",word2 = "mu") == 11
    assert candidate(wordsDict = ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z'],word1 = "x",word2 = "y") == 1
    assert candidate(wordsDict = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'],word1 = "fox",word2 = "dog") == 3
    assert candidate(wordsDict = ['zebra', 'yak', 'xenon', 'wolf', 'vulture', 'wolf', 'yak', 'xenon', 'zebra', 'yak', 'wolf'],word1 = "yak",word2 = "wolf") == 1
    assert candidate(wordsDict = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'],word1 = "a",word2 = "b") == 1
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],word1 = "a",word2 = "j") == 1
    assert candidate(wordsDict = ['optimize', 'this', 'code', 'for', 'performance', 'optimize', 'this', 'code', 'for', 'performance', 'optimize'],word1 = "optimize",word2 = "performance") == 1
    assert candidate(wordsDict = ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'quick', 'brown', 'fox'],word1 = "fox",word2 = "dog") == 3
    assert candidate(wordsDict = ['long', 'list', 'with', 'repeated', 'words', 'long', 'list', 'with', 'repeated', 'words', 'long', 'list'],word1 = "long",word2 = "words") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange'],word1 = "apple",word2 = "orange") == 12
    assert candidate(wordsDict = ['zebra', 'yak', 'xenon', 'wolf', 'vulture', 'zebra', 'yak', 'xenon', 'wolf', 'vulture'],word1 = "zebra",word2 = "vulture") == 1
    assert candidate(wordsDict = ['python', 'java', 'c++', 'ruby', 'python', 'java', 'c++', 'ruby', 'python'],word1 = "java",word2 = "ruby") == 2
    assert candidate(wordsDict = ['a', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b'],word1 = "a",word2 = "c") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'apple', 'banana', 'cherry'],word1 = "apple",word2 = "cherry") == 2
    assert candidate(wordsDict = ['hello', 'world', 'example', 'code', 'hello', 'code', 'world', 'example', 'hello', 'example'],word1 = "hello",word2 = "example") == 1
    assert candidate(wordsDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a'],word1 = "a",word2 = "z") == 1
    assert candidate(wordsDict = ['this', 'is', 'a', 'simple', 'test', 'for', 'the', 'shortest', 'distance', 'problem'],word1 = "this",word2 = "problem") == 9
    assert candidate(wordsDict = ['a', 'x', 'y', 'z', 'a', 'm', 'n', 'o', 'z', 'p', 'q', 'a', 'b', 'c', 'z'],word1 = "a",word2 = "z") == 1
    assert candidate(wordsDict = ['cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog'],word1 = "cat",word2 = "dog") == 1
    assert candidate(wordsDict = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'],word1 = "a",word2 = "c") == 1
    assert candidate(wordsDict = ['a', 'b', 'a', 'c', 'b', 'a', 'b', 'c', 'a', 'b'],word1 = "a",word2 = "c") == 1
    assert candidate(wordsDict = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'apple', 'banana'],word1 = "apple",word2 = "grape") == 2
    assert candidate(wordsDict = ['random', 'words', 'here', 'random', 'words', 'here', 'random', 'words', 'here'],word1 = "random",word2 = "here") == 1
    assert candidate(wordsDict = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua'],word1 = "lorem",word2 = "aliqua") == 18
    assert candidate(wordsDict = ['repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat', 'repeat'],word1 = "repeat",word2 = "repeat") == 0
