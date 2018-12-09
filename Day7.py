#%%
from Utils import Input, printHelper, re

def Parse(text):
    instructions = {}
    allChars = set()
    for line in text:
        (chars) = re.findall(r'Step (\w) must be finished before step (\w) can begin', line)
        #(PreReq, NextStep)
        if chars[0][1] in instructions:
            instructions[chars[0][1]].append(chars[0][0])
        else:
            instructions[chars[0][1]] = [chars[0][0]]
        #Attempt to add both characters to a set so we know
        # Which characters are indeed steps.
        allChars.add(chars[0][0])
        allChars.add(chars[0][1])

    return (instructions, allChars)

def updateState(state, instructions):
    #Now we need to loop through our instructions and remove
    # Each 
    finishedStates = []
    keysToRemove = []
    for k, v in instructions.items():
        if state in v:
            v.remove(state)
        if state in v:
            print("We had {} in the instructions list twice for {}".format(state, item))
        # Check to see if we have an empty list, which means the
        # State can now be complete.
        if not v:
            finishedStates.append(k)
            #Remove this key in the dict.
            keysToRemove.append(k)

    for item in keysToRemove:
        del instructions[item]

    return (finishedStates, instructions)

(instructions, allChars) = Parse(Input(7).readlines())

def advanceState(instructions, stateComplete, sequence):
    state = stateComplete[0]
    stateComplete.remove(state)
    sequence.append(state)
    (completeStates, instructions) = updateState(state, instructions)

    for item in completeStates:
        stateComplete.append(item)
    stateComplete.sort()

    return (instructions, stateComplete, sequence)

#Now that we have the pre reqs broken out, we need to create a list
# of states that are ready to complete, and sort alphabetically.
stateComplete = []
sequence = []

#Initial states that are ready to complete.
for item in allChars:
    if item not in instructions:
        stateComplete.append(item)

#Sort initial states.
stateComplete.sort()

while (len(stateComplete)):
    (instructions, stateComplete, sequence) = advanceState(instructions, stateComplete, sequence)

print(len(sequence))

seq = ''

for item in sequence:
    seq += item

print(seq)



