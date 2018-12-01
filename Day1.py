#Day 1.  Simple counting of frequencies.
#%%
#Import helper files
from norvigHelper import *
#import re

def parse(text):
    "Return a list of (turn, distance) pairs from text of form 'R2, L42, ...'"
    turns = dict(P='+', M='-')
    return [(turns[PM], int(d))
            # Search for '+' or '-' followed by a number.
           for (PM, d) in re.findall(r'(-|\+)(\d+)', text)]


"""
Sum 'Frequencies' to get total.
"""
def myParse(text):
    nums = []
    sum = 0
    for line in text:
        val = int(line[1:])
        if '+' not in line:
            val = val * -1
        nums.append(val)
        sum += val

    return (nums, sum)

"""
Get the first duplicate 'frequency'
"""
def myParse2(text, numDict, sum):
    for line in text:
        val = int(line[1:])
        if '+' not in line:
            val = val * -1
        sum += val
        if sum in numDict:
            #Found it.  Lets go home!
            return (False, sum, numDict)
        else:
            #First time seen, add to dict.
            numDict[sum] = 1
    
    # Didn't find the duplicate yet, let them know to keep searching.
    return(True, sum, numDict)

"""
For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Samples.
+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
"""

(numList,freqSum)  = myParse(Input(1).readlines())

numDict = {}
numDict[0] = 1
dupFreq = 0
notFound = True

while (notFound):
    (notFound, dupFreq, numDict) = \
    myParse2(Input(1).readlines(), numDict, dupFreq)
print('Frequency Sum for Part 1:' + str(freqSum))
print('First duplicate Freq: ' + str(dupFreq))