# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(head = list_node([1, 2])) == False
    assert candidate(head = list_node([1])) == False
    assert candidate(head = list_node([])) == False
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])) == False
    assert candidate(head = list_node([3, 2, 0, -4])) == False
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == False
