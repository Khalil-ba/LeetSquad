# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(head = list_node([0, 0, 0, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 0, 1, -1, 2])), list_node([1, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([10, 20, -30, 40, -50, 60, -10, -50])), list_node([40, -50]))
    assert candidate(head = list_node([1, -1, 1, -1])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, -3, 4])), list_node([1, 2, 4]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3])), list_node([3]))
    assert candidate(head = list_node([-1, 1, -1, 1, -1, 1])) == None
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert candidate(head = list_node([-1, 1, 0])) == None
    assert candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4])) == None
    assert is_same_list(candidate(head = list_node([1, 0, -1, 2])), list_node([2]))
    assert candidate(head = list_node([-1, 1])) == None
    assert is_same_list(candidate(head = list_node([10, 5, -5, 3, 2, -2])), list_node([10, 3]))
    assert candidate(head = list_node([-1, 1, -1, 1, -1, 1, -1, 1])) == None
    assert candidate(head = list_node([0])) == None
    assert candidate(head = list_node([0, 0, 0])) == None
    assert is_same_list(candidate(head = list_node([-1])), list_node([-1]))
    assert is_same_list(candidate(head = list_node([1, 2, -3, 3, 1])), list_node([3, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -3, -2])), list_node([1]))
    assert candidate(head = list_node([10, 5, 3, -3, -5, -10])) == None
    assert candidate(head = list_node([1, -1, 2, -2, 3, -3])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 0, 4, 0, -4])), list_node([1, 2, 3]))
    assert candidate(head = list_node([5, 6, 7, -7, -6, -5])) == None
    assert is_same_list(candidate(head = list_node([10, 20, -10, -10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, -28, 8, 9])), list_node([8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 1, 2, 3, 4])), list_node([1, 2, 3, 4]))
    assert candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, 5, -5])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -15, 5, 6, 7, 8, -30, 10, 11])), list_node([5, 6, 7, 8, -30, 10, 11]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, -5, -4, -3, -2, -1])) == None
    assert is_same_list(candidate(head = list_node([10, -5, -5, 3, 2, -2, 1, -1])), list_node([3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -6, 2, 3, 4, -9, 1, 2])), list_node([1, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -10, 1, 2, 3])), list_node([1, 2, 3, 2, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -2, -1, 1, 4])), list_node([1, 2, 1, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -6, 4, -4, 5, 0, -5, 6])), list_node([6]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, -21, 7, 8, 9, 10, -35, 11, 12])), list_node([7, 8, 9, 10, -35, 11, 12]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -6, 2, 3, 4, -9, 5])), list_node([5]))
    assert is_same_list(candidate(head = list_node([100, -50, -50, 200, 300, -500, 400, 500, -1000, 600])), list_node([400, 500, -1000, 600]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 4, 5, -9])), list_node([1, 2, 3]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5])), list_node([5]))
    assert candidate(head = list_node([100, -50, -50, 25, -25, 50, -50, 25, -25, 100, -100])) == None
    assert is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30, 40])), list_node([40]))
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, -5, 5, -3, -2])), list_node([1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 1, 2, -3, 3, -2, 2])), list_node([3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -3, -2, -1, 4, -4, 5])), list_node([5]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5])), list_node([5]))
    assert candidate(head = list_node([1, -2, 3, -3, 2, -1, 4, -4, 5, -5])) == None
    assert candidate(head = list_node([0, 1, 2, 3, 0, -3, -2, -1, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 2, -3, 3, -2, 2, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([3]))
    assert is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30, 40])), list_node([40]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -120, 16])), list_node([16]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -5, 5, -6, 6, -7, 7, 8])), list_node([1, 2, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 5, 5, -5])), list_node([5]))
    assert candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1])) == None
    assert is_same_list(candidate(head = list_node([1, 0, -1, 0, 1, 0, -1, 0, 1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([5, 1, 4, -10, 20, -5, -15, 2, 3, 4, -9, 1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 5, 6, 7, 8, -30, 9, 10])), list_node([5, 10]))
    assert is_same_list(candidate(head = list_node([10, -2, 3, -1, 5, -3, 2, -2, 1, -1])), list_node([10, 5, -3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, -3, -5, -10, 20])), list_node([1, 2, 20]))
    assert candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9])) == None
    assert is_same_list(candidate(head = list_node([5, 3, -5, 2, -2, 1])), list_node([5, -2, 1]))
    assert is_same_list(candidate(head = list_node([5, 6, -6, 7, 8, -15, 9])), list_node([5, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, -21, 7, 8, 9, 10, -35, 1, 2, 3])), list_node([2, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 5, 5])), list_node([5, 5]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 6, 7, 8, -8, -7, -6])) == None
    assert is_same_list(candidate(head = list_node([5, 6, 7, -18, 19, 20, -39, 21, 22, 23, -65, 24])), list_node([21, 22, 23, -65, 24]))
    assert is_same_list(candidate(head = list_node([100, -50, -50, 200, -100, -100, 300, -200, -200, 400])), list_node([300]))
    assert candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, -21, 7, 8, 9])), list_node([7, 8, 9]))
    assert candidate(head = list_node([5, -5, 5, -5, 5, -5])) == None
    assert is_same_list(candidate(head = list_node([0, 0, 0, 1, 2, 3, -6, 7, 8, -15, 9])), list_node([9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 3, 4, 5, -12, 6, 7])), list_node([6, 7]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -15, 6, 7, 8, 9, 10, -33, 11, 12])), list_node([6, 7, 8, 9]))
    assert candidate(head = list_node([1, 2, 3, 4, -10, 2, 3, 4, 5, -14])) == None
    assert is_same_list(candidate(head = list_node([5, 0, 5, -5, 10, -10, 15, -15, 20])), list_node([5, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, -3, 4, -4, 5])), list_node([1, 2, 5]))
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 10, 1, 2, 3, 4, -10, 10])), list_node([10, 10]))
    assert candidate(head = list_node([0, 1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 5, 6, 7, 8, 9, 10, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -50])), list_node([5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1000, -500, -250, 250, -250, 500, -1000, 2000, -2000, 3000, -3000])), list_node([1000, -500, -250, 500, -1000]))
    assert is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25])), list_node([25]))
    assert is_same_list(candidate(head = list_node([1, 2, -3, 3, -2, 2, 1, -1])), list_node([3]))
    assert candidate(head = list_node([1, 2, 3, -6, 3, 2, 1, 0, -1, -2, -3, 0])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55, 11, 12, 13, 14, 15, 16])), list_node([11, 12, 13, 14, 15, 16]))
    assert is_same_list(candidate(head = list_node([5, 6, -11, 1, 2, 3, -5, -6, 7])), list_node([1, -6, 7]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, -45])) == None
    assert is_same_list(candidate(head = list_node([1, 0, 0, 0, 0, 0, 1])), list_node([1, 1]))
    assert is_same_list(candidate(head = list_node([5, 6, -11, 10, 5, -10])), list_node([10, 5, -10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -15, 6])), list_node([6]))
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert candidate(head = list_node([100, -50, 25, -25, -25, 25, -100, 50])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, -3, 4, 0, 5, -5, 6])), list_node([1, 2, 4, 6]))
    assert is_same_list(candidate(head = list_node([10, -3, 4, -3, 6, -6, 2])), list_node([10]))
    assert is_same_list(candidate(head = list_node([100, -50, 50, -50, 50, -50, 50, -50, 50, -50])), list_node([100, -50]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -55, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 0, -5, 0, 0, 0, 6, 7, 8, -20])), list_node([1, 2, 3, 4, 6, 7, 8, -20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 6, 7, 8, -24])), list_node([1, 2, 3, 4, 5, 6, 7, 8, -24]))
    assert candidate(head = list_node([7, 8, 9, -9, -8, -7, 10, -10, 11, 12, -12, -11])) == None
    assert is_same_list(candidate(head = list_node([10, 20, -10, -10, 30, 40, -70, 80])), list_node([10, 80]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 5, 5, -10])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, -45, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -190])), list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -190]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 1, 2, 3, 4, 5, -14, 0, 0])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 0, 0, 0, 4, 5, -9, 6, 7, -13])), list_node([1, 2, 3]))
    assert is_same_list(candidate(head = list_node([10, -5, 5, -10, 20, -10, 5])), list_node([20, -10, 5]))
    assert is_same_list(candidate(head = list_node([5, 6, 7, 8, -20, 3, 4, 5, 6, -18, 1, 2])), list_node([5, 6, 7, 6, -18, 1, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -45, 11, 12, 13, 14, 15, 16, -80])), list_node([1, 2, 3, 4, 11, 12, 13, 14, 15, 16, -80]))
    assert candidate(head = list_node([-1, 1, 1, -1, 1, -1, 1, 1, -1, -1])) == None
    assert candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, -10, 5, 6, 7, 8, 9, 10, -40, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, -15, 10])), list_node([10]))
    assert is_same_list(candidate(head = list_node([10, -5, -3, 2, 3, -2, 1, 2, -1, 0, 0, 0])), list_node([10, -5, 1, 2, -1]))
    assert is_same_list(candidate(head = list_node([10, 20, -10, -10, 30, 40, -50, 20])), list_node([10, 30, 40, -50, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -1, 0, 1, -1, 0])), list_node([1, 2, 3, 4, 5, -1]))
    assert candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, 5, -5])) == None
