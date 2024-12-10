#Day01
#Part01


leftSide = []
rightSide = []
total = 0

    # Read the file
with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        leftSide.append(left)
        rightSide.append(right)
            
    leftSide.sort()
    rightSide.sort()
        
    for i in range(len(leftSide)):
        total += abs(leftSide[i] - rightSide[i])
            
    print("Total Distance =", total) 
        