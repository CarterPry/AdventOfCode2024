#Day02
#Part02


safeCount = 0
unsafeCount = 0

with open('input.txt', 'r') as file:
    for line in file:
        isItSafe = [int(x) for x in line.strip().split()]
        safe = True
        secondChance = True
        whichDirection = 0 
        for i in range(len(isItSafe) - 1): 
            difference = abs(isItSafe[i] - isItSafe[i+1])
            if difference < 1 or difference > 3:  
                if secondChance == True:
                    secondChance = False
                else:
                    safe = False
                    break
            if isItSafe[i+1] > isItSafe[i]:  
                if whichDirection == -1:  
                    if secondChance == True:
                        secondChance = False
                    else:
                        safe = False
                        break
                whichDirection = 1
            elif isItSafe[i+1] < isItSafe[i]: 
                if whichDirection == 1: 
                    if secondChance == True:
                        secondChance = False
                    else:
                        safe = False
                        break
                whichDirection = -1
        if safe:
            safeCount += 1
        else:
            unsafeCount += 1
    print(safeCount, "reports are safe")