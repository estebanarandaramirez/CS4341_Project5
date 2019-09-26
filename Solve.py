from typing import NamedTuple

class OutputBag(NamedTuple):
    bag: chr
    items: str
    numItems: int
    totalCapacity: int
    usedCapacity: int
    wastedCapacity: int

def printOutput(outputs):
    if len(outputs) == 0:
        print('No such assignment is possible')
    else:
        for output in outputs:
            print(output.bag, end=' ')
            for item in output.items:
                print(item, end=' ')
            print()
            print('number of items: %i' % output.numItems)
            print('total weight: %i/%i' % (output.usedCapacity, output.totalCapacity))
            print('wasted capacity: %i' % output.wastedCapacity)
            print()

#Breaks ties when two items have the same MRVHeusitic based on the total number of constraints each item has
def DegreeHeuristic(current, new):
    sumCurrent = 0
    for i in range(len(current)-1):
        sumCurrent += current[i + 1]
    sumNew = 0
    for i in range(len(new)-1):
        sumNew += new[i + 1]

    if sumCurrent >= sumNew:
        return current
    else:
        return new

#Helper for MRVHeusitic, iterates through unary constraints to check if the item has that constraint
def CheckUnaryConstraints(itemName, constraint):
    for line in constraint:
        if line.item == itemName:
            return 1
    return 0

#Helper for MRVHeusitic, iterates through binary constraints to check if the item has that constraint
def CheckBinaryConstraints(itemName, constraint):
    counter = 0
    for line in constraint:
        for element in line.items:
            if element == itemName:
                counter += 1
    return counter

#Returns the item with the highest heuristic value based on its weighted constraints
def MRVHeusitic(variables, inclusives, exclusives, equals, notEquals, simultaneous):
    heuristics = []
    for item in variables:
        itemHeuristic = []
        itemName = item.item
        itemHeuristic.append(itemName)
        #Check constraints in ascending order of importance
        itemHeuristic.append(CheckBinaryConstraints(itemName, simultaneous))
        itemHeuristic.append(CheckBinaryConstraints(itemName, notEquals))
        itemHeuristic.append(CheckUnaryConstraints(itemName, exclusives))
        itemHeuristic.append(CheckBinaryConstraints(itemName, equals))
        itemHeuristic.append(CheckUnaryConstraints(itemName, inclusives))
        #Sum the weighted number of constraints an item has
        sum = 0
        for i in range(len(itemHeuristic)-1):
            sum += itemHeuristic[i+1] * (i+1)
        itemHeuristic.append(sum)
        #Add to the list
        heuristics.append(itemHeuristic)
    #Decide item with max heuristic and break ties if any
    max = -1
    maxHeuristicItem = ''
    for itemHeuristic in heuristics:
        if itemHeuristic[6] == max:
            maxHeuristicItem = DegreeHeuristic(maxHeuristicItem, itemHeuristic)
        elif itemHeuristic[6] > max:
            max = itemHeuristic[6]
            maxHeuristicItem = itemHeuristic
    #Return item with highest heuristic
    return maxHeuristicItem[0]

bags = []
outputs = []

def CSP(variables, values, limits, inclusives, exclusives, equals, notEquals, simultaneous):
    for bag in values:
        bags.append(bag.bag)
        outputs.append(OutputBag(bag.bag, [], 0, bag.capacity, 0, bag.capacity))
    MRVHeusitic(variables, inclusives, exclusives, equals, notEquals, simultaneous)


def LeastConstrainingHeuristic():
    return

def ForwardChecking():
    return

def Backtracking():
    return