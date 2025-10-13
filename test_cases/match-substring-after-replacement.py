# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "fooleetbar",sub = "f00l",mappings = [['o', '0']]) == False
    assert candidate(s = "fool3e7bar",sub = "leet",mappings = [['e', '3'], ['t', '7'], ['t', '8']]) == True
    assert candidate(s = "Fool33tbaR",sub = "leetd",mappings = [['e', '3'], ['t', '7'], ['t', '8'], ['d', 'b'], ['p', 'b']]) == True
    assert candidate(s = "1234567890",sub = "120",mappings = [['3', '4'], ['5', '6'], ['7', '8'], ['9', '0']]) == False
    assert candidate(s = "thisisaverylongstringwithmanycharacters",sub = "thisisaverylongstringwithmanychar1",mappings = [['a', '1']]) == False
    assert candidate(s = "abcABC123",sub = "aBc12",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['1', '2'], ['2', '3']]) == True
    assert candidate(s = "A1B2C3D4E5F6G7H8I9J0",sub = "abcdefghij",mappings = [['1', 'a'], ['2', 'b'], ['3', 'c'], ['4', 'd'], ['5', 'e'], ['6', 'f'], ['7', 'g'], ['8', 'h'], ['9', 'i'], ['0', 'j']]) == False
    assert candidate(s = "abcde",sub = "edcba",mappings = [['a', 'e'], ['b', 'd'], ['c', 'c'], ['d', 'b'], ['e', 'a']]) == True
    assert candidate(s = "AaBbCc",sub = "abc",mappings = [['A', 'a'], ['B', 'b'], ['C', 'c']]) == False
    assert candidate(s = "UPPERlower",sub = "lower",mappings = [['U', 'l'], ['P', 'o'], ['E', 'w'], ['R', 'r']]) == True
    assert candidate(s = "12345678901234567890",sub = "13579",mappings = [['1', '2'], ['3', '4'], ['5', '6'], ['7', '8'], ['9', '0']]) == False
    assert candidate(s = "xyzuvw",sub = "xyzz",mappings = [['z', 'w'], ['z', 'u']]) == True
    assert candidate(s = "aaaaaaa",sub = "aaab",mappings = [['a', 'b']]) == False
    assert candidate(s = "aaaaabbbbcccc",sub = "abc",mappings = [['a', 'b'], ['b', 'c'], ['c', 'a']]) == True
    assert candidate(s = "1234567890qwertyuiopasdfghjklzxcvbnm",sub = "QWERTYUIOPASDFGHJKLZXCVBNM",mappings = [['q', 'Q'], ['w', 'W'], ['e', 'E'], ['r', 'R'], ['t', 'T'], ['y', 'Y'], ['u', 'U'], ['i', 'I'], ['o', 'O'], ['p', 'P'], ['a', 'A'], ['s', 'S'], ['d', 'D'], ['f', 'F'], ['g', 'G'], ['h', 'H'], ['j', 'J'], ['k', 'K'], ['l', 'L'], ['z', 'Z'], ['x', 'X'], ['c', 'C'], ['v', 'V'], ['b', 'B'], ['n', 'N'], ['m', 'M']]) == False
    assert candidate(s = "1234567890abcdefghijklmnopqrstuvwxyz",sub = "123abc",mappings = [['1', 'a'], ['2', 'b'], ['3', 'c'], ['a', '1'], ['b', '2'], ['c', '3']]) == False
    assert candidate(s = "mississippi",sub = "misp",mappings = [['i', 's'], ['s', 'i']]) == False
    assert candidate(s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789",sub = "abcdef",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['0', 'a'], ['1', 'b']]) == False
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",sub = "zzzzzzzzzzzzzzzz",mappings = []) == True
    assert candidate(s = "PythonProgrammingIsFun",sub = "PythnPrgrammngIsFn",mappings = [['o', '0'], ['r', '4'], ['g', '9'], ['m', 'n'], ['n', 'm'], ['u', '1']]) == False
    assert candidate(s = "abcXYZabcXYZabc",sub = "XYZ",mappings = [['X', 'a'], ['Y', 'b'], ['Z', 'c']]) == True
    assert candidate(s = "abcXYZ123defGHI456",sub = "xyz",mappings = [['x', 'X'], ['y', 'Y'], ['z', 'Z']]) == True
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",sub = "mnoPQR",mappings = [['m', 'M'], ['n', 'N'], ['o', 'O'], ['p', 'P'], ['q', 'Q'], ['r', 'R'], ['s', 'S'], ['t', 'T']]) == False
    assert candidate(s = "QwErTyUiOpAsDfGhJkLzXcVbNm",sub = "qwertyuiopasdfghjklzxcvbnm",mappings = [['Q', 'q'], ['W', 'w'], ['E', 'e'], ['R', 'r'], ['T', 't'], ['Y', 'y'], ['U', 'u'], ['I', 'i'], ['O', 'o'], ['P', 'p'], ['A', 'a'], ['S', 's'], ['D', 'd'], ['F', 'f'], ['G', 'g'], ['H', 'h'], ['J', 'j'], ['K', 'k'], ['L', 'l'], ['Z', 'z'], ['X', 'x'], ['C', 'c'], ['V', 'v'], ['B', 'b'], ['N', 'n'], ['M', 'm']]) == False
    assert candidate(s = "xyzabcxyz",sub = "zyx",mappings = [['x', 'y'], ['y', 'z'], ['z', 'x']]) == False
    assert candidate(s = "Python3.8",sub = "Python3.8",mappings = []) == True
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz0123456789",sub = "zyxwvutsrqp",mappings = [['z', '9'], ['y', '8'], ['x', '7'], ['w', '6'], ['v', '5'], ['u', '4'], ['t', '3'], ['s', '2'], ['r', '1'], ['q', '0']]) == False
    assert candidate(s = "aabbccddeeff",sub = "abc",mappings = [['a', 'b'], ['b', 'c'], ['c', 'd']]) == True
    assert candidate(s = "9876543210",sub = "123",mappings = [['1', '9'], ['2', '8'], ['3', '7']]) == True
    assert candidate(s = "mississippi",sub = "miss",mappings = [['m', 'i'], ['i', 's'], ['s', 'p']]) == True
    assert candidate(s = "mississippi",sub = "MISS",mappings = [['m', 'M'], ['i', 'I'], ['s', 'S']]) == False
    assert candidate(s = "ababababababab",sub = "AB",mappings = [['a', 'A'], ['b', 'B']]) == False
    assert candidate(s = "nestedparentheses",sub = "nest1dpar3ntheses",mappings = [['e', '1'], ['o', '3']]) == False
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",sub = "aaaaaaaaaa",mappings = [['z', 'a']]) == False
    assert candidate(s = "abcabcabcabcabcabc",sub = "abababa",mappings = [['a', 'b'], ['b', 'a']]) == False
    assert candidate(s = "MULTIPLEMAPPINGS",sub = "MAPPING",mappings = [['M', 'N'], ['A', 'B'], ['P', 'Q'], ['I', 'J'], ['G', 'H']]) == True
    assert candidate(s = "12345678901234567890",sub = "111111",mappings = [['1', '2'], ['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7']]) == False
    assert candidate(s = "abracadabra123",sub = "acad",mappings = [['a', '1'], ['d', '3'], ['a', 'b']]) == True
    assert candidate(s = "TheQuickBrownFox",sub = "TheQucikBrwnFks",mappings = [['u', 'i'], ['i', 'k'], ['B', 'r'], ['r', 'n'], ['F', 'k'], ['o', 'u']]) == False
    assert candidate(s = "MAPPINGmappings",sub = "mapping",mappings = [['M', 'm'], ['A', 'a'], ['P', 'p'], ['P', 'p'], ['I', 'i'], ['N', 'n'], ['G', 'g']]) == True
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",sub = "fedcba",mappings = [['f', 'Z'], ['e', 'Y'], ['d', 'X'], ['c', 'W'], ['b', 'V'], ['a', 'U']]) == False
    assert candidate(s = "mississippi",sub = "missi5",mappings = [['i', '5']]) == False
    assert candidate(s = "ababababab",sub = "abab",mappings = [['a', 'b'], ['b', 'a']]) == True
    assert candidate(s = "xyz123xyz123xyz123",sub = "abc",mappings = [['a', 'x'], ['b', 'y'], ['c', 'z'], ['1', 'a'], ['2', 'b'], ['3', 'c']]) == True
    assert candidate(s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ",sub = "ABCD123",mappings = [['E', '1'], ['F', '2'], ['G', '3']]) == False
    assert candidate(s = "00000000000000000000",sub = "1111111111",mappings = [['0', '1']]) == False
    assert candidate(s = "abcabcabcabcabcabc",sub = "aBc",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C']]) == False
    assert candidate(s = "HELLOworld",sub = "H3LL0",mappings = [['E', '3'], ['O', '0']]) == False
    assert candidate(s = "1234567890",sub = "123",mappings = [['1', '9'], ['2', '8'], ['3', '7']]) == True
    assert candidate(s = "a1b2c3d4e5f6g7h8i9j0",sub = "abcdefghij",mappings = [['a', '1'], ['b', '2'], ['c', '3'], ['d', '4'], ['e', '5'], ['f', '6'], ['g', '7'], ['h', '8'], ['i', '9'], ['j', '0']]) == False
    assert candidate(s = "abcXYZdefUVW",sub = "xyzuvw",mappings = [['a', 'x'], ['b', 'y'], ['c', 'z'], ['d', 'u'], ['e', 'v'], ['f', 'w']]) == False
    assert candidate(s = "xyxyxyxyxy",sub = "xyz",mappings = [['x', 'y'], ['y', 'x']]) == False
    assert candidate(s = "thisisaverylongstringwithmanymappings",sub = "short",mappings = [['s', 't'], ['h', 'i'], ['o', 's'], ['r', 'r'], ['t', 'o']]) == False
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",sub = "xyz",mappings = [['x', 'v'], ['y', 'w'], ['z', 'x']]) == True
    assert candidate(s = "A1B2C3D4E5F6G7H8I9J0",sub = "abcd",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D']]) == False
    assert candidate(s = "1234567890",sub = "abcdefghij",mappings = [['1', 'a'], ['2', 'b'], ['3', 'c'], ['4', 'd'], ['5', 'e'], ['6', 'f'], ['7', 'g'], ['8', 'h'], ['9', 'i']]) == False
    assert candidate(s = "abcdefabcdefabcdef",sub = "xyz",mappings = [['a', 'x'], ['b', 'y'], ['c', 'z']]) == False
    assert candidate(s = "zzzzzzzzzzzzzzzzzzzz",sub = "zzzz",mappings = [['z', 'Z'], ['Z', 'z']]) == True
    assert candidate(s = "aaaaaa",sub = "bbbbb",mappings = [['a', 'b']]) == False
    assert candidate(s = "abcabcabcabc",sub = "abca",mappings = [['a', 'b'], ['b', 'c'], ['c', 'a']]) == True
    assert candidate(s = "111222333444555666777888999",sub = "123456789",mappings = [['1', '2'], ['2', '3'], ['3', '4'], ['4', '5'], ['5', '6'], ['6', '7'], ['7', '8'], ['8', '9']]) == False
    assert candidate(s = "1234567890",sub = "123abc",mappings = [['4', 'a'], ['5', 'b'], ['6', 'c']]) == False
    assert candidate(s = "abcabcabcabcabc",sub = "abdc",mappings = [['a', 'd'], ['b', 'c']]) == False
    assert candidate(s = "AAABBBCCCDDD",sub = "abc",mappings = [['A', 'a'], ['B', 'b'], ['C', 'c']]) == False
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz",sub = "zyxwvutsrqponmlkjihgfedcba",mappings = [['a', 'z'], ['b', 'y'], ['c', 'x'], ['d', 'w'], ['e', 'v'], ['f', 'u'], ['g', 't'], ['h', 's'], ['i', 'r'], ['j', 'q'], ['k', 'p'], ['l', 'o'], ['m', 'n']]) == False
    assert candidate(s = "Python3.8",sub = "Python3.8",mappings = [['3', '2']]) == True
    assert candidate(s = "abcdefghij",sub = "abcd12",mappings = [['e', '1'], ['f', '2'], ['g', '3']]) == False
    assert candidate(s = "HelloWorld123",sub = "hello123",mappings = [['H', 'h'], ['W', 'w'], ['o', '0'], ['r', '4'], ['l', '1']]) == False
    assert candidate(s = "aabbccddeeffgg",sub = "abc",mappings = [['a', 'b'], ['b', 'c'], ['c', 'd']]) == True
    assert candidate(s = "abcdeABCDEabcdeABCDE",sub = "abcde",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E']]) == True
    assert candidate(s = "patternmatching",sub = "patt3rn",mappings = [['a', '3']]) == False
    assert candidate(s = "abcdefgABCDEFG",sub = "aBcDeFg",mappings = [['a', 'A'], ['b', 'B'], ['c', 'C'], ['d', 'D'], ['e', 'E'], ['f', 'F'], ['g', 'G']]) == True
    assert candidate(s = "abcdefghijk",sub = "abc123",mappings = [['d', '1'], ['e', '2'], ['f', '3']]) == False
    assert candidate(s = "zzzzzzzzzz",sub = "aaa",mappings = [['z', 'a']]) == False
    assert candidate(s = "hello123world456",sub = "hell12",mappings = [['l', '1'], ['o', '2']]) == False
    assert candidate(s = "helloWorld123",sub = "he1oW3ld",mappings = [['l', '1'], ['o', '0'], ['W', '3'], ['r', '2']]) == False
    assert candidate(s = "hellohellohello",sub = "world",mappings = [['w', 'h'], ['o', 'e'], ['r', 'l'], ['l', 'l'], ['d', 'o']]) == True
    assert candidate(s = "Python38",sub = "pyth0n39",mappings = [['P', 'p'], ['Y', 'y'], ['t', '0'], ['h', 'h'], ['o', '3'], ['n', '9']]) == False
    assert candidate(s = "12345678901234567890",sub = "12345",mappings = [['1', '2'], ['2', '3'], ['3', '4'], ['4', '5'], ['5', '6']]) == True
