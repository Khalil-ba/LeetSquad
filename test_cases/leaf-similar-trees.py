# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(root1 = tree_node([1, 2, 3]),root2 = tree_node([1, 3, 2])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])) == True
    assert candidate(root1 = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, None, None, None, None, None]),root2 = tree_node([5, 3, 8, 1, 4, 7, 9, None, 2, 6, None, None, None, None, None, None, None])) == True
    assert candidate(root1 = tree_node([5, 1, 4, None, 2, None, 3]),root2 = tree_node([5, 1, 3, None, 2, None, 4])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, 8]),root2 = tree_node([1, 2, 3, 4, 5, 7, 6, None, None, None, None, None, 8])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15])) == True
    assert candidate(root1 = tree_node([5, 1, 5, 5, None, 5, None, 5, 5, None, 5]),root2 = tree_node([5, 5, 1, None, 5, 5, None, 5, 5, None, 5])) == True
    assert candidate(root1 = tree_node([1, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, 2, None, 4, None, 3, None, 5])) == True
    assert candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, 2, 3, 4, 5])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, None, 5, None, None, 6]),root2 = tree_node([1, 2, 3, None, 5, 4, None, None, None, 6])) == False
    assert candidate(root1 = tree_node([4, 3, None, 1, 2]),root2 = tree_node([4, 3, None, 2, 1])) == False
    assert candidate(root1 = tree_node([1, 2, 3, None, None, None, 4]),root2 = tree_node([1, 2, 3, None, 4])) == False
    assert candidate(root1 = tree_node([4, 2, 7, 1, 3, 6, 9]),root2 = tree_node([4, 2, 7, 1, 3, 9, 6])) == False
    assert candidate(root1 = tree_node([5, 3, 8, 1, 4, None, 9, None, None, 2, 6, None, None, None, None, None, 7]),root2 = tree_node([5, 3, 8, 1, None, None, 9, None, 4, None, 7, None, None, 2, 6])) == False
    assert candidate(root1 = tree_node([5, 4, 6, 3, 8, 7, 9, 2, None, None, None, None, None, None, 1]),root2 = tree_node([5, 4, 7, 3, 8, 6, 9, 2, None, None, None, None, None, None, 1])) == False
    assert candidate(root1 = tree_node([2, 1, 4, None, None, 3, 6]),root2 = tree_node([2, 1, 6, None, None, 3, 4])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21])) == False
    assert candidate(root1 = tree_node([15, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),root2 = tree_node([15, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8, 9, 10, 11, 12, None, None, 13, 14, 15, 16]),root2 = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, None, 11, 8, 9, 10, None, None, None, 12, 13, 14, 15, 16])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11]),root2 = tree_node([3, 5, 1, 6, 10, 11, 2, None, None, None, None, None, 7, 4, 9, 8])) == False
    assert candidate(root1 = tree_node([8, 5, 9, 3, 7, None, None, 1, 4, 6, None]),root2 = tree_node([8, 5, 9, 3, 7, None, None, 1, None, 4, 6])) == True
    assert candidate(root1 = tree_node([5, 1, 9, None, 4, 3, None, 7, 6, None, 8, None, None, 2, None]),root2 = tree_node([9, 5, 1, 3, 4, None, None, 2, 6, None, 7, None, None, None, 8])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, 10]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, None, 9, None, None, None, None, 10])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),root2 = tree_node([1, 2, 3, 4, None, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 19])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, 16, 17, 18, 19, 20]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == True
    assert candidate(root1 = tree_node([7, 13, 10, 1, 2, None, 5, None, None, None, None, None, 4]),root2 = tree_node([10, 13, 5, 1, None, 2, 4, 7])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18])) == True
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 11, 12]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8, None, None, 11, 12])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9]),root2 = tree_node([1, 3, 2, 6, 7, 4, 5, None, None, None, None, 8, 9])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, 9, 10, None, None, 11, 12]),root2 = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, None, 8, 9, 10, None, None, 11, 13])) == False
    assert candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == False
    assert candidate(root1 = tree_node([2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, 10]),root2 = tree_node([2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, 10, None])) == False
    assert candidate(root1 = tree_node([10, 5, 15, None, None, 6, 20]),root2 = tree_node([10, 5, 15, None, None, 20, 6])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, 10, 11, 12, 13, None, None, None, None, None, None, 9, 8])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, None, None, 11]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8, 11, 10])) == False
    assert candidate(root1 = tree_node([5, None, 3, None, 4, None, 6]),root2 = tree_node([5, None, 3, None, 4, None, 7])) == False
    assert candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5]),root2 = tree_node([5, 4, 3, 2, 1])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18, 19]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18, 19])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9]),root2 = tree_node([1, 2, 3, 4, 5, None, None, 9, 8, None, None, 7, 6])) == False
    assert candidate(root1 = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185]),root2 = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185])) == True
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),root2 = tree_node([5, 1, 5, 6, 2, 9, 8, None, None, 7, 4])) == True
    assert candidate(root1 = tree_node([1]),root2 = tree_node([1])) == True
    assert candidate(root1 = tree_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]),root2 = tree_node([5, 15, 10, 25, 20, 35, 30, 55, 50, 65, 60, 75, 70, 45, 40])) == False
    assert candidate(root1 = tree_node([5, 1, 4, None, None, 3, 6]),root2 = tree_node([5, 1, 4, None, None, 3, None, None, 6])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, None, 6, 7, None, 8, 9, 10, None, None, 11, 12]),root2 = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, None, None, 11, 12])) == False
    assert candidate(root1 = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7])) == True
    assert candidate(root1 = tree_node([4, 10, None, 3, 2]),root2 = tree_node([4, 10, None, 3, None, None, 2])) == False
    assert candidate(root1 = tree_node([1, 2, 3, None, 4, None, 5, None, 6]),root2 = tree_node([1, 2, 3, None, 4, None, 5, None, 6])) == True
    assert candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6]),root2 = tree_node([6, 5, 4, 3, 2, 1])) == False
    assert candidate(root1 = tree_node([10, 5, 6, None, None, 3, 7, None, None, None, 4]),root2 = tree_node([10, 5, 6, None, None, 3, None, None, 4, None, 7])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == True
    assert candidate(root1 = tree_node([4, 2, 6, 1, 3, 5, 7]),root2 = tree_node([4, 2, 6, 1, None, 5, None, 3, None, 7])) == False
    assert candidate(root1 = tree_node([7, 5, 6, 1, 4, 3, 2, None, None, None, None, None, None, 8, 9]),root2 = tree_node([7, 5, 6, 1, 4, 3, None, 8, 9, None, None, 2])) == False
    assert candidate(root1 = tree_node([1, 2, 3, None, 4, 5, 6, 7, 8, 9, 10, 11, 12]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == False
    assert candidate(root1 = tree_node([4, 2, 6, 1, 3, 5, 7]),root2 = tree_node([4, 1, 6, None, 2, 5, 7])) == False
    assert candidate(root1 = tree_node([1, 2, None, 3, 4, 5, 6, 7, 8, 9, 10]),root2 = tree_node([1, 2, None, 3, 10, 4, 5, 6, 7, 8, 9])) == False
    assert candidate(root1 = tree_node([1, 2, None, 3, None, 4, None, 5]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5])) == True
    assert candidate(root1 = tree_node([10, 20, 30, 40, 50, 60, 70, None, 80, 90, 100, 110, 120, 130, 140]),root2 = tree_node([10, 20, 30, 40, 50, 60, 70, None, 80, 90, 100, 110, 120, 130, 140])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == True
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 11, 12]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8, 11, 12])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == True
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17])) == True
    assert candidate(root1 = tree_node([8, 3, 5, 6, 7, 9, 2, 10, None, None, 1, None, None, None, None, 11]),root2 = tree_node([8, 3, 5, 6, 7, 9, 2, None, None, None, None, None, None, 10, 11])) == False
    assert candidate(root1 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7]),root2 = tree_node([7, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18, 19, 20]),root2 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11, 12, 13, 14, 15, None, None, None, None, 16, None, None, 17, None, None, None, 18, 19, 20])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, None, None, 5, 6, 7, 8, 9]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9])) == False
    assert candidate(root1 = tree_node([2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),root2 = tree_node([2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])) == True
    assert candidate(root1 = tree_node([2, 1, None, 3]),root2 = tree_node([2, None, 1, None, 3])) == True
    assert candidate(root1 = tree_node([1, 2, None, 3, 4, None, 5, 6, None, 7]),root2 = tree_node([1, 2, None, 3, 4, None, 5, 6, None, 7])) == True
    assert candidate(root1 = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, None, None, 11, 14, None, None, None, None, None]),root2 = tree_node([10, 5, 15, 3, 7, None, 18, 1, 4, None, 13, None, None, 11, 14])) == False
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),root2 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 29])) == False
    assert candidate(root1 = tree_node([10, 5, 15, 3, 7, None, 18]),root2 = tree_node([10, 5, 15, None, 7, 18, None, 3])) == False
    assert candidate(root1 = tree_node([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4, 10, 11]),root2 = tree_node([3, 5, 1, 6, 7, 4, 2, 10, 11, None, None, None, None, None, None, 9, 8])) == False
    assert candidate(root1 = tree_node([1, 2, None, 3, 4]),root2 = tree_node([1, None, 2, 3, 4])) == True
    assert candidate(root1 = tree_node([8, 6, 7, None, 5, None, 4, None, 3, None, 2, None, 1]),root2 = tree_node([8, 7, 6, None, 5, None, 4, None, 3, None, 2, None, 1])) == True
    assert candidate(root1 = tree_node([10, 5, 15, 3, 7, None, 18]),root2 = tree_node([10, 15, 5, 18, None, 3, 7])) == False
    assert candidate(root1 = tree_node([3, 9, 20, None, None, 15, 7]),root2 = tree_node([3, 9, 20, None, None, 15, 7])) == True
    assert candidate(root1 = tree_node([2, 3, None, 1]),root2 = tree_node([2, 1, None, 3])) == False
    assert candidate(root1 = tree_node([1, 2, None, 3, None, 4, None, 5, None]),root2 = tree_node([1, 2, None, 3, None, 5, None, 4, None])) == False
    assert candidate(root1 = tree_node([4, 2, 7, 1, 3, 6, 9]),root2 = tree_node([4, 2, 7, 3, 1, 9, 6])) == False
    assert candidate(root1 = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),root2 = tree_node([10, 5, 15, 3, 6, 7, None, 1, None, 13, 18])) == False
    assert candidate(root1 = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),root2 = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])) == False
    assert candidate(root1 = tree_node([10, 5, 15, 3, 7, 13, 18, 1, 4, 6, 8, 12, 14, 17, 19]),root2 = tree_node([10, 5, 15, 1, 4, 3, 7, 6, 8, 13, 18, 12, 14, 17, 19])) == False
    assert candidate(root1 = tree_node([4, 7, 11, 5, 8, 14, None, None, None, None, 2, None, 9, 1, 12, None, None, None, 6, 10, 13, None, None, None, None, None, None, None, None, 3]),root2 = tree_node([4, 7, 11, 5, 8, 14, None, None, None, None, 3, None, 9, 1, 12, None, None, None, 6, 10, 13, None, None, None, None, None, None, None, None, 2])) == True
    assert candidate(root1 = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),root2 = tree_node([1, 3, 2, 6, 7, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8])) == False
