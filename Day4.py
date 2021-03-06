#%%
from Utils import Input, printHelper, re
import numpy as np

def Parse1(text):
    current_Guard = 0
    days = []
    for line in text:
        tempGuardId = re.findall(r"Guard #(\d+) begins shift", line)
        if tempGuardId:
            current_Guard = tempGuardId[0]
            continue
        # If we are here the guard is either falling asleep or waking up.
        asleep = 1
        if re.search(r'falls asleep', line) is not None:
            asleep = 1
        else:
            asleep = 0
        (date) = re.findall(r'(\d+-\d+-\d+) (\d+)\:(\d+)', line)
        days.append((date[0][0], current_Guard, asleep, int(date[0][1]), int(date[0][2])))

    return days

def Parse2(sleepSchedule):
    #sleeping = []
    isSleeping = False
    currentDay = ''
    startedSleeping = 0
    shift =  {}
    #Now that we have all our days... lets get the time sleeping.
    for item in sleepSchedule:
        # Lets initialize a shift for each guard.
        if item[1] not in shift:
            shift[item[1]] = [0] * 60
        # Also lets set our loop vars.
        if item[0] != currentDay:
            isSleeping = False
            currentDay = item[0]
            startedSleeping = 0
        # Case to handle falling asleep.
        if isSleeping == False and item[2] == 1:
            isSleeping = True
            startedSleeping = item[4]
        # Woke up, lets count minutes.
        if isSleeping == True and item[2] == 0:
            isSleeping = False
            #Transitioned from sleep to awake.
            for x in range (startedSleeping, item[4]):
                shift[item[1]][x] += 1

    return shift

# First, ran the sort command from command line.
# "sort Day4.txt -o Day4sort.txt"
days = Parse1(Input(4).readlines())
sleeping = Parse2(days)

mostSleepyMin = 0
guardSleepyMins = 0
guardthatSleepsAlot = 0
# Now we need to count each guard to get the max size.
#guardSleepyMins = max(sleeping.values(), key=sum)

for k,v in sleeping.items():
    locCount = sum(v)
    if locCount > guardSleepyMins:
        guardthatSleepsAlot = k
        guardSleepyMins = locCount

#Now that we have the guard who is alseep the most... lets find his 
# sleepy minute.
max_value = max(sleeping[guardthatSleepsAlot])
max_index = sleeping[guardthatSleepsAlot].index(max_value)

print ('Guard: {} - Most Min: {}'.format(guardthatSleepsAlot, max_index))
ans = int(max_index) * int(guardthatSleepsAlot)

print('Dat4a: {}'.format(ans))

#Now get the minute that a guard is asleep the most.
maxMin = 0
maxGuardMin = 0
for k,v in sleeping.items():
    locMax = max(v)
    if locMax > maxMin:
        maxGuardMin = k
        maxMin = locMax

#Now that we have the guard who is alseep the most... lets find his 
# sleepy minute.
max_index = sleeping[maxGuardMin].index(maxMin)

print ('Guard2: {} - Most Min2: {}'.format(maxGuardMin, max_index))
ans2 = int(max_index) * int(maxGuardMin)

print('Dat4b: {}'.format(ans2))
