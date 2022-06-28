import sys
import numpy as np

def loadWords(filename:str) -> list:
    with open(filename,'r') as f:
        return [ line.strip() for line in f ]
def isAnagram(item:str,word:str,)->int:  
    """
    params: 
    word: string to find anagrams and sub anagrams for 
    item: string to check against
    return:
    int 0 if False, 1 if true 
    """
    i:int = 0
    j:int = 0
    if len(item) == len(word):
        if sortedItem == sortedWord:
            return 1 
    elif len(word)>len(item):
        while (i < len(word) and j < len(item)):  
            if word[i] == item[j]:
                i+=1
                j+=1
                continue
            elif word[i] < item[j]:
                i+=1
                continue
            elif word[i] > item[j]:
                # Since the two strings are sorted, if the next character in
                break      
        if j == len(item):
            return 1      
    return 0
x:int = 0
while x == 0:    
    try: 
        fileName:str = sys.argv[1]
        wordList:list = loadWords(fileName)
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
        word:str = sys.argv[2]  
    except Exception:
        fileName:str = input('please enter the name of a file in the current directory containing the word list: ')
        wordList:list = loadWords(fileName)
        word:str = input('please enter the word to find anagrams and sub anagrams for: ')
        if len(wordList) !=0 and len(word) != 0:
            x+=1 
anagrams:int = 0
sortedWord:str = sorted(word)       
for item in wordList:
    sortedItem:str = sorted(item)
    if len(item) == len(word) or len(word)>len(item):
        if isAnagram(sortedItem,sortedWord) == 1:
            print('matching word:',item)
            anagrams+=1
        else:
            continue
    else: 
        continue
print('size of the word list is: ',len(wordList))                  
print(f"The number of matching anagrams and sub anagrams are: {anagrams}")


