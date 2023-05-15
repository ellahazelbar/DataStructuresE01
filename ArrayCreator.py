import random

def CreateArray(experimentID, i):
    n = 1500 * (2**i)
    if (experimentID == 0):
        return [n-j for j in range(n)]
    if (experimentID == 1):
        res = [j + 1 for j in range(n)]
        random.shuffle(res)
        return res
    else:
        res = []
        for blockId in range(5 * (2**i)):
            for j in range(300):
                res.append(300 * (blockId + 1) - j)
        return res
        