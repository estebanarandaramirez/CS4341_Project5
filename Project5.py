import sys
import numpy as np
from typing import NamedTuple

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
    bags: []

class UnaryExclusive(NamedTuple):
    item: chr
    bags: []

class BinaryEqual(NamedTuple):
    items: []

class BinaryNotEquals(NamedTuple):
    items: []

class BinarySimultaneous(NamedTuple):
    items: []
    bags: []

if len(sys.argv) != 2:
    sys.exit("Must specify input and output files")
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
file = open(inputFile, "r")
for line in file:
    line = line.strip()
    if line[0] != '#':
        category += 1
        print(line)
    else:
        if category == 0:
            iterateLine
        elif category == 1:
        elif category == 2:
        elif category == 3:
        elif category == 4:
        elif category == 5:
        elif category == 6:
        else: