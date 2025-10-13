# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(grid = ['\\/', '\\/', '\\/']) == 14
    assert candidate(grid = ['///', '///', '///']) == 6
    assert candidate(grid = ['\\\\', '\\\\', '\\\\']) == 14
    assert candidate(grid = ['/', '/', '/']) == 25
    assert candidate(grid = ['/\\', '/\\', '/\\']) == 14
    assert candidate(grid = ['\\/', '/\\', '\\/']) == 15
    assert candidate(grid = [' /', '/ ']) == 2
    assert candidate(grid = ['/\\', '\\/']) == 5
    assert candidate(grid = ['\\', '/']) == 9
    assert candidate(grid = [' /', '  ']) == 1
    assert candidate(grid = ['   ', '   ', '   ']) == 1
    assert candidate(grid = ['//', '\\']) == 6
    assert candidate(grid = [' / ', '/ \\/', ' \\ ', '\\ / ']) == 10
    assert candidate(grid = ['  ', '\\/', '/\\', '  ']) == 32
    assert candidate(grid = ['/\\/', '\\/\\', '/\\/', '\\/\\']) == 22
    assert candidate(grid = ['/\\/\\', '\\/\\/', '/\\/\\', '\\/\\/']) == 13
    assert candidate(grid = ['\\/', ' \\/', '\\/', '\\/', '/\\', '/\\', '/\\', '\\/']) == 191
    assert candidate(grid = ['\\ ', '\\ ', '\\ ', '\\ ']) == 30
    assert candidate(grid = ['/\\', '\\/', '/\\']) == 15
    assert candidate(grid = ['\\', '\\', '\\']) == 25
    assert candidate(grid = ['/\\ ', '\\/ ', '/\\ ', '\\/ ']) == 18
    assert candidate(grid = ['/ ', '\\ ', '/ ', '\\ ']) == 32
    assert candidate(grid = ['\\ ', ' / ', '\\ ']) == 7
    assert candidate(grid = ['\\/\\', '\\/\\', '\\/\\']) == 6
    assert candidate(grid = ['/\\/', '\\/\\', '/\\/']) == 8
    assert candidate(grid = ['\\/', ' / ', '/\\']) == 9
    assert candidate(grid = ['/\\', '\\/', '/\\']) == 15
    assert candidate(grid = ['\\/', '/\\', ' / ', '\\/']) == 29
    assert candidate(grid = ['\\/\\', '/\\/', '\\/\\']) == 8
    assert candidate(grid = ['\\\\', '/\\/', '\\/\\', '/\\\\']) == 24
    assert candidate(grid = ['  ', '  ', '  ', '  ']) == 29
    assert candidate(grid = ['     ', '     ', '     ', '     ', '     ']) == 1
    assert candidate(grid = ['/\\', '\\/', ' / ', '/\\', '\\/']) == 58
    assert candidate(grid = ['/\\/', '\\\\', '/\\/', '////']) == 21
    assert candidate(grid = ['    ', '    ', '    ', '    ']) == 1
    assert candidate(grid = [' / ', '/\\/', ' / ']) == 4
    assert candidate(grid = ['\\ ', '/ ', '\\ ', '/ ']) == 31
    assert candidate(grid = ['/\\/', '/\\/', '/\\/']) == 6
    assert candidate(grid = ['   ', '\\/', '   ']) == 4
    assert candidate(grid = ['\\/\\', '/\\/\\', '\\/\\', '/\\/\\']) == 17
    assert candidate(grid = ['\\ ', ' / ', ' / ', '\\ ']) == 21
    assert candidate(grid = ['   ', '   ', '   ']) == 1
    assert candidate(grid = ['\\/', '/\\', '\\/', '/\\']) == 35
    assert candidate(grid = [' /\\', '/\\ ', '\\/ ', ' \\ /']) == 15
    assert candidate(grid = ['///', '   ', '\\\\', '///']) == 20
    assert candidate(grid = ['////', '////', '////', '////']) == 8
    assert candidate(grid = ['/\\ ', ' \\ ', '/\\ ', ' \\ ']) == 14
    assert candidate(grid = ['\\ \\/', '/ \\/', '\\ /', '/\\ ']) == 11
    assert candidate(grid = ['/ /', ' \\ ', '/ /', ' \\ ']) == 14
    assert candidate(grid = ['/\\/\\', '\\/\\/\\', '/\\/\\/', '\\/\\/\\', '/\\/\\']) == 22
    assert candidate(grid = ['\\/', '/\\', '\\/']) == 15
    assert candidate(grid = ['  /', ' //', '///', '/\\']) == 20
    assert candidate(grid = ['\\', '\\', '\\']) == 25
    assert candidate(grid = ['/// ', '\\\\', '\\\\']) == 10
    assert candidate(grid = ['\\/\\', '\\/\\', '\\/\\', '\\/\\']) == 19
    assert candidate(grid = ['\\/\\', '\\/\\', '\\/\\']) == 6
    assert candidate(grid = [' /', '\\', ' ']) == 19
    assert candidate(grid = ['\\ ', '/ ', ' \\/', '/\\']) == 27
    assert candidate(grid = ['\\\\', '\\\\', '\\\\', '\\\\']) == 34
    assert candidate(grid = ['\\/\\', '/\\/\\', '\\/\\', '/\\/\\']) == 17
    assert candidate(grid = ['///', '///', '   ']) == 3
    assert candidate(grid = ['/\\\\', '\\/\\\\', '/\\\\', '\\/\\\\']) == 16
    assert candidate(grid = ['/\\/', '\\/\\', '/\\/', '\\/\\']) == 22
    assert candidate(grid = ['/\\ ', ' /\\ ', ' \\/\\', ' \\/ ']) == 7
    assert candidate(grid = ['\\\\ ', '\\\\ ', '\\\\ ', '\\\\ ', '\\\\ ']) == 38
    assert candidate(grid = ['\\/', '/\\', '\\/', '/\\']) == 35
    assert candidate(grid = ['\\\\', '////', '\\\\', '////']) == 22
    assert candidate(grid = [' //', '\\/', '  ']) == 8
    assert candidate(grid = ['/\\/', '\\///', '/\\/', '\\///']) == 16
    assert candidate(grid = [' /\\', '\\/ ', ' /\\', '\\/ ']) == 15
    assert candidate(grid = ['\\ ', '/\\', ' / ']) == 10
    assert candidate(grid = ['\\\\', '\\\\', '\\\\', '\\\\']) == 34
    assert candidate(grid = ['/\\/', '\\/\\', '\\/\\', '/\\/']) == 21
    assert candidate(grid = ['/\\/', '/\\/', '/\\/', '/\\/']) == 19
    assert candidate(grid = ['\\\\', '/\\/', '\\/\\', '/\\/']) == 25
    assert candidate(grid = ['\\\\', '\\\\', '\\\\', '    ']) == 25
    assert candidate(grid = [' \\/ ', '/\\/', ' \\/ ', '\\/ ']) == 9
    assert candidate(grid = ['\\\\', '\\ ', ' / ', '\\\\']) == 27
    assert candidate(grid = ['\\\\\\', '\\\\\\', '\\\\\\', '\\\\\\']) == 19
    assert candidate(grid = ['/\\/', ' / ', '\\/\\']) == 5
    assert candidate(grid = ['\\/\\', ' / ', '\\/\\', ' / ', '\\/\\']) == 41
    assert candidate(grid = ['\\\\', '///', '\\\\', '///']) == 27
    assert candidate(grid = ['\\/\\/', '\\/\\/', '\\/\\/', '\\/\\/']) == 8
    assert candidate(grid = ['/\\', '\\/', '/\\', '\\/']) == 36
    assert candidate(grid = ['/\\/', '\\/\\', '/\\/']) == 8
    assert candidate(grid = ['\\\\', '\\\\', '\\\\', '\\\\', '\\\\']) == 62
    assert candidate(grid = ['\\\\', '    ', '    ', '\\\\']) == 15
    assert candidate(grid = ['/ /', ' / ', ' / ', '/ /']) == 15
    assert candidate(grid = ['\\/\\', '/\\/', '\\/\\', '/\\/', '\\/\\']) == 47
