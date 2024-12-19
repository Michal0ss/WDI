numQueens = 8
currentSolution = [0 for x in range(numQueens)]
solutions = []

def isSafe(testRow, testCol):
    if testRow == 0:
        return True

    for row in range(0,testRow):
        if testCol == currentSolution[row]:
            return False

        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    # nie znaleziono ataku
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row,col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                solutions.append(currentSolution)
            else:
                placeQueen(row+1)
placeQueen(0)

print(len(solutions), "solutions found")
for solution in solutions:
    print(solution)