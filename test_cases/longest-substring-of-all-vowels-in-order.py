# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaauuaeiuuuuuuuuuuuuuuuuuuuuaaa") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuaauuaeiu") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuuaaaaaaeiou") == 10
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuu") == 7
    assert candidate(word = "aeeeiiiioooauuuaeiou") == 5
    assert candidate(word = "aeiaaioaaaaeiiiiouuuuuaaaaaaaaaeeeeiiiioooouuuuuu") == 27
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuooaaeiouaaaaaaaaaaeiouuuuuuuuuuuuuuuuuuuu") == 33
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuuaeiouuuaeiouuu") == 7
    assert candidate(word = "aeiaaioaaaaeiiaaaouuuooauuaeiu") == 0
    assert candidate(word = "aeiouaeiouaeiouaeiouaeiou") == 5
    assert candidate(word = "aaaaaaaaaeeeeeeeeeeiiiiiiioooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu") == 68
    assert candidate(word = "aeiaaioaaaaeiioooaeiouuu") == 7
    assert candidate(word = "aeiaaioaaaaeiiooouuuaeiou") == 13
    assert candidate(word = "a") == 0
    assert candidate(word = "aeiou") == 5
    assert candidate(word = "aeiaaioaaaaeiiaaaiiiiiouuuuuuuuuuuuuuuuuuuu") == 0
    assert candidate(word = "aeiaaioaaaaeiiaaaouuuooaauuaeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
    assert candidate(word = "aeiaaioaaaaeiiiiouuuooaauuaeiu") == 13
    assert candidate(word = "aeiaaioaaaaeiiooouuuooauuaeiu") == 13
    assert candidate(word = "uuuuuuuuuuuuuuuuuuuu") == 0
