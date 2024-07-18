image = [[1,1,1],[1,1,0],[1,0,1]]
sr= 1
sc= 1
color = 2

def floodFill(image, sr, sc, color):
    # Get the starting color to replace
    start_color = image[sr][sc]
    
    # Define a nested function for depth-first search (DFS) to fill adjacent pixels
    def fill(x, y):
        # Check for out-of-bounds conditions
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
            return
        
        # If the current pixel is already the target color or not the start color, return
        if image[x][y] == color or image[x][y] != start_color:
            return
        
        # Change the color of the current pixel to the target color
        image[x][y] = color
        
        # Define the four possible directions for movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Recursively apply the fill function to adjacent pixels
        for dr, dc in directions:
            fill(x + dr, y + dc)
    
    # Start the fill operation from the starting pixel
    fill(sr, sc)
    
    # Return the modified image
    return image
