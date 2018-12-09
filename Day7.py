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
        if not v:
            finishedStates.append(k)
            #Remove this key in the dict.
            keysToRemove.append(k)

    for item in keysToRemove:
        del instructions[item]

    return (finishedStates, instructions)

def advanceState(instructions, stateComplete, sequence):
    state = stateComplete[0]
    stateComplete.remove(state)
    sequence.append(state)
    (completeStates, instructions) = updateState(state, instructions)

    for item in completeStates:
        stateComplete.append(item)
    stateComplete.sort()

    return (instructions, stateComplete, sequence)

(instructions, allChars) = Parse(Input(7).readlines())

#Now that we have the pre reqs broken out, we need to create a list
# of states that are ready to complete, and sort alphabetically.
stateComplete = []
sequence = []

''' Get how much time this step takes'''
def getTimeforState(char):
    return 61 + ord(char) - ord('A')

#Initial states that are ready to complete.
for item in allChars:
    if item not in instructions:
        stateComplete.append(item)

#Sort initial states.
stateComplete.sort()

while (len(stateComplete)):
    (instructions, stateComplete, sequence) = advanceState(instructions, stateComplete, sequence)

seq = ''

for item in sequence:
    seq += item

print('Day7a: {}'.format(seq))

def assignWorker(state, activeWorkers, totalTime, stateComplete, sequence):
    stateComplete.remove(state)
    sequence.append([state, totalTime + getTimeforState(state)])
    activeWorkers += 1
    return (stateComplete, sequence, activeWorkers)

def updateTimeByWorkerwithLeastTimeLeft(totalTime, sequence):
    minTime = 0
    for item in sequence:
        tempTime = item[1] - totalTime
        if (tempTime > 0):
            if (minTime == 0):
                minTime = tempTime
            elif (tempTime < minTime):
                minTime = tempTime
    totalTime += minTime
    return totalTime

def checkForWorkerComplete(sequence, totalTime):
    stateJustFinished = []
    for item in sequence:
        if item[1] == totalTime:
            stateJustFinished.append(item[0])
    
    return stateJustFinished


def advanceState2(instructions, stateComplete, sequence, totalTime, activeWorkers):
    sjf = checkForWorkerComplete(sequence, totalTime)
    for item in sjf:
        if not item in stateComplete:
            if item not in masterCompleted:
                activeWorkers -= 1
                masterCompleted.add(item)
            (completeStates, instructions) = updateState(item, instructions)
            for item in completeStates:
                stateComplete.append(item)
            stateComplete.sort()
    # We can assign a new worker, so lets do that now.
    if (activeWorkers < 5):
        # We can assign someone to work it.
        if stateComplete:
            (stateComplete, sequence, activeWorkers) = assignWorker(stateComplete[0], activeWorkers, totalTime, stateComplete, sequence)
        # No more states to work, need to update totalTime
        else:
            totalTime = updateTimeByWorkerwithLeastTimeLeft(totalTime, sequence)
    # We can't assign another worker, need to update totaltime.
    else:
        totalTime = updateTimeByWorkerwithLeastTimeLeft(totalTime, sequence)

    return (instructions, stateComplete, sequence, totalTime, activeWorkers)

stateComplete2 = []
sequence2 = []
masterCompleted = set()
totalTime = 0
activeWorkers = 0
(instructions2, allChars2) = Parse(Input(7).readlines())
#Initial states that are ready to complete.
for item in allChars2:
    if item not in instructions2:
        stateComplete2.append(item)

while (len(sequence2) < 26):
    (instructions2, stateComplete2, sequence2, totalTime, activeWorkers) = advanceState2(instructions2, stateComplete2, sequence2, totalTime, activeWorkers)

print('Day7b: {}'.format(totalTime + getTimeforState('Q')))