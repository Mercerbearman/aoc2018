# This file will contain some helper classes/functions.

import re
import numpy as np
import math

def Input(day):
    "Open this day's input file."
    filename = 'Inputs/Day{}.txt'.format(day)
    try:
        return open(filename)
    except FileNotFoundError:
        print('Could not find file: {filename}')

def printHelper(data, heading):
    print(heading.format(str(data)))
