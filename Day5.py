#%%
from Utils import Input, printHelper, re

def Parse(text):
    idx = 0
    data = list(text)
    while (idx < len(data) - 1):
        (idx, data) = checkNext(data, idx)
    return text

def checkNext(text, idx):
    if idx < len(text) - 1:
        otherChar = ''
        prevChar = text[idx]
        # Check to see if char is upper or lower
        if prevChar.isupper():
            otherChar = prevChar.lower()
        else:
            otherChar = prevChar.upper()

        # Compare with next character
        if text[idx + 1] == otherChar:
            # Found a match, note it.
            text[idx] = '!'
            text[idx +1] = '!'
            #print('Idx: {}'.format(idx))
            #idx += 1
            return (idx + 2, text)
        # else:
            # NO else because we only want to return the next index for no match  
    #Did not find a match, increment index and try again.
    print("Did not find a match.  Idx: {}".format(idx))
    return (idx + 1, text)
        
polymer = Parse(Input(5).read())
print(polymer)
print('Count {}'.format(re.findall('!', polymer)))