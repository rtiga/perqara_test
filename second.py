def queen(boardSize, rowQueen, columnQueen, obstacles):
    if boardSize == 0:
        return 0

    obstacleSet = set([tuple(item) for item in obstacles])

    if (rowQueen, columnQueen) in obstacleSet:
        return 0

        #      up       down    right    left   upRight  downLeft   upLeft  downRight
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    count = 0

    for vertical, horizontal in directions:

        currentPosition = (rowQueen + vertical, columnQueen + horizontal)

        while 1 <= currentPosition[0] <= boardSize and 1 <= currentPosition[
            1] <= boardSize and currentPosition not in obstacleSet:
            currentPosition = (currentPosition[0] + vertical, currentPosition[1] + horizontal)
            count += 1

    return count


boardSize = 4

rowQueen, columnQueen = 4, 4

obstacles = [2, 2], [1, 1]

answer = queen(boardSize, rowQueen, columnQueen, obstacles)

print(answer)
