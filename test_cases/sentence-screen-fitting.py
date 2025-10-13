# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(sentence = ['abcde', 'fghij'],rows = 1,cols = 9) == 0
    assert candidate(sentence = ['hello', 'world'],rows = 2,cols = 8) == 1
    assert candidate(sentence = ['try', 'to', 'be', 'better'],rows = 10,cols = 20) == 10
    assert candidate(sentence = ['a', 'bcd', 'e'],rows = 3,cols = 6) == 2
    assert candidate(sentence = ['abc', 'de', 'fgh'],rows = 5,cols = 15) == 6
    assert candidate(sentence = ['try', 'to', 'be', 'better'],rows = 10,cols = 15) == 7
    assert candidate(sentence = ['try', 'to', 'beat', 'the', 'longest', 'word'],rows = 10,cols = 9) == 2
    assert candidate(sentence = ['i', 'had', 'apple', 'pie'],rows = 4,cols = 5) == 1
    assert candidate(sentence = ['a'],rows = 5,cols = 10) == 25
    assert candidate(sentence = ['try', 'to', 'be', 'better'],rows = 10,cols = 9) == 5
    assert candidate(sentence = ['a'],rows = 1,cols = 100) == 50
    assert candidate(sentence = ['f', 'p', 'a'],rows = 8,cols = 7) == 10
    assert candidate(sentence = ['a'],rows = 10000,cols = 10000) == 50000000
    assert candidate(sentence = ['small', 'words', 'here', 'and', 'there'],rows = 50,cols = 10) == 16
    assert candidate(sentence = ['averylongwordthatshouldntfit', 'but', 'it', 'will', 'because', 'cols', 'is', 'large'],rows = 20,cols = 50) == 13
    assert candidate(sentence = ['repeat', 'me'],rows = 25,cols = 7) == 12
    assert candidate(sentence = ['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 5,cols = 16) == 1
    assert candidate(sentence = ['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 7,cols = 15) == 2
    assert candidate(sentence = ['small', 'words', 'are', 'easier'],rows = 8,cols = 7) == 2
    assert candidate(sentence = ['this', 'is', 'a', 'test', 'sentence', 'that', 'is', 'quite', 'long'],rows = 8,cols = 12) == 1
    assert candidate(sentence = ['tiny', 'words', 'here'],rows = 100,cols = 5) == 33
    assert candidate(sentence = ['this', 'is', 'a', 'test', 'sentence'],rows = 100,cols = 50) == 200
    assert candidate(sentence = ['very', 'long', 'wordhere', 'and', 'anotherlongword'],rows = 15,cols = 20) == 7
    assert candidate(sentence = ['programming', 'is', 'fun'],rows = 8,cols = 11) == 4
    assert candidate(sentence = ['short', 'longword', 'medium'],rows = 15,cols = 25) == 15
    assert candidate(sentence = ['a'],rows = 1000,cols = 1) == 1000
    assert candidate(sentence = ['this', 'is', 'a', 'simple', 'test', 'case', 'for', 'the', 'problem', 'statement'],rows = 20,cols = 18) == 6
    assert candidate(sentence = ['short', 'words'],rows = 20,cols = 10) == 10
    assert candidate(sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g'],rows = 10,cols = 5) == 4
    assert candidate(sentence = ['x'],rows = 10000,cols = 1) == 10000
    assert candidate(sentence = ['this', 'is', 'a', 'test', 'sentence'],rows = 100,cols = 20) == 75
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 50,cols = 30) == 29
    assert candidate(sentence = ['quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 10,cols = 16) == 3
    assert candidate(sentence = ['abc', 'defg', 'hijkl', 'mnop', 'qrstu', 'vwxyz'],rows = 12,cols = 15) == 5
    assert candidate(sentence = ['this', 'is', 'a', 'test'],rows = 10,cols = 20) == 13
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 2000,cols = 10) == 399
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six'],rows = 5,cols = 25) == 4
    assert candidate(sentence = ['example', 'of', 'a', 'longer', 'sentence'],rows = 50,cols = 30) == 50
    assert candidate(sentence = ['this', 'is', 'an', 'example'],rows = 5,cols = 15) == 3
    assert candidate(sentence = ['leetcode', 'beyond', 'challenge'],rows = 7,cols = 10) == 2
    assert candidate(sentence = ['word', 'wordword', 'wordwordword'],rows = 1000,cols = 500) == 18500
    assert candidate(sentence = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 10,cols = 18) == 4
    assert candidate(sentence = ['example', 'sentence', 'that', 'repeats', 'itself', 'many', 'times'],rows = 30,cols = 40) == 24
    assert candidate(sentence = ['abcd', 'efgh', 'ijkl', 'mnop'],rows = 10,cols = 10) == 5
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five'],rows = 15,cols = 9) == 5
    assert candidate(sentence = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],rows = 25,cols = 20) == 14
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 30,cols = 15) == 8
    assert candidate(sentence = ['this', 'is', 'a', 'test'],rows = 20,cols = 10) == 13
    assert candidate(sentence = ['repeat', 'this', 'sentence', 'many', 'times'],rows = 15,cols = 14) == 6
    assert candidate(sentence = ['equal', 'length', 'words'],rows = 12,cols = 15) == 8
    assert candidate(sentence = ['short', 'words'],rows = 5000,cols = 10) == 2500
    assert candidate(sentence = ['hello', 'world'],rows = 10000,cols = 5000) == 4165000
    assert candidate(sentence = ['very', 'very', 'long', 'sentence', 'that', 'should', 'fit', 'nicely'],rows = 200,cols = 30) == 120
    assert candidate(sentence = ['short', 'words', 'only'],rows = 5,cols = 3) == 0
    assert candidate(sentence = ['averylongwordindeed'],rows = 10,cols = 20) == 10
    assert candidate(sentence = ['programming', 'is', 'fun'],rows = 20,cols = 12) == 10
    assert candidate(sentence = ['a', 'very', 'very', 'very', 'long', 'wordthat', 'cant', 'fit', 'in', 'one', 'row'],rows = 10,cols = 5) == 0
    assert candidate(sentence = ['short', 'words', 'only'],rows = 50,cols = 10) == 25
    assert candidate(sentence = ['short', 'words', 'only'],rows = 10000,cols = 5) == 3333
    assert candidate(sentence = ['longerwordhere', 'anotherlongword', 'and', 'short'],rows = 10,cols = 25) == 5
    assert candidate(sentence = ['short', 'words', 'only'],rows = 25,cols = 5) == 8
    assert candidate(sentence = ['repeat', 'this', 'sentence', 'many', 'times'],rows = 200,cols = 25) == 133
    assert candidate(sentence = ['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 50,cols = 20) == 24
    assert candidate(sentence = ['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 5,cols = 25) == 2
    assert candidate(sentence = ['optimize', 'for', 'performance'],rows = 5000,cols = 50) == 10000
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 6,cols = 30) == 3
    assert candidate(sentence = ['hello', 'world'],rows = 5000,cols = 15) == 5000
    assert candidate(sentence = ['one', 'two'],rows = 1,cols = 5) == 0
    assert candidate(sentence = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'],rows = 15,cols = 10) == 4
    assert candidate(sentence = ['abcdefghij'],rows = 1000,cols = 10) == 1000
    assert candidate(sentence = ['a', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'a'],rows = 15,cols = 20) == 6
    assert candidate(sentence = ['small', 'words', 'make', 'it', 'easier'],rows = 150,cols = 10) == 50
    assert candidate(sentence = ['a', 'bb', 'ccc', 'dddd'],rows = 20,cols = 8) == 10
    assert candidate(sentence = ['variable', 'lengths', 'of', 'words', 'here'],rows = 8,cols = 20) == 4
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'],rows = 12,cols = 30) == 10
    assert candidate(sentence = ['short', 'words'],rows = 1000,cols = 5) == 500
    assert candidate(sentence = ['hello', 'world', 'this', 'is', 'great'],rows = 15,cols = 10) == 5
    assert candidate(sentence = ['small', 'words', 'fit', 'easily'],rows = 20,cols = 8) == 5
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 20,cols = 30) == 11
    assert candidate(sentence = ['verylongword', 'anotherlongword', 'short'],rows = 10,cols = 20) == 4
    assert candidate(sentence = ['programming', 'is', 'fun'],rows = 10,cols = 12) == 5
    assert candidate(sentence = ['alibaba', 'cloud', 'is', 'amazing'],rows = 12,cols = 16) == 8
    assert candidate(sentence = ['even', 'longer', 'words', 'here', 'indeed'],rows = 500,cols = 20) == 300
    assert candidate(sentence = ['fit', 'this', 'sentence', 'perfectly', 'in', 'one', 'line'],rows = 5,cols = 27) == 3
    assert candidate(sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],rows = 20,cols = 30) == 11
    assert candidate(sentence = ['this', 'is', 'an', 'example', 'of', 'a', 'longer', 'sentence', 'that', 'will', 'wrap', 'around', 'multiple', 'times'],rows = 25,cols = 40) == 12
    assert candidate(sentence = ['complexity', 'in', 'programming', 'is', 'inherent'],rows = 25,cols = 30) == 16
    assert candidate(sentence = ['equal', 'equal', 'equal', 'equal', 'equal', 'equal'],rows = 30,cols = 15) == 10
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six'],rows = 10,cols = 20) == 6
    assert candidate(sentence = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],rows = 5,cols = 10) == 0
    assert candidate(sentence = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],rows = 7,cols = 9) == 1
    assert candidate(sentence = ['leetcode', 'offers', 'good', 'salaries'],rows = 5,cols = 30) == 5
    assert candidate(sentence = ['short', 'words'],rows = 10000,cols = 20) == 15000
    assert candidate(sentence = ['quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 12,cols = 18) == 4
    assert candidate(sentence = ['tiny', 'word'],rows = 1000,cols = 5) == 500
    assert candidate(sentence = ['fill', 'the', 'screen', 'with', 'these', 'words'],rows = 9,cols = 11) == 3
    assert candidate(sentence = ['repeated', 'word', 'repeated', 'word', 'repeated', 'word'],rows = 30,cols = 25) == 15
    assert candidate(sentence = ['python', 'programming', 'is', 'fun'],rows = 7,cols = 18) == 4
    assert candidate(sentence = ['this', 'is', 'a', 'test'],rows = 100,cols = 20) == 133
    assert candidate(sentence = ['equal', 'words', 'size'],rows = 50,cols = 13) == 33
    assert candidate(sentence = ['longerwordsinthelist'],rows = 100,cols = 15) == 0
    assert candidate(sentence = ['programming', 'is', 'fun'],rows = 15,cols = 20) == 15
    assert candidate(sentence = ['quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'],rows = 5,cols = 20) == 2
    assert candidate(sentence = ['abcd', 'efgh', 'ijkl', 'mnop'],rows = 100,cols = 8) == 25
    assert candidate(sentence = ['repeated', 'sentence', 'test'],rows = 30,cols = 12) == 10
    assert candidate(sentence = ['repeat', 'this', 'sentence', 'many', 'times'],rows = 50,cols = 25) == 33
    assert candidate(sentence = ['repeated', 'repeated', 'repeated'],rows = 100,cols = 5) == 0
    assert candidate(sentence = ['this', 'is', 'a', 'longer', 'sentence', 'to', 'fit'],rows = 10,cols = 20) == 5
    assert candidate(sentence = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz'],rows = 25,cols = 15) == 11
    assert candidate(sentence = ['programming', 'problems', 'are', 'fun'],rows = 20,cols = 50) == 33
    assert candidate(sentence = ['tiny'],rows = 10000,cols = 10000) == 20000000
    assert candidate(sentence = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],rows = 10,cols = 10) == 5
    assert candidate(sentence = ['tiny', 'words'],rows = 20000,cols = 100) == 180000
