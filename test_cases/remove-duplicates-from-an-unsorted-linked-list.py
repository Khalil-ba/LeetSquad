# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(head = list_node([2, 1, 1, 2])) == None
    assert is_same_list(candidate(head = list_node([5, 6, 7, 8, 9])), list_node([5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert candidate(head = list_node([5, 4, 3, 2, 1, 1, 2, 3, 4, 5])) == None
    assert is_same_list(candidate(head = list_node([3, 2, 2, 1, 3, 2, 4])), list_node([1, 4]))
    assert candidate(head = list_node([1, 1, 1, 1, 1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2])), list_node([1, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5])), list_node([6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])) == None
    assert candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 100000, 99999, 99998, 99997, 99996, 99995])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([100000, 99999, 100000, 99999, 100000])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])) == None
    assert candidate(head = list_node([100000, 99999, 100000, 99999, 1, 1, 2, 2, 3, 3])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50])) == None
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 2, 3, 4, 5])), list_node([1]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == None
    assert is_same_list(candidate(head = list_node([1, 2])), list_node([1, 2]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert candidate(head = list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])) == None
    assert candidate(head = list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 11, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 19])), list_node([1, 3, 4, 6, 7, 8, 10, 12, 13, 15, 16, 17, 18]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3])), list_node([4, 5, 6, 7, 8, 9, 10]))
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == None
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7])), list_node([1]))
    assert is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 15, 14, 13, 12, 11])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([5, 6, 7, 5, 8, 6, 9, 10, 7])), list_node([8, 9, 10]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970])), list_node([99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970]))
    assert is_same_list(candidate(head = list_node([100000, 100000, 100000, 99999, 99999, 99998])), list_node([99998]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6])) == None
    assert is_same_list(candidate(head = list_node([5, 5, 4, 3, 2, 1, 2, 3, 4, 5])), list_node([1]))
    assert candidate(head = list_node([100000, 99999, 100000, 99999, 100000, 99999])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([6, 7, 8, 9, 10]))
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert is_same_list(candidate(head = list_node([5, 5, 6, 7, 8, 6, 9, 10, 7, 11])), list_node([8, 9, 10, 11]))
    assert candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5])) == None
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 2, 3, 4, 5])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2])), list_node([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 50000, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 4, 5, 4, 6, 5, 7, 8, 9, 8, 10, 9])), list_node([3, 6, 7, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])) == None
    assert is_same_list(candidate(head = list_node([100000, 99999, 100000, 99999, 99998])), list_node([99998]))
    assert candidate(head = list_node([100000, 1, 2, 3, 4, 5, 100000, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10])) == None
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 4, 5, 5, 5, 6])), list_node([1, 3, 6]))
    assert candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([5, 6, 7, 8, 9, 5, 6, 7, 8, 9])) == None
    assert candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])) == None
    assert is_same_list(candidate(head = list_node([5, 5, 4, 3, 4, 2, 5, 1, 2])), list_node([3, 1]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5])), list_node([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([16, 17, 18, 19, 20]))
    assert candidate(head = list_node([5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
    assert candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])) == None
