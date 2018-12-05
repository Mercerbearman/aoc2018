
#https://adventofcode.com/2018/day/3

#%%
from Utils import Input, printHelper, re
import numpy as np
from collections import Counter
import time

def Parse(text):
    "Return a list of elf patch coords."
    "text will be #1 @ 1,3: 4x4"
    return [(int(id), int(rowOff), int(colOff), int(rowCount), int(colCount))
           for (id, rowOff, colOff, rowCount, colCount)
                in re.findall(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', text)]

def createGrid(patchList, row, col):
    cgStart = time.perf_counter()
    grid = [[0 for x in range(col)] for y in range(row)] 
    ids = set()
    overlappedElves = set()
    for elf in patchList:
        for rowRange in range(elf[1], elf[1] + elf[3]):
            for colRange in range(elf[2], elf[2] + elf[4]):
                data = grid[rowRange][colRange]
                if  data == 0:
                    grid[rowRange][colRange] = elf[0]
                    ids.add(elf[0])
                else:
                    #We have a conflict, handle it.
                    overlappedElves.add(data)
                    overlappedElves.add(elf[0])
                    grid[rowRange][colRange] = -1
    cgend = time.perf_counter()
    print('Time for create grid is: {}'.format(cgend - cgStart))
    return (grid, ids, overlappedElves)

def createGrid2(patchList):


start = time.perf_counter()

patchList = Parse(Input(3).read())

# Lets find the size of the matrix.
patchProfile = []
for elf in patchList:
    patchProfile.append((elf[0], elf[1] + elf[3], elf[2] + elf[4]))

# Helpful way to find the max of the list of tuples (per column)
maxRow = max(patchProfile, key=lambda item:item[1])
maxCol = max(patchProfile, key=lambda item:item[2])

(grid, elfIds, overlappedElfs) = createGrid(patchList, maxRow[1], maxCol[2])

# THere has to be a better way here.  find all -1 values in my matrix (multiple assigned)
count = 0
for item in grid:
    count += item.count(-1)

#Grab the only id that isn't overlapped, aka difference between the two lists.
ans = elfIds.difference(overlappedElfs)

end = time.perf_counter()

print('Dat3a: {}'.format(count))
print('Day3b: {}'.format(ans))
print('Day3 Time: {} seconds'.format(end - start))