#
from Utils import Input, printHelper, re
"""
For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. 
Multiplying these together produces a checksum of 4 * 3 = 12.
"""
#%%
from Utils import Input, printHelper, re
def getCharCounts(line):
    hasAtLeast2 = 0
    hasAtLeast3 = 0
    charCount = {}

    for item in line.strip():
        if item in charCount:
            charCount[item] = charCount[item] + 1
        else:
            charCount[item] = 1


    """Now lets get the times 2 is in the list and 3 or more"""
    for _,v in charCount.items():
        if v >= 3:
            hasAtLeast3 = 1
        if v == 2:
            hasAtLeast2 = 1
        if hasAtLeast3 and hasAtLeast2:
            return (hasAtLeast2, hasAtLeast3)

    return (hasAtLeast2, hasAtLeast3)


def Parse(text):
    occurrences = {}
    occurrences[2] = 0
    occurrences[3] = 0
    for line in text:
        (two, three) = getCharCounts(line)
        occurrences[2] = occurrences[2] + two
        occurrences[3] = occurrences[3] + three
    return occurrences


occs = Parse(Input(2).readlines())
print('Day2a: {}'.format(occs[2] * occs[3]))

#%%
def compareForDiffs(a, b):
    s = ''
    #Zip is a handy way to handle two iterables at once.
    for x, y in zip(a, b):
        #If they two chars are the same, make a not and build up 
        # the answer string.
        if x == y:
            s += str(x)
    #Success condition is when the string is different by at most 1
    # char.  aka, the lengths are off by 1.
    if len(s) == (len(a) - 1):
        """ Found it return"""
        return (True, s)
    return (False, s)


def Parse2(text):
    count = 0
    offset = 1
    while (True):
        line1 = text[count].strip()
        line2 = text[count + offset].strip()
        (success, ans) = compareForDiffs(line1, line2)
        """Found the answer, return"""
        if (success):
            return ans

        """Increment our loop variables.  Handle rollover if needed."""
        offset += 1
        if ((count + offset) == len(text)):
            
            count += 1
            offset = 1

ans = Parse2(Input(2).readlines())
print('Dat2b: {}'.format(ans))