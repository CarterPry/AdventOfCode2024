#Day01
#Part02


leftSide = []
rightSide = []
total = 0
similarityScore = []

    # Read the file
with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        leftSide.append(left)
        rightSide.append(right)        
    leftSide.sort()
    rightSide.sort()
        
    for i in range(len(leftSide)):
        counter = 0
        for j in range(len(rightSide)):
            if (leftSide[i] == rightSide[j]):
                counter += 1
        total += leftSide[i] * counter 
            
    print("Total Smilarity Score =", total) 
        