def isSafe(maze, i, j, visited, N):
    return (0 <= i < N and 0 <= j < N and not visited[i][j] and maze[i][j] == 1)

def solveAllPaths(maze, i, j, N, visited, current_path, all_paths):  
    # If we reach the destination (bottom-right corner)
    if i == N - 1 and j == N - 1:
        all_paths.append(current_path[:])  # Append the current path to the list of all paths
        return
    
    # Mark current cell as visited
    visited[i][j] = True

    # Move down
    if isSafe(maze, i + 1, j, visited, N):
        current_path.append("D")  # 'D' for down
        solveAllPaths(maze, i + 1, j, N, visited, current_path, all_paths)
        current_path.pop()  # Backtrack

    # Move right
    if isSafe(maze, i, j + 1, visited, N):
        current_path.append("R")  # 'R' for right
        solveAllPaths(maze, i, j + 1, N, visited, current_path, all_paths)
        current_path.pop()  # Backtrack

    # Move up
    if isSafe(maze, i - 1, j, visited, N):
        current_path.append("U")  # 'U' for up
        solveAllPaths(maze, i - 1, j, N, visited, current_path, all_paths)
        current_path.pop()  # Backtrack

    # Move left
    if isSafe(maze, i, j - 1, visited, N):
        current_path.append("L")  # 'L' for left
        solveAllPaths(maze, i, j - 1, N, visited, current_path, all_paths)
        current_path.pop()  # Backtrack

    # Unmark current cell as visited for backtracking
    visited[i][j] = False

# Test maze
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

N = len(maze)
visited = [[False] * N for _ in range(N)]
all_paths = []

solveAllPaths(maze, 0, 0, N, visited, [], all_paths)

print("All paths:", all_paths)
