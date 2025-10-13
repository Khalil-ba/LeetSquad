# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(nums = [0]) == [0]
    assert candidate(nums = [-1]) == [-1]
    assert candidate(nums = [50000]) == [50000]
    assert candidate(nums = [-50000]) == [-50000]
    assert candidate(nums = [1]) == [1]
