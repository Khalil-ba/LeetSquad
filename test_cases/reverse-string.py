# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = ['1', '2', '3', '4', '5']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == None
    assert candidate(s = ['a', 'b']) == None
    assert candidate(s = ['a']) == None
    assert candidate(s = ['A', 'b', 'C', 'd', 'E', 'f', 'G']) == None
    assert candidate(s = ['A', 'b', 'C', 'd', 'E', 'f']) == None
    assert candidate(s = ['Z']) == None
    assert candidate(s = ['h', 'e', 'l', 'l', 'o']) == None
    assert candidate(s = ['x', 'y', 'z', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p']) == None
    assert candidate(s = ['H', 'a', 'n', 'n', 'a', 'h']) == None
    assert candidate(s = ['t', 'e', 's', 't', 'i', 'n', 'g', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']) == None
    assert candidate(s = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'c', 'a', 's', 'e']) == None
    assert candidate(s = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'a', ' ', 'v', 'e', 'r', 'y', ' ', 'p', 'o', 'w', 'e', 'r', 'f', 'u', 'l', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']) == None
    assert candidate(s = ['Python', '!', 'is', 'fun']) == None
    assert candidate(s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']) == None
    assert candidate(s = ['race', 'car', '!']) == None
    assert candidate(s = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'f', 'u', 'n']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) == None
    assert candidate(s = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']) == None
    assert candidate(s = ['123', '456', '789']) == None
    assert candidate(s = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']) == None
    assert candidate(s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '<', '.', '>', '?']) == None
    assert candidate(s = ['Python', 'is', 'awesome!']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == None
    assert candidate(s = ['r', 'e', 'v', 'e', 'r', 's', 'i', 'b', 'l', 'e', ' ', 'S', 't', 'r', 'i', 'n', 'g']) == None
    assert candidate(s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ':', ';', "'", ',', '<', '>', '.', '/', '?', '[', ']', '{', '}', '|', '\\']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == None
    assert candidate(s = ['racecar', 'is', 'a', 'level', 'palindrome']) == None
    assert candidate(s = ['A', '1', 'B', '2', 'C', '3', 'D', '4', 'E', '5', 'F', '6', 'G', '7', 'H', '8', 'I', '9', 'J', '0']) == None
    assert candidate(s = ['A', 'n', 'k', 'u', 'r', ' ', 'P', 'a', 't', 'i', 'l']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == None
    assert candidate(s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) == None
    assert candidate(s = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ',', '.', '/', '?', ':', ';', "'", '"', '[', ']', '{', '}', '|', '\\', '`', '~', '<', '>']) == None
    assert candidate(s = ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']) == None
    assert candidate(s = ['x', 'y', 'z', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', ',', '.', '/', '<', '.', '>', '?']) == None
    assert candidate(s = ['L', 'o', 'r', 'e', 'm', ' ', 'i', 'p', 's', 'u', 'm', ' ', 'd', 'o', 'l', 'o', 'r', ' ', 's', 'i', 't', ' ', 'a', 'm', 'e', 't']) == None
    assert candidate(s = ['M', 'e', 'd', 'i', 'a', 'V', 'a', 'i', 'd', ' ', 'T', 'e', 'c', 'h', 'n', 'o', 'l', 'o', 'g', 'y']) == None
    assert candidate(s = ['A', 'n', 'n', 'a', 'k', 'a', 'l', 'a', 'k', 'a', 'n', 'n', 'A']) == None
