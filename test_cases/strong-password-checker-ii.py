# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(password = "IloveLe3tcode!") == True
    assert candidate(password = "Me+You--IsMyDream") == False
    assert candidate(password = "1aB!") == False
