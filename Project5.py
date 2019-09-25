import sys
import numpy as np
from typing import NamedTuple

def backtrack(variable, value, limits, unary_inclusive, unary_exclusive, binary_equal, binary_not_equals, binary_simultaneous):
# if complete, return bags
# Select the MRV variable to fill
# Fill in a value and solve further (recursively),
# backtracking an assignment when stuck


class Variable(NamedTuple):
    item: chr
    weight: int

class Value(NamedTuple):
    bag: chr
    capacity: int

class Limits(NamedTuple):
    lowerBound: int
    upperBound: int

# class UnaryInclusive(NamedTuple):
#     item: chr
#     bags: chr
#
# class UnaryExclusive(NamedTuple):
#     item: chr
#     bags: []
#
# class BinaryEqual(NamedTuple):
#     items: []
#
# class BinaryNotEquals(NamedTuple):
#     items: []
#
# class BinarySimultaneous(NamedTuple):
#     items: []
#     bags: []

if len(sys.argv) != 2:
    sys.exit("Must specify input file")
inputFile = sys.argv[1]

variables = []
values = []
limits = []
inclusives = []
exclusives = []
equals = []
notEquals = []
simultaneous = []

category = 0
counter = 0
inputData = np.loadtxt(inputFile, delimiter=' ', dtype='str')
file = open(inputFile, "r")
for line in file:
    line = line.strip()
    if line[0] == '#':
        category += 1
    else:
        if category == 1:
            weight = int(inputData[counter][1])
            variables.append(Variable(inputData[counter][0], weight))
        elif category == 2:
            capacity = int(inputData[counter][1])
            values.append(Value(inputData[counter][0], capacity))
        elif category == 3:
            lowerBound = int(inputData[counter][0])
            upperBound = int(inputData[counter][1])
            limits.append(Limits(lowerBound, upperBound))
        # elif category == 4:
        #     for category in inputData[counter]:
        # elif category == 5:
        #     for category in inputData[counter]:
        # elif category == 6:
        #     for category in inputData[counter]:
        # elif category == 7:
        #     for category in inputData[counter]:
        # else:
        #     for category in inputData[counter]:
        counter += 1
print(variables)
print(values)
print(limits)