import sys
import numpy as np
from typing import NamedTuple

class OutputBag(NamedTuple):
    bag: chr
    items: str
    numItems: int
    totalCapacity: int
    usedCapacity: int
    wastedCapacity: int

class Variable(NamedTuple):
    item: chr
    weight: int

class Value(NamedTuple):
    bag: chr
    capacity: int

class Limits(NamedTuple):
    lowerBound: int
    upperBound: int

class UnaryInclusive(NamedTuple):
    item: chr
    bags: str

class UnaryExclusive(NamedTuple):
    item: chr
    bags: str

class BinaryEqual(NamedTuple):
    items: str

class BinaryNotEquals(NamedTuple):
    items: str

class BinarySimultaneous(NamedTuple):
    items: str
    bags: str

def printOutput(outputs):
    for output in outputs:
        print(output.bag, end=' ')
        for item in output.items:
            print(item, end=' ')
        print()
        print("number of items: %i" % output.numItems)
        print("total weight: %i/%i" % (output.usedCapacity, output.totalCapacity))
        print("wasted capacity: %i" % output.wastedCapacity)
        print()

if len(sys.argv) != 2:
    sys.exit("Must specify input file")
inputFile = sys.argv[1]
data = np.loadtxt(inputFile, delimiter='\n', dtype='str')
inputData = []
for element in data:
    element = element.split()
    inputData.append(element)

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
        elif category == 4:
            bags = []
            for i in range(len(inputData[counter])):
                if i == 0:
                    item = inputData[counter][i]
                else:
                    bags.append(inputData[counter][i])
            inclusives.append(UnaryInclusive(item, bags))
        elif category == 5:
            bags = []
            for i in range(len(inputData[counter])):
                if i == 0:
                    item = inputData[counter][i]
                else:
                    bags.append(inputData[counter][i])
            exclusives.append(UnaryExclusive(item, bags))
        elif category == 6:
            items = []
            for i in range(len(inputData[counter])):
                items.append(inputData[counter][i])
            equals.append(BinaryEqual(items))
        elif category == 7:
            items = []
            for i in range(len(inputData[counter])):
                items.append(inputData[counter][i])
            notEquals.append(BinaryNotEquals(items))
        else:
            items = []
            bags = []
            for i in range(len(inputData[counter])):
                if ord(inputData[counter][i]) < 97:
                    items.append(inputData[counter][i])
                else:
                    bags.append(inputData[counter][i])
            simultaneous.append(BinarySimultaneous(items, bags))
        counter += 1

# print(variables)
# print(values)
# print(limits)
# print(inclusives)
# print(exclusives)
# print(equals)
# print(notEquals)
# print(simultaneous)

printOutput([OutputBag('a', ['A','B','C'], 3, 80, 70, 10), OutputBag('b', ['Y','G','L'], 3, 80, 80, 0)])