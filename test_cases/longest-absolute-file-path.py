# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
    assert candidate(input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
    assert candidate(input = "a") == 0
    assert candidate(input = "file1.txt\nfile2.txt\nlongfile.txt") == 12
