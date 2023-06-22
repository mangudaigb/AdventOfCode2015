
# with open('day3-test', 'r') as file:
# with open('day3-test', 'r') as file:
with open('day3-input', 'r') as file:
    dictSanta = {}
    dictRobo = {}
    input = file.read().strip()
    sx, sy = (0, 0)
    rx, ry = (0, 0)
    dictSanta[(sx,sy)] = 1
    dictRobo[(rx,ry)] = 1
    for i,c in enumerate(input):
        if i % 2 == 0:
            if c == '>':
                sx += 1
            if c == '<':
                sx -= 1
            if c == '^':
                sy += 1
            if c == 'v':
                sy -= 1
            dictSanta[(sx,sy)] = dictSanta.get((sx,sy), 0) + 1
        else:
            if c == '>':
                rx += 1
            if c == '<':
                rx -= 1
            if c == '^':
                ry += 1
            if c == 'v':
                ry -= 1
            dictRobo[(rx,ry)] = dictRobo.get((rx,ry), 0) + 1
    dups = 0
    skeys = set(dictSanta.keys())
    rkeys = set(dictRobo.keys())
    keys = list(skeys.union(rkeys))
    for key in keys:
        if dictSanta.get(key, 0) + dictRobo.get(key, 0) >= 1:
            dups += 1
    print("More: " + str(dups))
