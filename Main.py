
from ast import Break
import sys
import numpy as np
# from collections import defaultdict

from cv2 import sort

def loadWords(filename:str) -> list:
    with open(filename,'r') as f:
        return [ line.strip() for line in f ]
def isAnagram(item:str,word:str,)->int:  
    i:int = 0
    j:int = 0
    while (i < len(word) and j < len(item)):  
        if word[i] == item[j]:
            i+=1
            j+=1
            continue
        elif word[i] < item[j]:
            i+=1
            continue
        elif word[i] > item[j]:
            break      
    if j == len(item):
        return 1      
    return 0
x = 0
while x == 0:    
    try: 
        fileName:str = sys.argv[1]
        wordList = loadWords(fileName)
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
        word:str = sys.argv[2]  
    except Exception:
        fileName:str = input('please enter the name of a file in the current directory containing the word list: ')
        wordList = loadWords(fileName)
        word:str = input('please enter the word to find anagrams and sub anagrams for: ')
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
anagrams:int = 0
sortedWord:str = sorted(word)       

for item in wordList:
    sortedItem = sorted(item)
    if len(item) == len(word):
        if sortedItem == sortedWord:
            print('matching word:',item)
            anagrams+=1
        else:
            continue
    #TO COMPLETE            
    # can do using dict for every letter associated with a number in the word for this as well.
    # or can do creating list of charecters and removing them after each letter is matched from the original word.
    # can also do using numpy, using np.where and replacing the matched letter with 0.
    elif len(word)>len(item):
        if isAnagram(sortedItem,sortedWord) == 1:
           print('matching word:',item)
           anagrams+=1
    else: 
        continue

print('size of the word list is: ',len(wordList))                  
print(f"The number of anagrams and sub anagrams are: {anagrams}")

# getting a list of words and a single string as a arguments

