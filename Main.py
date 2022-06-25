
from ast import Break
import sys
# import numpy as np
from collections import defaultdict

from cv2 import sort

def load_words(filename:str) -> list:
    with open(filename,'r') as f:
        return [ line.strip() for line in f ]

print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))
x = 0
while x == 0:    
    try: 
        fileName:str = sys.argv[1]
        wordList = load_words(fileName)
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
        word:str = sys.argv[2]  
    except Exception as e:
        # print(e)
        fileName:str = input('please enter the name of a file in the current directory containing the word list: ')
        wordList = load_words(fileName)
        word:str = input('please enter the word to find anagrams and sub anagrams for: ')
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
anagrams:int = 0
sortedWord:str = sorted(word)           
for item in wordList:
    sortedItem = sorted(item)
    j:int = 0
    for i in range(min(len(item),len(word))):
        print(i)
        if sortedItem[i] == sortedWord[i]:
            j+=1
        else:
            Break
    if j==len(item):
        anagrams+=1           
print(f"The number of anagrams and sub anagrams are: {anagrams}")

# getting a list of words and a single string as a arguments
# print(wordList)
