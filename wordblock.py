

# --- IMPORTS --- #

from open_dictionary import *



# --- MACROS --- #

Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# --- WORDBLOCK HELPERS --- #

# args: letter, char, must be an alphabet character; blockLength, int, must be a natural number
# return: filteredList, array, a list of unique words which start with the char 'letter' of length 'blockLength'
def filter_list(letter, blockLength):
    unfilteredList = find_wordslist(letter) # 'find_wordslist' retrieves all words starting with the char 'letter'
    filteredList = []
    for word in unfilteredList: # iterate over each word which starts with 'letter'
        if len(word) == blockLength and word not in filteredList: # filtered for length and preexistence of word in list
            filteredList.append(word)
    return filteredList




# args: blockLength, int, must be a natural number
# return: filteredDict, dictionary, where each key is an alphabetic char, and each value is a list
#         of all words which start with the key letter and are of length 'blockLength'
def get_filtered_dict(blockLength):
    filteredDict = {}
    for letter in Alphabet:
        filteredDict.update({letter: filter_list(letter, blockLength)})
    return filteredDict




# args: wordBlock, array, a 2-dimensional matrix of chars where the top-level array has the same
#       length as all bottom-level arrays. Visually, forms a square of chars
# return: boolean, TRUE if all rows and columns form a word found in the dictionary, FALSE if not
def is_valid_wordblock(wordBlock):
    tempStr = ""
    wordsList = []
    for i in range(len(wordBlock)):
        for j in range(len(wordBlock)): # append i-th letter of each wordBlock[j]
            tempStr += wordBlock[j][i]
        wordsList.append(tempStr)
        tempStr = "" # append full string and clear
    # check if all strings are valid words (the first loop is the baseWord, should always be valid
    for word in wordsList:
        if word not in wordsDictionary.get(word[0]):
            return False
    return True # we know that each word is in the dictionary




# args: wordBlock, array, a 2-dimensional matrix of chars where the top-level array has the same
#       length as all bottom-level arrays. Visually, forms a square of chars
# return: none, side-effect prints 'wordBlock' in console
def print_wordblock(wordBlock):
    for word in wordBlock: # print each 'word' element
        print(*word) # each 'word' is a list of characters that are unpacked and printed
    print() # newline




# args: iterWord, str, string of alphabetic chars; wordBlock, array, a 2-dimensional array of chars
# return: none, side-effect creates and prints all possible valid word blocks that contain 'iterWord'
def recursive_iter(iterWord, wordBlock):
    if not iterWord: # if iterWord is null, a full wordblock must have been created
        if is_valid_wordblock(wordBlock):
            print_wordblock(wordBlock)
    else:
        # a recursive call for each word in the list, with said word added to wordBlock as an arg
        for word in wordsDictionary.get(iterWord[0]):
            wordBlock.append(word)
            recursive_iter(iterWord[1:], wordBlock)
            wordBlock.pop() # pop off the appended word to be replaced with the next iterated word in the for-loop



# --- MAIN --- #


"""
ex word block:
b a b y
e y l e
e l u l
r e e k

beer: grain-based fermented alcohol
ayle: archaic term for grandfather
blue: color
yelk: archaic form of 'yolk'

baby: everyone knows what a baby is
eyle: archaic form of 'ail'
elul: month in the Hebrew calendar corresponding to August - September
reek: state of smelling badly
"""

wordsDictionary = {} # a global skips having to pass the dictionary as an argument, which seems prudent for recursive functions
                     # should NEVER be modified/written to outside of the main function

# args: baseWord, str, containing only lowercase alphabetic chars. Does not have to be a dictionary word,
#       could be a proper noun, like a first name.
# return: none, sets up and calls the function recursive_iter, which creates and prints all possible word blocks containing baseWord
def make_wordblock(baseWord):
    wordBlock = []
    blockLength = len(baseWord)
    global wordsDictionary # this global is only modified once, at the beginning of the main program
    wordsDictionary = get_filtered_dict(blockLength) # 
    recursive_iter(baseWord, wordBlock) # recursive_iter runs until all possible permutations of words have been exhausted








