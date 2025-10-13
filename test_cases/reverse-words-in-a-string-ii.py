# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', ' ', 'f', 'g', 'h', 'i', 'j', 'k']) == None
    assert candidate(s = ['a']) == None
    assert candidate(s = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']) == None
    assert candidate(s = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'f', 'u', 'n']) == None
    assert candidate(s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']) == None
    assert candidate(s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ' ', '1', '2', '3', ' ', 'x', 'y', 'z']) == None
    assert candidate(s = ['l', 'e', 't', 's', ' ', 'c', 'o', 'd', 'e']) == None
    assert candidate(s = ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']) == None
    assert candidate(s = ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', 'i', 'o', 'n']) == None
    assert candidate(s = ['L', 'o', 'r', 'e', 'm', ' ', 'i', 'p', 's', 'u', 'm', ' ', 'd', 'o', 'l', 'o', 'r', ' ', 's', 'i', 't', ' ', 'a', 'm', 'e', 't', ' ', 'c', 'o', 'n', 's', 'e', 'c', 't', 'e', 't', 'u', 'r', 'a', 'd', 'i', 'p', 'i', 's', 'c', 'i', 'n', 'g', ' ', 'e', 'l', 'i', 't', ' ', 's', 'i', 'n', 'c', 'i', 'd', 'i', 'd', 'u', 'n', 't', ' ', 'u', 't', ' ', 'l', 'a', 'b', 'o', 'r', 'e', 't', ' ', 'n', 'i', 'h', 'i', 'l', ' ', 'f', 'a', 'c', 'i', 'l', 'i', 't', 'a', 't', 'i', 's']) == None
    assert candidate(s = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 't', 'h', 'i', 'n', 'g', ' ', 'a', 'b', 'o', 'u', 't', ' ', 't', 'h', 'e', ' ', 'r', 'i', 'g', 'h', 't', ' ', 'o', 'f', ' ', 'f', 'r', 'e', 'e', 'd', 'o', 'm']) == None
    assert candidate(s = ['Q', 'w', 'e', 'r', 't', 'y', ' ', 'U', 'i', 'o', 'p', ' ', 'A', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ' ', 'Z', 'x', 'c', 'v', 'b', 'n', 'm']) == None
    assert candidate(s = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'c', 'a', 's', 'e']) == None
    assert candidate(s = ['I', 'n', ' ', 't', 'h', 'e', ' ', 'b', 'e', 'g', 'i', 'n', 'n', 'i', 'n', 'g', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'e', 'n', 'd', ' ', 'o', 'f', ' ', 't', 'h', 'e', ' ', 'w', 'o', 'r', 'l', 'd']) == None
    assert candidate(s = ['J', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't', ' ', 'i', 's', ' ', 'a', ' ', 'v', 'e', 'r', 'y', ' ', 'p', 'o', 'p', 'u', 'l', 'a', 'r']) == None
    assert candidate(s = ['A', ' ', 's', 'h', 'o', 'r', 't', ' ', 'w', 'o', 'r', 'd']) == None
    assert candidate(s = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'f', 'o', 'r', ' ', 'r', 'e', 'v', 'e', 'r', 's', 'i', 'n', 'g']) == None
    assert candidate(s = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'w', 'i', 't', 'h', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's']) == None
    assert candidate(s = ['R', 'e', 'v', 'e', 'r', 's', 'i', 'n', 'g', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'i', 'n', ' ', 'a', ' ', 's', 'i', 'n', 'g', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']) == None
    assert candidate(s = ['C', 'a', 'n', ' ', 'y', 'o', 'u', ' ', 'r', 'e', 'a', 'd', ' ', 't', 'h', 'i', 's', '?', ' ', 'I', ' ', 'h', 'o', 'p', 'e', ' ', 's', 'o', '!']) == None
    assert candidate(s = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', ' ', 'c', 'a', 's', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'm', 'o', 'r', 'e', ' ', 'w', 'o', 'r', 'd', 's']) == None
    assert candidate(s = ['A', 'p', 'p', 'l', 'e', ' ', 'B', 'a', 'n', 'a', 'n', 'a', ' ', 'C', 'h', 'e', 'r', 'r', 'y', ' ', 'D', 'a', 't', 'e', ' ', 'E', 'l', 'd', 'e', 'r', 'b', 'e', 'r', 'r', 'y', ' ', 'F', 'i', 'g', ' ', 'G', 'r', 'a', 'p', 'e', ' ', 'H', 'a', 't', 'e', 'r', 'r', 'y', ' ', 'I', 'n', 'g', 'r', 'i', 'd', 'i', 'e', 'n', 't', ' ', 'J', 'a', 'c', 'u', 'm', 'b', 'o', 't', ' ', 'K', 'i', 'w', 'i']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'l', 'o', 'n', 'g', 'e', 'r', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 'w', 'i', 't', 'h', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's']) == None
    assert candidate(s = ['A', ' ', 'f', 'a', 's', 't', ' ', 'e', 'x', 'a', 'm', 'p', 'l', 'e']) == None
    assert candidate(s = ['T', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'f', 'o', 'x', ' ', 'j', 'u', 'm', 'p', 's', ' ', 'o', 'v', 'e', 'r', ' ', 't', 'h', 'e', ' ', 'l', 'a', 'z', 'y', ' ', 'd', 'o', 'g']) == None
    assert candidate(s = ['1', '2', '3', '4', ' ', '5', '6', '7', '8', ' ', '9', '1', '0', ' ', '1', '1', '1', '2', '1', '3', '1', '4', '1', '5', '1', '6', '1', '7', '1', '8', '1', '9', '2', '0']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'a', 'r', 'e', ' ', 's', 'h', 'o', 'r', 't', ' ', 'a', 'n', 'd', ' ', 's', 'o', 'm', 'e', ' ', 'a', 'r', 'e', ' ', 'l', 'o', 'n', 'g', 'e', 'r']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 's', 'h', 'o', 'r', 't', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'h', 'e', 'r', 'e']) == None
    assert candidate(s = ['J', 'u', 'm', 'p', 's', ' ', 'o', 'v', 'e', 'r', ' ', 't', 'h', 'e', ' ', 'l', 'a', 'z', 'y', ' ', 'd', 'o', 'g']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'l', 'o', 'n', 'g', 'e', 'r', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'r', 'e', 'v', 'e', 'r', 's', 'e']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', '1', '2', '3', ' ', 'a', 'n', 'd', ' ', 'l', 'e', 't', 't', 'e', 'r', 's']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'a', 'r', 'e', ' ', 'l', 'o', 'n', 'g', 'e', 'r', ' ', 't', 'h', 'a', 'n', ' ', 'o', 't', 'h', 'e', 'r', 's']) == None
    assert candidate(s = ['A', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'm', 'o', 'r', 'e', ' ', 'c', 'o', 'm', 'p', 'l', 'e', 'x', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'h', 'e', 'r', 'e']) == None
    assert candidate(s = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't']) == None
    assert candidate(s = ['T', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e', ' ', 'a', 'n', 'd', ' ', 't', 'h', 'e', ' ', 's', 'u', 'n', ' ', 'i', 's', ' ', 's', 'h', 'i', 'n', 'i', 'n', 'g']) == None
    assert candidate(s = ['E', 'x', 'a', 'm', 'p', 'l', 'e', ' ', 'i', 'n', 'p', 'u', 't', ' ', 'w', 'i', 't', 'h', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's']) == None
    assert candidate(s = ['1', '2', '3', ' ', '4', '5', '6', ' ', '7', '8', '9', ' ', '1', '0', '1', '1', '1', '2']) == None
    assert candidate(s = ['A', 'n', 'o', 't', 'h', 'e', 'r', ' ', 't', 'e', 's', 't', ' ', 'w', 'i', 't', 'h', ' ', 'd', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't', ' ', 'l', 'e', 'n', 'g', 't', 'h', 's']) == None
    assert candidate(s = ['A', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'f', 'o', 'x']) == None
    assert candidate(s = ['C', 'a', 'n', ' ', 'y', 'o', 'u', ' ', 'r', 'e', 'a', 'd', ' ', 't', 'h', 'i', 's', '?', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', '.']) == None
    assert candidate(s = ['R', 'e', 'v', 'e', 'r', 's', 'i', 'n', 'g', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'h', 'e', 'r', 'e']) == None
    assert candidate(s = ['R', 'e', 'v', 'e', 'r', 's', 'i', 'n', 'g', ' ', 'i', 's', ' ', 'a', ' ', 'k', 'e', 'y', ' ', 's', 'k', 'i', 'l', 'l']) == None
    assert candidate(s = ['C', 'a', 'n', ' ', 'y', 'o', 'u', ' ', 'r', 'e', 'a', 'd', ' ', 't', 'h', 'i', 's', '?', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'p', 'u', 'z', 'z', 'l', 'e']) == None
    assert candidate(s = ['O', 'n', 'e', ' ', 't', 'w', 'o', ' ', 't', 'h', 'r', 'e', 'e', ' ', 'f', 'o', 'u', 'r', ' ', 'f', 'i', 'v', 'e', ' ', 's', 'i', 'x', ' ', 's', 'e', 'v', 'e', 'n', ' ', 'e', 'i', 'g', 'h', 't', ' ', 'n', 'i', 'n', 'e', ' ', 't', 'e', 'n']) == None
    assert candidate(s = ['1', '2', '3', ' ', '4', '5', '6', ' ', '7', '8', '9', ' ', '0']) == None
    assert candidate(s = ['A', 'n', 'n', 'a', ' ', 'L', 'o', 'n', 'g', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's']) == None
    assert candidate(s = ['M', 'u', 'l', 't', 'i', 'p', 'l', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'w', 'i', 't', 'h', ' ', 'u', 'p', 'p', 'e', 'r', 'c', 'a', 's', 'e', ' ', 'a', 'n', 'd', ' ', 'l', 'o', 'w', 'e', 'r', 'c', 'a', 's', 'e']) == None
    assert candidate(s = ['A', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'f', 'o', 'x', ' ', 'j', 'u', 'm', 'p', 's', ' ', 'o', 'v', 'e', 'r', ' ', 't', 'h', 'e', ' ', 'l', 'a', 'z', 'y', ' ', 'd', 'o', 'g']) == None
    assert candidate(s = ['O', 'n', 'e', ' ', 't', 'w', 'o', ' ', 't', 'h', 'r', 'e', 'e', ' ', 'f', 'o', 'u', 'r']) == None
    assert candidate(s = ['W', 'e', ' ', 'w', 'i', 'l', 'l', ' ', 'n', 'e', 'v', 'e', 'r', ' ', 'g', 'i', 'v', 'e', ' ', 'u', 'p', ' ', 'u', 'n', 't', 'i', 'l', ' ', 't', 'h', 'e', ' ', 'l', 'i', 'g', 'h', 't', ' ', 'o', 'f', ' ', 'f', 'r', 'e', 'e', 'd', 'o', 'm']) == None
    assert candidate(s = ['T', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', 'r', 'o', 'w', 'n', ' ', 'f', 'o', 'x']) == None
    assert candidate(s = ['J', 'a', 'v', 'a', ' ', 'i', 's', ' ', 'a', 'l', 's', 'o', ' ', 'a', ' ', 'p', 'o', 'p', 'u', 'l', 'a', 'r', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']) == None
    assert candidate(s = ['L', 'o', 'r', 'e', 'm', ' ', 'i', 'p', 's', 'u', 'm', ' ', 'd', 'o', 'l', 'o', 'r', ' ', 's', 'i', 't', ' ', 'a', 'm', 'e', 't', ' ', 'c', 'o', 'n', 's', 'e', 'c', 't', 'e', 't', 'u', 'r', 'a', 'd', 'i', 'p', 'i', 's', 'c', 'i', 'n', 'g', ' ', 'e', 'l', 'i', 't', ' ', 's', 'e', 'd', ' ', 'd', 'o', 'l', 'o', 'r', 'e', 'm', ' ', 'i', 'p', 's', 'u', 'm']) == None
    assert candidate(s = ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 't', 'h', 'e', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'o', 'f', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']) == None
    assert candidate(s = ['S', 'o', 'm', 'e', ' ', 'm', 'i', 'x', 'e', 'd', ' ', 'c', 'a', 's', 'e', ' ', 'w', 'i', 't', 'h', ' ', 'U', 'P', 'P', 'E', 'R', ' ', 'a', 'n', 'd', ' ', 'l', 'o', 'w', 'e', 'r', ' ', 'c', 'a', 's', 'e']) == None
    assert candidate(s = ['W', 'h', 'a', 't', ' ', 'i', 'f', ' ', 't', 'h', 'e', ' ', 'w', 'o', 'r', 'd', 's', ' ', 'a', 'r', 'e', ' ', 'v', 'e', 'r', 'y', ' ', 'l', 'o', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'c', 'o', 'm', 'p', 'l', 'e', 'x']) == None
    assert candidate(s = ['A', 'b', 'c', ' ', 'd', 'e', 'f', 'g', ' ', 'h', 'i', 'j', 'k', ' ', 'l', 'm', 'n']) == None
