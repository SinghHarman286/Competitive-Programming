# ------------------------------------------------Warning-----------------------------------------------------
# if the comment is not deleted it means that the solution below does not work

def orangesRotting(grid):
    timeElapsed = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            turned = False
            if(grid[i][j] == 2):
                timeElapsed = helper(grid, i, j, turned, timeElapsed)
            else:
                continue

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return timeElapsed

def helper(grid, i, j, turned, timeElapsed):
    if i-1 >= 0 and grid[i-1][j] == 1:
        turned = True
        grid[i-1][j] = 2
    if i+1 < len(grid) and grid[i+1][j] == 1:
        turned = True
        grid[i+1][j] = 2
    if j-1 >= 0 and grid[i][j-1] == 1:
        turned = True
        grid[i][j-1] = 2
    if j+1 < len(grid[i]) and grid[i][j+1] == 1:
        turned = True
        grid[i][j+1] = 2
    if turned:
        timeElapsed += 1
    
    return timeElapsed

print(orangesRotting([[0,2]]))
