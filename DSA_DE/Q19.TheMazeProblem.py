def count_path(grid,i,j):

    if i < 0 or j<0:
        return 0

    if grid[i][j] == 1:
        return 0
    if i == 0 and j == 0:
        return 1
    return count_path(grid , i-1 , j)+count_path(grid,i,j-1)

grid = [[0 , 0 , 1],
[0 , 0 , 0],
[1, 0 , 0]]

print(count_path(grid,2,2))