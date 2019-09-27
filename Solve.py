from typing import NamedTuple

class OutputBag(NamedTuple):
    bag: chr
    items: str
    numItems: int
    totalCapacity: int
    usedCapacity: int
    wastedCapacity: int
    requiredCapacity: int

class ConstraintItems(NamedTuple):
    binarySimultaneousItems: str
    binarySimultaneousBags: str
    binaryNotEquals: str
    unaryExclusive: str
    binaryEquals: str
    unaryInclusive: str

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
    for i in range(len(current)-2):
        sumCurrent += current[i + 1]
    sumNew = 0
    for i in range(len(new)-2):
        sumNew += new[i + 1]

    if sumCurrent >= sumNew:
        return current
    else:
        return new

#Helper for MRVHeusitic, iterates through unary constraints to check if the item has that constraint
def CheckUnaryConstraints(itemName, constraint):
    relatedElements =[]
    for line in constraint:
        if line.item == itemName:
            relatedElements = line.bags
            return 1, relatedElements
    return 0, relatedElements

#Helper for MRVHeusitic, iterates through binary constraints to check if the item has that constraint
def CheckBinaryConstraints(itemName, constraint):
    relatedElements =[]
    counter = 0
    for line in constraint:
        for element in line.items:
            if element == itemName:
                for ele in line.items:
                    if ele != itemName:
                        relatedElements.append(ele)
                counter += 1
    return counter, relatedElements

#Helper for MRVHeusitic, iterates through binary constraints to check if the item has that constraint
def CheckSimultaneousConstraints(itemName, constraint):
    relatedItems = []
    relatedBags = []
    counter = 0
    for line in constraint:
        for element in line.items:
            if element == itemName:
                for ele in line.items:
                    if ele != itemName:
                        relatedItems.append(ele)
                for ele in line.bags:
                    relatedBags.append(ele)
                counter += 1
    return counter, relatedItems, relatedBags

#Returns the item with the highest heuristic value based on its weighted constraints
def MRVHeusitic(items, inclusives, exclusives, equals, notEquals, simultaneous):
    heuristics = []
    for item in items:
        itemHeuristic = []
        itemHeuristic.append(item)
        #Check constraints in ascending order of importance
        count, binarySimultaneousItems, binarySimultaneousBags = CheckSimultaneousConstraints(item, simultaneous)
        itemHeuristic.append(count)
        count, binaryNotEquals = CheckBinaryConstraints(item, notEquals)
        itemHeuristic.append(count)
        count, unaryExclusive = CheckUnaryConstraints(item, exclusives)
        itemHeuristic.append(count)
        count, binaryEquals = CheckBinaryConstraints(item, equals)
        itemHeuristic.append(count)
        count, unaryInclusive = CheckUnaryConstraints(item, inclusives)
        itemHeuristic.append(count)
        #Sum the weighted number of constraints an item has
        sum = 0
        for i in range(len(itemHeuristic)-1):
            sum += itemHeuristic[i+1] * (i+1)
        itemHeuristic.append(sum)
        itemHeuristic.append(ConstraintItems(binarySimultaneousItems, binarySimultaneousBags, binaryNotEquals, unaryExclusive, binaryEquals, unaryInclusive))
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
    return maxHeuristicItem

#NOT FINISHED
def ForwardChecking(itemToExpand, variables, outputs, limits):
    possibleBags = []
    constraints = itemToExpand[7]
    weight = 0
    variable = 0
    for item in variables:
        if item.item == itemToExpand[0]:
            weight = item.weight
            variable = item

    for bag in constraints.unaryInclusive:
        for outputBag in outputs:
            if outputBag.bag == bag:
                if outputBag.wastedCapacity >= weight:
                    possibleBags.append(bag)
                    for item in outputBag.items:
                        for element in constraints.binaryNotEquals:
                            if item == element:
                                possibleBags.remove(bag)
                                break
                        return bag, variable
    for outputBag in outputs:
        if outputBag.wastedCapacity >= weight:
            possibleBags.append(outputBag.bag)
    for bag in possibleBags:
        for outputBag in outputs:
            if outputBag.bag == bag:
                if outputBag.usedCapacity < outputBag.requiredCapacity:
                    return bag, variable

#Put item in output bag
def putInBag(outputs, bag, item):
    for outputBag in outputs:
        if outputBag.bag == bag:
            outputBag.items.append(item.item)
            l = list(outputBag)
            l[2] = outputBag.numItems + 1
            l[4] = outputBag.usedCapacity + item.weight
            l[5] = outputBag.wastedCapacity - item.weight
            newOutputBag = OutputBag(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
            outputs.remove(outputBag)
            outputs.append(newOutputBag)

items = []
bags = []
outputs = []

def CSP(variables, values, limits, inclusives, exclusives, equals, notEquals, simultaneous):
    for bag in values:
        bags.append(bag.bag)
        outputs.append(OutputBag(bag.bag, [], 0, bag.capacity, 0, bag.capacity, round(0.9*bag.capacity)))
    for item in variables:
        items.append(item.item)
    for i in range(len(variables)):
        itemToExpand = MRVHeusitic(items, inclusives, exclusives, equals, notEquals, simultaneous)
        items.remove(itemToExpand[0])
        bag, item = ForwardChecking(itemToExpand, variables, outputs, limits)
        putInBag(outputs, bag, item)
    printOutput(outputs)

def LeastConstrainingHeuristic():
    return

def Backtracking():
    return