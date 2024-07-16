grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
output = 1

def numIslands(grid):
    # If the grid is empty, return 0 as there are no islands
    if not grid:
        return 0

    # Helper function to perform Depth First Search (DFS) to mark the visited land
    def depth_first_search(grid, row, col):
        # Check if the current position is out of bounds or is water ('0')
        if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] == "0":
            return
        # Mark the current land ('1') as visited by setting it to '0'
        grid[row][col] = "0"

        # Directions for moving up, down, left, and right
        # for diagonals, directions for moving up, down, left, right, and all four diagonals will be:
        # directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Recursively visit all connected lands (4-directionally)
        for dr, dc in directions:
            depth_first_search(grid, row + dr, col + dc)

    # Get the number of rows and columns in the grid
    row_len, col_len = len(grid), len(grid[0])
    islands = 0  # Initialize the count of islands to 0

    # Iterate through each cell in the grid
    for row in range(row_len):
        for col in range(col_len):
            # If a cell is land ('1'), it is the start of a new island
            if grid[row][col] == "1":
                islands += 1  # Increment the island count
                # Perform DFS to mark all connected land as visited
                depth_first_search(grid, row, col)
                
    return islands  # Return the total number of islands found
