
import sys
import numpy as np

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

while True:
    try: 
        wordList = np.genfromtxt(sys.argv[0], dtype= 'char', comments='#', delimiter=None)
    except Exception as e:
        print(e)



