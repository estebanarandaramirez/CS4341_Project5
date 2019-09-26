from Project5 import OutputBag

def CSP(variables, values, limits, inclusives, exclusives, equals, notEquals, simultaneous):
    outputs = []
    for bag in values:
        outputs.append(OutputBag(bag.bag, [], 0, bag.weight, 0, bag.weight))
    return outputs